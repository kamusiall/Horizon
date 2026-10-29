"""Twitter scraper using Playwright + Cookie (replaces Apify)."""

import asyncio
import glob
import hashlib
import argparse
import json
import logging
import os
import random
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional
from urllib.parse import urlsplit

from ..models import ContentItem, SourceType, TwitterConfig
from .base import BaseScraper

logger = logging.getLogger(__name__)

# Optional Playwright imports — gracefully degraded if not installed
try:
    from playwright.async_api import async_playwright
    from playwright_stealth import Stealth

    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False
    Stealth = None  # type: ignore[misc,assignment]


def _get_proxy() -> str:
    """Resolve proxy from common env vars (PROXY, http_proxy, all_proxy)."""
    for key in ("PROXY", "https_proxy", "http_proxy", "all_proxy"):
        val = os.getenv(key, "").strip()
        if val:
            return val
    return ""


PROXY = _get_proxy()


def _load_browser_cookies(file_path: str) -> list[dict]:
    """Read browser-exported cookie JSON and convert to Playwright format."""
    if not Path(file_path).exists():
        return []
    with open(file_path, encoding="utf-8") as f:
        cookies = json.load(f)
    pw_cookies = []
    for c in cookies:
        pc: dict = {
            "name": c["name"],
            "value": c["value"],
            "domain": c["domain"],
            "path": c.get("path", "/"),
            "secure": c.get("secure", True),
            "httpOnly": c.get("httpOnly", False),
        }
        if c.get("expirationDate"):
            pc["expires"] = c["expirationDate"]
        pw_cookies.append(pc)
    return pw_cookies


_STATUS_HOSTS = {"x.com", "www.x.com", "mobile.x.com", "twitter.com", "www.twitter.com", "mobile.twitter.com"}
_USERNAME_RE = re.compile(r"[A-Za-z0-9_]{1,15}")
_TWEET_ID_RE = re.compile(r"[0-9]{1,25}")
_LOGIN_GATE_MARKERS = ("log in", "sign up", "create account")
_UNAVAILABLE_MARKERS = (
    "post is unavailable",
    "tweet is unavailable",
    "page doesn’t exist",
    "page doesn't exist",
    "posts are protected",
    "post was deleted",
    "account that no longer exists",
)


def parse_status_url(url: str) -> tuple[str, str]:
    """Return (username, tweet_id) for an X/Twitter post URL; raise ValueError otherwise."""
    try:
        parts = urlsplit(str(url).strip())
        host = (parts.hostname or "").lower()
        has_userinfo = "@" in parts.netloc
    except ValueError as exc:
        raise ValueError("Not a valid URL") from exc
    if parts.scheme not in ("http", "https"):
        raise ValueError("Status URL must use http(s)")
    if has_userinfo:
        raise ValueError("Status URL must not contain credentials")
    if host not in _STATUS_HOSTS:
        raise ValueError("Status URL must be on x.com or twitter.com")
    segments = [seg for seg in parts.path.split("/") if seg]
    if (
        len(segments) < 3
        or segments[1] not in ("status", "statuses")
        or not _USERNAME_RE.fullmatch(segments[0])
        or not _TWEET_ID_RE.fullmatch(segments[2])
    ):
        raise ValueError("Status URL needs the form /<user>/status/<numeric id>")
    return segments[0], segments[2]


async def _block_heavy_resources(route):
    if route.request.resource_type in ("media", "image", "video"):
        await route.abort()
    else:
        url = route.request.url.lower()
        if any(k in url for k in ("google-analytics", "doubleclick", "scribe.twitter.com")):
            await route.abort()
        else:
            await route.continue_()


def _tweet_author(obj: dict) -> str:
    user = obj.get("core", {}).get("user_results", {}).get("result", {})
    if user.get("__typename") == "UserUnavailable":
        return ""
    return user.get("core", {}).get("screen_name") or user.get("legacy", {}).get("screen_name") or ""


