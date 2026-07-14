# PROJECT — TikTok Research Sorter

## 1. Project

- Project name: `TikTok Research Sorter`
- Project type: `Chrome Extension / local social-content research tool`
- Current version: `0.4.0`
- Short description: a Manifest V3 browser extension that scans public TikTok profile and hashtag pages, stores research locally, ranks videos, saves favorites, and exports selected shortlists as standalone HTML.

## 2. Purpose

Supported workflows:

```text
public profile -> scan loaded profile videos -> calculate metrics -> filter/sort -> favorite/export
public hashtag -> scan loaded hashtag videos -> group by account -> top N + minimum views -> favorite/export
favorites -> checkbox selection -> standalone HTML shortlist -> send as a file
```

Primary users:

- short-form video researchers;
- creators and agencies;
- local-business marketers;
- the owner’s TikTok and Reels research workflows.

## 3. Source of truth

- Durable source: `projects/tiktok-research-sorter/` inside `oleg3479881328-code/Project-Execution-OS`.
- Stable implementation and distribution branch: `main`.
- Version 0.4.0 delivery issue: `#84`.
- Version 0.4.0 pull request: `#85`.

## 4. Architecture

```text
TikTok public page
→ selected fetch/XHR payload observer + embedded JSON + DOM fallback
→ isolated content script
→ serialized background persistence
→ chrome.storage.local profiles + hashtag snapshots + favorites
→ React side panel
→ CSV / JSON / standalone HTML export
```

## 5. Current status

- Mode: `stable / integrated`
- Phase: `v0.4.0 favorites and HTML shortlist delivered`
- Status: profile, hashtag, favorites, and selected HTML-export workflows are integrated into `main`; Linux, Windows, integrity, and packaging validation are green.

## 6. Key decisions and constraints

- Stack: `WXT + TypeScript + React + Manifest V3`.
- No backend, accounts, AI calls, payments, remote executable code, or cloud sync.
- Host access remains limited to TikTok.
- Do not bypass login, private accounts, CAPTCHA, rate limits, paywalls, or access controls.
- Prefer structured JSON payloads; DOM selectors are fallback only.
- Favorites are durable local snapshots independent of profile and hashtag deletion.
- HTML exports include only checked favorites.
- HTML text is escaped and external URLs are restricted to HTTP(S).
- Exported previews remain dependent on the external TikTok image URL remaining available.
- Preserve only sanitized fixtures. Never commit cookies, tokens, authorization headers, browser profiles, signatures, or raw identifying traffic.
- Keep generated deliverables and exports versioned.

## 7. Current validation baseline

- Project Execution OS integrity validation passes.
- Linux reproducible install, strict TypeScript check, all tests, production build, and versioned packaging pass.
- Windows updater dry-run, full local-source validation, and manifest check pass.
- Installable extension archive contains root-level `manifest.json` with version `0.4.0`.

## 8. Read next

1. `PROJECT_STATE.md`
2. `logs/latest.md`
3. `README.md`
4. `docs/RESEARCH_AND_DECISIONS.md`
5. `docs/IMPLEMENTATION_HANDOFF.md`
