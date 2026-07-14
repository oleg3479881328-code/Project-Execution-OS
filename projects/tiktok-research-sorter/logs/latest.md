# Latest Log — TikTok Research Sorter

Date: 2026-07-14
Version: `0.6.0` validated draft
Issue: none
Pull request: `#88` draft
Branch: `agent/tiktok-design-preview`
Status: design preview and per-card local download integration implemented and automated validation green

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
- Kept controls attached across React rerenders by comparing both card identity and the current DOM mount slot.
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

The existing HTML-export regression was advanced from `v0.5.0` to `v0.6.0`.

## Version and packaging

- `APP_VERSION`: `0.6.0`.
- WXT manifest version: `0.6.0`.
- package version: `0.6.0`.
- CI package and artifact names: `v0.6.0`.
- Windows manifest validation expects `0.6.0`.

## Validation result

Validated runtime head: `1a916679fd35bb00de14ac4d8423102f2038b7b8`.

- Project OS integrity run `29352113915`: passed.
- TikTok Research Sorter CI run `29352115086`: passed.
- Linux reproducible dependency install: passed.
- strict TypeScript: passed.
- all unit and regression tests: passed.
- production Chrome MV3 build: passed.
- v0.6.0 packaging: passed.
- unpacked extension upload: passed.
- packaged artifacts upload: passed.
- Windows updater dry run: passed.
- Windows full local-source validation: passed.
- generated manifest version `0.6.0`: passed.

Errors found and resolved during validation:

1. `useRef` required an explicit initial value under the current React type definitions.
2. The HTML-export regression still expected version `0.5.0` after the intentional version bump.

Both fixes are included and the subsequent full validation is green.

## Runtime boundary

- The local Download Manager must be running at `http://127.0.0.1:8000` when the user clicks Download.
- Only direct public HTTPS TikTok URLs containing `/video/` are accepted.
- A failed local connection stays visible on the card and can be retried.
- The research database and channel snapshots remain independent from downloaded media.

## Remaining owner smoke test

Install the v0.6.0 extension build, start the existing `Yt-Dlp-Download-Manager`, click `↓ Скачать` on profile, hashtag, and Favorites cards, and confirm that each creates the expected local queue job and downloaded file.
