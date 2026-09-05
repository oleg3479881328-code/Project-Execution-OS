# ChatGPT Workspace Manager — Latest State

## Date

2026-09-05

## Current Status

Architecture accepted and Slice 1 implemented as a private, unpacked owner-operated Chrome extension.

Machine validation is green for v0.1.4:

- dependency install: PASS;
- TypeScript: PASS;
- 9 unit tests: PASS;
- stable extension ID derivation test: PASS;
- WXT production build: PASS;
- unpacked artifact upload: PASS;
- built manifest inspected: version `0.1.4`, pinned manifest `key` present, permissions unchanged.

Real-browser acceptance is in progress on the owner's active ChatGPT account.

## Browser Acceptance Milestones

### v0.1.0 bridge failure

Observed after loading the unpacked extension while the ChatGPT tab was already open:

`CHATGPT_CONTENT_BRIDGE_MISSING: Could not establish connection. Receiving end does not exist.`

Root cause: the pre-existing ChatGPT tab had not received the declarative content script.

Permanent fix in v0.1.1:

- added `scripting` permission;
- missing bridge is detected;
- built `/content-scripts/content.js` is injected into the active ChatGPT tab;
- original request is retried once;
- no page reload is required.

### Live metadata sync — PASS

Browser evidence:

- self-healing bridge succeeded without manual tab reload;
- UI reported `Synced 1051 conversations`;
- local Workspace list populated with 1051 records.

Validated chain:

`Side Panel -> self-heal bridge -> ChatGPT session -> conversation list API -> normalization -> IndexedDB -> Workspace UI`.

### On-demand conversation hydration — PASS

Browser evidence from earlier unpacked installation:

- `ChatGPT Workspace Manager` hydrated with 583 messages;
- `Домен Vercel обсудить` hydrated with 15 messages;
- normalized user/assistant messages rendered in preview;
- tool/non-text items did not crash preview and are represented by a safe placeholder;
- 1051-record Workspace remained available during hydration.

Validated chain:

`local metadata record -> select -> ChatGPT read API -> normalization -> IndexedDB message cache -> Side Panel preview`.

### Owner favorite + local note persistence — PASS WITHIN ONE EXTENSION INSTALLATION

Browser evidence:

- favorite persisted after switching conversations;
- local note persisted after switching conversations;
- `Note` chip remained visible;
- owner metadata is independent from provider metadata.

### Health screen evidence bookkeeping — BUG FOUND AND FIXED

Observed in v0.1.1:

- `session`, `chatgpt-tab`, `local-search`, `local-db` were HEALTHY;
- `list-conversations` and `read-conversation` incorrectly returned UNKNOWN despite proven successful sync/read.

Root cause:

- a passive Health check stored newer UNKNOWN records and masked earlier explicit HEALTHY evidence.

Fix in v0.1.2:

- passive UNKNOWN no longer overrides a prior validated non-UNKNOWN result;
- newer explicit HEALTHY/DEGRADED/UNAVAILABLE still supersedes older evidence;
- controlled `Offline test` mode added.

### Offline test diagnostics — PASS FOR HEALTH / LOCAL STORAGE LAYER

Owner-exported diagnostics from v0.1.2 and v0.1.3 show:

- `local-db`: HEALTHY;
- `local-search`: HEALTHY;
- `session`: UNAVAILABLE with `OFFLINE_TEST_MODE`;
- `list-conversations`: UNAVAILABLE with `OFFLINE_TEST_MODE`;
- `read-conversation`: UNAVAILABLE with `OFFLINE_TEST_MODE`;
- last sync summary: received 1051 / upserted 1051.

This confirms Offline test blocks live ChatGPT access inside the extension while local storage/search remain operational.

### Offline test exit health restoration — EDGE CASE FOUND AND FIXED IN v0.1.3

Review of v0.1.2 found:

- while Offline test is enabled, list/read/session correctly receive explicit `OFFLINE_TEST_MODE = unavailable` evidence;
- after disabling Offline test, passive list/read checks return UNKNOWN;
- without additional logic, the temporary offline UNAVAILABLE evidence could remain the latest validated state.

Fix in v0.1.3:

- `latestCapabilities()` checks persisted `offlineMode`;
- temporary `OFFLINE_TEST_MODE` evidence is visible while test mode is enabled;
- after test mode is disabled, synthetic offline evidence is ignored and prior live evidence can surface again;
- dedicated unit test covers the transition.

### v0.1.3 browser result — STABLE LOCAL IDENTITY PROBLEM DISCOVERED

Browser screenshots and exported diagnostics on 2026-09-05 showed:

- after disabling Offline test, `list-conversations` was HEALTHY and `session` was HEALTHY;
- `read-conversation` remained UNKNOWN because no successful live read had occurred in that specific current unpacked installation;
- enabling Offline test correctly made live session/list/read UNAVAILABLE;
- all 1051 metadata records remained available in Workspace;
- selecting `ChatGPT Workspace Manager` in Offline test reported `selected conversation has no local message cache`.

