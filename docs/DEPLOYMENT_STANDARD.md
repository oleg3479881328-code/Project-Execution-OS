# Deployment Standard

## Purpose

This standard defines the default static deployment layer for `Project Execution OS`.

Default provider:

- `Cloudflare Pages`

This standard is for static and frontend deployment only.

## Applies To

Use this standard by default for:

- landing pages;
- documentation sites;
- static MVP websites;
- agent showcase pages;
- Website Design System demos;
- portfolio/static client sites.

## Default Flow

`VS Code / Codex -> GitHub -> Cloudflare Pages -> live URL`

## Default Source

- source: `GitHub repository`
- production branch: `main`

## Required Deployment Fields

Every deployable project that uses this standard should record:

- `deployment_provider`
- `github_repo`
- `production_branch`
- `build_command`
- `output_directory`
- `production_url`
- `preview_url`
- `custom_domain`
- `deployment_status`

## Standard Position

`Cloudflare Pages` is the default provider for static deployment in this system.

It is suitable for static/frontend projects only.

This standard does not cover:

- backend logic;
- databases;
- file storage;
- queues;
- long-running jobs;
- API runtimes.

If a project requires those layers, route it to a separate backend/runtime standard instead of stretching this document beyond static deployment.

`Workers`, `D1`, `R2`, or external services may be used later, but they must not be mixed into this standard unless a separate route exists.

## Minimum Project Recording

For a project using this deployment path, record the deployment fields inside the project entrypoint or equivalent durable project metadata.

Suggested values:

- `deployment_provider: Cloudflare Pages`
- `production_branch: main`

Other fields must remain honest and project-specific.

Unknown values are allowed when they are truly unknown.

Invented deployment state is not allowed.

## Codex Handoff Checklist

Before handing off or closing static deployment work, confirm:

- project type is static/frontend;
- build command is confirmed;
- output directory is confirmed;
- repo branch is confirmed;
- `README` includes deployment info;
- `PROJECT.md` includes deployment metadata;
- do not claim deployed unless the production URL is confirmed.

## Execution-State Rule

`generated_state != executed_state`

Codex may say:

- `prepared for Cloudflare Pages`

Codex must not say:

- `deployed`

unless `Cloudflare Pages` has actually produced a live production URL.

## Operational Rule

Keep this standard narrow, reusable, and MVP-first.

Use it to standardize static deployment routing and project metadata.

Do not expand it into a backend platform standard, infrastructure catalog, or secrets guide.
