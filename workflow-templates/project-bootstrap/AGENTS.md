Read `PROJECT.md` first.

This project is governed by `Project Execution OS`. Start from the central system entrypoint:
`https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/START_HERE.md`

Use only the minimum necessary route and project context.

Do not scan the whole repository unless the current task truly requires it.

Do not invent the project purpose, architecture, stack, scope, or prior decisions when they are not explicitly confirmed.

Treat model memory, hidden context, and chat history as non-authoritative unless the project records them durably.

Follow the canonical reuse-first standard:
`https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/docs/EXISTING_SOLUTION_FIRST_STANDARD.md`

- check for an adequate existing solution before designing, writing, or fixing your own;
- adapt before rebuilding;
- do not invent a new solution without that check.

For inter-agent transfer, use the official communication block:
`https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/blocks/communication-channel/BLOCK.md`

If `PROJECT.md` is absent but legacy `PROJECT_ENTRYPOINT.md` exists, read the legacy file temporarily and migrate it to `PROJECT.md` at the nearest safe opportunity without keeping both files active.

Preserve stable starts of accumulating files where practical. Add normal chronological updates lower in the file instead of rearranging unchanged blocks without a real reason.
