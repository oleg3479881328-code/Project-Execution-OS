# Website Creator — TOOL_DONOR_REGISTRY.md

## Purpose

Global website-specific view of reusable internal tools, external platforms, libraries and design/process donors.

This registry is client-agnostic. Time-sensitive third-party facts must be revalidated against current official documentation at adoption time.

## Validation Rule

For any adoption decision that depends on current pricing, API behavior, licensing, export, ownership, permissions, hosting or product features:

- record the source/date of the validation in the decision artifact;
- revalidate when the decision is actually executed or materially revisited;
- do not promote a research claim directly into a permanent default.

Status meanings:
- `ADOPTED / PROVEN` — successfully used/validated in our production methodology.
- `INTERNAL / ACTIVE` — our reusable capability/project.
- `STRONG DONOR / CANDIDATE` — researched and promising, not a universal default.
- `EXTERNAL / CONDITIONAL` — choose project-by-project.
- `RESEARCH CANDIDATE` — added to a comparison set; current official capabilities still require direct validation before adoption.

## Internal Capabilities

### PEOS Design Block — ADOPTED / PROVEN
Canonical: `../../blocks/design/BLOCK.md`
Role: single website-design orchestration authority for donor research, page strategy, sections/components, responsive/motion standards, implementation handoff and design QA.

### Design Picker — INTERNAL / ACTIVE
Canonical: https://github.com/oleg3479881328-code/Project-Execution-OS/tree/main/projects/design-picker
Role: collect/import visual references, select reusable patterns, produce design direction/brief.

### Universal Site Design Extractor — INTERNAL / ACTIVE PROTOTYPE
Role: extract site structure/design evidence into reusable artifacts such as design notes/tokens/evidence exports. Use after donor selection and normalize results into the target design system. Do not assume pixel-perfect cloning or universal animation/framework extraction unless current tests prove it.

### Website Intelligence / Site Baseline Scanner — INTERNAL / EXISTING
Role: inspect/qualify an existing website and capture a baseline before redesign/replacement. Standalone packaging remains subject to normalization.

### Visitor Analytics Control Plane — INTERNAL / ACTIVE
Canonical: https://github.com/oleg3479881328-code/Project-Execution-OS/tree/main/projects/visitor-analytics-control-plane
Role: reusable analytics/control layer; current internal direction favors a lightweight default with deeper product analytics only when justified.

## Visual Editor / CMS Technologies

The Universal Visual Editor contract is canonical. Tool choice is an implementation decision.

Before major new implementation-specific editor infrastructure, compare the strongest internal and external options against the same `EDITOR_CREATION_STANDARD.md` acceptance criteria.

### Puck — PROVEN IMPLEMENTATION OPTION / DEFAULT DECISION PENDING
Role: structured React page/block authoring surface suitable for bounded visual editing. It is a proven implementation option that can satisfy parts of `EDITOR_CREATION_STANDARD.md`, but it is not a universal default until build-vs-buy/adapt comparison is recorded.

### react-easy-crop — PROVEN IMPLEMENTATION OPTION
Role: visual, non-destructive crop/move/zoom interaction in an isolated overlay/modal. Preferred over custom pointer-coordinate crop math when using compatible React stacks.

### react-moveable — PROVEN IMPLEMENTATION OPTION
Role: direct resize handles for supported visual blocks; persist semantic percentage/layout values rather than editor-only pixels.

### Storyblok — RESEARCH CANDIDATE
Role: external visual/headless CMS candidate for the editor build-vs-buy comparison. Validate current visual editing, structured content, permissions, versioning, image handling, export/ownership, pricing and integration behavior from official sources before scoring.

### Sanity Visual Editing — RESEARCH CANDIDATE
Role: external structured-content + visual editing candidate. Validate current visual editing workflow, schema ownership, preview/editor integration, permissions, versioning, media and pricing from official sources before scoring.

### Builder.io — RESEARCH CANDIDATE
Role: external visual builder/CMS candidate, especially relevant where high-volume marketing/page composition matters. Validate current framework integration, content model, permissions, export/ownership, experimentation and pricing before scoring.

### WordPress — EXTERNAL / CONDITIONAL
Role: mature CMS/ownership ecosystem where WordPress editing/plugin/deployment requirements fit the project.

## Design / Style / Component Donors

