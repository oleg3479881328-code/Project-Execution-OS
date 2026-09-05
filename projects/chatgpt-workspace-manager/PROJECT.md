# ChatGPT Workspace Manager

## Status

Architecture accepted for implementation as a private, unpacked owner-operated Chrome extension.

## Purpose

Build a personal ChatGPT control center for organizing, searching, preserving, navigating, and managing conversations at scale without depending on a public Chrome Web Store release.

## Product Boundary

This is an internal operator tool for the owner. It is not a SaaS product and is not being designed for Chrome Web Store publication.

The extension may therefore optimize for owner productivity and operational power rather than public-store single-purpose restrictions. However, it must still minimize account risk, avoid rate-limit bypass behavior, keep data local by default, and isolate fragile ChatGPT-specific behavior behind adapters.

## Frozen Architecture

### Core principle

Do not build a monolithic ChatGPT content script.

Use a modular architecture:

```text
Workspace Core
  -> ChatGPT Provider Adapter
      -> Live API Strategy
      -> DOM Strategy
      -> Official Export Import Strategy
  -> Local Mirror / IndexedDB
  -> Search / Organization / Backup / Memory Modules
  -> Side Panel UI
```

### Authority split

ChatGPT remains authoritative for platform state:

- conversation existence;
- native title;
- native project placement;
- active / archived state;
- current platform conversation content.

The local manager is authoritative for owner metadata:

- folders and subfolders;
- tags and colors;
- notes;
- favorites and pins;
- bookmarks;
- smart collections;
- local snapshots;
- full-text and semantic indexes;
- operation history;
- export / backup state.

### Synchronization model

Use two-stage synchronization.

Stage 1: lightweight metadata sync

- conversation ID;
- title;
- timestamps;
- native project;
- active / archived state;
- other cheap metadata.

Stage 2: on-demand content hydration

Fetch or capture full conversation content only when needed, for example:

- preview;
- full-text indexing;
- local snapshot / backup;
- semantic indexing;
- user-requested export;
- selected bulk action safety backup.

Do not re-fetch the complete content of the entire account on every launch.

## UI

Use the Project Execution OS internal-operator Side Panel pattern.

Canonical owner UI donor:

`projects/tiktok-research-sorter/entrypoints/sidepanel/`

Use:

- persistent Chrome Side Panel;
- visible extension version in header;
- clear capability health/status;
- progress for long-running operations;
- queue pause / resume / cancel;
- readable dense operator UI rather than a tiny popup.

## Capability Health Layer

A compatibility harness is mandatory because ChatGPT runtime and internal endpoints can change.

Expose a capability health surface similar to:

```text
Session        OK / FAIL
List chats     OK / FAIL
Read chat      OK / FAIL
Projects       OK / FAIL
Archive        OK / FAIL
Delete         OK / FAIL
DOM navigator  OK / FAIL
Local DB       OK / FAIL
Search index   OK / FAIL
```

A failure in one capability must not take down unrelated modules.

## Functional Modules

### 1. Live workspace

- all chats;
- active / archived;
- native Projects;
- preview;
- open original;
- rename where safely supported;
- archive;
- delete.

### 2. Organization

- folders / nested folders;
- tags;
- colors;
- favorites;
- pins;
- notes;
- bookmarks;
- smart collections / saved filters.

### 3. Search

- title search;
- full-text local search;
- date filters;
- native project filters;
- owner folder / tag filters;
- archive state filters;
- saved searches.

### 4. Bulk operations

- selection and range selection;
- filter -> select;
- backup selected;
- archive selected;
- delete selected;
- tag selected;
- move to local folder;
- queue, pause, resume, cancel;
- retry failed items;
- result report.

Destructive flow:

```text
SELECT
-> SNAPSHOT / BACKUP OPTION
-> ACTION PLAN
-> USER CONFIRMATION
-> SEQUENTIAL EXECUTION
-> VERIFY EACH RESULT
-> STOP ON RATE LIMIT / ACCOUNT WARNING
-> OPERATION LOG
```

Never attempt to bypass rate limits. A 429 or equivalent limit signal pauses the queue.

### 5. Vault / backup

- local canonical snapshots;
- Markdown;
- JSON;
- HTML;
- ZIP;
- attachments / images when available;
- full local DB export;
- later optional encrypted export.

### 6. Long conversation navigator

- current-chat search;
- user / assistant turn navigation;
- headings;
- code blocks;
- bookmarks;
- highlights;
- jump controls.

### 7. Memory

Later capability, but architecture-ready from the beginning:

- BM25 / keyword search;
- local embeddings;
- semantic recall;
- select old context;
- inject selected context into composer.

### 8. Prompt library

Later capability, architecture-ready:

- folders;
- variables;
- favorites;
- prompt history / versions;
- insert into composer.

## Technology Baseline

Use the existing Chrome Extension block default:

`WXT + TypeScript + React + Tailwind + Manifest V3`

Storage:

- `IndexedDB` / Dexie for conversations, messages, snapshots, indexes, owner metadata;
- `chrome.storage.local` for lightweight settings and UI state;
- no external backend by default;
- no telemetry by default.

Do not require IndexedDB encryption for the first implementation. Keep the architecture compatible with optional encrypted exports or later encryption-at-rest if needed.

## Private ChatGPT APIs

Private ChatGPT endpoints may be used as an implementation strategy for this private owner tool, but they are never allowed to become the Workspace Core contract.

Rules:

- isolate them in `ChatGPTAdapter`;
- centralize endpoint definitions;
- centralize session/auth discovery;
- provide capability tests;
- keep DOM and import fallbacks where practical;
- treat endpoint changes as adapter breakage, not product-core breakage;
- do not bypass rate limits or account restrictions.

## Cross-provider Direction

Design provider interfaces so future adapters can support Claude, Gemini, Grok, Perplexity or others.

Do not implement those providers until there is a concrete need.

## Donor Strategy

Do not fork one monolithic extension.

Use licensed donors by capability and re-implement where a donor is unlicensed, overly coupled, or structurally weak.

Primary donors are tracked in `DONOR_CAPABILITY_MATRIX.md`.

## Acceptance Gate Before Implementation

Before coding the full product:

1. finalize donor capability matrix;
2. verify donor licenses;
3. define canonical data model;
4. define `ProviderAdapter` and `ChatGPTAdapter` contracts;
5. define compatibility harness;
6. define destructive-operation safety contract;
7. define local DB migration/versioning strategy;
8. create a bounded implementation plan.

## Immediate Next Action

Execute `CODEX_HANDOFF_SLICE_1.md`; do not start Slice 2 until Slice 1 passes real-browser acceptance.
