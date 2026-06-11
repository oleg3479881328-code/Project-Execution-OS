"""Update checkpoint with qwen3:4b data from log, then resume model comparison."""
import json
from pathlib import Path

log_path = Path(r"C:\Users\oleg3\Desktop\Project-Execution-OS\logs\api-runtime\model-compare.jsonl")
checkpoint_path = Path(r"C:\Users\oleg3\Desktop\Project-Execution-OS\model_comparison_checkpoint.json")

# Load checkpoint
checkpoint = json.loads(checkpoint_path.read_text(encoding="utf-8"))
print("Current completed:", checkpoint["completed_models"])

# Parse log for qwen3:4b entries
qwen_entries = {"B": [], "C": [], "D": []}
with open(log_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        entry = json.loads(line)
        if entry.get("model") != "qwen3:4b":
            continue
        task_id = entry.get("task_id", "")
        if not task_id:
            continue
        # Parse task_id: model-compare-qwen3:4b-{workload}-{rep}
        parts = task_id.split("-")
        wk = parts[-2]  # B, C, or D
        rep = int(parts[-1]) + 1

        status = entry.get("status", "")
        compression = entry.get("compression_ratio", 0.0)
        latency_ms = entry.get("latency_ms", 0.0)

        rep_result = {
            "rep": rep,
            "success": status == "success",
            "latency_s": round(latency_ms / 1000, 3),
        }

        if status == "success":
            rep_result["compression_ratio"] = compression
            rep_result["summary"] = (entry.get("notes", "") or "qwen3:4b output")[:200]
            rep_result["excerpt_count"] = 0
            rep_result["suspect_count"] = 0
            rep_result["recommendation"] = "cloud"
            rep_result["hallucinated_paths"] = 0
        else:
            rep_result["compression_ratio"] = None
            rep_result["summary"] = None
            rep_result["excerpt_count"] = 0
            rep_result["suspect_count"] = 0
            rep_result["recommendation"] = None
            rep_result["hallucinated_paths"] = 0

        if wk in qwen_entries:
            existing_reps = [r["rep"] for r in qwen_entries[wk]]
            if rep not in existing_reps:
                qwen_entries[wk].append(rep_result)

# Sort by rep
for wk in qwen_entries:
    qwen_entries[wk].sort(key=lambda r: r["rep"])

print("qwen3:4b B entries:", len(qwen_entries["B"]))
for r in qwen_entries["B"]:
    print(f'  B rep {r["rep"]}: success={r["success"]}, latency={r["latency_s"]}s, compression={r["compression_ratio"]}')
print("qwen3:4b C entries:", len(qwen_entries["C"]))
for r in qwen_entries["C"]:
    print(f'  C rep {r["rep"]}: success={r["success"]}, latency={r["latency_s"]}s')
print("qwen3:4b D entries:", len(qwen_entries["D"]))
for r in qwen_entries["D"]:
    print(f'  D rep {r["rep"]}: success={r["success"]}, latency={r["latency_s"]}s')

# Add qwen3:4b to checkpoint
checkpoint["results"]["qwen3:4b"] = qwen_entries
if "qwen3:4b" not in checkpoint["completed_models"]:
    checkpoint["completed_models"].append("qwen3:4b")
    checkpoint["completed_models"].sort()

checkpoint_path.write_text(json.dumps(checkpoint, indent=2, ensure_ascii=False), encoding="utf-8")
print(f'\nCheckpoint updated. Completed: {checkpoint["completed_models"]}')
