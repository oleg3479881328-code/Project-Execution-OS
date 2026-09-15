# Website Creator Engine — STATUS

Date: 2026-09-15
Status: ACTIVE — shared runtime + precise crop + owner Save/Publish image-state lifecycle FULL GREEN

## Verified Engine Boundary

Current reusable runtime:

`Site Instance → deterministic seed → Payload/Puck page state → shared renderer → authenticated visual editor → draft/publish/version state → public website → Playwright QA`

Implementation binding:

- Next.js / React;
- Payload CMS;
- PostgreSQL;
- Puck through `@delmaredigital/payload-puck`;
- `react-easy-crop` 6.2.3 for focused crop/move/zoom interaction;
- Playwright;
- Docker Compose for local database startup;
- Render staging deployment adapter through root `render.yaml`.

No Puck Cloud, Payload Cloud, Replit, Wix, Framer or other hosted website-builder dependency is required.

## Latest Full CI Verification

Commit: `727f4f00ea241a9d349acc51266ca673ca6ab0f5`
Workflow: Website Creator Engine run `35003482852`
Job: `build-and-runtime-smoke`
Result: PASS / FULL GREEN

Verified in one full run:
- PostgreSQL startup;
- checkout and dependency install;
- TypeScript check;
- committed production migration artifacts;
- migrations applied to an empty PostgreSQL database;
- Car Service Garage production seed;
- production Next.js build;
- Chromium installation;
- production server startup;
- authenticated editor load;
- Hero image selection with contextual toolbar + IMAGE inspector;
- IMAGE inspector integrated through Puck's official `fields` override instead of a fixed editor-shell layer;
- only the actually visible Puck fields host advertises the IMAGE portal target, avoiding hidden responsive/editor panel instances;
- native Puck Save / Publish controls remain unobstructed and normally clickable;
- sequential Shape change `portrait → square → portrait` without losing the active edit target;
- Fit/Whole and Fill semantics operating on the same canonical image state;
- legacy zoom/focal controls and Reset returning the image to legacy/default crop semantics;
- focused Crop / move dialog backed by `react-easy-crop`;
- crop zoom + Reset + Apply producing finite percentage crop geometry;
- applied precise crop persisted in Puck state and rendered as `data-crop="precise"`;
- reopening the crop dialog restoring the exact saved percentage rectangle;
- Escape closing the shell modal without mutating saved crop state;
- explicit Cancel closing the shell modal without mutating saved crop state;
- Reset crop returning from precise crop to legacy/default semantics;
- a fresh precise crop saved through the real owner-facing Puck `Save` action;
- Save request using the integration's draft semantics (`draft: true`);
- saved precise crop surviving a full editor reload with the exact same normalized rectangle;
- draft-only precise crop remaining absent from the public renderer, which continued to expose the previous published legacy crop;
- reopening the editor restoring the draft precise crop;
- publishing through the real owner-facing Puck `Publish` action;
- Publish request using `_status: 'published'`;
- the exact saved precise crop becoming visible on the public renderer only after Publish;
- restoration of the canonical seeded published state so acceptance remains repeatable;
- versions endpoint availability;
- Replace action opening the Payload media picker and exposing Upload New;
- browser/migration evidence upload.

This run is the canonical acceptance evidence for the current owner-facing semantic image-state lifecycle.

Earlier clean crop-only acceptance remains useful for regression comparison:
- commit `767502a3690e460f38207c9fd8bfa8d2dc3ef290`;
- Website Creator Engine run `34994907552`;
- precise crop Apply/reopen/Escape/Cancel/Reset passed before the owner-facing Save/Publish slice was added.

The diagnostic event trace used to locate the original non-finite crop geometry failure was removed before clean acceptance and is not part of the product contract.

## Image Editor State Integration — Accepted Architecture

Selection remains canonical Puck UI state.

Image-property mutations use Puck's atomic `replace` action rather than whole-page `setData`.

The replacement preserves:
- component ID;
- destination zone/index;
- `ui.itemSelector`.

Puck may still remount the rendered component after `replace`. The adapted Olga image frame therefore restores its transient local `active` UI state from Puck's canonical `selectedItem` after remount. This is an adapter concern, not a second selection store.

The bridge may also rebroadcast image activation into the same-origin Puck canvas after replacement, but canonical selection remains Puck-owned.

Architecture rule:

`Puck selectedItem/itemSelector = source of truth → local image active state is derived/restored from it → no parallel selection model.`

Precise crop metadata is canonical component data, not editor-only DOM geometry. The crop dialog keeps transient interaction state locally and commits the normalized percentage rectangle only on Apply.

The IMAGE inspector belongs to Puck's native fields layout. Puck can keep multiple fields containers mounted for different editor/responsive states, so the integration portals only into the currently visible official fields host. It must never float over the editor header or interfere with Save / Publish.

Detailed decision record: `IMAGE_EDITOR_STATE_INTEGRATION_DECISION.md`.

## Deterministic Seed Media Boundary

Car Service Garage seed media no longer depends on the old external demo host, whose hard-coded `/assets/...` URLs returned 404.

Deterministic engine-owned fixtures now live under:

`public/seed-media/`

They are same-origin test/seed fixtures for CI, local development and staging. They are not a replacement for real customer photography.

Real owner-selected photographs continue to use Payload's Media collection and picker.

Architecture rule:

`deterministic seed evidence = same-origin engine fixture; real mutable site media = Payload Media.`

## Older Green Baseline

Commit: `4304a3b2df1906da63f398f9cb2295151c2fe363`
Workflow: Website Creator Engine run `34876621298`
Result: PASS

