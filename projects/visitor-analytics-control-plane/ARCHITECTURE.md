# Universal Visitor Analytics — Architecture

## Goal

Provide one reusable system that answers, across all projects:

- who visited, where anonymity is preserved unless the user legitimately identifies themselves;
- which project/site they visited;
- how they arrived;
- what pages they viewed;
- what meaningful actions they performed;
- whether they converted;
- what the ordered session timeline looked like;
- when available and privacy-safe, what happened in session replay.

## Selected Donor

### Default: Umami v3

Use Umami as the analytics engine and datastore/API surface instead of creating our own collector.

Official capabilities verified on 2026-08-25 include:

- anonymous sessions;
- visitor activity history;
- pageviews/referrers/devices/countries;
- custom events with structured event data;
- funnels, journeys, retention, UTM tracking and goals;
- session replay and heatmaps;
- teams/access control;
- REST API;
- self-hosted or cloud operation;
- official Vercel hosting guide with PostgreSQL.

### Optional escalation: PostHog

Use only when a project needs capabilities Umami does not adequately cover, such as advanced product analytics, experimentation, feature flags or deeper customer-data infrastructure.

## System Shape

```text
Website / App
   |
Standard analytics adapter
   |
Umami tracking endpoint
   |
Central Umami + PostgreSQL
   |
Umami API
   |
Private cross-project operator console
```

The custom part should remain thin:

- integration adapter;
- project registry;
- normalized event naming;
- cross-project admin UI.

Do not custom-build ingestion/storage/sessionization first.

## Central Project Registry

Minimum metadata for every consumer project:

```text
project_id
project_name
website_id
domains
environment
owner
tracking_status
replay_enabled
event_schema_version
integration_type
last_verified_at
```

## Standard Event Contract

### Common event names

```text
nav_click
outbound_click
cta_click
contact_click
form_start
form_submit
entity_open
search
media_play
conversion
```

Projects may add domain-specific events, but they should map back to generic semantics where practical.

### Minimum event fields

```text
project_id
event_schema_version
page_path
page_title
entity_type   optional
entity_id     optional
entity_name   optional
destination   optional
cta_name      optional
source        optional
```

Never put secrets, payment details, passwords, medical data or raw sensitive form contents into analytics events.

## Identity Model

### Anonymous default

Use Umami's anonymous visitor/session model by default.

### Known identity

Only link a visitor to a known internal lead/customer when a legitimate first-party identification event exists.

Preferred analytics identifier:

```text
lead_id / customer_id / internal distinct id
```

Avoid sending raw email, phone number or other unnecessary PII to analytics when an internal opaque identifier can be used.

## Global Admin UI

Phase 2 is a thin private UI on top of the Umami API.

### Required screens

#### All Projects

- visitors;
- sessions;
- pageviews;
- conversions;
- top sources;
- trend by project.

#### Recent Visitors

- anonymous visitor/session ID;
- project;
- timestamp;
- landing page;
- referrer/UTM;
- country/device/browser;
- session duration;
- conversion status.

#### Session Timeline

Ordered timeline:

```text
landing page
-> page view
-> nav click
-> entity open
-> CTA/contact click
-> form start
-> form submit
```

#### Entity Interest

Cross-project reporting for reusable domain entities such as venue, wedding, product, article, service, vendor or listing.

#### Sources -> Behavior -> Conversion

Show which traffic source produced which behavior and which conversion outcome.

#### Replay

Only where enabled and privacy-reviewed. Link to or embed replay rather than cloning replay infrastructure.

## Olga Pilot Event Map

Sites:

- `olgapoloweddings.com`
- `venues.olgapoloweddings.com`

Events:

```text
nav_click { destination }
entity_open { entity_type: "venue", entity_id, entity_name }
entity_open { entity_type: "wedding", entity_id, entity_name }
contact_click { location }
form_start { form_id }
form_submit { form_id }
outbound_click { destination_domain }
```

Acceptance journey:

```text
main site
-> VENUES
-> Peterloon
-> CONTACT
```

The admin must show one coherent anonymous activity trail where the browser/session model technically permits it.

## Privacy And Security

- private admin only;
- mask sensitive replay fields;
- no secrets in client bundles;
- no raw sensitive form payloads in analytics;
- document retention and deletion/export procedure;
- enable replay per project only after privacy/consent review;
- keep production admin credentials separate from site tracking identifiers.

## Deployment Direction

Umami supports deployment on Vercel with a PostgreSQL database. Use an existing managed PostgreSQL provider supported by Umami/Vercel rather than inventing database operations.

Exact infrastructure choice must be based on the currently available connected account/resources and cost, but the interface above remains provider-independent.

## Capability Boundaries

Potential reusable capability entries:

- `analytics.track` — normalized event/page tracking adapter;
- `analytics.query` — normalized read adapter over the selected analytics provider.

These remain `idea` until executable code and tests exist.

## Promotion Plan

```text
architecture selected
-> central analytics deployed
-> analytics.track candidate
-> Olga Vercel pilot
-> Showit pilot
-> cross-surface QA
-> analytics.track validated
-> private global admin MVP
-> second independent project integration
-> production promotion
```
