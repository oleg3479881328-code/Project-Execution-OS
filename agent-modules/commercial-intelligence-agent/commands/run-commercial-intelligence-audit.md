---
description: Run a commercial intelligence audit from a customer website or short customer description.
argument-hint: "<customer website URL> [optional: country, niche, competitors, goal]"
status: candidate
version: 0.1.0
---

# /run-commercial-intelligence-audit

## Purpose

Run a minimal-input commercial intelligence audit for a customer or prospect.

Primary goal:

```text
Find what can most plausibly improve the customer's leads, replies, calls, conversions, sales, or revenue.
```

## Usage

Preferred input:

```text
/run-commercial-intelligence-audit https://example.com
```

Optional richer input:

```text
/run-commercial-intelligence-audit https://example.com country=US goal="more local service leads" known_competitors="competitor1.com, competitor2.com"
```

## Preconditions

At least one of the following must be available:

- customer website URL;
- customer name + market + country;
- short business description + market + country.

If only a website is provided, the workflow must infer everything possible and label confidence.

## Workflow

1. **Normalize input**
   - Validate URL.
   - Resolve homepage.
   - Record missing optional data.

2. **Extract customer website**
   - Crawl/scrape key pages.
   - Extract offer, services/products, CTAs, proof, contact details, language, geography, and funnel path.

3. **Infer business context**
   - Infer company identity, country, city/region, business model, target audience, offer type, and main conversion path.
   - Mark confidence for every inferred field.

4. **Generate search plan**
   - Create competitor discovery queries.
   - Create customer-voice queries.
   - Create distribution-channel queries.
   - Create SEO/content opportunity queries.

5. **Discover competitors**
   - Collect direct competitors.
   - Collect SEO competitors.
   - Collect directory/marketplace competitors.
   - Collect substitute solutions.

6. **Analyze competitors**
   - Extract positioning, offers, promises, pricing signals, proof, guarantees, funnel, and content patterns.
   - Identify what to adapt and what not to copy.

7. **Research customer voice**
   - Extract pains, objections, vocabulary, desired outcomes, buying triggers, and complaints.

8. **Diagnose offer and funnel**
   - Identify weak message, weak proof, weak CTA, weak service pages, missing comparison pages, and conversion blockers.

9. **Recommend distribution**
   - Rank channels by fit, speed, effort, and likely impact.
   - Prioritize channels that match the inferred business model.

10. **Create action plan**
    - Quick wins.
    - 30-day experiments.
    - Mid-term build tasks.
    - Do-not-do list.
    - Validation metrics.

## Output Contract

Return:

```markdown
# Commercial Intelligence Report — <customer/domain>

## Input Received

## Inference Summary

## Executive Diagnosis

## Competitor Map

## Competitor Patterns

## Customer Voice

## Offer Doctor

## Website / Funnel Audit

## Distribution Opportunities

## Lead Strategy

## 30-Day Action Plan

## Assumptions / Unknowns / Risks

## Suggested Next Test
```

## Stop Conditions

Stop and return a partial report when:

- the website is unreachable;
- the site contains too little public information;
- the inferred geography remains low confidence after search;
- no relevant competitors can be found;
- sources require login or private access;
- data collection would cross compliance or ethical boundaries.

## Related Skills

- `commercial-intelligence-research`

## Validation Status

`candidate` — this command must be validated on a real customer website before promotion.
