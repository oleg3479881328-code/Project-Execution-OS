from tusya_bot.domain.enums import ResourceType
from tusya_bot.monitoring.normalization import normalize_reddit_resource


def test_normalize_subreddit_short_form() -> None:
    result = normalize_reddit_resource("r/WedditNYC")
    assert result.canonical_url == "https://www.reddit.com/r/WedditNYC/new/"
    assert result.resource_type is ResourceType.SUBREDDIT
    assert result.sort_mode == "new"


def test_normalize_search_url_preserves_semantic_query() -> None:
    result = normalize_reddit_resource(
        "https://www.reddit.com/r/WedditNYC/search/?q=photographer&type=posts&sort=new&cId=123"
    )
    assert result.resource_type is ResourceType.SEARCH
    assert result.search_query == "photographer"
    assert "cId" not in result.canonical_url
    assert result.canonical_url.endswith("/search/?q=photographer&type=posts&sort=new")
