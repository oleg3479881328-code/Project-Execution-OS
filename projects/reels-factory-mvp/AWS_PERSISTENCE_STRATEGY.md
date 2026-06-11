# AWS Persistence Strategy — Reels Factory MVP

Date: 2026-06-11 (corrected)
Region: us-east-2 (Ohio)
Canonical instance: g5.xlarge

## Purpose

Avoid reinstalling ComfyUI and redownloading Wan model weights (~30 GB) every time a GPU instance is launched for the Reels Factory MVP smoke test.

---

## Options Comparison

### Option A: Keep Stopped Instance (Stop, Not Terminate)

| Metric | Value |
|---|---|
| **How it works** | Stop the instance instead of terminating. EBS root volume persists. Next launch: start instance. |
| **Monthly storage cost** | 100 GB gp3 x $0.08/GB = **$8.00/month** |
| **Per-restart time** | ~1 minute (start instance) |
| **Per-restart data cost** | $0 |
| **Complexity** | Very low |
| **Risk** | Easy to forget running; EBS costs $8/month regardless of use |
| **Preserves** | Everything: OS, ComfyUI, models, config |

### Option B: Detached EBS Volume

| Metric | Value |
|---|---|
| **How it works** | Terminate instance but keep the root volume. Attach to new instance on restart. |
| **Monthly storage cost** | 100 GB gp3 x $0.08/GB = **$8.00/month** |
| **Per-restart time** | ~5 min (create instance + attach volume) |
| **Per-restart data cost** | $0 |
| **Complexity** | Medium - requires manual volume attachment |
| **Risk** | Low - volume is passive |
| **Preserves** | Everything except instance-specific metadata |

### Option C: EBS Snapshot

| Metric | Value |
|---|---|
| **How it works** | Create an EBS snapshot of the root volume after setup. Create new volume from snapshot on restart. |
| **Monthly storage cost** | Snapshot ~80 GB x $0.05/GB = **$4.00/month** |
| **Per-restart time** | ~5-10 min (create volume from snapshot + attach) |
| **Per-restart data cost** | $0 (same region) |
| **Complexity** | Medium |
| **Risk** | Low - snapshot is passive |
| **Preserves** | Everything |

### Option D: Custom AMI (Recommended)

| Metric | Value |
|---|---|
| **How it works** | Create an AMI from the stopped instance. AMI is backed by EBS snapshots. Launch new instances from the AMI. |
| **Monthly storage cost** | AMI = EBS snapshot(s) of root volume. ~80 GB x $0.05/GB = **$4.00/month** (AMI itself has no separate fee) |
| **Per-restart time** | ~3-5 min (launch from AMI) |
| **Per-restart data cost** | $0 (same region) |
| **Complexity** | Low - AMI appears in EC2 launch wizard |
| **Risk** | Low - AMI is passive |
| **Preserves** | Everything including OS config, installed packages, model files |

### Option E: S3 Storage + Restore

| Metric | Value |
|---|---|
| **How it works** | Upload model files to S3. On each launch, download from S3 to instance storage. ComfyUI must be reinstalled each time. |
| **Monthly storage cost** | S3 Standard ~30 GB x $0.023/GB = **$0.69/month** |
| **Per-restart time** | ~30-60 min (download 30 GB) + ComfyUI reinstall |
| **Per-restart data cost** | **$0** - S3 to EC2 data transfer within the same AWS region is free (no internet egress charge) |
| **Complexity** | High - requires S3 bucket, IAM role, download script, ComfyUI reinstall |
| **Risk** | Low |
| **Preserves** | Model files only. ComfyUI + deps must be reinstalled each time |

---

## Pricing Summary (us-east-2)

| Option | Monthly Storage | Per-Restart Time | Per-Restart Data Cost | First Month Total |
|---|---|---|---|---|
| A: Keep Stopped Instance | **$8.00** | ~1 min | $0 | **$8.00** |
| B: Detached EBS Volume | **$8.00** | ~5 min | $0 | **$8.00** |
| C: EBS Snapshot | **$4.00** | ~5-10 min | $0 | **$4.00** |
| **D: Custom AMI** | **$4.00** | **~3-5 min** | **$0** | **$4.00** |
| E: S3 Restore | $0.69 | ~30-60 min | $0 (same-region) | $0.69 |

### Pricing Sources

- **EBS gp3:** $0.08/GB/month - https://aws.amazon.com/ebs/pricing/
- **EBS Snapshots:** $0.05/GB/month - https://aws.amazon.com/ebs/pricing/
- **AMI storage:** No separate fee. AMI is backed by EBS snapshots; you pay only for the snapshot storage at $0.05/GB/month.
- **S3 Standard:** $0.023/GB/month - https://aws.amazon.com/s3/pricing/
- **S3 to EC2 data transfer (same region):** Free. No internet egress charge. Verified: https://aws.amazon.com/s3/pricing/ (Data Transfer section: "Data transferred between AWS services in the same AWS Region is free.")

