# Website Creation — EDITOR_CREATION_STANDARD.md

## Status

`CURRENT / CANONICAL REUSABLE EDITOR STANDARD`

Created: 2026-09-13

## Why This Standard Exists

A new chat may read old editor notes and still build the wrong editor because descriptive history is not an implementation contract.

For Website Creation, the Olga editor is now treated as a **golden reusable production donor**. When a new project needs a visual/client editor, the executor must inspect the actual current editor source and golden screenshots before designing or coding anything.

Do **not** recreate the editor from memory, from a generic CMS idea, or from a summary alone.

## Golden Source Order

Use sources in this order:

1. Current Olga editor code — executable truth.
2. Golden visual screenshots — visible acceptance reference.
3. Current Olga Image Editor migration/architecture snapshot — rationale and known failure modes.
4. Older task notes only when historical evidence is needed.

### Current executable source

Repository:
https://github.com/oleg3479881328-code/olga-polo-weddings-web

Primary reusable files:

- `app/editor/EditableImageFrame.tsx`
- `app/editor/EditableImageFrame.module.css`
- `app/editor/ImageCropDialog.tsx`
- `app/editor/ImageCropDialog.module.css`
- `app/editor/ImageInspectorPanel.tsx`
- `app/editor/image-crop-model.ts`
- venue/wedding editor consumers and shared `ImageAssetField` / media helpers

### Current architecture snapshot

https://docs.google.com/document/d/1HWHTwXX2KvK-gPUqN3nIrlrh642IeDSWTiVg4vqK9v4/edit

### Golden visual references

Main selected-image editor:
https://drive.google.com/file/d/1Ru4q2lxz299P-C8Spz8v9Ww6j286iMtB/view

Crop / move modal:
https://drive.google.com/file/d/1pfpdTfBZRVW4cSKJxjQHfVxUIuthGdef/view

These are acceptance references, not decorative screenshots.

## Core Product Model

The editor is not “a form next to a page.”

It is a visual page editor with three coordinated control surfaces:

1. **Page/block structure** — Puck controls the page/block model.
2. **Direct manipulation on canvas** — selecting an image exposes an inline floating toolbar and resize handles.
3. **Detailed inspector** — the right-side IMAGE panel exposes the same underlying image state and actions.

The floating toolbar and right inspector must operate on the same state and event handlers. They are two views of one editing model, not parallel implementations.

## Required Editor Shell

The working Olga editor establishes this visual/interaction structure:

- top application bar with page identity and release controls;
- left sidebar for Blocks / Outline;
- central live visual canvas;
- right inspector panel;
- selected content is edited in context on the real visual page;
- image-specific controls appear only when an image is selected;
- crop/move opens as a focused modal overlay rather than forcing precision editing into the narrow inspector.

For a new site, the labels/categories may change, but the interaction model should not be casually replaced.

## Required Selected-Image Behavior

Clicking an editable image must:

- select that image block;
- show a visible selected frame/outline;
- show the floating image toolbar above the selected image;
- show the IMAGE inspector on the right;
- expose side resize handles when block resizing is allowed.

Double-clicking a crop-enabled image may open the crop editor directly.

Only one image should be the active image-editing target at a time.

## Floating Image Toolbar Contract

The current toolbar is the compact direct-manipulation surface.

It includes, in this order/conceptual grouping:

- replace photograph action;
- frame shape selector: `Natural / Landscape / Portrait / Square`;
- `Crop` action;
- display mode selector: `Fill / Whole`;
- block size control when resizing is allowed;
- text/details control for alt text and caption/credit;
- reset crop;
- remove photograph.

The exact styling may evolve, but new editors must not remove the direct on-canvas workflow and force every operation into raw numeric fields.

## Right IMAGE Inspector Contract

The detailed inspector must include the same image model, currently grouped as:

### Image

- current image preview/state;
- Replace file;
- Remove;
- URL/input path support where applicable.

### Frame & crop

- Shape: Natural / Landscape / Portrait / Square;
- clear help/state text;
- `Edit crop / move photo`;
- Display mode:
  - `Fill frame`;
  - `Show whole photo`;
- `Reset crop`.

### Block size & position

When layout resize is permitted:

- width percentage control;
- Left / Center / Right alignment.

### Text

- Alt text;
- Caption / credit.

The inspector is contextual. Hero-specific fields may map to hero storage names, but the editing behavior should remain consistent with normal image blocks.

## Crop / Move Modal Contract

Crop is a visual manipulation task and must remain visual.

The current working implementation uses `react-easy-crop` in a portal/modal isolated from Puck transforms.

Required UX:

- modal/backdrop above the editor;
- fixed crop frame with image moving underneath it;
- visible grid;
- drag photograph to position it;
- mouse/touch interaction, not numeric X/Y entry as the primary UI;
- zoom range from 1× to 3×;
- minus / range slider / current zoom label / plus;
- Reset;
- Cancel;
- Apply crop;
- Escape closes/cancels;
- clicking backdrop may cancel;
- saved crop reopens in its previous position.

Changing Shape from Natural to Landscape/Portrait/Square should automatically enter the crop workflow.

