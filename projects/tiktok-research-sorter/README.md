# TikTok Research Sorter

Local-first Manifest V3 extension for scanning public TikTok profile and hashtag pages, ranking videos, saving favorites with channel snapshots, queueing selected videos in the local yt-dlp Download Manager, and exporting selected research.

## Version 0.6.0

### Profile research

- Full profile card with avatar, display name, biography, verification, website, public IDs, region, language, account flags, followers, following, friends, profile likes, and public video count.
- Scan metadata: last scan, profile update time, collected coverage, estimated posting frequency, median views, average engagement, and strongest hashtags.
- Video cards with cover, rank, views, views/day, outlier score, engagement, hashtags, favorite control, and a local download button.
- Sorting, search, outlier filtering, CSV export, and JSON export.

### Hashtag research

Open a public page such as:

```text
https://www.tiktok.com/tag/weddingphotography
```

The side panel automatically detects hashtag mode. Choose:

- how many videos to scan from the hashtag page;
- how many highest-viewed videos to keep from each account: 1, 2, 3, 5, or 10;
- the minimum required view count.

The extension groups discovered videos by account and keeps the requested top videos from each account. Results can be adjusted after scanning because the locally stored hashtag snapshot retains all videos collected during that scan.

Important: hashtag mode ranks videos found on the open hashtag page. It does not silently claim to inspect videos TikTok did not load.

### Download every video card through the existing local manager

Every profile, hashtag, and Favorites video card includes `↓ Скачать`.

The button reuses the established local project `Yt-Dlp-Download-Manager` instead of adding a second downloader:

1. start the local manager at `http://127.0.0.1:8000`;
2. click `↓ Скачать` on a TikTok card;
3. the extension sends the direct public TikTok video URL to `POST /api/jobs`;
4. the existing manager analyzes the URL and queues the best video/audio download;
5. the card displays `Отправляем…`, `✓ В очереди`, or a retryable error.

The integration uses only `http://127.0.0.1:8000/*`. It does not send collected profile research, cookies, tokens, authorization headers, or browser data to the local manager.

### Favorites with complete channel information

Every video card has a star:

- `☆` adds the video to Favorites;
- `★` removes it from Favorites.

When a video is added, the extension stores a durable channel snapshot. It also requests public profile enrichment from the current TikTok tab without navigating away. Existing favorite snapshots are refreshed automatically whenever richer profile data is collected later.

The channel snapshot can contain every supported public field TikTok actually exposes:

- username, display name, avatar, biography, profile link, verification, and website;
- public user ID and `secUid`;
- followers, following, friends, total profile likes, and public video count;
- region, language, private-account flag, commerce-account flag, and account creation date;
- locally collected video count, median views, average engagement, and strongest hashtags;
- collection timestamps and data source.

Unavailable fields are displayed as `—`; values are never invented.

### Selected HTML with channels

Open the `★ Избранное` tab to:

1. review favorites grouped by channel;
2. refresh a channel profile when needed;
3. select videos with checkboxes;
4. select all or clear the current selection;
5. remove selected favorites;
6. download `tiktok-favorites-with-channels-v0.6.0.html`.

The standalone HTML file is suitable for sending to another person. Each channel section contains the full stored channel card followed by only that channel's checked videos. It includes:

- clickable TikTok video and profile links;
- channel avatar, biography, identifiers, public statistics, flags, dates, website, source, and channel analytics;
- preview images when TikTok provides them;
- video descriptions, hashtags, publication dates, audio titles, duration, pinned status, and metrics;
- a responsive and print-friendly layout.

User-controlled text is HTML-escaped, and non-HTTP(S) links or previews are rejected.

### Reliability and safety

- Side Panel interface opened from the extension toolbar.
- User-initiated automatic scrolling with explicit stop, challenge detection, and error recovery.
- Hybrid collection from embedded JSON, selected TikTok page requests, loaded DOM cards, and same-origin public profile enrichment.
- Serialized local persistence to prevent lost updates.
- Backward-compatible migration adds channel snapshots to existing favorites.
- Strict data-source precedence: API → embedded JSON → DOM fallback.
- CSV export with spreadsheet-formula protection.
- HTML export with markup escaping and URL protocol validation.
- Direct download requests accept only HTTPS TikTok `/video/` URLs.
- No login, CAPTCHA, private-profile, rate-limit, paywall, or access-control bypass.
- Host access remains limited to TikTok plus the exact local Download Manager endpoint `127.0.0.1:8000`.

## One-click Windows workflow

Open `automation/windows/README-RU.md` and run:

```text
Install-TikTok-Sorter.cmd
```

The installer creates a desktop shortcut. Every shortcut launch downloads `main`, builds in an isolated candidate directory, runs checks and tests, validates the generated manifest, preserves the current build on failure, keeps one previous build for rollback, and starts a dedicated persistent Chrome profile only after success.

Supported automation parameters:

```powershell
-DryRun
-SkipLaunch
-NonInteractive
-LocalSource <path>
```

## Local development

```bash
npm ci
npm run check
npm test
npm run build
npm run zip
```

Load `.output/chrome-mv3` through `chrome://extensions` with Developer mode enabled.

## CI artifacts

Each successful branch or pull-request run uploads versioned files:

- unpacked Chrome MV3 extension;
- `tiktok-research-sorter-extension-v0.6.0.zip`;
- `tiktok-sorter-auto-updater-setup-v0.6.0.zip`;
- `tiktok-research-sorter-source-v0.6.0.zip`.

## Product boundary

The project stores only public data TikTok makes available to the current browser session. TikTok can omit fields, request verification, change payloads, or expire external preview URLs. Missing fields remain unavailable rather than being inferred. Video downloading is delegated to the owner's existing local `Yt-Dlp-Download-Manager`; the extension does not embed yt-dlp, ffmpeg, a cloud downloader, or remote executable code.
