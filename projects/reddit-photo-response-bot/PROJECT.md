# Reddit Photo Response Bot

## Project

- Name: `reddit-photo-response-bot`
- Type: internal browser workflow automation
- Short description: review and classify wedding-photography opportunity posts from `r/WedditNYC` in a persistent Chrome side panel.

## Purpose

- Help the owner identify relevant wedding-photographer requests quickly.
- Current success condition: a locally installed Chrome extension detects visible subreddit posts and provides the complete review workflow in Chrome's side panel.
- The current product does not generate or publish Reddit comments.

## System Entry Point

- `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/START_HERE.md`

## Source Of Truth

- Repository: `oleg3479881328-code/Project-Execution-OS`
- Project root: `projects/reddit-photo-response-bot/`
- Current implementation branch: `feature/reddit-photo-extension-mvp`

## Source Trail

- Product discussion and backend monitor scope: `https://github.com/oleg3479881328-code/Project-Execution-OS/issues/69`
- Chrome Side Panel MVP execution channel: `https://github.com/oleg3479881328-code/Project-Execution-OS/issues/73`
- Reusable Chrome Extension standards: `blocks/chrome-extension/`

## Current Status

- Mode: implementation
- Phase: Chrome Side Panel MVP
- Status: built and automatically validated; awaiting real-browser acceptance and repository review

## Done So Far

- Selected WXT + TypeScript + React + Manifest V3 after Existing Solution First comparison.
- Implemented local deterministic post classification.
- Implemented a narrow Reddit content script for detection and infinite-scroll capture.
- Implemented a persistent Chrome side panel with filters, reasons, matched signals, manual classification, owner decisions, and source-post opening.
- Removed the popup and all injected Reddit-page review controls.
- Completed TypeScript, unit-test, and production-build validation.

## Current Focus

- Perform real Chrome validation against the live Reddit interface and verify toolbar side-panel opening.

## Next Practical Step

- Load the unpacked production build in Chrome and verify the side panel on `r/WedditNYC`.

## Key Decisions And Constraints

- Internal operator extension, not a public SaaS.
- The side panel is the only operator interface.
- Strict Reddit host allowlist.
- Permissions are limited to `storage` and `sidePanel`.
- No Reddit API credentials are required for the current browser-open MVP.
- No external AI calls, backend transmission, reply generation, or comment publishing.
- `Existing Solution First` remains mandatory for future phases.

## Read Next

1. `PROJECT_STATE.md`
2. `logs/latest.md`
3. `extension/README.md`
4. GitHub Issue `#73`
