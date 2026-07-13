from __future__ import annotations

from datetime import UTC, datetime

from tusya_bot.bot.callbacks import encode_callback, parse_callback
from tusya_bot.delivery.rendering import (
    build_delivery_keyboard,
    chunk_text,
    render_candidate_card,
)
from tusya_bot.domain.enums import PostStatus, ResourceType
from tusya_bot.domain.models import MonitoredResource, RedditPost
from tusya_bot.monitoring.models import DeliveryCandidate


def _candidate() -> DeliveryCandidate:
    resource = MonitoredResource(
        id=1,
        original_input="https://www.reddit.com/r/WedditNYC/new/",
        canonical_url="https://www.reddit.com/r/WedditNYC/new/",
        subreddit="WedditNYC",
        resource_type=ResourceType.SUBREDDIT,
        search_query=None,
        sort_mode="new",
    )
    post = RedditPost(
        id=7,
        reddit_id="abc123",
        resource_id=1,
        subreddit="WedditNYC",
        title="Need <photo> & planner",
        body="Hello <b>team</b> " * 40,
        permalink="https://www.reddit.com/r/WedditNYC/comments/abc123/post/",
        author="owner",
        created_utc=datetime(2026, 7, 13, 21, 0, tzinfo=UTC).isoformat(),
        matched_keywords_json='["photo","planner"]',
        status=PostStatus.NEW,
    )
    return DeliveryCandidate(resource=resource, post=post, matched_keywords=("photo", "planner"))


def test_new_post_card_rendering_and_escaping() -> None:
    text = render_candidate_card(_candidate())

    assert "Need &lt;photo&gt; &amp; planner" in text
    assert "r/WedditNYC" in text
    assert "Ключевые слова: photo, planner" in text
    assert "Черновик не опубликован." in text
    assert "<i>Hello &lt;b&gt;team&lt;/b&gt;" in text


def test_long_post_chunking() -> None:
    value = ("line\n" * 1200).strip()
    chunks = chunk_text(value, limit=500)

    assert len(chunks) > 2
    assert all(len(chunk) <= 500 for chunk in chunks)
    assert chunks[0].startswith("line")


def test_compact_callback_parsing() -> None:
    encoded = encode_callback("open", 42, page=3)
    payload = parse_callback(encoded)

    assert encoded == "open:42:3"
    assert payload.action == "open"
    assert payload.subject_id == 42
    assert payload.page == 3


def test_delivery_keyboard_contains_expected_buttons() -> None:
    keyboard = build_delivery_keyboard(7, "https://reddit.example/post")
    labels = [button.text for row in keyboard.inline_keyboard for button in row]

    assert labels == [
        "📖 Открыть в боте",
        "🔗 Открыть Reddit",
        "✍️ Создать черновик",
        "🙈 Игнорировать",
    ]
