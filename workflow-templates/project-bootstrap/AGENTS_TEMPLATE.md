# AGENTS.md Template

## Purpose

This file is a short local adapter for a specific project.

It should help a fresh agent enter the correct path quickly without duplicating the whole central system.

## Required Entry Order

Before project work:

1. Read the central top-level entrypoint:
   `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/START_HERE.md`
2. Open the live router selected by that entrypoint:
   `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/docs/ROUTER.md`
3. Read the local `PROJECT.md` for this project.
4. Check whether a useful project index already exists.
5. Read only the minimum additional files needed for the active task.

If `PROJECT.md` is absent but legacy `PROJECT_ENTRYPOINT.md` exists, read the legacy file temporarily and migrate it to `PROJECT.md` at the nearest safe opportunity without keeping both files active.

## Project Index

Before mass scanning the project, check whether a useful existing index is already present.

If the project has grown enough that a useful index is missing, create a minimal index.

After a meaningful structural change, update the index.

The agent that changes project structure is responsible for keeping the index current.

Do not create an index ritualistically for an empty project.

## Guardrails

- Do not scan the whole project unless the current task truly requires it.
- Treat model memory, hidden context, and chat history as non-authoritative unless the project records them durably.
- Do not invent project purpose, architecture, stack, scope, or prior decisions when they are not explicitly confirmed.
- Check for an adequate existing solution before designing, writing, or fixing your own.
- Preserve stable starts of accumulating files where practical. Add normal chronological updates lower in the file instead of rearranging unchanged blocks without a real reason.

## Central Standards To Use Directly

- Existing Solution First:
  `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
- Transfer readiness and continuity:
  `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md`
- Official communication channel:
  `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/blocks/communication-channel/BLOCK.md`

## Notes

For a standalone external project folder, `AGENTS.md` is required.

For an internal subproject inside an existing repository,
`AGENTS.md` is optional when `PROJECT.md` alone is sufficient
and no local subproject instructions are needed.
