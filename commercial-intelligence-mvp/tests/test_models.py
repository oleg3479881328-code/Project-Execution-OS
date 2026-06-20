from src.models import (
    CommercialIntelligenceReport,
    ConfidenceLevel,
    CustomerInput,
    ExecutionMetadata,
    ExtractedWebsite,
    InferredContext,
    InferredValue,
    OfferDiagnosis,
    SourceType,
)


def test_customer_input_defaults() -> None:
    customer = CustomerInput(url="https://example.com")
    assert customer.max_competitors == 5
    assert customer.known_competitors == []
    assert customer.no_web is False


def test_inferred_value_requires_confidence_and_source() -> None:
    inferred = InferredValue(
        field="business_model",
        value="SaaS",
        confidence=ConfidenceLevel.MEDIUM,
        source=SourceType.WEBSITE,
        reasoning_note="Matched software-related keywords.",
    )
    assert inferred.confidence == ConfidenceLevel.MEDIUM
    assert inferred.source == SourceType.WEBSITE


def test_report_serialization_contains_execution_metadata() -> None:
    report = CommercialIntelligenceReport(
        customer_input=CustomerInput(url="https://example.com"),
        execution=ExecutionMetadata(
            timestamp_utc="2026-06-20T00:00:00Z",
            web_search_enabled=False,
            competitor_query_plan=["example query"],
        ),
        extracted_website=ExtractedWebsite(
            requested_url="https://example.com",
            final_url="https://example.com",
            fetch_status="http_200",
        ),
        inferred_context=InferredContext(
            summary="Test context",
            business_model=InferredValue(
                field="business_model",
                value="General Service Business",
                confidence=ConfidenceLevel.LOW,
                source=SourceType.ASSUMPTION,
                reasoning_note="Fallback",
            ),
        ),
        offer_diagnosis=OfferDiagnosis(current_offer_summary="Basic offer"),
    )
    dumped = report.model_dump()
    assert dumped["execution"]["competitor_query_plan"] == ["example query"]
    assert dumped["inferred_context"]["business_model"]["source"] == "assumption"
