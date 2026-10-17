# ADR-001 — DeepSeek API for reply drafts

Status: Accepted
Date: 2026-07-13

## Decision

The AI provider for draft Reddit replies is **DeepSeek**, not OpenAI.

Use the official OpenAI-compatible DeepSeek endpoint:

- base URL: `https://api.deepseek.com`
- endpoint: `/chat/completions`
- default model: `deepseek-v4-flash`
- thinking: disabled for fast reply-draft generation
- provider value stored in `reply_drafts.provider`: `deepseek`

The model remains configurable through `DEEPSEEK_MODEL` so it can be changed without a code release.

## Environment

- `DEEPSEEK_API_KEY`
- `DEEPSEEK_BASE_URL=https://api.deepseek.com`
- `DEEPSEEK_MODEL=deepseek-v4-flash`
- `DEEPSEEK_TIMEOUT_SECONDS=30`

`OPENAI_API_KEY` and `OPENAI_MODEL` are not part of this project.

## Integration choice

Use the official `openai` Python SDK configured with the DeepSeek base URL. DeepSeek documents its API as OpenAI-compatible. The application must wrap the SDK behind a project-owned `DraftModelClient` protocol so the provider can be replaced later.

## Request policy

- non-streaming request for MVP;
- `thinking={"type": "disabled"}`;
- low temperature for stable business drafts;
- bounded `max_tokens`;
- title/body length limits before sending;
- no Telegram IDs, API keys, local paths or private owner data in the prompt;
- safe error mapping without logging request content or secrets.

## Output policy

The model returns plain text only. The result is labeled as a draft, saved in SQLite and never posted automatically to Reddit.
