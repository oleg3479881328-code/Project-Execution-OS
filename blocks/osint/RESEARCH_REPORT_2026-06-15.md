# OSINT Research Report — 2026-06-15

## Purpose

This report records the first donor pass for the `OSINT Block`.

The goal is to create a reusable Project Execution OS block for aggressive lawful open-source intelligence: investigative research, due diligence, source verification, evidence handling, timeline reconstruction and risk review.

## Why This Block Exists

General research is not enough for OSINT-style work.

OSINT tasks require:

- a decision-oriented intelligence question;
- strict source handling;
- evidence labels;
- fact/inference/hypothesis separation;
- contradiction hunting;
- risk review;
- lawful collection boundaries;
- reproducible handoff.

Without a dedicated block, OSINT tasks degrade into ad hoc search, weak source lists, unsupported conclusions, or unsafe overreach.

## Donor Categories

### 1. Intelligence-cycle methodology

Donor principle: start with the decision and intelligence question, not with search.

Reusable pattern:

```text
Decision -> Intelligence Question -> Source Map -> Collection -> Verification -> Analysis -> Risk -> Next Action
```

### 2. Investigative journalism and public-source verification

Donor principle: strong investigations show their work.

Reusable patterns:

- source-first reasoning;
- independent confirmation;
- contradiction handling;
- timeline reconstruction;
- evidence logs;
- clear separation of what is known, likely, weak or unknown.

### 3. Open-source investigation evidence handling

Donor principle: public evidence must be preserved and labeled.

Reusable patterns:

- source URL;
- access date;
- source type;
- claim supported;
- reliability notes;
- screenshots or archived copies when appropriate;
- uncertainty labels.

### 4. OSINT tool ecosystems

Donor principle: tools are subordinate to workflow.

Relevant tool categories:

- link analysis and entity graphs;
- domain, DNS, RDAP and certificate transparency;
- public code repositories;
- web archives;
- business registries;
- court and government databases;
- public cybersecurity exposure search;
- metadata extraction;
- social/public profile review;
- news and reputation search.

Tools must not define the investigation. They only help answer the intelligence question.

## Core Block Decision

The block should be positioned as:

```text
Aggressive Legal Open-Source Intelligence
```

Not soft research, not illegal surveillance.

Operating phrase:

```text
Relentless, but lawful.
Ruthless on evidence, not on people.
```

Russian phrase:

```text
Беспощадно к фактам, но не к людям.
```

## Safety Boundary Decision

The owner asked for a hard OSINT block. The correct interpretation is aggressive lawful public-source investigation, not illegal or abusive collection.

Explicitly excluded:

- hacking;
- phishing;
- social engineering;
- credential theft;
- malware;
- buying or using stolen/leaked private databases;
- doxxing private individuals;
- stalking;
- intimidation or blackmail;
- unlawful deanonymization;
- collecting private personal details for pressure.

This boundary is part of block quality, not a weakness. It keeps the block usable for business, legal, secretary, agent and project workflows.

## Initial Use Cases

- Vendor due diligence
- Contractor review
- Company credibility check
- Domain/site investigation
- Scam/fraud risk review
- AI tool credibility review
- Public reputation review
- Timeline reconstruction
- Evidence list for attorney/CPA/operator handoff
- Public cyber exposure triage
- Source reliability review

## Initial Files

Created as first block foundation:

- `BLOCK.md`
- `RESEARCH_REPORT_2026-06-15.md`
- `VALIDATION_BACKLOG.md`

Future optional files:

- `REFERENCES.md`
- `PATTERNS.md`
- `REVIEW.md`
- `TOOL_SELECTION_MATRIX.md`
- `SECURITY_AND_COMPLIANCE.md`

## Open Questions

- Should this block include a standard evidence-log table format?
- Should tool matrices be separated by use case: company, domain, person-public-profile, cyber exposure, reputation, legal handoff?
- Should OSINT task outputs be stored in project folders, Notion, or only active chat depending on sensitivity?
- What is the default retention policy for sensitive investigation notes?
- How should screenshots and archived evidence be stored without leaking private or sensitive material into GitHub?

## Recommendation

Use `BLOCK.md` immediately for real OSINT tasks, but treat it as v0.

Validate through 3–5 real investigations before adding a large tool matrix or pattern library.
