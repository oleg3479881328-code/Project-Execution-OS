# ChatGPT Workspace Manager — Latest State

## Date

2026-09-05

## Current Status

Architecture review completed and accepted for implementation as a private, unpacked owner-operated Chrome extension.

## Decisions Frozen

- Product is a personal ChatGPT control center, not a Chrome Web Store product.
- Use Project Execution OS Chrome extension baseline: WXT + TypeScript + React + Tailwind + Manifest V3.
- Use the existing Project Execution OS owner Side Panel pattern.
- Do not fork one donor application as the foundation.
- Isolate ChatGPT-specific behavior behind `ChatGPTAdapter`.
- Private ChatGPT endpoints may be used as a strategy for this private tool, but never as the Workspace Core contract.
- Maintain DOM and official-export/local-snapshot fallbacks where practical.
- Split authority: ChatGPT owns platform state; local DB owns owner metadata, cache, snapshots, indexes and operation history.
- Use two-stage synchronization: lightweight metadata sync + on-demand content hydration.
- Add mandatory compatibility/capability health harness.
- Bulk destructive actions must follow plan -> snapshot option -> confirm -> sequential execute -> verify -> log.
- Pause rather than bypass rate limits or account warnings.
- Local-first by default: no telemetry, no analytics, no vendor backend.
- IndexedDB encryption is not required for first implementation; optional encrypted backup can come later.
- Cross-provider support remains an interface-level future direction, not initial scope.

## Donor Conclusions

Primary live-action donor:

- `fineanmol/chatgpt-bulk-delete-manager` — MIT; current ChatGPT conversation list / preview / archive / delete patterns; structurally useful but not suitable as the main app foundation because logic is concentrated in a large content script.

Primary data/persistence donors:

- `world-wide-dev/chatgpt-export` — MIT; canonical semantic snapshots, incremental persistence, deterministic export.
- `terra901/Threadline` — Apache-2.0; IndexedDB/Dexie-style local memory, recall, graph, local embeddings.
- `marswangyang/personal-ai-memory` — Apache-2.0; hybrid local search / RAG and local embedding architecture.
- `OwlCt/ChatGPT-Export` — MIT; ZIP, Markdown/raw JSON, assets, project-aware archive and offline reader patterns.

Secondary donors:

- `carlosguadian/universal-prompt-library` — MIT; prompt organization/variables.
- long-conversation navigation donors, with license check required before any code reuse.
- Superpower / AI Toolbox / Simple Folder as specification and UX references only.
- qcrao bulk-delete project as reference-only unless its code license is clarified.

## Architecture Files

- `PROJECT.md` — project purpose, frozen architecture and acceptance gate.
- `DONOR_CAPABILITY_MATRIX.md` — donor selection and reuse boundaries.
- `TECHNICAL_ARCHITECTURE.md` — canonical contracts, DB, adapter, sync, bulk engine, health harness, tests and first implementation slice.

## First Implementation Slice

Build and validate:

1. WXT project shell;
2. owner Side Panel shell;
3. Dexie / IndexedDB schema + migrations;
4. `ChatGPTAdapter` capability framework;
5. metadata conversation sync;
6. local Workspace list;
7. on-demand preview;
8. local favorites + notes;
9. title / local metadata search;
10. Health panel;
11. diagnostics export;
12. no destructive actions yet.

## Acceptance Boundary

Do not begin archive/delete implementation until Slice 1 passes real-browser behavioral verification against the owner's ChatGPT account and adapter failure is demonstrated not to break cached workspace browsing.

## Next Action

Prepare a bounded Codex implementation handoff for Slice 1, using the frozen architecture and donor matrix. Before coding, inspect exact donor files needed for the slice and record licenses/commit references for any reused code.
