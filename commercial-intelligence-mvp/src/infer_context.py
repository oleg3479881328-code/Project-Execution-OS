from __future__ import annotations

import re
from urllib.parse import urlparse

from .models import (
    ConfidenceLevel,
    EvidenceItem,
    ExtractedWebsite,
    InferredContext,
    InferredValue,
    ResolvedEntity,
    SeedType,
    SourceType,
)

COUNTRY_BY_SUFFIX = {
    "uk": "United Kingdom",
    "ca": "Canada",
    "au": "Australia",
    "de": "Germany",
    "fr": "France",
    "it": "Italy",
    "es": "Spain",
    "us": "United States",
}


def _company_name(website: ExtractedWebsite) -> InferredValue | None:
    candidates = []
    if website.title:
        candidates.append(re.split(r"[|\-–:]", website.title)[0].strip())
    if website.headings:
        candidates.append(website.headings[0].strip())
    for record in website.json_ld:
        if record.get("name"):
            candidates.append(str(record["name"]).strip())
    parsed = urlparse(website.final_url)
    domain_guess = parsed.netloc.replace("www.", "").split(".")[0].replace("-", " ").title()
    candidates.append(domain_guess)
    best = next((item for item in candidates if item and len(item) > 2), None)
    if not best:
        return None
    return InferredValue(
        field="company_name",
        value=best,
        confidence=ConfidenceLevel.MEDIUM if best == domain_guess else ConfidenceLevel.HIGH,
        source=SourceType.WEBSITE,
        reasoning_note="Derived from page title, heading, schema name, or domain stem.",
        evidence=[EvidenceItem(source=SourceType.WEBSITE, detail=f"Candidate name: {best}", url=website.final_url)],
    )


def _country(website: ExtractedWebsite, known_country: str | None) -> InferredValue | None:
    if known_country:
        return InferredValue(
            field="country",
            value=known_country,
            confidence=ConfidenceLevel.HIGH,
            source=SourceType.USER_INPUT,
            reasoning_note="Provided directly by input.",
            evidence=[EvidenceItem(source=SourceType.USER_INPUT, detail=f"Known country: {known_country}")],
        )
    parsed = urlparse(website.final_url)
    suffix = parsed.netloc.split(".")[-1].lower()
    if suffix in COUNTRY_BY_SUFFIX:
        country = COUNTRY_BY_SUFFIX[suffix]
        return InferredValue(
            field="country",
            value=country,
            confidence=ConfidenceLevel.MEDIUM,
            source=SourceType.WEBSITE,
            reasoning_note="Inferred from domain suffix.",
            evidence=[EvidenceItem(source=SourceType.WEBSITE, detail=f"Domain suffix: .{suffix}", url=website.final_url)],
        )
    hints = [hint for hint in website.geography_hints if len(hint) > 2]
    if hints:
        return InferredValue(
            field="country",
            value=hints[-1],
            confidence=ConfidenceLevel.LOW,
            source=SourceType.WEBSITE,
            reasoning_note="Best-effort inference from geography hints.",
            evidence=[EvidenceItem(source=SourceType.WEBSITE, detail=f"Geography hints: {', '.join(hints[:3])}", url=website.final_url)],
        )
    return None


def _language(website: ExtractedWebsite, known_language: str | None) -> InferredValue | None:
    if known_language:
        return InferredValue(
            field="language",
            value=known_language,
            confidence=ConfidenceLevel.HIGH,
            source=SourceType.USER_INPUT,
            reasoning_note="Provided directly by input.",
            evidence=[EvidenceItem(source=SourceType.USER_INPUT, detail=f"Known language: {known_language}")],
        )
    if website.language_hints:
        value = website.language_hints[0]
        return InferredValue(
            field="language",
            value=value,
            confidence=ConfidenceLevel.MEDIUM,
            source=SourceType.WEBSITE,
            reasoning_note="Taken from language hint metadata.",
            evidence=[EvidenceItem(source=SourceType.WEBSITE, detail=f"Language hint: {value}", url=website.final_url)],
        )
    return None


def _match_keywords(text: str, groups: dict[str, tuple[str, ...]], fallback: str) -> tuple[str, ConfidenceLevel, str]:
    lowered = text.lower()
    for label, keywords in groups.items():
        if any(keyword in lowered for keyword in keywords):
            return label, ConfidenceLevel.MEDIUM, f"Matched keywords: {', '.join(keywords[:3])}"
    return fallback, ConfidenceLevel.LOW, "Weak heuristic fallback."


