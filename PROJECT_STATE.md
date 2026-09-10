---
project_name: Project Execution OS
project_mode: compact
status: transfer_ready
updated_at: 2026-09-09
source_of_truth: repository
active_branch: main
---

# PROJECT_STATE.md

## Current State

`Project Execution OS` is active and transfer-ready.

The canonical top-level architecture is now explicit:

```text
Project Execution OS — control plane
  -> owner intent / routing / context / policy / memory ownership / review / evidence / continuity

        ↓ governs

domain knowledge
-> executable capability
-> workflow / application adapter
-> owner-facing UI
```

The 2026-09-09 top-down architecture audit confirmed that the current routed architecture should be kept. No fixed five-box rewrite, monolithic kernel, or competing startup architecture is justified.

Canonical audit:

`docs/research/PEOS_TOP_DOWN_ARCHITECTURE_AUDIT_2026-09-09.md`

`PROJECT.md` now explicitly owns the high-level architecture map, canonical truth-ownership map, and readiness/evidence boundary.

Two cross-cutting maturity rules are now explicit:

1. every durable truth type has one canonical owner; other surfaces may link, summarize, index, cache or render it but must not silently become parallel truth;
2. external-tool architectural role and proof/readiness are separate dimensions, so `researched`, `connected`, `technically proven`, `workflow proven`, and `owner confirmed` cannot be conflated.

Internal capability readiness remains owned by `capability-library/REGISTRY.md`. Reusable knowledge lifecycle remains owned by `docs/KNOWLEDGE_SYSTEM.md`. External tool/stack adoption status remains owned by `docs/TOOL_STACK_AUDIT.md`.

A new architecture research track is active: determine whether official Codex App Server / Codex harness interfaces can replace or simplify parts of the current manual/bridge-based worker handoff while preserving Project Execution OS ownership of routing, memory, approvals, review, and durable evidence.

Research task: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/113
Trigger reference: https://pimenov.ai/articles/codex-stanovitsya-platformoy-agent-vnutri-raboty/

This is research only. No runtime replacement, Prompt Bridge removal, or architecture migration is approved until primary-source evidence is reviewed.

## Latest Architecture Milestone — 2026-09-09 — Top-Down Audit

Audit scope:

```text
control plane
knowledge
actionable capabilities
workflow / composition
applications / UI
canonical ownership
readiness / evidence
```

Verdict:

```text
KEEP CURRENT ARCHITECTURE
NO STRUCTURAL REWRITE
MAKE OWNERSHIP AND READINESS BOUNDARIES EXPLICIT
```

Accepted changes:

- `PROJECT.md` now states that Project Execution OS is the logical control plane around four application/execution layers;
- the control plane owns intent, routing, context rules, standards/policy, durable project-memory ownership, approvals/review, evidence/readiness semantics, and transfer continuity;
- external runtimes remain optional execution planes and replaceable implementation surfaces;
- a canonical ownership map now names the authoritative owner for system entry, navigation, architecture, project state, standards, knowledge, capability readiness, external tool adoption status, application orchestration, and durable file assets;
- internal capability readiness keeps the existing `idea -> candidate -> validated -> production -> deprecated -> retired` lifecycle;
- external tools keep architectural adoption role separate from evidence state;
- the second-opinion five-part model was accepted only as an explanatory lens, not as a replacement physical architecture.

Rejected changes:

- fixed-depth or fixed-five-part hierarchy;
- monolithic central kernel;
- new parallel startup workflow;
- moving canonical project memory into ChatGPT/Codex/Notion/another interface by default;
- treating researched external tools as operational capabilities;
- creating a new lifecycle standard where existing canonical artifacts already own the behavior.

## Latest Integration Milestone — 2026-08-30 — Archify Candidate

Upstream reviewed:

`https://github.com/tt-a1i/archify`

Canonical integration note:

`docs/integrations/archify/README.md`

Decision:

```text
ADOPT FOR PILOT
DO NOT REIMPLEMENT
DO NOT PROMOTE TO ACTIVE UNTIL VERIFIED
DO NOT REGISTER AS AN INTERNAL CAPABILITY YET
```

Archify is treated as an external architecture-visualization / architecture-evidence candidate, not as a Project Execution OS capability block. Project Execution OS keeps ownership of routing, standards, durable memory, approvals, review policy, capability readiness, and verified project state.

First pilot:

https://github.com/oleg3479881328-code/Project-Execution-OS/issues/132

