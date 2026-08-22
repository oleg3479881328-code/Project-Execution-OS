# Canonical Live State & Checkpoint Standard

## Purpose

This standard defines how every meaningful project under Project Execution OS preserves current state, history, checkpoints, and migration/handoff artifacts without turning chat boundaries into documentation boundaries.

The goal is simple: one current truth, minimal duplication, and recoverable history.

## Constitutional Rule

A chat boundary is not a project-state boundary.

Ending a chat, opening a new chat, changing model, or resuming after a short pause does **not** by itself justify a new migration page, handoff snapshot, or checkpoint.

Every active project maintains exactly one canonical **live Current State** artifact appropriate to its natural system.

## Canonical Live State

Canonical forms include:

- repository-first: `PROJECT_STATE.md`;
- Notion-first: one `Current State` page or explicitly declared current-state block;
- another system only when the project explicitly declares that system as canonical.

The live Current State answers only the present-tense question:

> Where is the project now, what is verified, what is risky, and what is the next safe action?

It should contain, as applicable:

- current objective and phase;
- verified working state;
- active artifacts, branches, PRs, deployments, datasets, automation, or external systems;
- open blockers and risks;
- do-not-repeat constraints;
- superseded or obsolete paths/decisions that could mislead a new executor;
- next exact step;
- `Last verified` date/time or equivalent evidence marker.

Do not reconstruct current state by reading a chain of historical migration snapshots.

## START HERE vs Current State

The project entrypoint (`PROJECT.md`, `START HERE`, or equivalent) is a stable router.

It changes only when one of these changes:

- project identity or scope;
- canonical source of truth;
- routing to current state;
- mandatory reading;
- precedence rules.

The live Current State is dynamic and changes whenever the execution state, blocker, risk, or next safe action changes.

Do not turn the entrypoint into a running diary.

## Work Log and Decision Log

History belongs in the correct durable layer:

- **Work / Change Log** — what happened, what was tested, what changed;
- **Decision Log** — why an important choice was made and what it supersedes;
- **Git** — code and version history where appropriate;
- **Checkpoints** — rare immutable recovery/audit points.

The live Current State summarizes the result of history. It does not reproduce the entire sequence.

## Supersedes / Obsolete Rule

When a current URL, architecture, workflow, source, branch, editor, database path, or decision replaces an older one, record the obsolete item explicitly under `Superseded / Obsolete` (or equivalent) in the live Current State until the risk of accidental reuse is gone.

Do not leave two apparently canonical active paths without marking which one wins.

## Checkpoint Rule

Create an immutable checkpoint only when preserving an exact transition state has real recovery, audit, or handoff value.

Typical triggers:

- before a major architecture migration;
- before a destructive or high-risk database/schema change;
- before replacing a production system or editor;
- before a major release or irreversible content migration;
- before moving between environments, owners, executors, or platforms when an exact handoff state matters;
- before another change where rollback or forensic comparison may be needed.

A checkpoint is frozen after creation.

Later corrections belong in:

- the live Current State;
- the Work/Decision Log;
- or a newer checkpoint.

Never silently rewrite historical checkpoints to make them match the present.

## Migration / Handoff Rule

A migration or handoff package is a **transport artifact**, not the primary memory layer.

Create one only when context actually crosses a meaningful boundary such as:

- system or environment migration;
- executor/owner transfer where the live state alone is insufficient;
- major phase boundary requiring a frozen handoff;
- export/import between tools or platforms.

Migration/handoff artifacts never outrank the canonical live Current State.

If an old migration snapshot conflicts with newer verified Current State, the live state wins unless the project explicitly documents a different precedence for a specific recovery operation.

## Chat-Boundary Rule

At the end of an ordinary chat or work segment:

1. update the live Current State if status, risk, or next action changed;
2. update the Work Log if meaningful work or verification happened;
3. promote reusable knowledge to the correct global/project standard if applicable;
4. do **not** create a new migration/checkpoint merely because the conversation ended.

The same rule applies when opening a new chat.

## Re-Entry Sequence

A new executor should restore project context in this order:

```text
1. project entrypoint
2. canonical live Current State
3. current Work Log or latest relevant checkpoint
4. only task-relevant decisions/standards/deep knowledge
5. raw sources only when needed
```

Historical migration snapshots are not part of the default reading path unless the current state explicitly points to one for a recovery or audit reason.

## Anti-Bureaucracy Rule

Minimum durable structure for a serious active project remains:

```text
one entrypoint
one live Current State
```

Add Work Log, Decisions, Checkpoints, GitHub, Drive, databases, or other layers only when the project actually needs them.

Do not create empty documentation structures in advance.

## Adoption Rule for Existing Projects

For an existing project:

1. identify the real current source of truth;
2. choose one canonical entrypoint;
3. choose one canonical live Current State;
4. mark stale competing entrypoints/states as obsolete;
5. stop creating chat-by-chat migration snapshots;
6. move ongoing chronology to a Work Log;
7. move important rationale to a Decision Log;
8. preserve only meaningful transition snapshots as immutable checkpoints;
9. record `Last verified` and the next exact action;
10. run the Project Memory Health Test.

Do not delete historical migration artifacts merely because they are no longer canonical; archive or label them clearly.

## Final Rule

**One live state. Rare immutable checkpoints. Migration only for real transfer. Chat is not a state boundary.**
