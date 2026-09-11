# AI Frontend Existing Solution First Toolchain

Type: pattern
Lifecycle status: candidate
Captured: 2026-09-11

## Source / Evidence

Research note triggered by comparison of four external tools:

- 21st.dev / Magic MCP — https://21st.dev/
- Impeccable — https://github.com/pbakaus/impeccable
- Humanizer — https://github.com/blader/humanizer
- Claude Code Setup — official Anthropic plugin / Claude Code setup recommender

Related existing PEOS artifact:

- `blocks/design/IMPECCABLE_DESIGN_QA_GATE.md`

Time-sensitive pricing, catalog counts, free-tier limits, compatibility details and product capabilities must be revalidated from current official sources before adoption.

## Problem / Context

AI-coded websites and interfaces tend to lose time in two places:

1. agents recreate UI patterns or components that already exist;
2. implementation is treated as finished when it compiles, even though design quality and public-facing copy still need dedicated QA.

The reusable idea is to separate discovery, implementation, visual QA and text QA instead of asking one model pass to do all four at once.

## Candidate Pattern

```text
Existing Solution First
-> ready-made UI/component/template discovery
-> implementation
-> frontend design QA
-> public-text editorial QA
```

Current candidate mapping:

```text
Existing Solution First
-> 21st.dev / Magic MCP
-> Codex
-> Impeccable
-> Humanizer
```

## Tool Roles

### 21st.dev / Magic MCP

Candidate role: external ready-made UI discovery layer.

Use it before inventing a component from scratch when a suitable professional component, template or pattern may already exist.

Why it matters to PEOS: it directly supports the system principle that an existing proven solution should be checked before new construction.

Status: strong donor / candidate first-class tool for frontend work. Not yet a mandatory dependency.

### Impeccable

Candidate role: post-implementation frontend QA gate.

PEOS already has a dedicated Impeccable design QA gate. Its responsibility is not initial ideation but design-quality review after implementation: hierarchy, responsiveness, accessibility, generic AI UI patterns, polish and release readiness.

Status: existing PEOS candidate quality gate.

### Humanizer

Candidate role: final editorial QA for public-facing text.

Useful areas include SEO copy, landing-page copy, wedding stories and client-specific tone-of-voice cleanup.

Do not define its value as guaranteed AI-detector evasion. Treat it as an editorial/style cleanup layer.

Status: candidate external tool.

### Claude Code Setup

Candidate role for PEOS: architecture donor, not core runtime dependency.

The useful transferable idea is a project-capability recommender: inspect a project, identify its stack and needs, then recommend only the already-existing MCPs, skills, hooks, agents or reusable capability blocks that fit that project.

Because the current preferred execution stack is Codex-first, the Anthropic-specific plugin itself should not become a mandatory dependency merely because the pattern is useful.

Status: architecture donor.

## Applies To

- AI-coded landing pages;
- marketing websites;
- portfolio sites;
- Automatic Website Factory work;
- client-facing web interfaces;
- Design Picker / donor-driven implementation flows.

## Triggers

Load this pattern when:

- a coding agent is about to build visible frontend UI;
- the owner asks how to reduce AI-slop or generic UI;
- the task can benefit from existing professional components/templates;
- frontend implementation is complete and needs a release-quality pass;
- public-facing copy needs a client-specific final style pass.

## Do Not Load When

- backend-only work;
- scripts/infrastructure with no visible UI;
- trivial text-only edits;
- tasks where no component discovery, frontend QA or public-copy QA is needed.

## Adaptation Notes

The pattern is layered, not bundled. Each tool should remain optional and task-scoped.

Do not force 21st.dev when a project's existing design system already owns the component.
Do not run a full Impeccable gate for trivial UI changes.
Do not run Humanizer before factual, legal, SEO or client-content correctness is settled.
Do not adopt Claude Code Setup as a dependency merely to copy its recommendation pattern.

## Risks

- vendor capabilities and pricing change;
- too many always-on tools can increase latency and context cost;
- component libraries can introduce visual inconsistency when copied without project design context;
- style cleanup can damage factual/SEO meaning if applied before content correctness is locked;
- tool overlap can create redundant QA unless roles remain explicit.

## Verification / Review Status

Candidate pattern assembled from current tool research and existing PEOS design QA architecture on 2026-09-11.

It is not yet a mandatory PEOS standard. Promote only after real project use confirms that the layered chain improves quality and/or reduces implementation time without excessive overhead.
