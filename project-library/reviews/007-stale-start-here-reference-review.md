# Review 007 — Stale START_HERE Reference Review

## Date

`2026-05-29`

## Scope

Bounded review of active canonical repository artifacts after the architecture split:

```text
START_HERE.md stable door
→ docs/ROUTER.md live internal map
→ smallest relevant internal node
```

This review checks whether active documents still incorrectly describe `START_HERE.md` as the live route catalogue.

## Review Method

1. Verified the current stable door and live router directly.
2. Attempted GitHub code search for `START_HERE.md` and related phrases.
3. GitHub code search returned no results even for the exact filename, so it could not be treated as reliable repository-wide coverage.
4. Manually inspected the highest-risk canonical active artifacts listed in `PROJECT_INDEX.md`.
5. Distinguished active instructions from historical logs and prior-state records.

## Confirmed Current Architecture

### Stable door

`START_HERE.md`

Current behavior:

```text
enter system
→ open docs/ROUTER.md
→ follow smallest relevant route
```

### Live internal map

`docs/ROUTER.md`

Current behavior:

```text
stores navigation only
→ may evolve as internal system grows
→ routes to smallest relevant internal node
```

## Findings

### Finding 1 — README.md is stale

Status: `revise`

Current stale statements include:

```text
That entrypoint is navigation only. It routes into the relevant internal system node...
For a possible new initiative, it routes to: Start New Project.md
START_HERE.md — system front door and router only
```

Problem:

`START_HERE.md` no longer owns the growing route catalogue. It now points only to `docs/ROUTER.md`.

Required correction:

Describe:

```text
START_HERE.md — stable door
docs/ROUTER.md — live internal router
```

### Finding 2 — START_FAST.md is stale

Status: `revise`

Current stale statements include:

```text
not as a replacement for the canonical startup router
If you are starting a new project, the canonical entrypoint is still: Start New Project.md
```

Problem:

The canonical top-level entrypoint is `START_HERE.md`, not `Start New Project.md`.

`Start New Project.md` is an internal route selected through `docs/ROUTER.md` when the request concerns a possible new initiative.

Required correction:

Make `START_FAST.md` explicitly a non-canonical shortcut and preserve:

```text
START_HERE.md
→ docs/ROUTER.md
→ relevant route
```

### Finding 3 — docs/REPOSITORY_MEMORY_STANDARD.md is stale

Status: `revise`

Current stale statements include:

```text
START_HERE.md
Purpose:
- top-level router only
...
Then follow only the route relevant to the current work.
...
The front door must remain a router
```

Problem:

The document still assigns the live-router function to `START_HERE.md`.

Required correction:

Change central memory layers and required read order to:

```text
START_HERE.md — stable top-level door
docs/ROUTER.md — live internal router
```

Also insert `docs/ROUTER.md` into conflict-resolution order after `START_HERE.md` where routing order matters.

### Finding 4 — project-library/DECISION_REGISTRY.md is partially stale

Status: `revise`

Current stale state remains in Decision 002:

```text
Create and route through docs/CONTEXT_ASSEMBLY_STANDARD.md
implemented — committed and routed from START_HERE.md
```

Problem:

The current route is now:

```text
START_HERE.md
→ docs/ROUTER.md
→ docs/CONTEXT_ASSEMBLY_STANDARD.md
```

Required correction:

Update the current registry to reflect the committed architecture and reference Decision 006.

## Checked And Acceptable Active Artifacts

### START_HERE.md

Status: `accept`

Reason:

Correctly reduced to a stable door pointing to `docs/ROUTER.md`.

### docs/ROUTER.md

Status: `accept`

Reason:

Correctly stores live navigation only and explicitly forbids operational details.

### PROJECT_INDEX.md

Status: `accept`

Reason:

Correctly records:

```text
START_HERE.md
→ docs/ROUTER.md
→ smallest relevant internal node
```

### docs/CONTEXT_ASSEMBLY_STANDARD.md

Status: `accept`

Reason:

Version 2 correctly separates stable door, live router and routed standards.

### docs/integrations/chatgpt/CORE_SYSTEM_PROMPT.md

Status: `accept`

Reason:

Correctly instructs ChatGPT to fetch `START_HERE.md`, open the live internal router named inside it and follow the smallest relevant route.

### SYSTEM_CONTEXT_MANIFEST.md

Status: `accept`

Reason:

Current active profile includes:

```text
CORE_SYSTEM_PROMPT
→ START_HERE.md
→ docs/ROUTER.md
→ CONTEXT_ASSEMBLY_STANDARD
→ KNOWLEDGE_SYSTEM
```

### docs/AI_COORDINATION_HUB_STANDARD.md

Status: `accept with no immediate change`

Reason:

Statements that agents route through `START_HERE.md` remain true. The file does not need to duplicate the internal `docs/ROUTER.md` hop unless later review finds ambiguity in real use.

### Start New Project.md

Status: `accept`

Reason:

Correctly describes itself as a thin internal entrypoint for a possible new project, not as the root system entrypoint.

### docs/PROJECT_ENTRYPOINT_STANDARD.md

Status: `accept`

Reason:

Concerns project-specific entrypoints and does not conflict with the central door/router split.

## Historical Artifacts

Historical logs and prior-state records may contain old route language.

Do not rewrite them merely to make history look current. They should preserve executed historical state unless a separate annotation is materially useful.

Examples:

- `logs/2026-05-29-context-cache-implementation.md`
- earlier commits and superseded manifest profiles

## Review Outcome

`accept with required revisions`

The architecture split is correct and committed.

Four active artifacts remain stale and should be revised before the door/router architecture is treated as fully synchronized:

```text
README.md
START_FAST.md
docs/REPOSITORY_MEMORY_STANDARD.md
project-library/DECISION_REGISTRY.md
```

## Coverage Limitation

This was a bounded review of high-risk canonical active nodes.

GitHub code search did not return results even for an exact filename query, so a fully exhaustive repository-wide stale-reference proof is not available from the current search interface.

A later Codex or local repository grep pass should perform an exhaustive textual scan before final acceptance.

## Next Action

Revise the four active stale artifacts in one bounded synchronization pass, then run a local or Codex grep check for remaining stale references.