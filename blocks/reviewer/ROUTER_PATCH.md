# Router Patch — Reviewer Block

## Intended Router Entry

Add this route to `docs/ROUTER.md` near the logic and review routes:

```md
- `режим ревьюера`, `ревьюер`, `режим эксперта`, `режим экспертизы`, `жесткий ревьюер`, `жёсткий ревьюер`, `жесткое ревью`, `жёсткое ревью`, `режим критика`, `экспертное ревью`, reviewer block, reviewer mode, expert reviewer, critical review, artifact review, or acceptance review -> `blocks/reviewer/BLOCK.md`
```

## Activation Reply Rule

When the owner sends only a reviewer activation phrase, the startup response is exactly:

`Ревьюер готов босс`

Do not list capabilities or explain the mode in that activation reply.

## Reason

The repository contains `blocks/reviewer/BLOCK.md` with a dedicated activation-command section.

The router should send reviewer activation phrases to that block.

## Manual Check

Before adding to the router, confirm that the route does not conflict with:

- `docs/REVIEW_STANDARD.md` for generic lightweight review;
- `blocks/logic/BLOCK.md` for logic-only reasoning review;
- domain-specific block review routes such as design, YouTube, Chrome Extension, immigration, tax, and OSINT.

## Intended Behavior

Use `blocks/reviewer/BLOCK.md` when the owner asks for a dedicated reviewer mode, expert review, hard critique, acceptance review, or cross-domain artifact review.

Use `docs/REVIEW_STANDARD.md` when the request is a small generic review and does not require the full reviewer block.