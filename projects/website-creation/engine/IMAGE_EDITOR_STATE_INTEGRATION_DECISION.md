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

## Verified Evidence

Superseded failing run:
- GitHub Actions run `34915425336`;
- first `portrait → square` mutation rendered correctly;
- the next shape operation timed out because the active image inspector/interaction target was no longer usable after the replacement lifecycle.

Accepted green run:
- GitHub Actions run `34916717349`;
- commit `2c9f3e63d037e7ebd4aeeb7d5727de61c4cad9cd`;
- job `build-and-runtime-smoke` passed completely;
- sequential `portrait → square → portrait` edits passed while the same image remained actively editable;
- sequential zoom edits passed;
- Payload media picker opened from the contextual Replace action;
- the rest of the draft/version/publish/restore browser loop also passed.

## Rejected Alternatives

### Whole-page `setData` for every image control
Rejected for this integration because it replaces more state than necessary and can destabilize transient editor UI.

### Separate Website Creator image-selection store
Rejected because Puck already owns canonical selected component state. A parallel store would create synchronization and lifecycle failure modes.

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
- public rendering must consume the persisted semantic image metadata rather than editor-only geometry;
- any future editor library replacement must preserve this behavioral contract even if the concrete APIs change.

## Next Acceptance Work

This decision solves selection continuity only. It does not by itself prove the full universal image editor.

Continue with:
- Fill / Whole semantics;
- Reset behavior;
- crop/move drag + zoom + Apply + reopen persistence;
- Save Draft + reload persistence;
- draft/public isolation;
- Publish parity;
- replace/remove persistence;
- another applicable reusable image block;
- direct semantic resize only where the component contract permits it.

## Final Rule

Puck selection is the source of truth. Website Creator adapts the image component to that state; it does not compete with it.
