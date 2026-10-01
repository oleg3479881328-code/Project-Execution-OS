"""Model comparison script for Issue #35.

Tests each installed Ollama model on Workload B, C, D.
Records: success, invalid-output, hallucinated-path, compression, latency.

Supports checkpointing: saves progress after each model so it can resume.
"""
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, '.')
from hybrid_agent import (
    EndpointConfig,
    build_input_payload,
    run_local_stage,
    DEFAULT_LOG_PATH,
    DEFAULT_SELECTED_ROUTE,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
FIXTURES = REPO_ROOT / "tools" / "hybrid-agent" / "fixtures"
LOG_PATH = REPO_ROOT / "logs" / "api-runtime" / "model-compare.jsonl"
CHECKPOINT_PATH = REPO_ROOT / "model_comparison_checkpoint.json"

MODELS = [
    "llama3.2:3b",
    "qwen3:4b",
    "qwen2.5-coder:7b",
    "deepseek-coder:6.7b",
]

WORKLOADS = {
    "B": {
        "name": "Workload B (medium log)",
        "log_paths": [FIXTURES / "synthetic_repetitive_log.txt"],
        "file_paths": [],
        "reps": 3,
    },
    "C": {
        "name": "Workload C (large log)",
        "log_paths": [FIXTURES / "large_repetitive_log.txt"],
        "file_paths": [],
        "reps": 3,
    },
    "D": {
        "name": "Workload D (real evidence)",
        "log_paths": [
            REPO_ROOT / "tools" / "hybrid-agent" / "hybrid_agent.py",
        ],
        "file_paths": [
            REPO_ROOT / "tools" / "hybrid-agent" / "workstation_route.py",
        ],
        "reps": 1,
    },
}

LOCAL_ENDPOINT = "http://localhost:11434/v1"
LOCAL_API_KEY = "ollama"
TASK_TEXT = "Compress this evidence into a compact structured payload preserving source paths and line ranges."


def load_checkpoint() -> dict:
    if CHECKPOINT_PATH.exists():
        try:
            return json.loads(CHECKPOINT_PATH.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    return {"completed_models": [], "results": {}}


def save_checkpoint(data: dict) -> None:
    CHECKPOINT_PATH.write_text(
        json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def test_model(model: str, workload_key: str) -> list[dict]:
    wl = WORKLOADS[workload_key]
    results = []
    for rep in range(wl["reps"]):
        # qwen3:4b is very slow, needs more time
        timeout = 600 if model == "qwen3:4b" else 120
        config = EndpointConfig(
            provider="local-ollama",
            endpoint=LOCAL_ENDPOINT,
            model=model,
            api_key=LOCAL_API_KEY,
            timeout_seconds=timeout,
        )
        input_payload = build_input_payload(
            task_text=TASK_TEXT,
            log_paths=wl["log_paths"],
            file_paths=wl["file_paths"],
            selected_route=DEFAULT_SELECTED_ROUTE,
        )
        started = time.perf_counter()
        result = run_local_stage(
            config=config,
            input_payload=input_payload,
            task_id=f"model-compare-{model}-{workload_key}-{rep}",
            project_id="project-execution-os",
            selected_route=DEFAULT_SELECTED_ROUTE,
            log_path=LOG_PATH,
        )
        elapsed = time.perf_counter() - started
        rep_result = {
            "rep": rep + 1,
            "success": result is not None,
            "latency_s": round(elapsed, 3),
        }
        if result is not None:
            payload = result["payload"]
            rep_result["compression_ratio"] = result["log_entry"]["compression_ratio"]
            rep_result["summary"] = payload.get("summary", "")[:200]
            rep_result["excerpt_count"] = len(payload.get("relevant_error_excerpts", []))
            rep_result["suspect_count"] = len(payload.get("suspected_files_modules", []))
            rep_result["recommendation"] = payload.get("escalation_recommendation")
            # Check for hallucinated paths
            hallucinated = 0
            for excerpt in payload.get("relevant_error_excerpts", []):
                p = excerpt.get("path", "")
                if "C:/" in p or p.startswith("/") or "not/in" in p:
                    hallucinated += 1
            for suspect in payload.get("suspected_files_modules", []):
                p = suspect.get("path", "")
                if "C:/" in p or p.startswith("/") or "not/in" in p:
                    hallucinated += 1
            rep_result["hallucinated_paths"] = hallucinated
        else:
            rep_result["compression_ratio"] = None
            rep_result["summary"] = None
            rep_result["excerpt_count"] = 0
            rep_result["suspect_count"] = 0
            rep_result["recommendation"] = None
            rep_result["hallucinated_paths"] = 0
        results.append(rep_result)
        print(f"  [{model}] {workload_key} rep {rep+1}/{wl['reps']}: {'OK' if result else 'FAIL'} ({elapsed:.1f}s)")
    return results


def print_summary(all_results: dict) -> None:
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    for model in MODELS:
        if model not in all_results:
            print(f"\n--- {model} --- (not tested yet)")
            continue
        print(f"\n--- {model} ---")
        total_runs = 0
        successes = 0
        invalid_output = 0
        hallucinated = 0
        compressions = []
        latencies = []
        for wk in ["B", "C", "D"]:
            for r in all_results[model].get(wk, []):
                total_runs += 1
                if r["success"]:
                    successes += 1
                    if r["compression_ratio"] is not None:
                        compressions.append(r["compression_ratio"])
                    latencies.append(r["latency_s"])
                    hallucinated += r["hallucinated_paths"]
                else:
                    invalid_output += 1
        avg_comp = sum(compressions) / len(compressions) if compressions else 0
        avg_lat = sum(latencies) / len(latencies) if latencies else 0
        sorted_lat = sorted(latencies)
        p50 = sorted_lat[len(sorted_lat) // 2] if sorted_lat else 0
        slowest = max(latencies) if latencies else 0
        print(f"  Success: {successes}/{total_runs}")
        print(f"  Invalid output: {invalid_output}")
        print(f"  Hallucinated paths: {hallucinated}")
        print(f"  Avg compression: {avg_comp:.4f}")
        print(f"  Avg latency: {avg_lat:.2f}s")
        print(f"  P50 latency: {p50:.2f}s")
        print(f"  Slowest: {slowest:.2f}s")


def main():
    print("=" * 70)
    print("MODEL COMPARISON — Issue #35")
    print("=" * 70)
    print()

    checkpoint = load_checkpoint()
    all_results = checkpoint.get("results", {})
    completed_models = set(checkpoint.get("completed_models", []))

    if completed_models:
        print(f"Resuming from checkpoint. Already completed: {', '.join(sorted(completed_models))}")
        print()

    for model in MODELS:
        if model in completed_models:
            print(f"--- {model} --- (already completed, skipping)")
            continue

        print(f"\n--- {model} ---")
        model_results = {}
        for wk in ["B", "C", "D"]:
            print(f"  Workload {wk}...")
            model_results[wk] = test_model(model, wk)

        all_results[model] = model_results
        completed_models.add(model)

        # Save checkpoint after each model
        checkpoint["completed_models"] = sorted(completed_models)
        checkpoint["results"] = all_results
        save_checkpoint(checkpoint)
        print(f"  [checkpoint saved after {model}]")

    print_summary(all_results)

    # Save full results
    report_path = REPO_ROOT / "model_comparison_results.json"
    report_path.write_text(json.dumps(all_results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nFull results saved to {report_path}")


if __name__ == "__main__":
    main()
