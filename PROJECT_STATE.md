---
status: transfer_ready
project_mode: document-first
current_step: issue-21-semantic-index-pilot-implemented
current_run: none
last_updated: 2026-06-06
next_action: Decide whether the semantic pilot should be published as-is or refined further for query quality before PR/merge.
---

# PROJECT STATE — Project Execution OS

## Current Phase

Foundation system is active and now includes an index-first discovery layer with a local semantic retrieval pilot for issue `#21`.

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

## Workflow Operating Notes

- The current repository itself is governed by `Project Execution OS`.
- The current knowledge-library portal implementation is local-preview-first and does not yet attach any public hosting target.
- The local Quartz scaffold remains local-only and public deployment is still deferred.
- The semantic runtime is local-only, uses `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`, and keeps the SQLite store outside Git under `.local/semantic-index/`.

## Open Questions

- Whether the current corpus boundary is sufficient or should be refined further for better query quality on sparse domains.
- Whether a separate lexical query companion should be added later for stronger fallback behavior.
- Whether the portal scaffold should remain as a nested local clone or be promoted into its own private GitHub repository next.

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
- `docs/ROUTER.md`
- `workflow-templates/project-bootstrap/AGENTS_TEMPLATE.md`
- `PROJECT.md`
- `PROJECT_STATE.md`
- `logs/latest.md`

## Latest Result

Issue `#21` now has a bounded local discovery implementation: a structural corpus builder, corpus validator, semantic SQLite store builder, semantic query CLI, semantic pilot workflow, refreshed generated corpus, and mandatory index-first routing updates in the root agent instructions, bootstrap template, context standard, agent-creation standard, router, and ChatGPT integration prompt. Local validation succeeded for corpus build, corpus validation, dependency install, semantic-store build, semantic queries, manifest validation, and Git ignore protection for `.local/semantic-index/semantic-index.sqlite3`.

## Next Action

Review query quality on additional real retrieval tasks, then publish or refine the issue `#21` implementation based on whether the current bounded corpus is adequate.
