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
import json
import re
import shlex
import subprocess
import sys
import time
from dataclasses import dataclass
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

# Runtime staging is intentionally narrow.
RUNTIME_STAGED_PATHS = {
    "coordination/FROM_EXECUTOR.md",
    "logs/latest.md",
}

# Development paths are allowed only when explicitly requested by a human
# executor during development work, not during runtime publication.
DEVELOPMENT_ALLOWED_PATHS = {
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
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class DispatchResult:
    """Structured publication result for durable reporting."""

    result_sha: str
    status_artifact_sha: str
    comment_url: str
    linkback_artifact_sha: Optional[str]
    summary_text: str
    evidence: list[str]


@dataclass
class AdapterResult:
    """Structured runner-adapter result contract."""

    status: str
    summary: str
    result_sha: str
    evidence: list[str]


@dataclass
class LinkbackState:
    """Result of post-comment linkback persistence."""

    linkback_artifact_sha: Optional[str]
    pending: bool
    evidence: list[str]


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

    summary_match = re.search(r"## Summary\s*\n\s*(.+?)(?:\n## |\Z)", content, re.DOTALL)
    if summary_match:
        result["Summary"] = summary_match.group(1).strip()

    evidence_match = re.search(r"## Evidence\s*\n\s*(.+)", content, re.DOTALL)
    if evidence_match:
        result["Evidence"] = evidence_match.group(1).strip()

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
    result_sha: str,
    status_artifact_sha: str,
    linkback_sha: Optional[str],
    local_status_sha: Optional[str],
    remote_push: Optional[str],
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
        f"Result-SHA: {result_sha}",
        f"Status-Artifact-SHA: {status_artifact_sha}",
    ]
    if linkback_sha is not None:
        lines.append(f"Linkback-SHA: {linkback_sha}")
    if local_status_sha is not None:
        lines.append(f"Local-Status-SHA: {local_status_sha}")
    if remote_push is not None:
        lines.append(f"Remote-Push: {remote_push}")
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
    result_sha: str,
    status_artifact_sha: str,
    linkback_sha: Optional[str],
    local_status_sha: Optional[str],
    remote_push: Optional[str],
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
        f"Result-SHA: {result_sha}\n"
        f"Status-Artifact-SHA: {status_artifact_sha}\n"
        f"Next-Automatic-Action: {next_action}\n"
        f"Owner-Action-Required: {owner_required}\n"
    )
    if linkback_sha is not None:
        content += f"Linkback-SHA: {linkback_sha}\n"
    if local_status_sha is not None:
        content += f"Local-Status-SHA: {local_status_sha}\n"
    if remote_push is not None:
        content += f"Remote-Push: {remote_push}\n"
    LATEST_LOG_PATH.write_text(content, encoding="utf-8")


def extract_linkback_artifact_sha(evidence: list[str]) -> Optional[str]:
    """Extract Linkback-Artifact-SHA from evidence lines when present."""
    prefix = "Linkback-Artifact-SHA: "
    for item in evidence:
        if item.startswith(prefix):
            value = item[len(prefix):].strip()
            if value:
                return value
    return None


def has_linkback_completion_marker(evidence: list[str]) -> bool:
    """Return True when durable evidence marks linkback as complete."""
    return "Linkback-State: complete" in evidence


def build_linkback_followup(linkback_artifact_sha: str) -> str:
    """Build a compact durable follow-up for linkback artifact reporting."""
    return (
        "Automatic linkback report\n\n"
        f"- Linkback-Artifact-SHA: `{linkback_artifact_sha}`\n"
        "- Linkback-State: complete\n"
    )


def get_dirty_entries() -> list[str]:
    """Return all dirty git entries from porcelain status."""
    result = run_command(["git", "status", "--porcelain"], check=True)
    entries = []
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        entries.append(line.rstrip())
    return entries


def filter_dirty_entries(entries: list[str], allowed_paths: set[str]) -> list[str]:
    """Filter dirty entries against the provided allowlist/prefix set."""
    offending = []
    for line in entries:
        status = line[:2].strip()
        path = line[3:].strip() if len(line) > 3 else ""
        allowed = False
        for allowed_path in allowed_paths:
            if path == allowed_path or path.startswith(allowed_path):
                allowed = True
                break
        if not allowed:
            offending.append(f"{status} {path}".strip())
    return offending


