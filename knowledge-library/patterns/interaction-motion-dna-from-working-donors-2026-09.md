# Interaction / Motion DNA From Working Donors

- Type: pattern
- Lifecycle status: candidate
- Captured: 2026-09-06
- Review status: preserved and source-checked; not yet an active mandatory design rule

## Source / Evidence

Primary project capture:
- SOFT Framer note: https://docs.google.com/document/d/19iKp-YMkOq6Ac3nYmmhvCuLqD3o5_9HLbdBEkiUoy-M/edit
- Durable source screenshot: https://drive.google.com/file/d/1qxVmVKotwD2yJRdJeusp7DAbwRxFbOpk/view

Example working donors captured from Marina ui ux design / Framer:
- Parallax remix: https://framer.link/05gE4Zj
- Chimes remix: https://framer.link/CfiBxSz

Official Framer evidence that remix links copy a working project into another workspace:
- https://www.framer.com/help/articles/how-to-create-a-remix-link/

Related existing PEOS design artifact:
- `blocks/design/DESIGN_PICKER.md`

## Problem / Context

A static screenshot can capture visual style but often loses the behavior that makes an interface feel premium: timing, physics, cursor response, parallax depth, transitions, sequencing, state changes and mobile fallbacks.

When a working donor is available, especially a remixable project or inspectable component, it can be more valuable than a screenshot because the interaction can be observed and decomposed rather than guessed.

## Candidate Reusable Pattern

Extend visual donor analysis with an optional `Interaction DNA` / `Motion DNA` layer when motion materially contributes to the reference.

Candidate flow:

`REFERENCE -> WORKING DONOR / REMIX -> INSPECT -> EXTRACT MOTION DNA -> ADAPT -> TEST -> PROMOTE IF PROVEN`

Useful fields when relevant:

- trigger: hover / scroll / cursor / drag / click / viewport / time;
- physics / response model;
- cursor dependency;
- scroll dependency;
- easing / spring behavior;
- depth / parallax model;
- layer relationships;
- timing and sequencing;
- state transitions;
- responsive and mobile fallback behavior;
- performance cost;
- accessibility implications;
- implementation type: native builder behavior / code component / React / external library;
- reusable component or pattern name;
- adaptation constraints;
- license / source trail;
- do / don't notes.

## Applies To

- website and landing-page design;
- Design Picker donor analysis;
- Automatic Website Factory donor extraction;
- premium portfolio / creative site work;
- reusable interaction-component libraries;
- visual-reference-to-implementation workflows.

## Triggers

Load this candidate when:

- the owner selects a donor mainly because of its motion or feel;
- a remixable / inspectable working interaction exists;
- the task involves parallax, cursor response, scroll motion, physics, layered movement or other nontrivial interaction;
- a future agent would otherwise have to reconstruct the interaction from a screenshot or memory.

## Do Not Load When

- the task is purely static visual styling;
- motion is incidental and does not affect the design decision;
- the donor cannot be legally or practically inspected and only a visual reference is needed.

## Adaptation Notes

Do not clone the donor wholesale. Extract the behavior and constraints, then normalize it to the target project's visual system, accessibility requirements, responsive behavior, performance budget and implementation stack.

Prefer a proven working donor over rebuilding an effect from first principles when the donor fits the requirement and source/license constraints allow adaptation.

## Risks / Validation Still Required

- A working remix or component is not automatically licensed for unrestricted commercial copying.
- Builder-specific implementation details may not transfer cleanly to a custom-code stack.
- Motion can harm performance, accessibility or mobile usability if copied without adaptation.
- Before promotion to an active design rule, validate this schema on several real donor-to-build cases and decide whether it belongs directly in `blocks/design/DESIGN_PICKER.md` or remains a reusable optional pattern.
