---
id: checklist-production-ready
type: checklist
title: Production ready
status: draft
updated: 2026-10-13
tags: [production, gate, review]
related: [guide-deploy, guide-operate, guide-monitor, guide-security, card-reference-architecture, card-ai-evaluation]
gate: Before real users depend on the application
---

# Production ready

## When to use

Before the first public launch, and again after any major architecture change.
The **minimum** section applies to every application. The **enterprise** section lists what
larger organisations add; for a small project you may skip these on purpose, but be able to
explain each one.

## Checklist

### Minimum: code and delivery

- [ ] Every change goes through a reviewed pull request · [Code](../guides/02-code.md)
- [ ] CI tests, lints and scans dependencies on every pull request · [Test](../guides/04-test.md)
- [ ] One immutable image per version, built by CI, tagged by commit · [Container image](../cards/container-image.md)
- [ ] Database migrations run automatically before each deploy · [Deploy](../guides/06-deploy.md)
- [ ] Rollback to the previous version tested and takes minutes · [Deploy](../guides/06-deploy.md)

### Minimum: runtime

- [ ] Served over HTTPS · [Deploy](../guides/06-deploy.md)
- [ ] Health checks configured; unhealthy instances restart automatically · [Operate](../guides/07-operate.md)
- [ ] Nothing important stored on container disk · [Operate](../guides/07-operate.md)

### Minimum: data

- [ ] Managed database with automatic backups · [Operate](../guides/07-operate.md)
- [ ] A backup restore has been tested at least once · [Operate](../guides/07-operate.md)
- [ ] Files in object storage, not on disk · [Operate](../guides/07-operate.md)

### Minimum: security

- [ ] No secrets in code, images, config files or CI variables in plain text · [Security](../guides/security.md)
- [ ] Applications use managed identities; CI uses OIDC · [Security](../guides/security.md)
- [ ] Least-privilege roles, scoped to the resources they need · [Security](../guides/security.md)

### Minimum: infrastructure, monitoring, cost

- [ ] All resources defined in Terraform; destroy-and-rebuild done once · [Infrastructure](../guides/infrastructure.md)
- [ ] Logs, traces and at least one alert that reaches a person · [Monitor](../guides/08-monitor.md)
- [ ] Budget alert and tags on every resource · [Cost](../guides/cost.md)

### Minimum: AI features (if the app uses models)

- [ ] Model versions pinned; provider reached through one internal client · [Model serving](../cards/model-serving.md)
- [ ] Timeouts, token limits and a budget alert on model calls · [Model serving](../cards/model-serving.md)
- [ ] Same embedding model and version for indexing and querying, checked in CI · [Embeddings](../cards/embeddings-vector-search.md)
- [ ] Retrieval filtered by user permissions; retrieved text treated as data · [RAG](../cards/rag.md)
- [ ] Versioned evaluation set runs in CI and blocks regressions · [AI evaluation](../cards/ai-evaluation.md)

### Enterprise extras (know and explain)

- [ ] Separate dev, test and prod environments; the same image promoted through each
- [ ] Approval gate before production
- [ ] Landing zone with policies (allowed regions, required tags)
- [ ] Private networking for data services
- [ ] High availability across zones; database standby
- [ ] Written and tested disaster recovery plan
- [ ] Web application firewall at the edge
- [ ] On-call rota, runbooks and blameless postmortems
- [ ] Privacy and audit requirements met (for Canada: PIPEDA, data residency)

## If an item fails

A failed **minimum** item blocks launch. Open an issue, fix it, re-run this checklist.
A skipped **enterprise** item is acceptable when recorded in an ADR with the reason and the
signal that would make you add it.
