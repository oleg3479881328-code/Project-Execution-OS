# Reviewer Block References

## Internal Sources

- `docs/REVIEW_STANDARD.md` — lightweight system-wide review standard.
- `docs/AGENT_QUALITY_SCORECARD_STANDARD.md` — outcome, cost, reliability, tool use, safety, and transferability scoring for agents.
- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md` — donor and ready-solution bias before custom invention.
- `docs/RESEARCH_STANDARD.md` — source-grounded research behavior.
- `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md` — continuity and handoff readiness.
- `skills/orchestration/domain-block-creation/SKILL.md` — block construction method.

## External Donor Sources

These sources influenced the block design.

### Google Engineering Practices — Code Review

URL: `https://google.github.io/eng-practices/review/reviewer/`

Useful donor principle:

- review should inspect correctness, clarity, maintainability, and reviewer comments as an operational discipline, not as vague opinion.

### NIST AI Risk Management Framework

URL: `https://www.nist.gov/itl/ai-risk-management-framework`

Useful donor principle:

- AI review should consider risk management across design, development, use, and evaluation rather than only output appearance.

### OWASP Top 10 for LLM and GenAI Applications 2025

URL: `https://genai.owasp.org/llm-top-10/`

Useful donor principle:

- AI-agent review should include prompt injection, sensitive information disclosure, supply chain, improper output handling, excessive agency, system prompt leakage, vector weaknesses, misinformation, and unbounded consumption.

### OpenAI Simple Evals

URL: `https://github.com/openai/simple-evals`

Useful donor principle:

- repeated model-backed work should be evaluated with representative tasks and transparent scoring, not judged by one impressive answer.

### Technical Peer Review Tradition

URL: `https://en.wikipedia.org/wiki/Technical_peer_review`

Useful donor principle:

- review is strongest when it finds defects early, separates roles, and uses structured inspection rather than informal approval.

## Source Use Rule

Use primary or official sources when a review depends on current facts, technical standards, public policy, legal rules, medical guidance, financial claims, product pricing, or platform behavior.

Use internal standards for Project Execution OS behavior.

## Final Rule

A reviewer may use external sources, but must never hide weak evidence behind confident language.