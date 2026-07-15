# Taste Frontend Execution Standard

## Purpose

This standard defines how `Project Execution OS` may use the external Taste Skill approach to guide AI coding agents during frontend implementation without allowing one author's visual preferences to override product context, usability, accessibility, performance, or the existing project stack.

The goal is to reduce generic AI-coded frontend output while keeping design decisions traceable, contextual, reviewable, and compatible with the existing Design Block and Impeccable Design QA Gate.

## Source Trail

- Source article: `https://pimenov.ai/knowledge/taste-skill-anti-slop-frontend/`
- Official repository: `https://github.com/Leonxlnx/taste-skill`
- Primary source reviewed: `skills/taste-skill/SKILL.md`
- Redesign source reviewed: `skills/redesign-skill/SKILL.md`
- Strict GPT variant reviewed: `skills/gpt-tasteskill/SKILL.md`
- Captured for Project Execution OS on: `2026-07-14`

## Status

`candidate`

The upstream default skill is experimental and can change. This file is the stable Project Execution OS interpretation. Production projects must not silently inherit future upstream changes.

## Core Decision

Taste Skill is not the design strategy, product specification, component library, or final quality gate.

Its approved role is a bounded frontend execution layer:

```text
goal and user scenario
-> donor research and selected visual direction
-> page strategy and UI system
-> implementation handoff
-> Taste-guided frontend execution when appropriate
-> Impeccable or manual design QA gate
-> final review and release decision
```

`Project Execution OS` decides what should be built and why.

Taste guidance helps the coding agent avoid generic visual defaults while implementing it.

Impeccable or the manual fallback gate checks the visible result after implementation.

## When To Use

Use this standard for:

- marketing landing pages;
- product marketing sites;
- portfolios and presentation websites;
- campaign or launch pages;
- visual redesigns of existing marketing surfaces;
- brand-forward pages where typography, composition, imagery, and motion materially affect the outcome;
- selected product surfaces when only the bounded product-safe rules below are enabled.

## When Not To Use

Do not apply the full Taste Skill behavior to:

- dashboards;
- admin panels;
- data tables;
- dense analytics interfaces;
- multi-step product workflows;
- accessibility-critical or regulated interfaces without substantial restriction;
- tiny UI edits where the full process would add ceremony;
- backend-only, infrastructure, script, or database work.

For these surfaces, use the product specification, the existing design system, and the Impeccable or manual QA gate. Only selected product-safe rules may be borrowed.

## Scope Modes

### Mode A: Marketing Full

Use for landing pages, portfolios, campaign pages, and brand-forward marketing sites.

Allowed:

- Design Read;
- Taste Profile dials;
- composition diversification;
- typography and palette discipline;
- visual asset planning;
- restrained motion based on the brief;
- full anti-slop pre-flight.

Not automatically allowed:

- mandatory GSAP;
- mandatory cinematic motion;
- random visual choices;
- arbitrary stack migration;
- unlicensed fonts.

### Mode B: Existing Surface Redesign

Use for an existing visible frontend that must preserve functionality and most of its visual language.

Required sequence:

```text
Scan -> Diagnose -> Fix -> Test -> QA
```

Rules:

- inspect the current framework, styling approach, dependencies, design tokens, and component patterns first;
- list concrete visual and interaction problems before editing;
- work with the existing stack;
- prefer small, reviewable changes over rewrites;
- test after each bounded change set;
- document any intentional visual-language change.

### Mode C: Product-Safe Partial

Use for SaaS product pages, Chrome extension interfaces, command centers, internal tools, and other functional product UI.

Allowed rules:

- Design Read;
- hierarchy and typography discipline;
- one coherent palette and radius logic;
- dependency verification;
- hover, focus, active, loading, empty, error, and disabled states;
- responsive behavior;
- accessibility checks;
- import and asset verification;
- anti-repetition review;
- final pre-flight.

Disabled by default:

- AIDA as a universal page structure;
- mandatory GSAP or scroll hijacking;
- mandatory imagery;
- huge cinematic spacing;
- forced asymmetry;
- visual randomization;
- motion on every clickable element;
- marketing-specific hero rules.

### Mode D: Excluded

For data-heavy dashboards, admin panels, regulated workflows, and tables, do not install or invoke the full external Taste Skill.

Use the project design system and a product-oriented QA checklist instead.

## Required Pre-Code Output

Before an AI coding agent writes or changes a substantial visible frontend, it must produce a compact Design Read.

