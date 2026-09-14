# Website Creator — Independent Speed & Ready-Solutions Review

Date: 2026-09-14
Status: REVIEW ONLY — no architecture changes applied by this document

## Executive conclusion

Website Creator is not slow because research, design quality, SEO, or QA are inherently too expensive. It is slow because the current operating flow still defaults too often to **assembling a custom website production stack** when the task is a normal marketing/local-business website that modern 2026 platforms can produce, edit, host, version and publish inside one environment.

The current system is strong as a **knowledge/control plane**. It is weak as a **speed-optimized execution selector**.

The main operational problem is that platform choice happens too late and the design/build/editor/deploy steps are treated as separate engineering work even when a ready-made platform already combines them.

## Real-case evidence: Car Service Garage

The current Car Service Garage experiment is a strong production diagnostic.

Connected Vercel account evidence on 2026-09-14 shows:

- main project `car-service-garage-ohio` created 2026-09-13 20:39 UTC;
- 12 production deployments on the main project within roughly 18 hours, including one failed deployment;
- a separate `car-service-garage-olga-editor` project;
- numerous `csg-*probe`, schema, binary, base64, path, redeploy, toolbar and shape-test projects created to investigate deployment/tool behavior;
- about 20 Car-Service-Garage-related Vercel projects visible in the workspace during the review.

This is not primarily website creation. It is **tooling/integration debugging performed inside the hosting layer**.

The site itself is already a relatively conventional local-business marketing site: hero, service sections, process, CTA, contact/directions, responsive assets and basic SEO. The implementation path became disproportionately complex because the workflow also tried to reconstruct a custom editor and solve deployment-format/tool-transport issues.

## Root causes

### 1. No early execution-lane decision

Website Creator currently has a global production pipeline, but does not force a rapid decision between:

- ready-made visual builder;
- managed CMS/visual editor;
- code-generating AI platform;
- factory/white-label platform;
- truly custom build.

As a result, agents can enter design and implementation before deciding whether most of that implementation should exist at all.

### 2. Ready Site Stacks are custom-code biased

The current PEOS `READY_SITE_STACKS.md` still frames most site types as React/Vite/Next.js/Astro + hosting/CMS combinations.

That was a reasonable reusable-stack catalogue, but it is no longer a complete 2026 Existing-Solution-First decision layer. It omits the current generation of integrated AI website execution systems.

### 3. The Design Block is too deep for every site

The Design Block is strong for premium and ambiguous design work, but its full chain is excessive for a straightforward local-business site when the owner already supplied a design reference.

The system needs variable depth:

- express visual match;
- normal design pass;
- full research/donor/design-system pass.

The current text says not to load everything, but the required design chain is still long enough to encourage over-processing.

### 4. Custom editor work begins too early

The universal editor behavioral contract is useful. The operational mistake is treating that contract as a reason to implement a new editor for every site.

For normal client sites the default should be:

`use platform-native editor first -> map Website Creator acceptance requirements -> custom-build only missing behavior`.

### 5. Vercel is being used as a development laboratory

Vercel should normally receive a stable repo/build or a deliberate preview deployment. It should not be the primary environment for probing binary transport, file schemas, base64 packaging, path handling and editor experiments.

A single website should normally have:

- one canonical source workspace/repo;
- local or platform preview loop;
- one deployment project;
- preview/staging deployments;
- production only after the build passes.

### 6. Architect and executor are conflated

ChatGPT/PEOS is good at research, product decisions, standards, acceptance criteria and orchestration.

It should not be forced to manually reconstruct a development environment through hosting/API calls when a purpose-built coding/site agent can execute the build directly.

### 7. No speed SLO

Website Creator measures quality categories but has no hard time target for common site classes. Without a time budget, every useful check can expand indefinitely.

## Recommended new operating model

### Step 0 — classify the job

Before sitemap/wireframe/code, choose one lane.

#### EXPRESS

Use for normal local-business, portfolio, brochure and simple marketing sites.

Target: credible live preview in <= 60 minutes.

Default platform candidates:
- Relume Publish;
- Framer;
- Wix Harmony / Wix Studio;
- B12;
- Webflow AI where its workflow is a fit.

No custom editor. No custom deployment stack unless a requirement forces it.

#### CONTROLLED / PREMIUM MARKETING

Use when design quality, CMS structure, interactions or editorial control matter more than absolute speed.

Target: strong first preview in 1–3 hours.

Candidates:
- Framer;
- Webflow;
- Storyblok or Sanity + custom frontend;
- Builder.io when its visual/content model fits.

#### CODE-OWNED

Use only when source ownership, custom behavior, backend logic, complex integrations or portability justify code.

Candidates:
- v0 + Vercel;
- Replit Agent;
- Lovable;
- Bolt;
- Codex in a real repo/workspace.

A managed CMS/editor should still be preferred to a custom editor unless the editor itself is product IP.

#### FACTORY / WHITE-LABEL

Use for repeated production at scale.

Candidates:
- Duda;
- 10Web;
- other validated white-label platforms.

The proprietary layer should stay in research, qualification, dossier, design intelligence, content orchestration, QA and sales workflow — not generic hosting/editor/account infrastructure.

## Highest-priority ready-made solution findings

### Relume Publish — highest-priority immediate test

Current official documentation shows one continuous product flow:

