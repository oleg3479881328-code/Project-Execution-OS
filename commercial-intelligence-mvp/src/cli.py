from __future__ import annotations

import argparse
from datetime import datetime, timezone

from .analyze_competitors import analyze_competitors
from .diagnose_offer import diagnose_offer
from .discover_competitors import discover_competitors
from .extract_site import extract_website
from .infer_context import infer_context
from .models import CommercialIntelligenceReport, CustomerInput, ExecutionMetadata
from .plan_distribution import plan_distribution
from .render_report import write_outputs


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Commercial Intelligence MVP CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    audit = subparsers.add_parser("audit", help="Run a commercial intelligence audit")
    audit.add_argument("--url", required=True, help="Customer website URL")
    audit.add_argument("--out", required=True, help="Output directory")
    audit.add_argument("--country", help="Known country")
    audit.add_argument("--language", help="Known language")
    audit.add_argument("--known-competitor", action="append", default=[], help="Known competitor URL or domain")
    audit.add_argument("--goal", help="Known business goal")
    audit.add_argument("--max-competitors", type=int, default=5, help="Maximum competitor candidates")
    audit.add_argument("--no-web", action="store_true", help="Disable live competitor web search")
    return parser


def run_audit(args: argparse.Namespace) -> None:
    customer = CustomerInput(
        url=args.url,
        country=args.country,
        language=args.language,
        known_competitors=args.known_competitor,
        goal=args.goal,
        max_competitors=args.max_competitors,
        no_web=args.no_web,
    )

    execution = ExecutionMetadata(
        timestamp_utc=datetime.now(timezone.utc).isoformat(),
        web_search_enabled=False,
        sources_attempted=["customer_website_fetch"],
        sources_succeeded=[],
        sources_failed=[],
        assumptions=[],
        competitor_query_plan=[],
    )

    website = extract_website(str(customer.url))
    execution.sources_succeeded.append("customer_website_fetch")
    context = infer_context(website, known_country=customer.country, known_language=customer.language, goal=customer.goal)
    competitors = discover_competitors(customer, context, execution)
    competitor_analyses = analyze_competitors(competitors)
    offer_diagnosis, funnel_issues, customer_voice = diagnose_offer(website, context)
    distribution, recommendations, growth_actions = plan_distribution(
        context,
        has_local_signals=bool(website.addresses or website.contact_phones or website.geography_hints),
    )

    confirmed_facts = [
        fact
        for fact in [
            f"Fetched customer website successfully: {website.final_url}",
            f"Detected {len(website.cta_texts)} CTA candidates.",
            f"Detected {len(website.contact_pages)} contact-path links.",
            f"Detected {len(website.service_pages)} service/product-like links.",
        ]
        if fact
    ]

    assumptions = list(execution.assumptions)
    if not context.country:
        assumptions.append("Country could not be confirmed from the inspected website evidence alone.")
    if not competitors:
        assumptions.append("Competitor map is partial because live discovery may not have executed.")

    risks = [
        "V1 uses public-page heuristics and may miss important context behind deeper pages.",
        "Competitor discovery quality depends on geography and offer inference quality.",
        "No guarantee of market completeness or revenue impact.",
    ]

    report = CommercialIntelligenceReport(
        customer_input=customer,
        execution=execution,
        extracted_website=website,
        inferred_context=context,
        competitors_discovered=competitors,
        competitor_analyses=competitor_analyses,
        customer_voice=customer_voice,
        offer_diagnosis=offer_diagnosis,
        funnel_issues=funnel_issues,
        distribution_opportunities=distribution,
        growth_actions=growth_actions,
        confirmed_facts=confirmed_facts,
        assumptions=assumptions,
        recommendations=recommendations,
        risks=risks,
    )
    write_outputs(report, args.out)


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "audit":
        run_audit(args)


if __name__ == "__main__":
    main()
