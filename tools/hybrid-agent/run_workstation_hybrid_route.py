from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from hybrid_agent import DEFAULT_LOG_PATH
from run_hybrid_agent import parse_paths
from workstation_route import DEFAULT_TIMEOUT_SECONDS, DEFAULT_WORKSTATION_ROUTE, run_workstation_route


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
    parser.add_argument("--selected-route", default=DEFAULT_WORKSTATION_ROUTE)
    parser.add_argument("--timeout-seconds", type=float, default=DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument("--debug-full-evidence", action="store_true")
    args = parser.parse_args()

    result = run_workstation_route(
        executor=args.executor,
        mode=args.mode,
        task_text=args.task,
        log_paths=parse_paths(args.log_path),
        file_paths=parse_paths(args.file_path),
        timeout_seconds=args.timeout_seconds,
        log_path=args.runtime_log.resolve(),
        selected_route=args.selected_route,
        include_full_evidence=args.debug_full_evidence,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
