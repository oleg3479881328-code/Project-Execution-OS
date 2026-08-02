# AI Hands

## Project

- Name: `AI Hands`
- Project ID: `ai-hands`
- Type: `system`
- Short description: A local AI execution layer that receives bounded tasks prepared by ChatGPT and performs approved work on the owner's computer.

## Purpose

AI Hands exists to reduce the owner's technical participation to initiating an idea or goal while an AI execution system handles the mechanical implementation loop.

The first MVP proves a narrow end-to-end workflow:

1. ChatGPT prepares a structured execution task.
2. A local model receives the task through an execution adapter.
3. The local executor reads an approved project workspace.
4. It edits files in a separate Git branch.
5. It runs explicitly allowed checks.
6. It returns the diff, command results, failures, and a concise execution report.

Success for MVP 1 means one repeatable local-model execution cycle works without manual copying between multiple technical tools beyond initiating the run.

## System Entry Point

- `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/START_HERE.md`

## Operating Principle

- This project operates under Project Execution OS.
- Existing Solution First is mandatory.
- Prefer adapting a proven local-agent shell before building a custom agent runtime.
- The local model is an executor, not the durable source of truth.

## Source Of Truth

- GitHub: code, technical configuration, versioned project artifacts, tests, execution adapters, and implementation history.
- Notion: readable project status, roadmap, decisions, and coordination.
- Chat: active commands and discussion until durable decisions are written to GitHub or Notion.

## Source Trail

- Project repository path: `projects/ai-hands/`
- Notion project page: `https://app.notion.com/p/3b0a08dab069812e97f8e97ff84327e9`
- Durable environment evidence: `https://github.com/oleg3479881328-code/Project-Execution-OS/issues/96`
- Earlier donor discussion was not preserved as a recoverable source and is therefore not authoritative. Candidate order must be validated from official documentation and live local tests under Existing Solution First.

## Current Status

- Status: `active`
- Current mode: `execution`
- Phase: `MVP 1 bootstrap and environment discovery`
- Confidence: architecture direction confirmed; executor and model choice require live validation.

## Done So Far

- Project purpose and MVP boundary confirmed by the owner.
- GitHub and Notion selected as active durable layers.
- Notion project registry entry created.
- Internal project location selected inside Project Execution OS.
- Local environment inventory completed in Issue #96.

## Current Focus

Validate the smallest already-installed executor path against the verified local environment and prove one bounded local-model execution loop.

## Next Practical Step

Run WP-002: a safe smoke test using the installed Cline CLI and Ollama with a small local model, an isolated branch, a harmless file edit, an allowlisted validation command, and a complete diff/report.

## MVP 1 Scope

### In scope

- Local model connection.
- Structured task input prepared by ChatGPT.
- Approved workspace selection.
- File reading and bounded editing.
- Separate Git branch per execution.
- Allowlisted command execution.
- Test or validation command execution.
- Diff and execution report returned to the controller.
- Clear failure and escalation output.

### Out of scope

- Automatic merge to the default branch.
- Unrestricted shell access.
- Automatic destructive commands.
- Autonomous purchasing, credential creation, or external account changes.
- Full browser autonomy.
- Multi-user operation.
- Complex multi-agent orchestration before the basic loop works.

## Key Decisions And Constraints

- This is an internal subproject of `Project-Execution-OS`; do not create a nested Git repository.
- Use branch isolation for every executor run.
- Never let an untrusted local model write directly to the default branch.
- Start with one executor and one local model; add routing only after the base loop is reliable.
- Local hardware and installed models must be detected directly and must not be inferred from old chat statements.
- Apply Existing Solution First to executor selection; the currently preferred first test is Cline because WP-001 verified it is already installed, not because of an unrecoverable prior conversation.
- Require explicit approval for destructive, privileged, credential-related, network-sensitive, or externally publishing operations.

## MVP Acceptance Criteria

MVP 1 is complete when all of the following are demonstrated in one recorded run:

- A structured task is generated.
- A local model receives it without manual prompt reconstruction.
- The executor opens an approved test repository.
- It creates or uses a non-default branch.
- It makes a correct bounded file change.
- It runs an approved validation command.
- It reports command output and errors.
- It produces a readable diff and final execution summary.
- The default branch remains untouched unless the owner explicitly merges the result.

## Read Next

1. `AGENTS.md`
2. `PROJECT_STATE.md` when current execution state or continuity matters.
3. `logs/latest.md` when the latest executor status or result matters.
4. `https://github.com/oleg3479881328-code/Project-Execution-OS/issues/96`
5. `https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
