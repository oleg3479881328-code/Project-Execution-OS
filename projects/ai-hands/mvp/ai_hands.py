#!/usr/bin/env python3
"""AI Hands MVP: bounded local-model file edit through Ollama."""

from __future__ import annotations

import argparse
import difflib
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


class ExecutionError(RuntimeError):
    pass


@dataclass(frozen=True)
class Task:
    workspace: Path
    model: str
    instruction: str
    target_file: str
    expected_branch: str
    validation_command: list[str]
    ollama_url: str = "http://127.0.0.1:11434"


def load_task(path: Path) -> Task:
    raw = json.loads(path.read_text(encoding="utf-8"))
    command = raw.get("validation_command")
    if not isinstance(command, list) or not command or not all(isinstance(x, str) for x in command):
        raise ExecutionError("validation_command must be a non-empty string array")
    expected_branch = str(raw.get("expected_branch", "")).strip()
    if not expected_branch:
        raise ExecutionError("expected_branch is required")
    return Task(
        workspace=Path(raw["workspace"]).expanduser().resolve(),
        model=str(raw["model"]),
        instruction=str(raw["instruction"]),
        target_file=str(raw["target_file"]),
        expected_branch=expected_branch,
        validation_command=command,
        ollama_url=str(raw.get("ollama_url", "http://127.0.0.1:11434")).rstrip("/"),
    )


def resolve_target(task: Task) -> Path:
    if not task.workspace.is_dir():
        raise ExecutionError(f"workspace does not exist: {task.workspace}")
    target = (task.workspace / task.target_file).resolve()
    try:
        target.relative_to(task.workspace)
    except ValueError as exc:
        raise ExecutionError("target_file escapes approved workspace") from exc
    if not target.is_file():
        raise ExecutionError(f"target file does not exist: {target}")
    return target


def git_output(workspace: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=workspace, text=True, capture_output=True,
        timeout=20, shell=False, check=False,
    )
    if result.returncode != 0:
        raise ExecutionError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


def verify_isolated_branch(task: Task) -> None:
    if git_output(task.workspace, "rev-parse", "--is-inside-work-tree") != "true":
        raise ExecutionError("workspace is not a Git worktree")
    branch = git_output(task.workspace, "branch", "--show-current")
    if not branch:
        raise ExecutionError("detached HEAD is not allowed")
    if branch != task.expected_branch:
        raise ExecutionError(f"current branch {branch!r} does not match expected_branch {task.expected_branch!r}")
    if branch.lower() in {"main", "master", "trunk"}:
        raise ExecutionError("refusing to write on a default-style branch")


def build_prompt(task: Task, current_content: str) -> str:
    return f"""You are a bounded file-edit executor. You do not choose architecture.
Follow the controller instruction exactly. Do not propose commands or other files.
Return JSON only with this exact schema:
{{"target_file": {json.dumps(task.target_file)}, "new_content": "complete replacement content", "summary": "one sentence"}}

CONTROLLER INSTRUCTION:
{task.instruction}

CURRENT FILE CONTENT:
---
{current_content}
---
"""


def parse_ollama_proposal(envelope: dict[str, Any]) -> dict[str, Any]:
    parse_errors: list[str] = []
    for field in ("response", "thinking"):
        candidate = envelope.get(field)
        if not isinstance(candidate, str) or not candidate.strip():
            continue
        try:
            proposal = json.loads(candidate)
        except json.JSONDecodeError as exc:
            parse_errors.append(f"{field}: {exc.msg}")
            continue
        if isinstance(proposal, dict):
            return proposal
        parse_errors.append(f"{field}: JSON value is not an object")
    detail = "; ".join(parse_errors)
    raise ExecutionError("model did not return valid proposal JSON" + (f" ({detail})" if detail else ""))