def check_dirty_tree_runtime() -> list[str]:
    """Return dirty entries outside the runtime-owned status artifacts."""
    return filter_dirty_entries(get_dirty_entries(), RUNTIME_STAGED_PATHS)


def stage_runtime_files() -> None:
    """Stage only runtime mailbox/log artifacts."""
    for allowed in sorted(RUNTIME_STAGED_PATHS):
        p = REPO_ROOT / allowed
        if p.exists():
            run_command(["git", "add", "--", allowed], check=True)


def validate_active_route() -> str:
    """Read ACTIVE_CHANNEL_ROUTE.md and return the Write Here URL."""
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
    """Validate active route and runtime dirty tree before any mutation."""
    active_channel = task.get("Active-Channel", "")
    route_url = validate_active_route()
    if active_channel and active_channel.rstrip("/") != route_url:
        raise RuntimeError(
            f"Active channel mismatch: TO_EXECUTOR says {active_channel}, "
            f"ACTIVE_CHANNEL_ROUTE.md says {route_url}"
        )

    dirty = check_dirty_tree_runtime()
    if dirty:
        raise RuntimeError(
            f"Dirty tree: found {len(dirty)} uncommitted change(s) outside runtime-owned paths.\n"
            + "\n".join(dirty)
        )

    return route_url


def persist_runtime_status(
    task_id: str,
    sequence: int,
    active_channel: str,
    comment_url: str,
    summary: str,
    evidence: list[str],
    next_action: str,
    owner_required: str,
    msg_type: str,
    result_sha_hint: str,
) -> tuple[str, str]:
    """Write runtime status artifacts and return status commit SHAs after durable push."""
    write_mailbox(
        path=FROM_EXECUTOR_PATH,
        sequence=sequence,
        task_id=task_id,
        from_role="Executor Agent — Infrastructure Executor",
        to_role="ChatGPT — Reviewer",
        msg_type=msg_type,
        active_channel=active_channel,
        comment_url=comment_url,
        result_sha=result_sha_hint,
        status_artifact_sha="pending",
        linkback_sha=None,
        local_status_sha=None,
        remote_push="pending",
        supersedes_sequence=None,
        owner_action_required=owner_required,
        next_automatic_action=next_action,
        summary=summary,
        evidence=evidence,
    )
    update_latest_log(
        marker=msg_type,
        task_id=task_id,
        status=summary,
        reply_surface_url=active_channel,
        comment_url=comment_url,
        result_sha=result_sha_hint,
        status_artifact_sha="pending",
        linkback_sha=None,
        local_status_sha=None,
        remote_push="pending",
        next_action=next_action,
        owner_required=owner_required,
    )

    stage_runtime_files()
    commit_message = f"dispatcher: persist {msg_type} status for {task_id} (seq {sequence})"
    run_command(["git", "commit", "-m", commit_message], check=True)
    status_commit_sha = get_current_commit_sha()

    write_mailbox(
        path=FROM_EXECUTOR_PATH,
        sequence=sequence,
        task_id=task_id,
        from_role="Executor Agent — Infrastructure Executor",
        to_role="ChatGPT — Reviewer",
        msg_type=msg_type,
        active_channel=active_channel,
        comment_url=comment_url,
        result_sha=result_sha_hint,
        status_artifact_sha=status_commit_sha,
        linkback_sha=None,
        local_status_sha=None,
        remote_push="pending",
        supersedes_sequence=None,
        owner_action_required=owner_required,
        next_automatic_action=next_action,
        summary=summary,
        evidence=evidence
        + [
            f"Result-SHA: {result_sha_hint}",
            f"Status-Artifact-SHA: {status_commit_sha}",
        ],
    )
    update_latest_log(
        marker=msg_type,
        task_id=task_id,
        status=summary,
        reply_surface_url=active_channel,
        comment_url=comment_url,
        result_sha=result_sha_hint,
        status_artifact_sha=status_commit_sha,
        linkback_sha=None,
        local_status_sha=None,
        remote_push="pending",
        next_action=next_action,
        owner_required=owner_required,
    )
    stage_runtime_files()
    artifact_commit_message = (
        f"dispatcher: publish {msg_type} status artifacts for {task_id} (seq {sequence})"
    )
    run_command(["git", "commit", "-m", artifact_commit_message], check=True)
    status_artifact_sha = get_current_commit_sha()
    run_command(["git", "push"], check=True)
    return status_commit_sha, status_artifact_sha


