# Reddit Photo Response Bot

## Project

- Name: `reddit-photo-response-bot`
- Type: internal browser workflow automation
- Short description: review and classify wedding-photography opportunity posts from `r/WedditNYC`.

## Purpose

- Help the owner identify relevant wedding-photographer requests quickly.
- Current success condition: a locally installed Chrome extension classifies visible subreddit posts and preserves manual review decisions.
- The current product does not generate or publish Reddit comments.

## System Entry Point

- `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/START_HERE.md`

## Source Of Truth

- Repository: `oleg3479881328-code/Project-Execution-OS`
- Project root: `projects/reddit-photo-response-bot/`
- Current implementation branch: `feature/reddit-photo-extension-mvp`

## Source Trail

- Product discussion and backend monitor scope: `https://github.com/oleg3479881328-code/Project-Execution-OS/issues/69`
- Chrome Extension MVP execution channel: `https://github.com/oleg3479881328-code/Project-Execution-OS/issues/73`
- Reusable Chrome Extension standards: `blocks/chrome-extension/`

## Current Status

- Mode: implementation
- Phase: Chrome Extension MVP
- Status: locally built and tested; awaiting browser validation and repository review

## Done So Far

- Selected WXT + TypeScript + React + Manifest V3 after Existing Solution First comparison.
- Implemented local deterministic post classification.
- Implemented Reddit page controls, manual decisions, popup review list, and local persistence.
- Completed local TypeScript, unit-test, and production-build validation.

## Current Focus

- Publish the tested implementation for review and perform real Chrome validation against live Reddit markup.

## Next Practical Step

- Load the unpacked production build in Chrome and verify behavior on `r/WedditNYC`.

## Key Decisions And Constraints

- Internal operator extension, not a public SaaS.
- Strict Reddit host allowlist and only the `storage` permission.
- No Reddit API credentials are required for the current browser-open MVP.
- No external AI calls, backend transmission, reply generation, or comment publishing.
- `Existing Solution First` remains mandatory for future phases.

## Read Next

1. `PROJECT_STATE.md`
2. `logs/latest.md`
3. `extension/README.md`
4. GitHub Issue `#73`
