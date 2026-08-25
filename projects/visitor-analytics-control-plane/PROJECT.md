# Visitor Analytics Control Plane

## Status

`active — architecture selected, implementation not yet deployed`

## Purpose

Create one reusable visitor-intelligence and operator-admin system for all current and future web projects.

This is a global Project Execution OS capability. Individual projects such as Olga Polo are consumers/pilots, not the owner of the analytics architecture.

## Project Type

Internal cross-project platform capability and private operator application.

## Operating System

This project operates under `Project Execution OS`.

Top-level entrypoint:

`START_HERE.md`

Relevant standards:

- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
- `docs/COMPOSABLE_CAPABILITY_BLOCKS_STANDARD.md`
- `docs/PROJECT_MEMORY_STANDARD.md`

## Existing Solution First Decision

Default analytics core: **Umami v3**.

Why:

- open source and self-hostable;
- privacy-first anonymous tracking without cookies by default;
- pageviews, referrers, devices, geography and sessions;
- individual anonymous visitor/session activity;
- custom events and event properties;
- funnels, journeys, goals and UTM attribution;
- session replay and heatmaps;
- REST API suitable for a custom private admin wrapper;
- official Vercel deployment path;
- one installation can serve multiple websites/projects.

PostHog is an optional escalation provider for projects that later require deeper product analytics, experiments, feature flags, warehouse/CDP or other capabilities beyond the current global requirement.

Do not build a custom event collector/database unless Umami is proven insufficient for a concrete requirement.

## Architecture

See:

`ARCHITECTURE.md`

## First Pilot

Olga Polo Weddings:

- `https://olgapoloweddings.com/`
- `https://venues.olgapoloweddings.com/`

The pilot must prove that one visitor journey can be inspected across pageviews and meaningful events without inventing identity.

## Identity Rule

Visitors are anonymous by default.

A real person identity may only be linked after an explicit identification event such as a submitted inquiry, authenticated account, or another legitimate first-party identifier. Analytics must not receive raw sensitive form contents.

## Source Of Truth

- architecture/current project state: `projects/visitor-analytics-control-plane/`
- reusable executable capability readiness: `capability-library/REGISTRY.md`
- execution task: GitHub Issue #127

## Current Work

1. establish the central Umami deployment and PostgreSQL storage;
2. create standard multi-project registry fields;
3. create reusable tracking contract for pageviews + events;
4. integrate Olga Vercel surface first;
5. integrate Showit surface;
6. validate session timeline and conversion events;
7. only then build the private cross-project admin wrapper on the Umami API.

## Next Exact Step

Deploy the central Umami instance using its supported Vercel path plus PostgreSQL, then register Olga as the first tracked website and issue the first website ID.
