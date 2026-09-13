# Website Creator — SITE_MODEL_STANDARD.md

## Status

- Decision: accepted architecture direction
- Schema state: `v0.1 NOT YET FROZEN`
- Derivation rule: first concrete version must come from a real new-site validation, not from abstract completeness planning

## Purpose

The Site Model is the **platform-independent execution contract** for a concrete website instance.

It sits between research/strategy and renderers/editors/platform adapters.

It does **not** replace Website Creator as the global knowledge/control plane.

Website Creator answers how websites should be produced. The Site Model expresses the structured state of one specific site so reusable execution capabilities can consume it.

## Core Boundary

`Website Creator standards / research / design decisions`
→ `Site Model`
→ `renderer / CMS / editor / platform adapters`
→ `QA / release / deployment`

No renderer, CMS or vendor should become the canonical definition of the website.

## v0.1 Derivation Rule

Do not attempt to pre-model every possible website category.

For the first real new-site production:

1. capture only the structured information actually needed to build, edit, QA and release that site;
2. separate universal fields from project-specific extensions;
3. implement one real renderer/adapter against that model;
4. validate the model against a second and third meaningfully different site;
5. only then promote recurring fields/contracts into a broader stable schema.

This protects Website Creator from designing a giant theoretical schema that no real workflow needs.

## Logical Capability Areas

The first Site Model may need data from these areas. These are **domains**, not a frozen field list:

- site identity and business/entity identity;
- site goals and primary conversion actions;
- page graph / sitemap / page identity;
- page/section/component content;
- structured factual data where required;
- design-system binding / tokens / variants;
- media references and non-destructive presentation metadata;
- navigation and internal relationships;
- forms / CTA / interaction configuration;
- SEO/discovery metadata and canonical/indexing intent;
- editor/CMS binding when applicable;
- publishing/release state;
- renderer/platform binding;
- QA/verification references;
- analytics/measurement binding when applicable.

A site must not be forced to populate irrelevant domains.

## Data / Rendering Separation

When repeatability, editing, migration or scale requires it:

- structured site facts/content live in the Site Model or referenced canonical data;
- rendering logic lives in renderers/adapters;
- editor UI changes the same canonical site state consumed by public rendering;
- vendor-specific IDs/config stay in adapter/platform bindings, not mixed into universal content fields unless required for identity.

## Site Instance

Conceptually:

`Site Instance = populated Site Model + assets + selected execution bindings + QA/release/deployment state`.

A Site Instance does not automatically require its own bespoke application code.

A platform-managed site, code-rendered site, WordPress site or other execution target may all represent the same architectural concept if they preserve the required contract.

## Secrets / Isolation Boundary

Secrets do not belong in the Site Model.

Credentials, API tokens, deployment secrets, private client access and domain-control credentials must live in an appropriate secrets/identity system.

Before shared infrastructure operates multiple live client sites, each Site Instance must have explicit isolation for:

- content/data;
- media;
- credentials/secrets;
- editor roles/permissions;
- deployment authority;
- domain/DNS authority;
- backups/history where applicable.

## Schema Representation

When v0.1 becomes concrete, prefer a machine-readable contract that can be validated deterministically.

Target representation:

- TypeScript types for implementation ergonomics where TypeScript is used;
- JSON Schema or equivalent machine-readable validation contract;
- explicit `schemaVersion`;
- examples/fixtures;
- migration notes for breaking changes.

Do not create fields merely because a schema can support them.

## Versioning Rule

- additive backward-compatible changes may evolve within the current compatible versioning policy;
- breaking semantic/structural changes require explicit migration handling;
- Site Instances must identify which schema version they conform to;
- adapters/renderers must declare supported schema versions when version drift becomes operationally relevant.

Exact semantic-version policy can be finalized when v0.1 has a real implementation.

## Renderer / Adapter Contract

A renderer or platform adapter should:

1. declare what Site Model version/capabilities it supports;
2. fail clearly on required unsupported data;
3. avoid silently inventing missing factual content;
4. preserve intended design/content/SEO semantics;
5. expose deterministic preview/output for QA;
6. keep vendor-specific behavior behind the adapter where practical.

## Editor Contract

If a visual editor is used:

- it edits canonical Site Model state or a deterministic mapped representation;
- editor/public rendering must agree;
- draft/editing state is not automatically published state;
- content history/rollback must exist in the chosen storage/CMS architecture when production editing requires it.

See `EDITOR_CREATION_STANDARD.md` for interaction behavior.

## QA Contract

The Site Model should make deterministic validation possible before release, including where relevant:

- required identity/page/content fields;
- broken references;
- invalid URL/canonical relationships;
- missing required media metadata;
- invalid publish states;
- renderer capability mismatches.

Browser/output QA remains a separate downstream layer.

## First Validation Gate

`v0.1` is considered real only when all are true:

1. derived from a real new-site build;
2. represented machine-readably;
3. consumed by at least one real renderer/adapter;
4. produces a QA-able preview;
5. survives one edit/re-render cycle without manual data reconstruction;
6. records gaps discovered during production.

Do not mark a theoretical document-only schema as `v0.1 complete`.

## Promotion Rule

After multiple real Site Instances:

- recurring project-specific fields may be promoted to the universal core;
- rare fields remain extension/domain-specific data;
- vendor fields remain adapter-specific when possible;
- remove unused theoretical fields instead of preserving them for imagined future cases.

## Final Rule

**The Site Model should be discovered through real production, then stabilized — not designed as an exhaustive universe before the first site exists.**