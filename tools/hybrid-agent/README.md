# Hybrid Agent Prototype

This prototype adds an optional hybrid local-model preprocessing layer for `Project Execution OS`.

The local model is used as a bounded worker, not the primary architect.

It can:

- compress repetitive logs and file excerpts into a structured payload;
- preserve source paths and line ranges in the compact payload;
- route work through `local-only`, `preprocess-then-cloud`, or `cloud-only` mode;
- log both local and cloud stages in JSONL with size metrics and optional token usage.

It does not:

- make a local model mandatory;
- replace the smallest-sufficient-context rule from `docs/CONTEXT_ASSEMBLY_STANDARD.md`;
- add autonomous orchestration, RAG, or vector infrastructure;
- guarantee that every OpenAI-compatible server exposes the same usage fields.

## Folder

```text
tools/hybrid-agent/
├─ hybrid_agent.py
├─ run_hybrid_agent.py
├─ benchmark_fixture.py
├─ fixtures/
└─ tests/
```

## Modes

- `local-only`: only run the bounded local preprocessing stage.
- `preprocess-then-cloud`: run local preprocessing first, then send the compact local payload to the cloud stage by default.
- `cloud-only`: skip local preprocessing entirely.

Successful hybrid path:

- cloud receives the compact local payload as the primary context;
- traceability is preserved through source paths and line ranges carried inside that compact payload;
- raw bounded evidence is excluded by default to keep the cloud-bound payload smaller.

Fallback or skip path:

- if local preprocessing fails or is skipped, cloud receives the original bounded evidence package;
- this preserves continuity even when the local stage is unavailable.

Debug path:

- pass `--debug-full-evidence` if you want successful hybrid runs to include both the compact payload and the original bounded evidence for inspection.

## Configuration

The CLI reads flags first, then falls back to environment variables.

Local stage:

```text
HYBRID_AGENT_LOCAL_ENDPOINT
HYBRID_AGENT_LOCAL_MODEL
HYBRID_AGENT_LOCAL_API_KEY
```

Cloud stage:

```text
HYBRID_AGENT_CLOUD_ENDPOINT
HYBRID_AGENT_CLOUD_MODEL
HYBRID_AGENT_CLOUD_API_KEY
```

## Minimal Local Setup With Ollama

Ollama exposes an OpenAI-compatible API at `/v1`, so this prototype can target it without a custom adapter.

Example:

```powershell
ollama pull llama3.2
$env:HYBRID_AGENT_LOCAL_ENDPOINT = "http://localhost:11434/v1"
$env:HYBRID_AGENT_LOCAL_MODEL = "llama3.2"
$env:HYBRID_AGENT_LOCAL_API_KEY = "ollama"
```

## Example Cloud Setup

```powershell
$env:HYBRID_AGENT_CLOUD_ENDPOINT = "https://api.openai.com/v1"
$env:HYBRID_AGENT_CLOUD_MODEL = "gpt-4.1-mini"
$env:HYBRID_AGENT_CLOUD_API_KEY = "YOUR_KEY_HERE"
```

## Example Commands

Cloud only:

```powershell
python tools/hybrid-agent/run_hybrid_agent.py `
  --mode cloud-only `
  --task "Summarize the failure and propose the next debugging step." `
  --log-path logs/latest.md
```

Local only:

```powershell
python tools/hybrid-agent/run_hybrid_agent.py `
  --mode local-only `
  --task "Compress this failure log into a compact triage payload." `
  --log-path logs/latest.md
```

Hybrid:

```powershell
python tools/hybrid-agent/run_hybrid_agent.py `
  --mode preprocess-then-cloud `
  --task "Analyze repeated failures and propose the next safe implementation step." `
  --log-path logs/latest.md `
  --file-path PROJECT_STATE.md

Hybrid with full-evidence debug:

```powershell
python tools/hybrid-agent/run_hybrid_agent.py `
  --mode preprocess-then-cloud `
  --debug-full-evidence `
  --task "Analyze repeated failures and inspect both compressed and raw evidence." `
  --log-path logs/latest.md
```
```

Benchmark fixture:

```powershell
python tools/hybrid-agent/benchmark_fixture.py
```

Tests:

```powershell
python -m unittest discover -s tools/hybrid-agent/tests -p "test_*.py" -v
```

## Runtime Logging

Runtime logs default to:

```text
logs/api-runtime/hybrid-agent.jsonl
```

Each stage records:

- `stage`;
- `provider`;
- `model`;
- `selected_route`;
- `loaded_modules`;
- `latency_ms`;
- `status`;
- `input_size_bytes`;
- `output_size_bytes`;
- `compression_ratio`;
- token and cache fields when the endpoint exposes them.

For this prototype, `compression_ratio` means:

```text
output_size_bytes / input_size_bytes
```

Smaller values mean stronger compression.

## Structured Local Output Shape

The local stage returns a single JSON object with:

- `summary`;
- `relevant_error_excerpts`;
- `suspected_files_modules`;
- `escalation_recommendation`;
- `local_stage_metadata`.

## Limitations

- Local models still have RAM, VRAM, and context-window limits.
- OpenAI-compatible servers vary, especially around usage and cache fields.
- This prototype preserves evidence references, but it only sees the bounded excerpts that were passed in.
- Fallback preserves continuity, but a failed local stage still adds some latency before the cloud stage continues.
