# Project Execution OS — Tool & Stack Audit

## Purpose

Single at-a-glance inventory of the tools, platforms, storage layers, editors, runtimes and operational services currently used across the owner's projects.

This is an inventory and routing aid, not a requirement to use every tool in every project.

## Status Legend

- `CORE` — system-wide default / foundational layer.
- `ACTIVE` — actively used and proven in at least one current workflow.
- `PROJECT-SPECIFIC` — valid active tool, but only where that project's architecture needs it.
- `CANDIDATE` — researched or approved direction, but not yet a universal/default dependency.
- `LEGACY` — existing historical dependency or migration source; avoid for new architecture unless explicitly required.

## 1. AI / Execution Layer

| Tool | Status | Primary role | Notes |
| --- | --- | --- | --- |
| ChatGPT | CORE | coordination, research, review, connected-app work, project orchestration | Human-facing control surface for Project Execution OS workflows. |
| OpenAI Codex | ACTIVE | code execution / implementation handoff | Use after task is sufficiently defined; governed by Codex handoff standards. |
| GitHub | CORE | source code, project standards, issues, PRs, durable technical state | Canonical code/repository layer. |
| VS Code | ACTIVE | local development environment | Primary local code editor in current development workflow. |

## 2. Web Application Stack

| Tool / technology | Status | Primary role | Notes |
| --- | --- | --- | --- |
| Next.js App Router | CORE for shared web family | web application framework | Proven common baseline for Olga/Tusia family. |
| React | CORE for shared web family | UI runtime | Underlying UI layer for Next.js projects. |
| TypeScript | CORE for shared web family | typed application code | Proven baseline in shared web architecture. |
| Vercel | CORE for shared web family | deployment / hosting / preview environments | Independent client deployment lifecycle. |
| Puck | ACTIVE | constrained visual editor / client CMS surface | Proven in Olga; family target is branded Puck with controlled client-facing blocks. Do not retrofit stable editors without need. |
| shadcn/ui | CANDIDATE / preferred component source where appropriate | editable component primitives | Use under Existing Solution First; not mandatory for every project. |
| Tailwind CSS | PROJECT-SPECIFIC | styling layer | Preserve when existing project uses it; do not force migration solely for convention. |

## 3. Design / UI Quality Layer

| Tool / system | Status | Primary role | Notes |
| --- | --- | --- | --- |
| Project Execution OS Design Block | CORE | design routing, design-system rules, frontend execution standards | Canonical internal design layer. |
| Taste Frontend Execution Standard | ACTIVE / bounded | anti-generic frontend execution guidance | Use by surface/mode; not a universal visual style. |
| Impeccable Design QA Gate | ACTIVE standard / integration-dependent | post-implementation UI quality review | Separate quality gate from generation-time design guidance. |
| Vercel Web Interface Guidelines | CANDIDATE | UX/accessibility/interface review | Strong review source; not yet treated as universal runtime dependency. |
| Puck component library | ACTIVE pattern | safe visual composition from approved components | Client edits composition/content without owning unrestricted CSS/layout internals. |

## 4. Durable Storage / Knowledge / Data Layer

Current approved architecture:

```text
Google Drive -> Google Sheets -> automation / API -> Notion + websites + graphs + other consumers
```

| Tool | Status | Primary role | Canonical boundary |
| --- | --- | --- | --- |
| Google Drive | CORE | durable files, PDFs, photos, video, DOCX, exports, archives, raw source packages | Primary heavy/binary durable storage. |
| Google Docs | CORE | durable human-readable project protocols, handoffs, working documents | Use for living documents where collaborative document editing is useful. |
| Google Sheets | CORE | structured operational datasets | Default current master for entities, contacts, URLs, SEO data, crawl/enrichment results when spreadsheet scale is appropriate. |
| Notion | ACTIVE | human-facing project/knowledge interface | Project pages, dashboards, decisions, research summaries, curated cards; not universal bulk storage or runtime DB. |
| PostgreSQL / Supabase-class database | CANDIDATE / scale trigger | future structured runtime database | Adopt when Sheets is no longer suitable for volume, concurrency, relations, integrity or runtime query needs. |

## 5. Automation / Integration Layer

| Tool | Status | Primary role | Notes |
| --- | --- | --- | --- |
| n8n | ACTIVE | workflow automation / cross-service orchestration | Approved option for syncing, transformation and publishing workflows. |
| Google Apps Script | ACTIVE option | Google Workspace-native automation | Prefer when the workflow is primarily inside Google Workspace and does not need a larger orchestrator. |
| APIs / webhooks | CORE pattern | service-to-service integration | Prefer direct supported integrations before custom workarounds. |
| MCP / connected app integrations | ACTIVE | agent access to external systems | Use supported connected tools where available instead of manual copying. |

