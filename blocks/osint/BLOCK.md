# OSINT Block — Aggressive Legal Open-Source Intelligence

## Purpose

This block routes and governs aggressive lawful open-source intelligence work inside `Project Execution OS`.

The block exists to support hard investigative research, due diligence, fraud-risk review, public-source verification, source reliability analysis, timeline reconstruction, and evidence-backed decision memos.

Core principle:

> Relentless, but lawful.
>
> Ruthless on evidence, not on people.

Russian operating phrase:

> Беспощадно к фактам, но не к людям.

## Scope

Use this block for:

- OSINT;
- open-source intelligence;
- public-source investigation;
- investigative research;
- company, vendor, contractor, service, website or domain due diligence;
- scam, fraud, credibility or reputation risk review;
- source verification;
- evidence log construction;
- contradiction hunting;
- timeline reconstruction;
- public cyber exposure review when limited to lawful open sources;
- preparation of attorney, CPA, operator, executor or owner handoff briefs.

## Hard Boundary

This block is not a license to act without limits.

Allowed posture: aggressive lawful investigation using public, authorized, or otherwise legally accessible sources.

Disallowed:

- hacking;
- phishing;
- credential theft;
- buying or using stolen/leaked private databases;
- malware;
- evading access controls;
- unauthorized account access;
- doxxing private individuals;
- stalking or surveillance of private persons;
- collecting home addresses, family details or private contact details for pressure or exposure;
- social engineering;
- blackmail, intimidation or coercion;
- instructions that help harm, harass, exploit, or illegally deanonymize a person.

If a request crosses this boundary, narrow it to lawful public-source verification, safety, defensive analysis, reporting, or professional handoff.

## Default Intelligence Question

OSINT does not begin with search.

It begins with the decision that the owner needs to make.

Default first question:

> What decision must this investigation support?

Examples:

- Can we safely pay this vendor?
- Is this AI tool credible enough to test?
- Is this domain connected to a legitimate company?
- Are there public red flags around this contractor?
- What is the evidence-backed timeline?
- What sources should be handed to an attorney or CPA?

## Core Workflow

1. Define the intelligence question.
2. Define the subject and scope.
3. Define safety and privacy boundaries.
4. Build a source map.
5. Collect public evidence.
6. Preserve links, access dates and source context.
7. Classify evidence strength.
8. Cross-check independent sources.
9. Hunt contradictions and missing pieces.
10. Separate fact, inference and hypothesis.
11. Produce risk rating.
12. Recommend next action.

## Source Map Categories

Use only categories relevant to the task.

- Official websites and about pages
- Corporate registries
- Court and government records
- Sanctions, enforcement and regulatory records
- Domain registration, RDAP, DNS and certificate transparency
- Web archives and historical pages
- GitHub and public code repositories
- App stores, browser extension stores and marketplaces
- Social media and public profiles
- Reviews and reputation platforms
- News and trade publications
- Academic or technical publications
- Public procurement and grants
- Job posts and hiring pages
- Maps, address records and business listings
- Public cybersecurity exposure search engines when used lawfully
- Public financial, token, blockchain or payment traces when relevant and lawful

## Evidence Labels

Every material finding should be labeled.

- `CONFIRMED` — directly supported by strong source evidence or multiple independent sources.
- `LIKELY` — supported by credible evidence but not fully proven.
- `WEAK` — plausible but thinly supported.
- `UNVERIFIED` — found but not confirmed.
- `CONTRADICTED` — sources conflict materially.
- `RED_FLAG` — risk signal requiring attention.
- `CLEARED` — checked and no material concern found within current scope.

## Fact / Inference / Hypothesis Rule

Never merge facts, inferences and hypotheses.

- Fact: what a source directly shows.
- Inference: what reasonably follows from one or more facts.
- Hypothesis: a possible explanation that needs more evidence.

## Output Formats

Choose the smallest useful output.

- Quick triage
- Source list
- Evidence log
- Red-flag memo
- Full dossier
- Timeline
- Domain or website risk review
- Vendor due-diligence memo
- Scam/fraud risk memo
- Attorney/CPA handoff brief
- Executor handoff brief

## Minimum Output Template

```text
OSINT RESULT

Subject:
Decision supported:
Scope:
Boundary notes:

Bottom line:
Risk rating: LOW / MEDIUM / HIGH / UNKNOWN

Confirmed facts:
- ...

Red flags:
- ...

Contradictions / gaps:
- ...

Sources checked:
- ...

Next action:
- ...
```

## Review Standard

A useful OSINT output must be:

- source-backed;
- dated;
- reproducible enough for another agent or person to verify;
- clear about uncertainty;
- explicit about assumptions;
- separated from speculation;
- limited to lawful and relevant collection.

## Relationship To Other Blocks

- General research tasks may route to `docs/RESEARCH_STANDARD.md` unless the request includes investigative verification, public-source intelligence, due diligence, evidence logs, scam review, or source reliability work.
- Legal interpretation routes to legal blocks. OSINT may prepare public-source evidence for legal handoff but does not give legal advice.
- Cybersecurity implementation or offensive tactics do not belong here unless limited to lawful public exposure review and defensive decision support.

## Read Next

1. `RESEARCH_REPORT_2026-06-15.md`
2. `VALIDATION_BACKLOG.md`
