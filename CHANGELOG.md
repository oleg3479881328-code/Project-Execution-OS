# Changelog

## 2026-05-29

- added `system-manifest.json` as the machine-readable core-node and typed-relationship map for Project Execution OS
- added `scripts/validate-system-integrity.ps1` and `.github/workflows/validate-system-integrity.yml` for document-network self-integrity validation
- clarified in `README.md` that the new manifest and validator harden the document-first foundation without introducing a runtime engine

## 2026-05-21

- clarified `START_HERE.md` as the one top-level entry, with routing into new-project, existing-project, and fast-orientation paths
- added machine-readable `PROJECT_STATE.md` frontmatter guidance and updated the `green-apple` sample project
- documented optional `CONTEXT_PACK.md` as a fast re-entry brief, not a source of truth
- added GitHub Actions project-structure validation through `.github/workflows/validate-project-structure.yml`
- created `docs/integrations/` and moved ChatGPT-facing entrypoints there as the preferred integration surface
