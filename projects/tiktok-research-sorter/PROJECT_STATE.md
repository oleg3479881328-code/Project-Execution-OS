---
project_mode: internal
status: active
version: 0.3.0
branch: agent/tiktok-research-sorter-tag-scan-v0.3.0
active_issue: 82
pull_request: 83
---

# TikTok Research Sorter — Project State

## Current phase

Version 0.3.0 adds public hashtag-page research while preserving the existing profile workflow. PR #83 is under automated validation before integration into `main`.

## Working implementation

- WXT Manifest V3 extension with a React side panel.
- Automatic detection of public profile pages and `/tag/<hashtag>` pages.
- Public profile scanning with profile card, outlier analytics, filtering, and export.
- Public hashtag scanning with automatic scrolling and selected TikTok challenge/search payload observation.
- Hashtag videos grouped by account.
- User-selectable top videos per account: 1, 2, 3, 5, or 10.
- User-selectable minimum view threshold.
- Local hashtag snapshots that can be re-filtered after scanning.
- Versioned CSV and JSON export.
- Atomic Windows one-click updater following `main`.

## Boundaries

- Hashtag mode selects top videos among items actually discovered on the open hashtag page.
- It does not silently open every creator profile.
- No login, CAPTCHA, private-profile, paywall, rate-limit, or access-control bypass.
- No additional host permissions beyond TikTok.
- No Chrome Web Store submission or public GitHub Release is authorized.

## Validation status

Local implementation validation completed before push:

- strict TypeScript check passed;
- hashtag selection fixture tests passed;
- production Chrome MV3 build passed.

Final GitHub Linux, Windows, Project Execution OS integrity, artifact, and merge evidence remain pending on PR #83.

## Distribution target

Successful CI must produce:

- unpacked Chrome MV3 extension;
- `tiktok-research-sorter-extension-v0.3.0.zip`;
- `tiktok-sorter-auto-updater-setup-v0.3.0.zip`;
- `tiktok-research-sorter-source-v0.3.0.zip`.
