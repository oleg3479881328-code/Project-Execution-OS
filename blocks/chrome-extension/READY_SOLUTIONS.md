# Chrome Extension Ready Solutions

## Purpose

Preserve ready frameworks, boilerplates, and donor repositories so agents check proven options before inventing custom extension infrastructure.

## Default Recommendation

Use `WXT` for most new serious extension products.

Reason:

- modern extension framework;
- TypeScript-friendly;
- supports React and other UI stacks;
- supports Manifest V3;
- supports multiple browsers;
- includes development, build, and publishing-oriented workflows.

## Framework Candidates

### WXT

Best default for productized extensions.

Use when:

- the extension may grow beyond a toy MVP;
- cross-browser support may matter later;
- React/TypeScript is expected;
- content scripts, background logic, popup/options UI, and publishing need a coherent workflow.

Risk:

- agents must still understand Manifest V3 concepts instead of hiding everything behind the framework.

### Plasmo

Strong product framework for React-based browser extensions.

Use when:

- speed of product UI development matters;
- the team wants a high-level extension framework;
- the extension is UI-heavy.

Risk:

- compare lock-in, build conventions, and publishing needs against WXT before choosing.

### CRXJS

Good Vite-centered option.

Use when:

- the team already works in Vite;
- manual control is preferred;
- the extension architecture is simple enough that a smaller layer is better.

Risk:

- less complete product scaffolding than WXT/Plasmo.

### Extension.js

Good zero-config/cross-browser candidate.

Use when:

- fast setup matters;
- the project wants broad browser-extension compatibility;
- the team wants less custom build wiring.

Risk:

- validate real project needs before adopting.

## Starter / Donor Repositories

### Minimal MV3 starter

Use a minimal Manifest V3 starter when the goal is to understand the platform or ship a tiny extension without framework ceremony.

Good for:

- proof of concept;
- learning `manifest.json`;
- content script and service worker basics;
- debugging Chrome-specific behavior.

### React + TypeScript + Vite starter

Use when the desired stack is already React/TypeScript/Vite and the project does not need a full extension framework.

Good for:

- popup/options UI;
- internal tools;
- small UI-heavy extensions;
- fast handoff to frontend agents.

## Donor Evaluation Checklist

Before accepting a donor:

- last meaningful update is recent enough for MV3 work;
- Manifest V3 support is real, not just claimed;
- permissions are not overly broad;
- build flow is understandable;
- local development works without secrets;
- license is compatible with intended use;
- issue tracker does not show unresolved blockers for Chrome MV3;
- publishing path is documented or easily inferable.

## Final Rule

Do not start a custom extension stack until WXT, Plasmo, CRXJS, Extension.js, and one minimal MV3 starter have been considered.