The pilot will map Project Execution OS itself using the canonical `START_HERE.md -> docs/ROUTER.md` path and the four-layer architecture, with typed/validated Archify output and explicit truth boundaries. Promotion requires successful tool validation plus human confirmation that the map improves orientation without inventing topology.

## Latest Standards Milestone — 2026-08-29 — Knowledge Promotion Gate

The existing knowledge/memory/review architecture was strengthened without adding a parallel standard.

Updated:

- `docs/KNOWLEDGE_SYSTEM.md` -> v3;
- `docs/REVIEW_STANDARD.md` -> v4;
- `docs/PROJECT_MEMORY_STANDARD.md` -> explicit promotion-gate responsibility.

New central rule:

```text
meaningful work
-> ask whether anything has durable future value
-> classify the result
-> update the narrowest correct existing canonical artifact first
-> create a new artifact only when responsibility is genuinely distinct
```

Routing now distinguishes:

- current fact / blocker / next action -> state or log;
- decision -> project decision / ADR-style record;
- verified failure + fix -> verified technical solution / known-fix entry / runbook;
- repeatable procedure -> SOP / checklist / runbook / playbook;
- reusable pattern -> project knowledge first, central knowledge after review;
- mandatory cross-task rule -> existing standard first, new standard only when necessary;
- reusable executable behavior -> skill / capability;
- raw external idea/reference -> reference capture.

No mechanical rule such as "second repetition = standard" was adopted. Promotion depends on evidence, reuse value, stability, scope, and risk.

The executor is responsible for running this gate during normal work; the owner should not need to repeatedly request preservation or standardization.

## Previous Standards Milestone — 2026-08-29 — DeepSeek Harness Extraction

Official donor/reference reviewed:

`https://github.com/deepseek-ai/deepseek-harness`

Extraction audit:

`docs/research/DEEPSEEK_HARNESS_EXTRACTION_AUDIT_2026-08-29.md`

`docs/HARNESS_ENGINEERING_STANDARD.md` upgraded to v3.

Accepted central runtime rules:

- model-visible runtime state must be reconstructable from durable state when replay/resume matters;
- reusable runtime capabilities should separate Service Definition / Provider / Consumer;
- safety-critical runtime behavior fails closed rather than silently degrading;
- reusable tool runtimes should prefer one shared policy/guard/approval/execute/post-process/result pipeline;
- execution/security policy should be resolved per call when sessions or workers can differ;
- partial enforcement must not be presented as full enforcement;
- incomplete/crashed work must recover as interrupted/unknown/failed, never silently successful;
- resumable delegated workers should preserve durable lineage/delegation identity when runtime support exists;
- unsupported provider capabilities must reject loudly rather than be silently ignored.

Architecture decision:

```text
Project Execution OS = control plane
external harness/runtime = optional execution plane
```

Project Execution OS keeps ownership of owner intent, routing, project standards, durable project memory, approvals/review policy, and durable business evidence.

DeepSeek Harness is an integration candidate for lower runtime concerns such as model calls, tool execution, sandbox enforcement, runtime session persistence, and child-agent execution.

No current Project Execution OS component was replaced or deleted by this audit. Cordis-specific topology, self-modification behavior, and DeepSeek pre-release compatibility policy were explicitly not adopted as universal OS rules.

## Previous Standards Milestone — 2026-08-28

The article `https://pimenov.ai/articles/vaybkoding-bez-bardaka/` was reviewed as a donor/reference against current Project Execution OS standards.

Gap analysis:

`docs/research/VIBECODING_WITHOUT_CHAOS_GAP_ANALYSIS_2026-08-28.md`

Accepted improvements were integrated into existing standards instead of creating a parallel “vibe coding” workflow:

- `docs/HARNESS_ENGINEERING_STANDARD.md` upgraded to v2, now superseded by v3;
- `docs/REVIEW_STANDARD.md` upgraded to v3.

New explicit central rules from that milestone:

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

DeepSeek Harness is now a second official donor/reference for the execution-plane architecture. It does not authorize a competing migration track. Findings from DeepSeek and Issue #113 must be reconciled before any runtime POC is promoted beyond an isolated experiment.

Archify is an orthogonal visualization/evidence candidate. It must not be confused with the execution-plane choice or used to infer runtime behavior that has not been established independently.

## Current Focus

