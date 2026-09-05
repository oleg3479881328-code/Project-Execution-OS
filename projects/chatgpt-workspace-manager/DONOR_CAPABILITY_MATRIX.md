# ChatGPT Workspace Manager — Donor Capability Matrix

## Purpose

Map proven external and internal donors to individual capabilities before implementation.

Rule: do not fork one monolithic extension. Reuse architecture, patterns, and licensed code selectively. Re-implement unlicensed or structurally weak donors cleanly.

## Selection Criteria

A donor is valuable when it provides one or more of:

- current ChatGPT compatibility;
- a clearly useful capability;
- compatible license;
- local-first behavior;
- understandable architecture;
- low external-service dependency;
- patterns that can be isolated behind our own interfaces.

## Matrix

| Capability | Primary donor | License / reuse status | What to reuse | What not to inherit |
|---|---|---|---|---|
| Owner Side Panel shell | `projects/tiktok-research-sorter/entrypoints/sidepanel/` | Internal canonical donor | Side Panel shell, owner UI DNA, visible version, progress/status patterns | TikTok-specific logic |
| Framework / product shell | Project Execution OS Chrome Extension Block | Internal standard | WXT + TypeScript + React + Tailwind + MV3 | N/A |
| Live conversation list | `fineanmol/chatgpt-bulk-delete-manager` | MIT | endpoint flow, list pagination ideas, local execution model | monolithic `content.js`, growth/share UI |
| Live conversation preview | `fineanmol/chatgpt-bulk-delete-manager` | MIT | on-demand conversation hydration and chronological thread reconstruction | direct coupling to its dashboard |
| Archive / delete | `fineanmol/chatgpt-bulk-delete-manager` | MIT | PATCH semantics, local-only execution, sequential action model | hard-coded product structure |
| Bulk throttling / verification | `fineanmol/chatgpt-bulk-delete-manager` + `qcrao/bulk-delete-chatGPT` | MIT for fineanmol; qcrao is reference-only unless license is clarified | queue concepts, delay, verify, pause-on-limit behavior | analytics / identity / external backend from qcrao; no copying unlicensed code |
| Conversation canonicalization | `world-wide-dev/chatgpt-export` | MIT | extract -> normalize -> persist -> export separation; message-level canonical model | making hydration DOM traversal the only source |
| Incremental local persistence | `world-wide-dev/chatgpt-export` | MIT | idempotent incremental updates, stable message identifiers, snapshot regeneration | tight dependence on current DOM hydration behavior |
| Local DB / memory | `terra901/Threadline` | Apache-2.0 | IndexedDB/Dexie patterns, session model, local memory graph, recall UI ideas | Plasmo shell; provider capture logic as-is |
| Hybrid local search / RAG | `marswangyang/personal-ai-memory` + Threadline | Apache-2.0 | BM25/vector hybrid search, local embeddings, Transformers.js/WASM architecture | automatic capture assumptions until separately validated |
| ZIP / Markdown / assets export | `OwlCt/ChatGPT-Export` | MIT | ZIP layout, filename sanitization, attachment organization, Markdown conversion, offline reader patterns | private-API exporter as the sole acquisition path |
| Official ChatGPT export import | OpenAI data export + our importer | first-party data source | parse official ZIP/conversation JSON into canonical model | treating manual export as daily sync mechanism |
| Long-chat navigation | `manxisuo/ChatGPTLongConversationToolkit`, `grayfallstown/Elegant-ChatGPT-Navigation`, `BhriguKumarDeka/ChatGPT_PromptNavigate` | license must be verified per repo before code reuse; Elegant/PromptNavigate previously identified MIT | navigation UX, bookmarks, search, jump rail, headings/code blocks | code reuse before license verification |
| Prompt library | `carlosguadian/universal-prompt-library` | MIT | folders, variables, favorites, drag/drop concepts | cross-site permissions not needed for first ChatGPT-only build |
| Feature coverage benchmark | Superpower for ChatGPT, AI Toolbox, Simple Folder | specification donors | feature inventory, UX patterns, gaps to avoid | source/code assumptions; paid/product telemetry architecture |

## Strongest Donors

### 1. Internal Side Panel donor

Use our existing owner-operated Side Panel visual and interaction language as the application shell.

Reason:

- already used in Project Execution OS;
- avoids another custom operator UI;
- already aligned with visible version, status chips and persistent progress.

### 2. fineanmol/chatgpt-bulk-delete-manager

Current value:

- MIT licensed;
- Manifest V3;
- local execution;
- current ChatGPT private endpoint mapping;
- conversation list;
- preview;
- archive;
- delete;
- Markdown backup;
- sequential safety delays.

Use as the primary live-action donor, not as the product foundation.

Structural weakness:

- much of the application is concentrated in one large `content.js`;
- therefore extract capability logic into our own typed adapters/services instead of forking the application.

### 3. world-wide-dev/chatgpt-export

Use as canonical-data and persistence donor.

Strong ideas:

- semantic representation instead of DOM cloning;
- message-level persistence;
- idempotent extraction;
- incremental update;
- deterministic derived exports.

### 4. Threadline + personal-ai-memory

Use as local memory/search donor family.

Strong ideas:

- IndexedDB local memory;
- branch-aware conversation model;
- local embeddings;
- Hybrid RAG;
- recall and context selection;
- no remote AI backend required for semantic memory.

### 5. OwlCt/ChatGPT-Export

Use as backup/export/import donor.

Strong ideas:

- project-aware archive structure;
- Markdown + raw JSON dual representation;
- attachments and images;
- ZIP organization;
- local offline reader.

## Reference-only Donors

### qcrao/bulk-delete-chatGPT

Useful for:

- adaptive delay concepts;
- batch cooldown;
- post-operation verification;
- multi-language DOM fallback strategies.

Do not copy code unless licensing is explicitly clarified.

### Superpower / AI Toolbox / Simple Folder

Use only to benchmark feature coverage and operator UX.

## Rejected Approaches

### Fork one donor and expand it

Rejected because:

- no donor owns all needed capabilities;
- architecture quality varies dramatically;
- it would import unnecessary permissions, telemetry, backend, UI and coupling;
- future ChatGPT compatibility would remain tangled with product logic.

### Make the private ChatGPT API the core data model

Rejected.

Private APIs are an adapter strategy only. Workspace Core must operate against our canonical provider-independent contracts.

### DOM-only architecture

Rejected.

DOM remains a fallback and a live-navigation source, not the only path for list/read/action behavior.

## Proposed Capability Ownership

```text
src/core/
  models/
  db/
  search/
  organization/
  backup/
  operations/

src/providers/
  chatgpt/
    adapter.ts
    capabilities.ts
    api-strategy.ts
    dom-strategy.ts
    export-import-strategy.ts
    compatibility.ts

src/features/
  workspace/
  bulk/
  navigator/
  memory/
  prompts/

entrypoints/
  sidepanel/
  content/
  background/
```

## Donor Gate Before Code Copy

For every borrowed implementation:

1. identify exact repository and commit;
2. verify license at that commit;
3. identify exact files / algorithms being reused;
4. record attribution if required;
5. remove external analytics/backends unless explicitly needed;
6. adapt into our interfaces instead of importing donor architecture wholesale;
7. add a regression test for the capability.

## Current Decision

The donor search is sufficient to begin technical architecture. Continue targeted donor inspection only when implementing a specific capability or when a capability has no validated donor.
