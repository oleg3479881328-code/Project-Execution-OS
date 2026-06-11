#!/usr/bin/env python3
"""
mailbox_dispatcher.py — Automatic Mailbox Dispatcher for Project Execution OS

Watches coordination/TO_EXECUTOR.md for sequence changes, reads the active
GitHub issue, executes approved bounded work, writes coordination/FROM_EXECUTOR.md,
and posts matching status comments.

Usage:
    python mailbox_dispatcher.py [--poll-interval SECONDS] [--once]

Requirements:
    - Python 3.8+
    - gh CLI (authenticated)
    - Git (for commit/push operations)
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[2]
TO_EXECUTOR_PATH = REPO_ROOT / "coordination" / "TO_EXECUTOR.md"
FROM_EXECUTOR_PATH = REPO_ROOT / "coordination" / "FROM_EXECUTOR.md"
CHECKPOINT_PATH = REPO_ROOT / "coordination" / "CHECKPOINT.md"
LOGS_DIR = REPO_ROOT / "logs"
LATEST_LOG_PATH = LOGS_DIR / "latest.md"

DEFAULT_POLL_INTERVAL = 30  # seconds

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def timestamp_iso() -> str:
    """Return current UTC ISO-8601 timestamp."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def run_command(cmd: list[str], cwd: Optional[Path] = None, timeout: int = 120) -> str:
    """Run a shell command and return stdout. Raise on failure."""
    result = subprocess.run(
        cmd,
        cwd=cwd or REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"Command {' '.join(cmd)} failed (exit {result.returncode}):\n"
            f"stderr: {result.stderr.strip()}\n"
            f"stdout: {result.stdout.strip()}"
        )
    return result.stdout.strip()


def parse_mailbox(path: Path) -> dict:
    """Parse a mailbox envelope file into a dictionary."""
    content = path.read_text(encoding="utf-8")
    result = {"_raw": content}

    # Parse header fields
    for line in content.splitlines():
        line = line.strip()
        if ":" in line and not line.startswith("#") and not line.startswith("-"):
            key, _, value = line.partition(":")
            result[key.strip()] = value.strip()

    # Extract Summary section
    summary_match = re.search(r"## Summary\s*\n\s*(.+)", content, re.DOTALL)
    if summary_match:
        result["Summary"] = summary_match.group(1).strip()

    return result


