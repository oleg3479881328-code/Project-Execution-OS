from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from hybrid_agent import DEFAULT_LOG_PATH, DEFAULT_SELECTED_ROUTE, EndpointConfig, run_hybrid_agent


def parse_paths(raw_paths: list[str] | None) -> list[Path]:
    return [Path(item).resolve() for item in (raw_paths or [])]


def env_or_value(value: str | None, env_name: str, default: str | None = None) -> str | None:
    return value or os.environ.get(env_name) or default


def build_endpoint_config(
    *,
    provider: str,
    endpoint: str | None,
    model: str | None,
    api_key: str | None,
    timeout: float,
) -> EndpointConfig | None:
    if not endpoint or not model:
        return None
    return EndpointConfig(
        provider=provider,
        endpoint=endpoint,
        model=model,
        api_key=api_key or "unused",
        timeout_seconds=timeout,
    )


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Run the hybrid local-model preprocessing prototype.")
    parser.add_argument("--task", required=True, help="Task text for the agent run.")
    parser.add_argument(
        "--mode",
        choices=["local-only", "preprocess-then-cloud", "cloud-only"],
        default="preprocess-then-cloud",
    )
    parser.add_argument("--log-path", action="append", default=[], help="Repeatable path to a log file.")
    parser.add_argument("--file-path", action="append", default=[], help="Repeatable path to a source file.")
    parser.add_argument("--task-id")
    parser.add_argument("--project-id", default="project-execution-os")
    parser.add_argument("--selected-route", default=DEFAULT_SELECTED_ROUTE)
    parser.add_argument("--runtime-log", type=Path, default=DEFAULT_LOG_PATH)
    parser.add_argument("--timeout-seconds", type=float, default=60.0)
    parser.add_argument(
        "--debug-full-evidence",
        action="store_true",
        help="Include raw bounded evidence in the cloud prompt even when local preprocessing succeeds.",
    )

    parser.add_argument("--local-endpoint")
    parser.add_argument("--local-model")
    parser.add_argument("--local-api-key")
    parser.add_argument("--local-provider", default="local-openai-compatible")

    parser.add_argument("--cloud-endpoint")
    parser.add_argument("--cloud-model")
    parser.add_argument("--cloud-api-key")
    parser.add_argument("--cloud-provider", default="cloud-openai-compatible")
    args = parser.parse_args()

    local_config = build_endpoint_config(
        provider=args.local_provider,
        endpoint=env_or_value(args.local_endpoint, "HYBRID_AGENT_LOCAL_ENDPOINT"),
        model=env_or_value(args.local_model, "HYBRID_AGENT_LOCAL_MODEL"),
        api_key=env_or_value(args.local_api_key, "HYBRID_AGENT_LOCAL_API_KEY", "ollama"),
        timeout=args.timeout_seconds,
    )
    cloud_config = build_endpoint_config(
        provider=args.cloud_provider,
        endpoint=env_or_value(args.cloud_endpoint, "HYBRID_AGENT_CLOUD_ENDPOINT"),
        model=env_or_value(args.cloud_model, "HYBRID_AGENT_CLOUD_MODEL"),
        api_key=env_or_value(args.cloud_api_key, "HYBRID_AGENT_CLOUD_API_KEY"),
        timeout=args.timeout_seconds,
    )

    result = run_hybrid_agent(
        task_text=args.task,
        mode=args.mode,
        log_paths=parse_paths(args.log_path),
        file_paths=parse_paths(args.file_path),
        local_config=local_config,
        cloud_config=cloud_config,
        log_path=args.runtime_log.resolve(),
        selected_route=args.selected_route,
        task_id=args.task_id,
        project_id=args.project_id,
        include_full_evidence=args.debug_full_evidence,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
