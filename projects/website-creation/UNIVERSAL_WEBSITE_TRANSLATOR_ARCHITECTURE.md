# Universal Website Translator — Dramaturg + Stagecraft Architecture

Status: `candidate / active research direction`
Date: 2026-09-21

## Purpose

Capture the generalized architecture discovered while testing Dramaturg/Playwright automation in visual website editors.

The target is not a Showit-specific script system and not another browser automation engine.

The target pattern is:

```text
SOURCE WEBSITE
→ CAPTURE
→ NORMALIZE
→ UNIVERSAL RECIPE
→ EDITOR ADAPTER
→ BUILD
→ VERIFY
```

Working label: **Universal Website Translator**.

Detailed durable research/decision record:
https://docs.google.com/document/d/1RmTaj0rH7J-VV3mTgOJRl_J09rs5J8UI6L0HuKH3H6k/edit

## Core Decision

Use existing browser automation infrastructure first.

Current primary candidate:

```text
Website Creator control/translation layer
        ↓
Stagecraft skills / recipes
        ↓
Dramaturg / playwright-repl
        ↓
Playwright / playwright-crx
        ↓
real authenticated Chrome session
```

Do not rebuild the Playwright engine, Chrome debugger/CDP bridge, PW parser, recorder, locator generation, snapshot engine, replay engine, variable substitution, browser MCP bridge, tab-attach plumbing, or JS debugger unless a concrete upstream gap is proven.

## PW-First Rule

- Linear browser/editor operations → native `.pw`.
- JavaScript is an escape hatch for loops, conditions, calculations, DOM diff, complex extraction, editor internals, or capabilities `.pw` cannot express reliably.
- Do not invent a second DSL before native `.pw` is proven insufficient.

## Stagecraft / Brick Layer

Stagecraft already provides much of the intended reusable-brick model:

- `SKILL.md`;
- `.pw` skills;
- `.js` fallback;
- user skill directory;
- discovery/list/run;
- `{{variable}}` substitution;
- recording/replay;
- ref-to-stable-locator conversion.

Our higher-level semantic operations may look like:

```text
showit.canvas.rename(name)
showit.text.set_content(value)
wix.page.rename(name)
wix.image.replace(asset)
```

These are conceptual control-layer names, not claims about native Dramaturg commands. Their implementation should use proven `.pw` sequences wherever practical.

## Capture Layer

A donor/source site fingerprint may include:

- page/section structure;
- content;
- typography;
- colors;
- spacing;
- geometry;
- images/media references;
- responsive states;
- interaction/motion evidence;
- design tokens;
- DOM/accessibility evidence;
- screenshots.

The normalized result must not be tied to a single editor.

## Editor Adapter Boundary

One normalized recipe should be able to feed different target adapters:

```text
Universal Recipe
  ├─ Showit Adapter
  ├─ Wix Adapter
  ├─ Webflow Adapter
  └─ future editor adapters
```

Each adapter translates normalized intent into tested browser/editor bricks.

## Showit / Wix Proof Strategy

Showit is the first proving ground. Existing work has already shown routine editor actions collapsing from large custom JS attempts into very short `.pw` flows.

Wix is the next strong proof candidate. Test a representative set such as page operations, sections, text, images, layout, mobile/responsive behavior, SEO controls and save/preview/publish.

If the same capture → recipe → adapter model works for both, that is strong evidence the subsystem is generic rather than Showit-specific.

## Scope: "Almost Any Website"

The architecture can potentially automate websites whose workflows are available through normal Chrome/browser surfaces such as DOM, accessibility tree, keyboard/pointer events, forms, frames/iframes and Playwright-accessible controls.

This is not a 100% universal-automation claim.

Common boundary classes include CAPTCHA, hardware WebAuthn, some 2FA steps, OS-native dialogs, hostile anti-bot systems, browser-internal restricted pages, opaque canvas/video-only interfaces, and workflows requiring native desktop software.

## AI Role

Preferred route:

```text
Task
→ find existing brick
→ compose bricks
→ fill parameters
→ execute native PW
→ verify
→ repair/create only missing brick
→ QA
→ promote accepted brick
```

AI should progressively work against a semantic registry of proven operations instead of generating raw Playwright from scratch for each task.

## Controlled Healing

Future locator healing should be explicit and acceptance-based:

```text
brick fails
→ recon/heal
→ identify equivalent target
→ test
→ QA
→ accept
→ update canonical brick
```

Do not silently mutate canonical automation on every run.

## Relationship To Website Creator

This architecture is an additional capture/execution path, not a replacement for the existing Website Creator shared engine or Site Model.

Possible routes:

1. donor site → fingerprint → normalized recipe → external editor adapter;
2. donor site → fingerprint → normalized recipe → Website Creator Site Model/components;
3. Website Creator Site Model → external editor adapter when a client must use Showit/Wix/etc.

Keep site intent/data, design fingerprint, normalized recipe and target-platform implementation as separate layers.

## Next Proof

Do not fork Dramaturg first.

Prove:

```text
known working Showit PW operation
→ Stagecraft skill
→ parameter
→ run/replay against real authenticated Chrome
→ deterministic verification
```

Then repeat against a small representative Wix operation set.

## Final Rule

The strategic goal is not to build another browser automation engine.

The strategic goal is to build the **minimum missing translation/control layer above a proven browser engine**.