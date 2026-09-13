# Website Creator — UNIVERSAL VISUAL EDITOR STANDARD

## Status

`CURRENT / CANONICAL / CLIENT-AGNOSTIC`

Created: 2026-09-13

## Purpose

Define the required behavior, data model and acceptance criteria for a reusable visual website editor.

This standard is self-contained. It does not depend on any client project or client-specific codebase.

Golden visual references stored in Website Creator Drive are behavioral acceptance evidence, not client references:

- Main selected-image editor:
  https://drive.google.com/file/d/1Ru4q2lxz299P-C8Spz8v9Ww6j286iMtB/view
- Crop / move modal:
  https://drive.google.com/file/d/1pfpdTfBZRVW4cSKJxjQHfVxUIuthGdef/view

## Core Product Model

The editor is not merely a form beside a preview.

It is a visual page editor with three coordinated surfaces:

1. **Page/block structure** — page composition and block hierarchy.
2. **Direct manipulation on canvas** — select/edit visible elements in context.
3. **Contextual inspector** — detailed properties/actions for the selected element.

All surfaces operate on the same underlying state. Do not implement parallel unsynchronized editing models.

## Required Editor Shell

A full visual-editor implementation should support the applicable parts of this structure:

- top application bar with page identity and release controls;
- left structure/sidebar for blocks and/or outline;
- central live visual canvas;
- right contextual inspector;
- selected content edited in context on the rendered page;
- element-specific controls appear when that element is selected;
- precision visual operations such as crop/move open in a focused overlay when a narrow inspector is not suitable.

Exact branding/layout may vary; the interaction model is the contract.

## Selected Image Contract

Selecting an editable image should, where applicable:

- make that image the single active image target;
- show a visible selected outline/frame;
- expose a compact floating toolbar near the image;
- expose the contextual IMAGE inspector;
- expose visual resize handles when block resizing is permitted.

Double-click may open crop/move directly for crop-enabled images.

## Floating Image Toolbar Contract

The direct-manipulation toolbar should provide the compact equivalents of:

- replace image;
- shape/frame selector: `Natural / Landscape / Portrait / Square`;
- crop/move action;
- display mode: `Fill / Whole`;
- block size control when resizing is permitted;
- text/details for alt text and caption/credit;
- reset crop;
- remove image.

Do not force common visual operations into raw numeric fields when a direct manipulation control is more natural.

## Right IMAGE Inspector Contract

### Image
- current image state/preview;
- replace/upload;
- remove;
- URL/path input when the implementation supports it.

### Frame & Crop
- Shape: Natural / Landscape / Portrait / Square;
- clear current-state/help text;
- `Edit crop / move photo`;
- `Fill frame`;
- `Show whole photo`;
- `Reset crop`.

### Block Size & Position
When layout resizing is allowed:
- width percentage;
- Left / Center / Right alignment.

### Text
- Alt text;
- Caption / credit.

Hero/feature images may store values under different field names, but visible editing behavior should stay consistent unless an intentional exception is documented.

## Crop / Move Modal Contract

Crop is a visual manipulation task.

Required UX:

- focused modal/backdrop above the editor;
- fixed crop frame with image moving underneath it;
- visible composition grid;
- drag/touch image positioning;
- visual zoom control;
- recommended zoom range around 1×–3× unless project requirements justify another range;
- minus / slider / current zoom label / plus controls;
- Reset;
- Cancel;
- Apply crop;
- Escape cancels/closes;
- backdrop click may cancel;
- reopening restores the saved crop.

Changing Shape from Natural to a forced aspect such as Landscape/Portrait/Square should enter the crop workflow automatically when practical.

## Shape / Display Semantics

### Natural
- preserve source aspect;
- no forced crop frame;
- crop action may be disabled/not applicable.

### Landscape / Portrait / Square
- selected shape defines crop-frame aspect;
- changing shape clears incompatible exact crop state;
- default to fill behavior and open crop/move when appropriate.

