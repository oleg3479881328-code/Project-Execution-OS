# Shared Solution Promotion Standard

## Purpose

This standard defines how a solution discovered inside one project becomes reusable across multiple projects without forcing future chats to rediscover it.

The goal is not to merge all client projects into one codebase. The goal is to create a controlled upward path from project-local learning into durable shared knowledge, shared contracts, shared code, shared review automation, and eventually project templates.

## Core Invariant

Use this promotion path:

```text
PROJECT LOCAL
→ CANDIDATE FOR REUSE
→ SECOND REAL USE-CASE OR CLEAR CROSS-PROJECT EVIDENCE
→ INDEPENDENT REVIEW
→ PROVEN
→ SHARED KNOWLEDGE / SHARED CODE / SHARED AUTOMATION / TEMPLATE
```

Do not promote a client-specific workaround into a shared dependency just because it worked once.

## Why This Exists

Multiple client projects may be nearly identical and still evolve at different speeds. One project may discover a better CMS contract, mobile rule, SEO resolver, publishing workflow, review check, or failure guard before another project reaches the same point.

Without a promotion layer, each new chat or project must rediscover the same solution. That is a system failure.

Shared promotion makes project progress cumulative:

```text
Project A learns
→ solution is reviewed and promoted
→ Project B, C, D ... can reuse it
→ later project discoveries can promote upward again
```

## Four Shared Targets

Classify every reusable candidate into exactly one primary target before implementation.

### 1. Shared Knowledge

Use for architecture rules, failure modes, invariants, acceptance contracts, and operational lessons.

Examples:
- published CMS data is authoritative for client-editable fields;
- CMS-published and fallback render paths must satisfy the same responsive contract;
- invalid published content must fail loudly instead of silently falling back to stale data.

### 2. Shared Code

Use only for implementation that is truly client-neutral and has stable interfaces.

Examples:
- generic entity identity types;
- generic published-document resolver contract;
- generic publication-state helpers;
- reusable validation utilities.

Do not move brand assets, client copy, client routes, client domains, client secrets, or project-specific environment names into shared code.

### 3. Shared Automation

Use for reusable CI, review, migration, or conformance checks.

Examples:
- typecheck/build;
- schema validation;
- entity-registry integrity;
- mobile overflow test;
- published-path + fallback-path smoke;
- canonical/robots/OG/schema contract checks.

Brand-specific visual snapshots are not automatically shared automation.

### 4. Project Template

Use only after shared contracts are mature enough that a new project can inherit them safely.

The template should provide the minimum reusable scaffold and placeholders, not a copied client site.

## Promotion Gate

A candidate is PROVEN only when all applicable conditions are met:

1. The originating project has real implementation evidence.
2. The reusable boundary is explicitly described.
3. Client-specific assumptions are separated from generic behavior.
4. A second real project or equivalent cross-project evidence supports the abstraction, unless the owner explicitly approves promotion earlier.
5. An independent review checks the candidate without relying on the implementer's explanation.
6. Regression/acceptance checks exist for the shared invariant.
7. The shared destination is identified before code is moved.

## Nearly-Identical Project Rule

When two or more projects are intentionally based on the same architecture, do not force them to rediscover identical decisions independently.

Instead:

- use the furthest-ahead project as evidence, not as unquestioned authority;
- promote verified generic improvements upward as soon as their reusable boundary is clear;
- let lagging projects consume the promoted solution rather than re-solving it;
- keep client-specific brand/data layers separate;
- avoid automatic production updates across all clients; shared code and shared standards must be versioned or otherwise explicitly adopted.

This allows projects to move at different speeds while still converging on one shared platform.

## Independent Review Questions

The reviewer must ask:

- Is this actually reusable, or just similar today?
- What exact assumptions belong to the originating client?
- Does the abstraction preserve each project's independent production lifecycle?
- Can a future project consume the solution without importing client-specific data or secrets?
- Is the shared API smaller than the source implementation?
- Are failure modes and regression checks documented?
- Is there a rollback/adoption path if a shared version causes a regression?

## Search Integration

This standard extends `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`.

Before inventing a solution inside a project, search in this order:

1. current project;
2. shared solution registry / shared standards in Project Execution OS;
3. sibling project evidence when the projects share an architecture;
4. official/external established solutions;
5. only then custom invention.

## No-Monorepo Requirement

Shared promotion does not require all client projects to live in one monorepo.

Client projects should remain independently deployable unless there is a separate explicit architecture decision to combine them.

## Adoption Rule

A shared solution becoming PROVEN does not automatically rewrite every production project.

Use explicit adoption:

```text
Shared solution version/state
→ canary project
→ review
→ next project(s)
```

For knowledge-only standards, new work should follow the current standard immediately unless a project-specific exception is recorded.

## Related Nodes

- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
- `docs/REVIEW_STANDARD.md`
- `docs/PROJECT_LIFECYCLE_MODEL.md`
- `docs/PROJECT_MEMORY_STANDARD.md`
- `docs/SHARED_WEB_PLATFORM_REGISTRY.md`
