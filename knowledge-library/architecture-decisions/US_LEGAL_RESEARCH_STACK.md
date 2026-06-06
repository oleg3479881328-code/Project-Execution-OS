# US Legal Research Stack

Type: `architecture-decision`
Lifecycle status: `candidate`
Captured: 2026-06-06
Review status: researched and preserved; not yet active system guidance

## Problem

United States legal questions cannot be answered safely from memory, a single search result, or a generic AI summary.

A reusable legal-research capability needs:

- jurisdiction identification;
- deadline and urgency triage;
- primary-source research;
- source-status verification;
- case-law and procedural review;
- practical options;
- evidence preservation;
- attorney escalation when required.

## Reusable Architecture Pattern

Use this workflow:

```text
facts
  -> dates
  -> urgency and deadline check
  -> jurisdiction
  -> issue classification
  -> primary-source search
  -> source-status verification
  -> case-law and procedure review
  -> secondary explanation
  -> practical options
  -> uncertainty statement
  -> attorney-escalation decision
  -> evidence package
```

## Applies To

Load this entry when work involves:

- U.S. federal law;
- state, territory, county, city, or municipal law;
- statutes;
- regulations;
- court opinions;
- court rules;
- agency procedure;
- legal deadlines;
- document review for a legal issue;
- preparation for an attorney consultation;
- legal-source automation.

## Triggers

Relevant triggers include:

- legal problem;
- law or regulation;
- lawsuit;
- court notice;
- immigration issue;
- arrest or police contact;
- eviction;
- contract dispute;
- employment termination;
- government agency notice;
- deadline;
- appeal;
- subpoena;
- legal research;
- find a lawyer;
- prepare for a lawyer.

## Do Not Load When

Do not load this entry for:

- casual non-legal discussion;
- ordinary business planning with no legal issue;
- purely historical discussion where current law is irrelevant;
- legal conclusions that should be made by a licensed attorney after full review.

## Federal Source Pattern

### Statutes

Use:

- United States Code: https://uscode.house.gov/
- GovInfo: https://www.govinfo.gov/
- Congress.gov: https://www.congress.gov/
- Congress.gov API: https://api.congress.gov/

Use Statutes at Large or enacted-law text when exact enacted language or historical sequence matters.

### Regulations

Use:

- eCFR: https://www.ecfr.gov/
- Federal Register: https://www.federalregister.gov/
- Regulations.gov: https://www.regulations.gov/
- GovInfo official publications: https://www.govinfo.gov/

Important distinction:

- eCFR is useful and updated daily;
- eCFR is an editorial compilation and should be checked against official publications when legal reliance matters.

### Courts

Use:

- Supreme Court opinions: https://www.supremecourt.gov/opinions/opinions.aspx
- federal rules: https://www.uscourts.gov/rules-policies/current-rules-practice-procedure
- PACER: https://pacer.uscourts.gov/
- CourtListener: https://www.courtlistener.com/
- CourtListener API: https://www.courtlistener.com/help/api/rest/

CourtListener is useful for research, alerts, citation checks, and automation. Verify material filings or opinions through official court sources or PACER when required.

### State And Local Sources

Use:

- USAGov state directory: https://www.usa.gov/state-governments
- USAGov agency directory: https://www.usa.gov/agency-index

Create state-specific source maps only when active work justifies them.

## Escalation Boundary

Escalate immediately when the matter may involve:

- arrest, detention, criminal charges, or police questioning;
- immigration detention, removal, status, interview, or travel risk;
- court summons, hearing, appeal, filing, or discovery deadlines;
- eviction, foreclosure, repossession, custody, domestic violence, or safety risk;
- tax levy, wage garnishment, benefits termination, license suspension, or major financial exposure;
- any situation where a missed deadline may permanently reduce rights.

## Evidence Package

For every legal-research matter preserve:

- question presented;
- facts relied on;
- missing facts;
- jurisdiction;
- dates and deadlines;
- primary authorities;
- source URLs;
- date checked;
- document copies or screenshots when useful;
- uncertainty;
- practical options;
- escalation recommendation.

## Adaptation Notes

Use the smallest relevant research path.

Do not preload every legal domain or every state code.

Create narrower reusable skills only after repeated real work demonstrates the need.

Likely early practice-area candidates:

- immigration;
- Ohio traffic and driver licensing;
- contracts and small business;
- employment;
- housing;
- consumer finance;
- AI, privacy, and platform compliance.

## Validation Still Required

This entry remains `candidate` until real matters validate:

- federal-source retrieval paths;
- point-in-time regulatory research;
- official PDF preservation;
- case citation treatment checks;
- state-specific source maps;
- CourtListener and other API automation;
- professional-platform workflows when access becomes available.

## Related Artifacts

- `blocks/us-law/BLOCK.md`
- `blocks/us-law/LEGAL_RESEARCH_PIPELINE.md`
- `blocks/us-law/SOURCE_HIERARCHY.md`
- `blocks/us-law/JURISDICTION_AND_DEADLINE_CHECKLIST.md`
- `blocks/us-law/LEGAL_AGENT_STANDARD.md`
- `blocks/us-law/ESCALATION_RULES.md`
- `blocks/us-law/TOOLS_AND_PLATFORMS.md`
- `blocks/us-law/REFERENCES.md`
- `blocks/us-law/VALIDATION_BACKLOG.md`
- `blocks/us-law/RESEARCH_REPORT_2026-06-06.md`

## Related Standards

- `docs/KNOWLEDGE_SYSTEM.md`
- `docs/AUTOMATIC_CAPTURE_STANDARD.md`
- `docs/RESEARCH_STANDARD.md`
- `blocks/us-law/BLOCK.md`

## Final Rule

Research the controlling law, verify currency, state uncertainty, preserve evidence, and escalate when the stakes require a licensed attorney.