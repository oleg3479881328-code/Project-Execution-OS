---
project_mode: internal
status: active
version: 0.2.0
branch: agent/tiktok-research-sorter-mvp
active_issue: 72
pull_request: 71
---

# TikTok Research Sorter — Project State

## Current phase

Reviewer-led stabilization after the first executor report. Code changes are implemented on the project branch; Linux and Windows CI evidence is being regenerated before the pull request can leave draft status.

## Working implementation

- WXT Manifest V3 extension with a React side panel.
- Public TikTok profile scanning initiated by the user.
- Profile card with avatar, name, bio, verification, followers, following, profile likes, video count, scan time, coverage, publication frequency, median views, and strongest hashtags.
- Video cards with cover, views, velocity, engagement, and outlier score.
- Selected TikTok API observation plus embedded-state and DOM fallbacks.
- Local per-profile storage, filters, CSV, and JSON export.
- Windows one-click updater with a dedicated persistent Chrome profile.

## Stabilization changes

- Background dashboard mutations are serialized to prevent lost updates.
- Stale scans recover automatically instead of leaving the interface permanently locked in `scanning`.
- The content script always resets its scan lock through `try/catch/finally`.
- API and embedded JSON data have priority over broad DOM fallbacks.
- Profile and media URLs are restricted to HTTP(S).
- Posting-frequency and average-engagement calculations are corrected.
- Localized compact numbers such as `1,2M`, `1,5 тыс.`, and `2,3 млн` are supported.
- Video duration distinguishes plausible seconds from millisecond payloads.
- CSV exports neutralize spreadsheet formulas.
- The Windows updater builds and validates in an isolated candidate directory, preserves the current build on failure, keeps one previous version for rollback, and supports non-interactive CI execution.

## Automated validation

- 40 unit/regression tests across parser, profile extraction, analytics, number parsing, merge behavior, and CSV safety.
- Linux CI: reproducible install, TypeScript check, tests, production build, and three downloadable packages.
- Windows CI: zero-side-effect dry run plus full local-source updater validation using `-SkipLaunch -NonInteractive`.
- Project Execution OS structure validation requires this file and `logs/latest.md`; both are maintained as durable state.

## Known external risks

1. TikTok may change API payloads, endpoint paths, or DOM selectors.
2. Logged-out or localized pages may omit some profile fields; the card degrades gracefully.
3. Large multi-profile datasets still use `chrome.storage.local`; a future version should move video records to IndexedDB if scale testing shows quota or latency pressure.
4. Chrome Web Store submission and public release remain outside the current authorization.

## Release gate

Do not merge or mark the pull request ready until:

- Linux CI is green;
- Windows updater CI is green;
- Project Execution OS integrity validation is green;
- extension, updater, and source artifacts exist for the final head SHA;
- durable report files and PR description match the final evidence.
