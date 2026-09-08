# Design Block Donors

## Purpose

This file records the main donor tools and patterns that informed the first `Design Block` shape.

The goal is pattern borrowing, not vendor lock-in.

## Donors And Borrowed Ideas

### Relume

Borrow:

- move from sitemap to wireframe instead of styling first;
- keep page structure explicit before component polish;
- treat site architecture as part of design work.

### v0

Borrow:

- use prompting to generate high-fidelity UI exploration quickly;
- keep outputs close to real frontend implementation;
- treat design and implementation handoff as adjacent, not separate worlds.

### shadcn/ui

Borrow:

- think in reusable components and composition patterns;
- prefer buildable UI systems over static mockup-only language;
- keep component naming and structure implementation-friendly.

### Builder.io / Visual Copilot

Borrow:

- map design output toward real code components and design tokens;
- keep design-to-code handoff explicit;
- care about responsive output and component reuse.

### Figma Make

Borrow:

- use prompt-driven iteration as a fast exploration step;
- allow design refinement through direct iteration rather than one-shot output;
- keep prototype thinking close to the working interface.

### Google Stitch

Borrow:

- support early UI exploration from text, sketch, or reference;
- move quickly from rough idea to structured interface candidate;
- treat exploration as upstream of review and implementation.

### screenshot-to-code / v0.diy

Borrow:

- use open-source implementation references as reality checks;
- value reproducible UI structure over presentation-only inspiration;
- keep awareness that generated designs eventually need code-level translation.

### AI UX Playground

Borrow:

- use explicit review prompts and checklist-style critique;
- make UX evaluation part of the workflow, not an optional afterthought;
- keep the system teachable for future agents.

### Refero / Refero Styles / Refero MCP

Status: `EXTERNAL / CANDIDATE DONOR`.

Borrow:

- make design research happen before the agent starts coding;
- use real shipped product screens and user flows as evidence instead of generic taste adjectives;
- convert a visual reference into AI-readable design context such as colors, typography, spacing, shapes, components, tokens and do/don't rules;
- use `DESIGN.md` as a compact transport format from donor analysis into Codex/Cursor/Claude/v0-style execution;
- support search by page type, UX pattern, UI pattern, product category, visual style and similar-reference intent;
- expose structured reference metadata to agents through MCP instead of forcing the agent to reason only from screenshots;
- keep a strict "reference, not clone" boundary: extract the system, hierarchy and reusable patterns rather than reproducing a source product exactly.

Important fit for our system:

- Refero Styles is a strong donor for `Design Picker` because it already demonstrates the flow `reference library -> owner/agent selection -> structured style extraction -> implementation context`;
- Refero MCP is a candidate external research/data layer for agent-driven design discovery;
- the local `Design Picker` still owns our project boards, owner decisions, rejected directions, reusable pattern records and portable export format unless a later evaluation proves an external product can replace those needs cleanly.

Revalidate pricing, access limits, terms and MCP availability at adoption time. Do not make paid Refero access a mandatory dependency of the reusable Design Block.

## What Stays Custom

This block stays custom in these areas:

- routing shape inside `Project Execution OS`;
- the exact lightweight document set;
- the buildability-first rule for Codex handoff;
- the review order and minimum output contract.

## Final Rule

Borrow the useful workflow shape, but keep the canonical reusable standard inside this repository.