- Preserve the clarified control-plane / canonical-ownership / readiness boundaries in future architecture work.
- Apply external-tool evidence state only where it affects routing, execution, cost, security, or readiness claims; do not mass-create registry ceremony.
- Research Issue #113: official Codex App Server / Harness integration surface and fit with Project Execution OS.
- Reconcile DeepSeek Harness donor findings with the Codex research before choosing any execution runtime.
- Run Issue #132: Archify self-map pilot against Project Execution OS and keep Archify at `CANDIDATE` until evidence exists.
- Apply Harness Engineering Standard v3 to future reusable/runtime work.
- Owner test on the target Windows computer with a real user-owned file.
- Keep Block Studio and `media.probe` at `candidate` until that confirmation is received.
- Build `media.clip` as the second capability and add its interactive Studio page.
- Extract shared SDK code only after real duplication appears between two blocks.

## Current Next Safe Actions

```text
Architecture track:
1. Treat PROJECT.md as canonical high-level architecture owner.
2. When docs/TOOL_STACK_AUDIT.md is next materially updated, record evidence state for tools where readiness ambiguity matters; do not perform a ceremonial mass migration.
3. Complete/review Issue #113 against official OpenAI primary sources.
4. Compare Codex runtime capabilities with the DeepSeek Harness extraction audit.
5. Run the independent Archify self-map pilot from Issue #132; do not treat it as an execution-runtime decision.
6. Define one execution-plane candidate matrix.
7. Only then decide whether one isolated read-only runtime POC is justified.

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
6. `docs/research/PEOS_TOP_DOWN_ARCHITECTURE_AUDIT_2026-09-09.md`
7. `docs/HARNESS_ENGINEERING_STANDARD.md`
8. `docs/research/DEEPSEEK_HARNESS_EXTRACTION_AUDIT_2026-08-29.md`
9. `docs/REVIEW_STANDARD.md`
10. `docs/research/VIBECODING_WITHOUT_CHAOS_GAP_ANALYSIS_2026-08-28.md`
11. `docs/CODEX_HANDOFF_STANDARD.md`
12. Issue #113 — Codex App Server / Harness research
13. `docs/integrations/archify/README.md`
14. Issue #132 — Archify self-map pilot
15. `apps/README.md`
16. `apps/block-studio/README.md`
17. `apps/block-studio/VALIDATION.md`
18. `capability-library/REGISTRY.md`
19. `capabilities/media-probe/BLOCK.md`
20. `docs/COMPOSABLE_CAPABILITY_BLOCKS_STANDARD.md`
21. `docs/TOOL_STACK_AUDIT.md`

## Known Blockers

- External tool inventory does not yet consistently expose a separate evidence-state field; the architectural rule is now explicit, but normalization should happen only during meaningful tool-audit updates rather than by ritual mass editing.
- Codex App Server / Harness fit has not yet been verified against current official OpenAI sources; Issue #113 is open.
- DeepSeek Harness is rapidly evolving, so direct runtime integration has upgrade-churn risk.
- No execution-plane POC has yet proved that a third-party harness deletes enough custom orchestration to justify adoption.
- Archify has not yet passed the Project Execution OS self-map pilot; it remains `CANDIDATE`, not ACTIVE.
- The owner has not yet run Block Studio on the target Windows computer.
- A real owner-owned media file has not yet been confirmed through the UI.
- Variable-frame-rate media remains an additional edge-case fixture.
- Other media capability entries remain `idea`.

## Do-Not-Break Rules

- Do not replace the recursive routed architecture with a fixed five-box physical hierarchy.
- Do not create a monolithic control-plane file or runtime merely to mirror the conceptual architecture.
- Do not create parallel truth when an existing canonical owner exists.
- Do not treat an external tool's adoption role as proof that it is accessible, technically proven, workflow proven, or owner confirmed.
- Do not replace or delete the current worker handoff/Prompt Bridge based only on donor research.
- Do not start competing DeepSeek and Codex runtime migrations in parallel.
- Do not treat DeepSeek Harness integration as approved production architecture without an isolated evidence-backed POC.
- Do not treat Archify as an execution runtime or source of canonical project truth.
- Do not promote Archify to ACTIVE or register it as an internal capability block without pilot evidence.
- Do not treat partial sandbox enforcement as full protection.
- Do not silently downgrade unsupported runtime/provider capabilities.
- Do not recover interrupted execution as successful execution without fresh evidence.
- Do not claim owner validation without the owner's explicit result.
- Do not copy capability provider code into Block Studio.
- Do not expose Block Studio beyond `127.0.0.1` by default.
- Do not retain temporary owner files after explicit cleanup.
- Do not promote `media.probe` or Block Studio beyond registry evidence.
- Do not extract a common SDK from one block alone.
- Do not preserve a validated state after an affecting post-verification change without re-running relevant checks.
- Do not interpret vague improvement requests as permission for unbounded refactoring.