```text
Design Read:
- Surface:
- Audience:
- Primary user action:
- Product or brand lane:
- Selected donor references:
- Existing design system or stack:
- Accessibility or regulatory constraints:
- Taste mode: Marketing Full | Existing Surface Redesign | Product-Safe Partial | Excluded
```

If the direction cannot be inferred and materially different interpretations would produce different work, ask exactly one clarifying question.

Do not ask when the existing specification, donor record, or project context already resolves the direction.

## Taste Profile

For approved scopes, record these three parameters in the project `DESIGN.md`, implementation handoff, or equivalent durable project artifact:

```text
Taste Profile:
- DESIGN_VARIANCE: 1-10
- MOTION_INTENSITY: 1-10
- VISUAL_DENSITY: 1-10
- Rationale:
```

Definitions:

- `DESIGN_VARIANCE`: 1 means highly conventional and symmetrical; 10 means highly experimental and compositionally irregular.
- `MOTION_INTENSITY`: 1 means nearly static; 10 means cinematic, scroll-driven, and physics-heavy.
- `VISUAL_DENSITY`: 1 means highly spacious; 10 means information-dense.

The agent may recommend values but must not silently change approved project values during implementation.

Suggested starting ranges:

| Surface | Variance | Motion | Density |
|---|---:|---:|---:|
| Mainstream SaaS landing | 6-7 | 4-6 | 3-4 |
| Creative agency landing | 8-9 | 6-8 | 3-4 |
| Premium consumer landing | 6-8 | 4-6 | 3-4 |
| Developer portfolio | 5-7 | 4-6 | 3-4 |
| Existing redesign, preserve | match existing | existing +0 to +1 | match existing |
| Product UI | 3-5 | 1-3 | 4-7 |
| Accessibility-critical UI | 2-4 | 1-2 | 4-6 |

## Rule Levels

Every imported Taste rule must be classified as one of these:

### Mandatory

Applies whenever relevant:

- understand the brief before coding;
- use the approved project stack and design system;
- verify dependencies before importing them;
- verify font and asset licensing;
- preserve accessibility fundamentals;
- implement relevant component states;
- define responsive behavior explicitly;
- avoid broken contrast, overflow, wrapping, and horizontal scroll;
- test functionality after redesign changes;
- record what was checked.

### Recommended

Normally useful but may be waived with a reason:

- avoid automatic AI-purple gradients;
- avoid repeated three-equal-card layouts;
- avoid making every section use the same composition;
- avoid unnecessary card containers;
- keep one coherent accent and neutral family;
- keep radius, icon, and shadow logic consistent;
- keep body copy at readable line lengths;
- use semantic HTML;
- use real content rather than lorem ipsum;
- prefer layout and spacing fixes before adding decorative effects.

### Contextual

Use only when supported by the brief:

- asymmetric hero layouts;
- bento composition;
- serif display typography;
- kinetic typography;
- generated hero imagery;
- GSAP, scroll pinning, horizontal scroll, magnetic hover, or other advanced motion;
- strict hero copy-length limits;
- AIDA page structure;
- cinematic section spacing;
- texture, grain, glass, mesh gradients, or other material effects.

No contextual rule becomes mandatory merely because it appears in an external skill.

## Protected Boundaries

### Existing Stack

Do not migrate React, Next.js, Tailwind, CSS modules, vanilla CSS, or another styling system solely because the upstream skill prefers a different stack.

Use official design-system packages when the project explicitly belongs to that ecosystem and the choice is approved. Do not mix multiple full design systems in one component tree without a documented architecture decision.

### Dependencies

Before importing any package:

1. inspect the project's dependency file;
2. confirm the package is present or add an explicit installation step;
3. verify framework and major-version compatibility;
4. avoid introducing a large animation or UI dependency for a minor visual effect.

### Font Licensing

A font named in an external skill is not automatically licensed for production.

Use only:

- already licensed brand fonts;
- open-source fonts with verified web-use terms;
- system fonts;
- fonts approved through a separate licensing decision.

Record any commercial font dependency in the project handoff.

### Motion

Motion must communicate hierarchy, state, continuity, or brand intent.

Do not add motion merely to make the interface appear expensive.

Required safeguards:

- honor `prefers-reduced-motion`;
- avoid scroll hijacking unless explicitly approved;
- prefer `transform` and `opacity` for animation;
- isolate client-side animation code in frameworks that distinguish server and client components;
- verify mobile performance;
- do not require GSAP for surfaces that can be implemented cleanly with CSS or a lighter existing dependency.

