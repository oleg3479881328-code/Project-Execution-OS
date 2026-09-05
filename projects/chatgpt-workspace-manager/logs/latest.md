# ChatGPT Workspace Manager — Latest State

## Date

2026-09-05

## Current Status

Architecture accepted and Slice 1 implemented as a private, unpacked owner-operated Chrome extension.

Machine validation is green for v0.1.2:

- dependency install: PASS;
- TypeScript: PASS;
- 7 unit tests: PASS;
- WXT production build: PASS;
- unpacked artifact upload: PASS.

Real-browser acceptance is in progress on the owner's active ChatGPT account.

## Browser Acceptance Milestones

### v0.1.0 bridge failure

Observed after loading the unpacked extension while the ChatGPT tab was already open:

`CHATGPT_CONTENT_BRIDGE_MISSING: Could not establish connection. Receiving end does not exist.`

Root cause:

- Side Panel extension context was running;
- the pre-existing ChatGPT tab had not received the declarative content script because it predated the extension load/reload;
- therefore Side Panel messaging had no receiving bridge.

Immediate workaround for v0.1.0:

- reload the ChatGPT tab once, then Sync.

### v0.1.1 self-heal fix

Permanent fix implemented and machine-validated:

- added `scripting` permission;
- `ChatGPTAdapter` detects the missing receiving-end error;
- it injects the built `/content-scripts/content.js` into the current ChatGPT tab via `browser.scripting.executeScript`;
- waits briefly and retries the original request once;
- reports explicit injection/retry diagnostics if recovery fails;
- no automatic page reload is required, avoiding loss of unsent ChatGPT input.

The v0.1.1 manifest contains:

- version `0.1.1`;
- permissions: `storage`, `sidePanel`, `activeTab`, `scripting`;
- host permissions only for `https://chatgpt.com/*` and `https://chat.openai.com/*`.

### Live metadata sync — PASS

Browser evidence on 2026-09-05:

- v0.1.1 loaded as unpacked extension;
- self-healing bridge succeeded without manual ChatGPT-tab reload;
- live metadata sync completed successfully;
- UI reported `Synced 1051 conversations`;
- local Workspace list populated with 1051 conversation records;
- cached/local workspace remained rendered in the Side Panel after sync.

This confirms the live chain works against the owner's real account:

`Side Panel -> self-heal bridge -> ChatGPT session -> conversation list API -> normalization -> IndexedDB -> Workspace UI`.

### On-demand conversation hydration — PASS

Browser evidence on 2026-09-05:

- selected the live conversation `ChatGPT Workspace Manager` from the local Workspace list;
- extension fetched the selected conversation on demand;
- UI reported `Hydrated 583 messages`;
- normalized user/assistant messages rendered in the preview pane;
- non-text/tool content was preserved safely as a placeholder rather than crashing preview;
- the rest of the 1051-conversation local Workspace remained available while the long conversation rendered.

A second conversation (`Домен Vercel обсудить`) also hydrated successfully with 15 messages, confirming repeated select/read/hydrate behavior across multiple conversations.

This confirms the second-stage sync path works on real conversations:

`local metadata record -> select -> ChatGPT read API -> message normalization -> IndexedDB message cache -> Side Panel preview`.

### Owner favorite + local note persistence — PASS

Browser evidence on 2026-09-05:

- marked `ChatGPT Workspace Manager` as favorite;
- saved a local note on that conversation;
- switched selection to another conversation;
- the original conversation remained visibly starred in the Workspace list;
- the `Note` chip remained visible after selection changed;
- therefore owner metadata persisted independently of the selected provider record and survived normal UI navigation.

This validates the intended authority split for these fields:

`ChatGPT platform metadata != owner-local favorite/note metadata`.

### Health screen evidence bookkeeping — BUG FOUND IN v0.1.1

Browser evidence on 2026-09-05:

- `session`, `chatgpt-tab`, `local-search`, and `local-db` rendered HEALTHY;
- `list-conversations` and `read-conversation` incorrectly rendered UNKNOWN even though live sync and real conversation hydration had already succeeded;
- status line showed `Preview loaded from local cache`, confirming cached preview path was active.

Root cause:

- successful sync/read explicitly stored HEALTHY capability evidence;
- a later passive Health check stored newer UNKNOWN records for operations it did not actively re-run;
- `latestCapabilities()` selected only the newest record, so UNKNOWN masked prior validated HEALTHY evidence.

### v0.1.2 Health + offline acceptance fix

Implemented and machine-validated:

- `latestCapabilities()` now preserves the latest validated non-UNKNOWN result when a newer passive record is only UNKNOWN;
- newer explicit HEALTHY/DEGRADED/UNAVAILABLE results still supersede older evidence;
- added unit coverage for both evidence-retention and explicit-failure precedence;
- added persistent `Offline test` mode in the Health panel;
- Offline test intentionally blocks live ChatGPT calls inside the extension without disabling the browser's network connection;
- cached Workspace list/search/favorites/notes remain available;
- already hydrated conversations can be opened from IndexedDB while offline mode is enabled;
- uncached conversations clearly report that live hydration is intentionally disabled;
- Health reports `OFFLINE_TEST_MODE` for live capabilities while local DB/search continue to be checked normally.

This creates a controlled acceptance test for the local-first contract without requiring the owner to disconnect the computer or interrupt the active ChatGPT session.

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
- `CODEX_HANDOFF_SLICE_1.md` — bounded implementation contract for the first non-destructive vertical slice.

## Slice 1 Implemented

1. WXT project shell;
2. owner Side Panel shell;
3. Dexie / IndexedDB schema;
4. `ChatGPTAdapter` capability framework;
5. metadata conversation sync;
6. local Workspace list;
7. on-demand preview;
8. local favorites + notes;
9. title / local metadata search;
10. Health panel;
11. diagnostics export;
12. self-healing content bridge in v0.1.1;
13. evidence-aware Health bookkeeping in v0.1.2;
14. controlled Offline test mode in v0.1.2;
15. no destructive actions yet.

## Acceptance Boundary

Do not begin archive/delete implementation until v0.1.2 passes the final browser checks below.

## Next Browser Checks

1. Install v0.1.2 and open Health; verify previously proven list/read capabilities no longer fall back to UNKNOWN after Run checks.
2. Enable Offline test.
3. Return to Workspace and verify all 1051 cached metadata records remain searchable/browsable.
4. Open `ChatGPT Workspace Manager` or `Домен Vercel обсудить` and verify cached messages load while Offline test is enabled.
5. Verify favorite/note remain available in Offline test.
6. Disable Offline test and verify normal live access resumes.
7. After these pass, close Slice 1 and review Slice 2.
