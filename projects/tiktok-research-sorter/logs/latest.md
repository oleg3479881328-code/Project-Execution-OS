# Latest Log — TikTok Research Sorter

Date: 2026-07-14
Version: `0.5.0`
Issue: `#86`
Pull request: `#87`
Branch: `agent/tiktok-research-sorter-channel-export-v0.5.0`
Status: implementation complete; final GitHub validation pending

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

## Product boundary

Only public fields TikTok actually provides are stored. TikTok can omit data, return a verification page, change its payloads, or expire external avatar/preview URLs. The extension does not bypass login, CAPTCHA, private accounts, paywalls, rate limits, or access controls.

## Pending final evidence

- Project Execution OS integrity CI;
- Linux reproducible install, strict TypeScript, all tests, build, packaging, and artifact upload;
- Windows updater dry-run, full local-source validation, and manifest version check;
- installable v0.5.0 ZIP inspection;
- PR #87 merge into `main`.

## Owner action

None during implementation and automated validation.
