# Website Creator Engine — Image Editor State Integration Decision

Date: 2026-09-15
Status: ACCEPTED
Scope: shared Website Creator engine image-editor integration with Puck

## Decision

Puck owns canonical editor selection, Puck owns the native fields layout, and the existing Payload/Puck draft/publish lifecycle owns persistence.

For reusable image editing:

1. identify the edited component by stable Puck component ID;
2. resolve its selector through Puck APIs;
3. mutate only that component with atomic `replace`;
4. preserve component ID and `ui.itemSelector`;
5. derive/restore transient local image activation from Puck `selectedItem` after remount;
6. keep crop interaction transient until Apply;
7. persist only finite normalized percentage crop geometry;
8. render IMAGE controls inside Puck's official `Plugin.overrides.fields` layout;
9. use the existing owner-facing Save and Publish controls for crop, alt, caption and other semantic image properties;
10. do not create a parallel selection store, image store, crop engine, metadata store or client-specific editor.

Canonical relationship:

`Puck selection → selected image component → transient image UI → semantic component data → Save Draft → reload → Publish → public renderer`

## Atomic State Integration

Primary files:

- `src/puck/image-editor/image-editor-plugin.tsx`
- `src/puck/image-editor/PersistentEditableImageFrame.tsx`
- `src/puck/image-editor/EditableImageFrame.tsx`
- `src/puck/editor-config.client.tsx`
- `tests/editor-loop.spec.ts`

Mutation path:

```text
image control
  → wc-image-layout-change
  → getSelectorForId(blockId)
  → getItemById(blockId)
  → dispatch({ type: 'replace', ..., ui: { itemSelector: selector } })
  → Puck state update
```

Puck may remount the rendered component after `replace`. Local `active` UI may be restored from canonical Puck selection, but that local state is never a second source of truth.

## Native IMAGE Inspector Boundary

The IMAGE inspector belongs inside Puck's native right-hand fields layout.

Accepted extension point:

`Plugin.overrides.fields`

Rejected approach:

`document.body + fixed top/right coordinates`

Reason: a fixed shell inspector can physically overlap native owner controls such as Save / Publish. Native layout integration preserves editor ownership and removes positional coupling.

Puck may keep multiple fields containers mounted for responsive/editor states. Only the actually visible official fields host may advertise the IMAGE inspector target.

Canonical relationship:

`Puck fields override → visible native fields host → IMAGE inspector`

## Crop Dialog / Shell Boundary

Crop / move uses `react-easy-crop` 6.2.3. The photograph stays in Puck's canvas iframe; the focused crop dialog lives in the editor-shell document.

Rules:

- crop modal CSS must be loaded in the shell;
- the modal takes focus on open;
- Escape handling binds to the modal's real `ownerDocument.defaultView`;
- Cancel and Escape do not commit transient crop state;
- Apply is the only path from transient crop interaction to canonical Puck data.

## Precise Crop Geometry

Precise crop metadata is stored as normalized percentage rectangle fields: X, Y, width, height.

Rules:

- media must be loaded before geometry can be committed;
- every persisted crop value must be finite;
- invalid/non-finite geometry is rejected;
- reopen restores the exact saved rectangle;
- legacy `focalX` / `focalY` / `zoom` remains fallback behavior;
- Fit/Whole may hide a precise crop without destroying it;
- image replacement or shape change resets precise crop;
- Reset crop clears precise crop and returns to legacy/default semantics.

A real pointer drag is now part of acceptance. The test drags inside the actual `react-easy-crop` stage with Playwright mouse events, then proves the persisted crop rectangle center moved away from the default 50/50 center. Direct test mutation of crop state is not accepted as drag evidence.

## Alt / Caption Metadata

Alt text and caption/credit are ordinary semantic properties of the same Puck component data.

For Hero:

`IMAGE Alt text → imageAlt`

`IMAGE Caption / credit → caption adapter → imageCredit`

The public renderer consumes those same persisted properties. There is no separate image-metadata database or save path.

Accepted lifecycle:

```text
IMAGE inspector edit
  → atomic component replacement
  → editor canvas reflects metadata
  → Save Draft
  → full reload restores metadata
  → public renderer keeps previous published metadata
  → Publish
  → public renderer receives the exact saved metadata
```

