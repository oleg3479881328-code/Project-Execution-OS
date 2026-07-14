# PROJECT — TikTok Research Sorter

## 1. Project

- Project name: `TikTok Research Sorter`
- Project type: `Chrome Extension / local social-content research tool`
- Current version: `0.3.0`
- Short description: a Manifest V3 browser extension that scans publicly visible TikTok profile and hashtag pages, stores metrics locally, selects unusually successful or highest-viewed videos, and exports research data.

## 2. Purpose

Supported workflows:

```text
public profile -> scan loaded profile videos -> calculate normalized metrics -> filter/sort -> export
public hashtag -> scan loaded hashtag videos -> group by account -> top N per account + minimum views -> export
```

Primary users:

- short-form video researchers;
- creators and agencies;
- local-business marketers;
- the owner’s TikTok and Reels research workflows.

## 3. Source of truth

- Durable source: `projects/tiktok-research-sorter/` inside `oleg3479881328-code/Project-Execution-OS`.
- Stable implementation and distribution branch: `main`.
- Version 0.3.0 delivery issue: `#82`.
- Version 0.3.0 pull request: `#83`.

## 4. Architecture

```text
TikTok public page
→ selected fetch/XHR payload observer + embedded JSON + DOM fallback
→ isolated content script
→ serialized background persistence
→ chrome.storage.local
→ React side panel
```

## 5. Current status

- Mode: `stable / integrated`
- Phase: `v0.3.0 hashtag discovery scan delivered`
- Status: profile and hashtag workflows are integrated into `main`; Linux and Windows validation and versioned packaging are green.

## 6. Key decisions and constraints

- Stack: `WXT + TypeScript + React + Manifest V3`.
- No backend, accounts, AI calls, payments, remote executable code, or cloud sync.
- Host access remains limited to TikTok.
- Do not bypass login, private accounts, CAPTCHA, rate limits, paywalls, or access controls.
- Prefer structured JSON payloads; DOM selectors are fallback only.
- Hashtag results represent videos actually loaded from the open hashtag page; the extension does not silently crawl every profile.
- Preserve only sanitized fixtures. Never commit cookies, tokens, authorization headers, browser profiles, signatures, or raw identifying traffic.
- Keep generated deliverables versioned.

## 7. Current validation baseline

- Project Execution OS integrity validation passes.
- Linux reproducible install, strict TypeScript check, tests, production build, and versioned packaging pass.
- Windows updater dry-run, full local-source validation, and manifest check pass.
- Installable extension archive contains root-level `manifest.json` with version `0.3.0`.

## 8. Read next

1. `PROJECT_STATE.md`
2. `logs/latest.md`
3. `README.md`
4. `docs/RESEARCH_AND_DECISIONS.md`
5. `docs/IMPLEMENTATION_HANDOFF.md`
