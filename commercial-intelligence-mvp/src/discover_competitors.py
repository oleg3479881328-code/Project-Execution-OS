from __future__ import annotations

import os
from urllib.parse import urlparse

import requests

from .models import ConfidenceLevel, CompetitorCandidate, CustomerInput, ExecutionMetadata, InferredContext, SourceType


def build_query_plan(customer: CustomerInput, context: InferredContext) -> list[str]:
    company = context.company_name.value if context.company_name else urlparse(str(customer.url)).netloc
    offer = context.main_offer.value if context.main_offer else "service"
    country = customer.country or (context.country.value if context.country else "")
    language = customer.language or (context.language.value if context.language else "")
    city = context.region_or_city.value if context.region_or_city else ""

    base_terms = [offer, company]
    if city:
        base_terms.append(city)
    if country:
        base_terms.append(country)
    if language:
        base_terms.append(language)

    concise_offer = offer[:80]
    plan = [
        f'"{concise_offer}" competitors {country}'.strip(),
        f'"{concise_offer}" alternatives {country}'.strip(),
        f'best {concise_offer} {city or country}'.strip(),
        f'"{company}" reviews'.strip(),
        f'"{company}" vs competitor'.strip(),
    ]
    return list(dict.fromkeys(query for query in plan if query and query != '""'))


def _search_tavily(query: str, max_results: int) -> dict:
    api_key = os.getenv("TAVILY_API_KEY", "").strip()
    response = requests.post(
        "https://api.tavily.com/search",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        json={
            "query": query,
            "search_depth": "basic",
            "include_answer": False,
            "include_raw_content": False,
            "max_results": max_results,
            "topic": "general",
        },
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


def discover_competitors(
    customer: CustomerInput,
    context: InferredContext,
    execution: ExecutionMetadata,
) -> list[CompetitorCandidate]:
    query_plan = build_query_plan(customer, context)
    execution.competitor_query_plan = query_plan

    candidates: list[CompetitorCandidate] = []
    for known in customer.known_competitors:
        domain = urlparse(known).netloc or known
        candidates.append(
            CompetitorCandidate(
                name=domain.replace("www.", "") or known,
                domain=domain or None,
                competitor_type="known",
                reason="Provided directly by user input.",
                discovery_query=None,
                source=SourceType.USER_INPUT,
                confidence=ConfidenceLevel.HIGH,
                executed_search=False,
            )
        )

    if customer.no_web:
        execution.assumptions.append("Live web search disabled by --no-web.")
        return candidates

    api_key = os.getenv("TAVILY_API_KEY", "").strip()
    if not api_key:
        execution.assumptions.append("No Tavily API key available; competitor discovery downgraded to query-plan mode.")
        execution.sources_failed.append("tavily_search:not_configured")
        return candidates

    execution.web_search_enabled = True
    execution.search_provider = "tavily"
    for query in query_plan[:2]:
        execution.sources_attempted.append(f"tavily_search:{query}")
        try:
            payload = _search_tavily(query, customer.max_competitors)
        except Exception as exc:
            execution.sources_failed.append(f"tavily_search:{query}:{exc}")
            continue
        execution.sources_succeeded.append(f"tavily_search:{query}")
        for result in payload.get("results", []):
            url = result.get("url", "")
            domain = urlparse(url).netloc.replace("www.", "")
            if not domain or domain in urlparse(str(customer.url)).netloc:
                continue
            candidates.append(
                CompetitorCandidate(
                    name=result.get("title") or domain,
                    domain=domain,
                    competitor_type="search_discovered",
                    reason=result.get("content", "Discovered through Tavily search.")[:240],
                    discovery_query=query,
                    source=SourceType.SEARCH,
                    confidence=ConfidenceLevel.MEDIUM,
                    executed_search=True,
                )
            )
        if len(candidates) >= customer.max_competitors:
            break

    deduped = []
    seen = set()
    for candidate in candidates:
        key = candidate.domain or candidate.name
        if key in seen:
            continue
        seen.add(key)
        deduped.append(candidate)
    return deduped[: customer.max_competitors]
