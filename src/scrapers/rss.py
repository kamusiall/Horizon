"""RSS feed scraper implementation."""

import hashlib
import logging
import os
import re
from datetime import datetime, timezone
from typing import List
from email.utils import parsedate_to_datetime
from dateutil.parser import isoparse
import httpx
import feedparser

from .base import BaseScraper
from ..models import ContentItem, SourceType, RSSSourceConfig

logger = logging.getLogger(__name__)


class RSSScraper(BaseScraper):
    """Scraper for RSS/Atom feeds."""

    def __init__(self, sources: List[RSSSourceConfig], http_client: httpx.AsyncClient, keep_undated: bool = False):
        """Initialize RSS scraper.

        Args:
            sources: List of RSS feed configurations
            http_client: Shared async HTTP client
            keep_undated: Research mode. Keep entries without a publication date and window
                only on publication. The default keeps Horizon's windowing (fall back to
                ``updated``; drop undated), because the digest has no cross-run dedup.
        """
        super().__init__({"sources": sources}, http_client)
        self.keep_undated = keep_undated

    async def fetch(self, since: datetime) -> List[ContentItem]:
        """Fetch RSS feed items.

        Args:
            since: Only fetch items published after this time

        Returns:
            List[ContentItem]: Fetched content items
        """
        items = []
        self.reset_coverage()
        self.coverage["instrumented"] = True
        self.coverage["selection_limits"] = {"scope": "entries in the returned feed; unknown publication dates retained"} if self.keep_undated else {
            "scope": "entries in the returned feed dated (published, else updated) within the window; undated entries dropped"}
        sources = self.config["sources"]

        for source in sources:
            if not source.enabled:
                continue

            feed_items = await self._fetch_feed(source, since)
            items.extend(feed_items)

        return items

    async def _fetch_feed(
        self, source: RSSSourceConfig, since: datetime
    ) -> List[ContentItem]:
        """Fetch items from a single RSS feed.

        Args:
            source: RSS feed configuration
            since: Only fetch items after this time

        Returns:
            List[ContentItem]: Feed content items
        """
        items = []

        try:
            # Expand environment variables in URL (e.g. ${LWN_TOKEN})
            feed_url = re.sub(
                r"\$\{(\w+)\}",
                lambda m: os.environ.get(m.group(1), m.group(0)).strip(),
                str(source.url),
            )

            # Fetch feed content
            response = await self.client.get(feed_url, follow_redirects=True)
            response.raise_for_status()

            # Parse feed
            feed = feedparser.parse(response.text)
            if feed.bozo:
                self.record_failure("parse_feed", feed.bozo_exception, source=source.name)

            for entry in feed.entries:
                # Parse published date
                published_at = self._parse_date(entry)
                updated_at = self._parse_date(entry, fields=("updated",))
                if self.keep_undated:
                    if published_at and published_at < since:
                        continue
                else:
                    window_at = published_at or updated_at
                    if not window_at or window_at < since:
                        continue

                # Generate unique ID from feed URL and entry ID
                feed_id = str(source.url).split("//")[1].replace("/", "_")
                entry_id = entry.get("id", entry.get("link", ""))
                entry_hash = hashlib.sha256(str(entry_id).encode("utf-8")).hexdigest()[
                    :16
                ]

                # Extract content
                content = self._extract_content(entry)

                item = ContentItem(
                    id=self._generate_id("rss", feed_id, entry_hash),
                    source_type=SourceType.RSS,
                    title=entry.get("title", "Untitled"),
                    url=entry.get("link", str(source.url)),
                    content=content,
                    author=entry.get("author", source.name),
                    published_at=published_at,
                    updated_at=updated_at,
                    metadata={
                        "original_url": entry.get("link", str(source.url)),
                        "native_entry": dict(entry),
                        "date_window": "unknown_publication" if published_at is None else "within_window",
                        "feed_name": source.name,
                        "category": source.category,
                        "tags": [tag.term for tag in entry.get("tags", [])],
                    },
                )
                items.append(item)

        except httpx.HTTPError as e:
            self.record_failure("fetch_feed", e, source=source.name)
            logger.warning("RSS fetch failed for %s (%s)", source.name, type(e).__name__)
        except Exception as e:
            self.record_failure("parse_feed", e, source=source.name)
            logger.warning("RSS parse failed for %s (%s)", source.name, type(e).__name__)

        return items

    def _parse_date(self, entry: dict, fields=("published", "created")) -> datetime | None:
        """Parse publication date from feed entry.

        Args:
            entry: Feed entry data

        Returns:
            datetime: Parsed publication date or None
        """
        # Try different date fields
        for field in fields:
            if field in entry:
                try:
                    # feedparser's structured time can assume UTC for a naive date.
                    # Parse the original spelling and require an explicit timezone.
                    date_str = entry[field]
                    try:
                        parsed = parsedate_to_datetime(date_str)
                        if parsed.tzinfo is None:
                            # RFC 5322 "-0000": UTC with unknown local offset.
                            parsed = parsed.replace(tzinfo=timezone.utc)
                    except (TypeError, ValueError):
                        parsed = isoparse(date_str)
                    if parsed.tzinfo is not None:
                        return parsed.astimezone(timezone.utc)
                except Exception:
                    continue

        return None

    def _extract_content(self, entry: dict) -> str:
        """Extract text content from feed entry.

        Args:
            entry: Feed entry data

        Returns:
            str: Extracted text content
        """
        # Try different content fields
        if "summary" in entry:
            return entry.summary
        if "description" in entry:
            return entry.description
        if "content" in entry and entry.content:
            # content is usually a list
            return entry.content[0].get("value", "")

        return ""
