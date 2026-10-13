---
id: decision-which-ci
type: decision
title: Which CI/CD?
status: draft
updated: 2026-10-13
tags: [ci, cd, pipelines, github-actions]
related: [guide-test, guide-release, guide-deploy]
question: Which tool should test, build and deploy every change?
default: GitHub Actions
---

# Which CI/CD?

## The question

Which tool should run tests, build images and deploy on every change?

## Decision tree

1. Where does the code live?
   - **GitHub** → go to 2.
   - **GitLab** → *GitLab CI*.
   - **Azure Repos** → *Azure DevOps Pipelines*.
   - **Elsewhere** → choose the CI built into that host, or go to 3.
2. Does the organisation already run Azure DevOps or Jenkins for all projects?
   - **Yes** → follow the standard.
   - **No** → **GitHub Actions** (default)
3. Must builds run entirely on your own servers, with full control of plugins?
   - **Yes** → *Jenkins* (self-hosted)
   - **No** → a hosted CI service.

## Options compared

| Option | Hosting | Configuration | Cloud login without secrets (OIDC) | Best for |
|---|---|---|---|---|
| **GitHub Actions** | Hosted, or self-hosted runners | YAML in the repo | Yes | Code on GitHub; most new projects |
| Azure DevOps Pipelines | Hosted, or self-hosted agents | YAML in the repo | Yes (workload identity federation) | Organisations already on Azure DevOps |
| GitLab CI | Hosted, or self-managed | YAML in the repo | Yes | Code on GitLab |
| Jenkins | Self-hosted | Groovy pipelines, plugins | Via plugins | Full control, long-established setups |
| CircleCI | Hosted | YAML | Yes | Teams wanting a dedicated CI service |

## Default and why

When the code is on GitHub, GitHub Actions keeps code, reviews, checks and deployments in one place,
links runs directly to pull requests, supports OIDC to every major cloud, and needs no server to run.

## When to revisit

- The organisation standardises on another tool.
- Build minutes or concurrency limits become a real cost; consider self-hosted runners.
- Builds need hardware or network access that hosted runners cannot provide.
