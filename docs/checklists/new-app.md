---
id: checklist-new-app
type: checklist
title: New app
status: draft
updated: 2026-10-13
tags: [start, onboarding]
related: [guide-architecture, guide-ai-agents, guide-plan, guide-code, guide-build, guide-infrastructure, guide-cost]
gate: From an empty repository to the first deployment
---

# New app

## When to use

Right after creating a repository with **Use this template**, before writing feature code.
Work top to bottom; each group unlocks the next.

## Checklist

### Repository and planning

- [ ] Repository created from the template; default branch is `main` · [Plan](../guides/01-plan.md)
- [ ] Branch protection on `main`: pull request required, status checks required · [Code](../guides/02-code.md)
- [ ] Project board created; first issues written from the spec template · [Plan](../guides/01-plan.md)
- [ ] Architecture diagram and services table committed · [Architecture](../guides/architecture.md)
- [ ] First ADR written: hosting choice · [Which hosting?](../decisions/which-hosting.md)
- [ ] Agent instruction file (`CLAUDE.md` or `AGENTS.md`) adapted to this app · [Working with AI agents](../guides/ai-agents.md)

### Local development

- [ ] App reads all settings from environment variables, with local defaults · [Code](../guides/02-code.md)
- [ ] `.env.example` committed; real `.env` ignored · [Security](../guides/security.md)
- [ ] Health endpoints `/healthz` and `/readyz` exist · [Code](../guides/02-code.md)
- [ ] Dockerfile builds; `docker compose up` runs the whole app locally · [Build](../guides/03-build.md)

### Automation

- [ ] CI runs tests, lint and dependency scan on every pull request · [Test](../guides/04-test.md)
- [ ] Image built by CI and tagged with the commit SHA · [Build](../guides/03-build.md)

### Cloud (only when ready to deploy)

- [ ] Budget alert created **before** any other resource · [Cost](../guides/cost.md)
- [ ] Remote state storage created; CI signs in with OIDC · [Infrastructure](../guides/infrastructure.md)
- [ ] Infrastructure created with Terraform, plan reviewed before apply · [Infrastructure](../guides/infrastructure.md)
- [ ] First deployment through the pipeline, not by hand · [Deploy](../guides/06-deploy.md)
- [ ] One alert reaches you · [Monitor](../guides/08-monitor.md)

## If an item fails

Stop and fix it before moving to the next group. Items later in the list assume the earlier
ones are true; skipping one usually costs more time later than it saves now.
