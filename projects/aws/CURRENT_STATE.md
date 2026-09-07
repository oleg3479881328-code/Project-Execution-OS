# AWS — Current State

Last updated: 2026-09-06

## Account / Region / Credits

- AWS account ID: `102885960265`
- Primary region: `us-east-2` (Ohio)
- Account plan preflight reported by Codex: `PAID / ACTIVE`
- AWS credits / account-plan balance reported after workstation validation: `$60`
- Current month cost at the earlier capture point: `$0.00`
- Forecast shown at that earlier capture point: approximately `$0.12`
- `Days remaining` widget was unable to load in Console Home.
- October 4, 2026 was confirmed as the completion deadline for the Bedrock Explore AWS reward activity; do not treat that date as the Free Plan expiration date without separate account-plan evidence.

## Explore AWS Rewards

Reward program state reached `$100 of $100 earned` in aggregate after completing the remaining activities; credits visible afterward were `$60.00`.

Completed reward activities:
- Launch an instance using EC2 — completed previously.
- Set up a cost budget using AWS Budgets — completed previously.
- Create a web app using AWS Lambda — completed on 2026-09-06; Function URL returned HTTP 200 and temporary resources were removed.
- Create an Aurora or RDS database — completed on 2026-09-06; temporary PostgreSQL `db.t3.micro` reached `Available` and was removed without snapshot.
- Use a foundation model in Amazon Bedrock playground — completed manually in Bedrock Playground using Amazon Nova Micro after API-only invocation did not satisfy the UI reward activity.

Execution evidence for the temporary reward resources is recorded in:
https://github.com/oleg3479881328-code/AI-Coordination-Hub/issues/4

## Olga Polo Remote Workstation

Purpose: provide a familiar remote Windows/browser environment with fast datacenter internet so large Olga Polo project transfers can run between PassGallery, Wix, Google Drive, GitHub/Vercel, etc., without bulk files passing through the user's local internet connection.

### EC2

- Instance name: `OlgaPolo-Remote-Worker`
- Instance ID: `i-0da38674cc948742c`
- AMI: `ami-0a6027e5bf7199725`
- OS: official AWS Windows Server 2022 Base
- Instance type: `t3.medium`
- Root storage: `100 GiB gp3`, encrypted
- Public networking: dynamic public IPv4 while running
- Elastic IP: none
- Instance-initiated shutdown behavior: `stop`
- AWS Security Group inbound rules: none
- Dedicated SSM role/profile used for remote management
- Dedicated EC2 key pair created; private PEM is stored locally outside repositories and must never be committed or pasted into chat/issues.
- Final validated state on 2026-09-06: `stopped`.

### Tailscale / Remote Access

Canonical console:
https://console.tailscale.com/admin/machines

Tailnet/account used during setup:
`oleg3479881328@gmail.com`

Known machines:
- Local laptop: `victus` — Tailscale IPv4 `100.94.62.103`
- AWS Windows server: `EC2AMAZ-2EIN5F9` — Tailscale IPv4 `100.81.114.123`

Validated behavior:
- Remote Windows is authenticated to the same tailnet.
- Tailscale runs unattended on the AWS Windows server.
- Full EC2 `stop` / `start` validation completed successfully.
- After a full stop/start, Tailscale automatically reconnected without requiring a new interactive login.
- The remote Tailscale address remained `100.81.114.123` after the stop/start test.

Security design:
- Do not expose TCP 3389 publicly.
- AWS Security Group remains with no inbound rules.
- Windows RDP firewall scope is restricted to Tailscale range `100.64.0.0/10`.
- RDP target is the Tailscale/private address `100.81.114.123`, not the EC2 public IP.
- This allows access from any physical network/location as long as the user's device is authenticated to the Tailscale tailnet.

### Owner UX Target

Normal operation must require one owner-facing action only:
- desktop shortcut / launcher: `OLGA POLO — AWS PC`

Launcher target behavior:
1. Verify local AWS CLI/authentication and local Tailscale availability.
2. Start `OlgaPolo-Remote-Worker` if stopped.
3. Wait for AWS/Windows/Tailscale readiness.
4. Resolve/use the remote Tailscale address.
5. Open RDP automatically through Tailscale.
6. After the RDP session closes, offer to stop the EC2 instance immediately.
7. Leave the machine stopped when not needed.

### Auto-stop Policy

- Preferred inactivity shutdown: approximately 2 hours of real inactivity.
- Do not stop merely because the RDP window disconnected if a large transfer is still active.
- Keep a 12-hour maximum-runtime hard cap only as a safety fallback.
- Owner preference: better to start the machine again than pay for long idle periods.

## Software Target On Remote Windows

- Google Chrome
- Google Drive for desktop, intended in Stream files mode after owner sign-in
- 7-Zip
- Olga Polo transfer folder: `C:\OlgaPolo-Transfer\Downloads`

Provisioning rule:
- unattended setup may install/configure software and infrastructure;
- do not enter or store Google/Wix/PassGallery credentials during infrastructure provisioning;
- owner signs into those services separately when needed.

## Execution / Validation Report

Canonical execution task:
https://github.com/oleg3479881328-code/AI-Coordination-Hub/issues/3

Final report:
https://github.com/oleg3479881328-code/AI-Coordination-Hub/issues/3#issuecomment-5563266466

Validated final state reported on 2026-09-06:
- EC2 left `stopped`;
- unattended Tailscale confirmed across full stop/start cycle;
- no repeated Tailscale login required;
- RDP available only via Tailscale/private overlay;
- no public RDP exposure;
- AWS Security Group has no inbound rules;
- account-plan / credits balance reported as `$60`.

## Previous Cleanup Context

Before this workstation project, the AWS account had been intentionally cleaned of old EC2/EBS/snapshots/AMI/Elastic IP resources on 2026-08-15. Do not resurrect old resources. Keep the new workstation narrowly scoped and cost-controlled.