## Owner Save / Publish Lifecycle

Website Creator does not add an image-specific persistence system.

Accepted lifecycle:

```text
semantic image edit
  → canonical Puck component data
  → owner Save
  → draft PATCH
  → full editor reload restores exact image state
  → public renderer remains on previous published image state
  → owner Publish
  → published PATCH
  → public renderer receives the same image state
```

Bindings:

- Save uses draft semantics and must not publish image changes;
- reload must restore the same saved semantic image state;
- public rendering ignores draft-only image changes;
- Publish promotes the already-saved semantic image state rather than recomputing it;
- acceptance restores seeded published state afterward so tests remain repeatable.

## Deterministic Seed Media Boundary

CI/local/staging seed images are same-origin engine-owned fixtures under `public/seed-media/`.

They exist for deterministic evidence only. Real mutable customer media continues through Payload Media.

## Canonical Evidence

Clean precise-crop baseline:
- run `34994907552`;
- commit `767502a3690e460f38207c9fd8bfa8d2dc3ef290`;
- Apply/reopen/Escape/Cancel/Reset all passed without diagnostic trace code.

Native fields + owner persistence acceptance:
- run `35003482852`;
- commit `727f4f00ea241a9d349acc51266ca673ca6ab0f5`;
- native IMAGE panel, unobstructed Save/Publish, draft reload, public isolation and Publish parity passed.

Real pointer drag acceptance:
- run `35004130921`;
- commit `3ee78386aedaa77169b33587509b685921a1a364`;
- real pointer drag changed normalized crop position;
- the moved crop survived Save Draft, reload, public isolation and Publish.

Alt/caption acceptance:
- run `35004973259`;
- commit `01d6d6950c3a58d5f47a5a4db562118f301d09cb`;
- Hero alt and caption/credit were edited through the real IMAGE inspector;
- both survived owner Save Draft and full editor reload;
- neither leaked to the public renderer while draft-only;
- both appeared exactly after owner Publish;
- moved precise crop continued to pass in the same lifecycle;
- seeded published state was restored;
- TypeScript, migrations, production seed, build, Chromium, browser acceptance and evidence upload all passed.

Run `35004973259` is the canonical evidence for the current owner-facing Hero semantic image lifecycle.

## Rejected Alternatives

- whole-page `setData` for ordinary image-property edits;
- separate Website Creator image-selection store;
- fixed IMAGE inspector over the editor shell;
- magic top/right offsets to avoid header controls;
- portalling into the first fields node found in the DOM;
- custom crop engine;
- pixel-only crop persistence;
- direct test mutation as proof of pointer drag;
- Escape handling only in the source iframe;
- image-specific Save/Publish store;
- separate alt/caption metadata store;
- external demo-host seed media;
- test-only re-clicks after every image property mutation;
- client-specific editor workaround.

## Invariants Going Forward

- canonical selection stays in Puck UI state;
- ordinary image changes use atomic component mutation;
- local activation is derived from canonical selection;
- toolbar, inspector and canvas operate on the same selected image state;
- IMAGE inspector lives in Puck's official fields layout;
- only the visible Puck fields host receives the IMAGE portal;
- Save / Publish remain unobstructed and normally clickable;
- crop modal keyboard ownership follows its actual shell document;
- transient crop geometry remains local until Apply;
- only finite normalized crop percentages enter canonical data;
- actual pointer interaction is required when claiming drag acceptance;
- alt/caption are canonical component properties, not a side store;
- Save Draft persists semantic image state without publishing it;
- reload restores saved draft image state exactly;
- public rendering ignores draft-only image state;
- Publish promotes the same semantic image state into public rendering;
- deterministic seed media is engine-owned and same-origin;
- real mutable media remains Payload Media owned.

## Next Acceptance Work

Continue with:

- alignment + visual-width persistence on reusable `ImageSection`;
- use that same work to prove shared image behavior beyond Hero;
- replace/remove persistence through Payload Media;
- owner-facing version restore;
- direct semantic resize where the reusable component contract permits it.

## Final Rule

Puck selection, Puck fields layout, and the Payload/Puck page lifecycle are the source of truth. Website Creator integrates mature image-editing primitives around those contracts; it does not rebuild or compete with them.
