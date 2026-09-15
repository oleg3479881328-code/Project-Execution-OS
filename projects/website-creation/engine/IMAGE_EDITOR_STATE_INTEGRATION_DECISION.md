# Website Creator Engine — Image Editor State Integration Decision

Date: 2026-09-15
Status: ACCEPTED
Scope: shared Website Creator engine image-editor integration with Puck

## Decision

Puck owns canonical editor selection.

For reusable image editing inside the Website Creator engine:

1. identify the edited Puck component by its stable component ID;
2. resolve the current selector with Puck APIs;
3. mutate only that component using the atomic `replace` action;
4. preserve the component ID and `ui.itemSelector`;
5. if the rendered image component remounts, restore only its transient local `active` UI state from Puck's canonical `selectedItem`;
6. do not create a second selection store or parallel page-state model.

Canonical relationship:

`Puck selectedItem/itemSelector → selected component identity → transient image active UI derived/restored from that identity`

## Why

The first generalized image-editor implementation used whole-page `setData` for image-property changes. Puck documents `setData` as expensive and recommends more atomic actions where possible.

The engine was changed to use Puck `replace` for the selected component. That correctly updated the image data and preserved component identity, but the rendered component could still remount. The image frame inherited from the proven Olga interaction owned its visual `active` state locally, so a remount could make the inspector/toolbar appear to disappear even while Puck still considered the component selected.

The correct fix is not to replace Puck selection with custom state. The adapter restores the local active image UI from Puck's canonical selection after remount.

## Implementation Binding

Primary files:

- `src/puck/image-editor/image-editor-plugin.tsx`
- `src/puck/image-editor/PersistentEditableImageFrame.tsx`
- `src/puck/editor-config.client.tsx`
- `tests/editor-loop.spec.ts`

Mutation path:

```text
image control
  → wc-image-layout-change
  → getSelectorForId(blockId)
  → getItemById(blockId)
  → dispatch({ type: 'replace', ... , ui: { itemSelector: selector } })
  → Puck state updates
  → rendered component may remount
  → PersistentEditableImageFrame reads selectedItem
  → local image active UI is restored for the same selected component
```

The plugin may rebroadcast image activation into the same-origin editor canvas after replacement as a compatibility bridge for the inherited event-driven image UI. That bridge is not canonical state.

## Crop Dialog / Shell Boundary

The reusable Crop / move interaction is backed by `react-easy-crop` 6.2.3 rather than a custom crop engine.

The photograph being edited remains rendered inside Puck's canvas iframe. The focused crop dialog is a portal in the editor-shell document.

Therefore:

- crop-dialog CSS must be available in the Payload/editor shell, not only inside the canvas iframe;
- keyboard ownership belongs to the shell modal while it is open;
- the dialog must take focus on open;
- Escape handling must bind to the dialog's actual `ownerDocument.defaultView`, not assume the source iframe window;
- Cancel and Escape close the dialog without committing transient crop state.

Canonical relationship:

`canvas image in Puck iframe → open focused shell modal → transient local crop interaction → Apply only → canonical Puck component data`

The shell modal is an editor integration boundary, not a parallel page-state model.

## Precise Crop Geometry

Precise crop data is persisted as a normalized percentage rectangle rather than editor-only pixel geometry.

The stored semantic fields represent:

- crop X percentage;
- crop Y percentage;
- crop width percentage;
- crop height percentage.

The renderer prefers that precise rectangle when present. Existing `focalX` / `focalY` / `zoom` behavior remains the legacy fallback.

Rules:

- `react-easy-crop` may only commit geometry after the media is loaded;
- every crop value must be finite before persistence;
- invalid / non-finite geometry is rejected at the product boundary rather than serialized;
- Apply commits the normalized rectangle;
- reopen restores that exact rectangle;
- Fit/Whole may hide crop visually without destroying the saved precise rectangle, so returning to Fill can restore it;
- changing the image source or changing shape resets precise crop because the old crop geometry no longer describes the new media/frame contract;
- Reset crop clears precise crop and returns to the legacy/default crop semantics.

Transient cropper state is local UI state until Apply. Canonical persisted crop metadata remains Puck component data.

## Deterministic Seed Media Boundary

The original Car Service Garage seed referenced hard-coded assets on an unrelated demo deployment. Those URLs returned 404 and caused the crop library to have no usable media geometry.

