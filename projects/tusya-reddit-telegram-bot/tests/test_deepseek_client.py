from types import SimpleNamespace

import pytest

from tusya_bot.ai.client import DeepSeekDraftClient, DraftRequest


class _FakeCreate:
    def __init__(self) -> None:
        self.kwargs: dict[str, object] | None = None

    async def create(self, **kwargs: object) -> SimpleNamespace:
        self.kwargs = kwargs
        return SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content="Draft reply text"))]
        )


class _FakeClient:
    def __init__(self) -> None:
        self.chat = SimpleNamespace(completions=_FakeCreate())


@pytest.mark.asyncio
async def test_deepseek_request_construction() -> None:
    fake_client = _FakeClient()
    client = DeepSeekDraftClient(
        api_key="test-key",
        model="deepseek-v4-flash",
        client=fake_client,
    )

    result = await client.create_draft(
        DraftRequest(
            title="Need photographer",
            body="Looking for someone in NYC.",
            subreddit="WedditNYC",
            matched_keywords=("photographer", "nyc"),
            owner_instruction="Mention Brooklyn experience only if asked.",
        )
    )

    assert result.text == "Draft reply text"
    assert result.provider == "deepseek"
    assert fake_client.chat.completions.kwargs["model"] == "deepseek-v4-flash"
    assert fake_client.chat.completions.kwargs["extra_body"] == {"thinking": {"type": "disabled"}}
    prompt = fake_client.chat.completions.kwargs["messages"][1]["content"]
    assert "Subreddit: r/WedditNYC" in prompt
    assert "Matched keywords: photographer, nyc" in prompt
    assert "Owner instruction: Mention Brooklyn experience only if asked." in prompt
