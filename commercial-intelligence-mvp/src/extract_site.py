from __future__ import annotations

import json
import re
from collections import OrderedDict
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

from .models import ExtractedWebsite

USER_AGENT = "CommercialIntelligenceMVP/0.1 (+https://github.com/oleg3479881328-code/Project-Execution-OS)"

PHONE_RE = re.compile(r"(\+?\d[\d\-\s\(\)]{7,}\d)")
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

CTA_KEYWORDS = (
    "book",
    "call",
    "contact",
    "demo",
    "get started",
    "learn more",
    "request",
    "schedule",
    "sign up",
    "start",
    "talk",
)

SOCIAL_DOMAINS = ("linkedin.com", "facebook.com", "instagram.com", "youtube.com", "t.me", "x.com")


def _unique(items: list[str]) -> list[str]:
    return list(OrderedDict.fromkeys(item for item in items if item))


def _extract_json_ld(soup: BeautifulSoup) -> list[dict]:
    records: list[dict] = []
    for tag in soup.select('script[type="application/ld+json"]'):
        raw = tag.string or tag.get_text(strip=True)
        if not raw:
            continue
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, list):
            records.extend(item for item in parsed if isinstance(item, dict))
        elif isinstance(parsed, dict):
            records.append(parsed)
    return records


def _extract_addresses(text: str) -> list[str]:
    matches = re.findall(
        r"\b\d{1,5}\s+[A-Za-z0-9.\-\s]+(?:Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Drive|Dr|Lane|Ln)\b.*",
        text,
        flags=re.IGNORECASE,
    )
    return _unique([match.strip()[:180] for match in matches[:5]])


def _find_language_hints(soup: BeautifulSoup) -> list[str]:
    hints: list[str] = []
    html = soup.find("html")
    if html and html.get("lang"):
        hints.append(html["lang"])
    for meta_name in ("language", "content-language"):
        tag = soup.find("meta", attrs={"name": meta_name}) or soup.find("meta", attrs={"http-equiv": meta_name})
        if tag and tag.get("content"):
            hints.append(tag["content"])
    return _unique(hints)


def _find_currency_hints(text: str) -> list[str]:
    hints = []
    if "$" in text:
        hints.append("USD")
    if "€" in text:
        hints.append("EUR")
    if "£" in text:
        hints.append("GBP")
    if "CAD" in text.upper():
        hints.append("CAD")
    if "AUD" in text.upper():
        hints.append("AUD")
    return _unique(hints)


def _classify_links(links: list[str]) -> tuple[list[str], list[str], list[str], list[str], list[str]]:
    service_pages: list[str] = []
    pricing_pages: list[str] = []
    contact_pages: list[str] = []
    legal_pages: list[str] = []
    social_links: list[str] = []

    for link in links:
        lower = link.lower()
        if any(domain in lower for domain in SOCIAL_DOMAINS):
            social_links.append(link)
        if any(keyword in lower for keyword in ("/service", "/solutions", "/product", "/pricing", "/plans")):
            service_pages.append(link)
        if any(keyword in lower for keyword in ("/pricing", "/plans", "/quote", "/cost")):
            pricing_pages.append(link)
        if any(keyword in lower for keyword in ("/contact", "/book", "/demo", "/consult")):
            contact_pages.append(link)
        if any(keyword in lower for keyword in ("/privacy", "/terms", "/legal")):
            legal_pages.append(link)

    return (
        _unique(service_pages),
        _unique(pricing_pages),
        _unique(contact_pages),
        _unique(legal_pages),
        _unique(social_links),
    )


def extract_website(url: str, timeout: int = 20) -> ExtractedWebsite:
    response = requests.get(
        url,
        timeout=timeout,
        headers={"User-Agent": USER_AGENT},
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string.strip() if soup.title and soup.title.string else None
    meta = soup.find("meta", attrs={"name": "description"}) or soup.find("meta", attrs={"property": "og:description"})
    meta_description = meta.get("content", "").strip() if meta else None

    headings = _unique(
        [
            tag.get_text(" ", strip=True)
            for tag in soup.select("h1, h2, h3")
            if tag.get_text(" ", strip=True)
        ]
    )[:15]
    links = _unique(
        [
            urljoin(response.url, tag.get("href", "").strip())
            for tag in soup.find_all("a", href=True)
            if tag.get("href", "").strip() and not tag.get("href", "").startswith("#")
        ]
    )[:80]

    service_pages, pricing_pages, contact_pages, legal_pages, social_links = _classify_links(links)

    cta_texts = _unique(
        [
            tag.get_text(" ", strip=True)
            for tag in soup.select("a, button")
            if tag.get_text(" ", strip=True)
            and any(keyword in tag.get_text(" ", strip=True).lower() for keyword in CTA_KEYWORDS)
        ]
    )[:20]

    text = soup.get_text(" ", strip=True)
    excerpt = re.sub(r"\s+", " ", text)[:2500]
    phones = _unique([match.strip() for match in PHONE_RE.findall(text)])[:10]
    emails = _unique([match.strip() for match in EMAIL_RE.findall(text)])[:10]
    json_ld = _extract_json_ld(soup)

    geography_hints = []
    parsed = urlparse(response.url)
    suffix = parsed.netloc.split(".")[-1].lower()
    if suffix in {"uk", "ca", "au", "de", "fr", "it", "es"}:
        geography_hints.append(suffix.upper())
    for record in json_ld:
        address = record.get("address")
        if isinstance(address, dict):
            for key in ("addressLocality", "addressRegion", "addressCountry"):
                value = address.get(key)
                if value:
                    geography_hints.append(str(value))

    trust_signals = []
    lowered = text.lower()
    if "testimonial" in lowered or "review" in lowered:
        trust_signals.append("Testimonials or reviews mentioned on site")
    if "case stud" in lowered:
        trust_signals.append("Case studies mentioned on site")
    if "certified" in lowered or "award" in lowered:
        trust_signals.append("Certification or awards mentioned")

    return ExtractedWebsite(
        requested_url=url,
        final_url=response.url,
        fetch_status=f"http_{response.status_code}",
        title=title,
        meta_description=meta_description,
        headings=headings,
        links=links,
        social_links=social_links,
        cta_texts=cta_texts,
        contact_emails=emails,
        contact_phones=phones,
        addresses=_extract_addresses(text),
        service_pages=service_pages,
        pricing_pages=pricing_pages,
        contact_pages=contact_pages,
        legal_pages=legal_pages,
        language_hints=_find_language_hints(soup),
        geography_hints=_unique(geography_hints),
        currency_hints=_find_currency_hints(text),
        json_ld=json_ld,
        raw_text_excerpt=excerpt,
        trust_signals=trust_signals,
    )
