---
project_mode: internal
status: design-preview
version: 0.5.0
branch: agent/tiktok-design-preview
base_branch: main
active_issue: null
pull_request: pending
---

# TikTok Research Sorter — Project State

## Current phase

Version 0.5.0 remains integrated and validated in `main`. The bounded branch `agent/tiktok-design-preview` adds an autonomous HTML design stand for visual iteration without changing the Chrome Extension runtime, permissions, data model, scanning, persistence, analytics, or export logic.

## Active design artifact

- File: `design/sidepanel-design-preview.html`.
- Format: one self-contained HTML file with embedded CSS, mock data, and minimal JavaScript.
- Runtime dependencies: none.
- Browser-extension APIs: none.
- Supported preview states: profile analysis, hashtag research, and favorites grouped by channel.
- Preview tools: fixed width presets, adjustable panel width, compact density, and layout outlines.
- Intended workflow: open the file directly in a browser, iterate with Codex, then selectively transfer approved styling and markup to `entrypoints/sidepanel/App.tsx` and `entrypoints/sidepanel/style.css`.

## Working implementation

- WXT Manifest V3 extension with a React side panel.
- Public profile scanning with expanded channel identity, counters, identifiers, flags, locale, timestamps, and analytics.
- Public hashtag scanning with per-account top-N selection and a minimum-view threshold.
- A star control on every video card.
- Durable favorite entries containing both the video snapshot and a channel snapshot.
- Backward-compatible migration of v0.4.0 favorites to partial channel snapshots.
- Automatic channel-snapshot refresh when richer profile information is collected.
- Same-origin public channel enrichment after adding a favorite, without navigating the visible TikTok page.
- Manual `Обновить канал` action as a fallback.
- Favorites grouped by channel with complete channel cards.
- Selected-only standalone HTML grouped by channel.
- Channel HTML includes identity, public IDs, counters, flags, locale, dates, website, source, channel analytics, links, and selected videos.
- HTML escaping and HTTP(S)-only URL validation.
- Atomic Windows one-click updater following `main`.

## Supported public channel fields

- username, profile URL, display name, avatar, biography, verification, and website;
- public user ID and `secUid`;
- followers, following, friends, total profile likes, and public video count;
- region, language, private-account flag, commerce-account flag, and account creation date;
- locally collected video count, median views, average engagement, and strongest hashtags;
- collection/update timestamps and data source.

Missing fields remain unavailable and are never inferred.

## Boundaries

- The design stand uses illustrative mock data only and must not be treated as collected TikTok data.
- The design stand does not call the network, `chrome.*`, WXT, React, npm packages, or external fonts.
- Data remains local unless the user explicitly exports it.
- TikTok can omit public fields, request verification, change payloads, or expire external preview/avatar URLs.
- Public channel enrichment uses the existing TikTok host permission and does not navigate the visible page.
- No login, CAPTCHA, private-profile, paywall, rate-limit, or access-control bypass.
- No additional host permissions beyond TikTok.
- No backend, cloud sync, Chrome Web Store submission, or public GitHub Release.

## Validation baseline

For stable `main` and PR #87 head `4d12189a5509c9ced21b397d1e5be0d16ed584ab`:

- Project Execution OS integrity run `29339387056`: passed.
- TikTok Research Sorter CI run `29339387139`: passed.
- Linux reproducible install, strict TypeScript, all tests, production build, packaging, and artifact upload: passed.
- Windows updater dry-run, full local-source validation, and manifest version check: passed.
- Installable ZIP inspected: root-level `manifest.json`, manifest version `0.5.0`, 10 extension files, and unchanged TikTok-only host permissions.
- PR #87 merged into `main` as `6a9817c923ed0e531ee7193b8e52ee986b5fe29d`.

For `agent/tiktok-design-preview`:

- the standalone document has complete HTML, style, script, and closing tags;
- the three preview views and width controls are present;
- JavaScript is intentionally limited to preview interaction;
- extension runtime validation is unchanged because runtime files were not edited.

## Distribution

Successful v0.5.0 CI produced:

- unpacked Chrome MV3 extension;
- `tiktok-research-sorter-extension-v0.5.0.zip`;
- `tiktok-sorter-auto-updater-setup-v0.5.0.zip`;
- `tiktok-research-sorter-source-v0.5.0.zip`.
