---
status: transfer_ready
project_mode: document-first
current_step: issue-27-hybrid-agent-prototype-implemented
current_run: none
last_updated: 2026-06-08
next_action: Validate the optional hybrid local-model preprocessing prototype against real local endpoints and decide whether it should stay experimental or be promoted into a broader central pattern.
---

# PROJECT STATE — Project Execution OS

## Current Phase

Foundation system is active and now includes an index-first discovery layer with a local semantic retrieval pilot for issue `#21` plus an optional hybrid local-model preprocessing prototype for issue `#27`.

## Current Workflow Run

None.

## Confirmed Decisions

- `START_HERE.md` remains the single stable external entrypoint.
- `docs/ROUTER.md` remains the live internal map.
- Project entry should stay narrow and selective rather than loading the whole repository by default.
- Active projects must preserve transfer-ready state as a byproduct of work rather than only on explicit handoff request.
- Existing solutions and current repository standards should be adapted before inventing new mechanisms.
- For code-like project work where donors are plausible, a relevant GitHub repository search is part of a complete reuse-first pass unless explicitly ruled out.
- The knowledge-library access layer should use `GitHub -> Obsidian -> Quartz` with an explicit allowlist sync boundary rather than whole-repository publication.
- The accepted repository-side implementation for issue `#11` was merged through PR `#13` at commit `d5cafedb169c89d4ad0c8b4d1192a78ff9fab851`.
- Issue `#14` should produce a lightweight reusable `blocks/design/` package centered on goal, user path, structure, wireframe, UI system, responsive behavior, frontend-aware handoff, and design review.
- Issue `#21` should add a bounded structural corpus builder, a local semantic SQLite runtime, and mandatory index-first entry rules without introducing hosted retrieval infrastructure.
- Issue `#27` should keep local-model use optional, bounded, and evidence-preserving while measuring cloud-context compression rather than assuming it.

## Workflow Operating Notes

- The current repository itself is governed by `Project Execution OS`.
- The current knowledge-library portal implementation is local-preview-first and does not yet attach any public hosting target.
- The local Quartz scaffold remains local-only and public deployment is still deferred.
- The semantic runtime is local-only, uses `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`, and keeps the SQLite store outside Git under `.local/semantic-index/`.
- The hybrid-agent prototype targets OpenAI-compatible local and cloud endpoints through a small isolated adapter under `tools/hybrid-agent/` and records stage-aware JSONL runtime logs under `logs/api-runtime/`.

## Open Questions

- Whether the current corpus boundary is sufficient or should be refined further for better query quality on sparse domains.
- Whether a separate lexical query companion should be added later for stronger fallback behavior.
- Whether the portal scaffold should remain as a nested local clone or be promoted into its own private GitHub repository next.
- Whether real endpoint runs confirm that the local preprocessing stage reduces cloud-bound payload size enough to justify the extra moving part.

## Active Files

- `.gitignore`
- `AGENTS.md`
- `SYSTEM_CONTEXT_MANIFEST.md`
- `.github/workflows/semantic-index-pilot.yml`
- `docs/AGENT_CREATION_STANDARD.md`
- `docs/AGENT_INDEX_FIRST_ENTRY_STANDARD.md`
- `docs/CONTEXT_ASSEMBLY_STANDARD.md`
- `docs/INDEXING_STANDARD.md`
- `docs/INDEXING_LAYER_STATUS.md`
- `docs/ROUTER.md`
- `docs/SEMANTIC_INDEX_ARCHITECTURE.md`
- `docs/SEMANTIC_SEARCH_RUNTIME.md`
- `docs/integrations/chatgpt/CORE_SYSTEM_PROMPT.md`
- `indexes/README.md`
- `indexes/semantic-documents.jsonl`
- `scripts/build_system_index.py`
- `scripts/validate_system_index_v3.py`
- `scripts/build_semantic_store.py`
- `scripts/query_semantic_store.py`
- `semantic-requirements.txt`
- `tools/hybrid-agent/hybrid_agent.py`
- `tools/hybrid-agent/run_hybrid_agent.py`
- `tools/hybrid-agent/benchmark_fixture.py`
- `tools/hybrid-agent/README.md`
- `tools/hybrid-agent/fixtures/synthetic_repetitive_log.txt`
- `tools/hybrid-agent/fixtures/mock_local_payload.json`
- `tools/hybrid-agent/tests/test_hybrid_agent.py`
- `docs/ROUTER.md`
- `workflow-templates/project-bootstrap/AGENTS_TEMPLATE.md`
- `PROJECT.md`
- `PROJECT_STATE.md`
- `logs/latest.md`

## Latest Result

Issue `#27` now has a runnable bounded hybrid-agent prototype under `tools/hybrid-agent/` with `local-only`, `preprocess-then-cloud`, and `cloud-only` modes; evidence-preserving local JSON compression; graceful fallback from local failure to cloud reasoning; JSONL runtime logs with stage-aware size metrics and optional token fields; unit tests using mocked OpenAI-compatible endpoints; and a no-paid-call benchmark fixture for repetitive logs. Narrow standards updates were added to `docs/CONTEXT_ASSEMBLY_STANDARD.md` and `docs/API_RUNTIME_COST_CACHE_LOGGING_STANDARD.md` so the prototype extends existing rules instead of replacing them.

## Next Action

Run the hybrid prototype against a real local OpenAI-compatible endpoint such as Ollama, compare observed compression ratios and latency against the cloud-only path, and decide whether the current isolated prototype is sufficient for review or needs one more refinement pass.
