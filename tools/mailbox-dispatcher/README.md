# Mailbox Dispatcher

Automatic polling bridge between `coordination/TO_EXECUTOR.md` and `coordination/FROM_EXECUTOR.md` for Project Execution OS.

## Purpose

Removes the need for the owner to manually relay routine messages between a reasoning agent (reviewer) and an execution agent. The dispatcher has two modes:

- **Notifier** — watches `TO_EXECUTOR.md` for **new** sequence changes (v4: no repeat ACK), validates the active route and dirty tree **before any mutation**, reads the active issue body (BLOCKER on failure), posts `ACK`, writes `FROM_EXECUTOR.md`, and waits for an external executor. Recoverable blockers do not terminate the long-running notifier.
- **Runner** — invokes one explicitly configured external command or adapter, captures its result, then posts `COMPLETE` or `BLOCKER`. The command comes from the `--command` CLI argument, **never from mailbox content** (v4 security boundary).

## How It Works

```text
Reviewer writes TO_EXECUTOR.md (new sequence)
        │
        ▼
Notifier polls (every N seconds)
        │
        ├─ Reads TO_EXECUTOR.md
        ├─ Validates active route against ACTIVE_CHANNEL_ROUTE.md
        ├─ Checks dirty tree (rejects changes outside allowed paths)
        ├─ Reads the active issue body (BLOCKER on failure)
        ├─ Posts ACK comment to active GitHub issue
        ├─ Writes FROM_EXECUTOR.md (Type: ACK)
        ├─ Updates logs/latest.md
        ├─ Stages only runtime files (FROM_EXECUTOR.md, logs/latest.md)
        └─ Two-phase commit: commit → get real SHA → post comment/mailbox/log → commit artifacts
                │
                ▼
Runner (invoked separately with --command "...")
        │
        ├─ Validates active route
        ├─ Checks dirty tree
        ├─ Reads the active issue body (BLOCKER on failure)
        ├─ Parses command with shlex.split() (supports quoted arguments)
        ├─ Executes the external command (from CLI arg, NOT mailbox content)
        ├─ Posts COMPLETE or BLOCKER comment
        ├─ Writes FROM_EXECUTOR.md
        ├─ Updates logs/latest.md
        └─ Two-phase commit: commit → get real SHA → post comment/mailbox/log → commit artifacts
```

## Key Design Decisions

### v4: Notifier Processes Only New Sequences

The notifier only posts ACK when `TO_EXECUTOR.md` sequence is **greater than** `FROM_EXECUTOR.md` sequence. It does **not** repeat ACK for the same sequence on every poll. The runner may execute the same sequence only when the current state is `ACK` (not terminal).

### v4: Commit/Push Failure Blocks COMPLETE

If `git commit` or `git push` fails during publication, the dispatcher posts a `BLOCKER` instead of silently continuing. This ensures the reviewer is always notified of publication failures.

### v4: Durable Dirty-Tree Blocker

When a dirty-tree blocker is posted, `FROM_EXECUTOR.md` and `logs/latest.md` are durably saved using status-only staging (`git add` of only those two files). This ensures the blocker state survives a crash or restart.

### v4: Recoverable Blocker Does Not Terminate Notifier

In the notifier, validation failures (dirty tree, route mismatch, issue read failure) post a `BLOCKER` but do **not** exit the process. The notifier continues polling, allowing the blocker to be resolved externally. In the runner, blockers are fatal (process exits).

### v4: Two-SHA Publication

The dispatcher reports two SHAs separately:

1. **Result-SHA** — the SHA of the pushed commit containing the result (ACK, COMPLETE, or BLOCKER).
2. **Status-Artifact-SHA** — the SHA of the second commit containing mailbox/log artifacts, reported separately if it differs from Result-SHA.

### v4: Runtime Staging Boundary

Runtime staging (`stage_runtime_files()`) only stages `coordination/FROM_EXECUTOR.md` and `logs/latest.md`. It explicitly excludes:
- `coordination/TO_EXECUTOR.md` (reviewer-owned)
- `tools/mailbox-dispatcher/mailbox_dispatcher.py` (source — development commits are explicit executor commits)
- `tools/mailbox-dispatcher/README.md` (documentation)
- `tools/mailbox-dispatcher/tests/` (tests)