`Brief -> Sitemap -> Wireframe -> Design -> Publish`

The Brief can ingest files, PDFs, brand guidelines, client call recordings or a URL. Relume then generates structure, wireframes and design, hosts the live site, includes roles/permissions, domain/discoverability/tracking/forms settings, analytics and continuing AI agents.

This overlaps heavily with Website Creator's current multi-tool pipeline and is therefore the strongest immediate benchmark for reducing production time.

### Framer 3.0 / Agents — promote from donor to execution candidate

Current Framer AI works directly on the canvas, generates editable pages/sections/copy/visuals, manages CMS, can build code components, review SEO/accessibility, uses branching/staging, hosts and publishes, and can connect external agents such as Codex.

For premium local-business and visual marketing sites this now covers a large part of our custom workflow.

### Webflow AI — serious execution candidate

Current Webflow AI Site Builder can generate a professional multi-page site in minutes, while Webflow AI can modify designs, generate sections/copy/code and assist SEO/AEO. Strong fit where visual CMS and structured marketing content matter.

### Wix Harmony / Wix Studio — serious local-business/agency candidate

Wix Harmony (2026) uses Aria to generate sites from business/style input. Wix Studio adds agency/client management, responsive controls, CMS/business solutions, roles/permissions, custom code and GitHub integration.

This deserves an execution benchmark, not only generic-builder status.

### B12 3.0 — speed benchmark for local service businesses

B12's current product claims a full first draft in about two minutes, with chat editing, visual editing, code editing, automatic version history and built-in business tools. It is particularly relevant as a speed benchmark for a garage/service-business use case.

### v0 / Replit / Lovable / Bolt — code-generation lane

These tools have moved beyond mockups into hosted/deployable websites and apps. For code-owned sites they are faster starting environments than manually scaffolding through PEOS + deployment APIs.

v0's own current training demonstrates a real website with database, email, custom domain and GitHub backup in under 20 minutes; this is not a quality guarantee, but it is a useful benchmark for our execution latency.

### Storyblok / Sanity / Builder.io — editor/CMS layer

If a custom-coded frontend is required, these should be evaluated before building visual CMS/editor infrastructure. They already provide live preview/click-to-edit/drag-and-drop or visual block editing and content workflows.

### Playwright — deterministic QA default

Use Playwright before deployment for interaction, responsive, link, form and browser checks. Vercel should not be used to discover errors that can be caught locally or in preview.

## Proposed fast production chain

For ordinary sites:

`INPUT / BUSINESS DOSSIER`
-> `EXECUTION LANE SELECT (<= 5 min)`
-> `FIRST VISUAL PREVIEW`
-> `OWNER VISUAL APPROVAL`
-> `CONTENT / MEDIA / SEO FILL`
-> `DETERMINISTIC QA`
-> `LIVE PREVIEW`
-> `PUBLISH`

Do not automatically insert wireframe, detailed frontend handoff, custom editor, custom renderer and multiple deployment experiments when the selected platform already owns those layers.

## Design approval gate

The Car Service Garage case also shows that implementation started before the visual direction was sufficiently locked.

For owner-facing sites, create a narrow approval gate before full production:

- one real homepage/hero direction;
- 2–3 representative sections;
- desktop and mobile indication;
- real or approved placeholder media;
- owner says GO / CHANGE.

Only after GO should the system build the whole site/editor/content stack.

## Speed targets to test

These are experimental SLOs, not promises:

- local-business Express first credible preview: <= 60 min;
- premium marketing first strong preview: <= 3 h;
- code-owned first functional preview: <= 2 h;
- editor/CMS: native platform editor by default; custom-editor work has its own separate project budget;
- QA + production publish after accepted preview: <= 30 min for simple sites.

Track actual wall-clock by phase and revise targets from evidence.

## Immediate recommendation for Car Service Garage

Do not continue using the current site as the main architecture experiment.

Preserve it as evidence/reference and run an identical-input benchmark using the same business facts and design reference through three ready-made lanes:

1. Relume Publish — integrated brief-to-live path;
2. Framer Agents — design-led editable path;
3. v0 or Replit — code-owned AI execution path.

Optionally use B12 as a fourth speed baseline.

Measure:
- time to first credible preview;
- visual quality;
- mobile quality;
- editor usability;
- SEO control;
- ability to use real images/content;
- custom-domain/ownership path;
- export/lock-in;
- time to make 5 owner-requested changes;
- total human intervention.

Do not choose a winner from vendor claims. Use the benchmark.

## Architecture verdict

Keep:
- Website Creator as global knowledge/control plane;
- No Client Dependency rule;
- Site Model direction for reusable execution;
- Design Block for deep work;
- editor behavior contract;
- release/QA discipline.

Change operationally:
- platform decision must happen before deep design/implementation;
- add Express/Controlled/Code-Owned/Factory lanes;
- make ready-made execution the default for ordinary sites;
- demote custom editor from default deliverable to exceptional requirement;
- stop deployment-layer probing;
- route code execution to a real coding/site environment;
- require visual approval before full build;
- measure wall-clock speed.

## Final conclusion

The system does **not** need fewer standards. It needs a much faster decision that says **which standards are not needed for this site because a ready-made platform already implements them**.

The Car Service Garage delay is therefore primarily an execution-architecture problem, not a design-quality problem.
