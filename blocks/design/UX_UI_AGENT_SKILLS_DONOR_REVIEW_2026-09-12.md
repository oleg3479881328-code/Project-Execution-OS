# UX/UI Agent Skills — Donor Review

Date: `2026-09-12`
Status: `EXTERNAL / STRONG DONOR / CANDIDATE FIRST-CLASS DESIGN-ENGINEERING TOOL`
Official source: `https://github.com/plugin87/ux-ui-agent-skills`
Reviewed release: `v2.5.1` published `2026-08-26`

## Purpose

This record preserves the review of `plugin87/ux-ui-agent-skills` as a reusable donor for the Project Execution OS Design Block.

The repository is not a normal UI runtime library. It is a structured knowledge and instruction layer for AI agents, with a request router, runnable design skills, design tokens, framework adapters, accessibility guidance, design-system references, deterministic validators, and QA/evaluation tooling.

The main reason it fits PEOS is architectural rather than aesthetic: it follows the same basic pattern of routing first, loading only relevant knowledge, invoking a bounded specialist capability, and verifying the result.

## Decision

Do **not** replace the PEOS Design Block with this repository.

Do **not** install the whole kit at the root of PEOS or allow its `CLAUDE.md` to become a canonical PEOS instruction surface.

Treat it as:

```text
PEOS Design Block
-> Existing Solution First
-> donor/reference research
-> owner direction / Design Picker when needed
-> ux-ui-agent-skills specialist execution or borrowed patterns
-> PEOS Taste anti-slop pre-flight
-> Impeccable or documented manual visual QA
-> release decision
```

PEOS remains the orchestrator and owns product context, business/user goals, existing project evidence, donor selection, page strategy, implementation constraints, acceptance, and durable knowledge.

`ux-ui-agent-skills` is a candidate specialist design-engineering layer.

## Strongest Reusable Findings

### 1. Screenshot/reference -> design system -> code

The `image-to-code` workflow is stronger than naive screenshot cloning.

It first infers:

- palette;
- typography feel and scale;
- spacing rhythm and density;
- radii and depth;
- layout archetype and sequence.

It then maps that into a shared token theme, builds components/code, renders the result, compares it to the reference, and runs checks.

Borrow the principle:

> extract the visual system and hierarchy, not copyrighted assets or one-off pixels.

This is a strong fit for PEOS `Design Picker`, Refero/Refero Styles, approved screenshots, and donor-site analysis.

### 2. Three-tier token architecture

The repository uses:

```text
Primitive -> Semantic -> Component
```

This is a strong default architecture for generated sites and editors because it reduces hardcoded values and keeps restyling, theming, dark mode, QA, migration and agent handoff coherent.

### 3. Deterministic design QA

The strongest technical value is the combination of design guidance with executable gates.

Useful checks include:

- token validation;
- color contrast validation;
- hardcoded-value linting;
- axe-style automated accessibility;
- rendered/composited contrast measurement;
- visual regression;
- state coverage;
- RTL;
- responsive breakpoints;
- keyboard/focus behavior;
- reduced motion;
- target size;
- overflow/clipping;
- token-by-intent checks.

This supports the PEOS distinction:

```text
measurable correctness -> deterministic gates
visual/taste quality -> critique / Impeccable / human judgment
```

A passing automated gate is not proof that the design is good.

### 4. Audit-first redesign

The donor's redesign sequence is:

```text
Scan -> Diagnose -> Direct -> Apply -> Verify
```

This is compatible with the PEOS Existing Surface Redesign flow:

```text
Scan -> Diagnose -> Fix -> Test -> QA
```

Important borrowed guardrails:

- inspect framework, styling, tokens and component reality before changing UI;
- preserve working behavior;
- diagnose before editing;
- apply tokens first, then typography/spacing/states/motion;
- verify again after redesign;
- keep one shared theme instead of page-specific palette drift.

### 5. Named aesthetic systems as translation input

The donor can resolve an archetype or named design system into semantic token roles rather than treating “make it like X” as a vague prompt.

Borrow the translation model:

```text
selected reference / aesthetic
-> semantic colors
-> typography
-> spacing
-> radius
-> shadow
-> motion
-> contrast verification
```

Do not treat named brands as clone targets.

### 6. Framework adapter protocol

The design logic is separated from one implementation framework.

Borrow the adapter-contract idea so PEOS design outputs can target the existing stack instead of making React/Tailwind a global assumption.

### 7. State-aware component discipline

A component specification should cover anatomy, variants, states, tokens, accessibility and responsive behavior, not only a default visual state.

