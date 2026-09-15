# Website Creator Engine — STATUS

Date: 2026-09-15
Status: ACTIVE — shared runtime + live editor loop + first image-editor interaction slice FULL GREEN

## Verified Engine Boundary

Current reusable runtime:

`Site Instance → deterministic seed → Payload/Puck page state → shared renderer → authenticated visual editor → draft/publish/version state → public website → Playwright QA`

Implementation binding:

- Next.js / React;
- Payload CMS;
- PostgreSQL;
- Puck through `@delmaredigital/payload-puck`;
- Playwright;
- Docker Compose for local database startup;
- Render staging deployment adapter through root `render.yaml`.

No Puck Cloud, Payload Cloud, Replit, Wix, Framer or other hosted website-builder dependency is required.

## Latest Full CI Verification

Commit: `2c9f3e63d037e7ebd4aeeb7d5727de61c4cad9cd`
Workflow: Website Creator Engine run `34916717349`
Job: `build-and-runtime-smoke`
Result: PASS / FULL GREEN

Verified in one clean run:
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
- sequential Shape change `portrait → square → portrait` without losing the active edit target;
- sequential zoom edits while the same image remains active;
- Replace action opening the Payload media picker;
- supported media-picker close path;
- draft mutation remaining invisible publicly;
- versions endpoint availability;
- publish mutation becoming visible publicly;
- restoration of original published content;
- browser/migration evidence upload.

The previous red run `34915425336` is superseded by this green run. Do not reopen the old selection-persistence diagnosis unless a regression reproduces it.

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

Detailed decision record: `IMAGE_EDITOR_STATE_INTEGRATION_DECISION.md`.

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
- Save and Publish actions are present;
- draft and published states are behaviorally distinct;
- version/history API path responds;
- public renderer reflects published edits and not draft-only edits;
- original content can be restored;
- Hero uses the Payload/Puck media picker in the editor;
- selected Hero image stays active through sequential atomic property replacements;
- contextual toolbar and inspector remain available after Shape/zoom edits.

## Site Model Evidence

First draft type:
`src/site-model/types.ts`

First Site Instance fixture:
`src/sites/car-service-garage.ts`

State: `0.1-draft`, not frozen.

The current shape is empirically sufficient for the first seed/render/editor/QA cycle. It must survive at least one additional, meaningfully different Site Instance before universal fields are promoted/frozen.

## Current Limitations / Not Yet Verified

The first image-editor continuity bug is solved, but the universal editor contract is not yet complete.

Still not fully browser-accepted end-to-end:
- crop/move modal drag behavior;
- crop persistence and reopen behavior;
- Fill vs Whole semantics;
- Reset crop semantics;
- alignment persistence;
- visual width/direct resize persistence where applicable;
- alt/caption persistence;
- replace/remove persistence and editor/public-render parity;
- image changes surviving Save Draft + reload;
- image changes remaining draft-only until Publish;
- image changes appearing publicly after Publish;
- version restore through owner-facing editor UI;
- shared image behavior across more than the Hero block;
- visual parity with the final accepted Car Service Garage design direction;
- multi-site isolation under shared live operation;
- second Site Instance reuse;
- durable production media storage (free staging filesystem is not the production target).

## Next Required Slice

Continue the universal image-editor acceptance contract in the shared engine, not client-specific code.

Priority order:
1. Add deterministic Playwright coverage for Fill / Whole + Reset semantics on the selected Hero image.
2. Add crop/move modal acceptance: open, drag/zoom, Apply, reopen, verify persisted crop metadata/visual state.
3. Verify Save Draft + reload persistence for image state while public remains unchanged.
4. Verify Publish makes the same image state reach the public renderer.
5. Add replace/remove persistence coverage using the Payload media picker without relying on disposable client-specific assets.
6. Expand the same image behavior to another applicable reusable block before calling the contract universal.
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
