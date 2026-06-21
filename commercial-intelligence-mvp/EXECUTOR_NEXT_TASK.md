# Executor Next Task

Prepare an owner-runnable launch path for the Commercial Intelligence MVP.

Owner feedback: do not hand the owner a long manual terminal sequence. The executor should make the MVP easy to start and verify.

## Required outcome

Create a simple local demo runner for Windows that starts the MVP in seed-first mode and produces a sample report without external API keys.

## Required changes

1. Add a demo runner in `commercial-intelligence-mvp/`.
2. The runner should prepare the local environment, run a seed-first demo audit, write outputs into a predictable report folder, and print the final report path.
3. Keep `--seed` as the primary interface.
4. Keep `--url` only as a backward-compatible alias.
5. Update owner-facing documentation with a short section named `One-command local demo`.
6. Fix stale README validation text that still presents `--url` as the main validation command.
7. Validate the demo runner and the existing tests.

## Execution report required

Post the result back to the canonical issue with:

- Status
- Files Changed
- Validation Performed
- Demo Result
- Report Path
- Remaining Limitations
- Ready For Owner Test: Yes / No

Do not create a second handoff link.