def infer_context(
    resolved_entity: ResolvedEntity,
    website: ExtractedWebsite,
    known_country: str | None = None,
    known_language: str | None = None,
    goal: str | None = None,
) -> InferredContext:
    seed_text = resolved_entity.seed.normalized_value
    evidence_text = " ".join(
        filter(
            None,
            [
                seed_text,
                website.title or "",
                website.meta_description or "",
                " ".join(website.headings),
                website.raw_text_excerpt,
            ],
        )
    )

    business_model_value, business_confidence, business_note = _match_keywords(
        evidence_text,
        {
            "SaaS": ("software", "platform", "demo", "trial", "integrations"),
            "Ecommerce": ("shop", "cart", "buy now", "checkout", "shipping"),
            "Agency": ("agency", "studio", "creative", "marketing"),
            "Consulting": ("consulting", "consultant", "advisory", "fractional"),
            "Local Service": ("book", "call now", "service area", "estimate", "appointment"),
        },
        "General Service Business",
    )

    offer_value = next(iter(website.headings), website.meta_description or website.title or "Public-facing offer not clearly stated")
    target_value, target_confidence, target_note = _match_keywords(
        evidence_text,
        {
            "Businesses": ("b2b", "teams", "companies", "enterprise", "sales"),
            "Homeowners": ("homeowners", "residential", "your home", "house"),
            "Local Consumers": ("local", "near you", "book online", "visit us"),
            "Creators or Personal Brands": ("creator", "audience", "followers", "content"),
        },
        "Target audience not explicit; likely broad buyer set",
    )

    if goal:
        conversion_value = goal
        conversion_confidence = ConfidenceLevel.HIGH
        conversion_note = "Taken from explicit goal input."
        conversion_source = SourceType.USER_INPUT
    else:
        conversion_value, conversion_confidence, conversion_note = _match_keywords(
            " ".join(website.cta_texts) + " " + evidence_text,
            {
                "Book a consultation or call": ("book", "schedule", "consultation", "call"),
                "Request a quote": ("quote", "estimate", "proposal"),
                "Start a demo or trial": ("demo", "trial", "get started"),
                "Buy directly": ("buy", "checkout", "shop"),
                "Contact the team": ("contact", "message", "talk to us"),
            },
            "Primary conversion path unclear; likely contact-led",
        )
        conversion_source = SourceType.WEBSITE

    company_name = _company_name(website) or resolved_entity.entity_name
    country = _country(website, known_country)
    language = _language(website, known_language)

    region_or_city = None
    if website.addresses:
        region_or_city = InferredValue(
            field="region_or_city",
            value=website.addresses[0],
            confidence=ConfidenceLevel.LOW,
            source=SourceType.WEBSITE,
            reasoning_note="Best-effort from public address-like text.",
            evidence=[EvidenceItem(source=SourceType.WEBSITE, detail=website.addresses[0], url=website.final_url)],
        )
    elif website.geography_hints:
        region_or_city = InferredValue(
            field="region_or_city",
            value=website.geography_hints[0],
            confidence=ConfidenceLevel.LOW,
            source=SourceType.WEBSITE,
            reasoning_note="Best-effort from geography hints.",
            evidence=[EvidenceItem(source=SourceType.WEBSITE, detail=website.geography_hints[0], url=website.final_url)],
        )

    if not country and resolved_entity.location_hint:
        country = InferredValue(
            field="country",
            value=resolved_entity.location_hint.value,
            confidence=ConfidenceLevel.LOW,
            source=SourceType.USER_INPUT,
            reasoning_note="Fallback from address-like seed because website evidence was unavailable or weak.",
            evidence=resolved_entity.location_hint.evidence,
        )

    if not language and resolved_entity.seed.seed_type == SeedType.SHORT_DESCRIPTION:
        language = InferredValue(
            field="language",
            value="unknown",
            confidence=ConfidenceLevel.LOW,
            source=SourceType.ASSUMPTION,
            reasoning_note="No language evidence available from seed-only execution.",
            evidence=resolved_entity.seed.evidence,
        )

    context = InferredContext(
        company_name=company_name,
        country=country,
        region_or_city=region_or_city,
        language=language,
        business_model=InferredValue(
            field="business_model",
            value=business_model_value,
            confidence=business_confidence,
            source=SourceType.WEBSITE,
            reasoning_note=business_note,
            evidence=[EvidenceItem(source=SourceType.WEBSITE, detail=business_note, url=website.final_url)],
        ),
        main_offer=InferredValue(
            field="main_offer",
            value=offer_value,
            confidence=ConfidenceLevel.MEDIUM if website.headings else ConfidenceLevel.LOW,
            source=SourceType.WEBSITE if website.fetch_status != "not_executed" else SourceType.ASSUMPTION,
            reasoning_note="Best public-facing offer candidate from heading, metadata, or seed fallback.",
            evidence=[
                EvidenceItem(
                    source=SourceType.WEBSITE if website.fetch_status != "not_executed" else SourceType.ASSUMPTION,
                    detail=offer_value,
                    url=website.final_url if website.fetch_status != "not_executed" else None,
                )
            ],
        ),
        target_customer=InferredValue(
            field="target_customer",
            value=target_value,
            confidence=target_confidence,
            source=SourceType.WEBSITE if website.fetch_status != "not_executed" else SourceType.ASSUMPTION,
            reasoning_note=target_note,
            evidence=[
                EvidenceItem(
                    source=SourceType.WEBSITE if website.fetch_status != "not_executed" else SourceType.ASSUMPTION,
                    detail=target_note,
                    url=website.final_url if website.fetch_status != "not_executed" else None,
                )
            ],
        ),
        conversion_goal=InferredValue(
            field="conversion_goal",
            value=conversion_value,
            confidence=conversion_confidence,
            source=conversion_source,
            reasoning_note=conversion_note,
            evidence=[EvidenceItem(source=conversion_source, detail=conversion_note, url=website.final_url)],
        ),
        summary="Commercial context inferred from seed resolution, public website evidence when available, and confidence-tagged heuristics.",
    )
    return context
