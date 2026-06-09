# Validation Backlog

## Purpose

Separate researched recommendations from workflows validated in practice.

## Priority 1: Provider Research

- compare US and international GPU-rental providers;
- compare mainland China providers;
- compare Hong Kong options;
- compare low-cost marketplaces, serverless GPU providers, and major clouds;
- record date, region, GPU, VRAM, hourly rate, billing granularity, storage, egress, stop behavior, and payment restrictions;
- identify providers usable from the United States without local payment friction.

## Priority 2: Video Generation Economics

- select representative open-source video models;
- record official hardware requirements and licenses;
- deploy one model on a rented GPU;
- measure cold start, warm start, generation time, output duration, storage, and cost per generated minute;
- compare SaaS, provider API, and rented-GPU execution on the same workload definition.

## Priority 3: Open-Source LLM Endpoint

- choose one useful open-source model that exceeds local-laptop constraints;
- deploy on rented compute;
- expose a private authenticated endpoint;
- route lightweight agent tasks to it;
- measure cost per useful task against DeepSeek API and premium APIs;
- test stop, resume, and model swap procedures.

## Priority 4: Hybrid Control Layer

- test a cheap always-on VPS;
- add queue and worker lifecycle control;
- start temporary GPU workers on demand;
- shut workers down after queue completion;
- collect per-job cost logs;
- confirm persistent-storage behavior.

## Priority 5: China Research Node

- verify mainland China provider signup from a US-based owner;
- verify identity and payment requirements;
- test browser-based research through a mainland IP;
- compare mainland China and Hong Kong visibility for Baidu, Bilibili, Gitee, and local services;
- document compliance constraints before any public hosting.

## Open Questions

- Which provider has the best real price for intermittent GPU workloads?
- Which provider has the best persistent-volume economics for large model weights?
- When is serverless GPU cheaper than a persistent endpoint?
- Which open-source video models are commercially usable?
- Which GPU profiles minimize cost per generated minute for each model?
- Which open-source LLM endpoint offers the best savings layer for Project Execution OS?

## Status

No provider, price, or deployment pattern should be treated as validated until it is checked against current official sources and tested where material.
