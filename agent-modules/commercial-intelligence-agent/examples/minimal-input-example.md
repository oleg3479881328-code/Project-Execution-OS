# Minimal Input Example

## Input

```text
customer_website: https://example.com
```

No other customer information is provided.

## Expected Behavior

The module should not ask a long questionnaire first.

It should infer what it can, label uncertainty, then proceed with the smallest useful research run.

## Inference Fields

```text
company_name: inferred from website title/logo/schema/contact page
country: inferred from address/phone/TLD/language/currency/legal pages/search results
city_or_region: inferred from contact page/service area/map links/search snippets
language: inferred from page text/hreflang
business_model: inferred from product/service pages and conversion path
target_customer: inferred from messaging, use cases, testimonials, pricing, audience words
main_offer: inferred from homepage and service/product pages
conversion_goal: inferred from CTA/form/phone/booking/checkout
known_competitors: discovered through search, directories, and market queries
```

## Expected Report Sections

```markdown
# Commercial Intelligence Report — example.com

## 1. Executive Diagnosis
The clearest likely sales blocker is ...

## 2. Inferred Business Context
| Field | Value | Confidence | Source | Note |

## 3. Competitor Map
| Competitor | Type | Why relevant | Key strength | Weakness | Source |

## 4. Competitor Patterns Worth Adapting

## 5. Customer Voice

## 6. Offer Doctor

## 7. Website / Funnel Audit

## 8. Distribution Opportunities

## 9. Lead Strategy

## 10. 30-Day Action Plan

## 11. Assumptions, Risks, Unknowns
```

## Good Output

A good output is specific and action-ready:

```text
Your homepage says what you do, but not why this buyer should choose you now.
Top competitors promise fixed timelines, visible proof, and a low-friction quote path.
Your first 30-day test should be: rebuild the first screen offer, create 3 service pages, add proof blocks, and test a direct outreach list of 50 qualified accounts.
```

## Bad Output

A bad output is generic:

```text
Improve SEO, post more content, use social media, and optimize your website.
```

## Validation Notes Template

After a real run, record:

```text
run_date:
website:
what_was_inferred_correctly:
what_was_inferred_wrong:
best_sources:
worst_sources:
most_useful_report_section:
least_useful_report_section:
next_module_change:
status_after_run: candidate | tested
```