### v4: Runner Trust Boundary

The runner **never** executes command text from mailbox content. The command to execute is always provided via the `--command` CLI argument. Mailbox content is only used for metadata (Task-ID, Active-Channel, etc.) and context (Summary, Evidence).

### Two-Phase SHA Publication

The dispatcher uses a two-phase approach to ensure the commit SHA is real:

1. **Phase 1**: Stage runtime files, commit, push
2. **Phase 2**: Get the real post-commit SHA via `git rev-parse HEAD`, then post the GitHub comment and write mailbox/log files with the real SHA
3. **Phase 3**: Stage the mailbox/log artifacts, commit, push

This guarantees the SHA in the comment and mailbox is the actual committed SHA, not a pre-commit prediction.

### Pre-Mutation Validation

Before any mutation (posting comments, writing files, executing commands), the dispatcher validates:

1. **Active route**: Reads `ACTIVE_CHANNEL_ROUTE.md` and verifies it matches `TO_EXECUTOR.md`'s `Active-Channel`. Mismatch produces a `BLOCKER`.
2. **Dirty tree**: Checks for uncommitted changes outside allowed paths. If found, produces a `BLOCKER`.

### Terminal States

- `COMPLETE` — terminal state. Dispatcher skips already-processed sequences.
- `BLOCKER` — terminal state. Dispatcher waits for corrected input.
- `ACK` — NOT terminal. Allows runner to re-process the same sequence (e.g., after restart).

### Issue Read Failure = BLOCKER

If the active issue body cannot be read (network error, invalid URL, empty body), the dispatcher posts a `BLOCKER` — it does not silently continue with a warning.

### Quoted Argument Support

The runner uses `shlex.split()` instead of `str.split()` to parse the command, supporting quoted arguments:

```bash
python mailbox_dispatcher.py runner --command 'git commit -m "fix: resolve timeout"'
```

## Requirements

- **Python 3.8+**
- **gh CLI** — authenticated with a GitHub token that has `issues:write` permission on the repository
- **Git** — configured with `user.name` and `user.email` for automated commits

## Installation

```bash
cd tools/mailbox-dispatcher
python --version
gh --version
```

No dependencies beyond Python standard library.

## Usage

### Notifier mode (continuous polling)

```bash
python mailbox_dispatcher.py notifier --poll-interval 30
```

Detects new sequences in `TO_EXECUTOR.md`, posts `ACK`, and waits for a runner.

### Runner mode (single execution)

```bash
python mailbox_dispatcher.py runner --command "python my_script.py" --timeout 300
```

Executes the command, captures stdout/stderr/exit code, posts `COMPLETE` or `BLOCKER`.

### Arguments

#### Notifier

| Argument | Default | Description |
|---|---|---|
| `--poll-interval SECONDS` | `30` | Polling interval in seconds |

#### Runner

| Argument | Default | Description |
|---|---|---|
| `--command COMMAND` | (required) | External command to execute |
| `--timeout SECONDS` | `300` | Command timeout in seconds |

## Security Boundary

1. **No secrets in repository.** The dispatcher uses `gh` CLI, which stores its authentication token outside the repository.
2. **Bounded execution only.** The dispatcher only executes safe operations:
   - Reading and writing mailbox files (`coordination/TO_EXECUTOR.md`, `coordination/FROM_EXECUTOR.md`)
   - Posting comments to GitHub issues via `gh`
   - Running `git add` on explicitly allowed paths only
   - Running `git commit` and `git push`
3. **No destructive actions.** The dispatcher does not delete files, modify repository settings, change visibility, deploy to production, or execute arbitrary code from mailbox text.
4. **v4: Runner never executes mailbox content.** The command to execute is always provided via the `--command` CLI argument. Mailbox content is never used as a command source.
5. **Dirty-tree protection.** If uncommitted changes exist outside the allowed paths, the dispatcher refuses to proceed and posts a `BLOCKER`.
6. **Active route validation.** Before any action, the dispatcher reads `ACTIVE_CHANNEL_ROUTE.md` and verifies it matches `TO_EXECUTOR.md`'s `Active-Channel`. Mismatch produces a `BLOCKER`.
7. **No external network access** beyond the GitHub API (via `gh`).

