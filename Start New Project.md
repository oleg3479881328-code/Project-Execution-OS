# Start New Project

## Purpose

This file is the thin entrypoint for a possible new project inside Project Execution OS.

Its only job is to identify the correct next path.

Do not place project-storage rules, workflow logic, tool instructions, architecture, or execution standards in this file. Those belong in the internal system nodes linked below.

## Route

First determine what the user is actually doing:

- exploring or discussing an idea only -> `docs/MODE_CLASSIFIER.md`
- preserving an idea or reference without starting a project -> `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md`
- explicitly starting project work -> `docs/PROJECT_LIFECYCLE_MODEL.md` and `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
- explicitly requesting a minimal project folder entrypoint -> `docs/PROJECT_BOOTSTRAP_STANDARD.md`, then `docs/PROJECT_ENTRYPOINT_STANDARD.md`
- continuing an existing project -> its current project entrypoint; if missing, use `docs/PROJECT_ENTRYPOINT_STANDARD.md`
- handing an already-defined execution task to Codex -> `docs/CODEX_HANDOFF_STANDARD.md`

## No Automatic Folder Mutation Rule

Creating or opening a folder, workspace, or Codex Desktop project does not automatically create project files under Project Execution OS.

Do not automatically create `AGENTS.md`, `PROJECT_ENTRYPOINT.md`, or other project artifacts solely because a new folder exists.

Minimal project initialization is performed only when the user explicitly requests it.

## Minimum Question

If the user says they are starting a new project but has not stated the idea, ask only:

`Какую идею или проект разрабатываем?`

If the user is already discussing a clear idea, do not restart a questionnaire. Route the work into the lightest correct path.

## Final Rule

This is a front door, not the system itself.

Classify the intent and follow the next internal node.
