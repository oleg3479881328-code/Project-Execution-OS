# Codex Handoff — ChatGPT Workspace Manager — Slice 1

## Objective

Implement the first bounded vertical slice of `ChatGPT Workspace Manager` as a private unpacked Chrome extension.

The purpose of this slice is to prove the architecture and compatibility model before any destructive archive/delete actions are added.

## Canonical Inputs

Read first:

1. `projects/chatgpt-workspace-manager/PROJECT.md`
2. `projects/chatgpt-workspace-manager/TECHNICAL_ARCHITECTURE.md`
3. `projects/chatgpt-workspace-manager/DONOR_CAPABILITY_MATRIX.md`
4. `blocks/chrome-extension/BLOCK.md`
5. `blocks/chrome-extension/ARCHITECTURE_PATTERNS.md`
6. `blocks/chrome-extension/SECURITY_AND_COMPLIANCE.md`

UI donor:

- `projects/tiktok-research-sorter/entrypoints/sidepanel/`

## Scope

Implement only these capabilities:

1. WXT + TypeScript + React + Tailwind + MV3 project shell.
2. Persistent Side Panel using the existing owner operator UI language.
3. Visible dynamic extension version from `chrome.runtime.getManifest().version`.
4. Dexie / IndexedDB database with explicit schema versioning.
5. `ChatGPTAdapter` capability framework.
6. Non-destructive ChatGPT session / capability detection.
7. Conversation metadata sync into local DB.
8. Workspace conversation browser reading from the local DB.
9. On-demand hydration / preview for one selected conversation.
10. Owner favorites and notes stored locally.
11. Title / local metadata search.
12. Health panel showing capability state.
13. Exportable diagnostics report without conversation content by default.
14. Cached workspace browsing must still work when live ChatGPT access becomes unavailable after a successful sync.

## Explicit Non-Scope

Do NOT implement:

- archive;
- delete;
- rename;
- bulk destructive operations;
- prompt library;
- semantic embeddings;
- BM25/vector recall;
- Claude/Gemini/Grok/Perplexity adapters;
- remote backend;
- telemetry;
- analytics;
- monetization;
- Chrome Web Store packaging work;
- unrelated UI redesign beyond the established owner Side Panel language.

## Architecture Contract

Do not create one giant content script.

Required structure should follow the intent below, with reasonable WXT naming adjustments allowed:

```text
src/core/
  models/
  db/
  search/
  organization/

src/providers/
  chatgpt/
    adapter.ts
    capabilities.ts
    api-strategy.ts
    dom-strategy.ts
    compatibility.ts

src/features/
  workspace/
  health/

entrypoints/
  sidepanel/
  content/
  background/
```

ChatGPT-specific endpoint names, selectors, parsing and session discovery must stay inside the ChatGPT provider layer.

Workspace UI and local DB code must depend on canonical models, not raw ChatGPT response shapes.

## Canonical Data

Use the canonical contracts from `TECHNICAL_ARCHITECTURE.md` as the starting point.

At minimum persist:

- provider conversation metadata;
- canonical messages hydrated on demand;
- owner conversation metadata;
- compatibility checks;
- settings.

Do not store the whole account as one JSON blob.

## Sync Behavior

### Metadata sync

A sync action should:

1. verify ChatGPT session/capability state;
2. list conversation metadata through the current validated live strategy;
3. normalize provider data;
4. upsert local records;
5. preserve all owner metadata;
6. update `lastSyncedAt`;
7. never delete local data merely because one sync does not return a conversation.

### Content hydration

Full conversation content must be fetched only when the user selects a conversation for preview in this slice.

Do not automatically hydrate every conversation.

Persist the normalized preview result locally so reopening the same conversation can use cached content unless an explicit refresh is requested or data is known stale.

## Capability Health

Implement non-destructive health states for at least:

- ChatGPT tab detected;
- session discovery;
- list conversations;
- read conversation;
- local DB;
- search index / local search;
- DOM navigator capability may be `unknown` or `not implemented` in Slice 1 if navigation itself is not implemented.

Use states:

- `healthy`;
- `degraded`;
- `unavailable`;
- `unknown`.

A live-provider failure must not crash the Side Panel or prevent reading cached local records.

## Donor Use

