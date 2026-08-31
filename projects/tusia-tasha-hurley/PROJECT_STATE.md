---
status: in-progress
project_mode: active-production
last_updated: 2026-08-31
next_action: Normalize SEO Production Queue to the Page Queue contract and run the next approved venue/wedding page through preview and QA without bypassing canonical data gates.
---

# Tusia / Tasha Hurley Weddings — Project State

## Current Phase

`Knowledge Engine established -> Website/Page Factory integration`

## Canonical Data

Google Sheet:

https://docs.google.com/spreadsheets/d/1QXNyfvWt-Y4Cro7CEStaa_WK8EcQ5qk25nHmiVuWy64/edit

The workbook is the canonical structured operational source of truth.

## Current Production Contract

`Research / first-party evidence -> canonical IDs -> Knowledge DB -> SEO Production Queue -> readiness + QA -> Page Factory -> staging preview -> technical QA -> explicit release -> verification -> DB feedback`

## Queue Rule

`SEO Production Queue` is the project's canonical Page Queue.

Do not create a second Page Queue unless the owner explicitly changes the architecture.

## Website Rule

Operational staging shell:

https://tashah.sg-host.com/

Reference wedding page:

https://tashah.sg-host.com/sophie-kendall/

The Page Factory must integrate with the existing Tasha site experience, navigation and transitions. Venue pages are the organizing layer; weddings are linked/embedded beneath the relevant venue context where appropriate.

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

Priority candidates include:

1. Ashley & Steve — Elizabeth House & Creekside Cabins
2. Deanna & Sam — Kalmia Garden at Gastler Farm
3. Ammie Chinchilla & Mark Veazie
4. Alexa & John
5. Malkah & Ryan — Adena Orchard & Vine
6. Sophie & Kendall — Brooklyn Grange / Central Park cluster

Other review-derived weddings remain enrichment-first until venue/media/evidence gates are satisfied.

## Active Risks / Cleanup

- Existing queue schema predates the full global Page Queue contract and needs normalization rather than replacement.
- Some DRY RUN research has newer candidate facts than canonical queue rows; promotion must be controlled.
- The workbook README contains legacy Cincinnati wording and must be corrected so a new executor cannot confuse Tusia with Olga Polo.
- Website & Design Drive folder is structurally present but still under-populated compared with the mature Knowledge DB.

## Next Practical Step

Normalize the existing queue fields and update project documentation/Change Log, then select the highest-priority row that passes identity, evidence, media and URL gates for Page Factory preview.

## Stop Conditions

Do not:

- publish from dry-run sheets;
- infer missing facts;
- create a parallel database;
- create a parallel standalone site shell;
- silently change canonical URLs;
- claim production completion based only on staging preview.
