# Website Design Pipeline

## Purpose

This pipeline defines the default flow for turning a website idea into a buildable and reviewable design package.

## Core Flow

```text
idea
-> website goal
-> user scenario
-> sitemap or page structure
-> wireframe
-> UI system
-> responsive spec
-> frontend handoff
-> design review
```

## Stage 1 - Website Goal

Define:

- the business or product outcome;
- the page or site type;
- the primary conversion or success action;
- the main audience;
- the biggest failure mode to avoid.

Output:

- one short goal statement;
- one primary action;
- one scope boundary.

## Stage 2 - User Scenario

Describe the main user path in plain language:

- where the user comes from;
- what they already know;
- what question or doubt they have;
- what they need to understand before acting;
- what action they should take next.

Output:

- one primary scenario;
- optional secondary scenarios only if they materially change page structure.

## Stage 3 - Sitemap Or Page Structure

Decide the smallest page set or section set that supports the goal.

For single-page work, this may be a section map instead of a multi-page sitemap.

Define:

- required pages or sections;
- order of information;
- relationship between pages or sections;
- where trust, proof, pricing, FAQ, or CTA elements belong.

Output:

- sitemap or ordered section list with short purpose notes.

## Stage 4 - Wireframe

Create a low-fidelity structure before visual styling.

Focus on:

- hierarchy;
- content grouping;
- CTA placement;
- scan path;
- section sequencing;
- essential states such as empty, loading, comparison, or expanded detail when relevant.

Avoid:

- premature color decisions;
- ornamental illustration decisions;
- pixel-level polishing before structure is stable.

Output:

- section-by-section wireframe notes, ASCII wireframe, or structured layout description.

## Stage 5 - UI System

Only after wireframe stability, define the visual and component system.

Cover:

- visual direction;
- typography roles;
- spacing rhythm;
- color roles;
- component families;
- interaction states;
- icon or media usage rules.

Output:

- compact UI system spec tied to the wireframe, not detached moodboard language.

## Stage 6 - Responsive Spec

Define how the design behaves across screen sizes.

Minimum coverage:

- mobile;
- tablet when relevant;
- desktop.

State:

- section stacking behavior;
- nav behavior;
- grid collapse rules;
- priority changes for content;
- interaction differences if any.

Output:

- responsive behavior notes for each important page or section.

## Stage 7 - Frontend Handoff

Translate the design into implementation-facing guidance.

Include:

- page and section inventory;
- component inventory;
- state and interaction notes;
- content constraints;
- accessibility concerns that affect structure;
- implementation risks or unanswered design questions.

Output:

- frontend-aware handoff package that reduces guesswork for the builder.

## Stage 8 - Design Review

Review the result against:

- goal fit;
- clarity;
- user-path coherence;
- usability;
- responsive behavior;
- component consistency;
- buildability.

If a design fails review, return to the narrowest broken stage rather than restarting from zero.

## Minimal Deliverable Shape

The default lightweight package is:

1. goal and user scenario;
2. sitemap or section map;
3. wireframe notes;
4. UI system notes;
5. responsive notes;
6. frontend handoff notes;
7. review findings.

## Final Rule

Lock structure before surface polish, and lock handoff before calling the design done.