def persist_blocker_locally(
    task_id: str,
    sequence: int,
    active_channel: str,
    comment_url: str,
    summary: str,
    evidence: list[str],
    next_action: str,
    owner_required: str,
) -> tuple[str, Optional[str]]:
    """Persist blocker state locally; push if possible, but surface failures honestly."""
    write_mailbox(
        path=FROM_EXECUTOR_PATH,
        sequence=sequence,
        task_id=task_id,
        from_role="Executor Agent — Infrastructure Executor",
        to_role="ChatGPT — Reviewer",
        msg_type="BLOCKER",
        active_channel=active_channel,
        comment_url=comment_url,
        result_sha="none",
        status_artifact_sha="pending",
        linkback_sha=None,
        local_status_sha=None,
        remote_push="pending",
        supersedes_sequence=None,
        owner_action_required=owner_required,
        next_automatic_action=next_action,
        summary=summary,
        evidence=evidence,
    )
    update_latest_log(
        marker="BLOCKER",
        task_id=task_id,
        status=summary,
        reply_surface_url=active_channel,
        comment_url=comment_url,
        result_sha="none",
        status_artifact_sha="pending",
        linkback_sha=None,
        local_status_sha=None,
        remote_push="pending",
        next_action=next_action,
        owner_required=owner_required,
    )
    stage_runtime_files()
    run_command(
        ["git", "commit", "-m", f"dispatcher: BLOCKER for {task_id} (seq {sequence})"],
        check=True,
    )
    local_sha = get_current_commit_sha()
    push_error = None
    try:
        run_command(["git", "push"], check=True)
    except RuntimeError as exc:
        push_error = str(exc)
        write_mailbox(
            path=FROM_EXECUTOR_PATH,
            sequence=sequence,
            task_id=task_id,
            from_role="Executor Agent — Infrastructure Executor",
            to_role="ChatGPT — Reviewer",
            msg_type="BLOCKER",
            active_channel=active_channel,
            comment_url=comment_url,
            result_sha="none",
            status_artifact_sha="pending",
            linkback_sha=None,
            local_status_sha=local_sha,
            remote_push="failed",
            supersedes_sequence=None,
            owner_action_required=owner_required,
            next_automatic_action=next_action,
            summary=summary,
            evidence=evidence + [f"Local-Status-SHA: {local_sha}", "Remote-Push: failed"],
        )
        update_latest_log(
            marker="BLOCKER",
            task_id=task_id,
            status=summary,
            reply_surface_url=active_channel,
            comment_url=comment_url,
            result_sha="none",
            status_artifact_sha="pending",
            linkback_sha=None,
            local_status_sha=local_sha,
            remote_push="failed",
            next_action=next_action,
            owner_required=owner_required,
        )
    return local_sha, push_error


