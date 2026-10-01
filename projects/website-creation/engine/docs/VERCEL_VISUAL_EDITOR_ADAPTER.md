# Vercel Visual Editor Adapter

Status: draft implementation branch

Goal: add a reusable `/editor` layer to existing Next.js projects deployed on Vercel, using the already adopted Puck stack. This is intentionally narrow: no new CMS, no ChatGPT dependency, no fingerprint importer, and no separate website-builder platform.

The implementation on this branch will define the minimum adapter contract, shared editor shell, and a reference integration using the existing Website Creator engine.
