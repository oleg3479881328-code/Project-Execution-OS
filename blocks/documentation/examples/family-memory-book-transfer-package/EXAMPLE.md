# Example

## Source

This example comes from the `Documentation-OS` test run:

`workflow-runs/0003-test-family-memory-book/`

## Why It Matters

It is a strong example because the target repository was not a toy repo:
- public static site;
- sensitive family content;
- generated and extracted assets;
- maintainer workflow constraints;
- explicit transfer-package-first discipline.

## Reusable Lesson

For sensitive repositories, documentation generation is not enough.

A concrete transfer package and explicit forbidden-change rules should exist before any target-repository write.