def call_ollama(task: Task, prompt: str) -> dict[str, Any]:
    payload = json.dumps({
        "model": task.model,
        "prompt": prompt,
        "stream": False,
        "format": "json",
        "options": {"temperature": 0},
    }).encode("utf-8")
    request = urllib.request.Request(
        f"{task.ollama_url}/api/generate", data=payload,
        headers={"Content-Type": "application/json"}, method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            envelope = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise ExecutionError(f"Ollama request failed: {exc}") from exc
    if not isinstance(envelope, dict):
        raise ExecutionError("Ollama response envelope must be a JSON object")
    return parse_ollama_proposal(envelope)


def validate_proposal(task: Task, proposal: dict[str, Any]) -> tuple[str, str]:
    if proposal.get("target_file") != task.target_file:
        raise ExecutionError("model attempted to change an unapproved file")
    new_content = proposal.get("new_content")
    summary = proposal.get("summary", "")
    if not isinstance(new_content, str):
        raise ExecutionError("new_content must be a string")
    if not isinstance(summary, str):
        raise ExecutionError("summary must be a string")
    return new_content, summary


def validate_validation_command(task: Task) -> None:
    command = task.validation_command
    executable = Path(command[0]).name.lower()
    allowed_executables = {"powershell", "powershell.exe", "pwsh", "pwsh.exe"}
    if executable not in allowed_executables:
        raise ExecutionError("validation executable is not allowlisted")
    if len(command) != 5:
        raise ExecutionError("validation command must use the approved five-argument PowerShell form")
    if command[1:4] != ["-ExecutionPolicy", "Bypass", "-File"]:
        raise ExecutionError("validation command arguments are not allowlisted")
    script = (task.workspace / command[4]).resolve()
    try:
        script.relative_to(task.workspace)
    except ValueError as exc:
        raise ExecutionError("validation script escapes approved workspace") from exc
    if script.name.lower() != "validate.ps1" or not script.is_file():
        raise ExecutionError("only an existing workspace-local validate.ps1 is allowlisted")


def run_validation(task: Task) -> subprocess.CompletedProcess[str]:
    validate_validation_command(task)
    return subprocess.run(
        task.validation_command, cwd=task.workspace, text=True, capture_output=True,
        timeout=120, shell=False, check=False,
    )


def set_next_action(report: dict[str, Any]) -> None:
    status = report["status"]
    actions = {
        "COMPLETE": "Controller should review the diff and validation evidence, then decide whether to accept or expand scope.",
        "DRY_RUN_OK": "Controller should review the proposed diff and authorize a non-dry run if acceptable.",
        "VALIDATION_FAILED_ROLLED_BACK": "Controller should inspect validation output and revise the task or implementation before retrying.",
        "INTERRUPTED_ROLLED_BACK": "Operator should confirm workspace state, then retry only after controller approval.",
        "FAILED": "Controller should inspect the error, correct the task or adapter, and issue a new bounded run instruction.",
    }
    report["next_recommended_action"] = actions.get(status, actions["FAILED"])


def execute(task: Task, dry_run: bool) -> tuple[dict[str, Any], int]:
    report: dict[str, Any] = {"status": "FAILED"}
    original: str | None = None
    target: Path | None = None
    wrote = False
    exit_code = 1
    try:
        verify_isolated_branch(task)
        target = resolve_target(task)
        original = target.read_text(encoding="utf-8")
        proposal = call_ollama(task, build_prompt(task, original))
        new_content, model_summary = validate_proposal(task, proposal)
        diff = "".join(difflib.unified_diff(
            original.splitlines(keepends=True), new_content.splitlines(keepends=True),
            fromfile=f"a/{task.target_file}", tofile=f"b/{task.target_file}",
        ))
        report.update({"model": task.model, "model_summary": model_summary, "diff": diff})
        if dry_run:
            report["status"] = "DRY_RUN_OK"
            exit_code = 0
        else:
            validate_validation_command(task)
            target.write_text(new_content, encoding="utf-8")
            wrote = True
            validation = run_validation(task)
            report["validation"] = {
                "command": task.validation_command,
                "returncode": validation.returncode,
                "stdout": validation.stdout,
                "stderr": validation.stderr,
            }
            if validation.returncode != 0:
                target.write_text(original, encoding="utf-8")
                wrote = False
                report["status"] = "VALIDATION_FAILED_ROLLED_BACK"
            else:
                report["status"] = "COMPLETE"
                exit_code = 0
    except KeyboardInterrupt:
        report["status"] = "INTERRUPTED_ROLLED_BACK"
        report["error"] = "execution interrupted by operator"
    except Exception as exc:
        report["error"] = str(exc)
    finally:
        if wrote and report["status"] != "COMPLETE" and original is not None and target is not None:
            try:
                target.write_text(original, encoding="utf-8")
            except OSError as exc:
                report["rollback_error"] = str(exc)
        set_next_action(report)
    return report, exit_code


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one bounded AI Hands Ollama task")
    parser.add_argument("task", type=Path, help="Path to task JSON")
    parser.add_argument("--dry-run", action="store_true", help="Do not write or validate")
    args = parser.parse_args()
    try:
        task = load_task(args.task.resolve())
        report, exit_code = execute(task, args.dry_run)
    except BaseException as exc:
        report = {"status": "FAILED", "error": str(exc)}
        set_next_action(report)
        exit_code = 1
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