The accepted fix is not another external media host and not a custom crop workaround.

Deterministic seed evidence now uses same-origin engine-owned fixtures under `public/seed-media/`.

Rules:

- CI/local/staging seed fixtures must be self-contained and same-origin;
- deterministic fixtures exist only to make engine behavior reproducible;
- they do not replace real customer photography;
- real owner-selected media continues through Payload Media.

Canonical relationship:

`deterministic engine fixture for seed/QA ≠ mutable customer media; customer media remains Payload-owned.`

## Verified Evidence

Superseded failing run:
- GitHub Actions run `34915425336`;
- first `portrait → square` mutation rendered correctly;
- the next shape operation timed out because the active image inspector/interaction target was no longer usable after the replacement lifecycle.

Selection-continuity green run:
- GitHub Actions run `34916717349`;
- commit `2c9f3e63d037e7ebd4aeeb7d5727de61c4cad9cd`;
- sequential `portrait → square → portrait` edits passed while the same image remained actively editable;
- sequential zoom edits passed;
- Payload media picker opened from the contextual Replace action;
- the rest of the draft/version/publish/restore browser loop also passed.

Crop diagnostic green run:
- GitHub Actions run `34990898658`;
- commit `471f74cd53e9331a3273e8e78a5cd80f66a4f1cf`;
- finite percentage crop Apply passed;
- reopen restored exact crop metadata;
- Escape and explicit Cancel preserved saved crop state.

Canonical clean crop acceptance:
- GitHub Actions run `34994907552`;
- commit `767502a3690e460f38207c9fd8bfa8d2dc3ef290`;
- temporary crop event diagnostics were removed before the run;
- TypeScript, migrations, production seed, production build, Chromium install and browser acceptance all passed;
- browser evidence upload passed;
- this is the canonical acceptance evidence for the current crop slice.

## Rejected Alternatives

### Whole-page `setData` for every image control
Rejected for this integration because it replaces more state than necessary and can destabilize transient editor UI.

### Separate Website Creator image-selection store
Rejected because Puck already owns canonical selected component state. A parallel store would create synchronization and lifecycle failure modes.

### Custom crop engine
Rejected. `react-easy-crop` already provides the required mature drag/zoom/crop interaction model. Website Creator should own only the integration and semantic persistence layer.

### Keeping crop geometry as pixel-only editor state
Rejected because public rendering and reload persistence require portable semantic data independent of the editor viewport dimensions.

### Listening for Escape only in the source canvas iframe
Rejected because the crop dialog is portaled into the shell document. A focused modal must own keyboard input in its actual document/window.

### External demo-host seed images
Rejected because deterministic engine QA must not depend on unrelated deployments or disposable asset URLs.

### Fixing the Playwright test by re-clicking the image after every property change
Rejected as the product behavior. The editor contract requires the selected image to remain actively editable through ordinary sequential control changes.

### Client-specific workaround
Rejected. The behavior belongs to the shared Website Creator editor adapter and must work for every Site Instance that uses the same reusable image component.

## Invariants Going Forward

- component ID must not change during ordinary image-property edits;
- canonical selection stays in Puck UI state;
- image property changes use atomic component mutation where supported;
- transient visual activation may be derived from canonical selection after remount;
- toolbar, inspector and canvas must operate on the same selected image state;
- crop modal focus/keyboard handling follows the modal's actual owner document;
- transient cropper geometry stays local until Apply;
- only finite normalized crop percentages may enter canonical state;
- public rendering consumes persisted semantic image metadata rather than editor-only geometry;
- deterministic seed media is same-origin and engine-owned;
- real mutable site media remains managed by Payload Media;
- any future editor/crop library replacement must preserve this behavioral contract even if the concrete APIs change.

## Next Acceptance Work

Selection continuity and the focused precise crop slice are accepted. The universal image editor is still broader than this slice.

Continue with:
- owner-facing Save Draft / reload persistence for semantic image state;
- draft/public isolation for the same image state;
- owner-facing Publish parity;
- deterministic pointer drag/move gesture coverage in the existing cropper;
- replace/remove persistence;
- alt/caption and applicable alignment/size persistence;
- another applicable reusable image block;
- direct semantic resize only where the component contract permits it.

## Final Rule

Puck selection and component data are the source of truth. Website Creator integrates mature image-editing primitives around that state; it does not compete with them or rebuild them from scratch.
