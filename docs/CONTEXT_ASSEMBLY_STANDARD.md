# Context Assembly Standard v2

## Purpose

This standard defines how a human or AI participant assembles the minimum sufficient, trustworthy context needed to perform a specific action through `Project Execution OS`.

Its goal is to reduce confusion, unnecessary context expansion, duplicated work and avoidable token cost while preserving the evidence needed for correct decisions and execution.

## Core Rule

Use the smallest sufficient context package for the active task.

```text
Enter through the stable door.
Route through the live internal map.
Load only what the route and task require.
Do not load the whole system or whole project by default.
```

This standard is model-agnostic. It applies to ChatGPT, Codex, DeepSeek, Claude, local models and future API-based agents.

## Context Layers

Use these layers only when applicable to the current task:

```text
0. Stable system instruction / integration prompt
1. START_HERE.md stable top-level entrypoint
2. docs/ROUTER.md live internal router
3. Relevant Project Execution OS standard or block selected by route
4. Project entrypoint and current durable evidence, when a project is involved
5. Minimum task-specific files, artifacts or evidence
6. Relevant reusable knowledge, skills or blocks only when triggered by the task
7. Current user instruction, new error, current log or immediate execution input
```

The presence of a later layer does not justify loading every artifact in earlier or adjacent layers.

## Layer Rules

### Layer 0 — Stable System Instruction

A connected assistant or automation may have a short stable system-layer instruction that requires entry through `START_HERE.md`.

Do not copy evolving workflow logic, project state or large knowledge libraries into the stable system instruction.

### Layer 1 — Stable Top-Level Entrypoint

Always enter project-related work through `START_HERE.md`.

`START_HERE.md` must remain minimal and durable. Its role is to point to the current internal router, not to store the growing route catalogue.

### Layer 2 — Live Internal Router

Open `docs/ROUTER.md` and follow only the narrowest route relevant to the current work.

The router may evolve as the system grows. Do not read every route target or every internal standard by default.

### Layer 3 — Relevant System Standard Or Block

Read the smallest internal node that governs the active work, for example:

- lifecycle or storage decision -> `docs/PROJECT_LIFECYCLE_MODEL.md`;
- research -> `docs/RESEARCH_STANDARD.md`;
- review -> `docs/REVIEW_STANDARD.md`;
- central knowledge work -> `docs/KNOWLEDGE_SYSTEM.md`;
- Codex execution handoff -> `docs/CODEX_HANDOFF_STANDARD.md`;
- connected-agent communication or channel selection -> `blocks/communication-channel/BLOCK.md`;
- detailed AI coordination policy or channel registry -> `docs/AI_COORDINATION_HUB_STANDARD.md`.

Read additional standards only when the task actually crosses into their scope.

### Layer 4 — Project Entrypoint And Durable Evidence

When work concerns a specific project, read that project's current entrypoint first.

The entrypoint should tell the participant what the project is, where truth lives, what matters now, what constraints apply and what to read next.

Do not replace project entrypoint use by indiscriminately reading an entire repository, full chat history or complete log archive.

The intended sequence is:

```text
START_HERE.md
→ docs/ROUTER.md
→ PROJECT.md for the specific project
→ existing project index if useful
→ minimum additional files needed for the task
```

### Project Index Rule

Before mass scanning a project, check whether a useful existing index already exists.

If the project has grown enough that a useful index is missing, create a minimal one.

After a meaningful structural change, update the index.

Do not create an index ritualistically for an empty project.

### Layer 5 — Task-Specific Evidence

Load only the files and evidence needed to perform or verify the active action.

Examples:

- bug fixing -> failing log, related source files, relevant validation path;
- design update -> current interface files, chosen reference and acceptance criteria;
- architecture review -> current architecture artifacts, decision registry and relevant standards;
- execution -> bounded handoff packet, allowed files and validation checks.

### Layer 6 — Reusable Knowledge, Skills And Blocks

Use central reusable knowledge only when the current task may benefit from a reviewed cross-project solution or pattern.

Use a skill, plugin, domain block or reusable agent artifact only when it is relevant to the active objective and allowed scope.

