---
project_mode: internal
status: active-development
version: 0.6.0
branch: agent/tiktok-design-preview
base_branch: main
active_issue: null
pull_request: 88
---

# TikTok Research Sorter — Project State

## Current phase

Version 0.5.0 remains the stable integrated baseline in `main`. Draft PR #88 now contains two bounded v0.6.0 additions:

1. an autonomous HTML design stand for visual iteration;
2. a per-video-card download control that reuses the existing local `Yt-Dlp-Download-Manager` queue.

## Active design artifact

- File: `design/sidepanel-design-preview.html`.
- Format: one self-contained HTML file with embedded CSS, mock data, and minimal JavaScript.
- Runtime dependencies: none.
- Browser-extension APIs: none.
- Supported preview states: profile analysis, hashtag research, and favorites grouped by channel.
- Preview tools: fixed width presets, adjustable panel width, compact density, and layout outlines.
- Intended workflow: open the file directly in a browser, iterate with Codex, then selectively transfer approved styling and markup to runtime side-panel files.

## Active download integration

- Every rendered `.video-card` in profile, hashtag, and Favorites views receives `↓ Скачать`.
- `VideoDownloadControls.tsx` discovers current card targets and mounts isolated React controls into each card.
- The button sends `DOWNLOAD_VIDEO` to the extension background.
- `lib/download-manager.ts` validates that the URL is HTTPS, belongs to TikTok, and contains `/video/`.
- The background submits `POST http://127.0.0.1:8000/api/jobs` with:
  - `mode: video`;
  - `quality: bestvideo*+bestaudio/best`.
- UI states: idle, sending, queued, and retryable error.
- The integration reuses `oleg3479881328-code/Yt-Dlp-Download-Manager`; no second yt-dlp binary, ffmpeg bundle, native host, or cloud downloader is introduced.

## Working implementation

- WXT Manifest V3 extension with a React side panel.
- Public profile scanning with expanded channel identity, counters, identifiers, flags, locale, timestamps, and analytics.
- Public hashtag scanning with per-account top-N selection and a minimum-view threshold.
- Star and download controls on every video card.
- Durable favorite entries containing both the video snapshot and a channel snapshot.
- Backward-compatible migration of v0.4.0 favorites to partial channel snapshots.
- Automatic channel-snapshot refresh when richer profile information is collected.
- Same-origin public channel enrichment after adding a favorite, without navigating the visible TikTok page.
- Manual `Обновить канал` action as a fallback.
- Favorites grouped by channel with complete channel cards.
- Selected-only standalone HTML grouped by channel.
- HTML escaping and HTTP(S)-only URL validation.
- Atomic Windows one-click updater following `main`.

## Permission boundary

- TikTok pages: `https://www.tiktok.com/*` and `https://tiktok.com/*`.
- Local Download Manager only: `http://127.0.0.1:8000/*`.
- No `<all_urls>`, localhost wildcard, LAN access, remote downloader host, or cloud endpoint.
- Download payloads contain only the direct public video URL and download mode/quality.
- No cookies, tokens, authorization headers, research snapshots, browser profiles, or private traffic are forwarded.

## Product boundaries

- The design stand uses illustrative mock data only and must not be treated as collected TikTok data.
- The design stand does not call the network, `chrome.*`, WXT, React, npm packages, or external fonts.
- TikTok data remains local unless the user explicitly exports it.
- Downloaded media is handled by the separately running local Download Manager.
- TikTok can omit public fields, request verification, change payloads, or expire external preview/avatar URLs.
- No login, CAPTCHA, private-profile, paywall, rate-limit, or access-control bypass.
- No cloud backend, cloud sync, Chrome Web Store submission, or public GitHub Release.

## Validation history

Stable v0.5.0:

- Project Execution OS integrity run `29339387056`: passed.
- TikTok Research Sorter CI run `29339387139`: passed.
- Linux reproducible install, strict TypeScript, all tests, production build, packaging, and artifact upload: passed.
- Windows updater dry-run, full local-source validation, and manifest version check: passed.
- PR #87 merged into `main` as `6a9817c923ed0e531ee7193b8e52ee986b5fe29d`.

Active draft PR #88:

- standalone design document added and structurally checked;
- download-manager client and four unit scenarios added;
- runtime message and background queue handler added;
- exact local host permission added;
- version and packaging moved to `0.6.0`;
- first Linux TypeScript run failed before tests because `useRef` lacked an explicit initial value;
- the TypeScript issue was corrected in `08240ea3e02fde80ac4f1612b7d5e8ec5a9c1a4f`;
- current head requires final green integrity, Linux check/test/build/package, Windows updater, and manifest validation.

## Distribution target

Successful v0.6.0 CI must produce:

- unpacked Chrome MV3 extension;
- `tiktok-research-sorter-extension-v0.6.0.zip`;
- `tiktok-sorter-auto-updater-setup-v0.6.0.zip`;
- `tiktok-research-sorter-source-v0.6.0.zip`.