Interpretation:

- Offline test itself behaved correctly;
- the current installation had metadata but did not contain the 583-message cache hydrated in an earlier unpacked installation;
- favorite/note test data from prior unpacked installations was also not guaranteed to survive when the extension was removed and a new extracted folder was loaded;
- the likely cause is a different unpacked Chrome extension origin/ID between version folders, which means a different IndexedDB origin.

### v0.1.4 Stable Identity — IMPLEMENTED AND MACHINE-VALIDATED

Official Chrome documentation confirms manifest `key` can control the unique extension ID during development/unpacked loading.

Implemented:

- pinned public manifest `key`;
- frozen expected Chrome extension ID: `ejpgnlcdfbbjkhlnbfonplngcfcjmbaa`;
- shared identity constants in `src/core/extension-identity.ts`;
- unit test derives Chrome extension ID from the pinned public key and asserts the frozen ID;
- `EXTENSION_IDENTITY.md` documents the identity contract and upgrade rule;
- built v0.1.4 manifest was inspected and contains the pinned key;
- permissions remain `storage`, `sidePanel`, `activeTab`, `scripting` with ChatGPT-only host permissions.

Important transition note:

- v0.1.4 is a one-time identity reset from prior path-derived development IDs;
- local state from v0.1.3 should be treated as test-only and may not automatically appear in v0.1.4;
- from v0.1.4 onward, loading later builds from different folders should retain the same extension ID and therefore the same extension IndexedDB origin, provided the manifest key is not changed.

## Decisions Frozen

- Product is a personal ChatGPT control center, not a Chrome Web Store product.
- Baseline: WXT + TypeScript + React + Tailwind + Manifest V3.
- Side Panel is the primary operator UI.
- Do not fork one donor application as the foundation.
- Isolate ChatGPT-specific behavior behind `ChatGPTAdapter`.
- Private ChatGPT endpoints may be used as a strategy for this private tool, but never as the Workspace Core contract.
- Split authority: ChatGPT owns platform state; local DB owns owner metadata, cache, snapshots, indexes and operation history.
- Two-stage synchronization: lightweight metadata sync + on-demand content hydration.
- Compatibility/capability health harness is mandatory.
- Bulk destructive actions must follow plan -> snapshot option -> confirm -> sequential execute -> verify -> log.
- Pause rather than bypass rate limits or account warnings.
- Local-first by default: no telemetry, analytics or vendor backend.
- IndexedDB encryption is not required for first implementation; encrypted backup can come later.
- Cross-provider support remains a future adapter direction.
- Stable unpacked extension identity is now mandatory; manifest `key` must not change accidentally.

## Donor Conclusions

Primary live-action donor:

- `fineanmol/chatgpt-bulk-delete-manager` — MIT; list / preview / archive / delete patterns.

Primary data/persistence donors:

- `world-wide-dev/chatgpt-export` — MIT; canonical snapshots / deterministic export.
- `terra901/Threadline` — Apache-2.0; local memory / recall / embeddings patterns.
- `marswangyang/personal-ai-memory` — Apache-2.0; hybrid local search / RAG patterns.
- `OwlCt/ChatGPT-Export` — MIT; ZIP / Markdown / assets / project-aware archive patterns.

Secondary donors:

- `carlosguadian/universal-prompt-library` — MIT; prompts/variables.
- Superpower / AI Toolbox / Simple Folder — UX/specification references only.
- qcrao bulk-delete — reference-only unless license is clarified.

## Slice 1 Implemented

1. WXT project shell;
2. Side Panel shell;
3. Dexie / IndexedDB schema;
4. `ChatGPTAdapter` capability framework;
5. metadata conversation sync;
6. local Workspace list;
7. on-demand preview;
8. local favorites + notes;
9. title/local metadata search;
10. Health panel;
11. diagnostics export;
12. self-healing content bridge;
13. evidence-aware Health bookkeeping;
14. controlled Offline test mode;
15. Offline test exit health restoration;
16. stable unpacked extension identity in v0.1.4;
17. no destructive actions yet.

## Acceptance Boundary

Do not begin archive/delete implementation until stable identity + cached preview persistence are verified in Chrome.

## Next Browser Checks

1. Install v0.1.4 and confirm Chrome extension ID is `ejpgnlcdfbbjkhlnbfonplngcfcjmbaa`.
2. Disable Offline test if it is enabled.
3. Sync metadata; expect approximately 1051 conversations.
4. Open `ChatGPT Workspace Manager` live once and hydrate it; verify `read-conversation` becomes HEALTHY.
5. Set one favorite and one local note.
6. Enable Offline test; verify the hydrated chat opens from local cache and owner metadata remains visible.
7. Disable Offline test.
8. For the final identity-persistence proof, install the next build from a different folder and confirm the same Chrome extension ID and retained local state.
9. After these pass, close Slice 1 and review Slice 2.
