# Website Creation — SOURCE_REGISTRY.md

## Purpose

This is the durable discovery index for website-creation knowledge already produced across projects.

Use it to find the current canonical source first, then the smallest supporting artifact. Do not reconstruct website methods from chat memory.

Status labels:

- `CURRENT / CANONICAL` — use first for present operating truth.
- `CODE / LIVE SOURCE` — executable/current repository source.
- `REUSABLE STANDARD` — cross-project PEOS standard/block.
- `PROVEN DONOR` — real production system/pattern worth generalizing.
- `RESEARCH / DONOR` — useful external/platform research; revalidate time-sensitive facts.
- `HISTORY / EVIDENCE` — archive, migration, task or incident evidence; do not treat as current truth by default.

---

## 1. Website Creation project core

- `CURRENT / CANONICAL` — Project entrypoint:
  `projects/website-creation/PROJECT.md`
- `CURRENT / CANONICAL` — Current state:
  `projects/website-creation/PROJECT_STATE.md`
- `CURRENT / CANONICAL` — Task router:
  `projects/website-creation/ROUTER.md`
- `CURRENT / CANONICAL` — Drive root:
  https://drive.google.com/drive/folders/15DIWML8HiLSJrNfP5r7IyZu_YkrD2GTU

---

## 2. Olga Polo Weddings — principal real production donor

### Current control layer

- `CURRENT / CANONICAL` — Olga Polo Weddings — CANONICAL PROJECT PROTOCOL — CURRENT:
  https://docs.google.com/document/d/17-MZN4RO3N-_xdwFSC10VIBBTD0FP_ZIGcvVtdrlOe8/edit
- `CURRENT / CANONICAL` — Olga Polo — OPERATIONAL ALGORITHMS — CURRENT:
  https://docs.google.com/document/d/1vjR5oBHopWG61nqsn4Sm21-2sZ-f0ESGEMtx6IIedf0/edit
- `CURRENT / CANONICAL` — Publication policy:
  https://docs.google.com/document/d/1xKodIOLr0rNNlM2JJlY4rfmndwPI7yDmLvVN88g51AI/edit
- `CURRENT / CANONICAL` — Gold Standard Production Checklist:
  https://docs.google.com/document/d/1hBuMFx-63xNtE1bcAbY3ZxkGb99skO9-rOMB9XXdr4Y/edit
- `CODE / LIVE SOURCE` — Olga website repository:
  https://github.com/oleg3479881328-code/olga-polo-weddings-web
- `CODE / LIVE SOURCE` — repository PROJECT.md:
  https://github.com/oleg3479881328-code/olga-polo-weddings-web/blob/main/PROJECT.md
- `CODE / LIVE SOURCE` — publication pipeline runbook:
  https://github.com/oleg3479881328-code/olga-polo-weddings-web/blob/main/docs/PUBLICATION_PIPELINE.md
- `CODE / LIVE SOURCE` — live-page visual QA standard:
  https://github.com/oleg3479881328-code/olga-polo-weddings-web/blob/main/docs/LIVE_PAGE_VISUAL_QA.md
- `CODE / LIVE SOURCE` — repository Gold Standard copy:
  https://github.com/oleg3479881328-code/olga-polo-weddings-web/blob/main/docs/GOLD_STANDARD_PRODUCTION_CHECKLIST.md
- `CODE / LIVE SOURCE` — repository publication standard:
  https://github.com/oleg3479881328-code/olga-polo-weddings-web/blob/main/docs/OLGA_PUBLICATION_STANDARD.md

### Architecture / page factory / Showit + Vercel

- `PROVEN DONOR` — SEO / TSEO Page Factory — Showit + Vercel Architecture:
  https://github.com/oleg3479881328-code/olga-polo-weddings-web/blob/main/docs/TSEO_SHOWIT_VERCEL_ARCHITECTURE.md
- Reusable concepts captured there:
  - keep stable production surface isolated during MVP;
  - structured `data -> template -> page -> indexation -> impressions -> clicks -> inquiry`;
  - entity-driven `/venues`, `/weddings`, `/locations` page families;
  - evidence/publishability gates before page generation;
  - structured GitHub data + Next.js renderer + Vercel deploy;
  - safe subdomain-first migration before risky unified routing;
  - GSC/GA4/GTM measurement chain;
  - image SEO and structured data as first-class page-factory concerns.

### Knowledge / entity database