## Shape / Display Semantics

### Natural

- source photograph is shown without forced crop shape;
- crop action is disabled/not applicable.

### Landscape / Portrait / Square

- selected shape defines the crop frame aspect;
- shape change clears incompatible previous crop state;
- default crop workflow enters `Fill` mode.

### Fill frame

- crop metadata is active;
- image fills the chosen frame;
- crop/move editor is available.

### Show whole photo

- display switches to fit/contain behavior;
- whole source image is visible;
- zoom resets to 1;
- exact crop is not used for rendering.

## Data Contract

Image editing is non-destructive.

The source image is not rewritten merely because the user crops, moves or zooms it.

Persist display metadata such as:

- `ratio` / hero equivalent;
- `fitMode`;
- `zoom`;
- `focalX`;
- `focalY`;
- exact crop area percentages:
  - `cropAreaX`;
  - `cropAreaY`;
  - `cropAreaWidth`;
  - `cropAreaHeight`;
- `visualWidth` when block resizing is allowed;
- `visualAlign`;
- `imageAlt`;
- caption/credit.

Crop area is stored in percentages so it is resolution-independent.

The crop center may update focal X/Y for compatibility, but focal coordinates are not the primary user interaction.

## Replace / Reset Semantics

Replacing the underlying image must reset incompatible crop state rather than applying the old crop blindly to a different photograph.

Current reset behavior returns crop state to:

- no exact crop area;
- focal point 50 / 50;
- zoom 1;
- fill mode.

Changing shape also clears incompatible old crop state and recenters/resets zoom.

## Block Resize Contract

Normal editable image blocks may expose visual width resizing.

Current proven implementation uses `react-moveable` with left/right resize handles and keeps aspect ratio.

On resize end:

- rendered width is converted to a bounded percentage of the parent;
- percentage is persisted;
- alignment remains explicit Left / Center / Right.

Do not treat pixel width in the editor as canonical page content.

Hero images may intentionally disable this block-resize behavior while still sharing crop/image controls.

## Proven Technical Architecture

Current Olga implementation uses:

- **Puck** — page/block editor and structured authoring surface;
- **EditableImageFrame** — shared selected-image editing wrapper;
- **ImageInspectorPanel** — right inspector using the same image state;
- **react-easy-crop** — crop/move/zoom inside isolated modal;
- **react-moveable** — visual width handles for supported image blocks;
- event-based patch/selection bridge so editor surfaces stay synchronized;
- shared crop model/helpers for normalized percentages and rendering.

For a new site using the same React/Puck family, this should be **reused/adapted from the actual implementation**, not rebuilt from prose.

If another frontend stack is chosen, preserve the interaction/data contract even if the underlying libraries differ.

## Explicitly Forbidden Failure Modes

Do not repeat these known bad approaches:

- custom pointer-to-Puck coordinate crop math;
- arbitrary coefficients added to “fix” crop drift;
- numeric focalX/focalY controls as the main client-facing crop UX;
- separate unrelated crop implementations for Hero vs regular images;
- separate unrelated logic for Weddings vs Venues when shared behavior applies;
- editor-only geometry hacks that make editor output differ from public rendering;
- modifying page/template/content data to hide an editor-component bug;
- using a stale local draft problem as evidence that the component architecture is wrong;
- replacing the working visual/direct-manipulation pattern with a generic property form because it is easier to code;
- declaring the editor “done” because controls exist without comparing behavior visually against the golden reference.

## Diagnosis Rule Before Fixing Editor Problems

Before changing code, classify the failure:

1. shared editor component/interaction bug;
2. local browser draft/state corruption;
3. content/template mutation;
4. media asset/path problem;
5. release/deploy mismatch.

Fix the correct layer only.

## Reuse Rule For New Website Projects

When a new website requires a visual editor:

1. open this standard;
2. inspect the current Olga editor code;
3. inspect both golden screenshots;
4. identify which existing components can be reused directly;
5. preserve the data/interaction contract;
6. adapt branding/content block schema only where the new project actually differs;
7. run visual acceptance against the golden behavior before inventing new editor UX.

The default is **adapt the proven editor**, not “design another editor inspired by Olga.”

## Minimum Acceptance Test

A new implementation is not accepted until all applicable items pass:

- selecting an image visibly activates it;
- floating toolbar appears and controls the same state as right inspector;
- replace/remove work;
- shape change works and opens crop where required;
- crop modal allows drag + zoom and stores/reopens crop correctly;
- Fill vs Whole behaves correctly;
- reset is deterministic;
- block resize handles persist percentage width where supported;
- alignment persists;
- alt/caption edit correctly;
- Hero and normal image blocks share behavior unless an intentional documented exception exists;
- editor rendering and public rendering agree;
- reload does not silently lose persisted state;
- no local draft corruption is mistaken for canonical content;
- visual result is compared to the golden screenshots, not merely asserted from code.

## Final Rule

For Website Creation, **the working Olga editor is a reusable production component and behavioral standard, not merely historical inspiration**.

When the owner asks for “the editor like we made for Olga,” the executor must reuse this golden implementation contract first and may deviate only for a stated project requirement.