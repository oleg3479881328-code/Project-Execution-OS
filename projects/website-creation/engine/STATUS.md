# Website Creator Engine — STATUS

Date: 2026-09-14
Status: ACTIVE — shared runtime + editor loop + first media field verified

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
- Render staging deployment adapter prepared through root `render.yaml`.

No Puck Cloud, Payload Cloud, Replit, Wix, Framer or other hosted website-builder dependency is required.

## Latest Full Verification

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

## Editor Architecture Proof

The shared component renderer remains server-safe.

Client-only editor capabilities such as Payload/Puck `createMediaField()` are added only in `src/puck/editor-config.ts` and are not invoked from the server-renderer component module.

This boundary is now protected by the same production build + browser acceptance workflow that caught the original server/client regression.

Current reusable section registry:
- Hero;
- Services;
- Process;
- Call to Action;
- Footer.

Current editor proof:
- `/editor` resolves to the canonical Puck editing route;
- Save and Publish actions are present;
- draft and published states are behaviorally distinct;
- version/history API path responds;
- public renderer reflects published edits and not draft-only edits;
- original content can be restored;
- Hero uses the Payload/Puck media picker in the editor.

## Render Staging State

Render workspace is connected and actionable from ChatGPT.

A free Ohio PostgreSQL staging instance has been created:
- Render resource: `website-creator-postgres`;
- resource id: `dpg-dak33ie1egvs739cfi90-a`;
- PostgreSQL 16;
- state verified as available.

The root `render.yaml` is the canonical free staging Blueprint and references this database by name through `fromDatabase.connectionString`.

Important connector boundary:
- Render's current direct `create_web_service` action only accepts literal environment-variable values and does not expose `fromDatabase` references;
- it also does not support the complete Docker/Blueprint configuration used by Website Creator;
- therefore the web service must be created/adopted through Render Blueprint sync, after which normal Render deploy/status/log actions can be managed from ChatGPT.

Do not copy database passwords/connection strings into Git or chat as a workaround.

## Site Model Evidence

First draft type:
`src/site-model/types.ts`

First Site Instance fixture:
`src/sites/car-service-garage.ts`

State: `0.1-draft`, not frozen.

The current shape is empirically sufficient for the first seed/render/editor/QA cycle. It must survive at least one additional, meaningfully different Site Instance before universal fields are promoted/frozen.

## Current Limitations / Not Yet Verified

- visual parity with the final accepted Car Service Garage design direction;
- direct image crop/move/zoom/resize interaction contract;
- full toolbar/inspector parity for image manipulation;
- version restore through owner-facing editor UI (API/version path exists);
- multi-site isolation under shared live operation;
- second Site Instance reuse;
- live Render web-service URL and production HTTP verification (waiting only on Blueprint resource creation/sync, not on engine build correctness).

## Next Required Slice

1. Create/sync the free Render staging Blueprint from the repository root `render.yaml` so it adopts/references `website-creator-postgres` and creates `website-creator-engine`.
2. Verify live `/health`, `/`, `/editor`, logs and first deploy.
3. Add the direct image interaction subset from `EDITOR_CREATION_STANDARD.md` (crop/move/zoom/size) as reusable editor capability, not client-specific code.
4. Validate a second, meaningfully different Site Instance without rebuilding generic infrastructure.
5. Promote only recurring Site Model/component contracts proven by both sites.

## Fresh-Chat Instruction

Before changing engine code:

1. read `../PROJECT.md`;
2. read `../PROJECT_STATE.md`;
3. read `../OWN_SYSTEM_EXECUTION_STANDARD.md`;
4. read this file;
5. read `README.md`;
6. read only the narrow contract relevant to the active change.

Do not create another engine, another client editor or another deployment experiment. Extend this shared engine unless a documented architecture decision replaces a binding.
