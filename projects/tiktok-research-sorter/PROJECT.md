# PROJECT — TikTok Research Sorter

## 1. Project

- Project name: `TikTok Research Sorter`
- Project type: `Chrome Extension / local social-content research tool`
- Short description: a Manifest V3 browser extension that scans publicly visible TikTok profile videos, stores their metrics locally, identifies unusually successful videos, and exports research data.

## 2. Purpose

The project exists to replace fragile “sort the current TikTok grid” extensions with a reliable research workflow:

`open public profile -> start scan -> collect loaded videos -> calculate normalized metrics -> filter and sort -> export`

Primary users:

- short-form video researchers;
- creators and agencies;
- local-business marketers;
- the owner’s TikTok and Reels research workflows.

Current-stage success means a loadable Chrome extension that can scan a public profile page, preserve collected records locally, show outlier and velocity analytics, and export CSV/JSON without a backend.

## 3. Source Of Truth

- Current durable source of truth: this internal project tree inside `oleg3479881328-code/Project-Execution-OS`.
- Active implementation branch: `agent/tiktok-research-sorter-mvp`.
- The project should later be extracted into a standalone repository when repository creation is available.

## 4. Source Trail

Primary product reference:

- https://chromewebstore.google.com/detail/sort-for-tiktok-videos-by/dpfmkbcoaddghkkhebjcjaoaiaefigln

Canonical Project Execution OS routes:

- https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/START_HERE.md
- https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/blocks/chrome-extension/BLOCK.md

Implementation sources and decisions are summarized in `docs/RESEARCH_AND_DECISIONS.md`.

## 5. Current Status

- Mode: `implementation / validation handoff`
- Phase: `desktop browser validation`
- Status: `buildable MVP; real TikTok smoke test still required`
- Confidence: high for extension architecture, build, unit-tested normalization, and local analytics; medium for long-term TikTok payload compatibility until real browser validation is completed.

## 6. Done So Far

- Confirmed the product direction and MVP scope.
- Applied Existing Solution First and selected WXT instead of custom build tooling.
- Created the Manifest V3 WXT/React/TypeScript project.
- Added a MAIN-world fetch/XHR observer for relevant TikTok responses.
- Added an isolated collector with initial-state parsing, DOM fallback, controlled auto-scroll, stop handling, and CAPTCHA stop condition.
- Added heuristic payload normalization and per-profile deduplication.
- Added local persistence through `chrome.storage.local`.
- Added views/day, Engagement Rate, Outlier Score, filters, CSV/JSON export, and a Chrome side panel UI.
- Added 5 passing unit tests.
- Passed TypeScript validation, WXT production build, ZIP build, and runtime dependency audit.
- Added a bounded desktop Chrome validation handoff.

## 7. Current Focus

Validate the built extension against real public TikTok profiles and harden parser adapters using captured, sanitized payload fixtures.

## 8. Next Practical Step

Load the production build as an unpacked extension in Chrome, execute `docs/IMPLEMENTATION_HANDOFF.md`, save sanitized failing payload examples, and update the TikTok adapter without expanding permissions.

## 9. Key Decisions And Constraints

- Existing Solution First is mandatory.
- Stack: `WXT + TypeScript + React + Manifest V3`.
- Architecture: local utility + content scripts + Chrome side panel.
- No backend, accounts, AI calls, payments, or cloud sync in MVP.
- Data remains in `chrome.storage.local` unless measured storage pressure or history requirements justify IndexedDB.
- Host access is limited to `https://www.tiktok.com/*`.
- Do not bypass login, private accounts, CAPTCHA, rate limits, or TikTok access controls.
- Prefer structured JSON payloads; DOM selectors are fallback only.
- Preserve raw sanitized fixtures during validation, but never commit cookies, tokens, headers, signatures, or personal account data.
- The generated `package-lock.json` must be committed by the desktop executor because the current connector cannot upload the local lock file directly.

## 10. Read Next

1. `PROJECT_STATE.md`
2. `logs/latest.md`
3. `README.md`
4. `docs/RESEARCH_AND_DECISIONS.md`
5. `docs/IMPLEMENTATION_HANDOFF.md`
