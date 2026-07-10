# PROJECT STATE — TikTok Research Sorter

## State

- Status: `active / transfer-ready MVP scaffold`
- Phase: `browser validation`
- Branch: `agent/tiktok-research-sorter-mvp`
- Storage layer: internal subproject in the parent Project Execution OS Git repository

## Working Implementation

- WXT Manifest V3 extension
- React side panel
- MAIN-world fetch/XHR observation
- isolated content-script collector
- controlled auto-scroll with stop and challenge detection
- heuristic TikTok payload adapter
- DOM fallback
- IndexedDB persistence
- views, velocity, engagement, and outlier analytics
- CSV and JSON export
- unit tests for parser and analytics

## Validation Status

- Dependency installation: complete
- TypeScript check: passed
- Unit tests: passed — 4 tests
- WXT production build: passed — Chrome MV3 bundle about 218 KB
- Real TikTok profile smoke test: not possible from the current GitHub connector environment; must be performed in desktop Chrome

## Known Risks

1. TikTok can change API paths and payload shapes.
2. Fetch/XHR interception begins at `document_start`, but page or CSP behavior must be tested in Chrome.
3. DOM view-count fallback depends on TikTok’s current markup.
4. A public release requires current TikTok terms and Chrome Web Store policy review.
5. Runtime dependency audit is clean. Development tooling still reports transitive advisories through WXT/web-ext-run and must be rechecked before publication.

## Next Action

Run the unpacked extension against a small profile and a large profile. Capture only sanitized JSON fixtures for parser failures, then harden the adapter and add regression tests.