## 6. Website / CMS / Client-Site Platforms

| Tool | Status | Primary role | Notes |
| --- | --- | --- | --- |
| Showit | PROJECT-SPECIFIC / ACTIVE | main photographer marketing-site visual CMS | Active where an existing client site is already built around Showit; not the default for programmatic entity layers. |
| WordPress | PROJECT-SPECIFIC / ACTIVE | blog/content layer behind some Showit setups | Treat hosting/SEO/plugin behavior separately from Showit canvas behavior. |
| Wix | LEGACY | migration source / historical client CMS | Preserve SEO equity and URLs during migration; do not choose as new default without a fresh decision. |
| Puck + Next.js + Vercel | ACTIVE / preferred reusable pattern | controlled client-editable programmatic sites | Current proven family direction for constrained visual editing. |

## 7. SEO / Analytics / Visibility Layer

| Tool | Status | Primary role | Notes |
| --- | --- | --- | --- |
| Google Search Console | ACTIVE | indexing, sitemap, canonical/search diagnostics | Search reality source. |
| Google Analytics | ACTIVE / project-specific | traffic analytics | Use where installed and configured. |
| Microsoft Clarity | ACTIVE / project-specific | behavioral analytics / recordings / heatmaps | Proven installed in current web work. |
| Cloudflare | PROJECT-SPECIFIC / ACTIVE | DNS/CDN/security/robots-side behavior depending on architecture | Do not assume a behavior originates in the site builder when CDN/hosting can inject it. |
| Structured data / JSON-LD | ACTIVE pattern | machine-readable entity/site semantics | Implementation technique, not a SaaS dependency. |

## 8. Research / Extraction / Media Utilities

| Tool | Status | Primary role | Notes |
| --- | --- | --- | --- |
| Web search / public web research | CORE | Existing Solution First, verification, current-source research | Prefer primary/official sources, then strong independent evidence. |
| ScrapeGraphAI / similar extraction tooling | CANDIDATE / project-specific | structured web/entity extraction | Useful for graph/enrichment workflows; validate output and provenance. |
| Archify | CANDIDATE | verified interactive architecture/workflow/sequence/data-flow/lifecycle maps | Existing Solution First candidate for architecture visualization/evidence. Pilot on Project Execution OS is Issue #132; canonical note: `docs/integrations/archify/README.md`. Do not treat diagrams as canonical state or register Archify as an internal capability until a separate verified contract exists. |
| yt-dlp | ACTIVE in video workflows | media acquisition where permitted | Routed through Video Production block. |
| FFmpeg | ACTIVE in video workflows | media transform/probe/edit automation | Reusable media capability. |
| Local Python | ACTIVE | scripting, processing, analysis, utilities | Project-local virtual environments preferred. |
| Ollama / local models | PROJECT-SPECIFIC | local inference / coding experiments | Use when workload and machine capacity make sense. |

## 9. Communication / Work Coordination

| Tool | Status | Primary role | Notes |
| --- | --- | --- | --- |
| GitHub Issues / PRs | ACTIVE | executable development tasks, review, code discussion | Best fit for code-bound execution. |
| Google Docs | ACTIVE | cross-agent handoffs, detailed task/result documents | Especially useful when a durable shared workspace is needed. |
| Notion | ACTIVE | project-facing navigation, project/task/research layer | Keep curated rather than mirroring everything. |
| Gmail | ACTIVE integration | email intake / correspondence workflows | Use connected access when a task depends on email. |
| Google Calendar | ACTIVE integration | events, scheduling, reminders | Use for explicit calendar operations. |

## 10. Current Proven Web Platform Combination

For new controlled React/Next.js client-editable web projects, the strongest currently proven internal pattern is:

```text
GitHub
  -> Next.js + React + TypeScript
  -> approved design system / component primitives
  -> Puck constrained visual editor when client editing is needed
  -> Vercel deploy / preview / production
  -> analytics + search verification as required

Durable project/data side:
Google Drive + Google Docs + Google Sheets
  -> automation/API (n8n / Apps Script / direct integrations)
  -> Notion as human-facing project/knowledge interface
```

This is a pattern, not a forced universal stack. Existing stable project architecture wins unless there is evidence that migration is justified.

## 11. Important Boundaries

