# Start New Project

## Purpose

This file is the thin entrypoint for a possible new project inside Project Execution OS.

Its only job is to identify the correct next path.

Do not place project-storage rules, workflow logic, tool instructions, architecture, or execution standards in this file. Those belong in the internal system nodes linked below.

## Route

First determine what the user is actually doing:

- exploring or discussing an idea only -> `docs/MODE_CLASSIFIER.md`
- preserving an idea or reference without starting a project -> `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md`
- starting a real project -> `docs/PROJECT_LIFECYCLE_MODEL.md`, then `docs/PROJECT_ENTRYPOINT_STANDARD.md`
- continuing an existing project -> its current project entrypoint; if missing, use `docs/PROJECT_ENTRYPOINT_STANDARD.md`
- handing an already-defined execution task to Codex -> `docs/CODEX_HANDOFF_STANDARD.md`

## Minimum Question

If the user says to create a project but has not stated the idea, ask only:

`Какую идею или проект разрабатываем?`

If the user is already discussing a clear idea, do not restart a questionnaire. Route the work into the lightest correct path.

## Final Rule

This is a front door, not the system itself.

Classify the intent and follow the next internal node.