# Website Creator — latest

Date: 2026-09-13

## Architecture Correction

Owner clarified that Website Creator must be global and must not reference a particular client project as an architectural source or dependency.

## Decision

Website Creator is now client-agnostic and self-contained.

Client-project learning may be promoted only after it is generalized, de-identified and expressed as an independent reusable standard/component/algorithm/test. The originating client project is not part of Website Creator runtime knowledge.

## Changes

- visible project name changed from `Website Creation` to `Website Creator`;
- technical path `projects/website-creation/` retained for routing stability;
- `PROJECT.md` rewritten around global reusable website production;
- `PROJECT_STATE.md` rewritten with the No Client Dependency / Knowledge Promotion rules;
- `ROUTER.md` no longer routes into client projects;
- `SOURCE_REGISTRY.md` replaced with a global capability/standards registry;
- `TOOL_DONOR_REGISTRY.md` rewritten without client-specific architecture dependencies;
- `EDITOR_CREATION_STANDARD.md` converted into a Universal Visual Editor Standard;
- golden editor screenshots remain in Website Creator Drive as anonymous behavioral acceptance references;
- client-specific source notes are being removed from the Website Creator core;
- Drive naming/indexes are being normalized to the same global architecture.

## Core Principle

Website Creator may know **what works**. It should not need to know **which client originally taught us that it works**.

## Knowledge Promotion Flow

`PROJECT-SPECIFIC FINDING → VERIFY → GENERALIZE → DE-IDENTIFY → DEFINE REUSABLE CONTRACT / COMPONENT / TEST → STORE IN WEBSITE CREATOR → USE INDEPENDENTLY`

## Current Universal Editor Contract

The visual editor is now defined globally by behavior/data rather than by a client implementation:

- visual canvas + structure + contextual inspector;
- direct image-selection toolbar;
- visual crop/move/zoom modal;
- non-destructive percentage crop metadata;
- replace/remove/reset/shape/fill/whole/size/alignment/text controls;
- shared state between toolbar and inspector;
- editor/public-render parity;
- persistence and visual acceptance gates.

Compatible technical options include Puck, react-easy-crop and react-moveable, but the behavioral contract is authoritative.

## Next Maintenance Rule

Any future reusable learning must be written into Website Creator in universal form. Do not add a client project link as a shortcut to required production knowledge.