- `PROVEN DONOR` — Olga Knowledge Database v1 — Cincinnati Wedding Ecosystem:
  https://docs.google.com/spreadsheets/d/1b45_FTuiv6o-ThfsSLZsKeU6UGeAKcCnFHFsGYxADWk/edit
- Reusable concepts:
  canonical IDs, slugs, entity relationships, evidence/confidence, publish state, internal graph reuse, vendor/venue/wedding relationships, structured data feeding pages.

### Editor / CMS / authoring

- `PROVEN DONOR` — SOFT — Olga Image Editor — MIGRATION SNAPSHOT — 2026-09-11:
  https://docs.google.com/document/d/1HWHTwXX2KvK-gPUqN3nIrlrh642IeDSWTiVg4vqK9v4/edit
- `CODE / LIVE SOURCE` — editor source folder:
  https://github.com/oleg3479881328-code/olga-polo-weddings-web/tree/main/app/editor
- Key current source files include:
  - `app/editor/EditableImageFrame.tsx`
  - `app/editor/EditableImageFrame.module.css`
  - `app/editor/ImageCropDialog.tsx`
  - `app/editor/ImageInspectorPanel.tsx`
  - `app/editor/image-crop-model.ts`
  - shared venue/wedding editor consumers.
- Reusable current decisions:
  - Puck owns page/block editing;
  - `react-easy-crop` runs in an isolated crop dialog outside Puck transforms;
  - crop/pan/zoom is non-destructive display metadata;
  - exact crop area stored in percentages;
  - shared behavior for Hero and normal images, Weddings and Venues;
  - floating image toolbar and right inspector share the same state/handlers;
  - no custom pointer-to-Puck crop coordinate math;
  - distinguish editor-component bug vs local draft bug vs content/template mutation before fixing.
- `HISTORY / EVIDENCE` — Split Editor into Venues and Weddings Workspaces:
  https://docs.google.com/document/d/1p8DEg-VzR_wDZoLYzUo9gLlUb_PIKzusJB3A4u1UwDA/edit
- `HISTORY / EVIDENCE` — duplicate gallery/editor-preview fix:
  https://docs.google.com/document/d/1SZhSwnzHlI8fYws5vcP6vhA8BdBNZMvhKNU0YG6uVW4/edit

### Publication / media / release architecture

Reusable production knowledge from current Olga sources:

- factual/source integrity and no-invention discipline;
- entity/media identity before publication;
- `ORIGINAL MASTER != DELIVERY ASSET`;
- source/delivery hash lineage and reproducible transformations;
- no upscaling;
- content staging / isolated PR paths;
- direct intake writes to `main` forbidden;
- PR -> authoritative CI -> merge -> production deploy -> live QA;
- deployed/build-success is not the same as PUBLISHED;
- rollback readiness requires previous known-good deployment;
- owner-facing orchestration should collapse normal internal steps into assignment -> result/blocker;
- machine-pipeline latency should be measured end-to-end and slow phases named precisely.

### SEO / search / migration evidence

- `CURRENT / EVIDENCE` — GSC / SERP Evidence Log — CURRENT:
  https://docs.google.com/document/d/1quVmXcSVvSF-ovs9kuwp0YjfA5TYCG5HgVW8HWGREB8/edit
- `PROVEN DONOR` — SEO Transformation Log — BEFORE → AFTER — 2026:
  https://docs.google.com/document/d/1REOp90bA-470yFYJ8ioQKtlEB0ZazUHF889gX6omzU8/edit
- `PROVEN DONOR` — Wix Legacy SEO Migration Plan:
  https://docs.google.com/document/d/1Uw0RFnjyG_l8-TYimH1OMgPH1q0XlAhn1BrtqBmxQwY/edit
- `HISTORY / EVIDENCE` — sitemap audit task:
  https://docs.google.com/document/d/1Zy0tJC6KweFNs8GuEvTgLwqYVz7e_VEHKyoboT0c1vA/edit
- `HISTORY / EVIDENCE` — full Sitemap / published URL inventory:
  https://docs.google.com/document/d/115lZkk5IdD7l9SdZVRvK2634UIw9sRV7Mo_RbF6LXvs/edit
- `HISTORY / EVIDENCE` — SEO / Sitemap / Blog Recovery / PASS pipeline migration:
  https://docs.google.com/document/d/1Cpa-QCqZMW_vmCvdV5oj_6V-uPDbcJq_9i25hqTZHxU/edit
