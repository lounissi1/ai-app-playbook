---
id: decision-which-hosting
type: decision
title: Which hosting?
status: draft
updated: 2026-10-13
tags: [hosting, containers, kubernetes, serverless]
related: [card-container-image, guide-deploy, guide-operate, decision-which-iac]
question: Where should my application's code run?
default: Managed container platform
---

# Which hosting?

## The question

Where should the application's code run, given how much operational work you can take on?

## Decision tree

1. Is the application already packaged as containers, or easy to package?
   - **No** → Is it a single, conventional web app? **Yes** → *Platform-as-a-service web app*. **No** → package it first.
   - **Yes** → go to 2.
2. Is it mostly small, event-driven functions that run briefly?
   - **Yes** → *Serverless functions*
   - **No** → go to 3.
3. Do you need direct control of the orchestrator: custom operators, special node pools (for example GPUs), service mesh, or a platform team serving many apps?
   - **Yes** → *Managed Kubernetes*
   - **No** → go to 4.
4. Does the software need a full operating system you manage (legacy software, special drivers)?
   - **Yes** → *Virtual machines*
   - **No** → **Managed container platform** (default)

## Options compared

| Option | You manage | Scale to zero | Ops effort | Best for | Azure | AWS | Google Cloud |
|---|---|---|---|---|---|---|---|
| Virtual machines | OS, patches, runtime, app | No | Very high | Legacy, full control | Virtual Machines | EC2 | Compute Engine |
| Managed Kubernetes | Cluster config, nodes, manifests | Not the nodes | High | Many teams, custom platform needs | AKS | EKS | GKE |
| PaaS web app | App and settings | Usually no | Low | One conventional web app or API | App Service | Elastic Beanstalk | App Engine |
| **Managed container platform** | Images and scale rules | **Yes** | **Low** | **Several containers with different load shapes, workers, jobs** | **Container Apps** | **ECS on Fargate, App Runner** | **Cloud Run** |
| Serverless functions | Single functions | Yes | Lowest | Small event handlers, glue code | Functions | Lambda | Cloud Functions |

## Default and why

A managed container platform gives the core orchestration features (replicas, health probes,
autoscaling, revisions, jobs) without operating a cluster. It scales to zero, so small projects
cost little, and it runs the same images you build for local development.

## When to revisit

- You need Kubernetes APIs, operators or custom networking the platform does not expose.
- A platform team will serve many applications and wants one shared cluster.
- Workloads need specialised hardware or very long-running stateful processes.
- Steady, high traffic where reserved capacity would be cheaper than per-second billing.
