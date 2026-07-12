# Latest Log — TikTok Research Sorter

Date: 2026-07-12
Version: `0.2.0`
Status: integrated into `main`; automatic updater follows `main`

## Completed

- Full TikTok profile and video research interface.
- Serialized background persistence and stale-scan recovery.
- API → embedded JSON → DOM source precedence.
- Corrected analytics, localized count parsing, duration normalization, and CSV formula safety.
- Atomic Windows updater with candidate build, validation, rollback, dedicated Chrome profile, and non-interactive CI mode.
- 40 unit and regression tests.
- Linux and Windows GitHub Actions validation.
- Automatic unpacked extension, extension ZIP, updater ZIP, and source ZIP artifacts.
- Project Execution OS structure and context-manifest integrity validation.
- PR #71 merged into `main`.
- Updater default branch changed from the development branch to `main`.

## Final automated verification

- Project Execution OS structure validation: passed.
- System-context manifest validation: passed.
- Linux reproducible install: passed.
- TypeScript strict check: passed.
- 40 tests: passed.
- Chrome MV3 production build: passed.
- Packaging and artifact upload: passed.
- Windows zero-side-effect dry run: passed.
- Windows full updater validation: passed.
- Generated manifest version check: passed.

## Distribution behavior

The desktop shortcut now downloads `main`, validates the candidate build, preserves the active build on failure, retains one previous version, and launches the dedicated persistent Chrome profile only after success.

## Remaining boundaries

- No Chrome Web Store submission is authorized.
- No public GitHub Release is authorized.
- TikTok can change its public APIs and DOM.
- IndexedDB remains a future scaling option for very large datasets.

## Owner action

None for installation updates, code validation, packaging, or repository integration.