Do not load the complete `knowledge-library/`, `skills/`, `agent-library/` or `blocks/` trees into routine work.

### Layer 7 — Live Input

Put the current request, current error, new log output or immediate execution instruction last in the working context whenever practical.

This makes the active change visible without destabilizing the reusable foundation of the context package.

## Context Selection Rule

Before loading an additional artifact, answer:

1. Does the active route require this artifact?
2. Does the project entrypoint point to it?
3. Does the current task require it for correctness, evidence or execution?
4. Does a reviewed reusable solution apply to the task?

If none of these is true, do not load it.

## Anti-Bloat Rule

Do not create context packages made of:

- entire repositories without a task-specific reason;
- complete historical chat dumps;
- every system standard at once;
- unreviewed reference collections;
- all knowledge, skills or templates merely because they exist;
- stale project files that are not required for the current action.

A large context is not a better context unless each major component has a reason to be present.

## Codex And Executor Context Rule

When execution is already decided and an executor is needed, use `docs/CODEX_HANDOFF_STANDARD.md`.

Codex or another execution agent should receive a bounded payload defining objective, allowed scope, forbidden changes, relevant repository context, acceptance criteria and validation requirements.

Do not use an executor to rediscover open-ended context that a reasoning model can assemble first.

## Knowledge Integration Rule

Central knowledge loading follows `docs/KNOWLEDGE_SYSTEM.md`.

Only reviewed and relevant knowledge should be loaded as active reusable guidance. Candidates and raw references may be read for research or review, but must not silently become operational rules.

## API And Cache-Aware Extension

When an API-based orchestrator is later used, the context package should be assembled deterministically where practical:

```text
stable system instruction
→ START_HERE.md stable door
→ docs/ROUTER.md live internal map
→ selected routed standards or blocks
→ stable project orientation when applicable
→ selected reusable knowledge or skill guidance
→ current project evidence
→ live instruction / new error / new log
```

For prefix-caching providers, this ordering can increase reuse of stable leading content. It must not be treated as permanent memory or guaranteed cache reuse.

An API implementation should, where available, log:

- model and provider;
- system/context version or commit reference;
- selected route and loaded modules;
- input/output token usage;
- cache-hit and cache-miss token counts;
- estimated or billed cost;
- task/project identifier when appropriate.

## Evidence That Motivated Immediate Adoption

On 2026-05-29, the owner supplied a screenshot of actual DeepSeek Platform usage for `deepseek-v4-flash` showing a high cache-hit ratio on a displayed daily workload:

```text
Displayed date: 2026-05-28
Input (Cache hit): 13,139,328 tokens
Input (Cache miss): 910,696 tokens
Output: 114,098 tokens
Input cache-hit share: approximately 93.5%
```

This evidence establishes that cache-aware context design has material economic relevance in the owner's real API usage. It does not establish which specific content produced those cache hits, and it does not replace provider documentation or future runtime logging.

## Review Rule

Review should check:

- whether required context was missing;
- whether unnecessary context was loaded;
- whether stale or unreviewed knowledge was treated as active guidance;
- whether executor context was adequately bounded;
- whether API context assembly remains measurable when costs or caching matter;
- whether `START_HERE.md` stayed minimal and internal route growth remained inside `docs/ROUTER.md`.

## Related Nodes

- `START_HERE.md`
- `docs/ROUTER.md`
- `docs/PROJECT_ENTRYPOINT_STANDARD.md`
- `docs/REPOSITORY_MEMORY_STANDARD.md`
- `docs/KNOWLEDGE_SYSTEM.md`
- `docs/RESEARCH_STANDARD.md`
- `docs/REVIEW_STANDARD.md`
- `docs/CODEX_HANDOFF_STANDARD.md`
- `blocks/communication-channel/BLOCK.md`
- `docs/AI_COORDINATION_HUB_STANDARD.md`

## Final Rule

The system must not depend on an AI reading everything.

It must enable an AI to enter through one stable door, follow one live internal map and load the smallest trustworthy context sufficient for the current action.

For project work, enter through `START_HERE.md` and `docs/ROUTER.md` first.
Then read the specific project's `PROJECT.md`, the project index if one exists,
and only the minimum additional files needed for the active task.
