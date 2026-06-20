from __future__ import annotations

from .models import (
    ConfidenceLevel,
    CustomerVoiceFinding,
    ExtractedWebsite,
    FunnelIssue,
    InferredContext,
    OfferDiagnosis,
    SourceType,
)


def diagnose_offer(website: ExtractedWebsite, context: InferredContext) -> tuple[OfferDiagnosis, list[FunnelIssue], list[CustomerVoiceFinding]]:
    problems: list[str] = []
    stronger_angles: list[str] = []
    headline_ideas: list[str] = []
    cta_ideas: list[str] = []
    trust_improvements: list[str] = []
    guarantee_ideas: list[str] = []
    funnel_issues: list[FunnelIssue] = []
    voice: list[CustomerVoiceFinding] = []

    company = context.company_name.value if context.company_name else "The company"
    offer = context.main_offer.value if context.main_offer else "the current offer"
    audience = context.target_customer.value if context.target_customer else "target buyers"

    if not website.cta_texts:
        problems.append("No clear CTA was detected on the public pages inspected.")
        funnel_issues.append(
            FunnelIssue(
                issue="Weak CTA visibility",
                reason="Visitors may not know the next step quickly.",
                fix="Add a visible primary CTA above the fold and repeat it on service pages.",
                priority="high",
            )
        )
    else:
        cta_ideas.extend(
            [
                f"Book a strategy call with {company}",
                f"Get a tailored quote for {audience}",
                f"See if {offer[:60]} fits your situation",
            ]
        )

    if not website.trust_signals:
        problems.append("Public proof signals are thin or absent.")
        trust_improvements.extend(
            [
                "Add customer testimonials close to the primary CTA.",
                "Show outcome-focused proof such as case studies, before/after, or metrics.",
                "Surface certifications, awards, or notable clients if available.",
            ]
        )
        funnel_issues.append(
            FunnelIssue(
                issue="Insufficient trust proof",
                reason="Buyers cannot quickly verify credibility or expected outcomes.",
                fix="Add testimonials, case studies, and trust badges on the homepage and offer pages.",
                priority="high",
            )
        )

    if not website.pricing_pages:
        problems.append("Pricing or budget expectation is not obvious from the inspected pages.")
        funnel_issues.append(
            FunnelIssue(
                issue="Low budget clarity",
                reason="Unclear pricing creates friction and low-intent leads.",
                fix="Publish pricing ranges, starting prices, or qualification criteria.",
                priority="medium",
            )
        )

    if not website.contact_pages and not website.contact_emails and not website.contact_phones:
        problems.append("Contact path is weak or hard to verify.")
        funnel_issues.append(
            FunnelIssue(
                issue="Fragile contact path",
                reason="Potential buyers may not find a reliable way to reach the business.",
                fix="Add a dedicated contact page with multiple contact methods and expected response time.",
                priority="high",
            )
        )

    stronger_angles.extend(
        [
            f"Make the outcome of {offer[:80]} concrete for {audience}.",
            "Reduce buyer risk with a clear process, proof, and next-step expectation.",
            "State who the offer is for and who it is not for.",
            "Translate generic benefits into measurable or observable outcomes.",
            "Tie the CTA to the buyer's current intent level, not a vague contact ask.",
        ]
    )

    headline_ideas.extend(
        [
            f"{company}: a clearer way for {audience} to achieve the desired result",
            f"Get {offer[:60]} without the usual friction, guesswork, or delays",
            f"See whether {company} is the right fit before you commit",
            f"Trusted support for {audience} who need results, not just promises",
            f"Start with a focused next step instead of a generic inquiry",
        ]
    )

    guarantee_ideas.extend(
        [
            "Offer a low-risk first step such as a short audit, fit call, or scoped review.",
            "Explain turnaround time, process clarity, and what happens after the CTA.",
        ]
    )

    if website.trust_signals:
        voice.append(
            CustomerVoiceFinding(
                theme="Trust and proof",
                evidence="The site references reviews, testimonials, or case studies.",
                language="Public proof matters in this buying process.",
                sales_implication="Strengthen trust proof near the first CTA and on service pages.",
                source=SourceType.WEBSITE,
                confidence=ConfidenceLevel.MEDIUM,
            )
        )

    if website.contact_phones:
        voice.append(
            CustomerVoiceFinding(
                theme="Speed to contact",
                evidence="Phone contact is publicly available.",
                language="Some buyers likely want a faster contact path than a long form.",
                sales_implication="Offer call-first and form-first paths to match buyer intent.",
                source=SourceType.WEBSITE,
                confidence=ConfidenceLevel.MEDIUM,
            )
        )

    offer_diagnosis = OfferDiagnosis(
        current_offer_summary=offer,
        problems=problems,
        stronger_angles=stronger_angles,
        headline_ideas=headline_ideas[:5],
        cta_ideas=cta_ideas[:5],
        trust_improvements=trust_improvements[:5],
        guarantee_ideas=guarantee_ideas[:5],
    )
    return offer_diagnosis, funnel_issues, voice
