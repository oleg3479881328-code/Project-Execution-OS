from __future__ import annotations

import httpx
import pytest
import respx

from tusya_bot.domain.enums import ResourceType
from tusya_bot.domain.models import MonitoredResource
from tusya_bot.reddit.client import PublicRedditClient, RedditTransportError


def _resource(*, canonical_url: str, resource_type: ResourceType) -> MonitoredResource:
    return MonitoredResource(
        id=1,
        original_input=canonical_url,
        canonical_url=canonical_url,
        subreddit="WedditNYC",
        resource_type=resource_type,
        search_query="photographer" if resource_type is ResourceType.SEARCH else None,
        sort_mode="new",
    )


@pytest.mark.asyncio
@respx.mock
async def test_subreddit_resource_fetch_parsing() -> None:
    respx.get("https://www.reddit.com/r/WedditNYC/new/.json").mock(
        return_value=httpx.Response(
            200,
            json={
                "data": {
                    "children": [
                        {
                            "data": {
                                "id": "abc123",
                                "subreddit": "WedditNYC",
                                "title": "Need a photographer",
                                "selftext": "Brooklyn wedding in August",
                                "permalink": "/r/WedditNYC/comments/abc123/need_a_photographer/",
                                "author": "planner01",
                                "created_utc": 1_720_000_000,
                            }
                        }
                    ]
                }
            },
        )
    )

    client = PublicRedditClient(user_agent="tusya-test/0.1")
    posts = await client.fetch_posts(
        _resource(
            canonical_url="https://www.reddit.com/r/WedditNYC/new/",
            resource_type=ResourceType.SUBREDDIT,
        )
    )
    await client.aclose()

    assert len(posts) == 1
    assert posts[0].reddit_id == "abc123"
    assert posts[0].permalink.startswith("https://www.reddit.com/r/WedditNYC/comments/")


@pytest.mark.asyncio
@respx.mock
async def test_search_resource_fetch_parsing() -> None:
    route = respx.get("https://www.reddit.com/r/WedditNYC/search/.json").mock(
        return_value=httpx.Response(
            200,
            json={
                "data": {
                    "children": [
                        {
                            "data": {
                                "id": "def456",
                                "subreddit": "WedditNYC",
                                "title": "Photographer available",
                                "selftext": "",
                                "permalink": "/r/WedditNYC/comments/def456/photographer_available/",
                                "author": "photo02",
                                "created_utc": 1_720_000_100,
                            }
                        }
                    ]
                }
            },
        )
    )

    client = PublicRedditClient(user_agent="tusya-test/0.1")
    posts = await client.fetch_posts(
        _resource(
            canonical_url=(
                "https://www.reddit.com/r/WedditNYC/search/"
                "?q=photographer&type=posts&sort=new"
            ),
            resource_type=ResourceType.SEARCH,
        ),
        limit=10,
    )
    await client.aclose()

    assert route.called
    request = route.calls[0].request
    assert request.url.params["q"] == "photographer"
    assert request.url.params["type"] == "posts"
    assert request.url.params["sort"] == "new"
    assert request.url.params["limit"] == "10"
    assert posts[0].reddit_id == "def456"


@pytest.mark.asyncio
@respx.mock
async def test_non_200_and_malformed_response_handling() -> None:
    client = PublicRedditClient(user_agent="tusya-test/0.1")
    subreddit_resource = _resource(
        canonical_url="https://www.reddit.com/r/WedditNYC/new/",
        resource_type=ResourceType.SUBREDDIT,
    )

    respx.get("https://www.reddit.com/r/WedditNYC/new/.json").mock(
        return_value=httpx.Response(503, text="temporary unavailable")
    )
    with pytest.raises(RedditTransportError):
        await client.fetch_posts(subreddit_resource)

    respx.reset()
    respx.get("https://www.reddit.com/r/WedditNYC/new/.json").mock(
        return_value=httpx.Response(200, text="{not json}")
    )
    with pytest.raises(RedditTransportError):
        await client.fetch_posts(subreddit_resource)

    await client.aclose()
