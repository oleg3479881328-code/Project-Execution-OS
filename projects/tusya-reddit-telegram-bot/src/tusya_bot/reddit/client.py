from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any, Protocol
from urllib.parse import parse_qsl, urlparse, urlunparse

import httpx

from tusya_bot.domain.models import MonitoredResource


class RedditTransportError(RuntimeError):
    """Raised when the public Reddit transport cannot return safe post data."""


@dataclass(frozen=True, slots=True)
class RedditFetchedPost:
    reddit_id: str
    subreddit: str
    title: str
    body: str
    permalink: str
    author: str | None
    created_utc: str


class RedditResourceClient(Protocol):
    async def fetch_posts(
        self,
        resource: MonitoredResource,
        *,
        limit: int = 25,
    ) -> list[RedditFetchedPost]: ...


class PublicRedditClient:
    def __init__(
        self,
        *,
        user_agent: str,
        timeout_seconds: float = 20.0,
        max_response_bytes: int = 1_000_000,
        client: httpx.AsyncClient | None = None,
    ) -> None:
        self._max_response_bytes = max_response_bytes
        self._owns_client = client is None
        self._client = client or httpx.AsyncClient(
            timeout=timeout_seconds,
            follow_redirects=True,
            headers={"User-Agent": user_agent},
        )

    async def aclose(self) -> None:
        if self._owns_client:
            await self._client.aclose()

    async def fetch_posts(
        self,
        resource: MonitoredResource,
        *,
        limit: int = 25,
    ) -> list[RedditFetchedPost]:
        if resource.id is None:
            raise RedditTransportError("Resource must be persisted before polling")

        url = _build_listing_json_url(resource.canonical_url)
        params = _build_listing_params(resource.canonical_url, limit)

        async with self._client.stream("GET", url, params=params) as response:
            if response.status_code != 200:
                raise RedditTransportError(
                    f"Reddit returned HTTP {response.status_code} for resource {resource.id}"
                )
            raw_body = await _read_bounded_body(
                response=response,
                max_response_bytes=self._max_response_bytes,
            )

        try:
            payload = json.loads(raw_body)
        except json.JSONDecodeError as error:
            raise RedditTransportError("Reddit returned invalid JSON") from error

        return _parse_listing_payload(payload)


def _build_listing_json_url(canonical_url: str) -> str:
    parsed = urlparse(canonical_url)
    path = parsed.path.rstrip("/")
    if not path:
        raise RedditTransportError("Canonical URL path is empty")
    return urlunparse((parsed.scheme, parsed.netloc, f"{path}/.json", "", "", ""))


def _build_listing_params(canonical_url: str, limit: int) -> dict[str, str]:
    parsed = urlparse(canonical_url)
    params = {
        key: value for key, value in parse_qsl(parsed.query, keep_blank_values=False)
    }
    params["limit"] = str(max(1, min(limit, 100)))
    params["raw_json"] = "1"
    return params


async def _read_bounded_body(
    *,
    response: httpx.Response,
    max_response_bytes: int,
) -> str:
    body = bytearray()
    async for chunk in response.aiter_bytes():
        body.extend(chunk)
        if len(body) > max_response_bytes:
            raise RedditTransportError("Reddit response exceeded configured size limit")
    return body.decode("utf-8")


def _parse_listing_payload(payload: Any) -> list[RedditFetchedPost]:
    if not isinstance(payload, dict):
        raise RedditTransportError("Reddit payload root must be an object")

    data = payload.get("data")
    if not isinstance(data, dict):
        raise RedditTransportError("Reddit payload is missing listing data")

    children = data.get("children")
    if not isinstance(children, list):
        raise RedditTransportError("Reddit payload is missing listing children")

    posts: list[RedditFetchedPost] = []
    for child in children:
        if not isinstance(child, dict):
            raise RedditTransportError("Reddit child entry must be an object")
        child_data = child.get("data")
        if not isinstance(child_data, dict):
            raise RedditTransportError("Reddit child data must be an object")
        posts.append(_parse_post(child_data))
    return posts


def _parse_post(data: dict[str, Any]) -> RedditFetchedPost:
    reddit_id = _expect_non_empty_string(data, "id")
    subreddit = _expect_non_empty_string(data, "subreddit")
    title = _expect_string(data, "title")
    body = _expect_string(data, "selftext")
    permalink = _expect_non_empty_string(data, "permalink")
    author = data.get("author")
    created_utc = data.get("created_utc")

    if author is not None and not isinstance(author, str):
        raise RedditTransportError("Reddit author must be a string when present")
    if not isinstance(created_utc, int | float):
        raise RedditTransportError("Reddit created_utc must be numeric")

    return RedditFetchedPost(
        reddit_id=reddit_id,
        subreddit=subreddit,
        title=title,
        body=body,
        permalink=f"https://www.reddit.com{permalink}",
        author=author,
        created_utc=datetime.fromtimestamp(created_utc, tz=UTC).isoformat(),
    )


def _expect_string(data: dict[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str):
        raise RedditTransportError(f"Reddit field {key!r} must be a string")
    return value


def _expect_non_empty_string(data: dict[str, Any], key: str) -> str:
    value = _expect_string(data, key)
    if not value.strip():
        raise RedditTransportError(f"Reddit field {key!r} must not be empty")
    return value