def _extract_tweets(obj, out: list[dict]) -> None:
    """Append every GraphQL object that looks like a tweet (rest_id + legacy) to out."""
    if isinstance(obj, dict):
        if obj.get("rest_id") and obj.get("legacy"):
            legacy = obj["legacy"]
            media_entities = (
                legacy.get("extended_entities", {}).get("media", [])
                or legacy.get("entities", {}).get("media", [])
            )
            images = [
                m["media_url_https"]
                for m in media_entities
                if m.get("type") == "photo" and m.get("media_url_https")
            ]
            tweet = {
                "tweet_id": obj["rest_id"],
                "text": legacy.get("full_text", ""),
                "datetime_raw": legacy.get("created_at", ""),
                "is_retweet": (
                    "retweeted_status_result" in obj.get("core", {})
                    or "retweeted_status_id_str" in legacy
                ),
                "images": images,
            }
            try:
                dt = datetime.strptime(tweet["datetime_raw"], "%a %b %d %H:%M:%S %z %Y")
                tweet["datetime"] = dt.isoformat()
            except (ValueError, TypeError):
                tweet["datetime"] = tweet["datetime_raw"]
            # Extra fields read by the status path; _parse_tweet ignores them.
            tweet["username"] = _tweet_author(obj)
            tweet["conversation_id"] = legacy.get("conversation_id_str")
            tweet["in_reply_to"] = legacy.get("in_reply_to_status_id_str")
            tweet["like_count"] = legacy.get("favorite_count")
            tweet["reply_count"] = legacy.get("reply_count")
            quoted = legacy.get("quoted_status_permalink", {})
            tweet["quoted_status_url"] = quoted.get("expanded") if isinstance(quoted, dict) else None
            note = obj.get("note_tweet", {}).get("note_tweet_results", {}).get("result", {})
            tweet["note_text"] = note.get("text") if isinstance(note, dict) else None
            out.append(tweet)
        for v in obj.values():
            _extract_tweets(v, out)
    elif isinstance(obj, list):
        for item in obj:
            _extract_tweets(item, out)


def select_status_thread(tweets: list[dict], tweet_id: str, max_replies: int) -> Optional[list[dict]]:
    """Pick the requested post, its author's thread and up to max_replies replies by others.

    Returns None when the requested post is not among the intercepted tweets.
    Each returned dict carries "kind": "status", "thread" or "reply".
    """
    unique: dict[str, dict] = {}
    for t in tweets:
        tid = str(t.get("tweet_id") or "")
        # User objects also have rest_id + legacy; only tweets have a conversation id.
        if tid and t.get("conversation_id") and tid not in unique:
            unique[tid] = t
    root = unique.get(str(tweet_id))
    if root is None:
        return None
    conversation = root.get("conversation_id") or root["tweet_id"]
    author = (root.get("username") or "").lower()
    selected = [{**root, "kind": "status"}]
    replies = 0
    for tid, t in unique.items():
        if tid == root["tweet_id"] or t.get("conversation_id") != conversation:
            continue
        if author and (t.get("username") or "").lower() == author:
            selected.append({**t, "kind": "thread"})
        elif replies < max_replies:
            selected.append({**t, "kind": "reply"})
            replies += 1
    return selected


