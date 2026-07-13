from __future__ import annotations

from enum import StrEnum


class ResourceType(StrEnum):
    SUBREDDIT = "subreddit"
    SEARCH = "search"


class MatchMode(StrEnum):
    CONTAINS = "contains"
    PHRASE = "phrase"
    EXACT = "exact"


class PostStatus(StrEnum):
    NEW = "new"
    IGNORED = "ignored"
    OPENED = "opened"
    DRAFTED = "drafted"


class DeliveryStatus(StrEnum):
    DELIVERED = "delivered"
    FAILED = "failed"
