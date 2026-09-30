# Showit Compiler — Proven Bricks Integrated Acceptance

Status: `PROVEN LIVE / OWNER VISUAL QA PASS`
Date: 2026-09-30

## Scope

This proof covers the integrated Showit compiler path assembled exclusively from already LIVE-PROVEN Showit bricks.

It does **not** promote an untested transport layer or claim that every wrapper API surface has separately passed owner-run acceptance.

## Owner-run chain

```text
fresh local image from computer
→ POST /useruploads
→ presigned S3 PUT
→ /useruploads/<upload_id>/complete
→ new Showit asset
→ create two brand-new Canvas blocks in page JSON
→ create text elements
→ bind uploaded asset through graphic.content
→ insert both Canvas blocks in memory
→ exactly one authenticated gzip page save
→ durable S3/page readback
→ reload Showit editor
→ open new image Canvas
→ owner visual QA
```

## Acceptance output

Owner-run console output showed:

```text
status: SHOWIT_PAGE_COMPILER_INTEGRATED_ACCEPTANCE_PASS
pageSaveCount: 1
durableReadback: PASS
readbackAttempt: 1
ui.heroCount: 1
ui.imageCount: 1
finalStatus: PROVEN BRICKS COMPOSED — READY FOR VISUAL QA
```

The output also returned a newly created Showit asset key and distinct generated Canvas names for the acceptance HERO and IMAGE blocks.

## Visual QA

Owner screenshot after editor reload showed:

- new `COMPILER ACCEPT — HERO — ...` Canvas present in the page list;
- new `COMPILER ACCEPT — IMAGE — ...` Canvas present in the page list;
- IMAGE Canvas selected;
- expected text `LOCAL FILE → SHOWIT ASSET → CANVAS` rendered;
- the newly selected local wedding image visibly rendered in the new Canvas;
- neighboring existing Showit Canvas content remained present;
- console reported one page save and durable readback PASS.

Visual QA result: `PASS`.

## Proven conclusion

The following integrated path is now live-proven:

```text
LOCAL FILE
→ DIRECT SHOWIT MEDIA UPLOAD
→ SHOWIT ASSET
→ GRAPHIC.CONTENT BINDING
→ MULTI-CANVAS JSON COMPILATION
→ ONE PAGE SAVE
→ DURABLE READBACK
→ EDITOR RELOAD
→ VISUAL RENDER
```

This proves that a page can be compiled in memory with text and uploaded imagery and written to Showit as one page save instead of saving after every element.

## Architecture consequence

The production direction is now supported by live owner evidence:

```text
Universal Recipe / Site Model
→ Showit compiler mapping
→ upload required local assets
→ assemble Canvas + elements in memory
→ ONE SAVE PER PAGE
→ readback + visual QA
```

## Important boundary

Do not conflate this proof with separate acceptance of the `showit-page-compiler-v1.js` wrapper API.

Current status:

```text
Showit primitive operations                 PROVEN LIVE
Integrated direct-bricks compiler path      PROVEN LIVE
showit-page-compiler-v1.js wrapper API      CANDIDATE until separately owner-run
```

## Process lesson

The successful acceptance used only existing proven bricks.

Experimental GitHub-fetch/eval acceptance loader attempts are not canonical and must not replace the direct proven-bricks path.

Canonical rule:

`CURRENT CANONICAL STANDARD → EXISTING LIVE-PROVEN BRICKS → EXECUTION → PERSISTED READBACK → OWNER VISUAL QA`
