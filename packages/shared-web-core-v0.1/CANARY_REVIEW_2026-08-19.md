# Shared Web Core v0.1 — first client integration canary review

Date: 2026-08-19
Client: Olga Polo Weddings
Status: PASS WITH SCOPE LIMITATION

## Fresh production evidence used

- `olga-polo-weddings-web/data/cms-entities.ts` on `main`: stable venue IDs `ven_001...ven_016`, kind + slug separated from public path.
- `olga-polo-weddings-web/lib/published-cms.ts` on `main`: published CMS JSON is authoritative; missing file may fall back; existing invalid document fails loudly.
- `olga-polo-weddings-web/data/editor-templates/venue/peterloon-estate.json` on `main`: real production document stores `kind`, `slug`, `updatedAt`, `source`, `data`; it does **not** require `entityId` or `publishId` inside the JSON document.

## Canary finding that changed Shared Core

The initial Shared Core contract incorrectly required `entityId` and `publishId` inside every `PublishedDocument`. That would have forced an unnecessary Olga storage migration and mixed two concerns:

- stable identity can live in the entity registry;
- publish/version verification can live in a separate publish receipt.

The contract was corrected:

- `PublishedDocument.entityId` is optional;
- `PublishedDocument.publishId` is optional;
- `kind + slug + content` are required;
- resolver validates requested entity against document `kind + slug` and optional `entityId` when present;
- exact public-version verification remains tied to `PublishReceipt.publishId`.

## Executed canary

`canaries/olga-main-canary.ts` mirrors the current Olga production storage boundary and exercises:

1. stable entity registry identity;
2. published document without embedded entityId/publishId;
3. published projection selection;
4. legitimate fallback only when published document is absent;
5. fail-loud behavior on slug mismatch;
6. publishId/live-version verification contract;
7. published/fallback responsive parity contract.

Local independent execution with TypeScript 5.8.3:

```text
tsc --module commonjs --target es2022 --strict ...
node out/canaries/olga-main-canary.js
OLGA_SHARED_CORE_CANARY_PASS
```

## Reviewer verdict

PASS for the first real-client contract canary.

The canary found and corrected a real abstraction error before production adoption, which is exactly the purpose of the canary stage.

## Scope limitation

This does **not** yet make Shared Web Core v0.1 `PROVEN` for automatic cross-project runtime consumption. Tusia's original durable source repository is still not located, so Tusia storage/publish internals remain unknown. The shared package stays `CANDIDATE` until a second client implementation or equivalent durable code source passes the same contract boundary.

No Olga production code or deployment was modified by this canary.
