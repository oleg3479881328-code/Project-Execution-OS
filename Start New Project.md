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
- explicitly starting a real project -> `docs/PROJECT_BOOTSTRAP_STANDARD.md`, then `docs/PROJECT_ENTRYPOINT_STANDARD.md` and `docs/PROJECT_MEMORY_STANDARD.md`
- starting or attaching a real project inside ChatGPT Projects -> establish the project's durable canonical entrypoint normally, but use the generic ChatGPT attachment defined by `docs/CHATGPT_PROJECT_START_HERE_TEMPLATE.md`; that attachment points to the global `START_HERE.md`, and project identity is resolved through recursive routing
- continuing an existing project -> enter through global `START_HERE.md`, follow the router tree to the project's current entrypoint, then restore context through `docs/PROJECT_MEMORY_STANDARD.md`; if the project entrypoint is missing, use `docs/PROJECT_ENTRYPOINT_STANDARD.md`
- delegating a substantial independent task to another AI or parallel ChatGPT worker while a shared durable workspace is available -> `docs/EXTERNAL_AI_NOTION_TASK_RESULT_STANDARD.md`, `docs/WORKER_IMMEDIATE_EXECUTION_STANDARD.md`, and `docs/WORKER_CHAT_NAMING_STANDARD.md`
- handing an already-defined execution task to Codex -> `docs/CODEX_HANDOFF_STANDARD.md`

## Bootstrap Boundary

Creating or opening a folder, workspace, ChatGPT Project, or Codex Desktop project does not automatically create project files under Project Execution OS.

When the owner intentionally creates a standalone real project folder, initialize it immediately with:

```text
git init
AGENTS.md
PROJECT.md
```

When the owner intentionally creates an internal subproject inside an existing Git repository, do not run nested `git init`; create `PROJECT.md` and add `AGENTS.md` only if local subproject instructions are useful.

When the owner intentionally uses ChatGPT Projects as an interface to externally stored project memory, attach the generic `START_HERE.md` pointer to the global Project Execution OS entrypoint. Do not put evolving project state into that attachment and do not require repeated uploads after ordinary project changes.

Project-specific canonical entrypoints still exist in durable project storage. They are reached through the router tree rather than being hard-coded into each ChatGPT Project attachment.

Do not create these artifacts solely because a new folder exists, a workspace is opened, or an idea is being discussed.

Do not automatically create any additional project artifacts beyond that minimum bootstrap set.

The universal memory architecture begins with the entrypoint and expands only after meaningful work exists. Follow `docs/PROJECT_MEMORY_STANDARD.md` and do not create empty memory structure for hypothetical future needs.

## Minimum Question

If the user says they are starting a new project but has not stated the idea, ask only:

`Какую идею или проект разрабатываем?`

If the user is already discussing a clear idea, do not restart a questionnaire. Route the work into the lightest correct path.

## Final Rule

The global `START_HERE.md` is the universal front door.

This file handles the new-project branch after routing has selected it.

Classify the intent and follow the next internal node.