This is especially useful for editors, product UI, image controls, forms, onboarding, and generated site tooling.

## Relationship To Existing PEOS Design Stack

### Refero / Refero Styles

Role: external reference discovery and Style DNA source.

Candidate chain:

```text
Refero research
-> owner selects references
-> structured style extraction / token normalization
-> implementation
-> QA
```

### 21st.dev / Magic MCP

Role: Existing Solution First component/template discovery.

Prefer finding a proven component/pattern before generating a new one. Normalize imported components to project tokens, accessibility and behavior.

### PEOS Taste Frontend Execution Standard

Role: generation-time anti-slop guidance grounded in product context.

The donor has overlapping taste guidance, but PEOS remains authoritative because the internal standard explicitly prevents aesthetic guidance from overriding product, audience, stack, accessibility, performance or existing project evidence.

### Impeccable

Role: downstream visible design QA/polish.

Keep Impeccable or documented manual fallback after deterministic gates. The two layers are complementary, not substitutes.

## Candidate Production Chain

```text
product goal + user path
-> Existing Solution First
-> inspect existing tokens/components
-> approved component donors when useful
-> visual donor research when direction is unresolved
-> owner selection when needed
-> normalize into design tokens/system rules
-> smallest relevant ux-ui-agent-skills capability
-> Codex implementation against the real stack
-> deterministic QA
-> PEOS anti-slop pre-flight
-> Impeccable/manual visual QA
-> release
```

## Current SOFT/PEOS Use Cases

Potential high-value pilots:

- Design Picker: convert approved references into portable style/system context;
- wedding-site work: preserve functionality while translating references into coherent implementation;
- image editor: specify crop/pan/zoom/focal/replace/remove controls with complete interaction states;
- Automatic Website Factory: enforce one shared theme and deterministic QA across generated pages;
- any AI-coded frontend: use token/a11y/responsive/state gates before declaring completion.

## Do Not Adopt Blindly

Do not:

- wholesale-install the external kit into PEOS root;
- let its agent persona/router replace PEOS routing;
- load every skill/design system on every task;
- migrate a project to the donor's preferred structure without need;
- copy brand assets, proprietary typography or copyrighted imagery;
- use a marketing aesthetic on dense workflow/product UI without justification;
- add motion because it exists;
- treat objective gates as proof of taste;
- depend on unpinned `main` for production behavior.

## Adoption Path

### Phase 1 — pattern extraction

Borrow and map the smallest useful ideas:

- image/reference -> design-system extraction;
- three-tier token architecture;
- deterministic design QA;
- audit-first redesign;
- framework adapter contract;
- state-aware component specifications.

### Phase 2 — controlled pilot

Test on one real PEOS/SOFT frontend surface with before/after evidence.

Measure:

- implementation effort;
- output quality;
- false positives/negatives in gates;
- token overhead;
- accessibility findings;
- compatibility with existing stack;
- whether it improves or duplicates Impeccable/Taste work.

### Phase 3 — PEOS-native wrapper

If the pilot succeeds, create a PEOS-native wrapper or bounded capability rather than making the donor's own project instructions canonical.

### Phase 4 — CI integration

Only after real validation, consider selected QA scripts/gates in CI and pin a reviewed version/commit.

## License / Version Notes

At the review snapshot:

- README and package metadata state MIT;
- GitHub repository metadata did not expose a license field in the connector response;
- reviewed release is `v2.5.1`;
- current version, license, dependencies and compatibility must be revalidated at adoption time.

## Source Trail

Primary reviewed source:

- `https://github.com/plugin87/ux-ui-agent-skills`
- repository README
- `docs/WORKFLOW.md`
- `.claude/skills/apply-aesthetic/SKILL.md`
- `.claude/skills/design-qa/SKILL.md`
- `.claude/skills/image-to-code/SKILL.md`
- `.claude/skills/redesign/SKILL.md`
- release `v2.5.1`

Related PEOS files:

- `blocks/design/BLOCK.md`
- `blocks/design/TASTE_FRONTEND_EXECUTION_STANDARD.md`
- `blocks/design/IMPECCABLE_DESIGN_QA_GATE.md`
- `blocks/design/DONORS.md`
- `docs/RESEARCH_STANDARD.md`

## Final Rule

PEOS chooses **what should be designed and why**.

`ux-ui-agent-skills` may help translate that decision into a coherent design system, implementation discipline and measurable QA.

Final visible quality still requires project-grounded review; deterministic correctness is necessary but not sufficient.