### Image-First Work

Image-first design is optional, not universal.

Use it when visual direction cannot be resolved through existing brand assets or donor references and the surface is marketing-oriented.

Do not require generated imagery for dashboards, utilities, settings, forms, tables, or other function-first surfaces.

Generated assets must still be checked for relevance, consistency, licensing, accessibility, crop behavior, and responsive use.

## Anti-Slop Pre-Flight

Before implementation is handed to the final QA gate, the executor must check all relevant items.

### Context

- The Design Read matches the actual project brief.
- The selected mode is appropriate for the surface.
- Approved donor references and existing brand assets were used.
- The implementation does not substitute the agent's favorite aesthetic for the audience's needs.

### Layout

- The page does not repeat the same section family without a reason.
- Marketing pages are not built only from equal cards.
- Multi-column sections have explicit mobile behavior.
- No accidental horizontal scrolling exists.
- Navigation, hero, CTAs, and dense sections fit their intended viewports.
- Bento or grid layouts contain no unexplained empty cells.

### Typography and Content

- Heading scale and line breaks are intentional.
- Paragraph line length is readable.
- Buttons do not wrap unexpectedly on desktop.
- Copy is specific and not generic AI marketing language.
- No placeholder content, fake links, or unexplained sample data remains.
- Fonts used are available and licensed.

### Color and Shape

- Text and interactive controls meet required contrast.
- Accent, neutral, corner-radius, icon, and shadow logic are coherent.
- AI-purple, beige-luxury, glass, or other fashionable palettes are present only when justified by the brief.
- Visual effects do not obscure function or readability.

### Interaction and States

- Relevant hover, focus, active, loading, empty, error, success, and disabled states exist.
- Keyboard focus is visible.
- Form labels are not replaced by placeholders.
- Error messages are direct and contextual.
- Motion has a reduced-motion path.

### Technical Integrity

- Every import resolves.
- Dependencies and versions were verified.
- Semantic elements and useful alternative text are present.
- Mobile behavior was tested rather than assumed.
- Existing functionality still works after redesign.
- No debug code, dead code, fake destinations, or arbitrary z-index escalation remains.

## Relationship To Impeccable

Taste-guided execution and Impeccable are complementary.

```text
Taste guidance = generation-time direction
Impeccable = post-implementation design QA
```

The Taste pre-flight does not replace the `IMPECCABLE_DESIGN_QA_GATE.md` process.

A release-bound or owner-facing frontend must still pass:

```text
Impeccable-backed gate
```

or:

```text
manual fallback gate
```

Do not claim either tool or skill was run without command, report, commit, or other evidence.

## Upstream Version Control

Do not depend on an unpinned upstream `main` branch for production behavior.

Approved options:

1. use this stable internal standard without installing the external skill;
2. pin the external repository to a reviewed commit;
3. copy a reviewed `SKILL.md` into the project and record its source commit;
4. install a named upstream skill only after verifying its current content.

When upstream changes are adopted, record:

```text
- upstream repository
- skill name
- commit or version
- date reviewed
- material changes
- Project Execution OS rules retained, changed, or rejected
```

## Recommended Project Handoff Record

```text
Taste Frontend Execution:
- Mode:
- Target surface:
- Design Read path:
- Taste Profile path:
- Upstream skill installed: yes/no
- Upstream skill name and commit:
- Existing stack preserved: yes/no
- Dependencies added:
- Fonts and licensing checked:
- Motion safeguards checked:
- Anti-slop pre-flight result:
- Waivers:
- Next QA gate: Impeccable | manual fallback
- Remaining design risks:
```

## Fail Conditions

Fail this execution layer when any of these are true:

- the agent starts coding before understanding the surface and audience;
- a marketing-oriented Taste profile is applied to a dashboard or workflow UI;
- existing functionality or stack is replaced without approval;
- GSAP, imagery, or cinematic motion is treated as mandatory by default;
- unlicensed or unavailable fonts are used;
- accessibility or mobile behavior is ignored;
- upstream behavior changed without version review;
- the executor claims a Taste or Impeccable pass without evidence;
- the result is visually novel but less clear, usable, performant, or maintainable.

## Final Rule

Use Taste to correct AI defaults, not to create a new default.

The interface must remain grounded in the product, audience, selected references, existing stack, accessibility requirements, and measurable user path.
