# TikTok Research Sorter

Local-first Manifest V3 extension for scanning public TikTok profile pages, ranking videos, calculating outlier metrics, and exporting research data.

## Current MVP

- Side Panel interface opened from the extension toolbar.
- User-initiated profile scan with automatic scrolling.
- Hybrid collection from embedded JSON, TikTok page requests, and loaded DOM cards.
- Per-profile deduplication and local storage.
- Sorting by views, likes, comments, shares, date, views/day, engagement rate, and outlier score.
- Text/hashtag filters.
- CSV and JSON export.
- CAPTCHA detection without bypass attempts.

## Local development

```bash
npm install
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
