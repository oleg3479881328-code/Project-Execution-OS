# US Law Block Deep Research Report

Date: 2026-06-06
Status: completed initial research pass

## Executive Conclusion

A useful US-law block must not behave like a generic question-answering bot.

It needs six layers:

1. jurisdiction and deadline triage;
2. source hierarchy;
3. primary-source verification;
4. case-law and procedural review;
5. practical options and evidence preservation;
6. attorney escalation when risk or deadlines require it.

## Federal Primary-Source Stack

### United States Code

Use:

https://uscode.house.gov/

Use for codified general and permanent federal statutes.

When exact enacted text or historical sequence matters, also inspect the enacted law and Statutes at Large.

### GovInfo

Use:

https://www.govinfo.gov/

GovInfo is the official GPO access and preservation layer for federal publications from all three branches. Use it to preserve official PDFs and authenticated publications.

### Congress.gov

Use:

https://www.congress.gov/

Use for bills, legislative status, public-law tracking, legislative materials, nominations, and treaties.

Use the API for monitoring and automation:

https://api.congress.gov/

### eCFR

Use:

https://www.ecfr.gov/

The eCFR is useful for current and point-in-time regulation research. It is an editorial compilation updated daily. It should be checked against official CFR editions, the daily Federal Register, and the List of CFR Sections Affected when legal reliance matters.

### Federal Register

Use:

https://www.federalregister.gov/

Use for rules, proposed rules, notices, and presidential documents. Preserve and verify the official PDF on GovInfo when publication context matters.

### Regulations.gov

Use:

https://www.regulations.gov/

Use for rulemaking dockets, supporting materials, and public comments.

## Court Stack

### Supreme Court

Use:

https://www.supremecourt.gov/opinions/opinions.aspx

Use for current slip opinions and official Supreme Court materials.

### Federal Rules

Use:

https://www.uscourts.gov/rules-policies/current-rules-practice-procedure

Also check local rules, standing orders, and judge-specific procedures.

### PACER

Use:

https://pacer.uscourts.gov/

Use for official federal electronic court records and docket materials.

### CourtListener And RECAP

Use:

https://www.courtlistener.com/

CourtListener is a useful search, automation, and alert layer. Its API includes case-law access, PACER and RECAP-related data, citation lookup, citation graphs, search, and alerts.

Use:

https://www.courtlistener.com/help/api/rest/

Important boundary:

Use CourtListener to accelerate research and automation. Verify material court documents against official sources or PACER when required.

## State And Local Law

Use:

- https://www.usa.gov/state-governments
- https://www.usa.gov/agency-index

The block must identify the relevant state, territory, county, city, court, and agency before drawing conclusions.

Do not attempt to preload every state code. Create state-specific source maps only when real work justifies them.

## Commercial Research Platforms

Evaluate when professional access is available:

- Westlaw Precision and KeyCite;
- Lexis+ AI and Shepard's;
- Bloomberg Law;
- vLex Vincent AI;
- Fastcase or vLex Fastcase;
- specialized practice-area databases.

Use them for faster research, citators, broader coverage, monitoring, and professional workflows.

Do not treat AI-generated summaries as authority. Verify the cited sources.

## Help And Escalation

Use:

- Legal Services Corporation legal-aid resources: https://www.lsc.gov/about-lsc/what-legal-aid/get-legal-help
- ABA free legal help resources: https://www.americanbar.org/groups/legal_services/flh-home/flh-free-legal-help/
- state and local bar referral services;
- court self-help centers;
- public defenders and emergency services when applicable.

## Architecture Added To The Block

The block now includes:

- `BLOCK.md`
- `LEGAL_RESEARCH_PIPELINE.md`
- `SOURCE_HIERARCHY.md`
- `JURISDICTION_AND_DEADLINE_CHECKLIST.md`
- `LEGAL_AGENT_STANDARD.md`
- `ESCALATION_RULES.md`
- `TOOLS_AND_PLATFORMS.md`
- `REFERENCES.md`
- `VALIDATION_BACKLOG.md`

## Recommended Next Expansion

Do not create dozens of practice-area modules immediately.

Build narrower modules only from repeated real use.

Likely early candidates:

- immigration;
- Ohio traffic, driver licensing, and administrative procedures;
- contracts and small business;
- employment;
- housing;
- consumer finance;
- AI, privacy, and platform compliance.

## Final Recommendation

Use this block as a central legal-research and triage layer.

For every real matter:

1. run deadline and jurisdiction triage;
2. research primary sources;
3. preserve source links and date checked;
4. state uncertainty;
5. escalate when attorney review is required.
