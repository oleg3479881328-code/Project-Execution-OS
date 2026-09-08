from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from hybrid_agent import DEFAULT_LOG_PATH
from workstation_route import DEFAULT_TIMEOUT_SECONDS, DEFAULT_WORKSTATION_ROUTE, run_workstation_route


DEFAULT_REPO_ROOT = Path(__file__).resolve().parents[2]


def resolve_cli_path(raw_path: str, base_dir: Path) -> Path:
    path = Path(raw_path)
    return path.resolve() if path.is_absolute() else (base_dir / path).resolve()


def parse_paths(raw_paths: list[str] | None, base_dir: Path) -> list[Path]:
    return [resolve_cli_path(item, base_dir) for item in (raw_paths or [])]


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Run the workstation hybrid route for Codex or DeepSeek tasks.")
    parser.add_argument("--executor", choices=["codex", "deepseek"], default="codex")
    parser.add_argument(
        "--mode",
        choices=["auto", "cloud-only", "local-only", "preprocess-then-cloud"],
        default="auto",
    )
    parser.add_argument("--task", required=True)
    parser.add_argument("--log-path", action="append", default=[], help="Repeatable path to a bounded log input.")
    parser.add_argument("--file-path", action="append", default=[], help="Repeatable path to a bounded file input.")
    parser.add_argument("--runtime-log", type=Path, default=DEFAULT_LOG_PATH)
    parser.add_argument("--repo-root", type=Path, default=DEFAULT_REPO_ROOT)
    parser.add_argument("--selected-route", default=DEFAULT_WORKSTATION_ROUTE)
    parser.add_argument("--timeout-seconds", type=float, default=DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument("--local-model", default=None, help="Override local Ollama model (e.g. qwen3:4b)")
    parser.add_argument("--debug-full-evidence", action="store_true")
    parser.add_argument("--no-launch-executor", action="store_true")
    args = parser.parse_args()
    repo_root = args.repo_root.resolve()

    result = run_workstation_route(
        executor=args.executor,
        mode=args.mode,
        task_text=args.task,
        log_paths=parse_paths(args.log_path, repo_root),
        file_paths=parse_paths(args.file_path, repo_root),
        timeout_seconds=args.timeout_seconds,
        log_path=resolve_cli_path(str(args.runtime_log), repo_root),
        selected_route=args.selected_route,
        include_full_evidence=args.debug_full_evidence,
        launch_executor=not args.no_launch_executor,
        repo_root=repo_root,
        local_model=args.local_model,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
