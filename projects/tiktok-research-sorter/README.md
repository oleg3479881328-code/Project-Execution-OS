# TikTok Research Sorter

Local-first Manifest V3 extension for scanning public TikTok profile pages and public TikTok hashtag pages, ranking videos, and exporting research data.

## Version 0.3.0

### Profile research

- Full profile card with avatar, display name, biography, verification status, followers, following, profile likes, and public video count.
- Scan metadata: last scan, collected coverage, estimated posting frequency, median views, and strongest hashtags.
- Video cards with cover, rank, views, views/day, outlier score, engagement, and hashtags.
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

Important: hashtag mode ranks videos found on the open hashtag page. It does not silently visit every creator profile or claim to inspect videos that TikTok did not load.

### Reliability and safety

- Side Panel interface opened from the extension toolbar.
- User-initiated automatic scrolling with explicit stop, challenge detection, and error recovery.
- Hybrid collection from embedded JSON, selected TikTok page requests, and loaded DOM cards.
- Serialized local persistence to prevent lost updates.
- Strict data-source precedence: API → embedded JSON → DOM fallback.
- CSV export with spreadsheet-formula protection.
- No login, CAPTCHA, private-profile, rate-limit, paywall, or access-control bypass.
- Host permissions remain limited to TikTok.

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
- `tiktok-research-sorter-extension-v0.3.0.zip`;
- `tiktok-sorter-auto-updater-setup-v0.3.0.zip`;
- `tiktok-research-sorter-source-v0.3.0.zip`.

## Product boundary

This project analyzes data already visible to the user on public TikTok pages. Data remains local in the browser unless the user explicitly exports it. TikTok can change public payloads and page structure, so platform parsing remains isolated and regression-tested.
