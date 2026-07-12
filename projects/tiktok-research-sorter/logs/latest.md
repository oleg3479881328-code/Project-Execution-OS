# Latest Log — TikTok Research Sorter

Date: 2026-07-12
Branch: `agent/tiktok-research-sorter-mvp`
Version: `0.2.0`
Status: reviewer stabilization complete; final pull-request evidence refresh in progress

## Implemented

- Full TikTok profile card and video-card research interface.
- Serialized background mutations so concurrent profile, video, and scan-state messages cannot overwrite each other.
- Automatic stale-scan recovery and guaranteed content-script cleanup through `try/catch/finally`.
- Strict source priority: API data takes precedence over embedded JSON, which takes precedence over DOM fallback.
- Narrower DOM selectors and HTTP(S)-only external profile/media URLs.
- Corrected publication-frequency and average-engagement calculations.
- Localized number parsing for decimal commas and Russian compact suffixes.
- Safer duration normalization for seconds versus milliseconds.
- CSV spreadsheet-formula neutralization.
- Atomic Windows updater:
  - builds in an isolated candidate directory;
  - runs reproducible dependency installation, TypeScript checks, tests, build, and manifest validation;
  - replaces the active build only after success;
  - preserves one previous version for rollback;
  - supports `DryRun`, `SkipLaunch`, `NonInteractive`, and `LocalSource`;
  - closes only the dedicated Chrome profile.
- Linux and Windows GitHub Actions validation.
- Automatic extension, updater, and source packages.
- Project Execution OS manifest and project-state integrity restored.

## Automated verification

The latest code-bearing validation completed successfully in GitHub Actions:

- Project Execution OS structure and system-context manifest: passed.
- Linux reproducible install: passed.
- TypeScript strict check: passed.
- 40 unit and regression tests: passed.
- Chrome MV3 production build: passed.
- Extension and package artifact upload: passed.
- Windows zero-side-effect dry run: passed.
- Windows full updater validation with local source and no browser launch: passed.
- Generated manifest version check: passed.

## Generated packages

- `tiktok-research-sorter-extension-0.2.0.zip`
- `tiktok-sorter-auto-updater-setup-0.2.0.zip`
- `tiktok-research-sorter-source-0.2.0.zip`
- unpacked Chrome MV3 build artifact

## Remaining boundaries

- No Chrome Web Store submission has been authorized.
- No public GitHub Release has been created.
- The updater intentionally follows `agent/tiktok-research-sorter-mvp` until the project is merged; switching it to `main` must happen only after merge.
- TikTok can still change public payloads or DOM structure; fixture coverage and graceful fallbacks reduce but cannot eliminate that external risk.
- Very large multi-profile datasets may eventually require IndexedDB instead of `chrome.storage.local`.

## Owner action

None for stabilization, CI, packaging, or evidence collection.

## Next repository action

Refresh the pull-request report against the final head, confirm all checks and artifacts, and then decide the separate merge gate. Do not publish externally.
