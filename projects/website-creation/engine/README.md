# Website Creator Engine

This directory is the first real implementation of the reusable Website Creator runtime.

It is not a Car Service Garage application. Car Service Garage is only the first Site Instance used to validate the engine.

## Architecture

`Site Instance -> Payload/Puck canonical page state -> shared renderer -> public site -> Playwright QA`

Core choices for v0.1:

- Next.js / React renderer;
- Payload CMS as self-hosted content/auth/versioning backend;
- PostgreSQL as database;
- Puck through the MIT `@delmaredigital/payload-puck` integration as the embedded visual editor;
- Playwright for deterministic browser QA;
- Docker / Docker Compose for a portable runtime;
- no Puck Cloud, Payload Cloud, Replit, Wix, Framer or other hosted website-builder dependency.

The external packages are replaceable implementation bindings. Website Creator contracts and Site Model remain canonical.

## Fastest local start

Requirements: Docker Desktop.

1. Copy `.env.example` to `.env` and replace `PAYLOAD_SECRET`, `WC_ADMIN_EMAIL`, and `WC_ADMIN_PASSWORD`.
2. Run `docker compose up --build`.
3. Open `http://localhost:3000/` for the site.
4. Open `http://localhost:3000/editor` for the stable editor entry point. It resolves the homepage and redirects to the Puck editor.
5. Open `http://localhost:3000/admin` for the full Payload admin.
6. Open `http://localhost:3000/health` for database/runtime health.

The container startup command runs committed Payload migrations first, seeds missing Car Service Garage fixture pages without overwriting owner edits, bootstraps the admin account only when the configured email does not already exist, and then starts the production server.

Set `WC_SEED_FORCE=true` only when you intentionally want the fixture seed to overwrite an existing matching page.

## Source-development start

Requirements: Node >= 20.9, pnpm, Docker.

1. Copy `.env.example` to `.env`.
2. Run `docker compose up -d postgres`.
3. Run `pnpm install`.
4. Run `pnpm payload migrate`.
5. Run `pnpm seed:csg`.
6. Run `pnpm dev`.

## Production deployment

The runtime is host-portable. Production requirements are:

- persistent PostgreSQL;
- persistent application filesystem or an object-storage adapter before relying on local uploaded media;
- `DATABASE_URL`;
- long random `PAYLOAD_SECRET`;
- `WC_ADMIN_EMAIL` and `WC_ADMIN_PASSWORD` for first-run admin bootstrap;
- HTTPS at the hosting layer.

`render.yaml` is included as the first replaceable deployment adapter. The application itself does not depend on Render.

Production start command:

```bash
pnpm start:prod
```

This runs database migrations, non-destructive fixture/admin bootstrap, then `next start`.

## Verification

GitHub Actions workflow `.github/workflows/website-creator-engine.yml` verifies on a fresh PostgreSQL database:

- TypeScript;
- committed production migrations;
- production seed/admin bootstrap;
- production build;
- runtime health endpoint;
- public desktop/mobile rendering;
- authenticated editor load;
- draft save that does not leak to public;
- version-history API availability;
- publish to public renderer;
- restoration of original content;
- browser screenshot evidence.

The Car Service Garage fixture is deliberately stored under `src/sites/`. It is evidence for Site Model v0.1, not a dependency of Website Creator standards.

## Current editor/media boundary

The shared Puck editor already exposes reusable media selection and standard image controls available from the integration component set, including alt override, aspect ratio, dimensions, alignment, transform, spacing and reset. Payload provides the Media library and image focal-point fields.

The Olga-style freeform crop/pan/zoom/direct-resize interaction remains a separate editor capability. It must be added only when a real Site Instance requires that richer behavior; it is not a prerequisite for ordinary sites that can use the standard media/editor controls.
