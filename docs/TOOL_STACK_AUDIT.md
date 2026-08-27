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

## 13. Maintenance Rule

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