That baseline remains useful for regression comparison of the pre-image-editor runtime/editor loop.

## Live Render Verification

Blueprint: `Website Creator Engine`

Web service:
- name: `website-creator-engine`;
- service id: `srv-dak6rte1egvs739bc1j0`;
- region: Ohio;
- plan: free;
- primary URL: `https://website-creator-engine.onrender.com`;
- health path: `/health`;
- root dir: `projects/website-creation/engine`;
- runtime: Docker;
- auto-deploy: enabled from `main`.

Database:
- name: `website-creator-postgres`;
- resource id: `dpg-dak33ie1egvs739cfi90-a`;
- PostgreSQL 16;
- region: Ohio;
- associated through Blueprint `fromDatabase.connectionString` rather than copied credentials.

First Blueprint deploy:
- deploy id: `dep-dak6rtm1egvs739bc27g`;
- result: LIVE;
- migrations completed;
- Car Service Garage Site Instance seeded;
- Next.js bound to Render port 10000;
- Render reported `Your service is live`.

Admin bootstrap deploy:
- deploy id: `dep-dak6ulu1egvs739bmsh0`;
- result: LIVE;
- Website Creator admin account created through environment-driven bootstrap;
- no admin password is stored in this repository.

Owner-browser proof on 2026-09-14:
- `/editor` redirected to Payload login before authentication;
- login succeeded;
- canonical Puck route opened at `/admin/puck-editor/pages/1`;
- Car Service Garage homepage rendered in the editor canvas;
- generic Puck Blocks/Outline/History UI visible;
- reusable Hero selected with Website Creator fields visible in the right inspector;
- Save and Publish controls visible;
- published status visible.

## Editor Architecture Proof

The shared component renderer remains server-safe.

Client-only editor capabilities such as Payload/Puck `createMediaField()` are added only in `src/puck/editor-config.ts` / client editor configuration and are not invoked from the server-renderer component module.

This boundary is protected by the same production build + browser acceptance workflow that caught the original server/client regression.

Current reusable section registry:
- Hero;
- Services;
- Process;
- Call to Action;
- Footer.

Current editor proof:
- `/editor` resolves to the canonical Puck editing route;
- authenticated owner can enter the live editor;
- Save and Publish actions are present and unobstructed by the image inspector;
- IMAGE inspector uses Puck's official right-hand `fields` extension point;
- draft and published states are behaviorally distinct;
- version/history API path responds;
- public renderer reflects published edits and not draft-only edits;
- original content can be restored;
- Hero uses the Payload/Puck media picker in the editor;
- selected Hero image stays active through sequential atomic property replacements;
- contextual toolbar and inspector remain available after Shape/zoom edits;
- Fill/Whole and Reset semantics are browser-accepted;
- precise crop Apply/reopen/Escape/Cancel behavior is browser-accepted;
- crop geometry is persisted as normalized finite percentage metadata;
- precise crop survives owner-facing Save Draft and a full editor reload;
- draft precise crop stays isolated from the public renderer;
- owner-facing Publish moves the same precise crop into the public renderer.

## Site Model Evidence

First draft type:
`src/site-model/types.ts`

First Site Instance fixture:
`src/sites/car-service-garage.ts`

State: `0.1-draft`, not frozen.

The current shape is empirically sufficient for the first seed/render/editor/QA cycle. It must survive at least one additional, meaningfully different Site Instance before universal fields are promoted/frozen.

## Current Limitations / Not Yet Verified

The semantic precise-crop + owner Save/Publish lifecycle is accepted, but the universal editor contract is broader.

Still not fully browser-accepted end-to-end:
- pointer drag/move gesture inside the cropper as a separate deterministic acceptance action;
- alignment persistence;
- visual width/direct resize persistence where applicable;
- alt/caption persistence;
- replace/remove persistence and editor/public-render parity;
- version restore through owner-facing editor UI;
- shared image behavior across more than the Hero block;
- visual parity with the final accepted Car Service Garage design direction;
- multi-site isolation under shared live operation;
- second Site Instance reuse;
- durable production media storage (free staging filesystem is not the production target).

## Next Required Slice

Continue the universal image-editor acceptance contract in the shared engine, not client-specific code.

Priority order:
1. Add deterministic pointer drag/move coverage inside the existing `react-easy-crop` dialog without replacing the library, and prove the resulting semantic crop persists through the already accepted Save/reload/Publish lifecycle.
2. Add alt/caption persistence through owner-facing Save/reload/Publish.
3. Add alignment and applicable visual-width persistence.
4. Add replace/remove persistence coverage using the Payload media picker without relying on disposable client-specific assets.
5. Expand the same image behavior to another applicable reusable block before calling the contract universal.
6. Add version restore through owner-facing editor UI.
7. Only then move to direct resize where the component contract actually permits it.
8. Bring Car Service Garage visual output to the accepted reference direction using only shared components and Site Instance data.
9. Validate a second, meaningfully different Site Instance without rebuilding generic infrastructure.
10. Promote only recurring Site Model/component contracts proven by both sites.

## Fresh-Chat Instruction

Before changing engine code:

1. read `../PROJECT.md`;
2. read `../PROJECT_STATE.md`;
3. read `../OWN_SYSTEM_EXECUTION_STANDARD.md`;
4. read this file;
5. read `README.md`;
6. read `../EDITOR_CREATION_STANDARD.md` for image/editor interaction work;
7. read only the narrow implementation files/tests required for the active slice.

Do not create another engine, another client editor or another deployment experiment. Extend this shared engine unless a documented architecture decision replaces a binding.