### Refero Styles / Refero MCP — STRONG DONOR / CANDIDATE
Official: https://styles.refero.design/ and https://refero.design/mcp
Role: design research, real product screens/flows, style-system references and token/design-language intelligence. Revalidate current access/pricing/limits.

### Framer — STRONG DONOR / CANDIDATE
Role: premium visual website builder, rapid demo surface, layout/motion/interaction donor and possible execution platform. Evaluate lock-in, export/ownership, CMS, hosting and cost per project.

### UX-UI Agent Skills — STRONG DONOR / CANDIDATE
Official: https://github.com/plugin87/ux-ui-agent-skills
Useful concepts:
- image/screenshot → inferred design language → tokens → components → rendered comparison;
- Primitive → Semantic → Component token architecture;
- aesthetic translation rather than brand pixel cloning;
- deterministic contrast/a11y/state/responsive QA;
- redesign sequence `Scan → Diagnose → Direct → Apply → Verify`;
- framework adapters;
- selective loading of only needed design knowledge.

Use as a specialist layer under PEOS/Website Creator orchestration, not as the master project authority.

### 21st.dev / Magic MCP — STRONG COMPONENT DONOR / CANDIDATE
Role: Existing Solution First component/pattern discovery before custom generation. Normalize selected components into project tokens/requirements and still run accessibility/design QA.

### Impeccable — CANDIDATE FRONTEND QA
Canonical PEOS gate: `../../blocks/design/IMPECCABLE_DESIGN_QA_GATE.md`
Role: downstream visible frontend/design critique and polish. Complements deterministic QA.

### Humanizer — CANDIDATE TEXT QA
Role: optional editorial pass for public-facing/client-tone copy. Do not frame as guaranteed detector bypass.

### Conditional component/motion donors
Research has included ecosystems such as shadcn/ui, coss ui, Beautiful UI, beUI, Rare UI and Transitions.dev. Evaluate compatibility, license, accessibility and performance before use.

## Hosting / Deployment / Site Platforms

### Vercel — ADOPTED / PROVEN OPTION
Role: code-based preview/production deployment, immutable deployments and rollback-friendly workflow. Use when compatible with the chosen stack.

### Netlify — EXTERNAL / CONDITIONAL
Role: deployment/CDN/functions alternative. Revalidate current pricing/features before adoption.

### Showit — EXTERNAL / CONDITIONAL
Role: high-control visual website platform; useful where its visual workflow and CMS model match the project. Not a universal backend.

### Duda — HIGH-PRIORITY FACTORY CANDIDATE
Role: factory execution candidate for generated/template sites, client editing/permissions, preview/provisioning and white-label workflows where current capabilities satisfy requirements. Revalidate current API/MCP/pricing/export/ownership/permission behavior from official sources before testing.

### 10Web — HIGH-PRIORITY FACTORY CANDIDATE
Role: managed AI/WordPress site generation and white-label/reseller/client infrastructure where an ownership-friendly WordPress path is useful. Revalidate current APIs/terms/pricing before testing.

### B12 — RESEARCH FACTORY CANDIDATE
Role: additional service-business/factory comparison candidate surfaced by the 2026-09-13 independent review. Do not assume fit or current capabilities; verify official product, ownership/editor/automation/pricing behavior before inclusion in an identical-input test.

### FieldLaunch — STRONG PROCESS DONOR
Role: end-to-end acquisition-to-preview process patterns such as Hunt → Enrich → Generate → Deploy → Outreach.

### LeadX — STRONG ACQUISITION DONOR
Role: prospect discovery, no-site/weak-site scoring and CRM/webhook acquisition-control patterns.

### Devonz — EXTERNAL / DONOR
Role: full-stack AI/vibe-coding platform reference; not a default.

### Bolt.diy / Bolt.new family — EXTERNAL / DONOR
Role: AI web-app/site generation references; not canonical production infrastructure.

## Research / Extraction / Implementation Support

### Firecrawl — RECOMMENDED ON-DEMAND EXTRACTION LAYER
Role: external site search/scrape/crawl/extract when normal web access or known evidence is insufficient. Select CLI/agent skill/MCP based on task/runtime efficiency.

