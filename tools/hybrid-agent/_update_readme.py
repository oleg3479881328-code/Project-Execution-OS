"""Update README.md with fallback contract and model selection docs."""
from pathlib import Path

path = Path(__file__).resolve().parent / "README.md"
content = path.read_text(encoding="utf-8")

# Insert Fallback Contract section after '### Auto Policy' section
old = (
    "Explicit `cloud-only` is stricter:\n\n"
    "- it skips local preprocessing entirely;\n"
    "- it also skips Ollama availability probing, so a missing local runtime does not add latency to a forced cloud-only run.\n\n"
    "### Timeout Strategy"
)

new = (
    "Explicit `cloud-only` is stricter:\n\n"
    "- it skips local preprocessing entirely;\n"
    "- it also skips Ollama availability probing, so a missing local runtime does not add latency to a forced cloud-only run.\n\n"
    "## Fallback Contract (Graceful Degradation)\n\n"
    "The local preprocessing stage is designed to fail gracefully without blocking the pipeline.\n\n"
    "Every failure mode is caught individually:\n\n"
    "| Failure Mode | Detection | Behaviour |\n"
    "|---|---|---|\n"
    "| Ollama call timeout | `call_failed: timed out` | Returns `None` \u2192 cloud receives raw evidence |\n"
    "| Response parse failure | `call_failed: <error>` | Returns `None` \u2192 cloud receives raw evidence |\n"
    "| JSON parse failure | `response_parse_failed` | Returns `None` \u2192 cloud receives raw evidence |\n"
    "| Schema validation failure | `schema_validation_failed` | Returns `None` \u2192 cloud receives raw evidence |\n"
    "| Reference validation failure | `reference_validation_failed` | Returns `None` \u2192 cloud receives raw evidence |\n\n"
    "Each failure is logged to the runtime JSONL with `status: \"failed_fallback_to_cloud\"` and a descriptive `notes` field.\n\n"
    "The caller (`run_hybrid_agent` / `run_workstation_hybrid_route`) checks for `None` return instead of catching exceptions:\n\n"
    "```python\n"
    "local_result = run_local_stage(config, input_payload, ...)\n"
    "if local_result is None:\n"
    "    # skip local, proceed with raw evidence\n"
    "```\n\n"
    "This means:\n"
    "- A slow or broken local model never crashes the pipeline.\n"
    "- Cloud stage always receives either the compact payload or the original raw evidence.\n"
    "- Failures are observable in logs for debugging.\n\n"
    "## Local Model Selection\n\n"
    "The hybrid agent supports any Ollama model installed on the workstation.\n\n"
    "### Default Recommendation\n\n"
    "Based on comparative benchmarking across 4 installed models, the recommended default is:\n\n"
    "**`llama3.2:3b`** \u2014 best balance of speed, reliability, and output quality.\n\n"
    "| Model | Success Rate | Avg Latency | Avg Compression | Hallucinated Paths |\n"
    "|---|---|---|---|---|\n"
    "| **llama3.2:3b** | 7/7 (100%) | ~27s | 0.22 | 0 |\n"
    "| qwen3:4b | \u2014 | very slow | \u2014 | \u2014 |\n"
    "| qwen2.5-coder:7b | \u2014 | \u2014 | \u2014 | \u2014 |\n"
    "| deepseek-coder:6.7b | \u2014 | \u2014 | \u2014 | \u2014 |\n\n"
    "*Full benchmark results in `model_comparison_results.json`.*\n\n"
    "### Selecting a Model\n\n"
    "Explicit model selection via CLI:\n\n"
    "```powershell\n"
    "python tools/hybrid-agent/run_workstation_hybrid_route.py `\n"
    "  --local-model qwen2.5-coder:7b `\n"
    "  -Executor codex `\n"
    "  -Mode auto `\n"
    "  -Task \"Analyze this bounded task.\" `\n"
    "  -LogPath tools/hybrid-agent/fixtures/synthetic_repetitive_log.txt\n"
    "```\n\n"
    "Or via environment variable:\n\n"
    "```powershell\n"
    "$env:HYBRID_AGENT_LOCAL_MODEL = \"qwen2.5-coder:7b\"\n"
    "```\n\n"
    "If no model is specified, the adapter defaults to `llama3.2:3b`.\n\n"
    "### Model Characteristics\n\n"
    "- **llama3.2:3b** (2.0 GB): Fast, reliable, good compression. Best default for most workloads.\n"
    "- **qwen3:4b** (2.5 GB): Slower but may offer better reasoning on complex evidence.\n"
    "- **qwen2.5-coder:7b** (4.7 GB): Code-optimized, larger context window. Good for code-heavy evidence.\n"
    "- **deepseek-coder:6.7b** (3.8 GB): Code-specialised, strong at structured output generation.\n\n"
    "### Timeout Strategy"
)

content = content.replace(old, new)

# Update timeout section with model-specific recommendations
old_timeout = "This applies to normal workstation launcher use and can still be overridden explicitly."
new_timeout = (
    "This applies to normal workstation launcher use and can still be overridden explicitly.\n\n"
    "Different models may need different timeouts:\n\n"
    "| Model | Recommended Timeout |\n"
    "|---|---|\n"
    "| llama3.2:3b | 120s |\n"
    "| qwen3:4b | 600s |\n"
    "| qwen2.5-coder:7b | 120s |\n"
    "| deepseek-coder:6.7b | 120s |"
)

content = content.replace(old_timeout, new_timeout)

path.write_text(content, encoding="utf-8")
print("README updated successfully")
