# Documentation Block

## Purpose

This block stores the reusable documentation-specific layer extracted from `Documentation-OS`.

Its goal is to help `Project-Execution-OS` produce, review, and transfer AI-ready repository documentation packages without recreating the same patterns from scratch.

## Status

`reviewed_candidate`

## When To Use

Use this block when the task is to:
- analyze a repository for documentation quality;
- generate an AI-ready documentation package;
- normalize repository documentation;
- prepare a transfer package before changing a target repository;
- review repository-facing maintainer documentation;
- document handoff and maintenance constraints for AI executors.

## When Not To Use

Do not use this block for:
- general project startup routing;
- implementation planning unrelated to documentation;
- backend, frontend, runtime, or database execution;
- broad architecture work with no documentation deliverable;
- tasks where a plain answer is enough.

## Inputs

Typical inputs:
- a target repository;
- existing repository docs and structure;
- current workflow state;
- review findings;
- transfer approval when documentation must be moved into a target repo.

## Outputs

Typical outputs:
- `README.md`
- `PROJECT.md`
- `PROJECT_STATE.md`
- `PROJECT_RULES.md`
- `docs/CODEX_HANDOFF.md`
- compact repository documentation workflow runs
- transfer package artifacts
- review and checklist artifacts

## Depends On

This block depends on central OS rules, especially:
- `docs/MODE_CLASSIFIER.md`
- `docs/WORKFLOW_CONTRACT.md`
- `docs/WORKFLOW_DECISION_TABLE.md`
- `docs/REVIEW_STANDARD.md`
- `docs/CODEX_HANDOFF_STANDARD.md`
- `docs/REPOSITORY_MEMORY_STANDARD.md`

## Structure

```text
blocks/documentation/
  BLOCK.md
  PROJECT_INDEX.md
  MIGRATION_MAP.md
  standards/
  templates/
  examples/
  skills/
```
