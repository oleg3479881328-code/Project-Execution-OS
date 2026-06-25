# Command 0.2 / 02 — Executor Reply Check Standard

## Purpose

This standard defines the owner shorthand command `0.2` / `02`.

The command means: check the executor's answer and continue from the actual latest execution state.

## Command Aliases

The following forms are equivalent:

- `0.2`
- `02`
- `проверить ответ исполнителя`
- `проверь ответ исполнителя`
- `check executor reply`
- `check executor answer`

Do not reinterpret `0.2` as a numbered option, a decimal, a stage number, or a request for clarification.

## Required Behavior

When the owner sends `0.2` or `02` in a project/executor context:

1. Identify the active project and active executor channel from the current conversation or durable project state.
2. Read the project entrypoint/state if needed.
3. Open the active GitHub issue, PR, review thread, Notion comment, or registered communication channel.
4. Inspect the latest relevant executor response.
5. If the executor reports commits, PRs, artifacts, logs, or validation output, inspect that evidence.
6. Compare the result against the handoff packet / acceptance criteria.
7. Respond to the owner with a concise review: accepted, needs fixes, blocked, or no executor reply yet.

## No Clarification Rule

Do not ask the owner what `0.2` means.

If no active executor channel can be determined after checking current context and durable pointers, say that the active channel could not be determined and state exactly what was checked.

## Routing

Use the communication-channel route for readback mechanics:

`blocks/communication-channel/BLOCK.md`

Then use the current project's entrypoint and active transport as evidence.

## Scope Boundary

`0.2` / `02` is a read/check command. It does not authorize destructive actions, scope expansion, repository visibility changes, external publication, production deployment, irreversible data migration, or new paid services.