1. **GitHub is not general file storage.** Keep code, repository standards and technical state there; heavy project source files belong in Drive or the project's approved durable store.
2. **Notion is not the universal database.** It is the human-facing project/knowledge layer unless a project explicitly makes it canonical for a small bounded dataset.
3. **Google Sheets is not a permanent database.** It is the current default structured layer only while spreadsheet characteristics remain appropriate.
4. **Puck is not mandatory.** It is the proven controlled-editor option for future React/Next.js work when visual client editing is needed. Do not disturb a stable existing editor just to standardize.
5. **Vercel is hosting/deployment, not the whole CMS.** Editorial capability must be supplied by Puck, another CMS, or project-specific tooling.
6. **One project must not silently dictate another project's brand shell.** Shared engine and contracts can be reused; visual identity stays local.
7. **CANDIDATE does not mean installed or adopted.** Research findings must pass compatibility and project-fit review before becoming dependencies.

## 12. Audit Findings

### What is strong today

- Clear separation between code (`GitHub`), files (`Drive`), structured operations (`Sheets`) and human project interface (`Notion`).
- Proven Next.js + TypeScript + Vercel family baseline.
- Proven constrained Puck visual-editor model.
- Existing shared web registry and capability matrix reduce repeated architecture work.
- Automation layer is intentionally plural: n8n, Apps Script, APIs and connected integrations are selected by fit rather than ideology.

### Current weaknesses / cleanup opportunities

- Tool knowledge is still distributed across project state, architecture decisions and domain blocks; this inventory should be updated when major tools are adopted/retired.
- Several researched UI/design tools are candidates but not yet formally ranked by adoption priority.
- Some platform-specific analytics/SEO integrations exist only in individual project records and should not be mistaken for global defaults.
- A future registry may benefit from fields for `owner`, `cost`, `account`, `credential location`, `projects using`, `replacement/exit path`, and `last verified`; credentials themselves must never be stored here.

## 13. Rationalization Audit — Duplicates, Gaps, Decisions

### A. Apparent overlaps that should remain separate

| Pair / group | Decision | Reason |
| --- | --- | --- |
| Google Drive vs GitHub | KEEP BOTH | Drive owns heavy/source files; GitHub owns code and technical state. No true duplication. |
| Google Docs vs Notion | KEEP BOTH, tighten boundary | Docs = living collaborative protocols/handoffs; Notion = navigation, dashboards, curated knowledge. Do not maintain the same canonical prose in both. |
| Google Sheets vs Notion databases | PREFER SHEETS for operational/bulk data | Notion is the human-facing layer. Duplicate only curated subsets with explicit ownership. |
| n8n vs Apps Script | KEEP BOTH, route by scope | Apps Script for Workspace-local/simple workflows; n8n for multi-service orchestration, branching, retries and broader integrations. |
| Puck vs Showit | KEEP BOTH by architecture | Puck is preferred for new controlled React/Next.js editing; Showit stays where an existing visual marketing site depends on it. Do not migrate for uniformity alone. |
| Puck vs shadcn/ui | NOT COMPETITORS | Puck is an editor/composition layer; shadcn is a component source. Approved components may be exposed through Puck. |
| GA vs Clarity | KEEP BOTH when useful | GA answers traffic/acquisition questions; Clarity answers behavioral/session questions. Do not install either without an actual measurement need. |
| ChatGPT vs Codex | KEEP ROLE SEPARATION | ChatGPT coordinates/researches/reviews; Codex executes bounded code work. Avoid using implementation agents as project memory. |

### B. Redundancy to reduce

1. **Canonical project prose duplicated across GitHub, Docs and Notion** — highest information-architecture risk. Every durable artifact should declare one canonical home; other surfaces should link or summarize.
2. **Design guidance proliferation** — Taste, Impeccable, Vercel guidelines and external UI libraries must not become four competing design systems. Internal Design Block remains authority; external tools are generation/review inputs.
3. **Automation choice by habit** — do not start n8n for a two-step Workspace-only task and do not stretch Apps Script into a complex cross-service orchestration engine.
4. **Analytics accumulation** — avoid adding trackers simply because they are available. Each tracker needs a question/KPI owner and an exit path.
5. **CMS multiplication** — no new CMS/editor should be introduced for a new React project until Puck is shown insufficient for the required editing model.

### C. Missing links / gaps

#### GAP-1 — Tool registry metadata
Current inventory names tools but does not yet track `cost`, `account/owner`, `projects using`, `last verified`, `data sensitivity`, `credential location reference`, and `exit/replacement path`.

**Priority: P1.** Add metadata without ever storing secrets themselves.

#### GAP-2 — Database promotion trigger is qualitative
The architecture correctly says Sheets should graduate to PostgreSQL/Supabase-class storage when scale/relations/concurrency demand it, but no measurable promotion gate exists.

**Priority: P1.** Define triggers such as write concurrency, relational integrity requirements, runtime API dependency, query complexity, row growth, and automation contention before choosing a database.

