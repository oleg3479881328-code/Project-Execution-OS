# Cost & Runtime Tracking Template — Reels Factory MVP Smoke Test

Date: _______________
Instance ID: _______________
Instance Type: g4dn.xlarge
Region: us-east-2

---

## Setup Phase

| Metric | Value |
|---|---|
| Instance launch time | _______________ |
| SSH first connected | _______________ |
| ComfyUI install completed | _______________ |
| Model download started | _______________ |
| Model download completed | _______________ |
| **Total setup time** | _______________ |

## Generation Phase

| Metric | Value |
|---|---|
| Input image prepared | _______________ |
| Generation started | _______________ |
| Generation completed | _______________ |
| **Generation time** | _______________ |
| Number of retries | _______________ |
| Retry reasons | _______________ |

## Output

| Metric | Value |
|---|---|
| Output file size | _______________ |
| Output resolution | _______________ |
| Output duration (seconds) | _______________ |
| Output quality assessment | _______________ |
| Was output usable? | Yes / No / Partial |

## Runtime & Cost

| Metric | Value |
|---|---|
| Instance launch time | _______________ |
| Instance terminate time | _______________ |
| **Total runtime** | _______________ |
| Compute cost (hours × $0.526) | $_______________ |
| EBS cost (hours × $0.0033) | $_______________ |
| IPv4 cost (hours × $0.005) | $_______________ |
| **Total estimated cost** | $_______________ |
| AWS credits consumed | $_______________ |
| Remaining credits after test | $_______________ |

## Charges After Termination

| Resource | Charged? | Amount |
|---|---|---|
| EBS root volume | Yes / No | $_______________ |
| Snapshots | Yes / No | $_______________ |
| Elastic IP | Yes / No | $_______________ |
| Other | Yes / No | $_______________ |

## Notes

- What went well: _______________
- What went wrong: _______________
- What to improve next time: _______________
- Should we continue with AWS or switch to RunPod? _______________

---

## Summary

| Metric | Value |
|---|---|
| Total setup time | _______________ |
| Total generation time | _______________ |
| Total runtime | _______________ |
| Total cost | $_______________ |
| Output quality | _______________ |
| AWS or RunPod next? | _______________ |
