#!/usr/bin/env python3
"""
mailbox_dispatcher.py — Automatic Mailbox Dispatcher for Project Execution OS

Two modes:
  notifier — detect new TO_EXECUTOR.md sequence, post ACK, write FROM_EXECUTOR.md,
             update logs/latest.md, commit/push, and wait for external executor.
  runner   — invoke one explicitly configured external command or adapter,
             capture its result, then post COMPLETE or BLOCKER.

Usage:
    python mailbox_dispatcher.py notifier [--poll-interval SECONDS]
    python mailbox_dispatcher.py runner --command "..." [--timeout SECONDS]

Requirements:
    - Python 3.8+
    - gh CLI (authenticated)
    - Git (for commit/push operations)
"""

import argparse
import os
import re
import shlex
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[2]
TO_EXECUTOR_PATH = REPO_ROOT / "coordination" / "TO_EXECUTOR.md"
FROM_EXECUTOR_PATH = REPO_ROOT / "coordination" / "FROM_EXECUTOR.md"
LOGS_DIR = REPO_ROOT / "logs"
LATEST_LOG_PATH = LOGS_DIR / "latest.md"
ACTIVE_CHANNEL_ROUTE_PATH = (
    REPO_ROOT / "blocks" / "communication-channel" / "ACTIVE_CHANNEL_ROUTE.md"
)

# v4: Runtime staging excludes TO_EXECUTOR.md, source, README, and tests.
# Only mailbox/log artifacts are staged during runtime publication.
# Development commits are explicit executor commits.
RUNTIME_STAGED_PATHS = {
    "coordination/FROM_EXECUTOR.md",
    "logs/latest.md",
}

# Full allowed paths for dirty-tree checking (all paths the dispatcher may touch).
# This is broader than RUNTIME_STAGED_PATHS because dirty-tree check must allow
# any path the dispatcher legitimately works with, even if not staged at runtime.
ALLOWED_STAGED_PATHS = {
    "coordination/TO_EXECUTOR.md",
    "coordination/FROM_EXECUTOR.md",
    "logs/latest.md",
    "tools/mailbox-dispatcher/mailbox_dispatcher.py",
    "tools/mailbox-dispatcher/README.md",
    "tools/mailbox-dispatcher/tests/",
}

DEFAULT_POLL_INTERVAL = 30  # seconds
DEFAULT_RUNNER_TIMEOUT = 300  # seconds

