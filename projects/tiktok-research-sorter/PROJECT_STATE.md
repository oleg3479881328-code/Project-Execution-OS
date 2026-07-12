---
project_mode: internal
status: ready_for_merge_review
version: 0.2.0
branch: agent/tiktok-research-sorter-mvp
active_issue: 72
pull_request: 71
---

# TikTok Research Sorter — Project State

## Current phase

Reviewer-led stabilization is complete. Required Linux CI, Windows updater CI, Project Execution OS integrity checks, and artifact generation are green. The pull request is ready to leave draft status and enter the separate merge-decision gate.

## Working implementation

- WXT Manifest V3 extension with a React side panel.
- Public TikTok profile scanning initiated by the user.
- Profile card with avatar, name, bio, verification, followers, following, profile likes, video count, scan time, coverage, publication frequency, median views, and strongest hashtags.
- Video cards with cover, views, velocity, engagement, and outlier score.
- Selected TikTok API observation plus embedded-state and DOM fallbacks.
- Local per-profile storage, filters, CSV, and JSON export.
- Windows one-click updater with a dedicated persistent Chrome profile.

## Stabilization completed

- Background dashboard mutations are serialized to prevent lost updates.
- Stale scans recover automatically instead of leaving the interface locked in `scanning`.
- The content script always releases its scan lock through `try/catch/finally`.
- API and embedded JSON data have priority over DOM fallbacks.
- Profile and media URLs are restricted to HTTP(S).
- Posting-frequency and average-engagement calculations are corrected.
- Localized compact numbers such as `1,2M`, `1,5 тыс.`, and `2,3 млн` are supported.
- Video duration distinguishes plausible seconds from millisecond payloads.
- CSV exports neutralize spreadsheet formulas.
- The Windows updater validates in an isolated candidate directory, preserves the current build on failure, keeps one previous version for rollback, and supports non-interactive CI execution.

## Automated validation

- 40 unit and regression tests pass.
- Strict TypeScript check passes.
- Chrome MV3 production build passes.
- Linux packaging produces the extension ZIP, updater ZIP, source ZIP, and unpacked build.
- Windows dry-run and complete local-source updater validation pass.
- Generated manifest version is verified.
- Project structure and system-context manifest validation pass.

## Artifacts

Successful CI uploads:

- unpacked Chrome MV3 extension;
- `tiktok-research-sorter-extension-0.2.0.zip`;
- `tiktok-sorter-auto-updater-setup-0.2.0.zip`;
- `tiktok-research-sorter-source-0.2.0.zip`.

## Known external risks

1. TikTok may change API payloads, endpoint paths, or DOM selectors.
2. Logged-out or localized pages may omit profile fields; the card degrades gracefully.
3. Very large multi-profile datasets may eventually require IndexedDB instead of `chrome.storage.local`.
4. Chrome Web Store submission and public release remain outside the current authorization.

## Remaining gate

Merging PR #71 and switching the updater default branch from `agent/tiktok-research-sorter-mvp` to `main` are separate repository decisions. No external publication is authorized.
