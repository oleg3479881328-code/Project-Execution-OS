# Design Review Standard

## Purpose

This standard defines how an agent reviews an existing website or page design clearly and practically.

## Review Goal

The review should identify whether the design is:

- aligned to its goal;
- understandable to the user;
- structurally coherent;
- visually consistent;
- responsive;
- realistically buildable.

## Review Order

Review in this order:

1. goal fit;
2. user path;
3. page structure;
4. wireframe or layout hierarchy;
5. UI system consistency;
6. responsive behavior;
7. frontend handoff quality.

## Findings Format

For each finding, state:

- severity;
- what is wrong;
- why it matters;
- what change would fix or reduce it.

Prefer practical language over taste-based commentary.

## Review Checklist

### Goal Fit

Check:

- Is the primary action obvious?
- Does the page spend enough space on the decision the user must make?
- Is any important proof or context missing before the CTA?

### User Path

Check:

- Does the information appear in a sensible order?
- Are questions answered before the CTA asks for commitment?
- Is the user forced to infer too much from visuals alone?

### Structure And Wireframe

Check:

- Are sections distinct and purposeful?
- Is hierarchy visible at a glance?
- Are there filler sections or duplicated content blocks?
- Does the page scan cleanly?

### UI System

Check:

- Are components consistent across the page?
- Do typography, spacing, and color roles behave like a system?
- Are emphasis and contrast used intentionally rather than everywhere?

### Responsive Behavior

Check:

- Does the layout still work on mobile?
- Are CTA, nav, and proof sections still easy to reach?
- Do grids, cards, or comparison tables collapse sensibly?

### Buildability

Check:

- Can this be built with standard frontend techniques?
- Are key interactions defined well enough to implement?
- Does the design depend on unrealistic one-off behavior or hidden assumptions?

## Output Shape

A useful review usually contains:

- brief context;
- ordered findings;
- open questions;
- pass / revise recommendation.

## Boundary

This standard is for product and execution-oriented design review.

It is not a substitute for brand critique, visual-art critique, or stakeholder preference debates.

## Final Rule

Review the design the user must use and the frontend team must build, not the imaginary version in the reviewer's head.
