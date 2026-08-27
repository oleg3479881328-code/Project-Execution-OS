# Taste Frontend Execution Standard

## Purpose

This standard defines how `Project Execution OS` guides AI coding agents during frontend implementation without allowing generic model defaults, one author's taste, or a component library's demo aesthetic to override product context, usability, accessibility, performance, brand, or the existing project stack.

The goal is to reduce generic AI-coded frontend output while keeping design decisions traceable, contextual, reviewable, and compatible with the existing Design Block and Impeccable Design QA Gate.

## Source Trail

Original reviewed source:

- Source article: `https://pimenov.ai/knowledge/taste-skill-anti-slop-frontend/`
- Official repository: `https://github.com/Leonxlnx/taste-skill`
- Primary source reviewed: `skills/taste-skill/SKILL.md`
- Redesign source reviewed: `skills/redesign-skill/SKILL.md`
- Strict GPT variant reviewed: `skills/gpt-tasteskill/SKILL.md`
- Captured for Project Execution OS on: `2026-07-14`

Additional independent review completed `2026-08-27`:

- UI Skills: `https://www.ui-skills.com/` — agent-oriented catalog/router for design-engineering skills, with CLI and MCP paths.
- shadcn/ui: `https://ui.shadcn.com/` — open-code component and distribution system; component source is copied into the project and is directly editable by agents.
- coss ui: `https://coss.com/ui` — modern Base UI-based system for developers and AI; shadcn CLI compatible; useful as an optional extension, not a mandatory base.
- Design System Checklist: `https://www.designsystemchecklist.com/` — reference checklist for design-system coverage; use as an audit frame, not as a substitute for project requirements.
- Beautiful UI: `https://www.beautifului.dev/` — components aimed at AI-native interfaces, including streaming, approval, tool, task, chat, flowchart, code and table patterns.
- beUI: `https://beui.dev/` — open-source React/Next motion components distributed through shadcn; useful selectively for interaction patterns.
- Rare UI: `https://www.rareui.com/` — small open-source set of distinctive animated React components installable through shadcn CLI; novelty layer only.
- Transitions.dev: `https://transitions.dev/` — copyable UI transitions plus an agent skill; use selectively for purposeful microinteraction patterns.
- Emil Kowalski, `You Don't Need Animations`: `https://emilkowal.ski/ui/you-dont-need-animations` — motion should have a purpose; common UI animation should generally remain under 300ms; frequent actions may be better without animation.
- Emil Kowalski, `Agents with Taste`: `https://emilkowal.ski/ui/agents-with-taste` — concrete agent-facing motion guidance and duration ranges.

## Status

`approved internal standard; external tools remain conditional`

The internal rules below are stable Project Execution OS policy. External libraries, catalogs and skills are not automatically approved dependencies. Their current version, compatibility, license, accessibility and maintenance status must be checked at implementation time.

## Core Decision

Do not solve AI design weakness with a stronger aesthetic prompt alone.

Use a constrained execution stack:

```text
product goal + user scenario
-> Existing Solution First
-> existing brand/design evidence
-> donor/reference research
-> compact Design Read
-> design-system rules/tokens
-> approved component primitives
-> optional specialist components
-> purposeful motion only
-> implementation
-> anti-slop pre-flight
-> Impeccable/manual visual QA
-> release decision
```

The agent is not allowed to treat its learned visual median as the design direction.

## UI Toolkit Hierarchy

### Layer 0 — Existing Solution First

Before generating a new component or visual pattern, inspect in this order:

1. existing project components and tokens;
2. existing project design system and brand assets;
3. previously approved Project Execution OS design patterns;
4. suitable established external components/patterns;
5. custom creation only when the above are insufficient.

Do not rebuild a solved UI pattern merely because generation is easy.

### Layer 1 — Rules and Judgment

Preferred sources:

- current project design specification;
- UI Skills, when its smallest relevant skill improves execution;
- Design System Checklist as coverage audit;
- Emil Kowalski motion principles;
- this Project Execution OS standard.

These sources guide decisions. They do not choose the product's visual identity.

### Layer 2 — Base Components

For compatible React projects without an established competing system, `shadcn/ui` is the preferred candidate base because the component source becomes project-owned open code and is straightforward for coding agents to inspect and modify.