- `PROVEN DONOR` — Homepage Image SEO Audit / snippet candidates:
  https://docs.google.com/document/d/1EFd3_HKvGifLaXEf8bIHraiSnnW4yDtshCPfxgDu2rQ/edit
- `PROVEN DONOR` — PASS Gallery / Content Ownership / New Wedding Pipeline:
  https://docs.google.com/document/d/1c659TtFY6xGiUBmb2iNLAueI8xJcn93EVcYiqisK2qQ/edit

### Editorial/page reference implementations

- `PROVEN DONOR` — Matt & Morgan Wedding Page Gold Standard migration:
  https://docs.google.com/document/d/1A-JDGag_kq6jWZbtdvYKKtYhI5wafWt-Excyb6Q83sA/edit
- `PROVEN DONOR` — Venue Page Content Quality & Expert Signal Audit:
  https://docs.google.com/document/d/17ohUEAGfpKDLveYOieN8o0gp12me9T_02xlPfMI-JN4/edit
- `PROVEN DONOR` — Full Venue + Wedding Standards Audit — 2026-09-11:
  https://docs.google.com/document/d/1-xgS-SvOES80gN9chR4VRAvw4SRCxIkxgZSZJVfTscI/edit
- Reference cluster named by current Gold Standard: Peterloon Estate + Matt & Morgan + Emanuel & Kristi + Kevin & Grace. Use as architecture/quality reference, not copy to clone.

### Olga historical context / continuity

- `HISTORY / EVIDENCE` — Full project protocol/history archive through 2026-09-07:
  https://docs.google.com/document/d/1-sjGRcDwV_7hW9wuTyG1Co8smkfvOJS6JPrTXt_aoKI/edit
- `HISTORY / EVIDENCE` — Publication Decisions & Evidence Log archive:
  https://docs.google.com/document/d/1zMmnZmYNfOQBWF1zyIiXXdKEuHqqs8tJFJIwIwybF_g/edit
- `HISTORY / EVIDENCE` — Master Handoff — 2026-08-28:
  https://docs.google.com/document/d/1VaYCQG9z6IUQwDF52myeHiTsVLYRsGuefJV7_i3G8OI/edit
- `HISTORY / EVIDENCE` — Migration Snapshot — 2026-08-28:
  https://docs.google.com/document/d/1-IwEFGKDXgfPZwFy8DSHPde23m8oyBWDbpxSzuK2g2A/edit
- `HISTORY / EVIDENCE` — Migration Snapshot — 2026-08-29 09:40 ET:
  https://docs.google.com/document/d/1Wu-3K0RgtQxVyCoFjLQx7sBWKkR3GMEvcffHG41U_20/edit
- Older project-state/backups remain evidence only and must not override current protocol/algorithms.

---

## 3. PEOS website design system

- `REUSABLE STANDARD` — Design Block:
  `../../blocks/design/BLOCK.md`
- Its routed library includes:
  - `WEBSITE_DESIGN_PIPELINE.md`
  - `DESIGN_AGENT_STANDARD.md`
  - `DONOR_ANALYSIS.md`
  - `DESIGN_PICKER.md`
  - `READY_SITE_STACKS.md`
  - `LANDING_PAGE_PATTERNS.md`
  - `SAAS_PATTERNS.md`
  - `SECTION_LIBRARY.md`
  - `UI_COMPONENT_LIBRARY.md`
  - `DESIGN_SYSTEMS.md`
  - `MOTION_AND_ANIMATION.md`
  - `CONVERSION_AND_MARKETING.md`
  - `IMPLEMENTATION_HANDOFF.md`
  - `TASTE_FRONTEND_EXECUTION_STANDARD.md`
  - `IMPECCABLE_DESIGN_QA_GATE.md`
  - `WEBSITE_REVIEW_CHECKLIST.md`
  - `DESIGN_REVIEW_STANDARD.md`
- Core reusable chain:
  `goal -> user scenario -> donor research -> visual donor selection -> page strategy -> sections -> wireframe -> UI system -> responsive behavior -> implementation handoff -> bounded frontend execution -> design QA`.

---

## 4. Our extraction / reverse-engineering tools

### Universal Site Design Extractor

- `PROVEN DONOR / INTERNAL TOOL` — status/source record:
  https://docs.google.com/document/d/1albuaKqO3Dy_rJmXbAPofP89B6R3_NItzH5raYaF7_I/edit
