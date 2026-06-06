# US Law Block

## Purpose

This block gives `Project Execution OS` a reusable workflow for researching and organizing legal issues under United States law.

It helps an agent identify the correct jurisdiction, find current primary sources, separate binding authority from persuasive or informational material, preserve evidence, identify deadlines and risks, prepare a research memo, and escalate matters that require a licensed attorney.

## Status

`candidate`

## When To Use

Use this block when the task involves:

- United States federal law;
- state, territory, county, city, or municipal law;
- statutes, regulations, court rules, cases, agency guidance, or administrative decisions;
- legal research;
- document review for a legal issue;
- issue spotting;
- legal-risk analysis;
- deadline and procedure checks;
- preparation for a lawyer consultation;
- comparison of legal-research tools;
- legal-source monitoring or automation.

## When Not To Use

Do not use this block as a substitute for:

- representation by a licensed attorney;
- legal advice requiring attorney-client duties;
- emergency response;
- filing a court document without jurisdiction-specific review;
- interpreting a document without reading its full text and current context;
- relying on stale law, summaries, search snippets, or AI output without source verification.

## Core Rule

Do not answer a legal question from memory alone.

A valid US-law workflow should connect:

`facts -> dates -> jurisdiction -> issue classification -> deadline check -> source hierarchy -> primary-source verification -> case-law treatment -> agency or court procedure -> risk analysis -> options -> attorney-escalation decision -> evidence package`

## Required Reading Inside This Block

Open only the smallest relevant path:

1. `blocks/us-law/LEGAL_RESEARCH_PIPELINE.md`
2. `blocks/us-law/SOURCE_HIERARCHY.md` when selecting sources or validating authority
3. `blocks/us-law/JURISDICTION_AND_DEADLINE_CHECKLIST.md` before substantive analysis
4. `blocks/us-law/LEGAL_AGENT_STANDARD.md` when preparing an answer, memo, or agent workflow
5. `blocks/us-law/ESCALATION_RULES.md` when the issue may carry material risk
6. `blocks/us-law/TOOLS_AND_PLATFORMS.md` when choosing research tools, APIs, or paid databases
7. `blocks/us-law/REFERENCES.md` for the source map
8. `blocks/us-law/RESEARCH_REPORT_2026-06-06.md` for the current research snapshot

## Typical Modes

This block may route work into:

- federal statutory research;
- federal regulatory research;
- state-law research;
- local-law research;
- case-law research;
- litigation-procedure research;
- agency-procedure research;
- legal document triage;
- contract issue spotting;
- immigration, tax, employment, consumer, business, housing, family, criminal, or administrative-law research;
- attorney-consultation preparation;
- legal-source monitoring;
- legal-research automation.

## Typical Outputs

Typical outputs:

- legal issue map;
- facts and dates matrix;
- jurisdiction matrix;
- deadline and urgency note;
- primary-source list;
- authority table;
- research memo;
- options and risks summary;
- unresolved questions;
- document checklist;
- attorney handoff packet;
- recommendation to create a narrower domain skill when a repeated workflow becomes clear.

## Boundary

This block is a reusable research and triage layer.

Keep case-specific personal data, confidential documents, attorney communications, final filings, and litigation strategy in the approved secure project layer.

## Final Rule

Use primary sources, verify currency, state uncertainty, and escalate when the stakes require a licensed attorney.