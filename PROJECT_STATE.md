---
project_name: Project Execution OS
project_mode: compact
status: transfer_ready
updated_at: 2026-08-28
source_of_truth: repository
active_branch: main
---

# PROJECT_STATE.md

## Current State

`Project Execution OS` is active and transfer-ready.

The repository contains all four intended layers:

```text
domain knowledge
-> executable capability
-> workflow / application adapter
-> owner-facing UI
```

A new architecture research track is active: determine whether official Codex App Server / Codex harness interfaces can replace or simplify parts of the current manual/bridge-based worker handoff while preserving Project Execution OS ownership of routing, memory, approvals, review, and durable evidence.

Research task: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/113
Trigger reference: https://pimenov.ai/articles/codex-stanovitsya-platformoy-agent-vnutri-raboty/

This is research only. No runtime replacement, Prompt Bridge removal, or architecture migration is approved until primary-source evidence is reviewed.

## Latest Standards Milestone — 2026-08-28

The article `https://pimenov.ai/articles/vaybkoding-bez-bardaka/` was reviewed as a donor/reference against current Project Execution OS standards.

Gap analysis:

`docs/research/VIBECODING_WITHOUT_CHAOS_GAP_ANALYSIS_2026-08-28.md`

Accepted improvements were integrated into existing standards instead of creating a parallel “vibe coding” workflow:

- `docs/HARNESS_ENGINEERING_STANDARD.md` upgraded to v2;
- `docs/REVIEW_STANDARD.md` upgraded to v3.

New explicit central rules:

- bounded execution contract: `GOAL / USER-OBSERVABLE RESULT / CONTEXT / CHANGE / DO NOT TOUCH / VERIFY / ROLLBACK` for non-trivial implementation work when relevant;
- any affecting change after verification invalidates the previous verification for affected behavior;
- user-facing work requires behavioral evidence when reasonably possible, not only machine checks;
- UI verification uses the relevant subset of success path, failure state, persistence/refresh, console/network, desktop/mobile checks;
- vague “improve/clean up” instructions must be converted into bounded observable outcomes before broad changes;
- Git-backed implementation should inspect the final diff, preserve rollback, and prefer one coherent completed change per checkpoint;
- skills should be extracted from observed stable repetition rather than invented before the process stabilizes.

The donor's fixed documentation tree and one-hour setup sequence were not adopted as universal OS architecture. Existing routed bootstrap and progressive memory remain authoritative.

## Latest Confirmed Product Milestone

`Block Studio 0.1.0` was implemented and merged as the first local visual application for capability blocks.

```text
Application: apps/block-studio/
Windows launcher: START_BLOCK_STUDIO.bat
PR: https://github.com/oleg3479881328-code/Project-Execution-OS/pull/90
Merge SHA: d70fbb1be0d419b3dcc5b47a9d3dc107a9551069
Status: candidate
```

The first interactive capability is:

```text
media.probe 0.1.0 — candidate
```

Owner-visible behavior:

- registry-driven block library;
- drag-and-drop video/audio selection;
- local browser preview;
- normalized duration, dimensions, formats, codecs, FPS, audio, and stream data;
- owner and developer modes;
- raw JSON, logs, contract, tests, and usage views;
- local runtime storage and explicit cleanup.

## Verification Evidence

```text
Local pytest: 5 passed
JavaScript syntax: passed
Real local H.264/AAC MP4 API test: passed
Ubuntu / Python 3.13 / ffprobe: passed
Windows / Python 3.13 / ffprobe: passed
Project OS integrity workflow: passed
```

The automated Windows run confirms package installation, ffprobe availability, file upload, capability execution, preview retrieval, and cleanup.

## Architecture Decisions

Applications may present and compose capabilities, but must not copy provider implementation logic.

```text
apps/block-studio
-> Python entry-point discovery
-> media.probe contract
-> media.probe core
-> ffprobe
```

New capability manifests and registry entries are visible in the Studio library. A block becomes interactive when an application adapter is added.

For worker orchestration, the existing OS architecture remains authoritative while Issue #113 evaluates official Codex runtime/harness surfaces under Existing Solution First. The research must distinguish what Codex can own from what must remain Project Execution OS responsibility.

## Current Focus

- Research Issue #113: official Codex App Server / Harness integration surface and fit with Project Execution OS.
- Apply the strengthened bounded-execution and verification rules to future implementation work.
- Owner test on the target Windows computer with a real user-owned file.
- Keep Block Studio and `media.probe` at `candidate` until that confirmation is received.
- Build `media.clip` as the second capability and add its interactive Studio page.
- Extract shared SDK code only after real duplication appears between two blocks.

## Current Next Safe Actions

```text
Architecture track:
1. Execute Issue #113 as bounded evidence-gathering research.
2. Review the report against official primary sources.
3. Only after review decide whether a small Codex App Server proof of concept is justified.

Capability track:
1. Open Block Studio on the owner's Windows computer.
2. Load a real MP4.
3. Run media.probe and inspect the visible result.
4. Record success or exact failure.
5. Begin media.clip.
```

## Active Files For Re-entry

1. `START_HERE.md`
2. `docs/ROUTER.md`
3. `PROJECT.md`
4. `PROJECT_STATE.md`
5. `logs/latest.md`
6. `docs/HARNESS_ENGINEERING_STANDARD.md`
7. `docs/REVIEW_STANDARD.md`
8. `docs/research/VIBECODING_WITHOUT_CHAOS_GAP_ANALYSIS_2026-08-28.md`
9. `docs/CODEX_HANDOFF_STANDARD.md`
10. Issue #113 — Codex App Server / Harness research
11. `apps/README.md`
12. `apps/block-studio/README.md`
13. `apps/block-studio/VALIDATION.md`
14. `capability-library/REGISTRY.md`
15. `capabilities/media-probe/BLOCK.md`
16. `docs/COMPOSABLE_CAPABILITY_BLOCKS_STANDARD.md`

## Known Blockers

- Codex App Server / Harness fit has not yet been verified against current official OpenAI sources; Issue #113 is open.
- The owner has not yet run Block Studio on the target Windows computer.
- A real owner-owned media file has not yet been confirmed through the UI.
- Variable-frame-rate media remains an additional edge-case fixture.
- Other media capability entries remain `idea`.

## Do-Not-Break Rules

- Do not replace or delete the current worker handoff/Prompt Bridge based only on the discovery article.
- Do not treat Codex App Server integration as approved until Issue #113 evidence is reviewed.
- Do not claim owner validation without the owner's explicit result.
- Do not copy capability provider code into Block Studio.
- Do not expose Block Studio beyond `127.0.0.1` by default.
- Do not retain temporary owner files after explicit cleanup.
- Do not promote `media.probe` or Block Studio beyond registry evidence.
- Do not extract a common SDK from one block alone.
- Do not preserve a validated state after an affecting post-verification change without re-running relevant checks.
- Do not interpret vague improvement requests as permission for unbounded refactoring.
- Update this file and `logs/latest.md` after every meaningful central-project change.