## Restart Behavior

- **Idempotent.** If the dispatcher restarts, it reads the current sequence from `FROM_EXECUTOR.md` and compares it with `TO_EXECUTOR.md`. Already-processed sequences are skipped.
- **No duplicate comments.** The notifier only processes **new** sequences (v4). If `FROM_EXECUTOR.md` sequence >= `TO_EXECUTOR.md` sequence, no action is taken.
- **ACK re-processing (runner only).** If the state is `ACK` (not terminal), the runner will re-process the same sequence on restart. The notifier will not repeat ACK.
- **Crash recovery.** On restart after a crash, the dispatcher resumes from the last committed state.

## Failure Recovery

| Failure Mode | Behavior |
|---|---|
| `gh` not authenticated | Dispatcher logs error and continues polling. No comment is posted. |
| Git push fails (network) | **v4: BLOCKER is posted.** Commit/push failure blocks COMPLETE. |
| Mailbox file missing | Dispatcher logs warning and continues polling. |
| Invalid sequence value | Dispatcher logs error and continues polling. |
| Active route mismatch | `BLOCKER` is posted. Notifier continues polling (v4 recoverable). Runner exits. |
| Dirty tree outside allowed paths | `BLOCKER` is posted. Notifier continues polling (v4 recoverable). Runner exits. |
| Issue read failure | `BLOCKER` is posted (not a warning). Notifier continues polling (v4 recoverable). Runner exits. |
| Command timeout | `BLOCKER` is posted with timeout details. |
| Python exception | Caught by main loop. Error is logged. Polling continues. |

## Process Management

### Windows (PowerShell)

```powershell
# Start notifier in background
Start-Process -NoNewWindow python "mailbox_dispatcher.py notifier --poll-interval 30"

# Stop
Get-Process -Name python | Where-Object { $_.CommandLine -like "*mailbox_dispatcher*" } | Stop-Process
```

### Linux / macOS

```bash
# Start notifier in background
nohup python mailbox_dispatcher.py notifier --poll-interval 30 > dispatcher.log 2>&1 &

# Stop
pkill -f "mailbox_dispatcher.py"
```

### Systemd (Linux)

```ini
[Unit]
Description=Project Execution OS Mailbox Dispatcher (Notifier)
After=network.target

[Service]
Type=simple
WorkingDirectory=/path/to/Project-Execution-OS
ExecStart=/usr/bin/python3 /path/to/Project-Execution-OS/tools/mailbox-dispatcher/mailbox_dispatcher.py notifier --poll-interval 30
Restart=always
RestartSec=10
User=your-user

[Install]
WantedBy=multi-user.target
```

## File Layout

```
Project-Execution-OS/
├── coordination/
│   ├── TO_EXECUTOR.md        # Reviewer → Executor (watched by notifier)
│   ├── FROM_EXECUTOR.md      # Executor → Reviewer (written by dispatcher)
│   └── CHECKPOINT.md         # Safe checkpoint state
├── logs/
│   └── latest.md             # Current status mirror
└── tools/
    └── mailbox-dispatcher/
        ├── mailbox_dispatcher.py   # The dispatcher script (v4)
        ├── README.md               # This file
        └── tests/
            └── test_dispatcher.py  # Behavioral tests (v4)
```

## Mailbox Envelope Format

See `docs/EXECUTOR_MAILBOX_STANDARD.md` for the canonical envelope specification.

## Related Standards

- `docs/EXECUTOR_MAILBOX_STANDARD.md` — Mailbox protocol specification
- `docs/EXECUTOR_CHANNEL_ACK_AND_PUBLISH_STANDARD.md` — Executor acknowledgement and publication rules
- `blocks/communication-channel/BLOCK.md` — Communication channel routing
- `blocks/communication-channel/ACTIVE_CHANNEL_ROUTE.md` — Active channel pointer
