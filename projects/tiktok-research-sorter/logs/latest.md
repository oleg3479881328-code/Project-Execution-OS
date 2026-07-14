# Latest Log — TikTok Research Sorter

Date: 2026-07-14
Version: `0.6.0` draft
Issue: none
Pull request: `#88` draft
Branch: `agent/tiktok-design-preview`
Status: design preview and per-card local download integration implemented; final CI validation in progress

## Delivered in the active branch

### Standalone design stand

- Added `design/sidepanel-design-preview.html` as a self-contained browser page for visual iteration with Codex.
- Reproduced profile analysis, hashtag research, and Favorites grouped by channel.
- Added representative mock data, width presets, continuous width control, compact density, and layout outlines.
- Kept the stand independent from WXT, React, Chrome APIs, npm runtime, network requests, and external assets.

### Download button on every TikTok video card

- Added `↓ Скачать` to profile, hashtag, and Favorites cards through `VideoDownloadControls.tsx`.
- Added visible states:
  - `Отправляем…`;
  - `✓ В очереди`;
  - retry after a displayed error.
- Added `DOWNLOAD_VIDEO` to the typed runtime-message contract.
- Added a background handler that delegates downloads to the existing local manager.
- Added `lib/download-manager.ts` with strict direct-video URL validation.
- Added the exact queue request used by the established manager:

```json
{
  "url": "https://www.tiktok.com/@creator/video/...",
  "mode": "video",
  "quality": "bestvideo*+bestaudio/best"
}
```

- Queue endpoint: `POST http://127.0.0.1:8000/api/jobs`.
- Reused `oleg3479881328-code/Yt-Dlp-Download-Manager`; did not duplicate yt-dlp, ffmpeg, native-host binaries, settings, history, or download logic.

## Permission change

Added only:

```text
http://127.0.0.1:8000/*
```

Reason: the MV3 background service worker must send the user-clicked public TikTok video URL to the owner’s local Download Manager queue.

Not added:

- `<all_urls>`;
- localhost or LAN wildcards;
- cloud endpoints;
- remote executable code;
- cookie, token, authorization-header, or browser-profile access.

## Tests added

`tests/download-manager.test.ts` covers:

- a valid TikTok `/video/` URL and the exact local queue request;
- rejection of non-TikTok and non-video URLs before network access;
- propagation of Download Manager API error details;
- actionable error text when the local manager is not running.

## Version and packaging

- `APP_VERSION`: `0.6.0`.
- WXT manifest version: `0.6.0`.
- package version: `0.6.0`.
- CI package and artifact names moved to `v0.6.0`.
- Windows manifest validation now expects `0.6.0`.

## Validation history

Stable v0.5.0 remains merged in `main` as `6a9817c923ed0e531ee7193b8e52ee986b5fe29d` with its original green validation baseline.

For active PR #88:

- Project OS integrity passed on the first runtime-download head.
- The first Linux run stopped at TypeScript before tests and build because `useRef` was created without an explicit initial value.
- The error was corrected in commit `08240ea3e02fde80ac4f1612b7d5e8ec5a9c1a4f`.
- Workflow packaging and manifest expectations were then updated from `0.5.0` to `0.6.0`.
- Final acceptance remains conditional on green integrity, Linux TypeScript/tests/build/package, Windows updater validation, and generated manifest inspection.

## Runtime boundary

- The local Download Manager must be running at `http://127.0.0.1:8000` when the user clicks Download.
- Only direct public HTTPS TikTok URLs containing `/video/` are accepted.
- A failed local connection stays visible on the card and can be retried.
- The research database and channel snapshots remain independent from downloaded media.

## Owner action after green CI

Install or update the v0.6.0 extension build, start the existing `Yt-Dlp-Download-Manager`, and click `↓ Скачать` on any scanned video card.
