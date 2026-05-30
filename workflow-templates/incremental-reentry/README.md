# Incremental Re-entry Templates

## Purpose

This folder contains a lightweight MVP — минимальный жизнеспособный слой — for incremental re-entry — инкрементальный повторный вход — in a GitHub-backed project — проект с GitHub-слоем.

Git remains the technical source of truth.

These templates only help agents return faster through delta-based reading — чтение через дельту изменений.

## When To Use

Use these templates when:

- agents re-enter the same project repeatedly;
- handoff between agents is common;
- the project is large enough that rereading everything is wasteful;
- Git history exists, but a short semantic change index would reduce re-entry cost.

Do not use them just to create structure.

## Recommended Placement

Recommended files in a GitHub-backed project:

```text
PROJECT_ENTRYPOINT.md
PROJECT_STATE.md
CONTEXT_PACK.md
PROJECT_CHANGE_INDEX.md
agent-checkpoints/
  <agent-id>.md
```

## Template Roles

- `PROJECT_CHANGE_INDEX_TEMPLATE.md` -> short semantic index of meaningful changes
- `AGENT_CHECKPOINT_TEMPLATE.md` -> short per-agent checkpoint
- `CONTEXT_PACK_TEMPLATE.md` -> optional fast re-entry brief

## MVP Boundary

This is an MVP only.

It does not add a backend — серверная часть, runtime engine — исполняемый движок, vector database — векторная база данных, semantic index — семантический индекс, or heavy automation — тяжёлая автоматизация.

## Final Rule

Use the smallest set of files that makes re-entry materially easier.
