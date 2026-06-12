# Mailbox Dispatcher

Automatic polling bridge between `coordination/TO_EXECUTOR.md` and `coordination/FROM_EXECUTOR.md` for Project Execution OS.

## Purpose

Removes the need for the owner to manually relay routine messages between a reasoning agent (reviewer) and an execution agent. The dispatcher has two modes:

- **Notifier** — watches `TO_EXECUTOR.md` for **new** sequence changes, validates the active route and runtime dirty tree before any mutation, reads the active issue body, posts `ACK`, writes `FROM_EXECUTOR.md`, and waits for an external executor. Recoverable blockers do not terminate the long-running notifier.
- **Runner** — invokes one explicitly configured external command, expects a structured JSON adapter result, then posts `COMPLETE` or `BLOCKER`. The command comes from the `--command` CLI argument, **never from mailbox content**.

## How It Works

```text
Reviewer writes TO_EXECUTOR.md (new sequence)
        │
        ▼
Notifier polls (every N seconds)
        │
        ├─ Reads TO_EXECUTOR.md
        ├─ Validates active route against ACTIVE_CHANNEL_ROUTE.md
        ├─ Checks dirty tree against runtime-owned files only
        ├─ Reads the active issue body (BLOCKER on failure)
        ├─ Persists runtime status locally and pushes it
        ├─ Posts ACK comment with durable SHA fields
        └─ Waits for external executor
                │
                ▼
Runner (invoked separately with --command "...")
        │
        ├─ Validates active route
        ├─ Checks dirty tree against runtime-owned files only
        ├─ Reads the active issue body (BLOCKER on failure)
        ├─ Allows same-sequence execution only from ACK state
        ├─ Parses command with shlex.split() (supports quoted arguments)
        ├─ Executes the external command (from CLI arg, NOT mailbox content)
        ├─ Parses adapter JSON: status, summary, result_sha, evidence
        ├─ Fails closed if COMPLETE leaves dirty non-runtime files behind
        ├─ Persists COMPLETE or BLOCKER locally and pushes it
        └─ Posts issue comment, then writes one immutable linkback artifact commit
```

## v7 Design Decisions

### Same-sequence runner gate

The runner may execute the current `TO_EXECUTOR.Sequence` only when `FROM_EXECUTOR.Sequence` matches and `FROM_EXECUTOR.Type == ACK`. Any other same-sequence state is skipped, including nonterminal states.

### Structured runner-adapter contract

On successful runner execution, the external adapter must emit JSON to stdout:

```json
{
  "status": "COMPLETE",
  "summary": "Short human-readable result",
  "result_sha": "40-char hex SHA or none",
  "evidence": ["fact one", "fact two"]
}
```

Rules:

- `status` must be `COMPLETE` or `BLOCKER`
- `summary` must be a non-empty string
- `result_sha` must be `none` or a full 40-character hexadecimal SHA
- `evidence` must be a list of strings

The dispatcher never re-labels its own mailbox/log status commit as an external work-result SHA.

### Durable publication fields

Runtime publication durably records:

1. **Result-SHA** — the commit containing the result state.
2. **Status-Artifact-SHA** — the status-artifact publication commit.
3. **Comment-URL** — the final issue comment URL after publication.

These fields are written to the GitHub comment, mailbox, and latest status mirror with matching semantics.

### Immutable linkback artifact

After the GitHub comment is published, the dispatcher writes one final immutable linkback artifact commit containing the final `Comment-URL`, `Result-SHA`, and `Status-Artifact-SHA`, then pushes it once.

A commit cannot durably contain its own final SHA. Because of that, the dispatcher does not try to store the linkback commit's own SHA inside mailbox or log contents. If that SHA needs to be reported, it is reported externally as `Linkback-Artifact-SHA`.

### Strict git return-code handling

Publication paths use strict command checking for `git status`, `git add`, `git commit`, and `git push`. A non-zero result is a `BLOCKER`, not a warning.

### Runtime dirty-tree policy is narrower than development policy

Runtime execution allows only:

- `coordination/FROM_EXECUTOR.md`
- `logs/latest.md`

Source files, tests, README, and `coordination/TO_EXECUTOR.md` are development artifacts and must not be dirty during runtime execution.

### Route preservation

The dispatcher validates `ACTIVE_CHANNEL_ROUTE.md` against the mailbox `Active-Channel` before any mutation. A mismatch is a `BLOCKER`.

### Post-run dirty-tree enforcement

The runner validates the dirty tree both before external execution and after adapter success. If non-runtime files become dirty after the adapter reports `COMPLETE`, the dispatcher fails closed and publishes a `BLOCKER` instead.

### Honest blocker persistence

If remote push fails while persisting a blocker, the dispatcher keeps a local pending marker with:

- `Local-Status-SHA`
- `Remote-Push: failed`

It does not falsely imply that the blocker was durably published remotely.

## Requirements

- **Python 3.8+**
- **gh CLI** — authenticated with a GitHub token that has `issues:write` permission on the repository
- **Git** — configured with `user.name` and `user.email` for automated commits

## Usage

### Notifier mode

```bash
python mailbox_dispatcher.py notifier --poll-interval 30
```

### Runner mode

```bash
python mailbox_dispatcher.py runner --command "python my_script.py" --timeout 300
```

### Tests

```bash
python -m unittest tools/mailbox-dispatcher/tests/test_dispatcher.py -v
```

## Security Boundary

1. The dispatcher does not load or execute command text from mailbox content.
2. The runner executes an **operator-supplied external command** with the current workstation user's permissions.
3. The dispatcher is not a sandbox. It does not enforce a network allowlist for the external command.
4. Runtime staging is limited to executor-owned mailbox/log artifacts.
5. Route mismatch or unexpected dirty source state becomes a `BLOCKER`.

## File Layout

```text
Project-Execution-OS/
├── coordination/
│   ├── TO_EXECUTOR.md
│   └── FROM_EXECUTOR.md
├── logs/
│   └── latest.md
└── tools/
    └── mailbox-dispatcher/
        ├── mailbox_dispatcher.py
        ├── README.md
        └── tests/
            └── test_dispatcher.py
```

## Related Standards

- `docs/EXECUTOR_MAILBOX_STANDARD.md`
- `docs/EXECUTOR_CHANNEL_ACK_AND_PUBLISH_STANDARD.md`
- `blocks/communication-channel/BLOCK.md`
- `blocks/communication-channel/ACTIVE_CHANNEL_ROUTE.md`
