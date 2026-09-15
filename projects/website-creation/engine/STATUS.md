# Website Creator Engine — STATUS

Date: 2026-09-15
Status: ACTIVE — shared runtime + owner-facing image semantic lifecycle FULL GREEN through crop drag + alt/caption

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

Commit: `01d6d6950c3a58d5f47a5a4db562118f301d09cb`
Workflow: Website Creator Engine run `35004973259`
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
- IMAGE inspector integrated through Puck's official `fields` override;
- only the actually visible Puck fields host advertises the IMAGE portal target;
- native Puck Save / Publish controls remain unobstructed and normally clickable;
- sequential Shape change without losing the selected image;
- Fit/Whole, Fill, legacy focal/zoom and Reset semantics;
- focused Crop / move dialog backed by `react-easy-crop`;
- finite normalized percentage crop geometry;
- Apply/reopen/Escape/Cancel/Reset behavior;
- a real pointer drag inside the crop stage, with the persisted percentage crop center proven to move away from the default 50/50 center;
- the moved precise crop saved through the real owner-facing Puck `Save` action;
- Save request using draft semantics (`draft: true`);
- moved precise crop surviving a full editor reload with the exact same normalized rectangle;
- draft-only crop remaining absent from the public renderer;
- Hero image alt text edited through the IMAGE panel and surviving Save/reload;
- Hero caption/credit edited through the IMAGE panel and surviving Save/reload;
- draft-only alt/caption remaining absent from the public renderer;
- publishing through the real owner-facing Puck `Publish` action;
- Publish request using `_status: 'published'`;
- the exact moved crop becoming public only after Publish;
- the exact alt text becoming public only after Publish;
- the exact caption/credit becoming public only after Publish;
- restoration of the canonical seeded published state so acceptance remains repeatable;
- versions endpoint availability;
- Replace action opening the Payload media picker and exposing Upload New;
- browser/migration evidence upload.

This run is the canonical acceptance evidence for the current owner-facing Hero image semantic lifecycle.

Supporting accepted runs:
- `34994907552` / `767502a3690e460f38207c9fd8bfa8d2dc3ef290`: clean precise-crop Apply/reopen/Escape/Cancel/Reset baseline after temporary diagnostics were removed;
- `35003482852` / `727f4f00ea241a9d349acc51266ca673ca6ab0f5`: native Puck fields panel + Save Draft → reload → public isolation → Publish lifecycle;
- `35004130921` / `3ee78386aedaa77169b33587509b685921a1a364`: real pointer drag changes semantic crop and survives Save/reload/Publish.

## Image Editor State Integration — Accepted Architecture

Selection remains canonical Puck UI state.

Image-property mutations use Puck's atomic `replace` action rather than whole-page `setData`.

The replacement preserves:
- component ID;
- destination zone/index;
- `ui.itemSelector`.

Puck may still remount the rendered component after `replace`. The adapted image frame restores only its transient local `active` UI state from Puck's canonical `selectedItem`. This is an adapter concern, not a second selection store.

Architecture rule:

`Puck selectedItem/itemSelector = source of truth → local image active state is derived/restored from it → no parallel selection model.`

Precise crop metadata is canonical component data, not editor-only DOM geometry. The crop dialog keeps transient interaction state locally and commits normalized finite percentage geometry only on Apply.

Alt text and caption/credit are ordinary component properties in the same Puck/Payload page lifecycle. They do not use a separate media-metadata store.

The IMAGE inspector belongs to Puck's native fields layout. Puck can keep multiple fields containers mounted, so the integration portals only into the currently visible official fields host. It must never float over the editor header or interfere with Save / Publish.

Detailed decision record: `IMAGE_EDITOR_STATE_INTEGRATION_DECISION.md`.

## Deterministic Seed Media Boundary

Car Service Garage seed media no longer depends on the old external demo host, whose hard-coded `/assets/...` URLs returned 404.

Deterministic engine-owned fixtures live under:

`public/seed-media/`

They are same-origin fixtures for CI, local development and staging. They are not a replacement for real customer photography.

Real owner-selected photographs continue to use Payload's Media collection and picker.

Architecture rule:

`deterministic seed evidence = same-origin engine fixture; real mutable site media = Payload Media.`

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

Client-only editor capabilities such as Payload/Puck `createMediaField()` are added only in the client editor configuration and are not invoked from the server-renderer component module.

Current reusable section registry includes:
- Hero;
- Services;
- Process;
- Call to Action;
- Footer;
- reusable ImageSection in the shared component library/editor configuration.

Current accepted image proof for Hero:
- authenticated editor selection;
- contextual toolbar and IMAGE inspector;
- sequential atomic mutations without losing selection;
- Shape, Fill/Whole, legacy focal/zoom and Reset;
- precise crop Apply/reopen/Escape/Cancel;
- real pointer drag in `react-easy-crop`;
- finite percentage crop persistence;
- owner Save Draft and full reload;
- draft/public isolation;
- owner Publish and public parity;
- alt text Save/reload/Publish persistence;
- caption/credit Save/reload/Publish persistence;
- Payload Media picker opens from Replace.

## Site Model Evidence

First draft type:
`src/site-model/types.ts`

First Site Instance fixture:
`src/sites/car-service-garage.ts`

State: `0.1-draft`, not frozen.

The current shape is empirically sufficient for the first seed/render/editor/QA cycle. It must survive at least one additional, meaningfully different Site Instance before universal fields are promoted/frozen.

## Current Limitations / Not Yet Verified

The Hero semantic image lifecycle is accepted, but the universal editor contract is broader.

Still not fully browser-accepted end-to-end:
- alignment persistence;
- visual width/direct resize persistence where applicable;
- replace/remove persistence and editor/public-render parity;
- version restore through owner-facing editor UI;
- the same image behavior on a second reusable image-bearing block;
- visual parity with the final accepted Car Service Garage design direction;
- multi-site isolation under shared live operation;
- second Site Instance reuse;
- durable production media storage (free staging filesystem is not the production target).

## Next Required Slice

Continue the universal image-editor acceptance contract in the shared engine, not client-specific code.

Priority order:
1. Accept alignment + visual-width persistence on the reusable `ImageSection`, because Hero intentionally has `allowLayoutResize=false`.
2. Use that same slice to prove the shared image behavior on a second reusable image-bearing block rather than adding Hero-only logic.
3. Add replace/remove persistence coverage using Payload Media without relying on disposable client-specific assets.
4. Add version restore through owner-facing editor UI.
5. Only then add direct pointer resize acceptance where the reusable component contract permits it.
6. Bring Car Service Garage visual output to the accepted reference direction using only shared components and Site Instance data.
7. Validate a second, meaningfully different Site Instance without rebuilding generic infrastructure.
8. Promote only recurring Site Model/component contracts proven by both sites.

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
