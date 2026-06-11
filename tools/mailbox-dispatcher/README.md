# Mailbox Dispatcher

Automatic polling bridge between `coordination/TO_EXECUTOR.md` and `coordination/FROM_EXECUTOR.md` for Project Execution OS.

## Purpose

Removes the need for the owner to manually relay routine messages between a reasoning agent (reviewer) and an execution agent. The dispatcher watches the reviewer-to-executor mailbox for sequence changes, reads the active GitHub issue, executes approved bounded work, writes the executor-to-reviewer mailbox, and posts matching status comments.

## How It Works

```text
Reviewer writes TO_EXECUTOR.md (new sequence)
        │
        ▼
Dispatcher polls (every N seconds)
        │
        ├─ Reads TO_EXECUTOR.md
        ├─ Compares sequence with FROM_EXECUTOR.md
        ├─ If new: parses task envelope
        ├─ Executes bounded work
        ├─ Posts status comment to active GitHub issue
        ├─ Writes FROM_EXECUTOR.md with result
        ├─ Updates logs/latest.md
        └─ Commits and pushes changes
```

## Requirements

- **Python 3.8+**
- **gh CLI** — authenticated with a GitHub token that has `issues:write` permission on the repository
- **Git** — configured with user.name and user.email for automated commits

## Installation

```bash
# Navigate to the dispatcher directory
cd tools/mailbox-dispatcher

# No dependencies beyond Python standard library
# Verify Python and gh are available
python --version
gh --version
```

## Usage

### Single cycle (for testing or cron)

```bash
python mailbox_dispatcher.py --once
```

### Continuous polling (for long-running sessions)

```bash
python mailbox_dispatcher.py --poll-interval 30
```

The default poll interval is 30 seconds. Adjust based on your latency requirements.

### Arguments

| Argument | Default | Description |
|---|---|---|
| `--poll-interval SECONDS` | `30` | Polling interval in seconds |
| `--once` | `false` | Run a single dispatch cycle and exit |

## Security Boundary

1. **No secrets in repository.** The dispatcher uses `gh` CLI, which stores its authentication token outside the repository (in the system credential store or GitHub CLI config).
2. **Bounded execution only.** The dispatcher only executes safe operations:
   - Reading and writing mailbox files (`coordination/TO_EXECUTOR.md`, `coordination/FROM_EXECUTOR.md`)
   - Posting comments to GitHub issues via `gh`
   - Running `git add`, `git commit`, `git push`
3. **No destructive actions.** The dispatcher does not delete files, modify repository settings, change visibility, deploy to production, or execute arbitrary code from task envelopes.
4. **No external network access** beyond the GitHub API (via `gh`).

## Restart Behavior

- **Idempotent.** If the dispatcher restarts, it reads the current sequence from `FROM_EXECUTOR.md` and compares it with `TO_EXECUTOR.md`. Already-processed sequences are skipped.
- **No duplicate comments.** The dispatcher checks the sequence before posting. If `FROM_EXECUTOR.md` sequence >= `TO_EXECUTOR.md` sequence, no action is taken.
- **Crash recovery.** On restart after a crash, the dispatcher resumes from the last committed state. Uncommitted local changes are detected by `git status` and reported.

## Failure Recovery

| Failure Mode | Behavior |
|---|---|
| `gh` not authenticated | Dispatcher logs error and continues polling. No comment is posted. |
| Git push fails (network) | Local commit is made. Next cycle will attempt push again. |
| Mailbox file missing | Dispatcher logs warning and continues polling. |
| Invalid sequence value | Dispatcher logs error and continues polling. |
| Python exception | Caught by main loop. Error is logged. Polling continues. |

## Process Management

### Windows (PowerShell)

```powershell
# Start in background
Start-Process -NoNewWindow python "mailbox_dispatcher.py --poll-interval 30"

# Stop (find and kill the process)
Get-Process -Name python | Where-Object { $_.CommandLine -like "*mailbox_dispatcher*" } | Stop-Process
```

### Linux / macOS

```bash
# Start in background with nohup
nohup python mailbox_dispatcher.py --poll-interval 30 > dispatcher.log 2>&1 &

# Stop
pkill -f "mailbox_dispatcher.py"
```

### Systemd (Linux)

```ini
[Unit]
Description=Project Execution OS Mailbox Dispatcher
After=network.target

[Service]
Type=simple
WorkingDirectory=/path/to/Project-Execution-OS
ExecStart=/usr/bin/python3 /path/to/Project-Execution-OS/tools/mailbox-dispatcher/mailbox_dispatcher.py --poll-interval 30
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
│   ├── TO_EXECUTOR.md        # Reviewer → Executor (watched by dispatcher)
│   ├── FROM_EXECUTOR.md      # Executor → Reviewer (written by dispatcher)
│   └── CHECKPOINT.md         # Safe checkpoint state
├── logs/
│   └── latest.md             # Current status mirror
└── tools/
    └── mailbox-dispatcher/
        ├── mailbox_dispatcher.py   # The dispatcher script
        └── README.md               # This file
```

## Mailbox Envelope Format

See `docs/EXECUTOR_MAILBOX_STANDARD.md` for the canonical envelope specification.

## Related Standards

- `docs/EXECUTOR_MAILBOX_STANDARD.md` — Mailbox protocol specification
- `docs/EXECUTOR_CHANNEL_ACK_AND_PUBLISH_STANDARD.md` — Executor acknowledgement and publication rules
- `blocks/communication-channel/BLOCK.md` — Communication channel routing
- `blocks/communication-channel/ACTIVE_CHANNEL_ROUTE.md` — Active channel pointer