- Known exported artifacts include `DESIGN.md`, `tokens.css`, `tokens.json`, DTCG JSON, Tailwind config, `evidence.json`, and Export All ZIP.
- Intended route:
  donor research/selection -> extractor -> normalized design profile/tokens -> implementation -> anti-slop execution -> design QA.
- Do not claim pixel-perfect cloning or universal animation/framework extraction until directly reverified.

### Browser extensions catalogue

- `CURRENT / INDEX` — Browser Extensions — MASTER INDEX — 2026-09-09:
  https://docs.google.com/document/d/1gpvYZdiRiNAubbwq6OFoWIiDgiJI9Pgl279LqkFcwDM/edit

### Site baseline / intelligence

- `PROVEN DONOR / INTERNAL` — Olga full site baseline scan task:
  https://docs.google.com/document/d/1Pazge8Ce5ggjPtRqocGM-KtMuVoExIWHDitx7Hu0oe4/edit
- Website Intelligence / Site Baseline Scanner is an existing internal capability referenced by Automatic Website Factory; use it for qualification/audit where proven.

---

## 5. Automatic Website Factory — child initiative

### Canonical project artifacts

- `CURRENT / CANONICAL` — PROJECT:
  https://docs.google.com/document/d/1QrJzBt0o55Bp38RBvo2DDgcVaBBPvxJDXUDOf2GOdpI/edit
- `CURRENT / CANONICAL` — PROJECT STATE:
  https://docs.google.com/document/d/1igLranCr462Em9aiHDzPrNXsf_DaoFDtkSa15FHLg0c/edit
- Drive folder:
  https://drive.google.com/drive/folders/122m-lLRzsFnVlJf2qa-rcUwEoZPs3YBH

### Design / donor / execution research

- `RESEARCH / DONOR` — Design integration with PEOS Design Block:
  https://docs.google.com/document/d/1eGT-NwYiyfwF1KG1JrBfmZebh1TZOzjvJY5vc7wP6fA/edit
- `RESEARCH / DONOR` — LeadX + Duda + 10Web + FieldLaunch decomposition:
  https://docs.google.com/document/d/1KVTz8XyZfwMN2rILqeiOkqaSHGDIsyT3AR2WIrQEIuM/edit
- `RESEARCH / DONOR` — Donors & Ready-Made Options review:
  https://docs.google.com/document/d/1njAbLfODR9XYVJ3ZJTG7-ECTjAbtCYTqMC5AQ8iO4xg/edit
- `BENCHMARK / READY` — Prewitt Auto Repair — Duda vs 10Web Shootout:
  https://docs.google.com/document/d/1WRIegloiO2dX9Nx9z8Drn-MJdccbXHIZzhaIBvWoPjg/edit

### Reusable business/production model

`prospect discovery -> qualification -> public-source research -> dossier -> content/IA -> generation -> safe editor -> QA -> preview -> outreach/trial -> purchase -> domain/ownership transfer -> support`.

Current architectural preference: compose proven internal capabilities with ready-made provisioning/editor/preview engines; do not build a generic CMS/provisioning monolith until existing solutions fail the real benchmark.

---

## 6. SOFT — website tooling and donors

- `CURRENT / INDEX` — SOFT project:
  `../soft/PROJECT.md`
- `CURRENT / INDEX` — Master Software Inventory:
  https://docs.google.com/document/d/1yTWfazVPhs-AWdSsvS4Q6xyNd7bXKtqi6EvrmQMdAOk/edit
- `CURRENT / INDEX` — Our Software Index:
  https://docs.google.com/document/d/1nzxaCsFTF7Z7VGFfYziysByeR63eMOELpDT5rBcTDHk/edit
- `CURRENT / INDEX` — Third-Party Software Index:
  https://docs.google.com/document/d/1C-F_ukN2AlryP-_FxlJqFIKSbKjat8kzzMw8HsaSPH0/edit
- `HISTORY / CLEANUP` — Duplicates & Legacy Cleanup Queue:
  https://docs.google.com/document/d/1lBpoB-bbj4ihk6VW_gny_XbdfYCVD8Im0u6z3OTaBuc/edit

SOFT owns generic software discovery. Website Creation owns how those tools fit into website production.

---

## 7. Framer / motion / interaction donors

- `RESEARCH / DONOR` — Framer — platform and interaction donor — 2026-09-06:
  https://docs.google.com/document/d/19iKp-YMkOq6Ac3nYmmhvCuLqD3o5_9HLbdBEkiUoy-M/edit
