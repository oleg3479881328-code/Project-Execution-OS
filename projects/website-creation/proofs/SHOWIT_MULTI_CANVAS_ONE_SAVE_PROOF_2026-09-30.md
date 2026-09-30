# Showit Multi-Canvas One-Save Proof — 2026-09-30

Status: `PROVEN LIVE`

## Purpose

Prove that multiple brand-new Showit Canvas sections can be compiled in memory and committed to the current page with exactly one authenticated whole-page save, while preserving all pre-existing page blocks.

## Live proof result

Execution environment: real authenticated Showit Chrome session through Dramaturg JS mode.

Result marker:

`SHOWIT MULTI-CANVAS ONE-SAVE — PROOF COMPLETED`

Top-level status:

`MULTI_CANVAS_ONE_SAVE_READBACK_VERIFIED`

Mode:

`4 BRAND-NEW CANVAS / ONE WHOLE-PAGE POST`

## Created Canvas sections

1. `API PAGE — HERO`
   - ID: `z2QpLNLUl`
   - slug: `api-page-hero`
   - 3 text elements

2. `API PAGE — SERVICES`
   - ID: `garlTKSI-`
   - slug: `api-page-services`
   - 3 text elements

3. `API PAGE — PROCESS`
   - ID: `XvFV4L9J3`
   - slug: `api-page-process`
   - 2 text elements

4. `API PAGE — CTA`
   - ID: `6h3HXmMWA`
   - slug: `api-page-cta`
   - 3 text elements

Total newly compiled elements: `11`.

## Save evidence

- design key: `ljhcybjw0lbnr_qqyok5ma`
- page ID: `JmaXuE-zc`
- inserted after: `API TEST — CREATED FROM SCRATCH`
- old ETag: `53bd3433ec7f6e7f37edda9530a8e0bd`
- new ETag: `0a7adf22622a980a70660c21467fde87`
- API write count: `1`
- raw JSON bytes: `25,865`
- gzip bytes: `3,127`
- durable readback attempt: `1`
- old blocks verified unchanged: `12`
- new blocks verified: `4`
- new elements verified: `11`
- total blocks after write: `16`
- auth path: `Bearer authToken` read only from the authenticated Showit session at runtime

## UI acceptance

After editor reload, each created Canvas name was found exactly once in the Showit UI:

- `API PAGE — HERO`: 1
- `API PAGE — SERVICES`: 1
- `API PAGE — PROCESS`: 1
- `API PAGE — CTA`: 1

Visual inspection confirmed Showit rendered the generated sections and text content.

## Accepted architecture consequence

This proves that Showit does not need to be automated element-by-element for this class of operation.

Accepted path:

```text
authenticated Showit tab
→ LOAD current page JSON + ETag
→ compile multiple Canvas sections and elements in memory
→ ONE authenticated gzip POST of the whole page model
→ receive new ETag
→ durable S3 readback
→ reload editor
→ visual QA
```

The page mutation is a whole-document save model.

This proof is stronger than the earlier single-Canvas from-scratch proof because it verifies multiple newly generated Canvas sections and multiple elements in one server write while proving all pre-existing blocks remain unchanged.

## What this proves

- multiple Canvas sections can be generated from scratch;
- multiple text elements can be generated from normalized specifications;
- desktop/mobile geometry, colors, type size, line height, letter spacing and section dimensions can be compiled into Showit JSON;
- the complete mutation can be committed with one POST;
- pre-existing blocks can be preserved exactly;
- durable readback and UI reload verification can close the acceptance loop.

## What this does not yet prove

Do not overstate this result.

Still unproven:

- replacing every existing Canvas on a page from a Recipe in one operation;
- creating a brand-new Showit page through API rather than editing an existing page file;
- media/image upload into Showit's media system;
- compiling image elements from local assets or fingerprint ZIPs;
- galleries, forms, menus, WordPress/blog-specific Canvas data, video, advanced interactions, site-wide styles and publish flow through this API path;
- arbitrary Universal Page Recipe → Showit parity on a real donor page.

## Current architectural status

`Universal Recipe → Showit JSON compiler → multi-Canvas one-save page mutation` is now `PROVEN LIVE` for text-only normal Canvas sections on an existing page.

The highest-value next missing capability is media/image handling. Without it, the compiler is useful for structural and typography reconstruction but not yet sufficient for realistic production page reconstruction.

## Security rule

Never persist the real `authToken` value in repositories, logs, fixtures, screenshots or generated artifacts. Read it only at execution time inside the authenticated Showit browser session and send it only to Showit's own API.
