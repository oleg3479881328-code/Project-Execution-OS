---
status: in-progress
project_mode: active-production
last_updated: 2026-09-10
next_action: Run one client-validation pilot from a single real wedding after Tasha provides the three-part input bundle; do not scale wedding/venue content production until that pilot is approved.
---

# Tusia / Tasha Hurley Weddings — Project State

## Current Phase

`Knowledge Engine established -> single-wedding client validation pilot -> Website/Page Factory scale`

## Canonical Data

Google Sheet:

https://docs.google.com/spreadsheets/d/1QXNyfvWt-Y4Cro7CEStaa_WK8EcQ5qk25nHmiVuWy64/edit

The workbook is the canonical structured operational source of truth.

## Current Production Contract

`Research / first-party evidence -> canonical IDs -> Knowledge DB -> SEO Production Queue -> readiness + QA -> Page Factory -> staging preview -> client validation -> technical QA -> explicit release -> verification -> DB feedback`

The newly explicit client-validation gate is important: broad production must not scale from generic draft content. One real wedding must first prove that the content, voice, presentation and editing burden are acceptable to Tasha.

## Queue Rule

`SEO Production Queue` remains the project's canonical Page Queue.

Do not create a second Page Queue.

Queue normalization remains valid infrastructure work, but it is no longer the client-facing next step. The first pilot must use the canonical queue/data path rather than bypassing it.

## Website / Page Factory Repository

https://github.com/oleg3479881328-code/tasha-hurley-weddings-web

The existing repository is the execution layer. Its venue/wedding data carries canonical PQ/EV/venue IDs for traceability back to the Knowledge DB.

## Website Rule

Operational staging shell:

https://tashah.sg-host.com/

Reference wedding page:

https://tashah.sg-host.com/sophie-kendall/

Tasha's existing website is not being replaced, migrated or rebuilt as part of this work. The Page Factory must integrate with the existing Tasha site experience, navigation and transitions. Venue pages are the organizing layer; weddings are linked/embedded beneath the relevant venue context where appropriate.

## Client Signal — 2026-09-10

Tasha explicitly confirmed that SEO work is wanted and useful. The blocker is not lack of interest in SEO. The blocker is time, review burden and low confidence in generic AI-generated copy.

Key client feedback:

- she does not want to spend substantial time rewriting AI-generated text;
- copy that sounds obviously AI-generated or reads as generic/gibberish is unacceptable;
- she needs a concrete, very small next action rather than a broad system explanation;
- she wants the final material to feel like her own voice and contain real, meaningful wedding detail;
- her existing site is already built and must remain the site shell;
- her immediate site task is choosing/replacing photographs, which is inherently a client judgment task;
- September and October are overloaded with weddings and gallery delivery; November is the preferred window for broader business/SEO optimization;
- a single pilot wedding can still proceed earlier if she sends the agreed source bundle;
- no pushing or repeated client follow-up is required while she is overloaded.

## Three-Part Client Input Contract

For the first pilot, Tasha's required contribution is intentionally limited to three source groups:

1. **One wedding gallery / selected photographs** — the real images she wants considered for the page.
2. **One Tasha-authored reference** — a blog post, page or block that demonstrates how she likes the content to look and/or sound.
3. **First-party personal wedding material** — for example an officiant/ceremony text, story of how the couple met, or other real personal details supplied by the couple.

Do not ask her to design the SEO architecture, write alt text, rename files, create schema, define entity relationships or manually produce a full draft.

## Pilot Output Contract

Using those inputs, produce **one complete real-wedding page** for review.

Requirements:

- no invented facts;
- no generic filler presented as wedding-specific information;
- no obviously synthetic "AI voice" as the default writing style;
- use Tasha's own writing/reference material to guide voice and tone;
- use first-party wedding material for substantive story/detail;
- organize useful venue/vendor/wedding context for search and AI retrieval without making the public copy feel like SEO scaffolding;
- perform technical SEO/AEO work under the hood, including appropriate filenames, image alt text, structured data, metadata, entity/venue/vendor relationships and internal linking where supported;
- preserve the existing site shell, menu, transitions and overall user experience;
- keep routine editing simple, especially swapping/removing images;
- present the client with a finished preview to approve/correct, not a pile of disconnected generated fragments.

## Client-Validation Gate

Do **not** mass-produce or scale the wedding-page pattern until Tasha approves the first real pilot as directionally correct.

Approval should validate at least:

- voice feels like Tasha rather than generic AI;
- factual content is accurate and useful;
- design belongs inside her real site rather than feeling like a disconnected clone;
- editing/review effort is acceptably small;
- SEO/AEO structure does not damage the human-facing experience.

After approval, convert the accepted pilot into the reusable page/content pattern and scale through the existing Knowledge DB -> Queue -> Page Factory pipeline.

## Current Database Layers

Present and live:

- Entities Master
- ID Crosswalk
- Events
- Relationships
- Evidence
- Reviews
- People
- Entity Dossiers
- Media
- SEO Production Queue
- Redirects URLs
- QA
- Change Log
- Dashboard

## Research State

- TASK 15: venue cluster pipeline tested.
- TASK 16: unresolved identity research completed safely; no canonical speculation.
- TASK 17: reverse venue/vendor research produced high-value candidates/enrichments in DRY RUN.
- TASK 18: Reddit/community discovery dry run exists.
- TASK 19: wedding-site/marketplace discovery dry run exists.

Dry-run outputs remain candidate evidence until promoted.

## Current Known Queue

Existing priority candidates include:

1. Ashley & Steve — Elizabeth House & Creekside Cabins
2. Deanna & Sam — Kalmia Garden at Gastler Farm
3. Ammie Chinchilla & Mark Veazie
4. Alexa & John
5. Malkah & Ryan — Adena Orchard & Vine
6. Sophie & Kendall — Brooklyn Grange / Central Park cluster

The first client-validation pilot does not have to be chosen from this list if Tasha supplies a different wedding as the agreed pilot. Her supplied real-wedding bundle determines the client-validation candidate.

## Active Risks / Cleanup

- Generic or speculative AI copy can destroy client confidence even when the underlying SEO architecture is sound.
- Asking Tasha to review large amounts of unfinished generated content creates unacceptable client workload.
- Showing system architecture before a finished single example obscures the practical value and makes the next step unclear.
- Existing queue schema predates the full global Page Queue contract and still needs normalization rather than replacement.
- Some DRY RUN research has newer candidate facts than canonical queue rows; promotion must be controlled.
- The workbook README contains legacy Cincinnati wording and must be corrected so a new executor cannot confuse Tusia with Olga Polo.
- Website & Design Drive folder is structurally present but still under-populated compared with the mature Knowledge DB.

## Next Practical Step

**External dependency:** receive the three-part pilot bundle from Tasha when she is ready.

**Then:** register the pilot wedding/evidence/media through the canonical Knowledge DB and SEO Production Queue, build one finished page inside the existing site shell, run technical QA, and send only that finished preview for client validation.

Until the pilot is approved, do not turn generic generated wedding/venue copy into a scaled production pattern.

## Timing / Client Load

September–October 2026: minimize required client participation; Tasha is focused on weddings and gallery delivery.

November 2026: preferred period for broader business/site/SEO optimization after the pilot direction is validated.

## Stop Conditions

Do not:

- publish from dry-run sheets;
- infer missing facts;
- create a parallel database;
- create a parallel standalone site shell;
- silently change canonical URLs;
- claim production completion based only on staging preview;
- scale generic AI-generated copy before client validation;
- require Tasha to manually rewrite or SEO-optimize bulk drafts;
- treat her September–October availability as an invitation for repeated follow-up or push.