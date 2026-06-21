from __future__ import annotations

import re
from urllib.parse import urlparse

from .models import ConfidenceLevel, CustomerSeed, EvidenceItem, InferredValue, ResolvedEntity, SeedType, SourceType

EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})$")
PHONE_RE = re.compile(r"^\+?\d[\d\-\s\(\)]{7,}\d$")
URL_RE = re.compile(r"^https?://", re.IGNORECASE)
SOCIAL_HINTS = ("linkedin.com", "facebook.com", "instagram.com", "x.com", "twitter.com", "t.me", "youtube.com")
MARKETPLACE_HINTS = ("etsy.com", "amazon.com", "upwork.com", "fiverr.com", "airbnb.com")
GOOGLE_BUSINESS_HINTS = ("google.com/maps", "g.page", "google business", "goo.gl/maps")


def detect_seed_type(seed: str) -> SeedType:
    value = seed.strip()
    lower = value.lower()
    if URL_RE.match(value):
        if any(hint in lower for hint in GOOGLE_BUSINESS_HINTS):
            return SeedType.GOOGLE_BUSINESS_PROFILE
        if any(hint in lower for hint in MARKETPLACE_HINTS):
            return SeedType.MARKETPLACE_PROFILE
        if any(hint in lower for hint in SOCIAL_HINTS):
            return SeedType.SOCIAL_PROFILE
        return SeedType.WEBSITE_URL
    if EMAIL_RE.match(value):
        return SeedType.EMAIL
    if PHONE_RE.match(value):
        return SeedType.PHONE_NUMBER
    if "," in value and any(token.strip() for token in value.split(",")) and any(ch.isdigit() for ch in value):
        return SeedType.ADDRESS
    if len(value.split()) >= 4:
        if any(keyword in lower for keyword in ("llc", "inc", "clinic", "dental", "agency", "studio", "company", "co.")):
            return SeedType.COMPANY_NAME
        return SeedType.SHORT_DESCRIPTION
    if len(value.split()) in {2, 3} and value.replace(" ", "").isalpha():
        if value.istitle():
            return SeedType.PERSON_NAME
    if len(value.split()) >= 2:
        return SeedType.COMPANY_NAME
    return SeedType.UNKNOWN


def normalize_seed(seed: str, seed_type: SeedType) -> str:
    value = seed.strip()
    if seed_type in {SeedType.WEBSITE_URL, SeedType.SOCIAL_PROFILE, SeedType.MARKETPLACE_PROFILE, SeedType.GOOGLE_BUSINESS_PROFILE}:
        return value.rstrip("/")
    if seed_type == SeedType.EMAIL:
        return value.lower()
    if seed_type == SeedType.PHONE_NUMBER:
        return re.sub(r"\s+", " ", value)
    return value


def resolve_seed(seed: str, seed_type: SeedType | None = None) -> ResolvedEntity:
    detected = seed_type or detect_seed_type(seed)
    normalized = normalize_seed(seed, detected)
    evidence = [EvidenceItem(source=SourceType.USER_INPUT, detail=f"Seed provided by user: {normalized}")]
    confidence = ConfidenceLevel.HIGH if seed_type else ConfidenceLevel.MEDIUM
    customer_seed = CustomerSeed(
        raw_value=seed,
        seed_type=detected,
        normalized_value=normalized,
        confidence=confidence,
        evidence=evidence,
    )

    entity_name = None
    website_url = None
    email_domain = None
    phone_hint = None
    location_hint = None
    profile_hint = None

    if detected in {SeedType.WEBSITE_URL, SeedType.SOCIAL_PROFILE, SeedType.MARKETPLACE_PROFILE, SeedType.GOOGLE_BUSINESS_PROFILE}:
        parsed = urlparse(normalized)
        host = parsed.netloc.replace("www.", "")
        domain_stem = host.split(".")[0].replace("-", " ").title() if host else normalized
        website_url = InferredValue(
            field="website_url",
            value=normalized,
            confidence=ConfidenceLevel.HIGH if detected == SeedType.WEBSITE_URL else ConfidenceLevel.MEDIUM,
            source=SourceType.USER_INPUT,
            reasoning_note="Derived directly from the provided seed or profile URL.",
            evidence=evidence,
        )
        entity_name = InferredValue(
            field="entity_name",
            value=domain_stem,
            confidence=ConfidenceLevel.LOW if detected != SeedType.WEBSITE_URL else ConfidenceLevel.MEDIUM,
            source=SourceType.ASSUMPTION,
            reasoning_note="Best-effort entity guess from URL host.",
            evidence=evidence,
        )
        if detected != SeedType.WEBSITE_URL:
            profile_hint = InferredValue(
                field="profile_hint",
                value=normalized,
                confidence=ConfidenceLevel.HIGH,
                source=SourceType.USER_INPUT,
                reasoning_note="Profile or listing URL provided directly as the seed.",
                evidence=evidence,
            )
    elif detected == SeedType.EMAIL:
        match = EMAIL_RE.match(normalized)
        domain = match.group(1) if match else normalized.split("@")[-1]
        email_domain = InferredValue(
            field="email_domain",
            value=domain,
            confidence=ConfidenceLevel.HIGH,
            source=SourceType.USER_INPUT,
            reasoning_note="Extracted from the email seed.",
            evidence=evidence,
        )
        entity_name = InferredValue(
            field="entity_name",
            value=domain.split(".")[0].replace("-", " ").title(),
            confidence=ConfidenceLevel.LOW,
            source=SourceType.ASSUMPTION,
            reasoning_note="Best-effort organization guess from email domain.",
            evidence=evidence,
        )
        website_url = InferredValue(
            field="website_url",
            value=f"https://{domain}",
            confidence=ConfidenceLevel.LOW,
            source=SourceType.ASSUMPTION,
            reasoning_note="Likely public website inferred from email domain.",
            evidence=evidence,
        )
    elif detected == SeedType.PHONE_NUMBER:
        phone_hint = InferredValue(
            field="phone_hint",
            value=normalized,
            confidence=ConfidenceLevel.HIGH,
            source=SourceType.USER_INPUT,
            reasoning_note="Phone number provided directly as the seed.",
            evidence=evidence,
        )
    elif detected == SeedType.ADDRESS:
        location_hint = InferredValue(
            field="location_hint",
            value=normalized,
            confidence=ConfidenceLevel.HIGH,
            source=SourceType.USER_INPUT,
            reasoning_note="Address-like seed provided directly by user.",
            evidence=evidence,
        )
    else:
        entity_name = InferredValue(
            field="entity_name",
            value=normalized,
            confidence=ConfidenceLevel.MEDIUM if detected in {SeedType.COMPANY_NAME, SeedType.PERSON_NAME} else ConfidenceLevel.LOW,
            source=SourceType.USER_INPUT,
            reasoning_note="Entity name or description comes directly from the provided seed.",
            evidence=evidence,
        )

    summary = "Seed classified and normalized before downstream evidence collection."
    return ResolvedEntity(
        seed=customer_seed,
        entity_name=entity_name,
        website_url=website_url,
        email_domain=email_domain,
        phone_hint=phone_hint,
        location_hint=location_hint,
        profile_hint=profile_hint,
        summary=summary,
    )
