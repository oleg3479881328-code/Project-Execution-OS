# Incremental Re-entry Standard

## Purpose

This standard defines incremental re-entry — инкрементальный повторный вход — for a GitHub-backed project — проект с GitHub-слоем.

Its purpose is to help an agent — агент — return quickly without rereading the whole repository.

Use it when one agent returns after work by other agents and needs only the delta — изменения.

## Agent Terminology

Use `agent` — агент — as the umbrella term for secondary acting entities.

Examples:

- `AI agent` — ИИ-агент
- `human agent` — агент-человек
- `service agent` — сервисный агент
- `automation agent` — агент-автоматизация

## Core Rule

```text
PROJECT.md
→ agent checkpoint
→ compare last_seen_commit..HEAD
→ PROJECT_CHANGE_INDEX
→ only changed and directly related files
→ continue task
→ update checkpoint
```

Do not reread the whole project by default.

Read the delta first.

## Required Concepts

- `last_seen_commit` — последний коммит, который уже видел агент
- `current_head` — текущий `HEAD`
- `git diff` — сравнение изменений Git
- `changed_files` — изменённые файлы
- `PROJECT_CHANGE_INDEX.md` — короткий индекс смысловых изменений
- `CONTEXT_PACK.md` — краткий пакет быстрого повторного входа
- `agent-checkpoints/<agent-id>.md` — checkpoint конкретного агента

## State Rule

`PROJECT_CHANGE_INDEX.md` helps explain the meaning of changes — смысл изменений — but it does not replace Git commits — коммиты Git — or canonical evidence — канонические подтверждения.

`CONTEXT_PACK.md` helps speed up re-entry — ускоряет повторный вход — but it does not replace `PROJECT.md`, `PROJECT_STATE.md`, code, or commits.

An `agent checkpoint` — контрольная отметка агента — shows where one specific agent stopped. It is not the project source of truth.

Git remains the technical source of truth for file changes.

## Re-entry Workflow

```text
1. Read PROJECT.md.
2. Read agent checkpoint if present.
3. Get last_seen_commit.
4. Get current HEAD.
5. Compare last_seen_commit..HEAD.
6. Read PROJECT_CHANGE_INDEX.md entries after last_seen_commit.
7. Read only changed files and directly related files needed for the active task.
8. Continue work.
9. Update checkpoint after meaningful completed work.
```

## First Entry Rule

If no checkpoint exists:

- read `PROJECT.md`;
- if `PROJECT.md` is missing but legacy `PROJECT_ENTRYPOINT.md` exists, read the legacy file and migrate it at the nearest safe opportunity;
- read only the minimum current state needed to start safely;
- record the current `HEAD` as the first checkpoint;
- do not read the whole repository without a real reason.

## When Full Read Is Allowed

A full project read is allowed only when at least one of these is true:

- the project is small;
- no checkpoint exists and documentation is not sufficient;
- the task is an architectural review — архитектурный review / обзор архитектуры — that needs full coverage;
- the delta shows a large structural migration — крупная структурная миграция;
- there are signs of stale or damaged context — устаревший или повреждённый контекст.

## Recommended Artifact Shape

For a GitHub-backed project, the recommended minimal placement is:

```text
PROJECT.md
PROJECT_STATE.md
CONTEXT_PACK.md
PROJECT_CHANGE_INDEX.md
agent-checkpoints/
  <agent-id>.md
```

Use only the artifacts that create real value for re-entry.

Do not create ceremony for its own sake.

## Anti-Bloat Rule

Do not create ritual updates after every tiny edit.

Update `PROJECT_CHANGE_INDEX.md` only after a meaningful change — значимое изменение.

Update the agent checkpoint only after meaningful completed work.

## Related Standards

- `docs/ROUTER.md`
- `docs/REPOSITORY_MEMORY_STANDARD.md`
- `docs/CONTEXT_ASSEMBLY_STANDARD.md`
- `docs/PROJECT_ENTRYPOINT_STANDARD.md`
- `docs/CODEX_HANDOFF_STANDARD.md`
- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`

## Final Rule

Incremental re-entry is a reuse-first operating rule.

Use Git for technical truth, use a short change index for meaning, use a context pack for speed, and read only the files the current task actually needs.
