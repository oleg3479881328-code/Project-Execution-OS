# Commercial Intelligence Agent

## Purpose

This candidate module helps an AI operator turn **minimal customer input** — ideally only a company website — into a practical commercial intelligence report focused on sales growth.

The module is not a magic sales button. It is a structured research and diagnosis workflow for finding:

- what the customer sells;
- where the customer likely operates;
- who the real competitors are;
- what the market and audience care about;
- where the customer's offer, website, funnel, visibility, and distribution are weak;
- which actions should be tested first to increase leads, replies, calls, sales, or revenue.

## When To Use

Use this module when the owner asks for an agent or workflow that can analyze a business, customer, client, website, market, competitor set, sales channel, offer, lead list, or growth opportunity.

Typical trigger phrases:

- "дам сайт заказчика, пусть агент сам поймёт нишу и страну";
- "исследуй конкурентов и продажи";
- "найди, как увеличить продажи";
- "сделай коммерческую разведку";
- "найди офферы, лиды, каналы, SEO, слабые места";
- "подготовь growth report".

## When Not To Use

Do not use this module for:

- legal, medical, financial, immigration, or other high-stakes advice without a domain-specific standard;
- pure copywriting when no market or competitor research is needed;
- automated spam, credential harvesting, or scraping private/non-consensual personal data;
- claims that sales will increase with certainty;
- autonomous contacting of leads without explicit owner approval and compliance review;
- stealth scraping or anti-bot bypass that violates target-site terms or applicable law.

## Core Product Shape

Working name: **AI Growth Scout**.

One-line product definition:

> Given a customer website, infer the business context, research the market and competitors, diagnose commercial weak points, and produce a prioritized sales-growth action plan.

Primary input:

```text
customer_website: required
```

Optional inputs:

```text
known_country
known_city_or_region
known_language
known_competitors
known_offer
known_target_customer
known_goal
budget_or_channel_constraints
```

The workflow must operate without optional fields when possible. Missing fields are inferred and labeled as assumptions.

## Minimal-Input Inference Contract

From a website alone, the module should attempt to infer:

1. Company identity: name, domain, brand names, products, services.
2. Geography: country, city, service area, phone prefix, address, currency, TLD, language, hreflang, schema.org markup, legal pages, map links.
3. Business model: B2B, B2C, local service, SaaS, ecommerce, agency, marketplace, consulting, creator/business media, etc.
4. Target customer: buyer roles, segments, pains, intent level.
5. Offer type: productized service, custom service, subscription, one-time project, local appointment, quote-based sale.
6. Funnel type: direct contact, booking, checkout, lead form, phone call, email, free audit, demo, consultation.
7. Current visibility: SEO pages, blog, Google Business Profile hints, social profiles, marketplaces, directories, content channels.
8. Competitor discovery query set: generated from inferred category, location, service phrases, audience language, and commercial modifiers.

Every inferred field must be tagged:

```text
confidence: high | medium | low
source: website | search | competitor | directory | assumption
```

## Workflow Overview

```text
1. Intake
   Input only the customer website when possible.

2. Website Understanding
   Crawl/scrape the site, extract pages, offers, metadata, schema, services, contact details, social links, and funnel elements.

3. Context Inference
   Infer country, market, business model, language, likely buyer, current offer, and goal hypotheses.

4. Competitor Discovery
   Search for direct, local, SEO, ad-like, directory, marketplace, and substitute competitors.

5. Competitor Analysis
   Analyze positioning, pricing signals, messaging, guarantees, trust proof, landing pages, content, lead magnets, reviews, and conversion path.

6. Customer Voice Research
   Extract customer language, pains, objections, triggers, comparisons, review patterns, and buying criteria.

7. Offer Diagnosis
   Compare the customer's offer against market language and competitor promises. Generate stronger offer angles.

8. Funnel / Website Audit
   Diagnose conversion blockers: unclear first screen, weak CTA, missing proof, friction, poor mobile flow, slow pages, weak service pages, bad forms.

9. Distribution Map
   Recommend channels based on business model and geography: SEO, local SEO, Google Business Profile, cold B2B outreach, directories, partnerships, communities, content, paid search, retargeting, marketplaces.

10. Lead / Account Research
   For B2B and local-service-compatible use cases, propose legally usable lead sources and lead qualification criteria. Do not auto-contact.

11. Prioritized Growth Plan
   Output quick wins, 30-day tests, mid-term build items, do-not-do list, and validation metrics.
```

## Output Contract

The final report should be concise enough for a business owner but structured enough for execution.

Required sections:

1. **Executive Diagnosis** — what likely blocks growth now.
2. **Inferred Business Context** — company, geography, market, audience, business model, confidence levels.
3. **Competitor Map** — direct competitors, SEO competitors, substitute competitors, directories/marketplaces.
4. **Competitor Patterns** — offers, promises, pricing signals, trust proof, funnel patterns.
5. **Customer Voice** — pains, objections, desired outcomes, exact market language.
6. **Offer Doctor** — weak points in the current offer and stronger offer variants.
7. **Website / Funnel Audit** — conversion issues and fixes.
8. **Distribution Opportunities** — channels ranked by fit, effort, speed, and likely impact.
9. **Lead Strategy** — who to target first and why; no automated outreach unless separately approved.
10. **30-Day Action Plan** — prioritized actions with expected evidence to collect.
11. **Risks / Assumptions / Unknowns** — what needs verification.

## Available Skills

- `skills/commercial-intelligence-research/SKILL.md` — commercial research, competitor analysis, market diagnosis, offer/funnel/channel recommendations.

## Available Commands

- `commands/run-commercial-intelligence-audit.md` — run the explicit audit workflow from a website or short customer description.

## Connector Requirements

Declared in `connectors.json`.

Important: connectors are capability declarations only. This module must never assume API keys, private data access, browser execution, or write permissions are available until verified at runtime.

## Evidence / Source Pattern

This module adapts patterns from:

- Project Execution OS reuse-first and research standards;
- WAT-style separation: workflows, agents, deterministic tools;
- Firecrawl / Tavily / Apify-style web data acquisition;
- LangGraph / CrewAI-style agent orchestration;
- public donor repos for competitor reports, lead enrichment, contractor sales intelligence, and SEO audit flows.

See `references/sources.md`.

## Status

`candidate`.

This module is drafted but not yet validated on a real customer website.

## Validation Record

No validation run has been completed yet.

First validation target:

```text
Input: one customer website only.
Expected result: first usable commercial intelligence report with explicit assumptions, competitor map, offer diagnosis, channel plan, and 30-day actions.
```
