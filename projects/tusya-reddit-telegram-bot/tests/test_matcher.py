import pytest

from tusya_bot.monitoring.matcher import KeywordRule, find_matching_keywords


def test_matcher_collects_unique_matches() -> None:
    matches = find_matching_keywords(
        title="Looking for wedding photographer recommendations",
        body="Photographer budget discussion here.",
        rules=[
            KeywordRule("photographer"),
            KeywordRule("photographer"),
            KeywordRule("budget", match_mode="contains"),
        ],
    )
    assert matches == ("photographer", "budget")


def test_matcher_rejects_unsupported_mode() -> None:
    with pytest.raises(ValueError):
        find_matching_keywords(
            title="hello",
            body="world",
            rules=[KeywordRule("hello", match_mode="regex")],
        )
