---
project_mode: internal
status: stable
version: 0.4.0
branch: main
active_issue: 84
pull_request: 85
---

# TikTok Research Sorter — Project State

## Current phase

Version 0.4.0 is integrated into `main`. It adds durable favorites, checkbox-based curation, and safe standalone HTML export while preserving the existing public-profile and hashtag research workflows. The Windows updater follows `main`.

## Working implementation

- WXT Manifest V3 extension with a React side panel.
- Public profile scanning with profile analytics, filters, and versioned CSV/JSON export.
- Public hashtag scanning with per-account top-N selection and a minimum-view threshold.
- A star control on every video card.
- Favorites stored independently from profile and hashtag snapshots.
- Dedicated Favorites view with favorite count.
- Checkbox selection, select all, clear selection, individual removal, and bulk removal.
- Standalone HTML export containing only checked favorites.
- HTML cards include clickable video/profile links, descriptions, preview images, dates, audio, hashtags, and available metrics.
- HTML escaping and HTTP(S)-only URL validation.
- Backward-compatible migration for dashboards created before Favorites existed.
- Atomic Windows one-click updater following `main`.

## Boundaries

- Data remains local unless the user explicitly exports it.
- Exported HTML references public TikTok links and externally hosted preview images; previews can stop loading if TikTok later expires those URLs.
- No login, CAPTCHA, private-profile, paywall, rate-limit, or access-control bypass.
- No additional host permissions beyond TikTok.
- No backend, cloud sync, Chrome Web Store submission, or public GitHub Release.

## Final validation

For PR #85 head `eb3328251cb256164237baefb66b25b449d222cb`:

- Project Execution OS integrity run `29333836074`: passed.
- TikTok Research Sorter CI run `29333836128`: passed.
- Linux reproducible install, strict TypeScript, all tests, production build, packaging, and artifact upload: passed.
- Windows updater dry-run, full local-source validation, and manifest version check: passed.
- PR #85 merged into `main` as `92f66e3fea0b96f30dfad8dc0de7aff5e1a5c696`.

## Distribution

Successful v0.4.0 CI produced:

- unpacked Chrome MV3 extension;
- `tiktok-research-sorter-extension-v0.4.0.zip`;
- `tiktok-sorter-auto-updater-setup-v0.4.0.zip`;
- `tiktok-research-sorter-source-v0.4.0.zip`.

The installable extension ZIP was independently inspected: `manifest.json` is at the archive root and declares version `0.4.0`.