### Playwright CLI / MCP — ADOPTED DEFAULT QA-BROWSER LAYER
Role: deterministic live UI verification, forms, interaction flows, regressions, responsive checks and accessibility-snapshot automation. Use the lightest interface that meets the task.

This is the default browser automation direction for Website Creator QA where browser-level validation is applicable; it does not replace human visual/taste review.

### Percy — EXTERNAL / CONDITIONAL VISUAL REGRESSION CANDIDATE
Role: screenshot-baseline/diff workflow when a project needs managed visual regression. Validate current integration/pricing before adoption.

### Chromatic — EXTERNAL / CONDITIONAL VISUAL REGRESSION CANDIDATE
Role: component/story-based visual regression and review when a component catalogue/workflow justifies it. Validate current integration/pricing before adoption.

### Context7 — RECOMMENDED CURRENT-DOCS LAYER
Role: current/version-specific framework/library/API documentation to reduce stale implementation assumptions.

### Codex — ADOPTED EXECUTION TOOL
Role: code implementation/review after Website Creator has established requirements and acceptance criteria. Executor, not product/design authority.

## Analytics / Validation

### Google Search Console — ADOPTED / PROVEN
Role: indexing, canonical diagnostics, query/page/impression/click validation.

### GA4 / GTM — EXTERNAL / CONDITIONAL
Role: conversion/event attribution when the project requires it.

### Umami — SELECTED LIGHTWEIGHT INTERNAL DIRECTION
Role: privacy-conscious analytics core for reusable cross-project analytics where deployed.

### PostHog — ESCALATION OPTION
Role: deeper product analytics/experimentation only when justified.

## Editor Comparison Rule

For a real editor build-vs-buy/adapt spike, use one representative site/page set and score each option against at least:

1. Website Creator behavioral editor acceptance contract;
2. structured content/Site Model compatibility;
3. image crop/move/zoom and media handling;
4. draft/version/history/rollback;
5. permissions/client isolation;
6. preview/public-render parity;
7. SEO/control surface;
8. integration/API quality;
9. ownership/export/lock-in;
10. implementation and recurring cost;
11. migration/recovery risk.

Do not select a winner from documentation alone.

## Factory Comparison Rule

Use the same verified business dossier/Site Model input across candidate platforms where possible.

Record:
- output quality;
- generation/provisioning time;
- editor usability;
- permissions;
- ownership/export/domain transfer;
- hosting/deployment behavior;
- API/automation surface;
- per-preview/per-live-site cost;
- support/maintenance burden;
- lock-in and recovery path.

No platform is the Website Factory default until real evidence is captured.

## Selection Rule

Do not ask “which website builder is best?” without a project contract.

Evaluate tools/platforms against:

1. business/user goal;
2. design quality/control;
3. structured content/data requirements;
4. editing/permission model;
5. SEO/schema/canonical control;
6. preview/release/rollback workflow;
7. ownership/export/domain transfer;
8. API/integration quality;
9. performance/accessibility;
10. cost and time per delivered site;
11. maintenance and lock-in.

Prefer integration over rebuilding solved infrastructure. Custom-build only the demonstrated gap.

## Final Rule

Tools serve Website Creator standards. A tool or external donor does not become the architecture merely because it is convenient, fashionable, already known, or recommended by a review.

### Dramaturg / playwright-repl + Stagecraft — STRONG DONOR / ACTIVE EVALUATION
Official: https://github.com/stevez/playwright-repl

Role: primary current candidate for real authenticated-Chrome automation and reusable browser/editor skills.

Relevant current capabilities include Playwright execution in the real browser session, `.pw` keyword scripts, JavaScript fallback, recorder, picker, snapshot, run/step/editor surfaces, relay/MCP/HTTP paths, and Stagecraft reusable `SKILL.md` + `.pw`/`.js` skills with variables and replay.

Website Creator decision 2026-09-21:
- prefer PW-first automation for linear editor work;
- use Stagecraft before inventing a custom brick runtime;
- do not fork/rebuild the browser engine first;
- build only the missing capture/normalization/editor-adapter/control layer after a real proof.

Architecture:
`UNIVERSAL_WEBSITE_TRANSLATOR_ARCHITECTURE.md`

Detailed durable note:
https://docs.google.com/document/d/1RmTaj0rH7J-VV3mTgOJRl_J09rs5J8UI6L0HuKH3H6k/edit
