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
- no Puck Cloud, Payload Cloud, Replit, Wix, Framer or other hosted builder dependency.

The external packages are replaceable implementation bindings. Website Creator contracts and Site Model remain canonical.

## Local start

Requirements: Node >= 20.9, pnpm, Docker.

1. Copy `.env.example` to `.env`.
2. Run `docker compose up -d`.
3. Run `pnpm install`.
4. Run `pnpm seed:csg`.
5. Run `pnpm dev`.
6. Open `/admin` to create the first admin user and edit Pages with Puck.

The Car Service Garage fixture is deliberately stored under `src/sites/`. It is evidence for Site Model v0.1, not a dependency of Website Creator standards.

## v0.1 acceptance slice

This first slice proves only the reusable plumbing:

- one canonical page record;
- Puck visual editing;
- Payload persistence/drafts/versions;
- public render from the same page state;
- deterministic seed from a Site Instance;
- browser QA path.

Pixel-perfect Car Service Garage parity and the reusable branded component set are the next validation slice, after this plumbing compiles and persists correctly.