def finalize_comment_linkback(
    task_id: str,
    sequence: int,
    active_channel: str,
    comment_url: str,
    summary: str,
    evidence: list[str],
    next_action: str,
    owner_required: str,
    msg_type: str,
    result_sha: str,
    status_artifact_sha: str,
) -> LinkbackState:
    """Persist final comment URL and return immutable linkback state."""
    success_evidence = evidence + ["Linkback-State: complete"]
    write_mailbox(
        path=FROM_EXECUTOR_PATH,
        sequence=sequence,
        task_id=task_id,
        from_role="Executor Agent — Infrastructure Executor",
        to_role="ChatGPT — Reviewer",
        msg_type=msg_type,
        active_channel=active_channel,
        comment_url=comment_url,
        result_sha=result_sha,
        status_artifact_sha=status_artifact_sha,
        linkback_sha=None,
        local_status_sha=None,
        remote_push="ok",
        supersedes_sequence=None,
        owner_action_required=owner_required,
        next_automatic_action=next_action,
        summary=summary,
        evidence=success_evidence,
    )
    update_latest_log(
        marker=msg_type,
        task_id=task_id,
        status=summary,
        reply_surface_url=active_channel,
        comment_url=comment_url,
        result_sha=result_sha,
        status_artifact_sha=status_artifact_sha,
        linkback_sha=None,
        local_status_sha=None,
        remote_push="ok",
        next_action=next_action,
        owner_required=owner_required,
    )
    stage_runtime_files()
    final_linkback_sha: Optional[str] = None
    try:
        run_command(
            ["git", "commit", "-m", f"dispatcher: linkback {msg_type} status for {task_id} (seq {sequence})"],
            check=True,
        )
        final_linkback_sha = get_current_commit_sha()
        run_command(["git", "push"], check=True)
    except RuntimeError as exc:
        if final_linkback_sha is None:
            pending_evidence = evidence + [f"Linkback-Pending-Reason: commit failed: {exc}"]
            remote_push = "pending"
            local_status_sha = None
        else:
            pending_evidence = evidence + [
                f"Linkback-Pending-Reason: push failed: {exc}",
                f"Linkback-Local-Status-SHA: {final_linkback_sha}",
            ]
            remote_push = "failed"
            local_status_sha = final_linkback_sha
        write_mailbox(
            path=FROM_EXECUTOR_PATH,
            sequence=sequence,
            task_id=task_id,
            from_role="Executor Agent — Infrastructure Executor",
            to_role="ChatGPT — Reviewer",
            msg_type=msg_type,
            active_channel=active_channel,
            comment_url=comment_url,
            result_sha=result_sha,
            status_artifact_sha=status_artifact_sha,
            linkback_sha=None,
            local_status_sha=local_status_sha,
            remote_push=remote_push,
            supersedes_sequence=None,
            owner_action_required=owner_required,
            next_automatic_action="reconcile final linkback only",
            summary=summary,
            evidence=pending_evidence,
        )
        update_latest_log(
            marker=msg_type,
            task_id=task_id,
            status=summary,
            reply_surface_url=active_channel,
            comment_url=comment_url,
            result_sha=result_sha,
            status_artifact_sha=status_artifact_sha,
            linkback_sha=None,
            local_status_sha=local_status_sha,
            remote_push=remote_push,
            next_action="reconcile final linkback only",
            owner_required=owner_required,
        )
        return LinkbackState(None, True, pending_evidence)
    return LinkbackState(
        final_linkback_sha,
        False,
        success_evidence + [f"Linkback-Artifact-SHA: {final_linkback_sha}"],
    )


def reconcile_pending_linkback() -> Optional[LinkbackState]:
    """Retry only the final linkback persistence from durable mailbox state."""
    state = parse_mailbox(FROM_EXECUTOR_PATH)
    if not state:
        return None
    if state.get("Comment-URL") in {"", "pending", "none"}:
        return None
    normalized_evidence = []
    for line in state.get("Evidence", "").splitlines():
        cleaned = line.strip()
        if cleaned.startswith("- "):
            normalized_evidence.append(cleaned[2:])
    if has_linkback_completion_marker(normalized_evidence):
        return None

    evidence_lines = []
    raw_evidence = state.get("Evidence", "")
    for line in raw_evidence.splitlines():
        cleaned = line.strip()
        if cleaned.startswith("- "):
            evidence_lines.append(cleaned[2:])

    return finalize_comment_linkback(
        task_id=state.get("Task-ID", "unknown"),
        sequence=int(state.get("Sequence", "0") or "0"),
        active_channel=state.get("Active-Channel", ""),
        comment_url=state.get("Comment-URL", "none"),
        summary=state.get("Summary", ""),
        evidence=evidence_lines,
        next_action=state.get("Next-Automatic-Action", "review linkback persistence"),
        owner_required=state.get("Owner-Action-Required", "none"),
        msg_type=state.get("Type", "COMPLETE"),
        result_sha=state.get("Result-SHA", "none"),
        status_artifact_sha=state.get("Status-Artifact-SHA", "pending"),
    )