- Recorded donor remix references include parallax and chimes interactions; use as interaction/motion donors rather than blindly cloning a whole site.
- Reusable principle: extract working interaction/motion DNA from proven donors, then adapt to the target design system and performance/accessibility constraints.

---

## 8. ChatGPT / AI-assisted website-creation research

- `RESEARCH / DONOR` — ChatGPT Website Creation Methods:
  https://docs.google.com/document/d/1VMfc8aag1cMaSDC_zTps_ju2CDb3dQ0mgZG6ka54-mE/edit
- Topics captured there include AI-assisted coding, CMS integration, WordPress, no-code/visual builders, screenshot-to-code, AI IDE workflows, pSEO/GEO, deployment and QA risks.
- Treat platform-specific/current feature claims as historical research until revalidated from current official documentation.

---

## 9. Analytics / behavior / optimization

- `REUSABLE / CROSS-PROJECT` — Visitor Analytics Control Plane — Microsoft Clarity — Canonical Knowledge:
  https://docs.google.com/document/d/1hl6Uckbzupj0kjE_81YWC-hiO7YxO-hUBAeS9_lnKHk/edit
- Olga TSEO architecture also defines GSC + GA4 + GTM measurement around query -> landing page -> click -> inquiry.

---

## 10. Core reusable website-production model distilled from existing work

This is a discovery map, not a replacement for the source standards.

1. **Research / identity**
   - confirm business/entity identity;
   - collect first-party/official/public evidence;
   - record confidence and conflicts;
   - audit an existing site before replacing it.

2. **Goal / conversion / IA**
   - define business goal and user path;
   - sitemap and page families;
   - page purpose and CTA;
   - cluster/internal-link strategy when applicable.

3. **Design**
   - donor-first research;
   - owner selection when visual direction is open;
   - extract/normalize tokens when useful;
   - section/component/UI system;
   - responsive + accessibility + performance + purposeful motion;
   - anti-generic frontend constraints and final design QA.

4. **Structured content**
   - facts/content separated from renderer;
   - stable IDs/slugs/entity links;
   - evidence/source/status metadata;
   - reusable templates render structured records;
   - no unsupported factual invention.

5. **Media**
   - immutable originals vs delivery derivatives;
   - traceable transformations;
   - no upscaling;
   - editorial selection/coverage;
   - alt/credit only when supported.

6. **Editor / CMS**
   - safe bounded authoring rather than unrestricted breakable layout when client editing is needed;
   - Puck is a proven internal block/page editor donor;
   - non-destructive image manipulation with shared state;
   - draft/staging/publish states must be explicit.

7. **SEO / AEO / pSEO**
   - unique metadata;
   - canonical/robots/sitemap/indexation;
   - structured data aligned with visible content;
   - internal linking/entity graph;
   - image SEO;
   - measured indexing/search traction before scaling thin page families.

8. **Implementation / release**
   - Git-backed change history when code-based;
   - preview/staging before production;
   - CI/build gates;
   - deploy is not terminal until live QA;
   - desktop/mobile visual verification;
   - previous known-good rollback target.

9. **Optimization**
   - measure wall-clock production time and precise slow phase;
   - measure search/behavior/conversion, not only aesthetic approval;
   - turn repeated successful work into deterministic algorithms and reusable components.

---

## 11. Archive / duplicate rule

Do not import every backup copy into Website Creation. Preserve **all knowledge** by indexing canonical/current sources plus the archive/evidence roots that contain history. Backups remain in their owning project and are consulted only when a current source points to history or a disputed decision requires evidence.

This prevents the new project from becoming a second stale copy of Olga Polo or SOFT.

---

## 12. Audit status

Initial high-value cross-project consolidation completed on 2026-09-13.

Coverage already includes:
- current Olga project/control docs;
- current Olga production policy/algorithm/runbook/QA;
- Showit + Vercel page-factory architecture;
- Olga knowledge database;
- current editor/image-editing architecture and code paths;
- SEO/migration/GSC/sitemap evidence;
- PEOS Design Block;
- Universal Site Design Extractor;
- Browser Extensions master index;
- Automatic Website Factory and its donors/benchmark;
- SOFT inventories;
- Framer donor research;
- ChatGPT/AI website-creation research;
- analytics control-plane source.

Audit is intentionally appendable. When another website-related artifact is discovered, add it here under the narrowest category rather than creating another parallel project index.