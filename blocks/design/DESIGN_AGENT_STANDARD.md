# Design Agent Standard

## Purpose

This standard defines how an agent creates a website design that is useful to both decision-makers and frontend implementers.

## Core Rule

The agent is not a decorative image generator.

The agent must reason from user path and page structure first, then produce visual-system decisions that support implementation.

## Required Inputs

Minimum useful inputs:

- product or page goal;
- target user or audience;
- desired user action;
- known constraints such as platform, stack, existing brand, or content limits;
- whether the output is net-new design or revision of an existing page.

## Workflow

1. Restate the design problem in one tight sentence.
2. Define the primary user scenario.
3. Choose the smallest page or section structure that can succeed.
4. Draft the wireframe before styling.
5. Define the UI system in terms that map to real components.
6. Specify responsive behavior.
7. Produce a frontend-aware handoff package.
8. Run design review before marking the work complete.

## Design Output Contract

The agent should usually return these sections:

- objective;
- primary user path;
- sitemap or section structure;
- wireframe;
- UI system;
- responsive behavior;
- implementation notes;
- open questions.

## Wireframe Rule

The wireframe should explain layout and hierarchy clearly enough that another agent or frontend engineer can reproduce the structure without guessing the intended flow.

## UI System Rule

The UI system should use implementation-facing language.

Prefer:

- section patterns;
- component names;
- state descriptions;
- spacing and hierarchy rules;
- reusable tokens or roles when relevant.

Avoid vague outputs such as:

- "make it modern";
- "clean and premium";
- "add nice animations";
- any style language not tied to actual page behavior.

## Frontend-Aware Handoff Rule

The design must acknowledge implementation reality.

At minimum, include:

- component inventory;
- layout behavior;
- important states;
- accessibility-sensitive elements;
- responsive rules;
- ambiguity or risk notes.

## Review Before Completion

Before completion, the agent must check:

- whether the design supports the stated goal;
- whether the CTA path is clear;
- whether any section exists only for visual filler;
- whether the layout remains coherent on mobile;
- whether the design can plausibly be implemented in a normal frontend stack.

## Anti-Patterns

Do not:

- jump straight from prompt to polished UI with no page logic;
- produce long style prose with no structure;
- hide missing reasoning behind aesthetic language;
- invent interaction details that the goal does not need;
- over-design an MVP page that only needs one clear action.

## Final Rule

Design decisions must survive both user scrutiny and frontend implementation.
