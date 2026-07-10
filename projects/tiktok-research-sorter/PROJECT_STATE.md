# PROJECT STATE — TikTok Research Sorter

## State

- Status: `active / transfer-ready MVP implementation`
- Phase: `desktop browser validation`
- Branch: `agent/tiktok-research-sorter-mvp`
- Storage layer: internal subproject in the parent Project Execution OS Git repository

## Working Implementation

- WXT Manifest V3 extension
- React side panel
- MAIN-world fetch/XHR observation for selected TikTok JSON responses
- isolated content-script collector
- controlled auto-scroll with stop and challenge detection
- heuristic TikTok payload adapter
- embedded-state and DOM fallback
- per-profile deduplication
- `chrome.storage.local` persistence
- views, velocity, engagement, and outlier analytics
- text and outlier filters
- CSV and JSON export
- unit tests for number parsing, parser normalization, and analytics

## Validation Status

- Dependency installation: complete
- TypeScript check: passed
- Unit tests: passed — 5 tests
- WXT production build: passed — Chrome MV3 bundle approximately 219 KB
- ZIP build: passed — approximately 72 KB
- Runtime dependency audit: passed — 0 known vulnerabilities
- Full development-tool audit: 8 transitive advisories, currently through WXT browser-runner tooling; review before publication
- Real TikTok profile smoke test: not possible from the current connector environment; must be performed in desktop Chrome
- Generated `package-lock.json`: exists in the local validated workspace but could not be uploaded through the current GitHub connector

## Known Risks

1. TikTok can change API paths and payload shapes.
2. Fetch/XHR interception begins at `document_start`, but page/CSP behavior must be tested in Chrome.
3. DOM view-count fallback depends on TikTok’s current markup.
4. `chrome.storage.local` is suitable for the MVP but may require IndexedDB if history snapshots or very large datasets are added.
5. A public release requires current TikTok terms and Chrome Web Store policy review.
6. Development-only transitive dependency advisories must be rechecked after WXT updates.

## Next Action

Run the unpacked extension against a small profile and a large profile by following `docs/IMPLEMENTATION_HANDOFF.md`. Capture only sanitized JSON fixtures for parser failures, add regression tests, commit the generated lock file, and report whether the branch is ready to merge.
