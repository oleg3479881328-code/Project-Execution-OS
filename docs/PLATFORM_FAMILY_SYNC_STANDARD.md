# Platform Family Synchronization Standard

## Purpose

This standard defines how near-identical client projects such as Olga Polo and Tusia/Tasha stay synchronized without forcing every chat to rediscover the same platform decisions.

The projects are separate client instances of one evolving platform family. They may move at different speeds, but shared capabilities must converge on the best reviewed solution.

## Core Model

```text
Client Project A ─┐
Client Project B ─┼─→ Shared Platform Capability Layer
Client Project C ─┘
```

Each client keeps its own:
- brand shell;
- content and entities;
- domain and routing particulars;
- secrets/environment values;
- production lifecycle.

The family shares reviewed platform capabilities such as:
- CMS contracts;
- entity identity rules;
- publish lifecycle;
- SEO/indexing state rules;
- responsive parity contracts;
- validation and review automation;
- project bootstrap patterns.

## No Permanent Master Client

Do not declare Olga, Tusia, or any future client the permanent master implementation.

Instead, determine the current best implementation per capability.

Example:

```text
CMS source-of-truth       → Olga leads today
Design capture evidence   → Tusia may lead tomorrow
SEO contract              → another project may lead later
```

The shared platform is the convergence target.

## Capability Synchronization Loop

For every substantive platform change:

1. Identify the affected capability.
2. Read `docs/SHARED_WEB_PLATFORM_REGISTRY.md`.
3. Read `docs/SHARED_PROJECT_CAPABILITY_MATRIX.md`.
4. Determine whether another sibling project already has a stronger reviewed implementation.
5. Reuse/adapt the stronger implementation instead of re-solving the problem.
6. If the current project discovers a stronger generic solution, run independent review and promote it under `docs/SHARED_SOLUTION_PROMOTION_STANDARD.md`.
7. Record the new family target state.
8. Put lagging sibling projects into an explicit adoption queue.
9. Adopt when each project reaches a safe integration point; do not force simultaneous production updates.

## Family Target State

Every shared capability has one current target state even if not every client has adopted it yet.

Use this shape:

```text
Capability
Current target: reviewed solution/version
Evidence origin: project/commit/incident
Adopted by: projects
Pending adoption: projects
Exceptions: explicit project-specific deviations
```

This avoids chat drift. A lagging project should ask "what is the current family target?" rather than "how should we solve this from scratch?"

## Adoption Queue

When a shared target improves, update sibling status explicitly:

- `ADOPTED` — current project satisfies the family target.
- `PENDING` — project should adopt when work reaches the capability.
- `BLOCKED` — adoption requires prerequisite or evidence.
- `EXCEPTION` — intentional project-specific deviation is documented.

Do not use `UNKNOWN` as a reason to invent a new solution if a family target already exists.

## Knowledge-First Propagation

When code-level synchronization is temporarily blocked because a sibling codebase is not durably inspectable, propagate the reviewed invariant immediately at the knowledge/acceptance level.

Example:

```text
Olga finds and fixes CMS/fallback mobile divergence
→ independent review passes
→ family rule becomes PROVEN
→ Tusia must inherit that rule in new work
→ code extraction may happen later
```

This prevents a known failure from being repeated just because shared package extraction is not ready yet.

## Code Synchronization Rule

Do not copy whole client repositories or large project-specific modules into shared core.

Extract the smallest client-neutral contract or module after:
- at least one real implementation exists;
- near-identical sibling evidence supports the abstraction;
- project-specific assumptions are removed;
- independent review passes;
- a canary adoption path exists.

When projects are intentionally near-identical, the owner may approve earlier code extraction before both durable implementations are available, but the abstraction must still undergo independent review and canary adoption.

## New Chat Requirement

A new chat working on a platform-family project must use this order before solving a platform-level problem:

1. current project entrypoint/state;
2. shared platform registry;
3. capability matrix;
4. family synchronization standard;
5. relevant global Project Execution OS standards;
6. only then project-local invention if no reviewed family solution exists.

The executor must not ask the owner to manually relay already-durable shared decisions between sibling chats.

## Project-Specific Work Boundary

Do not load unrelated client content when the task is purely brand/content-specific.

Shared lookup is mandatory only when the task affects a platform capability or could repeat a known cross-project problem.

## Review Questions

Independent review of a synchronization change must ask:
- Is the family target actually generic?
- Is a stronger sibling implementation being ignored?
- Is a client-specific exception being promoted accidentally?
- Is a lagging project about to re-solve a problem already marked PROVEN?
- Is adoption safe and independently reversible per client?
- Is the capability matrix updated after the decision?

## Related Nodes

- `docs/SHARED_SOLUTION_PROMOTION_STANDARD.md`
- `docs/SHARED_WEB_PLATFORM_REGISTRY.md`
- `docs/SHARED_PROJECT_CAPABILITY_MATRIX.md`
- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
- `docs/REVIEW_STANDARD.md`
