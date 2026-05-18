# Skill Lifecycle Standard v1

## Purpose

This standard defines lifecycle states for central reusable skills inside `Project-Execution-OS`.

## Lifecycle States

### draft

Raw or newly created skill.

### candidate

Structured skill ready for review or recently migrated from an incubator repository.

### reviewed

Reviewed artifact with explicit review output recorded.

### active

Approved for operational reuse in the central system.

### deprecated

Still available but should no longer be preferred.

### retired

Preserved for history but not for normal use.

## Transition Rules

Allowed transitions:

```text
draft -> candidate
candidate -> reviewed
reviewed -> active
active -> deprecated
deprecated -> retired
```

Alternative downgrade transitions may be used when review fails:

```text
candidate -> draft
reviewed -> candidate
active -> candidate
```

Use downgrades only with a documented reason.

## Review Rule

No central skill becomes `active` without review.

## Migration Rule

Skills imported from `3TestAgents` or another incubator repository should start as:

`candidate`

unless a new central review promotes them further.

## State Separation

Always distinguish:

- `generated`
- `committed`
- `reviewed`
- `active`

Do not treat a committed migration as an active approval.