class TwitterPlaywrightScraper(BaseScraper):
    """Fetch tweets via Playwright + Cookie using GraphQL interception (free alternative to Apify)."""

    def __init__(self, config: TwitterConfig, http_client=None):
        super().__init__(config.model_dump(), http_client)
        self.twitter_config = config
        # "@user/status/id" labels of status URLs that could not be read in the last fetch()
        self.failed_status_urls: list[str] = []

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self.twitter_config.enabled:
            return []

        users = [u.strip().lstrip("@") for u in self.twitter_config.users if u.strip()]
        self.failed_status_urls = []
        statuses: list[tuple[str, str]] = []
        for raw_url in self.twitter_config.status_urls:
            try:
                statuses.append(parse_status_url(raw_url))
            except ValueError as exc:
                logger.warning("Skipping invalid status URL: %s", exc)
        if not users and not statuses:
            logger.debug("No Twitter users or status URLs configured, skipping.")
            return []

        if not PLAYWRIGHT_AVAILABLE:
            logger.warning(
                "Playwright not installed. Run: uv sync --extra twitter && uv run playwright install chromium"
            )
            return []

        cookie_dir = Path(self.twitter_config.cookie_dir)
        pattern = self.twitter_config.cookie_file_pattern
        cookie_files = sorted(cookie_dir.glob(pattern))
        if not cookie_files:
            logger.warning("No cookie files found matching %s in %s", pattern, cookie_dir)
            return []

        logger.info(
            "Fetching Twitter (Playwright) for %d users and %d status URLs using %d cookie sets",
            len(users),
            len(statuses),
            len(cookie_files),
        )

        all_items: List[ContentItem] = []
        failed_users: list[tuple[str, int]] = []
        lock = asyncio.Lock()

        async with Stealth().use_async(async_playwright()) as p:  # type: ignore[union-attr]
            launch_kwargs: dict = {"headless": True}
            if PROXY:
                launch_kwargs["proxy"] = {"server": PROXY}
            browser = await p.chromium.launch(**launch_kwargs)

            contexts = []
            for i, cf in enumerate(cookie_files):
                cookies = _load_browser_cookies(str(cf))
                ctx = await browser.new_context(
                    user_agent=(
                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                        f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/13{i}.0.0.0 Safari/537.36"
                    ),
                    viewport={"width": 1280, "height": 800},
                    locale="en-US",
                    timezone_id="UTC",
                    color_scheme="dark",
                )
                if cookies:
                    await ctx.add_cookies(cookies)
                contexts.append(ctx)

            # Warm-up each context by visiting x.com/home
            for i, ctx in enumerate(contexts):
                page = await ctx.new_page()
                try:
                    await page.goto("https://x.com/home", wait_until="domcontentloaded", timeout=15000)
                    await asyncio.sleep(2)
                    logger.info("Cookie #%d warm-up done", i + 1)
                except Exception as exc:
                    logger.warning("Cookie #%d warm-up failed: %s", i + 1, exc)
                finally:
                    await page.close()

            num_contexts = len(contexts)

            async def process_queue(context_idx: int, queue: list[str], is_retry: bool = False):
                ctx = contexts[context_idx]
                consecutive_failures = 0

                for username in queue:
                    wait_time = (
                        random.uniform(5.0, 10.0) if not is_retry else random.uniform(10.0, 20.0)
                    )
                    await asyncio.sleep(wait_time)

                    if consecutive_failures >= 5:
                        logger.warning("Context #%d cooling down (30s)", context_idx + 1)
                        await asyncio.sleep(30)
                        consecutive_failures = 0

                    logger.info("Scraping @%s with cookie #%d...", username, context_idx + 1)
                    tweets = await self._scrape_user(ctx, username, since)

                    if tweets is not None:
                        logger.info("  -> @%s: %d tweets found", username, len(tweets))
                        consecutive_failures = 0
                        parsed = [item for item in (self._parse_tweet(t, username) for t in tweets) if item]
                        async with lock:
                            all_items.extend(parsed)
                    else:
                        consecutive_failures += 1
                        if not is_retry:
                            async with lock:
                                failed_users.append((username, context_idx))

            # Round-robin assign users to context queues
            queues: list[list[str]] = [[] for _ in range(num_contexts)]
            for i, username in enumerate(users):
                queues[i % num_contexts].append(username)

            # First pass — all queues in parallel
            await asyncio.gather(*[process_queue(i, q) for i, q in enumerate(queues)])

            # Retry failed users with a different context
            if failed_users:
                logger.info("Retrying %d failed Twitter accounts with alternate cookies", len(failed_users))
                await asyncio.sleep(20)
                retry_queues: list[list[str]] = [[] for _ in range(num_contexts)]
                for username, original_idx in failed_users:
                    new_idx = (original_idx + 1) % num_contexts if num_contexts >= 2 else 0
                    retry_queues[new_idx].append(username)

                await asyncio.gather(*[
                    process_queue(i, q, is_retry=True)
                    for i, q in enumerate(retry_queues)
                    if q
                ])

            async def process_status_queue(context_idx: int, queue: list[tuple[str, str]]):
                ctx = contexts[context_idx]
                for username, tweet_id in queue:
                    await asyncio.sleep(random.uniform(5.0, 10.0))
                    label = f"@{username}/status/{tweet_id}"
                    logger.info("Reading %s with cookie #%d...", label, context_idx + 1)
                    tweets = await self._scrape_status(ctx, f"https://x.com/{username}/status/{tweet_id}")
                    if tweets is None:
                        async with lock:
                            self.failed_status_urls.append(label)
                        continue
                    parsed = [item for item in (self._parse_status_tweet(t, username) for t in tweets) if item]
                    logger.info("  -> %s: %d items", label, len(parsed))
                    async with lock:
                        all_items.extend(parsed)

            if statuses:
                status_queues: list[list[tuple[str, str]]] = [[] for _ in range(num_contexts)]
                for i, status in enumerate(statuses):
                    status_queues[i % num_contexts].append(status)
                await asyncio.gather(*[
                    process_status_queue(i, q) for i, q in enumerate(status_queues) if q
                ])

            for ctx in contexts:
                await ctx.close()
            await browser.close()

        logger.info("Fetched %d tweets via Playwright.", len(all_items))
        return all_items

    async def _scrape_user(self, ctx, username: str, since: datetime) -> Optional[list[dict]]:
        """Scrape a single user's tweets via GraphQL interception."""
        page = await ctx.new_page()
        graphql_tweets: list[dict] = []

        async def handle_response(response):
            if "UserTweets" not in response.url and "UserByScreenName" not in response.url:
                return
            try:
                data = await response.json()
                _extract_tweets(data, graphql_tweets)
            except Exception as exc:
                logger.debug("GraphQL parse error: %s", exc)

        page.on("response", handle_response)

        # Block heavy resources
        await page.route("**/*", _block_heavy_resources)

        try:
            await asyncio.sleep(random.uniform(2, 4))

            for attempt in range(3):
                if attempt > 0:
                    await asyncio.sleep(random.uniform(5, 10))
                try:
                    await page.goto(
                        f"https://x.com/{username}",
                        wait_until="domcontentloaded",
                        timeout=25000,
                    )
                    break
                except Exception as exc:
                    if "Timeout" in str(exc):
                        logger.debug("Page load slow (attempt %d/3)", attempt + 1)
                        if attempt == 2:
                            break
                    else:
                        if attempt == 2:
                            raise
                        logger.debug("Page visit error (attempt %d/3): %s", attempt + 1, exc)

            await asyncio.sleep(5)
            start_time = asyncio.get_event_loop().time()

            # Quick diagnostic: check if page requires login
            body_text = await page.evaluate("document.body ? document.body.innerText : ''")
            if body_text and any(k in body_text.lower() for k in ("log in", "sign up", "create account")):
                logger.warning("  -> @%s page shows login gate — cookie may be invalid", username)

            while (asyncio.get_event_loop().time() - start_time) < 60:
                if graphql_tweets:
                    result = []
                    seen = set()
                    for t in graphql_tweets:
                        uid = t.get("tweet_id") or hashlib.md5(t["text"].encode()).hexdigest()
                        if uid in seen:
                            continue
                        seen.add(uid)
                        try:
                            tweet_time = datetime.fromisoformat(t["datetime"])
                            if tweet_time < since:
                                continue
                        except Exception:
                            continue
                        result.append(t)

                    if result:
                        logger.info("  -> @%s: %d tweets within time window", username, len(result))
                        return result[: self.twitter_config.fetch_limit]
                    logger.info("  -> @%s: intercepted %d tweets but all outside time window", username, len(graphql_tweets))
                    return []

                # Check for error pages
                body_text = await page.evaluate("document.body ? document.body.innerText : ''")
                if body_text and any(
                    kw in body_text
                    for kw in ("Retry", "Something went wrong", "出错了", "重新加载")
                ):
                    await page.reload(wait_until="load", timeout=30000)
                    await asyncio.sleep(5)

                # Simulate human browsing
                await page.mouse.move(random.randint(100, 600), random.randint(100, 600))
                await page.evaluate(f"window.scrollBy(0, {random.randint(300, 700)})")
                await asyncio.sleep(random.uniform(2, 4))

                at_bottom = await page.evaluate(
                    "window.innerHeight + window.scrollY >= document.body.scrollHeight"
                )
                if at_bottom and (asyncio.get_event_loop().time() - start_time) > 20:
                    break

            if not graphql_tweets:
                logger.warning("  -> @%s: no GraphQL data intercepted (cookie or page issue)", username)
                return None
            return []

        except Exception as exc:
            logger.warning("Failed to scrape @%s: %s", username, exc)
            return None
        finally:
            await page.close()

    async def _scrape_status(self, ctx, status_url: str) -> Optional[list[dict]]:
        """Read one post with its thread via TweetDetail interception; None when it cannot be read."""
        try:
            username, tweet_id = parse_status_url(status_url)
        except ValueError as exc:
            logger.warning("Invalid status URL: %s", exc)
            return None
        label = f"@{username}/status/{tweet_id}"
        max_replies = self.twitter_config.status_max_replies
        page = await ctx.new_page()
        graphql_tweets: list[dict] = []

        async def handle_response(response):
            if "TweetDetail" not in response.url and "TweetResultByRestId" not in response.url:
                return
            try:
                _extract_tweets(await response.json(), graphql_tweets)
            except Exception as exc:
                logger.debug("GraphQL parse error: %s", exc)

        page.on("response", handle_response)
        await page.route("**/*", _block_heavy_resources)

        try:
            await asyncio.sleep(random.uniform(2, 4))
            for attempt in range(3):
                if attempt > 0:
                    await asyncio.sleep(random.uniform(5, 10))
                try:
                    await page.goto(
                        f"https://x.com/{username}/status/{tweet_id}",
                        wait_until="domcontentloaded",
                        timeout=25000,
                    )
                    break
                except Exception as exc:
                    if "Timeout" in str(exc):
                        logger.debug("Page load slow (attempt %d/3)", attempt + 1)
                        if attempt == 2:
                            break
                    else:
                        if attempt == 2:
                            raise
                        logger.debug("Page visit error (attempt %d/3): %s", attempt + 1, exc)

            await asyncio.sleep(5)
            start_time = asyncio.get_event_loop().time()
            scrolls_with_root = 0

            # Bounded by polls as well as time; each poll waits 2-4 s.
            for _ in range(20):
                if (asyncio.get_event_loop().time() - start_time) >= 60:
                    break
                selected = select_status_thread(graphql_tweets, tweet_id, max_replies)
                if selected is not None:
                    replies = sum(1 for t in selected if t["kind"] == "reply")
                    if replies >= max_replies or scrolls_with_root >= 3:
                        break
                    scrolls_with_root += 1
                else:
                    if "/login" in page.url or "/i/flow/" in page.url:
                        logger.warning("  -> %s: redirected to login — cookies may be expired", label)
                        return None
                    body_text = await page.evaluate("document.body ? document.body.innerText : ''") or ""
                    lowered = body_text.lower().replace("\u2019", "'")
                    if any(k in lowered for k in _UNAVAILABLE_MARKERS):
                        logger.warning("  -> %s: post deleted, protected or unavailable", label)
                        return None
                    if not graphql_tweets and any(k in lowered for k in _LOGIN_GATE_MARKERS):
                        logger.warning("  -> %s: page shows login gate — cookies may be expired", label)
                        return None
                    if any(kw in body_text for kw in ("Retry", "Something went wrong", "出错了", "重新加载")):
                        await page.reload(wait_until="load", timeout=30000)
                        await asyncio.sleep(5)

                # Scroll to load more of the reply thread
                await page.mouse.move(random.randint(100, 600), random.randint(100, 600))
                await page.evaluate(f"window.scrollBy(0, {random.randint(300, 700)})")
                await asyncio.sleep(random.uniform(2, 4))

            selected = select_status_thread(graphql_tweets, tweet_id, max_replies)
            if selected is not None:
                return selected
            if not graphql_tweets:
                logger.warning("  -> %s: no GraphQL data intercepted (cookie or page issue)", label)
            else:
                logger.warning("  -> %s: requested post not in GraphQL data (deleted or no access)", label)
            return None

        except Exception as exc:
            logger.warning("Failed to read %s: %s", label, exc)
            return None
        finally:
            await page.close()

    def _parse_status_tweet(self, tweet: dict, fallback_username: str) -> Optional[ContentItem]:
        """Convert a tweet from select_status_thread to a ContentItem with thread metadata."""
        username = tweet.get("username") or fallback_username
        item = self._parse_tweet({**tweet, "text": tweet.get("note_text") or tweet.get("text", "")}, username)
        if item is None:
            return None
        item.metadata.update({
            "kind": tweet.get("kind", "status"),
            "conversation_id": tweet.get("conversation_id"),
            "in_reply_to": tweet.get("in_reply_to"),
            "like_count": tweet.get("like_count"),
            "reply_count": tweet.get("reply_count"),
        })
        if tweet.get("quoted_status_url"):
            item.metadata["quoted_status_url"] = tweet["quoted_status_url"]
        return item

    def _parse_tweet(self, tweet: dict, username: str) -> Optional[ContentItem]:
        """Convert raw tweet dict to Horizon ContentItem."""
        try:
            tweet_id = str(tweet.get("tweet_id", ""))
            if not tweet_id:
                return None

            text = tweet.get("text", "")
            if not text:
                return None

            created_at_raw = tweet.get("datetime", "")
            try:
                published_at = datetime.fromisoformat(created_at_raw)
                if published_at.tzinfo is None:
                    published_at = published_at.replace(tzinfo=timezone.utc)
            except (ValueError, TypeError):
                return None

            title_body = text[:50].replace("\n", " ").strip()
            if len(text) > 50:
                title_body += "..."

            return ContentItem(
                id=self._generate_id(SourceType.TWITTER.value, "tweet", tweet_id),
                source_type=SourceType.TWITTER,
                title=f"@{username}: {title_body}",
                url=f"https://x.com/{username}/status/{tweet_id}",
                content=text,
                author=username,
                published_at=published_at,
                metadata={
                    "tweet_id": tweet_id,
                    "is_retweet": tweet.get("is_retweet", False),
                    "images": tweet.get("images", []),
                },
            )
        except Exception as exc:
            logger.debug("Failed to parse tweet: %s", exc)
            return None


