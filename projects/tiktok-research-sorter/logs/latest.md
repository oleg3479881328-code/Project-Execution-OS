# Latest Log — TikTok Research Sorter

Date: 2026-07-14
Version: `0.5.0` design-only follow-up
Issue: none
Pull request: `#88` draft
Branch: `agent/tiktok-design-preview`
Status: standalone design preview added; extension runtime unchanged

## Current bounded change

- Added `design/sidepanel-design-preview.html` as a self-contained browser page for visual iteration with Codex.
- Reproduced the three active extension surfaces: profile analysis, hashtag research, and favorites grouped by channel.
- Added representative mock profile, channel, video, metrics, controls, cards, filters, and selected states.
- Added width presets for 360, 430, 520, and 760 pixels plus a continuous width control.
- Added compact-density and layout-outline preview switches.
- Centralized the main visual settings in CSS custom properties near the top of the file.
- Kept CSS and JavaScript embedded so the preview opens directly without npm, WXT, React, a local server, or Chrome Extension APIs.
- Did not change `entrypoints/sidepanel/App.tsx`, `entrypoints/sidepanel/style.css`, `manifest.json`, permissions, storage, scanning, analytics, or exports.

## Intended workflow

1. Open `design/sidepanel-design-preview.html` directly in a browser.
2. Use Codex to modify the mock markup and CSS until the visual direction is approved.
3. Transfer only approved changes into the React side panel.
4. Run the full extension validation before merging runtime design changes.

## Design-preview validation

- Complete HTML document and closing tags are present.
- Profile, hashtag, and favorites preview panels are present.
- Tab switching, width controls, compact mode, outline mode, and favorite selection are implemented with local JavaScript.
- No external scripts, styles, fonts, images, network requests, or remote executable code were added.
- No TikTok credentials, cookies, tokens, browser profiles, private payloads, or user-identifying traffic were added.
- Runtime CI is not materially affected because the extension implementation was not changed.

## Stable v0.5.0 baseline

PR #87 was merged into `main` as `6a9817c923ed0e531ee7193b8e52ee986b5fe29d` after:

- Project Execution OS integrity validation passed;
- TikTok Research Sorter CI passed;
- Linux reproducible install passed;
- strict TypeScript passed;
- all unit and regression tests passed;
- production Chrome MV3 build passed;
- packaging and artifact upload passed;
- Windows updater dry-run and full local-source validation passed;
- generated manifest version validation passed.

The stable extension remains version `0.5.0` with TikTok-only host access and no backend, cloud sync, remote executable code, login bypass, CAPTCHA bypass, private-profile access, or access-control evasion.

## Owner action

Open the standalone HTML file from draft PR #88 and use it as the visual workspace. No extension installation or rebuild is required for design iteration.
