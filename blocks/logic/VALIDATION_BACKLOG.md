# Logic Block Validation Backlog

## Purpose

Track which reusable logic workflows still need testing before they become stable system behavior.

## Candidate Validation Tasks

### 1. Sequence vs causation explanation

Test whether the block helps an agent clearly distinguish time order from cause and result.

Acceptance check:

- answer uses plain examples;
- answer does not overclaim causation;
- answer names the reasoning error when useful;
- English definitions include Russian translation when English terms are introduced.

### 2. Argument map output

Test whether an agent can turn a messy claim into:

- claim;
- premises;
- hidden assumptions;
- evidence;
- inference;
- conclusion;
- weak points;
- stronger version.

Acceptance check:

- map is useful without becoming academic noise;
- missing evidence is clearly separated from falsehood;
- confidence is stated honestly.

### 3. Project decision review

Test whether the block improves project decisions by checking:

- goal;
- assumptions;
- evidence;
- alternatives;
- risks;
- testable next step.

Acceptance check:

- does not replace the project workflow;
- does not create a new project by itself;
- gives a concrete decision aid.

### 4. Reasoning error detection

Test a compact review for common reasoning mistakes:

- confusing sequence with cause;
- presenting only two options when more may exist;
- using a claim as its own proof;
- weakening the opposing claim before answering it;
- replacing evidence with pressure or emotion;
- generalizing too broadly;
- making a conclusion stronger than the evidence allows.

Acceptance check:

- labels are used only when helpful;
- explanation is plain-language first;
- correction is practical.

### 5. Agent-output reasoning review

Test whether the block can review another agent's answer for:

- unsupported claims;
- hidden assumptions;
- stale facts presented as current;
- domain evidence missing;
- conclusion stronger than sources allow.

Acceptance check:

- review is direct;
- review does not invent missing facts;
- review tells what evidence is needed next.

## Current Status

`not_validated`

The block is created as a candidate reusable domain layer. It should remain candidate until several real conversations or project reviews prove the workflows are useful.
