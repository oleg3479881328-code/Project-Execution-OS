---
project_mode: internal
status: stable
version: 0.2.0
branch: main
active_issue: 72
pull_request: 71
---

# TikTok Research Sorter — Project State

## Current phase

Version 0.2.0 is integrated into `main`. The automatic Windows updater follows `main`, so future approved changes can be delivered through the desktop shortcut without manual extension reinstallation.

## Working implementation

- WXT Manifest V3 extension with a React side panel.
- Public TikTok profile scanning initiated by the user.
- Full profile card with avatar, name, bio, verification, followers, following, profile likes, video count, scan time, coverage, publication frequency, median views, and strongest hashtags.
- Video cards with cover, views, velocity, engagement, and outlier score.
- Selected TikTok API observation plus embedded-state and DOM fallbacks.
- Local per-profile storage, filters, CSV, and JSON export.
- Atomic Windows one-click updater with a dedicated persistent Chrome profile.

## Stabilization completed

- Background dashboard mutations are serialized to prevent lost updates.
- Stale scans recover automatically.
- Content-script scan locks are released through `try/catch/finally`.
- Source precedence is API → embedded JSON → DOM.
- External URLs are restricted to HTTP(S).
- Publication frequency, average engagement, localized counts, duration normalization, and CSV formula safety are covered.
- The updater validates in an isolated candidate directory, preserves the current build on failure, and keeps one previous version for rollback.

## Automated validation

- 40 unit and regression tests pass.
- Strict TypeScript check passes.
- Linux production build and packaging pass.
- Windows updater dry-run and full local-source validation pass.
- Project Execution OS structure and system-context manifest validation pass.

## Distribution

The updater default is `main`. Successful CI produces:

- unpacked Chrome MV3 extension;
- `tiktok-research-sorter-extension-0.2.0.zip`;
- `tiktok-sorter-auto-updater-setup-0.2.0.zip`;
- `tiktok-research-sorter-source-0.2.0.zip`.

## Remaining boundaries

- No Chrome Web Store submission or public GitHub Release is authorized.
- TikTok may change public payloads or DOM structure.
- Very large future datasets may require IndexedDB instead of `chrome.storage.local`.
