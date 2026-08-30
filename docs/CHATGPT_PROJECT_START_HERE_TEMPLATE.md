# ChatGPT Project START_HERE Template

## Purpose

This file defines the optional stable bootstrap attachment for ChatGPT Projects when durable project knowledge lives outside the ChatGPT interface.

ChatGPT Project is a working window. It is not canonical project memory and does not need its own project-specific navigation architecture.

## Core Rule

There is one canonical global AI entrypoint:

`Project-Execution-OS/START_HERE.md`

If the active ChatGPT user/system instructions already guarantee that project work enters through that global `START_HERE.md`, no per-project attachment is required at all.

If an attachment is useful or an interface requires one, use the same generic file in every project:

```text
START_HERE.md
```

It points only to the global Project Execution OS entrypoint. It must not hard-code a specific project's state or create a second project-specific entry hierarchy.

## Default Russian Template

```md
# START_HERE

Это необязательный интерфейсный указатель на единственную глобальную входную точку Project Execution OS.
Перед проектной работой сначала открой канонический START_HERE по ссылке ниже, затем следуй по текущему Router и его дочерним роутерам/реестрам до нужного проекта и минимально необходимого контекста.
Не считай этот файл, историю чата или память модели актуальным состоянием проекта.

Канонический START_HERE:
https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/START_HERE.md
```

## Recursive Routing Rule

After opening the global `START_HERE.md`, routing may recurse through any number of navigation layers:

```text
START_HERE
→ global ROUTER
→ zero or more routers / registries / indexes
→ canonical project entrypoint
→ zero or more project-local routers / indexes
→ minimum task-specific evidence
```

Routing depth is determined by the information architecture, not by a fixed system limit.

## Legacy ChatGPT Project Compatibility

Older ChatGPT Projects may already contain project-specific files such as `<Project_Name>_START_HERE.md` or another pointer that routes directly to a project-specific Notion/GitHub/Drive entrypoint.

Do not require the owner to manually replace those existing attachments merely to adopt the global-entry architecture.

When global user/system instructions require entry through Project Execution OS `START_HERE.md`, that global entry has precedence. A legacy project-specific attachment becomes a non-authoritative compatibility hint that may be ignored until the router tree has selected the project.

Legacy attachments must not override:

1. global `START_HERE.md`;
2. the live router path;
3. the selected project's canonical durable entrypoint;
4. current durable evidence.

Remove or replace legacy attachments only during convenient maintenance or when they actively cause ambiguity. Their physical presence alone is not a migration blocker.

## Usage Rules

- Prefer no ChatGPT Project attachment when stable user/system instructions already guarantee the global `START_HERE.md` entry.
- If an attachment is needed, use one generic `START_HERE.md` pointer to the global entrypoint.
- Do not create new project-specific ChatGPT pointer contracts.
- Resolve project identity through the live router tree and durable project sources.
- Do not duplicate live project state, task lists, architecture, research, decisions, or history inside interface attachments.
- Do not regenerate attachments because projects evolve behind the router tree.

## Final Rule

One global `START_HERE.md` = one stable AI door.

Stable client instruction = preferred bootstrap.

Generic ChatGPT attachment = optional compatibility bootstrap.

Legacy project-specific attachment = non-authoritative compatibility artifact.

Recursive routers and durable project entrypoints = the live system.