# Website Creation — TOOL_DONOR_REGISTRY.md

## Purpose

Website-specific view of tools, platforms, libraries and donors already researched or used across SOFT, Olga Polo, Automatic Website Factory and PEOS Design work.

This is a routing layer, not a substitute for the canonical SOFT inventory or current official documentation.

Status meanings:
- `ADOPTED / PROVEN` — used successfully in our production/workflow.
- `INTERNAL / ACTIVE` — our existing capability/project.
- `STRONG DONOR / CANDIDATE` — researched and promising, not universal default.
- `EXTERNAL / CONDITIONAL` — useful platform/tool; choose task-by-task.
- `HISTORICAL / REVALIDATE` — prior research whose current product facts must be checked before adoption.

## Internal capabilities

### PEOS Design Block — ADOPTED / PROVEN

Canonical: `../../blocks/design/BLOCK.md`

Role: upstream website-design orchestration: business/user goal, donor research, visual selection, page strategy, sections/components, responsive behavior, motion, implementation handoff, Taste execution guidance and final design QA.

### Design Picker — INTERNAL / ACTIVE

Canonical:
https://github.com/oleg3479881328-code/Project-Execution-OS/tree/main/projects/design-picker

Role: import/browse visual donors, choose reusable patterns and export design direction/brief.

### Universal Site Design Extractor — INTERNAL / ACTIVE PROTOTYPE

Status/source:
https://docs.google.com/document/d/1albuaKqO3Dy_rJmXbAPofP89B6R3_NItzH5raYaF7_I/edit

Role: full-site design/structure extraction and normalized artifacts such as `DESIGN.md`, tokens, DTCG/Tailwind/evidence exports. Use for approved donor analysis; do not assume perfect cloning or animation extraction without revalidation.

### Website Intelligence / Site Baseline Scanner — INTERNAL / EXISTING

Role: existing-site qualification/audit and full-site baseline capture. Exact standalone canonical packaging still needs normalization; current evidence lives through Automatic Website Factory and Olga baseline work.

### Olga production stack — ADOPTED / PROVEN DONOR

Repo:
https://github.com/oleg3479881328-code/olga-polo-weddings-web

Role: real production reference for structured data, reusable renderers, Puck authoring, staged release, PR/CI/Vercel, SEO/schema/canonical, live QA and rollback discipline.

### Visitor Analytics Control Plane — INTERNAL / ACTIVE

Canonical:
https://github.com/oleg3479881328-code/Project-Execution-OS/tree/main/projects/visitor-analytics-control-plane

Current architecture selects Umami v3 as default analytics core, PostHog only when deeper product analytics is justified.

## Adopted libraries/patterns from Olga

### Puck — ADOPTED / PROVEN

Role: structured page/block visual authoring layer in Olga editor. Treat it as a proven donor for bounded client-safe authoring, not an automatic requirement for every site.

### react-easy-crop — ADOPTED / PROVEN

Current Olga source:
https://docs.google.com/document/d/1HWHTwXX2KvK-gPUqN3nIrlrh642IeDSWTiVg4vqK9v4/edit

Role: isolated non-destructive image crop/pan/zoom UI outside Puck coordinate transforms. Chosen specifically after custom pointer math caused drift/breakage.

## Design research / Style DNA

### Refero Styles / Refero MCP — STRONG DONOR / CANDIDATE

Official:
https://styles.refero.design/
https://refero.design/mcp

Role: visual research, real product screens/flows, style-system references, DESIGN.md/tokens. Current SOFT decision: benchmark as design intelligence before expanding custom tooling; do not make paid MCP mandatory. Revalidate current pricing/limits.

### Framer — STRONG DONOR / CANDIDATE

Durable note:
https://docs.google.com/document/d/19iKp-YMkOq6Ac3nYmmhvCuLqD3o5_9HLbdBEkiUoy-M/edit

Role: premium website/design/motion donor, rapid demos, interaction DNA, possible factory execution option. Compare against custom-code/Vercel and revalidate lock-in/pricing before adoption.

### UX-UI Agent Skills (plugin87) — STRONG DONOR / CANDIDATE FIRST-CLASS DESIGN-ENGINEERING TOOL

SOFT review:
https://docs.google.com/document/d/1fvthph93xy6TcnQ7WMGSvsc2YUK6VdIrplDYjnQX6U0/edit

Official repo:
https://github.com/plugin87/ux-ui-agent-skills

Decision: do not replace PEOS Design Block and do not wholesale-install at PEOS root. Highest-value donor concepts:
- image-to-code as screenshot -> inferred design language -> tokens -> components -> rendered comparison;
- Primitive -> Semantic -> Component token architecture;
- apply-aesthetic as translation into semantic colors/type/spacing/radius/shadows/motion, not brand cloning;
- deterministic QA for contrast, accessibility, hardcodes, states, responsive behavior, reduced motion, keyboard/focus, overflow;
- redesign sequence `Scan -> Diagnose -> Direct -> Apply -> Verify`;
- framework adapter contracts;
- selective loading of only the required skill/knowledge.

Candidate chain:
`PEOS Design Block -> Existing Solution First -> donor/reference research -> Design Picker -> UX-UI Agent specialist capability -> Codex implementation -> deterministic QA -> PEOS Taste -> Impeccable/manual visual QA -> release`.

### 21st.dev / Magic MCP — STRONG COMPONENT DONOR / CANDIDATE

Role: Existing Solution First discovery for already-solved frontend components/patterns before custom generation. Normalize selected patterns into project tokens/requirements and still run accessibility/design QA.