def main(argv: Optional[list[str]] = None) -> int:
    """Read one X post with its replies and write {"items": [...]}; no LLM, scoring or notifications.

    Exit codes: 0 success, 1 invalid URL or configuration, 2 the post could not be read.
    """
    parser = argparse.ArgumentParser(
        prog="python -m src.scrapers.twitter_playwright",
        description="Read one X post and its reply thread with exported browser cookies (read-only).",
    )
    parser.add_argument("--status-url", required=True, help="https://x.com/<user>/status/<id>")
    parser.add_argument("--cookie-dir", default="data", help="Directory with x_cookies_*.json (default: data)")
    parser.add_argument("--out", help="Output JSON file (default: stdout)")
    parser.add_argument("--max-replies", type=int, default=TwitterConfig().status_max_replies)
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s", stream=sys.stderr)

    try:
        username, tweet_id = parse_status_url(args.status_url)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    if args.max_replies < 0:
        print("error: --max-replies must be >= 0", file=sys.stderr)
        return 1
    if not PLAYWRIGHT_AVAILABLE:
        print(
            "error: Playwright not installed. Run: uv sync --extra twitter && uv run playwright install chromium",
            file=sys.stderr,
        )
        return 1

    config = TwitterConfig(
        enabled=True,
        mode="playwright",
        users=[],
        status_urls=[f"https://x.com/{username}/status/{tweet_id}"],
        status_max_replies=args.max_replies,
        cookie_dir=args.cookie_dir,
    )
    if not sorted(Path(config.cookie_dir).glob(config.cookie_file_pattern)):
        print(f"error: no {config.cookie_file_pattern} in {config.cookie_dir}", file=sys.stderr)
        return 2

    scraper = TwitterPlaywrightScraper(config)
    items = asyncio.run(scraper.fetch(datetime.now(timezone.utc)))
    if scraper.failed_status_urls or not items:
        print(f"error: could not read @{username}/status/{tweet_id}", file=sys.stderr)
        return 2

    payload = json.dumps({"items": [item.model_dump(mode="json") for item in items]}, ensure_ascii=False, indent=2)
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(payload + "\n", encoding="utf-8")
    else:
        sys.stdout.buffer.write((payload + "\n").encode("utf-8"))
    kinds = {k: sum(1 for i in items if i.metadata.get("kind") == k) for k in ("status", "thread", "reply")}
    print(
        f"ok: {len(items)} items ({kinds['status']} status, {kinds['thread']} thread, {kinds['reply']} replies)",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
