# Hybrid Ollama Model Comparison — Interim Results

Updated: 2026-06-09
Status: `interim`
Source task: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/35
Source PR: https://github.com/oleg3479881328-code/Project-Execution-OS/pull/39

## Purpose

Preserve measured interim results from the workstation hybrid-agent hardening and Ollama model-comparison phase before final PR integration.

## Implemented Reliability Improvements

- Graceful degradation added for local preprocessing failures.
- `run_local_stage()` returns `None` instead of crashing on:
  - timeout;
  - response parse failure;
  - JSON parse failure;
  - schema validation failure;
  - reference validation failure.
- Caller falls back safely instead of propagating the local-stage exception.
- Invented paths remain untrusted and are not forwarded as validated evidence.
- Explicit local-model selection added through:
  - CLI flag: `--local-model`;
  - environment variable: `HYBRID_AGENT_LOCAL_MODEL`.
- Current documented default model: `llama3.2:3b`.

## Validation Snapshot

- Unit tests: `23/23 passed`.
- Benchmark fixture: passed.
- Fixture compression ratio: approximately `0.50`.
- Fixture latency: approximately `12.8 ms`.

## Measured Local Model Comparison

| Model | Success Rate | Average Latency | Average Compression Ratio | Hallucinated Paths | Interim Assessment |
|---|---:|---:|---:|---:|---|
| `llama3.2:3b` | `7/7` (`100%`) | approximately `27 s` | `0.22` | `0` | Best current default: reliable, acceptable speed, good compression. |
| `qwen3:4b` | `3/7` (`43%`) | approximately `403 s` | `0.33` | `0` | Too slow on this workstation; large workload timed out. |
| `qwen2.5-coder:7b` | `4/7` (`57%`) | approximately `16 s` | `0.21` | `0` | Fast, but unstable on medium workload due to invalid output. |
| `deepseek-coder:6.7b` | `5/7` (`71%`) | approximately `59 s` | `0.24` | `0` | Mixed result; slower and less reliable than `llama3.2:3b`. |

## Interim Recommendation

Keep `llama3.2:3b` as the default local preprocessing model for the current workstation configuration.

Reasoning order:

1. reliability first;
2. latency second;
3. compression third.

`llama3.2:3b` currently wins because it completed all measured runs successfully, produced zero hallucinated paths, and preserved useful compression with acceptable latency.

## Important Boundary

These are measured workstation results for the current hybrid preprocessing role. They do not prove that `llama3.2:3b` is the best model for all local-agent tasks, coding tasks, or future larger hardware configurations.

## Current Integration State

- PR #39 contains the implementation and benchmark artifacts.
- PR #39 is not yet ready to merge because GitHub Actions currently fails at system-context manifest validation.
- Reviewer correction requested: update required manifest bookkeeping, keep the change narrow, avoid unnecessary benchmark reruns, and reassess whether transient checkpoint/output files belong in the PR.

## Next Step

Review and merge the corrected PR #39 after CI passes.
