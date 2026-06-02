# Changelog

## 2026-06-02

- added `docs/DEPLOYMENT_STANDARD.md` to define `Cloudflare Pages` as the default static deployment layer for static/frontend projects
- added a deployment/hosting route in `docs/ROUTER.md` pointing to `docs/DEPLOYMENT_STANDARD.md`
- added optional deployment metadata fields to the project entrypoint standard and `PROJECT.md` templates
- clarified execution-state language so prepared deployment is not treated as executed deployment

## 2026-05-21

- clarified `START_HERE.md` as the one top-level entry, with routing into new-project, existing-project, and fast-orientation paths
- added machine-readable `PROJECT_STATE.md` frontmatter guidance and updated the `green-apple` sample project
- documented optional `CONTEXT_PACK.md` as a fast re-entry brief, not a source of truth
- added GitHub Actions project-structure validation through `.github/workflows/validate-project-structure.yml`
- created `docs/integrations/` and moved ChatGPT-facing entrypoints there as the preferred integration surface
