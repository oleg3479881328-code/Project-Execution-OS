# Decision 007 — MVP-First Cache Strategy

## Date

`2026-05-29`

## Decision

For the MVP, optimize cache usage through stable context ordering only.

Use:

```text
stable reusable prefix
→ START_HERE.md stable door
→ docs/ROUTER.md live internal map
→ only required routed standards
→ project-specific context when needed
→ current instruction / error / live input last
```

## Reason

DeepSeek already exposes cache-hit, cache-miss, token and expense information in its own account dashboard.

The immediate value comes from preserving stable prefix ordering, not from building duplicate analytics infrastructure.

## Keep And Use Now

- stable `START_HERE.md` door;
- live `docs/ROUTER.md` internal map;
- `docs/CONTEXT_ASSEMBLY_STANDARD.md`;
- stable-prefix-first ordering;
- dynamic input last.

## Defer Unless A Real Need Appears

- custom dashboard;
- automatic cache-hit/cache-miss ingestion;
- automatic cost reports;
- automatic fingerprint regeneration;
- heavy runtime logging;
- provider-specific analytics adapters.

## Existing Optional Artifacts

Keep these committed artifacts as optional future infrastructure, but do not treat them as MVP requirements:

```text
docs/SYSTEM_CONTEXT_VERSION_STANDARD.md
SYSTEM_CONTEXT_MANIFEST.md
docs/API_RUNTIME_COST_CACHE_LOGGING_STANDARD.md
```

## Status

`accepted — recorded MVP direction; no new runtime implementation required now`

## Next Rule

Do not build additional cache analytics infrastructure unless a real operational need appears.