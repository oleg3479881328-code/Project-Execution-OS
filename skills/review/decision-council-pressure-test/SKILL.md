---
name: decision-council-pressure-test
description: Pressure-test a high-stakes decision through five adversarial review lenses, anonymous peer review, and one synthesized recommendation.
category: review
status: candidate
target_agent: tool-neutral
compatibility:
  - chatgpt
  - codex
  - claude
inputs:
  - decision_question
  - options_or_tradeoff
  - relevant_context
outputs:
  - advisor_responses
  - peer_review_findings
  - council_verdict
  - recommendation
  - first_action
safety_level: medium
source: adapted_from_tenfoldmarc_llm_council_skill
review_status: not_reviewed
version: 0.1.0
---

# Purpose

Pressure-test an important decision before acceptance when a single agreeable answer would be too weak or too risky.

# When to Use

Use this skill when:
- the user faces a real tradeoff with non-trivial downside;
- several options compete and framing bias is likely;
- a decision needs adversarial tension before project commitment;
- a recommendation should survive multiple independent lenses, not one assistant's first instinct.

Good fits:
- pricing or offer choice
- pivot vs continue
- positioning choice
- tool vs workflow tradeoff
- hire vs automate
- launch now vs delay

# When Not to Use

Do not use this skill for:
- factual questions with one right answer;
- simple summarization;
- pure writing or generation tasks;
- trivial yes/no questions with no real stakes;
- situations where the user already wants direct execution instead of decision review.

# Core Principle

One answer is not a council.

The value comes from structured disagreement, anonymous peer review, and one final synthesis.

# Review Lenses

Run five distinct lenses on the same question:

1. Contrarian
2. First Principles
3. Expansionist
4. Outsider
5. Executor

These are thinking styles, not vanity personas.

# Workflow

1. Frame the question neutrally.
2. Gather only the context that materially changes the decision.
3. Run all five lenses independently.
4. Anonymize the responses.
5. Run peer review across the anonymized responses.
6. Synthesize:
   - where the council agrees
   - where it clashes
   - blind spots caught
   - recommendation
   - one concrete first action

# Output Contract

Return:

1. Framed question
2. Lens responses
3. Peer review highlights
4. Final council verdict

The verdict should contain:
- where the council agrees
- where the council clashes
- blind spots the council caught
- the recommendation
- the one thing to do first

# Constraints

Do not:
- use the council as decorative theater for simple tasks;
- smooth over real disagreements just to sound balanced;
- let one lens dominate before peer review;
- confuse pressure-testing with factual verification;
- turn the output into a giant report when a concise verdict is enough.

# Failure Modes

Possible failures:
- fake disagreement between weakly different lenses;
- using the council for trivial tasks;
- allowing framing bias to infect every lens;
- producing five polite variants of the same answer;
- returning "it depends" instead of a real recommendation.

# Validation Checklist

Before finalizing:
- the question was framed neutrally;
- all five lenses were run independently;
- peer review actually happened;
- agreement and disagreement were separated;
- one concrete first action was returned.

# References

See `references.md`.
