# AWS-First VPS Route

## Purpose

Use existing AWS budget before adding new providers.

This route is intentionally narrow: start with one low-cost VPS-like control node in AWS, validate remote access, and only then add GPU workloads.

## Decision

Use AWS as the first implementation environment because the owner already has subscription value or credits there.

Do not begin with GPU infrastructure.

Begin with a small always-on control node.

## Recommended First Runtime

Use one EC2 instance as the head node.

Initial profile:

- service: Amazon EC2;
- operating system: Ubuntu LTS;
- architecture: x86_64 for maximum compatibility;
- instance class: burstable general-purpose;
- starting size: `t3.small` or similar;
- disk: 20-30 GB gp3 EBS;
- network: public IPv4 only if needed;
- SSH key-based access;
- security group restricted to SSH from the owner's IP when practical.

## Why Not Lightsail First

Lightsail is simpler, but EC2 is the better long-term donor for Project Execution OS because it integrates naturally with:

- IAM;
- EBS;
- S3;
- CloudWatch;
- Systems Manager;
- future GPU instances;
- automation APIs;
- lifecycle control.

Lightsail remains a fallback when simplicity matters more than future extensibility.

## Initial Responsibilities Of The Head Node

Phase 1 only:

- remote SSH access;
- Docker;
- Docker Compose;
- small control services;
- test API endpoint;
- logs;
- future queue and orchestrator host.

Do not install heavy AI models on the head node.

## Minimal Phase 1 Stack

- Ubuntu LTS
- Docker
- Docker Compose
- Git
- Python 3
- curl
- jq
- tmux
- optional Caddy or Nginx later

## Security Baseline

- SSH key authentication;
- no password SSH login when practical;
- restrict inbound ports;
- do not expose Docker daemon publicly;
- do not store secrets in repository files;
- keep AWS credentials outside the server image;
- enable basic logging;
- tag the instance clearly;
- set a billing alert.

## Naming

Suggested EC2 instance name:

`peos-head-node`

Suggested security group:

`peos-head-node-sg`

Suggested key pair:

`peos-head-node-key`

## Next Route After Validation

Once SSH access and Docker are validated:

1. add S3 bucket or compatible object storage;
2. deploy a small health endpoint;
3. add cost logging;
4. test one GPU workload separately;
5. decide whether GPU should run on AWS, RunPod, Vast.ai, or another provider.

## Important Boundary

Existing AWS credits justify starting in AWS.

They do not imply that AWS must remain the cheapest GPU provider.

Use AWS first for the control plane. Compare GPU providers separately after the head node is running.
