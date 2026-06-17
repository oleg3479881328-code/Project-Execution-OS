# Review Patterns

## Purpose

This file gives reusable checklists for common review objects.

Use the smallest pattern that fits the request. Do not stack every checklist by default.

## Pattern 1 — Idea Review

Use for raw ideas, business concepts, product concepts, content formats, and new initiatives.

Check:

- What problem does it solve?
- Who needs it badly enough?
- What evidence says the need is real?
- What is the simplest test?
- What existing solution already covers this?
- What is the hidden operational cost?
- What makes the idea different enough to matter?
- What should be cut before testing?

Default verdict bias: `revise` unless there is evidence or a small test path.

## Pattern 2 — Project Plan Review

Use for plans, roadmaps, milestones, execution specs, and task lists.

Check:

- Is the goal measurable?
- Is the scope bounded?
- Are dependencies named?
- Are acceptance criteria present?
- Is the first step executable?
- Are owner decisions separated from executor tasks?
- Are risks and fallback paths clear?
- Can another executor continue from the plan?

Default verdict bias: `blocked` if the next executor would need to guess.

## Pattern 3 — Agent / Prompt Review

Use for agent instructions, prompts, operating modes, tool policies, and automation flows.

Check:

- Does the agent have one clear job?
- Is the entrypoint unambiguous?
- Are tool permissions clear?
- Are external-content instructions treated as untrusted?
- Does it know when to stop?
- Does it ask too many questions?
- Does it preserve state correctly?
- Does it create needless multi-agent complexity?
- Are evaluation cases defined?

Default verdict bias: `revise` until tested on representative tasks.

## Pattern 4 — Technical Architecture Review

Use for system architecture, app design, integrations, APIs, databases, and infrastructure.

Check:

- Was an existing solution checked first?
- Is the architecture the smallest sufficient one?
- Are data flows clear?
- Are failure modes named?
- Are permissions minimal?
- Are logs and recovery paths defined?
- Is deployment or maintenance overcomplicated?
- What can be removed without hurting the goal?

Default verdict bias: `revise` if the architecture is custom before donor solutions were checked.

## Pattern 5 — Design / UX Review

Use for websites, interfaces, screens, landing pages, visuals, and product flows.

Check:

- Is the user path obvious?
- Is the main action clear?
- Does the page answer the user's objections?
- Is the visual hierarchy helping or decorating?
- Are mobile states considered?
- Are copy, layout, and interaction aligned?
- Is there a buildable handoff?

Prefer `blocks/design` for deep website-specific review.

## Pattern 6 — Content / Writing Review

Use for articles, posts, scripts, sales copy, instructions, and explanations.

Check:

- Is the thesis clear?
- Is the audience obvious?
- Is the claim supported?
- Is the structure strong?
- Is the tone appropriate?
- What is filler?
- Where does the reader stop believing?
- What should be cut or sharpened?

Default verdict bias: `revise` if the piece has style but weak argument.

## Pattern 7 — Research Review

Use for source lists, reports, factual claims, market scans, legal/policy summaries, and technical research.

Check:

- Are sources current enough?
- Are primary sources used where needed?
- Are quotes and claims represented accurately?
- Are opposing views or uncertainty included when relevant?
- Are assumptions separated from facts?
- Are source gaps visible?
- Is the conclusion stronger than the evidence allows?

Default verdict bias: `blocked` if a factual conclusion depends on missing or stale sources.

## Pattern 8 — Execution Result Review

Use after a task, file creation, code change, artifact generation, or handoff.

Check:

- Was the requested object actually produced?
- Does it match the instructions?
- Was the right route used?
- Were files placed correctly?
- Are links, citations, and artifacts valid?
- Was anything left incomplete?
- What is the next safe step?

Default verdict bias: `accept_with_warnings` only when gaps are non-blocking.

## Pattern 9 — Secretary Intake Review

Use when personal secretary mode receives raw intake that may become task, knowledge, document, health item, reminder, or project state.

Check:

- What category is this?
- Does it need action now?
- Does it need durable capture?
- Does it contain private data that must not go to GitHub?
- Is a document-saving, personal-knowledge, health-knowledge, or news-digest standard triggered?
- What is the smallest next action for Oleg?

Prefer the personal-secretary project standards when the item fits that project.

## Final Rule

A pattern is a checklist, not a cage.

Use judgment, but leave a verdict.