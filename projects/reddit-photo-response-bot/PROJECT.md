# Reddit Photo Response Bot

## Project

- Name: `reddit-photo-response-bot`
- Type: internal browser workflow automation
- Short description: review and classify wedding-photography opportunity posts from `r/WedditNYC` in a persistent Chrome side panel with optional DeepSeek semantic analysis.

## Purpose

- Help the owner identify relevant wedding-photographer requests quickly.
- Use a fast local rules stage for every visible post.
- Use an optional secure semantic AI stage for ambiguous or promising candidates.
- Keep all decisions human-reviewable.
- The current product does not generate or publish Reddit comments.

## System Entry Point

- `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/START_HERE.md`

## Source Of Truth

- Repository: `oleg3479881328-code/Project-Execution-OS`
- Project root: `projects/reddit-photo-response-bot/`
- Chrome side-panel branch: `feature/reddit-photo-extension-mvp`
- DeepSeek stacked implementation branch: `feature/reddit-photo-deepseek-analysis`

## Source Trail

- Product discussion and backend monitor scope: `https://github.com/oleg3479881328-code/Project-Execution-OS/issues/69`
- Chrome Side Panel MVP execution channel: `https://github.com/oleg3479881328-code/Project-Execution-OS/issues/73`
- DeepSeek semantic analysis channel: `https://github.com/oleg3479881328-code/Project-Execution-OS/issues/76`
- Reusable Chrome Extension standards: `blocks/chrome-extension/`

## Current Status

- Mode: implementation
- Phase: secure DeepSeek semantic analysis
- Status: implementation complete in stacked branch; awaiting automated CI and live secret-backed acceptance

## Done So Far

- Selected WXT + TypeScript + React + Manifest V3 after Existing Solution First comparison.
- Implemented deterministic local post classification.
- Implemented narrow Reddit detection and infinite-scroll capture.
- Implemented persistent Chrome side panel with complete review controls.
- Implemented optional DeepSeek analysis through a Cloudflare Worker proxy.
- Kept the DeepSeek API key exclusively in Worker secrets.
- Added per-post, batch, and optional automatic semantic analysis.
- Added strict AI response validation, persistent AI results, tests, deployment docs, and dedicated CI.

## Current Focus

- Validate the extension and Worker in GitHub Actions.
- Deploy the Worker with owner-controlled secrets.
- Run one live DeepSeek analysis in real Chrome.

## Next Practical Step

- Deploy `deepseek-worker/`, set `DEEPSEEK_API_KEY` and `EXTENSION_ACCESS_KEY` through Wrangler, connect the Worker URL in the side panel, and analyze one controlled post.

## Key Decisions And Constraints

- Internal operator extension, not a public SaaS.
- The side panel is the only operator interface.
- Required host permissions remain limited to `r/WedditNYC`; AI Worker access is granted at runtime only to the configured HTTPS origin.
- The DeepSeek API key must never exist in extension code, storage, chat, GitHub, or build artifacts.
- Automatic AI analysis is disabled by default to control cost.
- Manual classification has final priority.
- No reply generation or automatic Reddit commenting.
- `Existing Solution First` remains mandatory for future phases.

## Read Next

1. `PROJECT_STATE.md`
2. `logs/latest.md`
3. `extension/README.md`
4. `deepseek-worker/README.md`
5. GitHub Issues `#73` and `#76`