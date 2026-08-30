# Changelog

This is a curated milestone log for significant Project Execution OS changes. It is not a per-commit ledger; Git history and `logs/latest.md` remain the detailed execution record.

## 2026-08-30

- established `START_HERE.md` as the single stable global AI/client entrypoint with recursive, unbounded router depth
- added `projects/ROUTER.md` and aligned project-entry, context-assembly, ChatGPT compatibility and project-memory rules with the global routing architecture
- upgraded `docs/KNOWLEDGE_SYSTEM.md` to knowledge-in-the-flow behavior adapted from KCS: search/reuse early, improve canonical knowledge during execution, capture expensive-to-reconstruct learning in the moment, and retain the final promotion gate as a safety net
- aligned `docs/PROJECT_MEMORY_STANDARD.md` and `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md` with continuous knowledge/state preservation
- added a machine-checked completion contract to the repository integrity workflow so the core chain `agent instructions -> knowledge-in-flow -> project memory -> transfer-ready state -> review promotion gate` cannot silently disappear
- repaired `SYSTEM_CONTEXT_MANIFEST.md` after integrity validation exposed stale profile SHAs
- added `scripts/audit_system_hygiene.py` and expanded `docs/INDEXING_STANDARD.md` so PEOS can detect structural bloat signals such as undiscoverable entrypoints, unindexed skills, aged candidates, duplicate canonical Markdown, possibly orphaned standards and stale curated milestones without auto-deleting knowledge

## 2026-06-10

- added `docs/AGENT_QUALITY_SCORECARD_STANDARD.md` for measuring agent quality by successful outcomes, cost, latency, context efficiency, tool-use quality, regression protection, observability, safety and transferability
- routed agent-quality, eval and orchestration-complexity work through `docs/ROUTER.md`
- updated `SYSTEM_CONTEXT_MANIFEST.md` to `system-context-manifest-v10` / `knowledge-aware-core-v10`
- recorded the change in `logs/2026-06-10-agent-quality-scorecard-standard.md`

## 2026-06-01

- added root `PROJECT_STATE.md` and `logs/latest.md` so the central repository complies with its own active transfer-readiness standard
- updated `PROJECT.md` and `PROJECT_INDEX.md` after the successful temporary `Test123` bootstrap smoke test and its deletion
- recorded the central project as transfer-ready for the next executor

## 2026-05-21

- clarified `START_HERE.md` as the one top-level entry, with routing into new-project, existing-project, and fast-orientation paths
- added machine-readable `PROJECT_STATE.md` frontmatter guidance and updated the `green-apple` sample project
- documented optional `CONTEXT_PACK.md` as a fast re-entry brief, not a source of truth
- added GitHub Actions project-structure validation through `.github/workflows/validate-project-structure.yml`
- created `docs/integrations/` and moved ChatGPT-facing entrypoints there as the preferred integration surface