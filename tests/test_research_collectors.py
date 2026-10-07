"""Offline standard-library checks for collector handoff (no AI/config imports)."""
import asyncio
import unittest
from unittest.mock import patch
from datetime import datetime, timezone

import httpx
from src.models import RSSSourceConfig, GitHubSourceConfig, HackerNewsConfig
from src.scrapers.rss import RSSScraper
from src.scrapers.github import GitHubScraper
from src.scrapers.hackernews import HackerNewsScraper

SINCE = datetime(2026, 10, 1, tzinfo=timezone.utc)


class CollectorTests(unittest.IsolatedAsyncioTestCase):
    def test_rss_naive_dates_remain_unknown_and_native_identity_is_stable(self):
        scraper = RSSScraper([], None)
        self.assertIsNone(scraper._parse_date({"published": "2026-10-05T12:00:00", "published_parsed": (2026, 10, 5, 12, 0, 0, 0, 278, 0)}))
        self.assertEqual(scraper._parse_date({"published": "2026-10-05T12:00:00+02:00"}), datetime(2026, 10, 5, 10, tzinfo=timezone.utc))
        # Reuse the established deterministic-ID regression without pytest installation.
        from test_rss import test_rss_ids_are_deterministic
        test_rss_ids_are_deterministic()

    async def test_rss_unknown_and_updated_only_dates_and_native_entry(self):
        feed = '<feed xmlns="http://www.w3.org/2005/Atom"><title>F</title><entry><id>unknown</id><title>Unknown</title><link href="https://example.com/unknown"/></entry><entry><id>updated</id><title>Updated</title><link href="https://EXAMPLE.com/a/"/><updated>2026-10-05T00:00:00Z</updated><content>original</content></entry><entry><id>old</id><title>Old</title><link href="https://example.com/old"/><published>2020-01-01T00:00:00Z</published><updated>2026-10-05T00:00:00Z</updated></entry></feed>'
        async with httpx.AsyncClient(transport=httpx.MockTransport(lambda r: httpx.Response(200, text=feed))) as client:
            scraper = RSSScraper([RSSSourceConfig(name="F", url="https://example.com/feed")], client, keep_undated=True)
            rows = await scraper.fetch(SINCE)
        self.assertEqual(len(rows), 2)
        self.assertTrue(all(item.published_at is None for item in rows))
        self.assertIsNone(rows[0].updated_at)
        self.assertEqual(rows[1].updated_at, datetime(2026, 10, 5, tzinfo=timezone.utc))
        self.assertEqual(rows[1].metadata["original_url"], "https://EXAMPLE.com/a/")
        self.assertEqual(rows[1].metadata["native_entry"]["id"], "updated")
        self.assertEqual(scraper.coverage["failures"], [])

    async def test_rss_timeout_is_visible_without_exception_url(self):
        def timeout(request):
            raise httpx.ReadTimeout("https://example.com?token=SYNTHETIC_TOKEN", request=request)
        async with httpx.AsyncClient(transport=httpx.MockTransport(timeout)) as client:
            scraper = RSSScraper([RSSSourceConfig(name="F", url="https://example.com/feed")], client)
            self.assertEqual(await scraper.fetch(SINCE), [])
        self.assertEqual(scraper.coverage["failures"][0]["error_type"], "ReadTimeout")
        self.assertNotIn("SYNTHETIC_TOKEN", str(scraper.coverage))

    async def test_hn_story_and_comment_timeouts_and_sampling_are_visible(self):
        def handler(request):
            if request.url.path.endswith("topstories.json"):
                return httpx.Response(200, json=[1, 2, 3])
            if request.url.path.endswith(("/2.json", "/11.json")):
                raise httpx.ReadTimeout("synthetic", request=request)
            return httpx.Response(200, json={"id": 1, "time": 1791244800, "title": "T", "url": "https://example.com", "score": 1, "kids": [11]})
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
            scraper = HackerNewsScraper(HackerNewsConfig(min_score=0, fetch_top_stories=2), client)
            rows = await scraper.fetch(SINCE)
        self.assertEqual(len(rows), 1)
        self.assertEqual({row["native_id"] for row in scraper.coverage["failures"]}, {2, 11})
        self.assertFalse(scraper.coverage["truncated"])
        self.assertTrue(scraper.coverage["selection_limits"]["sampled"])
        self.assertEqual(rows[0].metadata["discussion_url"], "https://news.ycombinator.com/item?id=1")
        self.assertIn("native_story", rows[0].metadata)

    async def test_hn_null_item_is_an_explicit_gap(self):
        def handler(request):
            return httpx.Response(200, json=[1]) if request.url.path.endswith("topstories.json") else httpx.Response(200, text="null")
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler), trust_env=False) as client:
            scraper = HackerNewsScraper(HackerNewsConfig(min_score=0), client)
            self.assertEqual(await scraper.fetch(SINCE), [])
        self.assertEqual(scraper.coverage["failures"][0]["stage"], "item_unavailable")

    async def releases(self, handler):
        with patch("src.scrapers.github.os.getenv", return_value=None):
            return await self._releases(handler)

    async def _releases(self, handler):
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler), trust_env=False) as client:
            scraper = GitHubScraper([GitHubSourceConfig(type="repo_releases", owner="a", repo="b")], client)
            rows = await scraper.fetch(SINCE)
        return rows, scraper.coverage

    def release(self, number):
        return {"id": number, "published_at": "2026-10-05T00:00:00Z", "updated_at": "2026-10-06T00:00:00Z", "tag_name": f"v{number}", "html_url": f"https://example.com/v{number}", "author": {"login": "a"}}

    async def test_github_pagination_follows_beyond_old_release(self):
        calls = []
        def handler(request):
            page = int(request.url.params.get("page", "1"))
            calls.append(page)
            release = self.release(page)
            if page == 1:
                release["published_at"] = "2020-01-01T00:00:00Z"
                return httpx.Response(200, json=[self.release(10), release], headers={"Link": '<https://api.github.com/repos/a/b/releases?page=2>; rel="next"'})
            return httpx.Response(200, json=[release], headers={"Link": '<https://api.github.com/repos/a/b/releases?page=2>; rel="next"'} if page == 1 else {})
        rows, coverage = await self.releases(handler)
        self.assertEqual(calls, [1, 2])
        self.assertEqual([row.metadata["native_release"]["id"] for row in rows], [10, 2])
        self.assertFalse(coverage["truncated"])

    async def test_github_later_page_timeout_retains_first_page(self):
        def handler(request):
            if "page" in request.url.params:
                raise httpx.ReadTimeout("synthetic", request=request)
            return httpx.Response(200, json=[self.release(1)], headers={"Link": '<https://api.github.com/repos/a/b/releases?page=2>; rel="next"'})
        rows, coverage = await self.releases(handler)
        self.assertEqual(len(rows), 1)
        self.assertEqual(coverage["failures"][0]["error_type"], "ReadTimeout")

    async def test_github_page_budget_and_untrusted_next_target(self):
        def handler(request):
            page = int(request.url.params.get("page", "1"))
            return httpx.Response(200, json=[self.release(page)], headers={"Link": f'<https://api.github.com/repos/a/b/releases?page={page+1}>; rel="next"'})
        rows, coverage = await self.releases(handler)
        self.assertEqual(len(rows), 5)
        self.assertTrue(coverage["truncated"])
        rows, coverage = await self.releases(lambda request: httpx.Response(200, json=[self.release(1)], headers={"Link": '<https://evil.example/releases>; rel="next"'}))
        self.assertEqual(len(rows), 1)
        self.assertEqual(coverage["failures"][0]["error_type"], "ValueError")

    async def test_github_real_repositories_link_format_is_followed(self):
        calls = []
        def handler(request):
            calls.append(request.url.path)
            page = int(request.url.params.get("page", "1"))
            headers = {"Link": '<https://api.github.com/repositories/12888993/releases?per_page=1&page=2>; rel="next"'} if page == 1 else {}
            return httpx.Response(200, json=[self.release(page)], headers=headers)
        rows, coverage = await self.releases(handler)
        self.assertEqual(len(rows), 2)
        self.assertEqual(coverage["failures"], [])
        self.assertEqual(calls[1], "/repositories/12888993/releases")

    async def test_github_drafts_are_skipped(self):
        draft = dict(self.release(2), draft=True, published_at=None)
        rows, coverage = await self.releases(lambda request: httpx.Response(200, json=[self.release(1), draft]))
        self.assertEqual([row.metadata["native_release"]["id"] for row in rows], [1])

    async def test_github_stops_when_whole_page_is_old(self):
        calls = []
        def handler(request):
            page = int(request.url.params.get("page", "1"))
            calls.append(page)
            release = dict(self.release(page), published_at="2020-01-01T00:00:00Z")
            return httpx.Response(200, json=[release], headers={"Link": f'<https://api.github.com/repos/a/b/releases?page={page+1}>; rel="next"'})
        rows, coverage = await self.releases(handler)
        self.assertEqual(calls, [1])
        self.assertEqual(rows, [])
        self.assertFalse(coverage["truncated"])

    async def test_github_malformed_release_does_not_stop_others(self):
        bad = dict(self.release(2), author=None)
        rows, coverage = await self.releases(lambda request: httpx.Response(200, json=[self.release(1), bad, self.release(3)]))
        self.assertEqual([row.metadata["native_release"]["id"] for row in rows], [1, 3])
        self.assertEqual(coverage["failures"][0]["native_id"], 2)
        self.assertEqual(coverage["failures"][0]["repo"], "a/b")

    async def test_github_failure_names_repo(self):
        def timeout(request):
            raise httpx.ReadTimeout("synthetic", request=request)
        rows, coverage = await self.releases(timeout)
        self.assertEqual(coverage["failures"][0]["repo"], "a/b")
        self.assertTrue(coverage["instrumented"])

    async def test_rss_default_keeps_original_windowing(self):
        feed = '<feed xmlns="http://www.w3.org/2005/Atom"><title>F</title><entry><id>unknown</id><title>Unknown</title><link href="https://example.com/unknown"/></entry><entry><id>updated</id><title>Updated</title><link href="https://example.com/a"/><updated>2026-10-05T00:00:00Z</updated></entry><entry><id>stale</id><title>Stale</title><link href="https://example.com/s"/><updated>2020-10-05T00:00:00Z</updated></entry></feed>'
        async with httpx.AsyncClient(transport=httpx.MockTransport(lambda r: httpx.Response(200, text=feed))) as client:
            scraper = RSSScraper([RSSSourceConfig(name="F", url="https://example.com/feed")], client)
            rows = await scraper.fetch(SINCE)
        self.assertEqual([row.title for row in rows], ["Updated"])
        self.assertTrue(scraper.coverage["instrumented"])

    async def test_rss_failure_names_source(self):
        def boom(request):
            raise httpx.ConnectError("https://example.com?token=SYNTHETIC_TOKEN", request=request)
        async with httpx.AsyncClient(transport=httpx.MockTransport(boom)) as client:
            scraper = RSSScraper([RSSSourceConfig(name="F", url="https://example.com/feed")], client)
            await scraper.fetch(SINCE)
        self.assertEqual(scraper.coverage["failures"][0]["source"], "F")
        self.assertNotIn("SYNTHETIC_TOKEN", str(scraper.coverage))

    def test_rss_minus_zero_offset_is_utc(self):
        scraper = RSSScraper([], None)
        self.assertEqual(scraper._parse_date({"published": "Mon, 05 Oct 2026 12:00:00 -0000"}), datetime(2026, 10, 5, 12, tzinfo=timezone.utc))

    def test_contract_and_uninstrumented_default(self):
        from src.scrapers import base
        self.assertGreaterEqual(base.COLLECTOR_CONTRACT, 1)
        class Plain(base.BaseScraper):
            async def fetch(self, since):
                return []
        self.assertFalse(Plain({}, None).coverage["instrumented"])

    async def test_hn_sampling_is_not_truncation(self):
        def handler(request):
            if request.url.path.endswith("topstories.json"):
                return httpx.Response(200, json=[1, 2, 3])
            return httpx.Response(200, json={"id": 1, "time": 1791244800, "title": "T", "score": 1, "kids": list(range(10, 20))})
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as client:
            scraper = HackerNewsScraper(HackerNewsConfig(min_score=0, fetch_top_stories=1), client)
            await scraper.fetch(SINCE)
        self.assertFalse(scraper.coverage["truncated"])
        self.assertTrue(scraper.coverage["selection_limits"]["sampled"])


if __name__ == "__main__":
    unittest.main()
