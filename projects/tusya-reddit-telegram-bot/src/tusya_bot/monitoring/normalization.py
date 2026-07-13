from __future__ import annotations

from dataclasses import dataclass
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

from tusya_bot.domain.enums import ResourceType

_TRANSIENT_QUERY_KEYS = {"cid", "iid", "utm_source", "utm_medium", "utm_campaign"}
_SEMANTIC_QUERY_KEYS = {"q", "type", "sort", "t"}


@dataclass(frozen=True, slots=True)
class NormalizedResource:
    original_input: str
    canonical_url: str
    subreddit: str
    resource_type: ResourceType
    search_query: str | None
    sort_mode: str


def normalize_reddit_resource(raw_value: str) -> NormalizedResource:
    value = raw_value.strip()
    if not value:
        raise ValueError("Reddit resource cannot be empty")

    if value.lower().startswith("r/"):
        value = f"https://www.reddit.com/{value.strip('/')}/new/"
    elif not value.lower().startswith(("http://", "https://")):
        raise ValueError("Expected a Reddit URL or r/subreddit")

    parsed = urlparse(value)
    host = parsed.netloc.lower().removeprefix("www.")
    if host not in {"reddit.com", "old.reddit.com"}:
        raise ValueError("Only reddit.com resources are supported")

    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) < 2 or parts[0].lower() != "r":
        raise ValueError("A subreddit resource is required")

    subreddit = parts[1]
    if not subreddit.replace("_", "").isalnum():
        raise ValueError("Invalid subreddit name")

    is_search = len(parts) >= 3 and parts[2].lower() == "search"
    query_pairs = []
    for key, val in parse_qsl(parsed.query, keep_blank_values=False):
        key_lower = key.lower()
        if key_lower in _TRANSIENT_QUERY_KEYS:
            continue
        if key_lower in _SEMANTIC_QUERY_KEYS:
            query_pairs.append((key_lower, val))

    query = dict(query_pairs)
    sort_mode = query.get("sort", "new")
    search_query = query.get("q") if is_search else None

    if is_search:
        canonical_path = f"/r/{subreddit}/search/"
        canonical_query = urlencode(
            [
                ("q", search_query or ""),
                ("type", query.get("type", "posts")),
                ("sort", sort_mode),
            ]
        )
        resource_type = ResourceType.SEARCH
    else:
        canonical_path = f"/r/{subreddit}/new/"
        canonical_query = ""
        resource_type = ResourceType.SUBREDDIT
        sort_mode = "new"

    canonical_url = urlunparse(
        ("https", "www.reddit.com", canonical_path, "", canonical_query, "")
    )
    return NormalizedResource(
        original_input=raw_value,
        canonical_url=canonical_url,
        subreddit=subreddit,
        resource_type=resource_type,
        search_query=search_query,
        sort_mode=sort_mode,
    )
