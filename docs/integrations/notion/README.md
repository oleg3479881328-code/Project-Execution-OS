# Notion Adapter Standard

## Purpose

This document defines how `Notion` should work with `Project Execution OS` as a normal external adapter rather than an accidental second brain.

## Core Position

`Project Execution OS` remains repository-first.

The repository is still the source of truth.

`Notion` is allowed as a useful external working surface for:

- shared project context;
- readable briefs;
- research synthesis;
- spec drafting;
- meeting preparation;
- decision capture;
- lightweight status views.

## What Notion Is Good For

Use `Notion` when you need:

- a shared human-readable workspace;
- a cleaner view than raw repository files;
- collaborative notes or decision pages;
- research rollups from multiple artifacts;
- spec pages that later become implementation work;
- meeting prep, agendas, or summaries;
- a temporary working surface before durable repository write-back.

If a `Notion` project needs a clean first-read surface for humans or AI, use the shared contract from:

- `docs/PROJECT_ENTRYPOINT_STANDARD.md`

and the `Notion`-specific template:

- `workflow-templates/project-entrypoint/NOTION_PROJECT_ENTRYPOINT_TEMPLATE.md`

## What Notion Must Not Replace

Do not treat `Notion` as:

- the committed source of truth;
- a substitute for repository memory;
- the only place where important project state lives;
- proof that execution happened;
- a hidden state layer unknown to the repository.

If it matters durably, it must still be written back into repository artifacts.

## Canonical Rule

Use this model:

`repository = source of truth`

`Notion = adapter / workspace / readable layer`

Not:

`Notion = brain`

## Allowed Operating Modes

### 1. Capture Mode

Use `Notion` to capture:

- meeting notes;
- research notes;
- decision drafts;
- working summaries.

Then promote only the durable parts back into the repository.

### 2. Synthesis Mode

Use `Notion` to combine:

- repository artifacts;
- research findings;
- meeting context;
- project summaries.

Then write the stable output back to repository files when it becomes project memory.

### 3. Spec Workspace Mode

Use `Notion` to draft:

- feature specs;
- implementation outlines;
- task plans.

Before execution, ensure the relevant committed version or derived packet exists in the repository.

### 4. Shared Visibility Mode

Use `Notion` as a readable shared surface for humans who do not want to navigate raw repository files.

This is a presentation and coordination function, not a truth-layer override.

## When To Use Notion Vs GitHub

Prefer `Notion` when the work is lightweight, personal, or coordination-heavy, for example:

- travel planning;
- recipe collections;
- shopping comparisons;
- life planning notes;
- shared checklists;
- idea discussion and rough structuring;
- human-readable project coordination that does not need repository-grade execution history.

Prefer `GitHub` when the work becomes repository-driven, for example:

- code or executable artifacts;
- implementation packets for `Codex`;
- reviewable diffs and validation history;
- committed technical documentation;
- durable project memory tied to files and versions;
- work that needs branch, PR, issue, or review-thread discipline.

Use this mental model:

`Notion = light workspace`

`GitHub = durable execution and repository truth`

If something starts in `Notion` and later becomes a real project, move the durable project state into the repository rather than forcing the whole project to stay only in `Notion`.

## Sync Rule

When `Notion` is used:

1. read the repository first;
2. use `Notion` as workspace, adapter, or presentation layer;
3. write durable outcomes back into repository artifacts;
4. never leave critical state trapped only in `Notion`.

## Tooling Map

Current useful external skills and connectors around `Notion` include:

- `notion-knowledge-capture`
- `notion-research-documentation`
- `notion-spec-to-implementation`
- `notion-meeting-intelligence`
- `notion-memory-ritual`

Inside `Project Execution OS`, these are treated as adapters or environment-specific capabilities, not as the universal core workflow.

## Default Recommendation

If a user explicitly wants `Notion`, use it.

If a task benefits from a shared readable workspace, `Notion` is a good adapter.

If the task needs durable truth, final state still belongs in the repository.

## Final Rule

`Notion` is welcome.

But it must stay an adapter, not a silent replacement for repository memory.
