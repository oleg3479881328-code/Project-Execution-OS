# TikTok Research Sorter — Project State

## Version
0.2.0 — стабилизирован, все Phases 1–6 выполнены.

## Stack
- WXT 0.20.27 + TypeScript 5.8.3 + React 19.2.7
- Vitest 4.1.10
- Manifest V3
- chrome.storage.local

## Architecture
MAIN-world page hook → window.postMessage → isolated content script → background SW → chrome.storage.local → React side panel

## Test Coverage
**35 tests** (7 files), all passing:
- `tests/numbers.test.ts` — 2 tests (compact number parsing)
- `tests/analytics.test.ts` — 2 tests (median, outlier score)
- `tests/parser.test.ts` — 1 test (basic payload extraction)
- `tests/profile.test.ts` — 1 test (basic profile extraction)
- `tests/profile-analytics.test.ts` — 2 tests (posting frequency, hashtag ranking)
- `tests/parser-regression.test.ts` — 15 tests (fixtures, edge cases, cyclic refs, pinned, alternate fields)
- `tests/profile-regression.test.ts` — 12 tests (profile extraction, merge logic, edge cases)

## Fixtures
`tests/fixtures/` contains 7 JSON files for reproducible regression testing:
- `basic-video-list.json`
- `profile-user-info.json`
- `empty-item-list.json`
- `null-payload.json`
- `missing-fields.json`
- `cyclic-payload.json`
- `pinned-video.json`
- `alternate-field-names.json`

## CI
GitHub Actions workflow: `.github/workflows/tiktok-research-sorter-ci.yml`
- Triggers on push/PR to `main` and `agent/**` branches
- Steps: npm ci → tsc --noEmit → npm test → npm run build → upload artifact
- On `main` branch: also packages as ZIP

## Windows Updater
`automation/windows/Update-and-Launch-TikTok-Sorter.ps1`
- New testability flags: `-DryRun`, `-SkipLaunch`, `-LocalSource`
- Environment variable support: `$env:TRS_GITHUB_BRANCH`, `$env:TRS_LOCAL_SOURCE`

## Hardening (Phase 2)
- MAX_VISITS (50,000) guard against cyclic payloads
- Localized DOM selectors for TikTok in different locales
- Multi-language pinned detection (EN, RU, FR, DE)
- DASHBOARD_UPDATED type added to RuntimeMessage union
- Alternate field name support (`aweme_id`, `authorInfo`, `video_info`, `statistics`, etc.)

## Build Output
- Production build: ~229 KB (`.output/chrome-mv3/`)
- ZIP packaging available via `npm run zip`

## Branch
`agent/tiktok-research-sorter-mvp`
