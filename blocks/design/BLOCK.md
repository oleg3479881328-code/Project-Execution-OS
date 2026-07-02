# Design Block

## Purpose

This block gives `Project Execution OS` one reusable workflow for website, landing-page, SaaS-site, and product-interface design that must stay research-grounded, usable, conversion-aware, buildable, reviewable, and protected from generic AI-coded frontend output.

It teaches an agent to move from product intent to donor research, visual donor selection, page strategy, section composition, UI system, responsive behavior, implementation handoff, frontend design QA, and design review instead of stopping at decorative mockups or compiling generic UI.

## Status

`candidate_v3`

The block has been expanded from a process-only design block into a fuller website-building, site-design, and AI-coded frontend QA domain block. It remains candidate until validated on real website projects.

## Core Principle

Design = Research + Adaptation + Execution Readiness + QA.

Do not start by drawing.

Start by understanding the product, user path, competitors, donor websites, proven patterns, conversion goal, and implementation stack.

When owner taste or visual direction is not yet fixed, show a curated visual catalog and let the owner select concrete references before drafting the specification.

When AI codes a visible frontend, do not accept compile success as design success. Run the narrowest useful design QA gate before release or handoff.

## When To Use

Use this block when the task is to:

- design a new website, landing page, marketing page, SaaS site, dashboard, pricing page, onboarding flow, or product web interface;
- turn a project idea into a structured website plan;
- research donor websites and reusable patterns;
- let the owner choose a design direction visually from donor examples;
- choose a ready site stack;
- define sitemap, page structure, or user-path-first page scope;
- create a frontend-aware UI specification before implementation;
- review an existing website design for usability, clarity, conversion, consistency, and buildability;
- prepare design guidance that a frontend executor can implement;
- apply a design QA gate to AI-coded frontend work, including Impeccable-backed or manual fallback review.

## When Not To Use

Do not use this block for:

- pure branding work with no website or product-flow outcome;
- decorative image generation;
- final visual polish without first clarifying user path and page structure;
- backend-only or infrastructure-only work;
- tasks where direct frontend implementation should begin immediately from an already-accepted spec and no design review or QA gate is requested.

## Required Design Chain

A valid website design pass must connect:

`goal -> user scenario -> donor research -> visual donor selection when needed -> page strategy -> section plan -> wireframe -> UI system -> responsive behavior -> implementation handoff -> frontend design QA when AI-coded or release-bound -> review`

If one of those required layers is missing, the design is incomplete.

## Required Reading Inside This Block

Smallest useful path:

1. `blocks/design/BLOCK.md`
2. `blocks/design/WEBSITE_DESIGN_PIPELINE.md`
3. `blocks/design/DESIGN_AGENT_STANDARD.md`
4. `blocks/design/DONOR_ANALYSIS.md` for donor-first work
5. `blocks/design/DESIGN_PICKER.md` when the owner should choose a visual direction from examples
6. `blocks/design/READY_SITE_STACKS.md` when implementation stack matters
7. `blocks/design/LANDING_PAGE_PATTERNS.md` for landing pages
8. `blocks/design/SAAS_PATTERNS.md` for SaaS/product websites
9. `blocks/design/SECTION_LIBRARY.md` for page composition
10. `blocks/design/UI_COMPONENT_LIBRARY.md` for component/state planning
11. `blocks/design/DESIGN_SYSTEMS.md` for UI-system decisions
12. `blocks/design/MOTION_AND_ANIMATION.md` when motion is requested or visible
13. `blocks/design/CONVERSION_AND_MARKETING.md` when business conversion matters
14. `blocks/design/IMPLEMENTATION_HANDOFF.md` before frontend execution
15. `blocks/design/IMPECCABLE_DESIGN_QA_GATE.md` when AI-coded frontend work needs design QA or an Impeccable-backed review path
16. `blocks/design/WEBSITE_REVIEW_CHECKLIST.md` for review
17. `blocks/design/DESIGN_REVIEW_STANDARD.md` when deeper formal review is needed
18. `blocks/design/DONORS.md` only when legacy donor rationale or older pattern notes are needed

Do not load every file by default. Load the smallest path that fits the current task.

## Relationship To Frontend Execution

This block does not replace frontend implementation.

Its job is to produce a design package that a frontend executor can build with minimal guessing and then check visible AI-coded output against a design QA gate when the surface is release-bound or owner-facing.

That means the design output should make clear:

- what the page is trying to achieve;
- what the user must notice, decide, and do;
- which donor patterns influenced the design;
- which visual references the owner selected or rejected;
- which sections and components exist;
- how the layout changes across screen sizes;
- which interaction states or content rules matter;
- which ready site stack fits the work;
- whether Impeccable-backed design QA or manual fallback QA is required;
- what is still intentionally left for implementation judgment.

## Typical Outputs

Typical outputs:

- donor research summary;
- owner design-selection record when visual choice is needed;
- website goal summary;
- primary user path;
- sitemap or page structure;
- section-by-section page plan;
- low-fidelity wireframe notes;
- UI system direction;
- ready site stack recommendation;
- responsive behavior rules;
- conversion review;
- frontend-aware handoff spec;
- Impeccable or manual Design QA Gate record when AI-coded frontend work is reviewed;
- design review findings and required revisions.

## Boundary

This block stores the reusable website-design, site-building, and frontend-design-QA workflow layer.

Keep project-specific brand choices, final copy, customer data, proprietary screenshots, Impeccable runtime outputs, and implementation details in the target project unless they are being generalized into a reusable standard.

## Final Rule

Make designs that can be understood, trusted, converted, built, checked, and reviewed — not just admired.
