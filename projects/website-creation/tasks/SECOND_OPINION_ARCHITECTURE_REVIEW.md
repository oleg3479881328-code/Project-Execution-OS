# TASK — Website Creator — Independent Architecture & Technical Review

## Entry

Enter through PEOS first:

https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/START_HERE.md

Then enter Website Creator:

https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/projects/website-creation/PROJECT.md

Project state:

https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/projects/website-creation/PROJECT_STATE.md

Project router:

https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/projects/website-creation/ROUTER.md

Source registry:

https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/projects/website-creation/SOURCE_REGISTRY.md

Tool/donor registry:

https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/projects/website-creation/TOOL_DONOR_REGISTRY.md

Universal editor standard:

https://github.com/oleg3479881328-code/Project-Execution-OS/blob/main/projects/website-creation/EDITOR_CREATION_STANDARD.md

Google Drive project root:

https://drive.google.com/drive/folders/15DIWML8HiLSJrNfP5r7IyZu_YkrD2GTU

## Role

Act as an independent senior architect reviewing an AI-native website production system.

Do not assume the current architecture is correct. Do not modify the project on the first pass.

Follow:

READ → RESEARCH → REVIEW → PROPOSE

not:

READ → REWRITE

## Mission

Perform a second-opinion architecture and technical review of Website Creator.

Website Creator is a global system for creating websites. It must not depend architecturally on any client project. Client work may contribute lessons only after they are generalized into universal standards/capabilities.

Review the project for:

- architecture and module boundaries;
- knowledge vs intelligence vs execution vs tooling separation;
- routing/context loading;
- reusable capability boundaries;
- canonical Site Model / platform-independent intermediate representation;
- design pipeline and anti-AI-slop quality control;
- visual editor/CMS architecture;
- SEO/AEO/content-factory architecture;
- build/deploy/release/rollback semantics;
- QA architecture;
- AI-native/agent-native execution;
- scalability to many sites;
- security/client isolation;
- build-vs-buy-vs-integrate decisions;
- technical debt, duplication and hidden coupling.

## Mandatory Internet Research

Search the current internet and official documentation for the best available solutions as of the current date.

Do not rely on model memory for time-sensitive platform capabilities.

Research strong existing solutions in categories such as:

- structured website/site models;
- visual/page editors;
- headless CMS / visual CMS;
- component/page builders;
- design-system extraction and token tooling;
- AI-native site generation;
- browser automation and QA;
- accessibility and regression testing;
- SEO/schema/indexation tooling;
- deployment/provisioning;
- analytics/observability;
- agent orchestration;
- open-source frameworks/SDKs.

Prefer official docs, official GitHub repos, engineering docs/blogs and strong production case studies.

For notable candidates classify:

USE / ADAPT / DONOR / WATCH / REJECT

with reasons.

## Existing Solution First

Before recommending custom development, check:

1. Website Creator itself.
2. PEOS reusable standards/capabilities.
3. SOFT/internal tools.
4. Mature open-source solutions.
5. Mature SaaS/API/platform solutions.
6. Custom build only for a demonstrated gap.

Operating principle: integrate proven solutions rather than rebuild commodity infrastructure.

## Questions To Answer

1. Is Website Creator structurally correct as a global system?
2. What is its weakest architectural area?
3. What single change would produce the largest improvement?
4. What are we at risk of building ourselves that existing solutions already solve better?
5. Should Website Creator have one canonical platform-independent Site Model with adapters/renderers for different execution engines?
6. Should it remain a PEOS project or develop a deeper internal operating layer of routers, capabilities, adapters, QA gates and site instances?
7. Is a `Website Creator → Site Instance` model the right abstraction for individual websites?
8. Which operations should be fully automatic, AI + deterministic validation, or human-gated?
9. What breaks at 10 / 100 / 1,000 / 10,000 sites?
10. What should Website Creator look like in 6–12 months?

## Required Output

Create an independent review, not a rewrite.

Structure:

### A. Executive conclusion
### B. What is strong and should remain
### C. Architectural problems
### D. Missing layers
### E. Current internet research findings
### F. Build vs Buy vs Integrate
### G. Proposed target architecture
### H. Proposed production pipeline
### I. Capability map
### J. Technology recommendations
### K. What to remove / simplify
### L. Migration plan
### M. Priorities: P0 / P1 / P2 / P3

For every major recommendation include:

- Problem
- Why it matters
- Current approach
- Better approach
- Existing solution available?
- Recommended action
- Expected benefit
- Complexity
- Risk
- Priority

## Important Boundary

On the first pass, do not edit Website Creator files, standards, routing or implementation.

Return findings and proposals only. Changes happen only after owner approval.