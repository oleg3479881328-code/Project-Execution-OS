# AWS Persistence Strategy — Reels Factory MVP

Date: 2026-06-11
Region: us-east-2 (Ohio)
Canonical instance: g5.xlarge

## Purpose

Avoid reinstalling ComfyUI and redownloading Wan model weights (~30 GB) every time a GPU instance is launched.

## Options Comparison

### A: Keep EBS (Stop)
- Monthly: **$8.00** (100 GB gp3)
- Restart: ~1 min
- Preserves everything
- Risk: easy to forget running

### B: EBS Snapshot
- Monthly: **$4.00** (~80 GB snapshot)
- Restart: ~5-10 min
- Preserves everything

### C: Custom AMI (Recommended)
- Monthly: **$4.00** (EBS snapshot-backed)
- Restart: ~3-5 min
- Preserves everything including OS config
- Simplest launch workflow

### D: S3 Restore
- Monthly: **$0.69** + $2.70/restart egress
- Restart: ~30-60 min
- Only preserves model files, not ComfyUI

## Recommendation: Custom AMI

Best balance of cost ($4/month), speed (3-5 min), and simplicity.

## Restart Workflow

1. Create AMI once after setup: `aws ec2 create-image`
2. Launch from AMI each test: `aws ec2 run-instances --image-id ami-xxx`
3. Start ComfyUI, generate, download
4. Terminate after test

## What Stays Stopped vs Stored

| Resource | State | Cost |
|---|---|---|
| GPU instance | Terminated | $0 |
| EBS volume | Deleted | $0 |
| Custom AMI | Stored | $4/month |
| Security group | Stored | Free |
| Key pair | Stored | Free |