#### GAP-3 — Unified observability
Deployment, workflow, indexing, analytics and automation health are observed in separate products. There is no single operational view answering: `what is broken right now?`

**Priority: P1.** Build a lightweight control-plane/dashboard from existing APIs before buying another observability platform.

#### GAP-4 — Secrets / credential governance
The inventory intentionally does not store credentials, but the system needs a canonical policy for where secrets live, rotation ownership, environment scoping and how agents reference them without copying values into project memory.

**Priority: P0 security/governance.** Existing solution first: prefer platform secret stores / environment management; document references, never secret values.

#### GAP-5 — Backup / restore verification
Drive/GitHub/SaaS persistence is not the same as a tested recovery plan. Critical project state needs explicit recovery ownership and periodic restore evidence.

**Priority: P1.** Define minimum backup/restore checks by data class.

#### GAP-6 — Design system persistence for new sites
The design pipeline has generation and QA standards, but every new site needs a small durable project-local design contract so later agents do not re-invent typography, spacing, radii, components and motion.

**Priority: P1.** Standardize a project-local `DESIGN_SYSTEM.md` or equivalent generated/updated from the approved design direction. Do not retrofit stable projects merely to satisfy the convention.

#### GAP-7 — Automated UI acceptance loop
Impeccable and design standards exist, but a complete repeatable loop should connect rendered viewport screenshots, accessibility/interaction checks, anti-slop/static checks and human approval.

**Priority: P1.** Treat code inspection alone as insufficient evidence of visual quality.

#### GAP-8 — Tool adoption / retirement gate
Candidates can accumulate indefinitely. There is no single explicit promotion rule for tools themselves.

**Priority: P2.** Candidate tool should have: problem solved, existing-solution comparison, integration cost, recurring cost, data/security impact, pilot evidence, owner, rollback/exit path. Retire candidates that never pass a pilot.

### D. Current default stack after rationalization

```text
CONTROL / EXECUTION
ChatGPT -> Codex when bounded implementation is needed

CODE
GitHub -> Next.js / React / TypeScript -> Vercel

DESIGN
Project Execution OS Design Block
  -> existing approved components first
  -> shadcn/ui or other reviewed component source when useful
  -> Puck only when visual client editing is required
  -> rendered UI QA / Impeccable review before acceptance

DATA / KNOWLEDGE
Drive = files
Docs = living collaborative documents
Sheets = current operational structured data
Notion = human-facing navigation / curated knowledge
Postgres/Supabase-class DB = only after promotion trigger

AUTOMATION
Direct supported integration/API first
Apps Script for Google-local workflows
n8n for cross-service orchestration

MEASUREMENT
GSC = search/indexing reality
GA = traffic/acquisition when needed
Clarity = behavior/session evidence when needed
```

### E. Decisions — do now / later / avoid

**DO NOW**
- Preserve current core stack; no migration campaign.
- Add explicit tool metadata and ownership fields to this registry.
- Define secrets-governance and database-promotion gates.
- Make project-local design-system persistence + rendered UI QA the default for future web projects.
- Design a lightweight unified operational dashboard from existing sources.

**DO LATER, ON TRIGGER**
- Adopt PostgreSQL/Supabase-class backend when Sheets crosses a defined suitability threshold.
- Add specialized component/UI libraries only after a project-specific need and compatibility review.
- Replace project-specific legacy CMS only when business/technical evidence justifies migration.

**AVOID**
- Rebuilding stable Olga/Puck editor merely to standardize it.
- Moving all project knowledge into one SaaS.
- Installing every researched design library.
- Duplicating the same canonical data across Sheets and Notion without field ownership.
- Adding another automation platform while n8n/Apps Script/direct APIs cover the requirement.
- Treating Vercel, Puck or Notion as universal answers outside their boundaries.

## 14. Maintenance Rule

Update this inventory when any of these occur:

- a new system-wide or cross-project tool is adopted;
- a tool becomes deprecated or replaced;
- a candidate is promoted to active/default;
- a storage/source-of-truth boundary changes;
- a reusable platform capability moves into or out of the shared web family.

Do not add every one-off website or research utility. Record tools that materially affect architecture, repeatable workflow, durable storage, delivery, or cross-project capability.

## Related Canonical Nodes

- `docs/SHARED_WEB_PLATFORM_REGISTRY.md`
- `docs/SHARED_PROJECT_CAPABILITY_MATRIX.md`
- `knowledge-library/architecture-decisions/google-workspace-notion-data-layer-architecture.md`
- `docs/ROUTER.md`
- `blocks/design/BLOCK.md`
- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`