# Impeccable Design QA Gate

## Purpose

This file defines how `Project Execution OS` uses Impeccable as a design-quality gate for AI-coded frontend work.

The goal is to prevent visible AI-built interfaces from shipping as generic, unreviewed UI when the work includes a landing page, website, SaaS page, dashboard, onboarding flow, settings page, portfolio, or other user-facing web surface.

This gate runs after frontend implementation. When appropriate, the implementation phase may first use `TASTE_FRONTEND_EXECUTION_STANDARD.md` as bounded generation-time guidance.

## Source Trail

- Source article: `https://pimenov.ai/knowledge/impeccable-dizajn-skill-dlya-ai-kodinga/`
- Official repository: `https://github.com/pbakaus/impeccable`
- Captured for Project Execution OS on: `2026-07-02`

## Status

`candidate`

This gate is reusable guidance inside the Design Block. Project-specific installation remains a per-project decision.

## What Impeccable Adds

Impeccable is an external design-guidance skill for AI coding agents. At capture time, the official repository described it as a setup flow plus a shared `/impeccable` command vocabulary, deterministic detector rules, and integrations for common AI coding tools.

Useful commands include:

```text
/impeccable init
/impeccable document
/impeccable shape
/impeccable craft
/impeccable critique
/impeccable audit
/impeccable polish
/impeccable harden
/impeccable adapt
/impeccable optimize
```

The external tool can change. Re-check the official repository before production installation.

## When To Use

Use this gate when AI implements, refactors, polishes, or reviews:

- landing pages;
- marketing websites;
- SaaS or product websites;
- dashboards;
- onboarding flows;
- settings pages;
- intake flows;
- portfolio sites;
- client-facing tools;
- any visible frontend where first impression, clarity, accessibility, and responsive behavior matter.

## When Not To Use

Do not use this gate for backend-only work, scripts, infrastructure, database work, decorative image generation, early brainstorming before the product/user path is known, or tiny text-only UI edits where a full gate would be ceremony.

If Impeccable is unavailable, use the manual fallback gate below instead of claiming the tool was used.

## Core Rule

Frontend AI-coding work should not be treated as design-ready until it passes one of these:

```text
Impeccable-backed gate
```

or

```text
manual fallback gate based on the same quality criteria
```

Do not claim that Impeccable was run unless the executor actually ran it or verified an existing generated report.

## Placement In The Design Chain

Recommended chain:

```text
goal
-> user scenario
-> donor research if needed
-> page strategy
-> section plan / wireframe
-> UI system direction
-> implementation handoff
-> bounded Taste-guided execution when appropriate
-> frontend implementation
-> Impeccable design QA gate
-> final review / release decision
```

This gate does not replace the upstream Design Block or generation-time execution guidance. It protects downstream implementation from drifting into generic AI-coded UI and catches visible issues that remain after coding.

## Relationship To Taste Frontend Execution

`TASTE_FRONTEND_EXECUTION_STANDARD.md` and this gate have different roles:

```text
Taste guidance = generation-time direction
Impeccable = post-implementation design QA
```

Taste may be excluded, product-safe partial, redesign, or full marketing mode depending on the surface.

Impeccable remains the release-bound QA layer for all relevant visible frontend work, including dashboards and product UI where the full external Taste Skill is not appropriate.

A Taste pre-flight result does not count as an Impeccable pass.

## New Frontend Project Flow

When Impeccable is approved for a new frontend project:

```bash
npx impeccable install
```

Then inside the active AI coding tool:

```text
/impeccable init
/impeccable shape <target surface>
/impeccable craft <target surface>
```

Expected durable context artifacts may include:

```text
PRODUCT.md
DESIGN.md
.impeccable/config.json
.impeccable/design.json
.impeccable/critique/*.md
```

`PRODUCT.md` and `DESIGN.md` must be grounded in the project purpose, audience, brand/product lane, user path, selected references, rejected references, and implementation constraints.

When Taste-guided execution is also approved, `DESIGN.md` or the implementation handoff should additionally record the selected Taste mode and, when relevant, `DESIGN_VARIANCE`, `MOTION_INTENSITY`, and `VISUAL_DENSITY`.

