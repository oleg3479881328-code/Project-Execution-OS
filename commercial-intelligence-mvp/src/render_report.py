from __future__ import annotations

import json
from pathlib import Path

from .models import CommercialIntelligenceReport, InferredValue


def _format_inferred(value: InferredValue | None) -> str:
    if not value:
        return "| unknown | unknown | unknown | unknown | unknown |"
    return f"| {value.field} | {value.value} | {value.confidence.value} | {value.source.value} | {value.reasoning_note} |"


def render_markdown(report: CommercialIntelligenceReport) -> str:
    competitor_patterns = [
        f"- {analysis.competitor.name}: {analysis.positioning}" for analysis in report.competitor_analyses
    ]
    if not competitor_patterns:
        competitor_patterns = ["- No live competitor analysis executed in this run."]

    offer_problem_lines = [f"- {item}" for item in report.offer_diagnosis.problems]
    if not offer_problem_lines:
        offer_problem_lines = ["- No major automatic issue detected; manual review still recommended."]

    context_rows = [
        "| Field | Value | Confidence | Source | Note |",
        "| --- | --- | --- | --- | --- |",
        _format_inferred(report.inferred_context.company_name),
        _format_inferred(report.inferred_context.country),
        _format_inferred(report.inferred_context.region_or_city),
        _format_inferred(report.inferred_context.language),
        _format_inferred(report.inferred_context.business_model),
        _format_inferred(report.inferred_context.main_offer),
        _format_inferred(report.inferred_context.target_customer),
        _format_inferred(report.inferred_context.conversion_goal),
    ]

    competitor_rows = [
        "| Competitor | Type | Why relevant | Source |",
        "| --- | --- | --- | --- |",
    ]
    if report.competitors_discovered:
        for competitor in report.competitors_discovered:
            competitor_rows.append(
                f"| {competitor.name} | {competitor.competitor_type} | {competitor.reason} | {competitor.source.value} |"
            )
    else:
        competitor_rows.append("| Not executed | query-plan only | No live competitor discovery executed | system |")

    funnel_rows = [
        "| Issue | Why it hurts sales | Fix | Priority |",
        "| --- | --- | --- | --- |",
    ]
    if report.funnel_issues:
        for issue in report.funnel_issues:
            funnel_rows.append(f"| {issue.issue} | {issue.reason} | {issue.fix} | {issue.priority} |")
    else:
        funnel_rows.append("| No critical funnel issue auto-detected | n/a | Manual review still recommended | low |")

    distribution_rows = [
        "| Channel | Fit | Why now | First test | Priority |",
        "| --- | --- | --- | --- | --- |",
    ]
    for channel in report.distribution_opportunities:
        distribution_rows.append(
            f"| {channel.channel} | {channel.fit} | {channel.why_now} | {channel.first_test} | {channel.priority} |"
        )

    voice_rows = [
        "| Theme | Evidence | Exact language / paraphrase | Sales implication |",
        "| --- | --- | --- | --- |",
    ]
    if report.customer_voice:
        for item in report.customer_voice:
            voice_rows.append(
                f"| {item.theme} | {item.evidence} | {item.language} | {item.sales_implication} |"
            )
    else:
        voice_rows.append("| Limited direct customer voice | Only website evidence inspected in v1 | More review/forum research needed | Treat offer wording carefully |")

    action_rows = [
        "| Week | Action | Owner | Evidence to collect |",
        "| --- | --- | --- | --- |",
    ]
    for action in report.growth_actions:
        action_rows.append(f"| {action.week} | {action.action} | {action.owner} | {action.evidence_to_collect} |")

    return "\n".join(
        [
            f"# Commercial Intelligence Report — {report.extracted_website.final_url}",
            "",
            "## Input Received",
            f"- URL: `{report.customer_input.url}`",
            f"- Goal: `{report.customer_input.goal or 'not provided'}`",
            f"- Live web search enabled: `{report.execution.web_search_enabled}`",
            "",
            "## Inference Summary",
            report.inferred_context.summary,
            "",
            "## Executive Diagnosis",
            *(f"- {item}" for item in report.recommendations[:3]),
            "",
            "## Inferred Business Context",
            *context_rows,
            "",
            "## Competitor Map",
            *competitor_rows,
            "",
            "## Competitor Patterns",
            *competitor_patterns,
            "",
            "## Customer Voice",
            *voice_rows,
            "",
            "## Offer Doctor",
            "### Current Offer Problems",
            *offer_problem_lines,
            "### Stronger Offer Angles",
            *(f"- {item}" for item in report.offer_diagnosis.stronger_angles),
            "### Headline / CTA Ideas",
            *(f"- {item}" for item in report.offer_diagnosis.headline_ideas + report.offer_diagnosis.cta_ideas),
            "",
            "## Website / Funnel Audit",
            *funnel_rows,
            "",
            "## Distribution Opportunities",
            *distribution_rows,
            "",
            "## Lead Strategy",
            "- Start with public, high-intent buyers that match the inferred business model and CTA path.",
            "- Use qualification signals before collecting or contacting leads.",
            "- Do not automate outreach in v1.",
            "",
            "## 30-Day Action Plan",
            *action_rows,
            "",
            "## Assumptions / Unknowns / Risks",
            *(f"- Assumption: {item}" for item in report.assumptions),
            *(f"- Risk: {item}" for item in report.risks),
            "",
            "## Suggested Next Test",
            "- Run the same audit on one real customer site and compare inferred context with owner-confirmed facts.",
        ]
    )


def write_outputs(report: CommercialIntelligenceReport, out_dir: str) -> None:
    target = Path(out_dir)
    target.mkdir(parents=True, exist_ok=True)
    (target / "report.md").write_text(render_markdown(report), encoding="utf-8")
    (target / "report.json").write_text(report.model_dump_json(indent=2), encoding="utf-8")
    (target / "sources.json").write_text(
        json.dumps(report.execution.model_dump(), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
