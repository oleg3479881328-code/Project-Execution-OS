# AI Hands Agent Instructions

## Required Entry Order

Before project work:

1. Read `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/START_HERE.md`.
2. Read `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/docs/ROUTER.md`.
3. Read `projects/ai-hands/PROJECT.md`.
4. Read `projects/ai-hands/PROJECT_STATE.md`.
5. Read `projects/ai-hands/logs/latest.md`.
6. Read only the minimum additional files required for the active task.

## Project-Specific Guardrails

- This directory is an internal subproject. Never run nested `git init` here.
- Treat the parent `Project-Execution-OS` repository as the Git boundary.
- Apply Existing Solution First before creating an executor, adapter, protocol, or integration.
- Verify the owner's actual local environment directly before choosing a model or runtime.
- Never rely on remembered hardware or model lists as authoritative.
- Use an isolated branch or worktree for every local executor run.
- Do not permit direct writes to the default branch by the local model.
- Keep command execution allowlisted during MVP 1.
- Require owner approval for destructive, privileged, credential-related, externally publishing, or security-sensitive actions.
- Store secrets outside the repository and never write them into logs or examples.
- Every execution attempt must return a diff, commands run, validation results, errors, and the next recommended action.

## Working Rule

The controller decides and verifies. The local executor performs bounded mechanical work. Codex or another stronger executor may be used for escalation, but the project must not depend on a single model provider.

## Central Standards

- Existing Solution First: `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
- Transfer readiness: `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md`
- File organization: `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/docs/FILE_ORGANIZATION_STANDARD.md`
- Official communication channel: `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/blocks/communication-channel/BLOCK.md`