### Fill Frame
- image fills the selected frame;
- exact crop metadata may be active;
- crop/move is available.

### Show Whole Photo
- fit/contain semantics;
- entire source image visible;
- zoom normally resets to 1;
- exact crop should not determine rendering while in whole-photo mode.

## Data Contract

Image manipulation is non-destructive by default.

Do not rewrite the original image merely because the user crops/moves/zooms it.

Persist semantic display metadata such as:

- `ratio`;
- `fitMode`;
- `zoom`;
- `focalX`;
- `focalY`;
- exact crop percentages:
  - `cropAreaX`;
  - `cropAreaY`;
  - `cropAreaWidth`;
  - `cropAreaHeight`;
- `visualWidth` where resizable;
- `visualAlign`;
- `imageAlt`;
- caption/credit.

Store exact crop area in percentages so it is resolution-independent.

Focal coordinates may be derived from crop center for compatibility, but numeric focal X/Y is not the primary client-facing crop UX.

## Replace / Reset Semantics

Replacing the source image must clear incompatible crop state.

Recommended reset state:

- no exact crop;
- focal 50 / 50;
- zoom 1;
- fill mode for forced-aspect shapes.

Changing shape should also clear incompatible crop metadata and recenter/reset zoom.

## Visual Block Resize Contract

Resizable image blocks may expose direct left/right handles with aspect ratio preserved.

At resize completion:

- convert rendered size to a bounded percentage/semantic layout value;
- persist that semantic value;
- keep alignment explicit.

Editor pixel width must not become canonical page content.

Some feature/hero blocks may intentionally disallow free width resizing while still sharing crop/image behavior.

## Recommended Implementation Options

The contract is stack-independent. In compatible React projects, proven implementation options include:

- **Puck** for structured page/block authoring;
- **react-easy-crop** for isolated visual crop/move/zoom;
- **react-moveable** for direct resize handles;
- portal/overlay isolation for crop UI;
- shared state/event bridge so toolbar and inspector stay synchronized;
- shared crop model/helpers for normalization and rendering.

These libraries are options, not the standard itself. A different stack is acceptable if it satisfies the same behavior/data/acceptance contract.

## Explicitly Forbidden Failure Modes

Do not use:

- custom pointer-to-transformed-editor coordinate crop math when a proven crop library solves it;
- arbitrary coefficients added to compensate for crop drift;
- raw focalX/focalY numeric fields as the primary crop UX;
- separate unrelated crop implementations for feature vs normal images without a real requirement;
- duplicated editor logic across page types when behavior is shared;
- editor-only geometry hacks that render differently on the public site;
- page/content mutation to disguise an editor-component bug;
- stale local draft/state corruption as justification for rewriting canonical content;
- a generic property form as a replacement for required direct-manipulation behavior simply because it is easier to implement;
- declaring the editor complete because controls exist without visual/behavioral acceptance.

## Diagnosis Rule Before Fixing

Classify the failure first:

1. shared editor component/interaction bug;
2. local browser draft/state corruption;
3. real content/template mutation;
4. media asset/path issue;
5. persistence/API issue;
6. release/deploy mismatch.

Fix the correct layer only.

## Minimum Acceptance Test

A visual-editor implementation is not accepted until applicable items pass:

- selecting an image visibly activates it;
- floating toolbar and right inspector edit the same state;
- replace/remove work;
- shape changes behave correctly;
- crop modal supports drag + zoom;
- crop persists and reopens correctly;
- Fill vs Whole behaves correctly;
- reset is deterministic;
- visual resize persists semantic width where supported;
- alignment persists;
- alt/caption persist;
- shared image behavior is consistent across applicable block types;
- editor and public rendering agree;
- reload does not lose saved state;
- client/local draft corruption does not silently become canonical content;
- result is visually compared with the Website Creator golden references when reproducing this editor pattern.

## Final Rule

Website Creator owns this editor behavior as a universal reusable capability.

Implementations may change technology or styling, but they must not silently replace the direct-manipulation interaction/data contract with a weaker generic editor.