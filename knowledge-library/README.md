# Central Knowledge Library

## Purpose

This is the central reusable knowledge library for `Project Execution OS`.

It stores reviewed knowledge that has value beyond one project and is useful for future work.

Layer selection follows `docs/PROJECT_LIFECYCLE_MODEL.md` and knowledge promotion follows `docs/KNOWLEDGE_SYSTEM.md`.

## Project-Specific vs Central Knowledge

Project-specific knowledge stays in the durable layer the project actually uses:

- Notion-managed projects may keep local decisions and lessons in their Notion project space;
- GitHub-backed technical projects may keep technical lessons beside their versioned artifacts;
- Google Drive-backed asset collections may be referenced from the project's management layer.

Do not create a GitHub repository or local library folder merely because one note exists.

For a GitHub-backed project that genuinely benefits from a local library, `project-library/` is an available pattern, not a requirement.

Central reusable knowledge lives here in `knowledge-library/` only after there is evidence that it is worth reuse across projects.

## Review Before Active Reuse

A central knowledge entry becomes active only after review.

Before review, useful material may be kept as a `candidate` when preserving it prevents rediscovery or supports later validation.

A candidate is not an active system rule.

## Useful Entry Categories

Create category folders only when an accepted or useful candidate entry needs them. Categories may include:

- `patterns/`;
- `anti-patterns/`;
- `workflow-lessons/`;
- `research-methods/`;
- `architecture-decisions/`;
- `execution-standards/`;
- `verified-technical-solutions/`.

## Entry Content

A reusable entry should include only what helps later reuse:

- type and review status;
- source and evidence;
- problem addressed;
- reusable pattern or lesson;
- when to use and when not to use;
- adaptation notes;
- risks and validation still required.

For a narrow verified technical fix, use the compact format defined in `docs/KNOWLEDGE_SYSTEM.md`: `Problem / Investigation / Solution / Verification`.

## Anti-Dump Rule

Do not store random chat fragments, speculative active rules, project-only noise, secrets, duplicated entries or empty templates here.

Do not promote a historical claim as an active solution until current evidence supports it.