This is a preference, not a forced migration rule.

Never migrate an existing design system to shadcn solely because this standard mentions it.

### Layer 3 — Optional Extensions

Use only when a concrete requirement is not cleanly covered by the existing system/base:

- `coss ui` — broader modern primitives/patterns;
- `Beautiful UI` — AI-native application surfaces;
- `beUI` — motion-rich interaction components;
- `Rare UI` — rare/distinctive effects.

Do not mix libraries casually. Imported components must be normalized to project tokens, accessibility rules, interaction behavior and visual language.

### Layer 4 — Motion

Use `Transitions.dev`, beUI motion patterns, or equivalent existing project solutions only after the interaction purpose is identified.

Motion must communicate at least one of:

- state;
- continuity;
- hierarchy;
- spatial relationship;
- progress/feedback;
- intentional brand expression on an appropriate marketing surface.

If none applies, default to no animation.

## Required Pre-Code Output

Before an AI coding agent writes or changes a substantial visible frontend, it must produce a compact Design Read.

```text
Design Read:
- Surface:
- Audience:
- Primary user action:
- Product or brand lane:
- Existing components/tokens found:
- Selected donor references:
- Base component source:
- Optional specialist components required:
- Accessibility or regulatory constraints:
- Motion purpose, if any:
- Taste mode: Marketing Full | Existing Surface Redesign | Product-Safe Partial | Excluded
```

If the direction cannot be inferred and materially different interpretations would produce different work, ask exactly one clarifying question.

Do not ask when the existing specification, donor record, or project context already resolves the direction.

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

Required sequence:

```text
Scan -> Diagnose -> Fix -> Test -> QA
```

Inspect the current framework, styling, dependencies, design tokens and component patterns first. List concrete problems before editing. Prefer bounded changes over rewrites and preserve functionality.

### Mode C: Product-Safe Partial

Use for SaaS product pages, command centers, internal tools and other functional product UI.

Allowed:

- hierarchy and typography discipline;
- coherent palette/radius logic;
- verified components;
- hover, focus, active, loading, empty, error and disabled states;
- responsive behavior;
- accessibility checks;
- anti-repetition review;
- final pre-flight.

Disabled by default:

- AIDA as universal structure;
- mandatory GSAP or scroll hijacking;
- mandatory imagery;
- huge cinematic spacing;
- forced asymmetry;
- visual randomization;
- motion on every clickable element.

### Mode D: Excluded

For data-heavy dashboards, regulated workflows and dense tables, do not invoke a full marketing-oriented Taste behavior. Use the project design system and product-oriented QA.

## Taste Profile

For approved scopes, record:

```text
Taste Profile:
- DESIGN_VARIANCE: 1-10
- MOTION_INTENSITY: 1-10
- VISUAL_DENSITY: 1-10
- Rationale:
```

Suggested ranges:

| Surface | Variance | Motion | Density |
|---|---:|---:|---:|
| Mainstream SaaS landing | 6-7 | 4-6 | 3-4 |
| Creative agency landing | 8-9 | 6-8 | 3-4 |
| Premium consumer landing | 6-8 | 4-6 | 3-4 |
| Developer portfolio | 5-7 | 4-6 | 3-4 |
| Existing redesign | match existing | existing +0 to +1 | match existing |
| Product UI | 3-5 | 1-3 | 4-7 |
| Accessibility-critical UI | 2-4 | 1-2 | 4-6 |

## Anti-Slop Hard Gate

The following defaults are forbidden unless justified by project evidence or an explicit design decision:

- blue/purple/indigo gradient as an automatic AI aesthetic;
- Inter or another default font chosen only because it is convenient;
- glassmorphism used as generic decoration;
- every content group placed inside a rounded card;
- repeated three-equal-card sections without information-architecture reason;
- identical section composition repeated down the page;
- generic `hero -> logos -> features -> testimonials -> CTA` skeleton used without content/strategy justification;
- oversized rounded corners everywhere;
- arbitrary glow, blur, mesh gradient, grain or shadow effects;
- decorative dashboard charts or fake metrics;
- meaningless badges/pills above headings;
- placeholder copy presented as production content;
- animation added only to make the interface look premium;
- component-library demo styling shipped without adapting it to the project.