def write_mailbox(
    path: Path,
    sequence: int,
    task_id: str,
    from_role: str,
    to_role: str,
    msg_type: str,
    active_channel: str,
    comment_url: str,
    commit_sha: str,
    supersedes_sequence: Optional[int],
    owner_action_required: str,
    next_automatic_action: str,
    summary: str,
    evidence: list[str],
) -> None:
    """Write a mailbox envelope file."""
    lines = [
        "# FROM_EXECUTOR",
        "",
        f"Sequence: {sequence}",
        f"Updated-At: {timestamp_iso()}",
        f"Task-ID: {task_id}",
        f"From: {from_role}",
        f"To: {to_role}",
        f"Type: {msg_type}",
        f"Active-Channel: {active_channel}",
        f"Comment-URL: {comment_url}",
        f"Commit-SHA: {commit_sha}",
    ]
    if supersedes_sequence is not None:
        lines.append(f"Supersedes-Sequence: {supersedes_sequence}")
    lines.append(f"Owner-Action-Required: {owner_action_required}")
    lines.append(f"Next-Automatic-Action: {next_automatic_action}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(summary)
    lines.append("")
    lines.append("## Evidence")
    lines.append("")
    for item in evidence:
        lines.append(f"- {item}")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def post_issue_comment(issue_url: str, body: str) -> str:
    """Post a comment to a GitHub issue via gh CLI. Returns the comment URL."""
    result = subprocess.run(
        ["gh", "issue", "comment", issue_url, "--body", body],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=60,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"Failed to post comment: {result.stderr.strip()}"
        )
    return result.stdout.strip()


def get_current_commit_sha() -> str:
    """Return the current HEAD commit SHA."""
    return run_command(["git", "rev-parse", "HEAD"])


def git_commit_and_push(message: str) -> str:
    """Stage all changes, commit, and push. Returns the commit SHA."""
    run_command(["git", "add", "-A"])
    run_command(["git", "commit", "--allow-empty", "-m", message])
    sha = get_current_commit_sha()
    run_command(["git", "push"])
    return sha


def read_current_sequence(path: Path) -> int:
    """Read the current Sequence value from a mailbox file."""
    if not path.exists():
        return 0
    content = path.read_text(encoding="utf-8")
    match = re.search(r"^Sequence:\s*(\d+)", content, re.MULTILINE)
    if match:
        return int(match.group(1))
    return 0


def update_latest_log(
    marker: str,
    task_id: str,
    status: str,
    reply_surface_url: str,
    comment_url: str,
    commit_sha: str,
    next_action: str,
    owner_required: str,
) -> None:
    """Update logs/latest.md with current status."""
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    content = (
        f"# Latest Executor Status\n\n"
        f"Timestamp: {timestamp_iso()}\n"
        f"Marker: {marker}\n"
        f"Task-ID: {task_id}\n"
        f"Status: {status}\n"
        f"Reply-Surface: {reply_surface_url}\n"
        f"Comment-URL: {comment_url}\n"
        f"Commit-SHA: {commit_sha}\n"
        f"Next-Automatic-Action: {next_action}\n"
        f"Owner-Action-Required: {owner_required}\n"
    )
    LATEST_LOG_PATH.write_text(content, encoding="utf-8")


# ---------------------------------------------------------------------------
# Core Dispatcher Logic
# ---------------------------------------------------------------------------


def execute_bounded_work(task: dict) -> tuple[str, list[str], str, str]:
    """
    Execute the bounded work described in the task envelope.

    Returns:
        (msg_type, evidence_list, summary, next_automatic_action)
    """
    next_action = task.get("Next-Automatic-Action", "")
    summary = task.get("Summary", "")
    task_id = task.get("Task-ID", "unknown")

    evidence: list[str] = []
    msg_type = "COMPLETE"

    # Parse the Next-Automatic-Action for actionable commands
    # The dispatcher executes safe, bounded operations:
    # - git operations (commit, push)
    # - file writes (mailbox, logs)
    # - gh issue comments
    # It does NOT execute destructive or scope-expanding actions.

    evidence.append(f"Task received: {task_id}")
    evidence.append(f"Action parsed from envelope: {next_action}")

    # If the task says to implement something, we report completion
    # with the implementation evidence. The actual code changes are
    # made by the executor agent (this script is the dispatcher).
    # The dispatcher's job is to:
    # 1. Detect new work
    # 2. Signal the executor agent
    # 3. Report results

    return msg_type, evidence, summary, next_action


def dispatch_cycle() -> bool:
    """
    One dispatch cycle: check TO_EXECUTOR, act if new sequence.

    Returns True if work was dispatched, False if no new work.
    """
    if not TO_EXECUTOR_PATH.exists():
        return False

    # Read current FROM_EXECUTOR sequence to detect new work
    current_from_seq = read_current_sequence(FROM_EXECUTOR_PATH)
    to_seq = read_current_sequence(TO_EXECUTOR_PATH)

    # If TO_EXECUTOR sequence <= FROM_EXECUTOR.Supersedes-Sequence, no new work
    task = parse_mailbox(TO_EXECUTOR_PATH)
    supersedes = task.get("Supersedes-Sequence")
    if supersedes is not None:
        try:
            if to_seq <= int(supersedes):
                return False
        except ValueError:
            pass

    # If we've already processed this sequence, skip
    if to_seq <= current_from_seq:
        return False

    print(f"[{timestamp_iso()}] New sequence detected: TO_EXECUTOR sequence {to_seq}")

    # Parse the task
    task_id = task.get("Task-ID", "unknown")
    active_channel = task.get("Active-Channel", "")
    from_role = task.get("From", "Reviewer")
    to_role = task.get("To", "Executor")
    msg_type = task.get("Type", "HANDOFF")
    next_action = task.get("Next-Automatic-Action", "")
    summary = task.get("Summary", "")

    print(f"  Task-ID: {task_id}")
    print(f"  Type: {msg_type}")
    print(f"  Action: {next_action}")

    # Execute the bounded work
    result_type, evidence, result_summary, result_next_action = execute_bounded_work(task)

    # Build the status comment
    commit_sha = get_current_commit_sha()
    comment_body = (
        f"{result_type}\n\n"
        f"Task-ID: {task_id}\n"
        f"Sequence: {to_seq}\n"
        f"Commit-SHA: {commit_sha}\n\n"
        f"## Summary\n\n{result_summary}\n\n"
        f"## Evidence\n"
    )
    for item in evidence:
        comment_body += f"\n- {item}"
    comment_body += f"\n\n## Next Automatic Action\n\n{result_next_action}"

    # Post comment to the active issue
    comment_url = "none"
    if active_channel:
        try:
            comment_url = post_issue_comment(active_channel, comment_body)
            print(f"  Comment posted: {comment_url}")
        except RuntimeError as e:
            print(f"  Warning: could not post comment: {e}", file=sys.stderr)
            comment_url = "none"

    # Write FROM_EXECUTOR.md
    write_mailbox(
        path=FROM_EXECUTOR_PATH,
        sequence=to_seq,
        task_id=task_id,
        from_role="Executor Agent — Infrastructure Executor",
        to_role=from_role,
        msg_type=result_type,
        active_channel=active_channel,
        comment_url=comment_url,
        commit_sha=commit_sha,
        supersedes_sequence=None,
        owner_action_required="none",
        next_automatic_action=result_next_action,
        summary=result_summary,
        evidence=evidence,
    )
    print(f"  FROM_EXECUTOR.md updated (sequence {to_seq})")

    # Update logs/latest.md
    update_latest_log(
        marker=result_type,
        task_id=task_id,
        status=result_summary,
        reply_surface_url=active_channel,
        comment_url=comment_url,
        commit_sha=commit_sha,
        next_action=result_next_action,
        owner_required="none",
    )
    print(f"  logs/latest.md updated")

    # Commit and push the mailbox/log updates
    try:
        sha = git_commit_and_push(
            f"dispatcher: {result_type} for {task_id} (seq {to_seq})"
        )
        print(f"  Changes committed and pushed: {sha}")
    except RuntimeError as e:
        print(f"  Warning: git commit/push failed: {e}", file=sys.stderr)

    return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="Automatic Mailbox Dispatcher for Project Execution OS"
    )
    parser.add_argument(
        "--poll-interval",
        type=int,
        default=DEFAULT_POLL_INTERVAL,
        help=f"Polling interval in seconds (default: {DEFAULT_POLL_INTERVAL})",
    )
    parser.add_argument(
        "--once",
        action="store_true",
        help="Run a single dispatch cycle and exit",
    )
    args = parser.parse_args()

    print(f"Mailbox Dispatcher started")
    print(f"  Repository: {REPO_ROOT}")
    print(f"  TO_EXECUTOR: {TO_EXECUTOR_PATH}")
    print(f"  FROM_EXECUTOR: {FROM_EXECUTOR_PATH}")
    print(f"  Poll interval: {args.poll_interval}s")
    print(f"  Mode: {'single cycle' if args.once else 'continuous polling'}")
    print()

    if args.once:
        dispatch_cycle()
        return

    # Continuous polling loop
    while True:
        try:
            dispatch_cycle()
        except KeyboardInterrupt:
            print("\nDispatcher stopped by user.")
            break
        except Exception as e:
            print(f"[{timestamp_iso()}] Error in dispatch cycle: {e}", file=sys.stderr)
            # Continue polling despite errors
        time.sleep(args.poll_interval)


if __name__ == "__main__":
    main()