---

## Recommendation

### Primary: Option D - Custom AMI

**Why:** Best balance of cost ($4/month), restart speed (3-5 min), and simplicity. The AMI preserves the entire OS state. Launching from an AMI is a standard AWS workflow with no manual volume attachment.

**Cost note:** The AMI itself has no separate fee. You pay only for the underlying EBS snapshots (~80 GB x $0.05/GB = $4/month).

### Fallback: Option C - EBS Snapshot

**Why:** Same cost as AMI ($4/month). Use this if you want to keep the snapshot separate from the AMI registry, or if you need to attach the volume to a different instance type in the future.

### When to use Option A (Keep Stopped) instead:
- If the gap between tests is short (days, not weeks)
- If $8/month is acceptable for instant restart (~1 min)
- If you want to avoid any setup steps between tests

---

## One-Time AMI Creation Workflow

Run these commands after the next successful smoke test setup (ComfyUI + models installed):

```bash
# 1. Stop the instance
aws ec2 stop-instances --instance-ids i-xxxxxxxx --region us-east-2
aws ec2 wait instance-stopped --instance-ids i-xxxxxxxx --region us-east-2

# 2. Create the AMI (this also creates the backing EBS snapshots)
aws ec2 create-image --instance-id i-xxxxxxxx --name "reels-factory-smoke-test-ami" --description "Reels Factory MVP: ComfyUI + Wan2.1-I2V-14B-480P" --region us-east-2

# 3. Wait until the AMI is available before terminating the source instance
aws ec2 wait image-available --image-ids ami-xxxxxxxx --region us-east-2

# 4. Verify the AMI and snapshot
aws ec2 describe-images --image-ids ami-xxxxxxxx --region us-east-2
aws ec2 describe-snapshots --filters "Name=description,Values=*reels-factory-smoke-test-ami*" --region us-east-2

# 5. Terminate the temporary GPU instance (no longer needed)
aws ec2 terminate-instances --instance-ids i-xxxxxxxx --region us-east-2
```

## Restart Workflow (from AMI)

```bash
# 1. Launch new instance from the AMI
aws ec2 run-instances --image-id ami-xxxxxxxx --instance-type g5.xlarge --key-name reels-factory-smoke-key --security-group-ids sg-xxxxxxxx --block-device-mappings "[{\"DeviceName\":\"/dev/sda1\",\"Ebs\":{\"VolumeSize\":100,\"VolumeType\":\"gp3\",\"DeleteOnTermination\":true}}]" --region us-east-2

# 2. SSH in with tunnel and start ComfyUI on localhost only
ssh -i reels-factory-smoke-key.pem -L 8188:localhost:8188 ubuntu@<IP>
# In the SSH session:
cd ~/ComfyUI && source venv/bin/activate && python main.py --listen 127.0.0.1 --port 8188

# 3. Open http://localhost:8188 in your browser (traffic goes through SSH tunnel)
#    Generate and download output

# 4. Terminate after test (volume auto-deletes with DeleteOnTermination=true)
aws ec2 terminate-instances --instance-ids i-xxxxxxxx --region us-east-2
```

## Cleanup After Restart

- The EBS volume is created fresh from the AMI each time
- With DeleteOnTermination=true, the volume is automatically deleted when the instance is terminated
- No orphaned volumes remain
- The AMI and its backing snapshots persist for future use

## Fallback Decision Rule

| Situation | Recommended Option |
|---|---|
| First test, no AMI exists yet | A: Keep Stopped (or just launch fresh) |
| Gap between tests < 1 week | A: Keep Stopped ($8/month, instant restart) |
| Gap between tests > 1 week | D: Custom AMI ($4/month, 3-5 min restart) |
| Need to change instance type | C: EBS Snapshot (attach to any instance) |
| Budget is critical, time is not | E: S3 Restore ($0.69/month, slow restart) |

## What Should Remain Stopped vs Stored

| Resource | Between Tests | Stored? | Cost |
|---|---|---|---|
| GPU instance (g5.xlarge) | **Terminated** | No | $0 |
| EBS root volume | **Deleted** (with instance) | No | $0 |
| Custom AMI | **Stored** | Yes | $4/month (snapshot cost) |
| EBS snapshots | **Stored** (if used) | Yes | $4/month |
| S3 bucket | **Stored** (if used) | Yes | $0.69/month |
| Security group | **Stored** | Yes | Free |
| Key pair | **Stored** | Yes | Free |
| SSH key (.pem file) | **Stored locally** | Yes | Free |

## Remaining Unknowns

1. **AMI creation time** - depends on root volume size (100 GB). Estimate ~10 minutes.
2. **First launch from AMI** - may be slightly slower while AWS caches the AMI.
3. **Model compatibility** - if the Wan model or ComfyUI version changes, a new AMI must be created.
4. **Actual snapshot size** - the billed snapshot size may be less than 80 GB due to compression and empty blocks.
