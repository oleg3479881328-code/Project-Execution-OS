# References — Domain Block Creation

## Central Standards

- `START_HERE.md`
- `docs/ROUTER.md`
- `blocks/skill-creator/BLOCK.md`
- `docs/SKILL_SPEC.md`
- `docs/SKILL_LIFECYCLE.md`
- `docs/SKILL_REVIEW_STANDARD.md`
- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
- `docs/RESEARCH_STANDARD.md`
- `docs/KNOWLEDGE_SYSTEM.md`
- `docs/INDEXING_STANDARD.md`
- `docs/AGENT_INDEX_FIRST_ENTRY_STANDARD.md`

## Proven Internal Examples

### Music Domain Block

- `blocks/music/BLOCK.md`
- `knowledge-library/architecture-decisions/AI_MUSIC_CREATION_STACK.md`

### United States Law Domain Block

- `blocks/us-law/BLOCK.md`
- `blocks/us-law/immigration/BLOCK.md`
- `knowledge-library/architecture-decisions/US_LEGAL_RESEARCH_STACK.md`
- `knowledge-library/workflow-lessons/MARRIAGE_BASED_I485_PM_602_0199.md`

### Telegram Domain Block

- `blocks/telegram/BLOCK.md`
- `blocks/telegram/PRODUCT_SURFACES.md`
- `blocks/telegram/READY_SOLUTIONS.md`
- `blocks/telegram/SECURITY_AND_COMPLIANCE.md`
- `blocks/telegram/CURRENT_CAPABILITIES_2026-06-06.md`
- `blocks/telegram/VALIDATION_BACKLOG.md`
- `knowledge-library/architecture-decisions/TELEGRAM_PRODUCT_STACK.md`

## Reusable Lessons Extracted

1. A block is a reusable domain layer, not a random folder of notes.
2. `BLOCK.md` is the stable entrypoint and local router, not the encyclopedia.
3. Use three levels: reference note, compact block, full block.
4. Separate stable principles from dated capability snapshots.
5. Research candidates and verified workflows must remain distinct.
6. Ready-made solutions should be captured before custom invention.
7. Router registration, curated indexes, knowledge capture, and generated index refresh are part of block completion.
8. New blocks start as `candidate` until real use validates them.
9. The smallest sufficient reading path reduces token cost and context pollution.
10. Do not create blocks merely to create the appearance of progress.

## Duplicate Check

Repository search performed before creation.

No existing central skill was found with the same scope: converting a recurring domain into a right-sized reusable block with research, routing, knowledge capture, indexing, and validation.

The closest existing artifact is `blocks/skill-creator/BLOCK.md`, which governs creation of reusable skills. It does not replace this domain-block creation workflow.
