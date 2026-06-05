# Design Block

## Purpose

This block gives `Project Execution OS` one reusable workflow for website-design work that must stay usable, buildable, and reviewable.

It teaches an agent to move from product intent to page structure to wireframe to UI system to frontend-aware handoff, instead of stopping at decorative mockups.

## Status

`candidate`

## When To Use

Use this block when the task is to:

- design a new website, landing page, marketing page, or product flow;
- turn a project idea into a structured website plan;
- define sitemap, page structure, or user-path-first page scope;
- create a frontend-aware UI specification before implementation;
- review an existing website design for usability, clarity, and buildability;
- prepare design guidance that Codex or another frontend executor can implement.

## When Not To Use

Do not use this block for:

- pure branding work with no website or product-flow outcome;
- decorative image generation;
- final visual polish without first clarifying user path and page structure;
- backend-only or infrastructure-only work;
- tasks where direct frontend implementation should begin immediately from an already-accepted spec.

## Core Rule

Do not treat website design as image prompting.

A valid design pass must connect:

`goal -> user scenario -> page structure -> wireframe -> UI system -> responsive behavior -> frontend-aware handoff -> review`

If one of those layers is missing, the design is incomplete.

## Required Reading Inside This Block

Open in this order:

1. `blocks/design/WEBSITE_DESIGN_PIPELINE.md`
2. `blocks/design/DESIGN_AGENT_STANDARD.md`
3. `blocks/design/DESIGN_REVIEW_STANDARD.md` when the task is review-first or after a design draft exists
4. `blocks/design/DONORS.md` only when donor rationale or pattern borrowing is needed

## Relationship To Codex And Frontend Execution

This block does not replace frontend implementation.

Its job is to produce a design package that a frontend executor can build with minimal guessing.

That means the design output should make clear:

- what the page is trying to achieve;
- what the user must notice, decide, and do;
- which sections and components exist;
- how the layout changes across screen sizes;
- which interaction states or content rules matter;
- what is still intentionally left for implementation judgment.

## Typical Outputs

Typical outputs:

- website goal summary;
- primary user path;
- sitemap or page structure;
- low-fidelity wireframe notes;
- UI system direction;
- responsive behavior rules;
- frontend-aware handoff spec;
- design review findings and required revisions.

## Boundary

This block stores the reusable website-design workflow layer.

Keep project-specific brand choices, final copy, and implementation details in the target project unless they are being generalized into a reusable standard.

## Final Rule

Make designs that can be built and reviewed, not just admired.
