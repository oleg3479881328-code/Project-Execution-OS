from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol

from openai import AsyncOpenAI


@dataclass(frozen=True, slots=True)
class DraftRequest:
    title: str
    body: str
    subreddit: str
    matched_keywords: tuple[str, ...]
    language: str = "English (US)"
    tone: str = "helpful, natural, non-pushy"
    max_words: int = 120
    owner_instruction: str | None = None


@dataclass(frozen=True, slots=True)
class DraftResult:
    text: str
    provider: str
    model: str
    prompt_version: str


class DraftModelClient(Protocol):
    async def create_draft(self, request: DraftRequest) -> DraftResult: ...


class DeepSeekDraftClient:
    PROMPT_VERSION = "reddit-reply-v1"

    def __init__(
        self,
        *,
        api_key: str,
        base_url: str = "https://api.deepseek.com",
        model: str = "deepseek-v4-flash",
        timeout_seconds: float = 30.0,
        client: Any | None = None,
    ) -> None:
        self._model = model
        self._client = client or AsyncOpenAI(
            api_key=api_key,
            base_url=base_url.rstrip("/"),
            timeout=timeout_seconds,
            max_retries=2,
        )

    async def create_draft(self, request: DraftRequest) -> DraftResult:
        title = request.title.strip()[:500]
        body = request.body.strip()[:8_000]
        keywords = ", ".join(request.matched_keywords[:20]) or "none"
        instruction = (request.owner_instruction or "").strip()[:1_000]

        system_prompt = (
            "You write draft Reddit replies for a wedding photographer. "
            "Return only the proposed reply text. Never claim the reply was posted. "
            "Do not invent facts, prices, availability, credentials, or personal experience. "
            "Avoid spammy sales language. Respect the requested language, tone, and word limit."
        )
        user_prompt = (
            f"Subreddit: r/{request.subreddit}\n"
            f"Post title: {title}\n"
            f"Post body: {body}\n"
            f"Matched keywords: {keywords}\n"
            f"Language: {request.language}\n"
            f"Tone: {request.tone}\n"
            f"Maximum words: {request.max_words}\n"
            f"Owner instruction: {instruction or 'none'}\n\n"
            "Write one useful, human-sounding draft reply."
        )

        response = await self._client.chat.completions.create(
            model=self._model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            stream=False,
            temperature=0.4,
            max_tokens=500,
            extra_body={"thinking": {"type": "disabled"}},
        )

        text = (response.choices[0].message.content or "").strip()
        if not text:
            raise RuntimeError("DeepSeek returned an empty draft")

        return DraftResult(
            text=text,
            provider="deepseek",
            model=self._model,
            prompt_version=self.PROMPT_VERSION,
        )