def parse_adapter_result(stdout: str) -> AdapterResult:
    """Parse structured JSON emitted by the external runner adapter."""
    try:
        payload = json.loads(stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Adapter output is not valid JSON: {exc}")

    if not isinstance(payload, dict):
        raise RuntimeError("Adapter output must be a JSON object")

    status = payload.get("status")
    summary = payload.get("summary")
    result_sha = payload.get("result_sha", "none")
    evidence = payload.get("evidence", [])

    if status not in {"COMPLETE", "BLOCKER"}:
        raise RuntimeError("Adapter output field 'status' must be COMPLETE or BLOCKER")
    if not isinstance(summary, str) or not summary.strip():
        raise RuntimeError("Adapter output field 'summary' must be a non-empty string")
    if result_sha is None:
        result_sha = "none"
    if not isinstance(result_sha, str):
        raise RuntimeError("Adapter output field 'result_sha' must be a string or null")
    normalized_result_sha = result_sha.strip() or "none"
    if normalized_result_sha != "none" and not re.fullmatch(r"[0-9a-f]{40}", normalized_result_sha):
        raise RuntimeError(
            "Adapter output field 'result_sha' must be 'none' or a full 40-character hexadecimal SHA"
        )
    if not isinstance(evidence, list) or any(not isinstance(item, str) for item in evidence):
        raise RuntimeError("Adapter output field 'evidence' must be a list of strings")

    return AdapterResult(
        status=status,
        summary=summary.strip(),
        result_sha=normalized_result_sha,
        evidence=evidence,
    )


def post_blocker_and_exit(
    task: dict,
    to_seq: int,
    error_msg: str,
    active_channel: str,
    recoverable: bool = False,
) -> None:
    """Post a BLOCKER comment and write FROM_EXECUTOR.md."""
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
    comment_error = None
    if active_channel:
        try:
            comment_url = post_issue_comment(active_channel, blocker_comment)
        except RuntimeError as exc:
            comment_error = str(exc)

    summary = f"Pre-mutation validation failed: {error_msg}"
    evidence = [f"Error: {error_msg}"]
    if comment_error:
        evidence.append(f"Comment publish failed: {comment_error}")

    try:
        local_sha, push_error = persist_blocker_locally(
            task_id=task_id,
            sequence=to_seq,
            active_channel=active_channel,
            comment_url=comment_url,
            summary=summary,
            evidence=evidence,
            next_action="wait for corrected TO_EXECUTOR",
            owner_required="fix validation error",
        )
        if push_error:
            print(
                f"  BLOCKER persisted locally at {local_sha}, but push failed: {push_error}",
                file=sys.stderr,
            )
        else:
            print(f"  BLOCKER posted and pushed at {local_sha}")
    except RuntimeError as exc:
        print(f"  BLOCKER persistence failed locally: {exc}", file=sys.stderr)

    if not recoverable:
        sys.exit(1)


def build_comment_body(
    msg_type: str,
    task_id: str,
    sequence: int,
    summary_text: str,
    evidence: list[str],
    next_auto: str,
    result_sha: str,
    status_artifact_sha: str,
) -> str:
    """Build a durable GitHub comment body including both SHA fields."""
    lines = [
        msg_type,
        "",
        f"Task-ID: {task_id}",
        f"Sequence: {sequence}",
        "",
        "## Summary",
        "",
        summary_text,
        "",
        "## Evidence",
        "",
    ]
    for item in evidence:
        lines.append(f"- {item}")
    lines.append(f"- Result-SHA: {result_sha}")
    lines.append(f"- Status-Artifact-SHA: {status_artifact_sha}")
    lines.extend(["", "## Next Automatic Action", "", next_auto])
    return "\n".join(lines)


def commit_and_publish(
    task: dict,
    to_seq: int,
    msg_type: str,
    summary_text: str,
    evidence: list[str],
    active_channel: str,
    next_auto: str,
    owner_required: str,
    result_sha_hint: str,
) -> DispatchResult:
    """Persist runtime status first, then publish a comment with durable SHA fields."""
    task_id = task.get("Task-ID", "unknown")

    try:
        result_sha, status_artifact_sha = persist_runtime_status(
            task_id=task_id,
            sequence=to_seq,
            active_channel=active_channel,
            comment_url="pending",
            summary=summary_text,
            evidence=evidence,
            next_action=next_auto,
            owner_required=owner_required,
            msg_type=msg_type,
            result_sha_hint=result_sha_hint,
        )
    except RuntimeError as exc:
        error_msg = f"Git commit/push failed before publication: {exc}"
        print(f"  BLOCKER: {error_msg}", file=sys.stderr)
        post_blocker_and_exit(task, to_seq, error_msg, active_channel, recoverable=False)
        raise

    enriched_comment = build_comment_body(
        msg_type=msg_type,
        task_id=task_id,
        sequence=to_seq,
        summary_text=summary_text,
        evidence=evidence,
        next_auto=next_auto,
        result_sha=result_sha_hint,
        status_artifact_sha=status_artifact_sha,
    )

    try:
        comment_url = post_issue_comment(active_channel, enriched_comment) if active_channel else "none"
    except RuntimeError as exc:
        error_msg = f"Could not post comment after durable publication: {exc}"
        print(f"  BLOCKER: {error_msg}", file=sys.stderr)
        post_blocker_and_exit(task, to_seq, error_msg, active_channel, recoverable=False)
        raise

    linkback_state = finalize_comment_linkback(
        task_id=task_id,
        sequence=to_seq,
        active_channel=active_channel,
        comment_url=comment_url,
        summary=summary_text,
        evidence=evidence + [
            f"Result-SHA: {result_sha_hint}",
            f"Status-Artifact-SHA: {status_artifact_sha}",
        ],
        next_action=next_auto,
        owner_required=owner_required,
        msg_type=msg_type,
        result_sha=result_sha_hint,
        status_artifact_sha=status_artifact_sha,
    )
    if not linkback_state.pending and linkback_state.linkback_artifact_sha and active_channel:
        post_issue_comment(
            active_channel,
            build_linkback_followup(linkback_state.linkback_artifact_sha),
        )

    return DispatchResult(
        result_sha=result_sha_hint,
        status_artifact_sha=status_artifact_sha,
        comment_url=comment_url,
        linkback_artifact_sha=linkback_state.linkback_artifact_sha,
        summary_text=summary_text,
        evidence=linkback_state.evidence,
    )


# ---------------------------------------------------------------------------
# Notifier Mode
# ---------------------------------------------------------------------------


def notifier_cycle() -> bool:
    """
    One notifier cycle: check TO_EXECUTOR, post ACK if new sequence.
    """
    if not TO_EXECUTOR_PATH.exists():
        return False

    current_from_seq = read_current_sequence(FROM_EXECUTOR_PATH)
    to_seq = read_current_sequence(TO_EXECUTOR_PATH)

    task = parse_mailbox(TO_EXECUTOR_PATH)
    supersedes_str = task.get("Supersedes-Sequence")
    if supersedes_str is not None:
        try:
            if to_seq <= int(supersedes_str):
                return False
        except ValueError:
            pass

    if to_seq <= current_from_seq:
        return False

    print(f"[{timestamp_iso()}] New sequence detected: TO_EXECUTOR sequence {to_seq}")

    task_id = task.get("Task-ID", "unknown")
    active_channel = task.get("Active-Channel", "")
    msg_type = task.get("Type", "HANDOFF")
    next_action = task.get("Next-Automatic-Action", "")
    summary = task.get("Summary", "")

    print(f"  Task-ID: {task_id}")
    print(f"  Type: {msg_type}")

    try:
        validate_before_mutation(task, to_seq)
    except RuntimeError as e:
        post_blocker_and_exit(task, to_seq, str(e), active_channel, recoverable=True)
        return True

    if active_channel:
        try:
            issue_body = read_active_issue_body(active_channel)
            print(f"  Read issue body ({len(issue_body)} chars)")
        except RuntimeError as e:
            post_blocker_and_exit(
                task, to_seq, f"Could not read active issue: {e}", active_channel,
                recoverable=True,
            )
            return True

    ack_summary = f"Handoff received. Waiting for runner mode to execute: {summary}"
    evidence_items = [
        f"Task-ID: {task_id}",
        f"Sequence: {to_seq}",
        f"Type: {msg_type}",
        f"Active channel validated: {active_channel}",
        "Runner command source: --command CLI argument only",
    ]

    commit_and_publish(
        task=task,
        to_seq=to_seq,
        msg_type="ACK",
        summary_text=ack_summary,
        evidence=evidence_items,
        active_channel=active_channel,
        next_auto=next_action,
        owner_required="none",
        result_sha_hint="none",
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

    if not TO_EXECUTOR_PATH.exists():
        print("No TO_EXECUTOR.md found. Nothing to run.")
        return

    task = parse_mailbox(TO_EXECUTOR_PATH)
    to_seq = read_current_sequence(TO_EXECUTOR_PATH)
    current_from_seq = read_current_sequence(FROM_EXECUTOR_PATH)
    current_from_type = read_current_type(FROM_EXECUTOR_PATH)

    if to_seq < current_from_seq:
        print("No new sequence to execute. Older sequence already processed.")
        return
    elif to_seq == current_from_seq and current_from_type != "ACK":
        print("No new sequence to execute. Same sequence may run only from ACK state.")
        return

    task_id = task.get("Task-ID", "unknown")
    active_channel = task.get("Active-Channel", "")
    next_action = task.get("Next-Automatic-Action", "")
    summary = task.get("Summary", "")

    print(f"  Task-ID: {task_id}")
    print(f"  Sequence: {to_seq}")
    print(f"  Current state: {current_from_type}")

    try:
        validate_before_mutation(task, to_seq)
    except RuntimeError as e:
        post_blocker_and_exit(task, to_seq, str(e), active_channel, recoverable=False)
        return

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

    try:
        cmd_parts = shlex.split(command)
    except ValueError as e:
        post_blocker_and_exit(
            task, to_seq, f"Invalid command syntax: {e}", active_channel,
            recoverable=False,
        )
        return

    print(f"  Executing: {cmd_parts}")
    exit_code = -1
    adapter_result = AdapterResult(
        status="BLOCKER",
        summary="Adapter result not available",
        result_sha="none",
        evidence=[],
    )
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
        msg_type = "BLOCKER"
        evidence = [f"Command timed out after {timeout}s: {e}"]
        summary_text = f"Runner command timed out: {command}"
        next_auto = "review and retry with longer timeout"
        owner_required = "review timeout"
    else:
        if exit_code == 0:
            try:
                adapter_result = parse_adapter_result(stdout)
                if adapter_result.status == "COMPLETE":
                    post_run_dirty = check_dirty_tree_runtime()
                    if post_run_dirty:
                        raise RuntimeError(
                            "Post-run dirty tree outside runtime-owned paths:\n"
                            + "\n".join(post_run_dirty)
                        )
                msg_type = adapter_result.status
                evidence = [
                    f"Command: {command}",
                    f"Exit code: {exit_code}",
                    f"Adapter-Result-SHA: {adapter_result.result_sha}",
                ] + adapter_result.evidence
                if stderr:
                    evidence.append(f"Stderr: {stderr[:500]}")
                summary_text = adapter_result.summary
                next_auto = (
                    next_action if msg_type == "COMPLETE" else "review blocker and retry"
                )
                owner_required = "none" if msg_type == "COMPLETE" else "review blocker"
            except RuntimeError as exc:
                msg_type = "BLOCKER"
                evidence = [
                    f"Command: {command}",
                    f"Exit code: {exit_code}",
                    f"Runner validation error: {exc}",
                ]
                if stderr:
                    evidence.append(f"Stderr: {stderr[:500]}")
                summary_text = f"Runner adapter contract failed: {command}"
                next_auto = "review adapter output and retry"
                owner_required = "review adapter output"
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

    evidence.append("Runner command source: --command CLI argument only")
    evidence.append(f"Task summary: {summary}")

    commit_and_publish(
        task=task,
        to_seq=to_seq,
        msg_type=msg_type,
        summary_text=summary_text,
        evidence=evidence,
        active_channel=active_channel,
        next_auto=next_auto,
        owner_required=owner_required,
        result_sha_hint=adapter_result.result_sha if msg_type == "COMPLETE" else "none",
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="Automatic Mailbox Dispatcher for Project Execution OS"
    )
    subparsers = parser.add_subparsers(dest="mode", help="Dispatcher mode")

    notifier_parser = subparsers.add_parser(
        "notifier", help="Detect new sequences, post ACK, wait for runner"
    )
    notifier_parser.add_argument(
        "--poll-interval",
        type=int,
        default=DEFAULT_POLL_INTERVAL,
        help=f"Polling interval in seconds (default: {DEFAULT_POLL_INTERVAL})",
    )

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

    subparsers.add_parser(
        "reconcile-linkback",
        help="Retry only the final linkback persistence without rerunning the adapter",
    )

    args = parser.parse_args()

    if args.mode == "notifier":
        run_notifier(args.poll_interval)
    elif args.mode == "runner":
        run_runner(args.command, args.timeout)
    elif args.mode == "reconcile-linkback":
        result = reconcile_pending_linkback()
        if result is None:
            print("No pending linkback reconciliation required.")
        elif result.pending:
            print("Linkback reconciliation still pending.")
            sys.exit(1)
        else:
            print(f"Linkback reconciliation complete: {result.linkback_artifact_sha}")
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
