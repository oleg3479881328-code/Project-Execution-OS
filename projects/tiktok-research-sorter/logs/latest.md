# Latest Log — TikTok Research Sorter

Date: 2026-07-14
Version: `0.5.0`
Issue: `#86`
Pull request: `#87`
Branch: `main`
Status: integrated and validated

## Delivered

- Expanded public channel parsing for user ID, `secUid`, display name, biography, avatar, verification, website, followers, following, friends, total profile likes, public video count, region, language, account flags, and account creation date.
- Durable channel snapshot attached to every new favorite.
- Backward-compatible migration of v0.4.0 favorites to partial channel snapshots.
- Automatic refresh of favorite channel snapshots when richer public profile data is collected.
- Same-origin public profile enrichment after adding a favorite without navigating the visible TikTok page.
- Manual `Обновить канал` action in Favorites.
- Favorites grouped by channel.
- Complete channel cards in the extension with public counters, identifiers, flags, dates, data source, and locally calculated analytics.
- Selected-only standalone HTML grouped by channel.
- Complete channel card before each channel’s selected videos in HTML.
- HTML includes channel and video links, avatars/previews, descriptions, dates, audio, hashtags, video metrics, channel metrics, source, and timestamps.
- Missing public fields displayed as unavailable instead of being invented.
- Versioned HTML filename and installation artifacts using `v0.5.0`.

## Automated coverage added

- complete public channel payload parsing;
- identifiers, counters, flags, locale, website, and account date;
- preservation of explicit false flags;
- millisecond timestamp normalization;
- unsafe profile website rejection;
- legacy favorite migration to a partial channel snapshot;
- rich channel snapshot creation from a scanned profile;
- richer channel snapshot merging;
- favorite grouping by case-insensitive channel identity;
- selected-only channel-grouped HTML;
- complete channel and video information in HTML;
- channel and video markup escaping;
- rejection of unsafe channel/video/avatar/preview URLs;
- omission of unselected channels and videos.

## Final verification

For PR #87 head `4d12189a5509c9ced21b397d1e5be0d16ed584ab`:

- Project Execution OS integrity run `29339387056`: passed;
- TikTok Research Sorter CI run `29339387139`: passed;
- Linux reproducible install: passed;
- strict TypeScript check: passed;
- all unit and regression tests: passed;
- production Chrome MV3 build: passed;
- versioned packaging and artifact upload: passed;
- Windows zero-side-effect updater dry run: passed;
- Windows full local-source updater validation: passed;
- generated manifest version check: passed.

PR #87 merged into `main` as commit `6a9817c923ed0e531ee7193b8e52ee986b5fe29d`.

## Artifacts

- unpacked Chrome MV3 extension;
- `tiktok-research-sorter-extension-v0.5.0.zip`;
- `tiktok-sorter-auto-updater-setup-v0.5.0.zip`;
- `tiktok-research-sorter-source-v0.5.0.zip`.

The installable extension ZIP was independently inspected: `manifest.json` is at the archive root, it declares version `0.5.0`, the archive contains 10 extension files, and permissions remain `storage`, `sidePanel`, `activeTab`, and `scripting` with TikTok-only host access.

## Product boundary

Only public fields TikTok actually provides are stored. TikTok can omit data, return a verification page, change its payloads, or expire external avatar/preview URLs. The extension does not bypass login, CAPTCHA, private accounts, paywalls, rate limits, or access controls.

## Owner action

None for code implementation, testing, packaging, merge, or repository delivery. The owner only needs to install the provided versioned extension ZIP.
