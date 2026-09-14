# Website Creator — ROUTER.md

## Purpose

Route Website Creator work to the smallest global reusable standard/capability required for the task.

## Routes

- project orientation / current state / where are we now -> `PROJECT_STATE.md`
- own system / shared engine / speed / reuse / no arbitrary SaaS / fresh-chat execution rules -> `OWN_SYSTEM_EXECUTION_STANDARD.md`
- **shared engine implementation / build / seed / runtime / component registry / renderer code -> `engine/README.md` then `engine/STATUS.md`**
- **current engine verification / what is already working / next implementation slice -> `engine/STATUS.md`**
- architecture review decisions / second opinion / accepted vs rejected changes -> `reviews/SECOND_OPINION_DECISION_2026-09-13.md`
- speed bottleneck / ready-solution review evidence -> `reviews/SPEED_SYSTEM_REVIEW_2026-09-14.md`
- find an existing reusable website capability / standard / production contract -> `SOURCE_REGISTRY.md`
- tools / SaaS / libraries / frameworks / execution platforms / donors -> `TOOL_DONOR_REGISTRY.md`
- Site Model / canonical site schema / Site Instance / platform-independent site state / renderer contract / adapter contract -> `SITE_MODEL_STANDARD.md`
- website design / visual direction / donor analysis / sections / UI / responsive / motion / design QA -> `../../blocks/design/BLOCK.md`
- visual editor / image editor / CMS editor / safe client editing / crop / move / zoom / image resize / direct manipulation -> `EDITOR_CREATION_STANDARD.md` plus `engine/README.md` for implementation
- research / entity dossier / evidence / existing-site audit -> `SOURCE_REGISTRY.md` Research & Evidence section
- information architecture / conversion / page strategy -> `SOURCE_REGISTRY.md` Strategy & IA section
- structured content / page data / reusable renderers / publication states -> `SITE_MODEL_STANDARD.md` plus `SOURCE_REGISTRY.md` Content & Data section
- media / image derivatives / galleries / crop metadata -> `SOURCE_REGISTRY.md` Media section and `EDITOR_CREATION_STANDARD.md` when interaction is involved
- SEO / local SEO / AEO / GEO / pSEO / schema / canonical / sitemap / indexing -> `SOURCE_REGISTRY.md` SEO & Discovery section
- implementation / Git / preview / staging / release / rollback / deployment adapter / DNS / domain -> `OWN_SYSTEM_EXECUTION_STANDARD.md` plus `engine/README.md` plus `SOURCE_REGISTRY.md` Build & Release section
- accessibility / responsive checks / browser QA / visual QA -> `SOURCE_REGISTRY.md` QA section; use Playwright as default browser-QA direction where applicable; engine tests live under `engine/tests/`
- analytics / search validation / conversion measurement -> `SOURCE_REGISTRY.md` Measurement section
- automated local-business website production / prospect discovery / preview-first selling -> `OWN_SYSTEM_EXECUTION_STANDARD.md` plus `SOURCE_REGISTRY.md` Website Factory section
- AI-assisted website creation / coding-agent workflow -> `OWN_SYSTEM_EXECUTION_STANDARD.md` plus applicable tool/production standard
- new site implementation -> `PROJECT_STATE.md` → `OWN_SYSTEM_EXECUTION_STANDARD.md` → `engine/STATUS.md` → `SITE_MODEL_STANDARD.md` → relevant task standards → shared engine
- shared engine capability missing -> `OWN_SYSTEM_EXECUTION_STANDARD.md` → relevant canonical contract → implement once in `engine/` → verify against active Site Instance

## Work Classification Rule

Every website task must classify itself as one of:

1. `SITE INSTANCE WORK` — use the existing Website Creator engine and reusable capabilities.
2. `WEBSITE CREATOR CORE WORK` — add a genuinely missing reusable capability to the shared engine.

Do not create a normal third path consisting of one-off client infrastructure.

## Loading Rule

Do not mass-read the whole project. Load the narrowest standard required by the active task.

Default fresh-chat/new-site path:

`PROJECT.md → PROJECT_STATE.md → OWN_SYSTEM_EXECUTION_STANDARD.md → engine/STATUS.md → SITE_MODEL_STANDARD.md → ROUTER.md → narrow task standards → shared engine → QA/release gates`.

For any shared-engine code change, read `engine/README.md` and `engine/STATUS.md` before implementation.

For any client-facing visual editor task, read `EDITOR_CREATION_STANDARD.md` before implementation.

For any design task, use `../../blocks/design/BLOCK.md` as the design-process authority rather than reconstructing a second design pipeline inside Website Creator.

## No Silent Platform Rule

Do not introduce an external hosted builder, coding sandbox, CMS cloud, deployment platform or new editor architecture merely for convenience.

Check the shared Website Creator engine first. Prefer replaceable open-source/self-hostable building blocks when a core capability is genuinely missing.

An external service may be used only when explicitly selected as an adapter/infrastructure dependency and it does not become the canonical definition of the website.

## Client-Agnostic Rule

Do not route from Website Creator into a client project to obtain required production knowledge. If a reusable fact exists only in a client project, promote/generalize it into Website Creator first.

## Evidence Rule

Do not create extra routing/manifests merely because they might be useful later. Add deeper task manifests only when real routing/context failures prove they are needed.

## Final Rule

Website Creator owns reusable website-production knowledge, execution contracts and the shared engine. Site Instances consume Website Creator. New chats reuse the system; they do not reinvent it.
