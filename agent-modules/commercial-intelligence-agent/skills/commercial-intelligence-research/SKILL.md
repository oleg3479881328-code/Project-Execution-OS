---
name: commercial-intelligence-research
description: Use when a task asks to analyze a customer, website, niche, market, competitor set, sales growth, offers, leads, SEO, funnel, or distribution using minimal input such as a single website URL.
status: candidate
version: 0.1.0
scope: commercial research and sales-growth diagnosis
---

# Commercial Intelligence Research

## Purpose

Produce a practical commercial intelligence diagnosis from minimal customer input, ideally a website URL.

The skill converts web research and market evidence into prioritized recommendations for improving leads, replies, calls, conversions, sales, or revenue.

## Use When

Use this skill when the task includes one or more of:

- customer website analysis;
- competitor research;
- market research for sales growth;
- offer improvement;
- funnel or landing-page diagnosis;
- lead or account research;
- SEO / local SEO / AI visibility recommendations;
- distribution-channel selection;
- growth plan creation.

## Do Not Use When

Do not use this skill when:

- the user only wants a short opinion without research;
- the task is pure creative copywriting;
- the requested action is automated spam or non-compliant scraping;
- the output would require private data that is not available;
- the task is high-stakes advice outside commercial growth;
- the user expects guaranteed sales results.

## Inputs Required

Minimum:

```text
customer_website
```

Optional:

```text
known_country
known_region_or_city
known_language
known_competitors
known_offer
known_target_customer
known_goal
known_budget
known_constraints
```

When optional data is missing, infer it and label the confidence.

## Workflow

### 1. Normalize Input

- Clean the URL.
- Resolve the domain.
- Identify homepage, main navigation, service/product pages, pricing pages, contact pages, blog/resources, case studies, reviews/testimonials, legal pages, and social links.

### 2. Website Extraction

Extract and structure:

- page titles and meta descriptions;
- H1/H2 headings;
- product/service names;
- offer claims;
- CTAs;
- proof elements;
- testimonials/reviews;
- pricing or quote signals;
- lead forms and booking/contact paths;
- phone, email, address, maps, service areas;
- schema.org markup when available;
- language, currency, hreflang, TLD, legal/compliance signals.

### 3. Context Inference

Infer:

- country / region / city;
- language and customer geography;
- business model;
- audience segments;
- likely purchase intent;
- main conversion action;
- primary revenue path;
- likely sales cycle.

Tag each inference:

```text
field:
value:
confidence: high | medium | low
source:
reasoning_note:
```

### 4. Competitor Discovery

Generate competitor searches from:

- inferred service/product category;
- region/city/country;
- customer language;
- commercial modifiers: price, best, near me, agency, service, provider, software, alternative, reviews, comparison;
- competitor pages and directories surfaced from search results.

Competitor classes:

- direct competitors;
- SEO competitors;
- local competitors;
- paid-search-like competitors;
- directory / marketplace competitors;
- substitute solutions.

### 5. Competitor Analysis

For each useful competitor, extract:

- positioning;
- headline / first-screen promise;
- offer structure;
- pricing signals;
- guarantees / risk reversal;
- trust proof;
- case studies;
- reviews;
- CTA path;
- lead magnet;
- content/SEO structure;
- obvious strengths;
- obvious weaknesses;
- ideas worth adapting;
- ideas not worth copying.

### 6. Customer Voice Research

Search for market language and buyer pain through:

- reviews;
- comments;
- forums;
- Reddit/Quora when relevant;
- niche communities;
- directories;
- social profiles;
- marketplace reviews;
- competitor testimonials;
- search snippets and People Also Ask-style questions.

Extract:

- pains;
- desired outcomes;
- objections;
- decision criteria;
- trust concerns;
- vocabulary;
- repeated complaints;
- emotional triggers;
- urgent purchase triggers.

### 7. Offer Diagnosis

Evaluate the customer's offer against market evidence:

- Is the target buyer clear?
- Is the result concrete?
- Is the proof strong?
- Is the risk reduced?
- Is there a reason to act now?
- Is the differentiator real?
- Does the offer match how customers describe the problem?
- Is the CTA aligned with purchase intent?

Generate:

- 5 stronger offer angles;
- 5 headline variants;
- 5 CTA variants;
- trust-proof improvements;
- guarantee or risk-reversal ideas when appropriate.

### 8. Funnel / Website Audit

Diagnose:

- first-screen clarity;
- conversion path;
- CTA visibility;
- page hierarchy;
- mobile friction;
- lead form friction;
- missing proof;
- missing pricing/range clarity;
- weak local trust;
- poor service-page structure;
- missing comparison/content pages;
- slow or technically weak pages when performance data is available.

### 9. Distribution Recommendation

Rank channels by fit, speed, effort, and likely impact.

Channel classes:

- local SEO / Google Business Profile;
- SEO service pages;
- comparison pages;
- programmatic directory pages;
- cold B2B outreach;
- partnerships;
- marketplace/directory listing optimization;
- content engine;
- short video;
- paid search;
- retargeting;
- LinkedIn / Telegram / Reddit / VC / niche communities;
- email nurture;
- referral loops.

### 10. Lead Strategy

For B2B-compatible businesses, propose:

- ideal customer profile;
- lead-source categories;
- qualification signals;
- disqualification signals;
- first-contact angle;
- CSV fields for lead list;
- compliance limits.

Do not auto-contact leads. Do not collect sensitive personal data unless explicitly permitted and lawful.

### 11. Prioritize Actions

Use a simple scoring table:

```text
impact: 1-5
effort: 1-5
speed: 1-5
confidence: 1-5
priority_score = impact + speed + confidence - effort
```

Output:

- quick wins;
- 30-day experiments;
- mid-term build tasks;
- do-not-do list;
- validation metrics.

## Output Contract

Return this structure:

```markdown
# Commercial Intelligence Report

## 1. Executive Diagnosis

## 2. Inferred Business Context
| Field | Value | Confidence | Source | Note |

## 3. Competitor Map
| Competitor | Type | Why relevant | Key strength | Weakness | Source |

## 4. Competitor Patterns Worth Adapting

## 5. Customer Voice
| Theme | Evidence | Exact language / paraphrase | Sales implication |

## 6. Offer Doctor
### Current Offer Problems
### Stronger Offer Angles
### Headline / CTA Ideas

## 7. Website / Funnel Audit
| Issue | Why it hurts sales | Fix | Priority |

## 8. Distribution Opportunities
| Channel | Fit | Why now | First test | Priority |

## 9. Lead Strategy

## 10. 30-Day Action Plan
| Week | Action | Owner | Evidence to collect |

## 11. Assumptions, Risks, Unknowns
```

## Constraints and Stop Conditions

Stop or downgrade output when:

- the website cannot be reached and no alternate source exists;
- the geography cannot be inferred with at least medium confidence;
- competitor discovery returns irrelevant results;
- the niche is regulated and recommendations require legal/compliance review;
- data sources forbid extraction or access;
- the report would rely mostly on assumptions.

Always separate:

- confirmed facts;
- assumptions;
- recommendations;
- risks.

Do not claim a tool was used unless it actually was used.
Do not claim research is complete when only a small sample was checked.
Do not promise revenue growth.

## Evidence / References

See `../../references/sources.md`.

## Validation Status

`candidate` — not yet validated on a real customer website.
