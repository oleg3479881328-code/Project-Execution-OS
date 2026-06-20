from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, HttpUrl


class ConfidenceLevel(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class SourceType(str, Enum):
    WEBSITE = "website"
    SEARCH = "search"
    COMPETITOR = "competitor"
    DIRECTORY = "directory"
    ASSUMPTION = "assumption"
    USER_INPUT = "user_input"
    SYSTEM = "system"


class EvidenceItem(BaseModel):
    source: SourceType
    detail: str
    url: str | None = None


class InferredValue(BaseModel):
    field: str
    value: str
    confidence: ConfidenceLevel
    source: SourceType
    reasoning_note: str
    evidence: list[EvidenceItem] = Field(default_factory=list)


class CustomerInput(BaseModel):
    url: HttpUrl
    country: str | None = None
    language: str | None = None
    known_competitors: list[str] = Field(default_factory=list)
    goal: str | None = None
    max_competitors: int = Field(default=5, ge=1, le=10)
    no_web: bool = False


class ExtractedWebsite(BaseModel):
    requested_url: str
    final_url: str
    fetch_status: str
    title: str | None = None
    meta_description: str | None = None
    headings: list[str] = Field(default_factory=list)
    links: list[str] = Field(default_factory=list)
    social_links: list[str] = Field(default_factory=list)
    cta_texts: list[str] = Field(default_factory=list)
    contact_emails: list[str] = Field(default_factory=list)
    contact_phones: list[str] = Field(default_factory=list)
    addresses: list[str] = Field(default_factory=list)
    service_pages: list[str] = Field(default_factory=list)
    pricing_pages: list[str] = Field(default_factory=list)
    contact_pages: list[str] = Field(default_factory=list)
    legal_pages: list[str] = Field(default_factory=list)
    language_hints: list[str] = Field(default_factory=list)
    geography_hints: list[str] = Field(default_factory=list)
    currency_hints: list[str] = Field(default_factory=list)
    json_ld: list[dict[str, Any]] = Field(default_factory=list)
    raw_text_excerpt: str = ""
    trust_signals: list[str] = Field(default_factory=list)


class InferredContext(BaseModel):
    company_name: InferredValue | None = None
    country: InferredValue | None = None
    region_or_city: InferredValue | None = None
    language: InferredValue | None = None
    business_model: InferredValue | None = None
    main_offer: InferredValue | None = None
    target_customer: InferredValue | None = None
    conversion_goal: InferredValue | None = None
    summary: str


class CompetitorCandidate(BaseModel):
    name: str
    domain: str | None = None
    competitor_type: str
    reason: str
    discovery_query: str | None = None
    source: SourceType
    confidence: ConfidenceLevel
    executed_search: bool = False


class CompetitorAnalysis(BaseModel):
    competitor: CompetitorCandidate
    positioning: str
    headline: str | None = None
    pricing_signal: str | None = None
    trust_signals: list[str] = Field(default_factory=list)
    strengths: list[str] = Field(default_factory=list)
    weaknesses: list[str] = Field(default_factory=list)
    ideas_to_adapt: list[str] = Field(default_factory=list)
    ideas_to_avoid: list[str] = Field(default_factory=list)
    evidence: list[EvidenceItem] = Field(default_factory=list)
    status: str = "not_executed"


class CustomerVoiceFinding(BaseModel):
    theme: str
    evidence: str
    language: str
    sales_implication: str
    source: SourceType
    confidence: ConfidenceLevel


class OfferDiagnosis(BaseModel):
    current_offer_summary: str
    problems: list[str] = Field(default_factory=list)
    stronger_angles: list[str] = Field(default_factory=list)
    headline_ideas: list[str] = Field(default_factory=list)
    cta_ideas: list[str] = Field(default_factory=list)
    trust_improvements: list[str] = Field(default_factory=list)
    guarantee_ideas: list[str] = Field(default_factory=list)


class FunnelIssue(BaseModel):
    issue: str
    reason: str
    fix: str
    priority: str


class DistributionOpportunity(BaseModel):
    channel: str
    fit: str
    why_now: str
    first_test: str
    priority: str


class GrowthAction(BaseModel):
    week: str
    action: str
    owner: str = "owner"
    evidence_to_collect: str
    expected_impact: str
    confidence: ConfidenceLevel


class ExecutionMetadata(BaseModel):
    timestamp_utc: str
    web_search_enabled: bool
    search_provider: str | None = None
    sources_attempted: list[str] = Field(default_factory=list)
    sources_succeeded: list[str] = Field(default_factory=list)
    sources_failed: list[str] = Field(default_factory=list)
    assumptions: list[str] = Field(default_factory=list)
    competitor_query_plan: list[str] = Field(default_factory=list)


class CommercialIntelligenceReport(BaseModel):
    customer_input: CustomerInput
    execution: ExecutionMetadata
    extracted_website: ExtractedWebsite
    inferred_context: InferredContext
    competitors_discovered: list[CompetitorCandidate] = Field(default_factory=list)
    competitor_analyses: list[CompetitorAnalysis] = Field(default_factory=list)
    customer_voice: list[CustomerVoiceFinding] = Field(default_factory=list)
    offer_diagnosis: OfferDiagnosis
    funnel_issues: list[FunnelIssue] = Field(default_factory=list)
    distribution_opportunities: list[DistributionOpportunity] = Field(default_factory=list)
    growth_actions: list[GrowthAction] = Field(default_factory=list)
    confirmed_facts: list[str] = Field(default_factory=list)
    assumptions: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
    risks: list[str] = Field(default_factory=list)
