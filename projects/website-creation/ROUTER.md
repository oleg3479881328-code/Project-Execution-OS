# Website Creator — ROUTER.md

## Purpose

Route Website Creator work to the smallest global reusable standard/capability required for the task.

## Routes

- project orientation / current state / where are we now -> `PROJECT_STATE.md`
- architecture review decisions / second opinion / accepted vs rejected changes -> `reviews/SECOND_OPINION_DECISION_2026-09-13.md`
- find an existing reusable website capability / standard / production contract -> `SOURCE_REGISTRY.md`
- tools / SaaS / libraries / frameworks / execution platforms / donors -> `TOOL_DONOR_REGISTRY.md`
- Site Model / canonical site schema / Site Instance / platform-independent site state / renderer contract / adapter contract -> `SITE_MODEL_STANDARD.md`
- website design / visual direction / donor analysis / sections / UI / responsive / motion / design QA -> `../../blocks/design/BLOCK.md`
- visual editor / image editor / CMS editor / safe client editing / crop / move / zoom / image resize / direct manipulation -> `EDITOR_CREATION_STANDARD.md`
- research / entity dossier / evidence / existing-site audit -> `SOURCE_REGISTRY.md` Research & Evidence section
- information architecture / conversion / page strategy -> `SOURCE_REGISTRY.md` Strategy & IA section
- structured content / page data / reusable renderers / publication states -> `SITE_MODEL_STANDARD.md` plus `SOURCE_REGISTRY.md` Content & Data section
- media / image derivatives / galleries / crop metadata -> `SOURCE_REGISTRY.md` Media section and `EDITOR_CREATION_STANDARD.md` when interaction is involved
- SEO / local SEO / AEO / GEO / pSEO / schema / canonical / sitemap / indexing -> `SOURCE_REGISTRY.md` SEO & Discovery section
- implementation / Git / preview / staging / release / rollback / Vercel / Netlify / DNS / domain -> `SOURCE_REGISTRY.md` Build & Release section plus `TOOL_DONOR_REGISTRY.md`
- accessibility / responsive checks / browser QA / visual QA -> `SOURCE_REGISTRY.md` QA section; use Playwright as default browser-QA direction where applicable
- analytics / search validation / conversion measurement -> `SOURCE_REGISTRY.md` Measurement section
- automated local-business website production / prospect discovery / preview-first selling -> `SOURCE_REGISTRY.md` Website Factory section plus `TOOL_DONOR_REGISTRY.md`
- AI-assisted website creation / coding-agent workflow -> `TOOL_DONOR_REGISTRY.md` and applicable production standard
- new site implementation -> `PROJECT_STATE.md` → `SITE_MODEL_STANDARD.md` → relevant task standards → `../../docs/EXISTING_SOLUTION_FIRST_STANDARD.md` → implementation

## Loading Rule

Do not mass-read the whole project. Load the narrowest standard required by the active task.

Default new-site path:

`PROJECT.md → PROJECT_STATE.md → SITE_MODEL_STANDARD.md → ROUTER.md → relevant Website Creator standard(s) → Design Block when visual work is required → implementation → QA/release gates`.

For any client-facing visual editor task, read `EDITOR_CREATION_STANDARD.md` before implementation.

For any design task, use `../../blocks/design/BLOCK.md` as the design-process authority rather than reconstructing a second design pipeline inside Website Creator.

## Client-Agnostic Rule

Do not route from Website Creator into a client project to obtain required production knowledge. If a reusable fact exists only in a client project, promote/generalize it into Website Creator first.

## Evidence Rule

Do not create extra routing/manifests merely because they might be useful later. Add deeper task manifests only when real routing/context failures prove they are needed.

## Final Rule

Website Creator owns reusable website-production knowledge and execution contracts. Client projects consume Website Creator; Website Creator does not depend on client projects.