## Existing Frontend Project Flow

For an existing UI:

```bash
npx impeccable install
```

Then inside the active AI coding tool:

```text
/impeccable document
/impeccable critique <target surface>
/impeccable polish <target surface>
/impeccable audit <target surface>
/impeccable harden <target surface>
/impeccable adapt <target surface>
```

Use this when the project needs to preserve an existing visual language instead of replacing it with a new one.

If Taste redesign guidance was used before this gate, preserve its audit-first evidence and review whether the targeted fixes actually improved the rendered surface without breaking functionality.

## CLI Detector Flow

For deterministic checking without relying on an LLM:

```bash
npx impeccable detect src/
npx impeccable detect index.html
npx impeccable detect https://example.com
npx impeccable detect --json .
```

Use JSON output when the result should be attached to CI, a GitHub issue, a PR, or a handoff packet.

## Minimum Gate Checklist

A frontend surface passes this gate only if the executor can answer yes to all relevant items:

1. Product context exists and was used.
2. Design context exists and was used.
3. The main user path is clear.
4. The page has visual hierarchy, not just a stack of cards.
5. Typography choices are intentional and readable.
6. Color choices are intentional and accessible.
7. Spacing and rhythm feel designed, not default.
8. Components have states where relevant: hover, focus, loading, empty, error, disabled.
9. Text overflow and long-content cases are handled.
10. Mobile and desktop behavior are checked.
11. Accessibility basics are checked: contrast, focus, touch targets, heading order, labels.
12. Obvious generic AI-design patterns are removed or justified.
13. Detector warnings are fixed or explicitly waived with a reason.
14. Any Taste mode, profile, or pre-flight record used during implementation is consistent with the actual product surface.
15. The final handoff records what was checked and what remains unresolved.

## Fail Conditions

Fail the gate if any of these are true:

- the UI was polished without product/design context;
- the result is described only as "clean", "modern", or "beautiful" without user-path evidence;
- mobile behavior is assumed but not checked;
- accessibility issues are ignored;
- detector findings are dismissed without a written reason;
- a marketing Taste profile was applied to a dashboard or workflow UI without justification;
- the executor claims Taste or Impeccable ran but provides no command, report, commit, or other evidence.

## Manual Fallback Gate

If Impeccable cannot be installed or run, the executor must still perform a manual pass:

```text
1. Read PRODUCT.md / DESIGN.md, or create a project-grounded equivalent if they do not exist.
2. Review hierarchy, clarity, typography, color, layout, states, responsiveness, and accessibility.
3. Identify generic AI-design patterns.
4. Review any Taste mode or profile used during implementation and confirm it fit the surface.
5. Fix what can be fixed immediately.
6. Record unresolved issues and reasons.
```

The final report must say:

```text
Impeccable not run; manual fallback gate used.
```

## Required Handoff Record

When this gate is used, include this compact record in the handoff, PR, issue, or `logs/latest.md` when relevant:

```text
Design QA Gate:
- Gate used: Impeccable | manual fallback
- Target surface:
- Product context checked: yes/no/path
- Design context checked: yes/no/path
- Taste guidance used: excluded | product-safe partial | redesign | marketing full | no
- Taste pre-flight path or result:
- Commands run:
- Detector result:
- Key fixes made:
- Waivers:
- Remaining design risks:
- Next safe action:
```

## Relationship To Existing Design Block Files

Use this file with the existing Design Block instead of replacing it.

Minimum related files:

```text
blocks/design/BLOCK.md
blocks/design/WEBSITE_DESIGN_PIPELINE.md
blocks/design/DESIGN_AGENT_STANDARD.md
blocks/design/IMPLEMENTATION_HANDOFF.md
blocks/design/TASTE_FRONTEND_EXECUTION_STANDARD.md
blocks/design/WEBSITE_REVIEW_CHECKLIST.md
blocks/design/DESIGN_REVIEW_STANDARD.md
```

Use only the files needed for the active task.

## Final Rule

Do not let AI-coded frontend work pass as finished merely because it compiles.

A visible user-facing surface must also survive design QA: context, hierarchy, usability, accessibility, responsiveness, and non-generic visual intent.
