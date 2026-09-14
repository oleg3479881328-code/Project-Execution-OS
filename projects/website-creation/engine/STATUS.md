# Website Creator Engine — STATUS

Date: 2026-09-14
Status: ACTIVE — shared runtime + live editor loop + first media field verified

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

Commit: `4304a3b2df1906da63f398f9cb2295151c2fe363`
Workflow: Website Creator Engine run `34876621298`
Result: PASS

Verified in one clean run:
- dependency install;
- TypeScript check;
- committed production migration artifacts;
- migrations applied to an empty PostgreSQL database;
- Car Service Garage seed;
- production Next.js build;
- Chromium installation;
- production server startup;
- health/public HTTP checks;
- authenticated Puck editor load;
- draft mutation not visible publicly;
- versions endpoint available;
- publish mutation visible publicly;
- restore of original published content;
- editor screenshot/evidence upload;
- first reusable Hero media field wired editor-only so the server renderer remains build-safe.

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

Client-only editor capabilities such as Payload/Puck `createMediaField()` are added only in `src/puck/editor-config.ts` and are not invoked from the server-renderer component module.

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
- Hero uses the Payload/Puck media picker in the editor.

## Site Model Evidence

First draft type:
`src/site-model/types.ts`

First Site Instance fixture:
`src/sites/car-service-garage.ts`

State: `0.1-draft`, not frozen.

The current shape is empirically sufficient for the first seed/render/editor/QA cycle. It must survive at least one additional, meaningfully different Site Instance before universal fields are promoted/frozen.

## Current Limitations / Not Yet Verified

- visual parity with the final accepted Car Service Garage design direction;
- direct per-instance image crop/move/zoom/resize interaction contract;
- full toolbar/inspector parity for image manipulation;
- version restore through owner-facing editor UI (API/version path exists);
- multi-site isolation under shared live operation;
- second Site Instance reuse;
- durable production media storage (free staging filesystem is not the production target).

## Next Required Slice

1. Add the direct per-instance image interaction subset from `EDITOR_CREATION_STANDARD.md` as reusable Website Creator capability, not client-specific code.
2. Prefer proven building blocks: Payload/Puck media selection, percentage-based crop metadata, `react-easy-crop` for crop/pan/zoom, and `react-moveable` only where direct canvas resize is needed and proven stable.
3. Verify editor/public-render parity after image edits and persistence after reload.
4. Bring Car Service Garage visual output to the accepted reference direction using only shared components and Site Instance data.
5. Validate a second, meaningfully different Site Instance without rebuilding generic infrastructure.
6. Promote only recurring Site Model/component contracts proven by both sites.

## Fresh-Chat Instruction

Before changing engine code:

1. read `../PROJECT.md`;
2. read `../PROJECT_STATE.md`;
3. read `../OWN_SYSTEM_EXECUTION_STANDARD.md`;
4. read this file;
5. read `README.md`;
6. read only the narrow contract relevant to the active change.

Do not create another engine, another client editor or another deployment experiment. Extend this shared engine unless a documented architecture decision replaces a binding.
