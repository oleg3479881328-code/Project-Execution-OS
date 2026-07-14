# Latest Log — TikTok Research Sorter

Date: 2026-07-14
Version: `0.4.0`
Issue: `#84`
Pull request: `#85`
Branch: `main`
Status: integrated and validated

## Delivered

- Star control on every profile and hashtag video card.
- Durable Favorites storage independent from scanned profile and hashtag data.
- Dedicated Favorites tab with live favorite count.
- Checkbox selection of favorite videos.
- Select all, clear selection, remove selected, and individual favorite removal.
- Standalone HTML generation from only the checked favorites.
- HTML cards with clickable video/profile links, descriptions, preview images, dates, audio titles, hashtags, and available metrics.
- Responsive and print-friendly HTML layout suitable for sending as a file.
- HTML escaping for user-controlled text and HTTP(S)-only external URL validation.
- Backward-compatible dashboard migration for existing v0.3.0 installations.
- Versioned exports and installation artifacts using `v0.4.0`.

## Automated coverage added

- stable case-insensitive favorite keys;
- newest-first favorite ordering;
- selected-only favorite extraction;
- standalone HTML structure and version metadata;
- inclusion of links, previews, descriptions, and metrics;
- markup/script escaping;
- rejection of `javascript:` and `data:` URLs;
- omission of unselected favorites from generated HTML.

## Final verification

For PR #85 head `eb3328251cb256164237baefb66b25b449d222cb`:

- Project Execution OS integrity run `29333836074`: passed;
- TikTok Research Sorter CI run `29333836128`: passed;
- Linux reproducible install: passed;
- strict TypeScript check: passed;
- all unit and regression tests: passed;
- production Chrome MV3 build: passed;
- versioned packaging and artifact upload: passed;
- Windows zero-side-effect updater dry run: passed;
- Windows full local-source updater validation: passed;
- generated manifest version check: passed.

PR #85 merged into `main` as commit `92f66e3fea0b96f30dfad8dc0de7aff5e1a5c696`.

## Artifacts

- unpacked Chrome MV3 extension;
- `tiktok-research-sorter-extension-v0.4.0.zip`;
- `tiktok-sorter-auto-updater-setup-v0.4.0.zip`;
- `tiktok-research-sorter-source-v0.4.0.zip`.

The installable extension ZIP was separately inspected: `manifest.json` is at the archive root, the archive contains 10 extension files, and the manifest declares version `0.4.0`.

## Product boundary

The exported HTML is a local static file. Video and profile links point to public TikTok pages, and preview images use the public image URLs captured during scanning. TikTok can later expire those preview URLs. No TikTok access controls are bypassed.

## Owner action

None for code implementation, testing, packaging, merge, or repository delivery. The owner only needs to install the provided versioned extension ZIP.
