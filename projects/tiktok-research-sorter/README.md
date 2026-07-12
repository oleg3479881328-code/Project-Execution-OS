# TikTok Research Sorter

Local-first Manifest V3 extension for scanning public TikTok profile pages, ranking videos, calculating outlier metrics, and exporting research data.

## Version 0.2.0

- Full profile card with avatar, display name, biography, verification status, followers, following, profile likes, and public video count.
- Scan metadata: last scan, collected coverage, estimated posting frequency, median views, and strongest hashtags.
- Video cards with cover, rank, views, views/day, outlier score, engagement, and hashtags.
- Side Panel interface opened from the extension toolbar.
- User-initiated profile scan with automatic scrolling and explicit stop/error recovery.
- Hybrid collection from embedded JSON, selected TikTok page requests, and loaded DOM cards.
- Serialized per-profile persistence to prevent lost updates.
- Strict data-source precedence: API → embedded JSON → DOM fallback.
- Sorting by views, likes, comments, shares, date, views/day, engagement rate, and outlier score.
- Text/hashtag filters.
- CSV and JSON export with spreadsheet-formula protection.
- CAPTCHA detection without bypass attempts.
- One-click Windows updater and launcher under `automation/windows/`.
- 40 automated tests covering parser, profile extraction, analytics, localized numbers, merge logic, duration normalization, cyclic payloads, and CSV safety.
- Linux CI for TypeScript, tests, production build, and downloadable packages.
- Windows CI for zero-side-effect dry run and full updater validation.

## One-click Windows workflow

Open `automation/windows/README-RU.md` and run:

```text
Install-TikTok-Sorter.cmd
```

The installer creates a desktop shortcut. Every shortcut launch:

1. downloads or reads the selected source;
2. builds in an isolated candidate directory;
3. runs TypeScript checks and unit tests;
4. validates the generated manifest;
5. replaces the active build only after all checks pass;
6. preserves the previous build for rollback;
7. starts a dedicated persistent Chrome profile.

Supported test and automation parameters:

```powershell
-DryRun
-SkipLaunch
-NonInteractive
-LocalSource <path>
```

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

## CI artifacts

Each successful branch or pull-request run uploads:

- unpacked Chrome MV3 extension;
- `tiktok-research-sorter-extension-0.2.0.zip`;
- `tiktok-sorter-auto-updater-setup-0.2.0.zip`;
- `tiktok-research-sorter-source-0.2.0.zip`.

## Product boundary

This project analyzes data already visible to the user on a public TikTok profile page. It does not bypass authentication, CAPTCHA, paywalls, private profiles, rate limits, or access controls. Data remains local in the browser unless the user explicitly exports it.