### Impeccable — CANDIDATE FIRST-CLASS FRONTEND QA

Canonical PEOS gate:
`../../blocks/design/IMPECCABLE_DESIGN_QA_GATE.md`

Role: downstream visible frontend/design quality critique and polish. Complements deterministic QA; does not replace it.

### Humanizer — CANDIDATE TEXT QA

Role: optional final editorial QA for public-facing/client-tone copy. Do not frame as guaranteed AI-detector bypass.

### Ready-made component/design donors already reviewed

Automatic Website Factory / PEOS research has also covered conditional donors such as shadcn/ui, coss ui, Beautiful UI, beUI, Rare UI and Transitions.dev. These are candidates, not universal dependencies; check compatibility, license, accessibility and performance before use.

## Website execution / provisioning platforms

### Vercel — ADOPTED / PROVEN

Role: current production/preview deployment for Olga code-based pages; immutable deployments and Instant Rollback are part of the proven release model.

### Netlify — EXTERNAL / CONDITIONAL

Role: deployment/CDN/functions alternative. Historical Drive duplicates exist; use SOFT canonicalization before relying on old notes.

### Showit — ADOPTED IN OLGA / CONDITIONAL ELSEWHERE

Role: Olga premium human-facing site during MVP while programmatic Next.js pages were safely isolated on Vercel. Strong donor for visual workflow and staged migration architecture, not a universal factory backend.

### WordPress — EXTERNAL / CONDITIONAL

Role: CMS ecosystem / ownership-friendly execution path. Current usage decision depends on project requirements; 10Web research is one managed AI/white-label route.

### Duda — HIGH-PRIORITY FACTORY CANDIDATE

Automatic Website Factory donor analysis:
https://docs.google.com/document/d/1KVTz8XyZfwMN2rILqeiOkqaSHGDIsyT3AR2WIrQEIuM/edit

Previously verified strengths: AI/site generation APIs, template/Instant Website paths, client accounts and granular/content-only permissions, white-label editor/preview/access. Revalidate current API/pricing/ownership rules at execution time.

### 10Web — HIGH-PRIORITY FACTORY CANDIDATE

Same donor analysis above. Previously verified strengths: AI site generation API/WordPress route, sitemap/styles/secondary pages, white-label reseller/client/site/billing infrastructure. Revalidate current product terms before execution.

### FieldLaunch — STRONG PROCESS DONOR

Role: end-to-end Hunt -> Enrich -> Generate -> Deploy -> Outreach process and preview-first sales sequencing.

### LeadX — STRONG ACQUISITION DONOR

Role: prospect discovery, no-site/weak-site scoring, acquisition control plane and CRM/webhook workflow.

### Devonz — EXTERNAL / DONOR

Role: full-stack vibe-coding platform saved for comparison; not selected as default.

### Bolt.diy / Bolt.new family — EXTERNAL / DONOR

Role: AI web-app generation references; not selected as canonical production workflow.

## Research / extraction / implementation support

### Firecrawl — RECOMMENDED ON-DEMAND EXTRACTION LAYER

Role: external website search/scrape/crawl/extract when ordinary web access or project files are insufficient. Choose CLI/skill/MCP based on task and token/runtime needs.

### Playwright CLI / MCP — RECOMMENDED QA-BROWSER LAYER

Role: deterministic live UI/browser verification, forms/flows/regressions and accessibility-snapshot interaction. Prefer the smallest adequate interface; persistent MCP is not mandatory for every test.

### Context7 — RECOMMENDED CURRENT-DOCS LAYER

Role: current/version-specific framework/library/API documentation to reduce stale implementation assumptions. It is not a replacement for code review or business reasoning.

### Codex — ADOPTED EXECUTION TOOL

Role: code implementation/review within our Git/PEOS workflow when the task is sufficiently specified.

## Analytics / validation

### Google Search Console — ADOPTED / PROVEN FOR SEARCH VALIDATION

Olga evidence demonstrates its role in indexation, canonical diagnostics, query/page/impression/click monitoring.

### GA4 / GTM — CONDITIONAL MEASUREMENT LAYER

Used/planned where conversion/search attribution requires it. Olga TSEO architecture defines candidate inquiry events.

### Umami v3 — SELECTED DEFAULT ANALYTICS CORE FOR INTERNAL CONTROL PLANE

Use for privacy-conscious cross-project analytics when the Visitor Analytics Control Plane is deployed.

### PostHog — ESCALATION OPTION

Use only when deeper product analytics/experimentation justifies the additional system.

## Current selection rule

Do not ask “which website builder do we use?” in the abstract.

Route by project need:
1. define business/user goal and required ownership/editing model;
2. check existing project stack and proven Olga patterns;
3. search PEOS Design/Website Creation/SOFT before inventing;
4. use ready-made platform/component/library when it satisfies quality/control/ownership/economics;
5. custom-build only the verified gaps;
6. run deterministic + visual + live QA before release.

## Canonical software source

SOFT Master Software Inventory:
https://docs.google.com/document/d/1yTWfazVPhs-AWdSsvS4Q6xyNd7bXKtqi6EvrmQMdAOk/edit

SOFT Third-Party Software Index:
https://docs.google.com/document/d/1C-F_ukN2AlryP-_FxlJqFIKSbKjat8kzzMw8HsaSPH0/edit

Time-sensitive third-party claims in this file are routing context only and must be revalidated against current official sources when making an adoption/purchase/implementation decision.