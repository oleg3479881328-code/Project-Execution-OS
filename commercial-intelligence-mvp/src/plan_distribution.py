from __future__ import annotations

from .models import DistributionOpportunity, GrowthAction, InferredContext, SourceType


def plan_distribution(context: InferredContext, has_local_signals: bool) -> tuple[list[DistributionOpportunity], list[str], list[GrowthAction]]:
    business_model = context.business_model.value if context.business_model else "General Service Business"
    company = context.company_name.value if context.company_name else "The company"

    opportunities: list[DistributionOpportunity] = []
    recommendations: list[str] = []
    actions: list[GrowthAction] = []

    if business_model in {"Local Service", "General Service Business"} or has_local_signals:
        opportunities.append(
            DistributionOpportunity(
                channel="Local SEO / Google Business Profile",
                fit="high",
                why_now="Location and contact-path clarity matter for lead capture.",
                first_test="Improve Google Business Profile, service pages, and location trust signals.",
                priority="high",
            )
        )
    if business_model in {"Agency", "Consulting", "SaaS", "General Service Business"}:
        opportunities.append(
            DistributionOpportunity(
                channel="SEO service and comparison pages",
                fit="high",
                why_now="The site can capture intent-driven buyers if offer pages match search language.",
                first_test="Create one high-intent service page and one comparison/problem page.",
                priority="high",
            )
        )
        opportunities.append(
            DistributionOpportunity(
                channel="Case-study-led content",
                fit="medium",
                why_now="Proof content reduces friction for mid-intent buyers.",
                first_test="Publish one short case-study page tied to a common buying objection.",
                priority="medium",
            )
        )
    if business_model in {"Agency", "Consulting", "SaaS"}:
        opportunities.append(
            DistributionOpportunity(
                channel="B2B outreach or partnerships",
                fit="medium",
                why_now="Structured outbound or referrals can complement inbound while traffic is still thin.",
                first_test="Define ICP, qualification rules, and one non-spam referral or outreach angle.",
                priority="medium",
            )
        )

    recommendations.extend(
        [
            "Tighten the first-screen promise so the buyer immediately understands the result and next step.",
            "Match service pages and CTAs to the inferred purchase intent rather than using one generic contact ask everywhere.",
            "Add trust proof close to conversion points before scaling traffic acquisition.",
        ]
    )

    actions.extend(
        [
            GrowthAction(
                week="Week 1",
                action=f"Rewrite the homepage hero and primary CTA for {company}.",
                evidence_to_collect="Before/after screenshot and CTA click or inquiry-rate change.",
                expected_impact="Higher clarity and more qualified first-step conversions.",
                confidence="high",
            ),
            GrowthAction(
                week="Week 2",
                action="Publish or improve one high-intent service page and add proof near the CTA.",
                evidence_to_collect="Search impressions, session quality, and conversion events on the page.",
                expected_impact="Better search relevance and stronger buyer trust.",
                confidence="medium",
            ),
            GrowthAction(
                week="Week 3-4",
                action="Run one distribution experiment from the highest-fit channel list.",
                evidence_to_collect="Lead quality, volume, and cost or effort per qualified conversation.",
                expected_impact="Validate the best short-term acquisition channel.",
                confidence="medium",
            ),
        ]
    )
    return opportunities, recommendations, actions
