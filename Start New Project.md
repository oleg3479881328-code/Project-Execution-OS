# Start New Project

## Purpose

This file is the thin entrypoint for a possible new project inside Project Execution OS.

Its only job is to identify the correct next path.

Do not place project-storage rules, workflow logic, tool instructions, architecture, or execution standards in this file. Those belong in the internal system nodes linked below.

## Route

First determine what the user is actually doing:

- exploring or discussing an idea only -> `docs/MODE_CLASSIFIER.md`
- preserving an idea or reference without starting a project -> `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md`
- explicitly creating a new project or new project workspace -> `docs/PROJECT_BOOTSTRAP_STANDARD.md`, then `docs/PROJECT_LIFECYCLE_MODEL.md` and `docs/PROJECT_ENTRYPOINT_STANDARD.md`
- continuing an existing project -> its current project entrypoint; if missing, use `docs/PROJECT_ENTRYPOINT_STANDARD.md`
- handing an already-defined execution task to Codex -> `docs/CODEX_HANDOFF_STANDARD.md`

## Explicit Creation Rule

If the user explicitly creates a new project through chat, a desktop interface, an IDE, an agent workspace, a folder command or an equivalent action, do not postpone initialization until the project idea is described.

Follow `docs/PROJECT_BOOTSTRAP_STANDARD.md` first. The project may be initialized truthfully as `initialized — purpose not yet defined`.

Only after the minimal project bootstrap exists should the project purpose be obtained or refined.

That bootstrap must already inherit `docs/EXISTING_SOLUTION_FIRST_STANDARD.md` so the project starts with reuse-first constraints instead of invention-first drift.

## Minimum Question After Bootstrap

If the project has been initialized but its idea has not been stated, ask only:

`Какую идею или проект разрабатываем?`

If the user is already discussing a clear idea, do not restart a questionnaire. Route the work into the lightest correct path after bootstrap.

## Final Rule

This is a front door, not the system itself.

Classify the intent and follow the next internal node.
