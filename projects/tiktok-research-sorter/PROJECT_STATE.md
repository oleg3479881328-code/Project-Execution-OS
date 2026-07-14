---
project_mode: internal
status: active
version: 0.5.0
branch: agent/tiktok-research-sorter-channel-export-v0.5.0
active_issue: 86
pull_request: 87
---

# TikTok Research Sorter — Project State

## Current phase

Version 0.5.0 adds complete public channel snapshots to Favorites and selected HTML exports while preserving the profile, hashtag, favorites, and checkbox-selection workflows. PR #87 is under final automated validation before integration into `main`.

## Working implementation

- WXT Manifest V3 extension with a React side panel.
- Public profile scanning with expanded channel identity, counters, identifiers, flags, locale, timestamps, and analytics.
- Public hashtag scanning with per-account top-N selection and a minimum-view threshold.
- A star control on every video card.
- Durable favorite entries containing both the video snapshot and a channel snapshot.
- Backward-compatible migration of v0.4.0 favorites to partial channel snapshots.
- Automatic channel-snapshot refresh when richer profile information is collected.
- Same-origin public channel enrichment after adding a favorite, without navigating the visible TikTok page.
- Manual `Обновить канал` action as a fallback.
- Favorites grouped by channel with complete channel cards.
- Selected-only standalone HTML grouped by channel.
- Channel HTML includes identity, public IDs, counters, flags, locale, dates, website, source, channel analytics, links, and selected videos.
- HTML escaping and HTTP(S)-only URL validation.
- Atomic Windows one-click updater following `main` after merge.

## Supported public channel fields

- username, profile URL, display name, avatar, biography, verification, and website;
- public user ID and `secUid`;
- followers, following, friends, total profile likes, and public video count;
- region, language, private-account flag, commerce-account flag, and account creation date;
- locally collected video count, median views, average engagement, and strongest hashtags;
- collection/update timestamps and data source.

Missing fields remain unavailable and are never inferred.

## Boundaries

- Data remains local unless the user explicitly exports it.
- TikTok can omit public fields, request verification, change payloads, or expire external preview/avatar URLs.
- Public channel enrichment uses the existing TikTok host permission and does not navigate the visible page.
- No login, CAPTCHA, private-profile, paywall, rate-limit, or access-control bypass.
- No additional host permissions beyond TikTok.
- No backend, cloud sync, Chrome Web Store submission, or public GitHub Release.

## Validation status

Implementation and regression coverage are committed on PR #87. Final evidence still required:

- Project Execution OS integrity validation;
- Linux reproducible install, TypeScript, all tests, production build, packaging, and artifact upload;
- Windows updater dry-run, full local-source validation, and manifest version check;
- installable extension ZIP inspection;
- PR merge into `main`.

## Distribution target

Successful v0.5.0 CI must produce:

- unpacked Chrome MV3 extension;
- `tiktok-research-sorter-extension-v0.5.0.zip`;
- `tiktok-sorter-auto-updater-setup-v0.5.0.zip`;
- `tiktok-research-sorter-source-v0.5.0.zip`.
