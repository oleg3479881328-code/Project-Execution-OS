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
1. a Puck config for the React components that are editable;
2. current page data;
3. a draft-save handler;
4. a publish handler only when the project has a separate publish step;
5. optional title/path/viewports/plugins.

The shared editor must not know project-domain concepts. Those remain in the project adapter/component config.

## Reuse policy

Reuse the existing Website Creator Puck integration, existing project persistence routes, generic Olga image-editing mechanisms, and Playwright QA. Do not create parallel persistence or deployment paths.

## Current proof

`CsgPuckEditor` is the first reference adapter. Its former project-specific Puck shell has been extracted to `src/visual-editor/VisualEditorShell.tsx`; CSG now only supplies config, initial data, image plugin, and persistence callbacks. A second Vercel project should be able to reuse the same shell without copying the editor implementation.
