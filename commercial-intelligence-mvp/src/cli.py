from __future__ import annotations

import argparse
from datetime import datetime, timezone

from .analyze_competitors import analyze_competitors
from .diagnose_offer import diagnose_offer
from .discover_competitors import discover_competitors
from .extract_site import extract_website
from .infer_context import infer_context
from .models import (
    CommercialIntelligenceReport,
    ConfidenceLevel,
    CustomerInput,
    ExecutionMetadata,
    ExtractedWebsite,
    InferredValue,
    SeedType,
    SourceType,
)
from .plan_distribution import plan_distribution
from .resolve_seed import resolve_seed
from .render_report import write_outputs


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Commercial Intelligence MVP CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    audit = subparsers.add_parser("audit", help="Run a commercial intelligence audit")
    audit.add_argument("--seed", help="Customer seed such as website, company name, phone, email, address, or short description")
    audit.add_argument("--url", help="Backward-compatible alias for website URL seed")
    audit.add_argument(
        "--seed-type",
        choices=[seed_type.value for seed_type in SeedType],
        help="Optional explicit seed type",
    )
    audit.add_argument("--out", required=True, help="Output directory")
    audit.add_argument("--country", help="Known country")
    audit.add_argument("--language", help="Known language")
    audit.add_argument("--known-competitor", action="append", default=[], help="Known competitor URL or domain")
    audit.add_argument("--goal", help="Known business goal")
    audit.add_argument("--max-competitors", type=int, default=5, help="Maximum competitor candidates")
    audit.add_argument("--no-web", action="store_true", help="Disable live competitor web search")
    return parser


def _empty_website(seed: str) -> ExtractedWebsite:
    return ExtractedWebsite(
        requested_url=seed,
        final_url=seed,
        fetch_status="not_executed",
    )


def _fallback_context_from_seed(customer: CustomerInput, resolved_entity) -> InferredValue:
    candidate = (
        resolved_entity.entity_name.value
        if resolved_entity.entity_name
        else resolved_entity.seed.normalized_value
    )
    return InferredValue(
        field="main_offer",
        value=candidate,
        confidence=ConfidenceLevel.LOW,
        source=SourceType.ASSUMPTION,
        reasoning_note="Seed-only fallback because no website evidence was collected.",
        evidence=resolved_entity.seed.evidence,
    )


def run_audit(args: argparse.Namespace) -> None:
    seed_value = args.seed or args.url
    if not seed_value:
        raise SystemExit("Either --seed or --url must be provided.")

    explicit_seed_type = SeedType(args.seed_type) if args.seed_type else None
    if args.url and not args.seed and not explicit_seed_type:
        explicit_seed_type = SeedType.WEBSITE_URL

    customer = CustomerInput(
        seed=seed_value,
        seed_type=explicit_seed_type,
        url_alias=args.url,
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
        sources_attempted=["seed_resolution"],
        sources_succeeded=[],
        sources_failed=[],
        assumptions=[],
        competitor_query_plan=[],
    )

    resolved_entity = resolve_seed(customer.seed, customer.seed_type)
    execution.sources_succeeded.append("seed_resolution")

    website = _empty_website(customer.seed)
    website_url = resolved_entity.website_url.value if resolved_entity.website_url else None
    if website_url:
        execution.sources_attempted.append("customer_website_fetch")
        try:
            website = extract_website(website_url)
        except Exception as exc:
            execution.sources_failed.append(f"customer_website_fetch:{exc}")
            execution.assumptions.append("Website extraction was not available from the provided or inferred seed.")
        else:
            execution.sources_succeeded.append("customer_website_fetch")
    else:
        execution.assumptions.append("No website was provided or inferred from the seed, so website extraction was skipped.")

    context = infer_context(
        resolved_entity,
        website,
        known_country=customer.country,
        known_language=customer.language,
        goal=customer.goal,
    )
    if not context.main_offer:
        context.main_offer = _fallback_context_from_seed(customer, resolved_entity)

    competitors = discover_competitors(customer, resolved_entity, context, execution)
    competitor_analyses = analyze_competitors(competitors)
    offer_diagnosis, funnel_issues, customer_voice = diagnose_offer(website, context)
    distribution, recommendations, growth_actions = plan_distribution(
        context,
        has_local_signals=bool(website.addresses or website.contact_phones or website.geography_hints),
    )

    confirmed_facts = [f"Resolved seed type: {resolved_entity.seed.seed_type.value}"]
    if website.fetch_status != "not_executed":
        confirmed_facts.extend(
            [
                f"Fetched customer website successfully: {website.final_url}",
                f"Detected {len(website.cta_texts)} CTA candidates.",
                f"Detected {len(website.contact_pages)} contact-path links.",
                f"Detected {len(website.service_pages)} service/product-like links.",
            ]
        )
    if resolved_entity.website_url and website.fetch_status == "not_executed":
        confirmed_facts.append(f"Identified likely website from seed: {resolved_entity.website_url.value}")
    if resolved_entity.email_domain:
        confirmed_facts.append(f"Extracted email domain from seed: {resolved_entity.email_domain.value}")
    if resolved_entity.phone_hint:
        confirmed_facts.append(f"Captured phone seed: {resolved_entity.phone_hint.value}")

    assumptions = list(execution.assumptions)
    if not context.country:
        assumptions.append("Country could not be confirmed from the available seed and public evidence alone.")
    if not competitors:
        assumptions.append("Competitor map is partial because live discovery may not have executed.")
    if website.fetch_status == "not_executed":
        assumptions.append("Website and funnel findings are partial because no website was fetched in this run.")

    risks = [
        "V1 uses public evidence heuristics and may miss important context behind deeper pages or unlinked profiles.",
        "Competitor discovery quality depends on seed resolution, geography inference, and offer inference quality.",
        "No guarantee of market completeness or revenue impact.",
    ]

    report = CommercialIntelligenceReport(
        customer_input=customer,
        seed_resolution=resolved_entity,
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
