# Shared Web Core v0.1 — Contract Canary

Status: `CANDIDATE / OWNER-APPROVED EARLY EXTRACTION`

This is the first client-neutral code layer for the Olga/Tusia platform family.

It is intentionally **not** a full shared UI library and **not** a copy of either client project. It contains only small contracts already supported by reviewed family knowledge.

## Included

- stable entity identity independent of public slug/URL;
- published document envelope and projection contract;
- explicit publication/indexing state;
- publish adapter interface and public-version verification result;
- CMS/fallback presentation parity acceptance contract.

## Excluded

- brand CSS, fonts, logos, crops, header/footer markup;
- client content and entity records;
- domains and routing particulars;
- repository names, branches, actor strings, environment variable names;
- Puck block labels or client-specific editor UI.

## Canary

`canaries/tusia-runtime-canary.json` is a durable representation of what can be independently observed from the current Tusia Vercel runtime. It is **not** represented as original source code.

The canary proves only the capabilities visible from runtime evidence. Unknown internals stay unknown.

## Promotion gate

v0.1 may become `PROVEN` only after:

1. fresh independent review of these contracts against Olga implementation evidence and Tusia runtime evidence;
2. a real client integration canary (prefer Tusia when durable source becomes available);
3. build/runtime regression PASS;
4. capability matrix and registry update.

Until then projects may consume these contracts as design targets, but production dependency migration is not automatic.
