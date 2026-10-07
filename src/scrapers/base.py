"""Base scraper interface."""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List
import httpx

from ..models import ContentItem


class BaseScraper(ABC):
    """Abstract base class for all scrapers."""

    def __init__(self, config: dict, http_client: httpx.AsyncClient):
        """Initialize scraper.

        Args:
            config: Scraper-specific configuration
            http_client: Shared async HTTP client
        """
        self.config = config
        self.client = http_client
        self.reset_coverage()

    def reset_coverage(self) -> None:
        """Optional collector diagnostics; callers on older revisions can ignore it."""
        self.coverage = {"failures": [], "truncated": False, "selection_limits": {}}

    def record_failure(self, stage: str, error: Exception, **identity) -> None:
        # Never include exception text or request URLs: they may contain credentials.
        self.coverage["failures"].append({"stage": stage, "error_type": type(error).__name__, **identity})

    @abstractmethod
    async def fetch(self, since: datetime) -> List[ContentItem]:
        """Fetch content items published since the given time.

        Args:
            since: Only fetch items published after this time

        Returns:
            List[ContentItem]: Fetched content items
        """
        pass

    def _generate_id(self, source_type: str, subtype: str, native_id: str) -> str:
        """Generate unique content item ID.

        Args:
            source_type: Source type (github, hackernews, etc.)
            subtype: Content subtype (event, release, story, etc.)
            native_id: Native ID from the source platform

        Returns:
            str: Unique ID in format {source}:{subtype}:{native_id}
        """
        return f"{source_type}:{subtype}:{native_id}"
