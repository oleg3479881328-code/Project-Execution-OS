# Router Patch — Reviewer Block

## Intended Router Entry

Add this route to `docs/ROUTER.md` near the logic and review routes:

```md
- reviewer block, expert review, critical review, artifact review, acceptance review, `ревью`, `экспертиза`, `критика`, or `аудит` -> `blocks/reviewer/BLOCK.md`
```

## Reason

The repository now contains `blocks/reviewer/BLOCK.md`, but the automated router update was not completed during initial creation.

## Manual Check

Before adding to the router, confirm that the route does not conflict with:

- `docs/REVIEW_STANDARD.md` for generic lightweight review;
- `blocks/logic/BLOCK.md` for logic-only reasoning review;
- domain-specific block review routes such as design, YouTube, Chrome Extension, immigration, tax, and OSINT.

## Intended Behavior

Use `blocks/reviewer/BLOCK.md` when the owner asks for a dedicated reviewer, expert review, hard critique, acceptance review, or cross-domain artifact review.

Use `docs/REVIEW_STANDARD.md` when the request is a small generic review and does not require the full reviewer block.