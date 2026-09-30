# Showit From-Scratch Canvas API Proof — 2026-09-30

Status: `PROVEN LIVE / ACCEPTED EVIDENCE`

## Purpose

Prove that a normal Showit page Canvas can be created as a brand-new JSON object, without cloning an existing Canvas and without using Showit UI creation controls, then committed through the already proven whole-page save path.

## Live proof result

The owner ran the proof inside the real authenticated Showit Chrome session through Dramaturg JS mode.

Operation:

```text
current authenticated Showit page
→ discover current design/page resource
→ GET current page JSON + current ETag
→ read localStorage.authToken inside the session
→ construct a new Canvas object from scratch in memory
→ add 3 text elements from scratch
→ insert the new block into blocks[] / blockData
→ gzip the whole-page payload
→ POST api.showit.com/designs/<design-key> with Authorization: Bearer <authToken>
→ receive saved:true + new ETag
→ GET page JSON again from S3
→ durable readback
→ verify all pre-existing blocks are unchanged
→ reload editor
→ visually confirm the new Canvas renders in Showit
```

## Accepted evidence

- created Canvas name: `API TEST — CREATED FROM SCRATCH`;
- generated new block ID: `An1jSSOtI`;
- inserted after: `IRONLINE — PROCESS-1`;
- design key: `ljhcybjw0lbnr_qqyok5ma`;
- page ID: `JmaXuE-zc`;
- old ETag: `59d65ae6c1ef5d366a45bd9f71d49860`;
- new ETag: `53bd3433ec7f6e7f37edda9530a8e0bd`;
- durable readback passed on attempt 1;
- stored index: 8;
- total blocks after write: 12;
- created element count: 3;
- all 11 unrelated pre-existing blocks verified unchanged;
- authentication path: runtime `Bearer authToken` from the already-authenticated Showit session;
- creation mode: `BRAND NEW JSON OBJECT — NO SOURCE CANVAS CLONED`;
- editor reload succeeded;
- Canvas name UI readback count: 1;
- final marker: `SHOWIT FROM-SCRATCH CANVAS — PROOF COMPLETED`.

## Visual evidence

After reload, Showit visibly rendered the three created text elements inside the new Canvas:

- `THIS CANVAS WAS CREATED BY API`
- `NO SHOWIT UI WAS USED`
- `TEST COMPLETE`

The auxiliary Playwright exact-text counters for those inner rendered texts returned `0`, even though the editor visibly rendered them. Therefore those locator counts are not a valid acceptance gate for inner Showit canvas text. For this class of proof, acceptance must rely on:

1. durable JSON readback of the exact element data;
2. editor reload;
3. visual/render QA (screenshot and/or a Showit-aware render check).

## Architecture consequence

The Showit adapter is now proven to support programmatic structure generation, not only mutation/duplication of existing structure.

Accepted direction:

```text
Universal Recipe / page model
→ Showit JSON compiler
→ construct many Canvas/elements in memory
→ ONE whole-page authenticated save
→ durable readback
→ editor reload
→ visual QA
```

This means a future page compiler does not need to create and save each element individually. Multiple Canvas and elements may be assembled locally and committed in one page save, subject to preserving Showit data-model invariants.

## Remaining unproven areas before full production promotion

- media/image upload and Showit asset references;
- broader element kinds beyond the currently proven text structure;
- full-page generation from a Universal Page Recipe in one save;
- robust visual QA for rendered inner element content;
- publish path if production publish is required after page-file save.

## Next proof

Build a bounded whole-page compiler proof using multiple newly generated Canvas and multiple text elements in one save. Keep media out of that proof. Verify exact page-model readback, block order, unchanged unrelated metadata, editor reload, and visual rendering.

Security rule: never persist the real `authToken` value in notes, fixtures, logs, or source files.