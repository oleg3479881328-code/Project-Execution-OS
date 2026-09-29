# Car Service Garage — Light Minimal landing + editor + Vercel release handoff

Date: 2026-09-29
Status: CODE/EDITOR ACCEPTED; PRODUCTION VERCEL RELEASE BLOCKED BEFORE FIRST DEPLOYMENT

## Owner assignment

Build the supplied light-minimal Car Service Garage landing, keep the established visual editor, and publish to Vercel with exactly one production deployment pass.

## Canonical route used

Existing Solution First was applied. The implementation stays inside the shared Website Creator engine rather than creating another static/client-specific site:

`Site Instance → Payload/Puck canonical page state → shared renderer → authenticated visual editor → draft/publish/version state → public site → QA → GitHub main → Vercel production`

Olga Polo was used only as the proven release/editor donor: GitHub is the source transport, Vercel Git Integration is the production release trigger, and Vercel is not used as an iterative fix/test loop.

## Implemented

Merged PR: https://github.com/oleg3479881328-code/Project-Execution-OS/pull/149
Main SHA: `3fac7cab5057def9bfea121f9db8277bd573aaa0`

Changes:
- rebuilt `car-service-garage-ohio` Site Instance to the supplied light/blue minimal direction;
- preserved the shared Payload/Puck visual editor instead of shipping static HTML;
- added reusable Header, Trust Strip, Benefits, and Testimonials/Contact sections;
- retained existing Website Creator Hero/Services/Process/Footer components and image editor;
- reused the previously approved Car Service Garage media donor;
- public renderer and editor canvas share the same presentation styles;
- updated desktop/mobile and editor draft/publish/version acceptance tests.

## Acceptance evidence

Authoritative Website Creator Engine PR CI:
- run `36614221098` / run number 121;
- dependency install PASS;
- TypeScript check PASS;
- production migrations on empty PostgreSQL PASS;
- Car Service Garage seed PASS;
- production Next.js build PASS;
- Chromium setup PASS;
- browser acceptance PASS;
- desktop/mobile screenshots and migration evidence uploaded;
- authenticated editor load PASS;
- shared image toolbar/inspector interaction PASS;
- media picker PASS;
- draft not visible publicly PASS;
- publish visible publicly PASS;
- versions endpoint PASS;
- restore to original published content PASS.

The repository-wide `Validate Project OS Integrity` job failed independently on a pre-existing `docs/ROUTER.md` manifest SHA mismatch (`recorded 4dfde07f...`, `calculated cf24479f...`). Website Creator-specific CI was green and the failure was not caused by this landing/editor change.

## Vercel state / one-pass gate

Target project:
- name: `car-service-garage-ohio`
- project ID: `prj_bfJqHLA7VRZtwAEWrOCP7mbmOqIf`
- team ID: `team_2eC69dsqCNN9P3if0ppakpN7`
- production URL: `https://car-service-garage-ohio.vercel.app/`

Historical related editor project also exists:
- `car-service-garage-olga-editor`
- project ID: `prj_MTdqeZFGFVszFfI6SMMCYlspL94L`

After merging PR #149, Vercel deployment history was checked for both projects. No new deployment was created. Therefore the requested one-pass production deployment has NOT been consumed.

Diagnosis:
- the target Car Service Garage Vercel projects are not currently receiving GitHub main pushes;
- their historical deployment metadata does not contain GitHub commit metadata;
- the current ChatGPT Vercel connector can read teams/projects/deployments, but its advertised `deploy_to_vercel` write tool is backend-broken (`Tool deploy_to_vercel not found`) and it exposes no project Git-connect/update action;
- `get_project` also has a connector schema/backend mismatch (`projectId` advertised, backend requests `idOrName`).

Olga Polo confirms the desired proven route: Vercel Git Integration is authoritative; manual fallback workflow is disabled.

## Runtime dependency gate before Vercel connection

The shared editor runtime is not static. It requires persistent PostgreSQL plus Payload runtime configuration.

Current shared staging database is Render PostgreSQL `website-creator-postgres` (`dpg-dak33ie1egvs739cfi90-a`), PostgreSQL 16, Ohio, currently free and scheduled to expire 2026-10-14. It is suitable as existing staging evidence, not a durable long-term production database without an explicit infrastructure decision.

Do NOT connect the Vercel Git project and trigger the first production build until production runtime variables/database are ready. Required baseline includes at minimum `DATABASE_URL` and `PAYLOAD_SECRET`; owner admin bootstrap uses `WC_ADMIN_EMAIL` / `WC_ADMIN_PASSWORD` when a new database is initialized.

## Exact next action

Use Vercel project settings (or a browser-capable Work session) to complete the one-time production binding BEFORE deployment:

1. choose/confirm a durable PostgreSQL resource for the Website Creator production editor;
2. configure required Vercel runtime variables without exposing secrets in chat/logs;
3. connect existing Vercel project `car-service-garage-ohio` to GitHub repository `oleg3479881328-code/Project-Execution-OS`;
4. set Root Directory to `projects/website-creation/engine`;
5. production branch = `main`;
6. only after all preflight settings are complete, allow exactly ONE production deployment;
7. wait for READY;
8. run public landing read-back plus `/editor` authentication/editor smoke plus desktop/mobile Live QA;
9. only then mark DEPLOYED/PUBLISHED.

Do not use Vercel preview deployments or repeated production pushes as a fix/test loop.

## Do not repeat

- Do not deploy the earlier static ZIP as the final architecture.
- Do not overwrite the unrelated `autoservice-landing` / SIS Motors repository.
- Do not invent another client-specific editor.
- Do not use Vercel Drop as the normal route.
- Do not claim production deployed until a new Vercel deployment exists and Live QA passes.
