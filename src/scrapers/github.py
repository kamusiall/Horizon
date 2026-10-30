"""GitHub scraper implementation."""

import logging
import os
import re
from datetime import datetime
from typing import List, Optional
from urllib.parse import urlsplit
import httpx

from .base import BaseScraper
from ..models import ContentItem, SourceType, GitHubSourceConfig

logger = logging.getLogger(__name__)


class GitHubScraper(BaseScraper):
    """Scraper for GitHub events and releases."""

    def __init__(self, sources: List[GitHubSourceConfig], http_client: httpx.AsyncClient):
        """Initialize GitHub scraper.

        Args:
            sources: List of GitHub source configurations
            http_client: Shared async HTTP client
        """
        super().__init__({"sources": sources}, http_client)
        self.token = os.getenv("GITHUB_TOKEN")
        self.base_url = "https://api.github.com"

    def _get_headers(self) -> dict:
        """Get request headers with optional authentication.

        Returns:
            dict: HTTP headers
        """
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "Horizon-Aggregator"
        }
        if self.token:
            headers["Authorization"] = f"token {self.token}"
        return headers

    async def fetch(self, since: datetime) -> List[ContentItem]:
        """Fetch GitHub content items.

        Args:
            since: Only fetch items published after this time

        Returns:
            List[ContentItem]: Fetched content items
        """
        items = []
        self.reset_coverage()
        self.coverage["instrumented"] = True
        self.coverage["selection_limits"] = {"release_pages": 5, "releases_per_page": 100}
        sources = self.config["sources"]

        for source in sources:
            if not source.enabled:
                continue

            if source.type == "user_events" and source.username:
                user_items = await self._fetch_user_events(source.username, since)
                items.extend(user_items)
            elif source.type == "repo_releases" and source.owner and source.repo:
                release_items = await self._fetch_repo_releases(
                    source.owner, source.repo, since
                )
                items.extend(release_items)

        return items

    async def _fetch_user_events(
        self,
        username: str,
        since: datetime
    ) -> List[ContentItem]:
        """Fetch public events for a user.

        Args:
            username: GitHub username
            since: Only fetch events after this time

        Returns:
            List[ContentItem]: Event content items
        """
        url = f"{self.base_url}/users/{username}/events/public"
        items = []

        try:
            response = await self.client.get(url, headers=self._get_headers(), follow_redirects=True)
            response.raise_for_status()
            events = response.json()

            for event in events:
                created_at = datetime.fromisoformat(
                    event["created_at"].replace("Z", "+00:00")
                )

                if created_at < since:
                    continue

                # Filter interesting event types
                event_type = event["type"]
                if event_type not in [
                    "PushEvent", "CreateEvent", "ReleaseEvent",
                    "PublicEvent", "WatchEvent"
                ]:
                    continue

                item = self._parse_event(event, username)
                if item:
                    items.append(item)

        except httpx.HTTPError as e:
            self.record_failure("user_events", e)
            logger.warning("GitHub events failed (%s)", type(e).__name__)

        return items

    def _parse_event(self, event: dict, username: str) -> Optional[ContentItem]:
        """Parse GitHub event into ContentItem.

        Args:
            event: GitHub event data
            username: GitHub username

        Returns:
            Optional[ContentItem]: Parsed content item or None
        """
        event_type = event["type"]
        event_id = event["id"]
        created_at = datetime.fromisoformat(event["created_at"].replace("Z", "+00:00"))

        repo_name = event["repo"]["name"]
        repo_url = f"https://github.com/{repo_name}"

        # Generate title and content based on event type
        if event_type == "PushEvent":
            commits = event["payload"].get("commits", [])
            title = f"{username} pushed {len(commits)} commit(s) to {repo_name}"
            content = "\n".join([c.get("message", "") for c in commits[:3]])
        elif event_type == "CreateEvent":
            ref_type = event["payload"].get("ref_type", "repository")
            title = f"{username} created {ref_type} in {repo_name}"
            content = event["payload"].get("description", "")
        elif event_type == "ReleaseEvent":
            release = event["payload"].get("release", {})
            title = f"{username} released {release.get('tag_name', '')} in {repo_name}"
            content = release.get("body", "")
            repo_url = release.get("html_url", repo_url)
        elif event_type == "PublicEvent":
            title = f"{username} made {repo_name} public"
            content = ""
        elif event_type == "WatchEvent":
            title = f"{username} starred {repo_name}"
            content = ""
        else:
            return None

        return ContentItem(
            id=self._generate_id("github", "event", event_id),
            source_type=SourceType.GITHUB,
            title=title,
            url=repo_url,
            content=content,
            author=username,
            published_at=created_at,
            metadata={
                "event_type": event_type,
                "repo": repo_name,
            }
        )

    async def _fetch_repo_releases(
        self,
        owner: str,
        repo: str,
        since: datetime
    ) -> List[ContentItem]:
        """Fetch releases for a repository.

        Args:
            owner: Repository owner
            repo: Repository name
            since: Only fetch releases after this time

        Returns:
            List[ContentItem]: Release content items
        """
        url = f"{self.base_url}/repos/{owner}/{repo}/releases"
        repo_name = f"{owner}/{repo}"
        allowed_paths = re.compile(r"^(%s|/repositories/\d+/releases)$" % re.escape(urlsplit(url).path))
        items = []

        try:
            next_url = url + "?per_page=100"
            for page in range(1, 6):
                response = await self.client.get(next_url, headers=self._get_headers(), follow_redirects=True)
                response.raise_for_status()
                self.coverage["release_pages_fetched"] = page
                in_window = False
                for release in response.json():
                    native_id = release.get("id") if isinstance(release, dict) else None
                    try:
                        if release.get("draft"):
                            continue  # unpublished; visible only to push-capable tokens
                        published_at = datetime.fromisoformat(release["published_at"].replace("Z", "+00:00")) if release.get("published_at") else None
                        if published_at and published_at < since:
                            continue
                        in_window = True
                        items.append(ContentItem(
                            id=self._generate_id("github", "release", str(release["id"])),
                            source_type=SourceType.GITHUB,
                            title=f"{repo_name} released {release['tag_name']}",
                            url=release["html_url"],
                            content=release.get("body", ""),
                            author=release["author"]["login"],
                            published_at=published_at,
                            updated_at=datetime.fromisoformat(release["updated_at"].replace("Z", "+00:00")) if release.get("updated_at") else None,
                            metadata={
                                "original_url": release["html_url"],
                                "native_release": dict(release),
                                "repo": repo_name,
                                "tag": release["tag_name"],
                                "prerelease": release.get("prerelease", False),
                            }
                        ))
                    except (ValueError, KeyError, TypeError, AttributeError) as e:
                        in_window = True  # unknown date: do not treat the page as exhausted
                        self.record_failure("release", e, repo=repo_name, native_id=native_id)
                        logger.warning("GitHub release skipped for %s (%s)", repo_name, type(e).__name__)
                following = response.links.get("next", {}).get("url")
                if not following or not in_window:
                    break  # last page, or every release on this page predates the window
                parts = urlsplit(following)
                if parts.scheme != "https" or parts.netloc != "api.github.com" or not allowed_paths.match(parts.path):
                    raise ValueError("Unexpected release pagination target")
                if page == 5:
                    self.coverage["truncated"] = True
                    break
                next_url = following

        except (httpx.HTTPError, ValueError, KeyError, TypeError) as e:
            self.record_failure("repo_releases", e, repo=repo_name)
            logger.warning("GitHub releases failed for %s (%s)", repo_name, type(e).__name__)

        return items