### Internal UI donor

Reuse/adapt Side Panel visual language and interaction patterns from:

`projects/tiktok-research-sorter/entrypoints/sidepanel/`

### fineanmol/chatgpt-bulk-delete-manager

May be used as a MIT-licensed reference/code donor for current conversation list and preview behavior.

Before copying any code:

- record exact repository commit;
- confirm LICENSE at that commit;
- extract only the relevant capability;
- do not inherit social/share UI or monolithic structure;
- rewrite into typed provider services where practical.

### world-wide-dev/chatgpt-export

May be used for MIT-licensed canonicalization / incremental persistence patterns.

Do not make hydration-aware DOM traversal the only acquisition strategy.

### Threadline / personal-ai-memory

Use only if needed for DB structure/search patterns in Slice 1.

Do not introduce embeddings or memory graph dependencies yet.

## Permissions

Keep host access initially limited to ChatGPT domains.

Use only permissions necessary for the implemented slice, likely including:

- `storage`;
- `sidePanel`;
- `activeTab`;
- `scripting` only if required by the actual implementation.

No unrelated host permissions.

## Local-First Runtime Rules

- no telemetry;
- no analytics;
- no vendor backend;
- no remote conversation storage;
- no embedded secret/API key;
- no sending conversation content outside the browser.

## UI Requirements

Header:

- product name;
- dynamic `vX.Y.Z`;
- ChatGPT adapter status;
- sync state.

Primary Slice 1 surfaces:

### Workspace

- conversation count;
- sync button;
- search box;
- conversation list;
- active/archived/project metadata when available;
- favorite toggle;
- note indicator;
- selected conversation preview.

### Health

- capability table/chips;
- last check time;
- sanitized diagnostic message/code;
- local DB schema version;
- export diagnostics button.

Do not overload the first slice with decorative features.

## Diagnostics Export

Export a JSON diagnostics file that excludes conversation titles/content by default.

Include:

- extension version;
- DB schema version;
- adapter version;
- capability states;
- timestamps;
- recent sanitized errors;
- sync counts;
- environment/browser basics if available without sensitive data.

## Tests

### Unit tests required

- provider conversation normalization;
- owner metadata preservation on sync;
- Dexie migration/open logic;
- local search filtering;
- capability health classification;
- diagnostics sanitization.

### Integration tests required where feasible

- mocked list response -> local DB;
- selected conversation -> normalized preview -> cache;
- provider unavailable -> cached workspace still loads.

### Real browser acceptance

Final validation must use an unpacked build in Chrome against the owner's actual ChatGPT session.

Do not claim completion based only on unit tests.

## Acceptance Criteria

Slice 1 is complete only when all of the following are true:

1. Extension loads unpacked without manifest/runtime errors.
2. Toolbar action opens the persistent Side Panel.
3. Side Panel visibly shows the manifest-derived version.
4. ChatGPT session/capability detection works on `chatgpt.com`.
5. Metadata sync stores conversations in IndexedDB.
6. Reloading Side Panel shows cached conversations without a mandatory full refetch.
7. Selecting one conversation hydrates and displays its preview.
8. Reopening the same preview can use cached canonical messages.
9. Favorite toggle persists across reload.
10. Notes persist across reload.
11. Search over local title/metadata works.
12. Health panel accurately reports live/local capability state.
13. If live ChatGPT access becomes unavailable after sync, cached workspace browsing still works.
14. Diagnostics export works and excludes conversation content by default.
15. No external backend/analytics traffic is introduced by our code.
16. Relevant tests pass.
17. Real browser behavioral verification is recorded after the final affecting change.

## Rollback / Safety

This slice must perform no destructive ChatGPT mutations.

If live endpoint assumptions prove unstable, disable the affected capability and keep local cached browsing operational rather than adding hidden workaround logic.

## Required Deliverables

- working source code;
- unpacked build output;
- test results;
- donor attribution/license notes for copied code;
- compatibility notes;
- browser acceptance evidence;
- update to `projects/chatgpt-workspace-manager/logs/latest.md` with final Slice 1 state;
- explicit list of blockers before Slice 2.

## Stop Condition

Do not start Slice 2 archive/delete work in the same implementation pass.

After Slice 1 is validated, stop and return the implementation result for review.
