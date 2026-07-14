---
project_mode: internal
status: stable
version: 0.3.0
branch: main
active_issue: 82
pull_request: 83
---

# TikTok Research Sorter — Project State

## Current phase

Version 0.3.0 is integrated into `main`. It adds public TikTok hashtag-page research while preserving the existing public-profile workflow. The Windows updater already follows `main`, so approved future builds can be delivered through the existing desktop shortcut.

## Working implementation

- WXT Manifest V3 extension with a React side panel.
- Automatic detection of public profile pages and `/tag/<hashtag>` pages.
- Public profile scanning with profile card, outlier analytics, filtering, and versioned export.
- Public hashtag scanning with automatic scrolling and selected TikTok challenge/search payload observation.
- Hashtag videos grouped by account.
- User-selectable top videos per account: 1, 2, 3, 5, or 10.
- User-selectable minimum view threshold.
- Local hashtag snapshots that can be re-filtered after scanning.
- Versioned CSV and JSON exports.
- Atomic Windows one-click updater following `main`.

## Boundaries

- Hashtag mode selects top videos among items actually discovered on the open hashtag page.
- It does not silently open every creator profile.
- No login, CAPTCHA, private-profile, paywall, rate-limit, or access-control bypass.
- No additional host permissions beyond TikTok.
- No Chrome Web Store submission or public GitHub Release is authorized.

## Final validation

For PR #83 head `5de3ce07dace425ea63359b4340c0beedf3fa5a0`:

- Project Execution OS integrity run `29294689690`: passed.
- TikTok Research Sorter CI run `29294689721`: passed.
- Linux reproducible install, TypeScript, tests, build, packaging, and artifact upload: passed.
- Windows updater dry-run, full local-source validation, and manifest version check: passed.
- PR #83 merged into `main` as `b1d0d79a369c5aa7595c48d5b29aea235e775748`.

## Distribution

Successful v0.3.0 CI produced:

- unpacked Chrome MV3 extension;
- `tiktok-research-sorter-extension-v0.3.0.zip`;
- `tiktok-sorter-auto-updater-setup-v0.3.0.zip`;
- `tiktok-research-sorter-source-v0.3.0.zip`.

The installable extension ZIP was verified to contain `manifest.json` at its archive root with manifest version `0.3.0`.
