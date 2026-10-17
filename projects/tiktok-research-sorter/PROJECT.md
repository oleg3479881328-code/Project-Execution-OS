# PROJECT — TikTok Research Sorter

## 1. Project

- Project name: `TikTok Research Sorter`
- Project type: `Chrome Extension / local social-content research tool`
- Current version: `0.6.0`
- Short description: a Manifest V3 browser extension that scans public TikTok profile and hashtag pages, stores research locally, ranks videos, saves favorites with durable channel snapshots, queues individual public video URLs in the owner’s existing local `Yt-Dlp-Download-Manager`, and exports selected channel-and-video shortlists as standalone HTML.

## 2. Purpose

Supported workflows:

```text
public profile -> scan loaded profile videos + public channel data -> metrics -> filter/sort -> favorite/download/export
public hashtag -> scan loaded hashtag videos -> group by account -> top N + minimum views -> favorite/download
favorite -> preserve video + channel snapshot -> enrich/refresh channel data -> download when needed
favorites -> checkbox selection -> channel-grouped standalone HTML -> send as a file
video card -> direct public TikTok video URL -> local 127.0.0.1 Download Manager queue -> yt-dlp download
```

Primary users:

- short-form video researchers;
- creators and agencies;
- local-business marketers;
- the owner’s TikTok and Reels research workflows.

## 3. Source of truth

- Durable source: `projects/tiktok-research-sorter/` inside `oleg3479881328-code/Project-Execution-OS`.
- Stable implementation and distribution branch: `main`.
- Version 0.5.0 delivery issue: `#86`.
- Version 0.5.0 pull request: `#87`.
- Version 0.6.0 design and download integration pull request: `#88`.

## 4. Architecture

```text
TikTok public page
→ selected fetch/XHR payload observer + embedded JSON + DOM fallback
→ optional same-origin public profile enrichment
→ isolated content script
→ serialized background persistence
→ chrome.storage.local profiles + hashtag snapshots + favorite video/channel snapshots
→ React side panel grouped by channel
→ per-card DOWNLOAD_VIDEO runtime message
→ strict TikTok video URL validation
→ POST http://127.0.0.1:8000/api/jobs
→ existing local Yt-Dlp-Download-Manager queue
→ CSV / JSON / channel-grouped standalone HTML export
```

## 5. Current status

- Mode: `active development / draft PR #88`.
- Stable base: `v0.5.0 complete public channel information` in `main`.
- Active phase: `v0.6.0 standalone design preview + per-card local download integration`.
- Runtime change: every video card in profile, hashtag, and Favorites surfaces receives a download control with sending, queued, and retryable error states.

## 6. Key decisions and constraints

- Stack: `WXT + TypeScript + React + Manifest V3`.
- No cloud backend, accounts, AI calls, payments, remote executable code, or cloud sync.
- TikTok host access remains limited to TikTok.
- The only additional host permission is the exact owner-local manager origin `http://127.0.0.1:8000/*`.
- Downloads reuse `oleg3479881328-code/Yt-Dlp-Download-Manager`; yt-dlp and ffmpeg are not duplicated inside this extension.
- Only direct HTTPS TikTok URLs containing `/video/` are accepted for queueing.
- A download request contains the video URL, mode `video`, and the existing manager quality expression; it does not include cookies, tokens, channel snapshots, research databases, or browser profiles.
- The local manager must already be running at `127.0.0.1:8000`.
- Do not bypass login, private accounts, CAPTCHA, rate limits, paywalls, or access controls.
- Prefer structured JSON payloads; DOM selectors are fallback only.
- Store only fields TikTok actually returns; display missing values as unavailable.
- Favorites are durable local snapshots independent of profile and hashtag deletion.
- Existing favorite channel snapshots are refreshed only when richer public data becomes available.
- Same-origin profile enrichment must not navigate the visible page.
- HTML exports include only checked favorites and group them by channel.
- HTML text is escaped and external URLs are restricted to HTTP(S).
- Exported avatars and previews remain dependent on external URLs remaining available.
- Preserve only sanitized fixtures. Never commit cookies, tokens, authorization headers, browser profiles, signatures, or raw identifying traffic.
- Keep generated deliverables and exports versioned.

## 7. Validation baseline

Stable v0.5.0:

- Project Execution OS integrity validation passed.
- Linux reproducible install, strict TypeScript check, all tests, production build, versioned packaging, and artifact upload passed.
- Windows updater dry-run, full local-source validation, and manifest check passed.
- PR #87 merged into `main` as `6a9817c923ed0e531ee7193b8e52ee986b5fe29d`.

Active v0.6.0 validation:

- unit coverage added for valid queue requests, invalid URL rejection, API errors, and unavailable local manager errors;
- Project OS integrity and full TikTok Research Sorter CI run automatically for each current PR head;
- the first TypeScript run exposed a missing `useRef` initial value and was corrected in commit `08240ea3e02fde80ac4f1612b7d5e8ec5a9c1a4f`;
- final acceptance requires green TypeScript, tests, production build, packaging, Windows updater validation, and manifest version `0.6.0`.

## 8. Read next

1. `PROJECT_STATE.md`
2. `logs/latest.md`
3. `README.md`
4. `design/sidepanel-design-preview.html`
5. `lib/download-manager.ts`
6. `entrypoints/sidepanel/VideoDownloadControls.tsx`
7. `coordination/CHANNEL_PROFILE_EXPORT_V0.5.0.md`
