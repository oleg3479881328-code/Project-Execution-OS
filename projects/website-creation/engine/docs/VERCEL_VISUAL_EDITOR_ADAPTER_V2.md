# Vercel Visual Editor Adapter

Status: implementation in progress on `feature/vercel-visual-editor-adapter`.

## Scope

Add a reusable `/editor` layer to existing Next.js projects deployed on Vercel using the already adopted Puck stack.

Explicitly out of scope:
- a new CMS;
- ChatGPT as an editing dependency;
- fingerprint/Showit import;
- a separate website-builder platform;
- project-specific Olga/Venue/Wedding concepts.

## Target integration

Existing Vercel/Next.js project
→ register editable React components
→ provide page-state load/save binding
→ mount shared `/editor`
→ edit with Puck
→ public renderer consumes the same canonical page state.

## Minimal adapter contract

A project adapter must provide only:
1. a Puck `Config` for the React components that are editable;
2. current page data (`Data`);
3. a save handler for draft state;
4. a publish handler only when the project has a separate publish step;
5. optional project metadata (page label, public URL, viewport presets).

The shared editor must not know project-domain concepts. Those remain in the project adapter/component config.

## Reuse policy

Reuse existing Website Creator Puck integration, Git-backed persistence route, Olga image-editing mechanisms where they are generic, and Playwright QA. Do not create parallel persistence or deployment paths.
