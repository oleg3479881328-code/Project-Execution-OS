# PROJECT — TikTok Research Sorter

## 1. Project

- Project name: `TikTok Research Sorter`
- Project type: `Chrome Extension / local social-content research tool`
- Current version: `0.5.0`
- Short description: a Manifest V3 browser extension that scans public TikTok profile and hashtag pages, stores research locally, ranks videos, saves favorites with durable channel snapshots, and exports selected channel-and-video shortlists as standalone HTML.

## 2. Purpose

Supported workflows:

```text
public profile -> scan loaded profile videos + public channel data -> metrics -> filter/sort -> favorite/export
public hashtag -> scan loaded hashtag videos -> group by account -> top N + minimum views -> favorite
favorite -> preserve video + channel snapshot -> enrich/refresh channel data
favorites -> checkbox selection -> channel-grouped standalone HTML -> send as a file
```

Primary users:

- short-form video researchers;
- creators and agencies;
- local-business marketers;
- the owner’s TikTok and Reels research workflows.

## 3. Source of truth

- Durable source: `projects/tiktok-research-sorter/` inside `oleg3479881328-code/Project-Execution-OS`.
- Stable implementation and distribution branch: `main`.
- Active feature branch: `agent/tiktok-research-sorter-channel-export-v0.5.0` until PR #87 is merged.
- Version 0.5.0 delivery issue: `#86`.
- Version 0.5.0 pull request: `#87`.

## 4. Architecture

```text
TikTok public page
→ selected fetch/XHR payload observer + embedded JSON + DOM fallback
→ optional same-origin public profile enrichment
→ isolated content script
→ serialized background persistence
→ chrome.storage.local profiles + hashtag snapshots + favorite video/channel snapshots
→ React side panel grouped by channel
→ CSV / JSON / channel-grouped standalone HTML export
```

## 5. Current status

- Mode: `implementation / automated validation`
- Phase: `v0.5.0 complete public channel information`
- Status: implementation and tests are committed on PR #87; final Linux, Windows, integrity, artifact, and merge evidence are pending.

## 6. Key decisions and constraints

- Stack: `WXT + TypeScript + React + Manifest V3`.
- No backend, accounts, AI calls, payments, remote executable code, or cloud sync.
- Host access remains limited to TikTok.
- Do not bypass login, private accounts, CAPTCHA, rate limits, paywalls, or access controls.
- Prefer structured JSON payloads; DOM selectors are fallback only.
- Store only fields TikTok actually returns; display missing values as unavailable.
- Favorites are durable local snapshots independent of profile and hashtag deletion.
- Existing favorite channel snapshots are refreshed only when richer public data becomes available.
- Same-origin profile enrichment must not navigate the visible page.
- HTML exports include only checked favorites and group them by channel.
- HTML text is escaped and external URLs are restricted to HTTP(S).
- Exported avatars and previews remain dependent on external URLs remaining available.
- Preserve only sanitized fixtures. Never commit cookies, tokens, authorization headers, browser profiles, signatures, or raw identifying traffic.
- Keep generated deliverables and exports versioned.

## 7. Current validation gate

Before v0.5.0 is integrated:

- Project Execution OS integrity validation passes;
- Linux reproducible install, strict TypeScript check, all tests, production build, and versioned packaging pass;
- Windows updater dry-run, full local-source validation, and manifest check pass;
- installable extension archive contains root-level `manifest.json` with version `0.5.0`;
- PR #87 is mergeable and merged into `main`.

## 8. Read next

1. `PROJECT_STATE.md`
2. `logs/latest.md`
3. `README.md`
4. `coordination/CHANNEL_PROFILE_EXPORT_V0.5.0.md`
5. `docs/RESEARCH_AND_DECISIONS.md`
6. `docs/IMPLEMENTATION_HANDOFF.md`
