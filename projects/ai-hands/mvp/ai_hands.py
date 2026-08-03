#!/usr/bin/env python3
"""AI Hands MVP: bounded local-model file edit through Ollama.

The controller supplies an exact task packet. The local model may propose one
full-file replacement in JSON. This adapter validates the proposal, applies it
inside the approved workspace only, runs one allowlisted validation command,
and prints a machine-readable execution report.
"""

from __future__ import annotations

import argparse
import difflib
import json
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
    validation_command: list[str]
    ollama_url: str = "http://127.0.0.1:11434"


def load_task(path: Path) -> Task:
    raw = json.loads(path.read_text(encoding="utf-8"))
    command = raw.get("validation_command")
    if not isinstance(command, list) or not command or not all(isinstance(x, str) for x in command):
        raise ExecutionError("validation_command must be a non-empty string array")
    return Task(
        workspace=Path(raw["workspace"]).expanduser().resolve(),
        model=str(raw["model"]),
        instruction=str(raw["instruction"]),
        target_file=str(raw["target_file"]),
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
    """Parse structured model output from supported Ollama envelope fields.

    Most models place final output in ``response``. Some reasoning models emit
    the requested JSON in ``thinking`` while leaving ``response`` empty. We
    accept the first non-empty valid JSON object from those known fields only.
    """
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
    suffix = f" ({detail})" if detail else ""
    raise ExecutionError(f"model did not return valid proposal JSON{suffix}")


def call_ollama(task: Task, prompt: str) -> dict[str, Any]:
    payload = json.dumps({
        "model": task.model,
        "prompt": prompt,
        "stream": False,
        "format": "json",
        "options": {"temperature": 0},
    }).encode("utf-8")
    request = urllib.request.Request(
        f"{task.ollama_url}/api/generate",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
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


def run_validation(task: Task) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        task.validation_command,
        cwd=task.workspace,
        text=True,
        capture_output=True,
        timeout=120,
        shell=False,
        check=False,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one bounded AI Hands Ollama task")
    parser.add_argument("task", type=Path, help="Path to task JSON")
    parser.add_argument("--dry-run", action="store_true", help="Do not write or validate")
    args = parser.parse_args()

    report: dict[str, Any] = {"status": "FAILED"}
    original: str | None = None
    target: Path | None = None
    try:
        task = load_task(args.task.resolve())
        target = resolve_target(task)
        original = target.read_text(encoding="utf-8")
        proposal = call_ollama(task, build_prompt(task, original))
        new_content, model_summary = validate_proposal(task, proposal)
        diff = "".join(difflib.unified_diff(
            original.splitlines(keepends=True),
            new_content.splitlines(keepends=True),
            fromfile=f"a/{task.target_file}",
            tofile=f"b/{task.target_file}",
        ))
        report.update({"model": task.model, "model_summary": model_summary, "diff": diff})
        if args.dry_run:
            report["status"] = "DRY_RUN_OK"
        else:
            target.write_text(new_content, encoding="utf-8")
            validation = run_validation(task)
            report["validation"] = {
                "command": task.validation_command,
                "returncode": validation.returncode,
                "stdout": validation.stdout,
                "stderr": validation.stderr,
            }
            if validation.returncode != 0:
                target.write_text(original, encoding="utf-8")
                report["status"] = "VALIDATION_FAILED_ROLLED_BACK"
            else:
                report["status"] = "COMPLETE"
    except Exception as exc:  # final safety boundary for CLI report
        if original is not None and target is not None and target.exists():
            try:
                target.write_text(original, encoding="utf-8")
            except OSError:
                pass
        report["error"] = str(exc)

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] in {"COMPLETE", "DRY_RUN_OK"} else 1


if __name__ == "__main__":
    sys.exit(main())
