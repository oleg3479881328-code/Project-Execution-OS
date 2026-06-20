from __future__ import annotations

from .models import CompetitorAnalysis, CompetitorCandidate, EvidenceItem, SourceType


def analyze_competitors(candidates: list[CompetitorCandidate]) -> list[CompetitorAnalysis]:
    analyses: list[CompetitorAnalysis] = []
    for candidate in candidates:
        executed = "executed" if candidate.executed_search else "not_executed"
        analyses.append(
            CompetitorAnalysis(
                competitor=candidate,
                positioning="Initial competitor placeholder based on discovery evidence; detailed page extraction not executed in v1.",
                headline=None,
                pricing_signal=None,
                trust_signals=["Requires direct competitor page extraction for stronger conclusions."],
                strengths=["Visible enough to appear in known list or discovery results."],
                weaknesses=["Detailed funnel, pricing, and messaging analysis not yet executed."],
                ideas_to_adapt=["Compare this competitor's headline, CTA, and proof on a future pass."],
                ideas_to_avoid=["Do not copy positioning without validating audience fit."],
                evidence=[
                    EvidenceItem(
                        source=SourceType.SEARCH if candidate.executed_search else candidate.source,
                        detail=candidate.reason,
                        url=f"https://{candidate.domain}" if candidate.domain else None,
                    )
                ],
                status=executed,
            )
        )
    return analyses
