# Blocks

## Domain Blocks

The existing `blocks/` directory contains reusable domain modules embedded inside `Project Execution OS`.

A domain block is not a separate operating system and is not automatically an executable code package.

A domain block is a focused reusable knowledge and decision layer that:

- has a clear purpose;
- defines when to use and when not to use it;
- preserves research, donors, ready solutions, patterns, standards, templates, and examples when useful;
- supports creation and review;
- depends on central OS rules instead of replacing them.

Use domain blocks when a field is mature enough to deserve a stable reusable home inside the central brain.

## Executable Capability Blocks

Reusable code that performs a bounded operation belongs to the capability-block architecture defined in:

`docs/COMPOSABLE_CAPABILITY_BLOCKS_STANDARD.md`

Examples:

```text
media.download
media.transcribe
media.clip
```

Executable readiness is tracked in:

`capability-library/REGISTRY.md`

## Separation Rule

```text
Domain block = knows how to decide.
Capability block = performs one reusable action.
Workflow = composes capability blocks.
Application = provides product-specific UI and business logic.
```

Do not mistake a specification or knowledge block for implemented reusable code.