Passing the gate does not require being visually unusual. It requires every major visual choice to be explainable by the product, audience, brand, content, interaction or selected reference direction.

## Design System Minimum Coverage

For substantial new surfaces, verify at minimum:

- color roles and contrast;
- typography roles and scale;
- spacing system;
- sizing/container logic;
- radii;
- borders and shadows;
- icon treatment;
- responsive breakpoints/behavior;
- interactive states;
- form states and validation;
- loading/empty/error/success states where relevant;
- focus and keyboard behavior;
- motion tokens/rules if motion exists;
- image/illustration treatment if visual assets exist.

A checklist is a coverage tool, not proof of design quality.

## Motion Standard

Motion must be purposeful and fast.

Default guidance from reviewed Emil Kowalski material:

- micro-interactions: roughly 100-150ms;
- common UI such as tooltips/dropdowns: roughly 150-250ms;
- modals/drawers: roughly 200-300ms;
- common UI animation should generally stay under 300ms;
- repeated high-frequency actions may need no animation;
- exit can often be faster than entrance;
- honor `prefers-reduced-motion`;
- prefer compositor-friendly `transform` and `opacity` where appropriate;
- do not introduce a large animation dependency for a minor effect.

These are defaults, not immutable laws.

## Component Import Gate

Before importing any external UI component:

1. confirm an equivalent does not already exist locally;
2. verify framework/version compatibility;
3. verify dependency cost;
4. inspect accessibility and keyboard behavior;
5. inspect responsive behavior;
6. verify license and asset/font rights;
7. normalize tokens and styling to the project;
8. remove demo-only effects/content;
9. test relevant states;
10. record the source when the component becomes an approved reusable pattern.

## Anti-Slop Pre-Flight

Before final QA, verify:

### Context
- Design Read matches the brief.
- Existing solutions were inspected first.
- Donor/brand evidence was used where available.
- Agent preference did not replace audience/product needs.

### Layout
- Repetition has a reason.
- Mobile behavior is explicit.
- No accidental horizontal scroll.
- Navigation, hero, CTAs and dense sections fit target viewports.

### Typography and Content
- Heading scale/line breaks are intentional.
- Paragraph line length is readable.
- Buttons do not wrap unexpectedly.
- Copy is specific, not generic AI marketing language.
- No unexplained placeholder content remains.
- Fonts are available and licensed.

### Color and Shape
- Contrast is adequate.
- Accent, neutral, radius, icon and shadow logic are coherent.
- AI-purple, beige-luxury, glass or other fashionable defaults appear only when justified.

### Interaction and States
- Relevant hover/focus/active/loading/empty/error/success/disabled states exist.
- Keyboard focus is visible.
- Labels are not replaced by placeholders.
- Motion has a reduced-motion path.

### Technical Integrity
- Imports resolve.
- Dependencies/versions are verified.
- Semantic elements and useful alt text are present.
- Mobile behavior was tested.
- Existing functionality still works.
- No debug code, fake destinations or arbitrary z-index escalation remains.

## Relationship To Impeccable

```text
Taste/UI guidance = generation-time direction
Anti-Slop Gate = implementation sanity check
Impeccable = post-implementation visual QA
```

A release-bound or owner-facing frontend must still pass the Impeccable-backed gate or documented manual fallback. Never claim a tool/skill was run without evidence.

## Upstream Version Control

Do not depend on an unpinned external `main` branch for production behavior. Pin reviewed versions/commits where practical and record material upstream changes before adopting them.

## Fail Conditions

Fail the execution layer when any of these are true:

- coding starts before the surface and audience are understood;
- Existing Solution First was skipped;
- an external component was imported merely because it looked impressive;
- a marketing aesthetic was applied to a workflow UI;
- existing functionality or stack was replaced without approval;
- animation, imagery or cinematic motion was treated as mandatory;
- unavailable/unlicensed fonts or assets were used;
- accessibility/mobile behavior was ignored;
- a component-library demo aesthetic was mistaken for the project's design system;
- the result is visually novel but less clear, usable, performant or maintainable.

## Final Rule

Use design guidance to correct AI defaults, not to create a new default.

The best interface is not the one that looks least like AI. It is the one whose visual and interaction decisions are grounded in the product, audience, brand, selected references, existing stack, accessibility requirements and measurable user path.