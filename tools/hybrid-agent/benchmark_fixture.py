from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from hybrid_agent import build_input_payload, compression_ratio, json_size_metrics


HERE = Path(__file__).resolve().parent
DEFAULT_LOG_FIXTURE = HERE / "fixtures" / "synthetic_repetitive_log.txt"
DEFAULT_LOCAL_FIXTURE = HERE / "fixtures" / "mock_local_payload.json"


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Measure local compression savings without any paid cloud call.")
    parser.add_argument("--task", default="Summarize repeated build failures and highlight likely files to inspect.")
    parser.add_argument("--log-fixture", type=Path, default=DEFAULT_LOG_FIXTURE)
    parser.add_argument("--local-payload", type=Path, default=DEFAULT_LOCAL_FIXTURE)
    args = parser.parse_args()

    started = time.perf_counter()
    bounded_payload = build_input_payload(
        task_text=args.task,
        log_paths=[args.log_fixture.resolve()],
        file_paths=[],
        selected_route="tools/hybrid-agent/benchmark-fixture",
    )
    local_payload = json.loads(args.local_payload.read_text(encoding="utf-8"))
    elapsed_ms = (time.perf_counter() - started) * 1000.0

    raw_metrics = json_size_metrics(bounded_payload)
    compact_metrics = json_size_metrics(local_payload)
    result = {
        "input_size_bytes": raw_metrics["bytes"],
        "output_size_bytes": compact_metrics["bytes"],
        "input_size_chars": raw_metrics["chars"],
        "output_size_chars": compact_metrics["chars"],
        "compression_ratio": compression_ratio(raw_metrics["bytes"], compact_metrics["bytes"]),
        "latency_ms_local_fixture": round(elapsed_ms, 3),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
