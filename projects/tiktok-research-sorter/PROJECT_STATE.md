# PROJECT STATE — TikTok Research Sorter

## State

- Status: `active / version 0.2.0 ready for owner validation`
- Phase: `profile-card and one-click updater validation`
- Branch: `agent/tiktok-research-sorter-mvp`
- Storage layer: internal subproject in the parent Project Execution OS Git repository

## Working Implementation

- WXT Manifest V3 extension
- React side panel
- full profile card with avatar, display name, bio, verification status, followers, following, profile likes, and video count
- profile insights: last scan, collection coverage, estimated posting frequency, median views, and strongest hashtags
- video cards with cover, rank, views, velocity, engagement, and outlier score
- MAIN-world observation limited to selected TikTok JSON responses
- embedded-state and DOM fallback
- controlled auto-scroll with stop and challenge detection
- per-profile deduplication and `chrome.storage.local` persistence
- CSV and JSON export
- one-click Windows updater that downloads the current GitHub branch, rebuilds, and opens a dedicated persistent Chrome profile

## Validation Status

- Owner confirmed version `0.1.1` installs, connects to TikTok, and starts successfully on a public profile.
- CSP-related global XHR interception was corrected before version `0.2.0`.
- TypeScript check for `0.2.0`: passed.
- Unit tests: passed — 8 tests across 5 files.
- WXT Chrome MV3 production build: passed — approximately 229 KB.
- ZIP build: passed — approximately 74 KB.
- Profile parser, publication-frequency calculation, and strong-hashtag ranking have regression tests.
- Windows updater scripts are implemented and packaged but have not yet been executed on the owner's Windows computer.
- Full profile-card extraction against the owner's live TikTok profile still requires owner validation.

## Known Risks

1. TikTok can change API paths, payload shapes, and DOM selectors.
2. Some profile fields may be unavailable on localized or logged-out TikTok pages; the card must degrade gracefully.
3. Posting frequency requires known video publication timestamps and may remain blank when TikTok exposes only DOM cards.
4. The development updater currently follows `agent/tiktok-research-sorter-mvp`; change it to `main` after merge.
5. The branch is behind the current `main` and must be updated before merging.
6. Public release still requires current TikTok terms and Chrome Web Store policy review.

## Next Action

Install the packaged Windows updater, launch the dedicated Chrome profile, scan `@jasminebrookephotography`, and verify every profile-card field. Record any blank or incorrect field and capture only sanitized evidence needed to harden the parser.
