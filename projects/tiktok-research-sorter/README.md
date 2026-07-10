# TikTok Research Sorter

Local-first Manifest V3 extension for scanning public TikTok profile pages, ranking videos, calculating outlier metrics, and exporting research data.

## Version 0.2.0

- Full profile card with avatar, display name, biography, verification status, followers, following, profile likes, and public video count.
- Scan metadata: last scan, collected coverage, estimated posting frequency, median views, and strongest hashtags.
- Video cards with cover, rank, views, views/day, outlier score, engagement, and hashtags.
- Side Panel interface opened from the extension toolbar.
- User-initiated profile scan with automatic scrolling.
- Hybrid collection from embedded JSON, selected TikTok page requests, and loaded DOM cards.
- Per-profile deduplication and local storage.
- Sorting by views, likes, comments, shares, date, views/day, engagement rate, and outlier score.
- Text/hashtag filters.
- CSV and JSON export.
- CAPTCHA detection without bypass attempts.
- One-click Windows development updater and launcher under `automation/windows/`.

## One-click Windows workflow

Open `automation/windows/README-RU.md` and run:

```text
Install-TikTok-Sorter.cmd
```

The installer creates a desktop shortcut. Every shortcut launch downloads the latest development branch from GitHub, rebuilds the extension, and starts a dedicated persistent Chrome profile with the new build loaded.

## Local development

```bash
npm ci
npm run dev
```

Build and validate:

```bash
npm run check
npm test
npm run build
npm run zip
```

Load `.output/chrome-mv3` through `chrome://extensions` with Developer mode enabled.

## Product boundary

This project analyzes data already visible to the user on a public TikTok profile page. It does not bypass authentication, CAPTCHA, paywalls, or access controls. Data remains local in the browser in the MVP.