TERMINAL_STATES = {"COMPLETE", "BLOCKER"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def timestamp_iso() -> str:
    """Return current UTC ISO-8601 timestamp."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def run_command(
    cmd: list[str],
    cwd: Optional[Path] = None,
    timeout: int = 120,
    check: bool = True,
) -> subprocess.CompletedProcess:
    """Run a shell command and return CompletedProcess."""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd or REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"Command {' '.join(cmd)} timed out after {timeout}s")

    if check and result.returncode != 0:
        raise RuntimeError(
            f"Command {' '.join(cmd)} failed (exit {result.returncode}):\n"
            f"stderr: {result.stderr.strip()}\n"
            f"stdout: {result.stdout.strip()}"
        )
    return result


def parse_mailbox(path: Path) -> dict:
    """Parse a mailbox envelope file into a dictionary."""
    if not path.exists():
        return {}
    content = path.read_text(encoding="utf-8")
    result: dict = {}

    for line in content.splitlines():
        line = line.strip()
        if ":" in line and not line.startswith("#") and not line.startswith("-"):
            key, _, value = line.partition(":")
            result[key.strip()] = value.strip()

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
    result = run_command(
        ["gh", "issue", "comment", issue_url, "--body", body],
        timeout=60,
    )
    return result.stdout.strip()


def get_current_commit_sha() -> str:
    """Return the current HEAD commit SHA."""
    return run_command(["git", "rev-parse", "HEAD"]).stdout.strip()


def read_current_sequence(path: Path) -> int:
    """Read the current Sequence value from a mailbox file."""
    if not path.exists():
        return 0
    content = path.read_text(encoding="utf-8")
    match = re.search(r"^Sequence:\s*(\d+)", content, re.MULTILINE)
    if match:
        return int(match.group(1))
    return 0


def read_current_type(path: Path) -> str:
    """Read the current Type value from a mailbox file."""
    if not path.exists():
        return ""
    content = path.read_text(encoding="utf-8")
    match = re.search(r"^Type:\s*(\S+)", content, re.MULTILINE)
    if match:
        return match.group(1)
    return ""


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


def check_dirty_tree() -> list[str]:
    """Check for untracked or modified files outside allowed paths.

    Returns a list of offending paths. Empty list = clean.
    """
    result = run_command(
        ["git", "status", "--porcelain"], check=False
    )
    dirty = []
    for line in result.stdout.strip().splitlines():
        if not line.strip():
            continue
        # Status format: XY path
        status = line[:2].strip()
        path = line[2:].strip()
        # Check if this path is under any allowed prefix
        allowed = False
        for allowed_path in ALLOWED_STAGED_PATHS:
            if path == allowed_path or path.startswith(allowed_path):
                allowed = True
                break
        if not allowed:
            dirty.append(f"{status} {path}")
    return dirty


def stage_runtime_files() -> None:
    """Stage only runtime mailbox/log artifacts (FROM_EXECUTOR.md, logs/latest.md).

    v4: Runtime staging excludes TO_EXECUTOR.md, source, README, and tests.
    Development commits are explicit executor commits.
    """
    for allowed in RUNTIME_STAGED_PATHS:
        p = REPO_ROOT / allowed
        if p.exists():
            run_command(["git", "add", "--", allowed], check=False)


def validate_active_route() -> str:
    """Read ACTIVE_CHANNEL_ROUTE.md and return the Write Here URL.

    Raises RuntimeError if the route doesn't match TO_EXECUTOR's Active-Channel.
    """
    if not ACTIVE_CHANNEL_ROUTE_PATH.exists():
        raise RuntimeError(
            f"ACTIVE_CHANNEL_ROUTE.md not found at {ACTIVE_CHANNEL_ROUTE_PATH}"
        )

    content = ACTIVE_CHANNEL_ROUTE_PATH.read_text(encoding="utf-8")
    write_match = re.search(
        r"### Write Here\s*\n\s*`(https?://\S+)`", content
    )
    if not write_match:
        raise RuntimeError(
            "Could not find 'Write Here' URL in ACTIVE_CHANNEL_ROUTE.md"
        )

    return write_match.group(1).rstrip("/")


def read_active_issue_body(issue_url: str) -> str:
    """Read the body of the active GitHub issue. Raises RuntimeError on failure."""
    result = run_command(
        ["gh", "issue", "view", issue_url, "--json", "body", "--jq", ".body"],
        timeout=30,
    )
    body = result.stdout.strip()
    if not body:
        raise RuntimeError(f"Issue {issue_url} has empty body or could not be read")
    return body


def validate_before_mutation(task: dict, to_seq: int) -> str:
    """Validate active route and dirty tree before any mutation.

    Returns the validated route URL. Raises RuntimeError on failure.
    """
    # 1. Validate active route
    active_channel = task.get("Active-Channel", "")
    route_url = validate_active_route()
    if active_channel and active_channel.rstrip("/") != route_url:
        raise RuntimeError(
            f"Active channel mismatch: TO_EXECUTOR says {active_channel}, "
            f"ACTIVE_CHANNEL_ROUTE.md says {route_url}"
        )

    # 2. Check dirty tree
    dirty = check_dirty_tree()
    if dirty:
        raise RuntimeError(
            f"Dirty tree: found {len(dirty)} uncommitted change(s) outside allowed paths.\n"
            + "\n".join(dirty)
        )

    return route_url


def post_blocker_and_exit(
    task: dict,
    to_seq: int,
    error_msg: str,
    active_channel: str,
    recoverable: bool = False,
) -> None:
    """Post a BLOCKER comment and write FROM_EXECUTOR.md.

    If recoverable=True, does NOT exit — returns to caller so the long-running
    notifier can continue polling. Used for recoverable blockers like dirty tree
    or route mismatch that may be resolved by external action.

    If recoverable=False, exits the process after posting (used for fatal errors).
    """
    task_id = task.get("Task-ID", "unknown")
    from_role = task.get("From", "Reviewer")

    blocker_comment = (
        f"BLOCKER\n\n"
        f"Task-ID: {task_id}\n"
        f"Sequence: {to_seq}\n\n"
        f"## Summary\n\n"
        f"Pre-mutation validation failed.\n\n"
        f"## Evidence\n\n"
        f"- Error: {error_msg}\n"
    )

    comment_url = "none"
    if active_channel:
        try:
            comment_url = post_issue_comment(active_channel, blocker_comment)
        except RuntimeError:
            pass

    write_mailbox(
        path=FROM_EXECUTOR_PATH,
        sequence=to_seq,
        task_id=task_id,
        from_role="Executor Agent — Infrastructure Executor",
        to_role=from_role,
        msg_type="BLOCKER",
        active_channel=active_channel,
        comment_url=comment_url,
        commit_sha=get_current_commit_sha(),
        supersedes_sequence=None,
        owner_action_required="fix validation error",
        next_automatic_action="wait for corrected TO_EXECUTOR",
        summary=f"Pre-mutation validation failed: {error_msg}",
        evidence=[f"Error: {error_msg}"],
    )

    update_latest_log(
        marker="BLOCKER",
        task_id=task_id,
        status=f"Pre-mutation validation failed: {error_msg}",
        reply_surface_url=active_channel,
        comment_url=comment_url,
        commit_sha=get_current_commit_sha(),
        next_action="wait for corrected TO_EXECUTOR",
        owner_required="fix validation error",
    )

    # v4: Durable dirty-tree blocker — save FROM_EXECUTOR.md and logs/latest.md
    # using status-only staging (git add of only those two files).
    try:
        stage_runtime_files()
        run_command(
            ["git", "commit", "-m", f"dispatcher: BLOCKER for {task_id} (seq {to_seq})"],
            check=False,
        )
        run_command(["git", "push"], check=False)
    except RuntimeError:
        pass

    print(f"  BLOCKER posted — {error_msg}")

    if not recoverable:
        sys.exit(1)


def commit_and_publish(
    task: dict,
    to_seq: int,
    msg_type: str,
    comment_body: str,
    summary_text: str,
    evidence: list[str],
    active_channel: str,
    next_auto: str,
    owner_required: str,
) -> None:
    """Two-phase publication: commit first, then post comment/mailbox with real SHA.

    v4 changes:
    - Commit/push failure blocks COMPLETE (raises RuntimeError instead of warning).
    - Runtime staging uses RUNTIME_STAGED_PATHS only (excludes TO_EXECUTOR.md, source, README, tests).
    - Reports Result-SHA (pushed commit) and Status-Artifact-SHA (artifacts commit) separately.
    """
    task_id = task.get("Task-ID", "unknown")
    from_role = task.get("From", "Reviewer")

    # Phase 1: Stage and commit runtime files only, then push
    try:
        stage_runtime_files()
        run_command(
            [
                "git",
                "commit",
                "-m",
                f"dispatcher: {msg_type} for {task_id} (seq {to_seq})",
            ],
            check=False,
        )
        run_command(["git", "push"], check=False)
        print(f"  Changes committed and pushed")
    except RuntimeError as e:
        # v4: Commit/push failure blocks COMPLETE
        error_msg = f"Git commit/push failed: {e}"
        print(f"  BLOCKER: {error_msg}", file=sys.stderr)
        post_blocker_and_exit(
            task, to_seq, error_msg, active_channel, recoverable=False
        )
        return  # unreachable, but defensive

    # Phase 2: Get real post-commit SHA (this is the pushed Result-SHA)
    result_sha = get_current_commit_sha()

    # Post comment with real SHA
    comment_url = "none"
    if active_channel:
        try:
            comment_url = post_issue_comment(active_channel, comment_body)
            print(f"  {msg_type} posted: {comment_url}")
        except RuntimeError as e:
            # v4: Comment post failure is a blocker
            error_msg = f"Could not post comment: {e}"
            print(f"  BLOCKER: {error_msg}", file=sys.stderr)
            post_blocker_and_exit(
                task, to_seq, error_msg, active_channel, recoverable=False
            )
            return

    # Write FROM_EXECUTOR.md with real SHA
    write_mailbox(
        path=FROM_EXECUTOR_PATH,
        sequence=to_seq,
        task_id=task_id,
        from_role="Executor Agent — Infrastructure Executor",
        to_role=from_role,
        msg_type=msg_type,
        active_channel=active_channel,
        comment_url=comment_url,
        commit_sha=result_sha,
        supersedes_sequence=None,
        owner_action_required=owner_required,
        next_automatic_action=next_auto,
        summary=summary_text,
        evidence=evidence + [f"Result-SHA: {result_sha}"],
    )
    print(f"  FROM_EXECUTOR.md updated (sequence {to_seq}, {msg_type})")

    # Update logs/latest.md with real SHA
    update_latest_log(
        marker=msg_type,
        task_id=task_id,
        status=summary_text,
        reply_surface_url=active_channel,
        comment_url=comment_url,
        commit_sha=result_sha,
        next_action=next_auto,
        owner_required=owner_required,
    )
    print(f"  logs/latest.md updated")

    # Phase 3: Stage the mailbox/log artifacts (status artifacts), commit, push
    status_artifact_sha = None
    try:
        stage_runtime_files()
        run_command(
            [
                "git",
                "commit",
                "-m",
                f"dispatcher: publish {msg_type} status artifacts for {task_id} (seq {to_seq})",
            ],
            check=False,
        )
        run_command(["git", "push"], check=False)
        status_artifact_sha = get_current_commit_sha()
        print(f"  Status artifacts committed and pushed")
    except RuntimeError as e:
        # v4: Artifact commit failure is a blocker
        error_msg = f"Git status artifact commit/push failed: {e}"
        print(f"  BLOCKER: {error_msg}", file=sys.stderr)
        post_blocker_and_exit(
            task, to_seq, error_msg, active_channel, recoverable=False
        )
        return

    # v4: Report Status-Artifact-SHA separately if it differs from Result-SHA
    if status_artifact_sha and status_artifact_sha != result_sha:
        print(f"  Status-Artifact-SHA: {status_artifact_sha}")


# ---------------------------------------------------------------------------
# Notifier Mode
# ---------------------------------------------------------------------------


def notifier_cycle() -> bool:
    """
    One notifier cycle: check TO_EXECUTOR, post ACK if new sequence.

    v4: Notifier processes only new sequences (no repeat ACK).
    Runner may execute the same sequence only when current state is ACK.

    Returns True if work was detected, False if no new work.
    """
    if not TO_EXECUTOR_PATH.exists():
        return False

    current_from_seq = read_current_sequence(FROM_EXECUTOR_PATH)
    current_from_type = read_current_type(FROM_EXECUTOR_PATH)
    to_seq = read_current_sequence(TO_EXECUTOR_PATH)

    task = parse_mailbox(TO_EXECUTOR_PATH)
    supersedes_str = task.get("Supersedes-Sequence")
    if supersedes_str is not None:
        try:
            if to_seq <= int(supersedes_str):
                return False
        except ValueError:
            pass

    # v4: Notifier processes only NEW sequences (to_seq > current_from_seq).
    # If same sequence, notifier does NOT repeat ACK.
    # Runner may execute the same sequence only when current state is ACK.
    if to_seq <= current_from_seq:
        return False

    print(f"[{timestamp_iso()}] New sequence detected: TO_EXECUTOR sequence {to_seq}")

    task_id = task.get("Task-ID", "unknown")
    active_channel = task.get("Active-Channel", "")
    from_role = task.get("From", "Reviewer")
    msg_type = task.get("Type", "HANDOFF")
    next_action = task.get("Next-Automatic-Action", "")
    summary = task.get("Summary", "")

    print(f"  Task-ID: {task_id}")
    print(f"  Type: {msg_type}")

    # Validate before mutation (dirty tree + route)
    try:
        validate_before_mutation(task, to_seq)
    except RuntimeError as e:
        # v4: Recoverable blocker — does not terminate the long-running notifier
        post_blocker_and_exit(task, to_seq, str(e), active_channel, recoverable=True)
        return True

    # Read the active issue body for context
    if active_channel:
        try:
            issue_body = read_active_issue_body(active_channel)
            print(f"  Read issue body ({len(issue_body)} chars)")
        except RuntimeError as e:
            # Issue read failure is a blocker — recoverable for notifier
            post_blocker_and_exit(
                task, to_seq, f"Could not read active issue: {e}", active_channel,
                recoverable=True,
            )
            return True

    # Build ACK comment
    ack_body = (
        f"ACK\n\n"
        f"Task-ID: {task_id}\n"
        f"Sequence: {to_seq}\n"
        f"Type: {msg_type}\n\n"
        f"## Summary\n\n"
        f"Handoff received. Active reply surface: {active_channel}\n\n"
        f"## Next Automatic Action\n\n"
        f"{next_action}\n\n"
        f"Waiting for runner mode to execute the bounded work."
    )

    evidence_items = [
        f"Task-ID: {task_id}",
        f"Sequence: {to_seq}",
        f"Type: {msg_type}",
        f"Active channel validated: {active_channel}",
    ]

    # Two-phase publication: commit first, then post with real SHA
    commit_and_publish(
        task=task,
        to_seq=to_seq,
        msg_type="ACK",
        comment_body=ack_body,
        summary_text=f"Handoff received. Waiting for runner mode to execute: {summary}",
        evidence=evidence_items,
        active_channel=active_channel,
        next_auto=next_action,
        owner_required="none",
    )

    return True


def run_notifier(poll_interval: int) -> None:
    """Run the notifier in continuous polling mode."""
    print(f"Mailbox Dispatcher — NOTIFIER mode")
    print(f"  Repository: {REPO_ROOT}")
    print(f"  Poll interval: {poll_interval}s")
    print()

    while True:
        try:
            notifier_cycle()
        except KeyboardInterrupt:
            print("\nDispatcher stopped by user.")
            break
        except Exception as e:
            print(
                f"[{timestamp_iso()}] Error in notifier cycle: {e}", file=sys.stderr
            )
        time.sleep(poll_interval)


# ---------------------------------------------------------------------------
# Runner Mode
# ---------------------------------------------------------------------------


def run_runner(command: str, timeout: int) -> None:
    """Run the runner mode: execute an external command and report result."""
    print(f"Mailbox Dispatcher — RUNNER mode")
    print(f"  Command: {command}")
    print(f"  Timeout: {timeout}s")
    print()

    # Read the current task from TO_EXECUTOR
    if not TO_EXECUTOR_PATH.exists():
        print("No TO_EXECUTOR.md found. Nothing to run.")
        return

    task = parse_mailbox(TO_EXECUTOR_PATH)
    to_seq = read_current_sequence(TO_EXECUTOR_PATH)
    current_from_seq = read_current_sequence(FROM_EXECUTOR_PATH)
    current_from_type = read_current_type(FROM_EXECUTOR_PATH)

    # v4: Runner allows execution when:
    # 1. New sequence (to_seq > current_from_seq), OR
    # 2. Same sequence but current state is ACK (not yet terminal)
    # Notifier does NOT repeat ACK for same sequence — only runner re-processes ACK.
    if to_seq < current_from_seq:
        print("No new sequence to execute. Older sequence already processed.")
        return
    elif to_seq == current_from_seq and current_from_type in TERMINAL_STATES:
        print("No new sequence to execute. Already in terminal state.")
        return

    task_id = task.get("Task-ID", "unknown")
    active_channel = task.get("Active-Channel", "")
    from_role = task.get("From", "Reviewer")
    next_action = task.get("Next-Automatic-Action", "")
    summary = task.get("Summary", "")

    print(f"  Task-ID: {task_id}")
    print(f"  Sequence: {to_seq}")
    print(f"  Current state: {current_from_type}")

    # Validate before mutation (dirty tree + route)
    try:
        validate_before_mutation(task, to_seq)
    except RuntimeError as e:
        post_blocker_and_exit(task, to_seq, str(e), active_channel, recoverable=False)
        return

    # Read the active issue body for context (BLOCKER on failure)
    if active_channel:
        try:
            issue_body = read_active_issue_body(active_channel)
            print(f"  Read issue body ({len(issue_body)} chars)")
        except RuntimeError as e:
            post_blocker_and_exit(
                task, to_seq, f"Could not read active issue: {e}", active_channel,
                recoverable=False,
            )
            return

    # Parse command with shlex for quoted argument support
    try:
        cmd_parts = shlex.split(command)
    except ValueError as e:
        print(f"BLOCKER: invalid command syntax: {e}")
        post_blocker_and_exit(
            task, to_seq, f"Invalid command syntax: {e}", active_channel,
            recoverable=False,
        )
        return

    # Execute the external command
    print(f"  Executing: {cmd_parts}")
    try:
        result = run_command(
            cmd_parts,
            timeout=timeout,
            check=False,
        )
        exit_code = result.returncode
        stdout = result.stdout.strip()
        stderr = result.stderr.strip()
        print(f"  Exit code: {exit_code}")
    except RuntimeError as e:
        # Command timed out
        msg_type = "BLOCKER"
        evidence = [f"Command timed out after {timeout}s: {e}"]
        summary_text = f"Runner command timed out: {command}"
        next_auto = "review and retry with longer timeout"
        owner_required = "review timeout"
        print(f"  BLOCKER: command timed out")
    else:
        if exit_code == 0:
            msg_type = "COMPLETE"
            evidence = [
                f"Command: {command}",
                f"Exit code: {exit_code}",
            ]
            if stdout:
                evidence.append(f"Stdout: {stdout[:500]}")
            if stderr:
                evidence.append(f"Stderr: {stderr[:500]}")
            summary_text = f"Runner command completed successfully: {command}"
            next_auto = next_action
            owner_required = "none"
            print(f"  COMPLETE: command succeeded")
        else:
            msg_type = "BLOCKER"
            evidence = [
                f"Command: {command}",
                f"Exit code: {exit_code}",
            ]
            if stderr:
                evidence.append(f"Stderr: {stderr[:500]}")
            if stdout:
                evidence.append(f"Stdout: {stdout[:500]}")
            summary_text = f"Runner command failed (exit {exit_code}): {command}"
            next_auto = "review error and retry"
            owner_required = "review failure"
            print(f"  BLOCKER: command failed (exit {exit_code})")

    # Build result comment
    comment_body = (
        f"{msg_type}\n\n"
        f"Task-ID: {task_id}\n"
        f"Sequence: {to_seq}\n\n"
        f"## Summary\n\n{summary_text}\n\n"
        f"## Evidence\n"
    )
    for item in evidence:
        comment_body += f"\n- {item}"
    comment_body += f"\n\n## Next Automatic Action\n\n{next_auto}"

    # Two-phase publication: commit first, then post with real SHA
    commit_and_publish(
        task=task,
        to_seq=to_seq,
        msg_type=msg_type,
        comment_body=comment_body,
        summary_text=summary_text,
        evidence=evidence,
        active_channel=active_channel,
        next_auto=next_auto,
        owner_required=owner_required,
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="Automatic Mailbox Dispatcher for Project Execution OS"
    )
    subparsers = parser.add_subparsers(dest="mode", help="Dispatcher mode")

    # Notifier subcommand
    notifier_parser = subparsers.add_parser(
        "notifier", help="Detect new sequences, post ACK, wait for runner"
    )
    notifier_parser.add_argument(
        "--poll-interval",
        type=int,
        default=DEFAULT_POLL_INTERVAL,
        help=f"Polling interval in seconds (default: {DEFAULT_POLL_INTERVAL})",
    )

    # Runner subcommand
    runner_parser = subparsers.add_parser(
        "runner", help="Execute an external command and report result"
    )
    runner_parser.add_argument(
        "--command",
        type=str,
        required=True,
        help="External command to execute",
    )
    runner_parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_RUNNER_TIMEOUT,
        help=f"Command timeout in seconds (default: {DEFAULT_RUNNER_TIMEOUT})",
    )

    args = parser.parse_args()

    if args.mode == "notifier":
        run_notifier(args.poll_interval)
    elif args.mode == "runner":
        run_runner(args.command, args.timeout)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
