---
id: guide-deploy
type: guide
title: Deploy
status: draft
updated: 2026-10-13
tags: [deployment, migrations, rollback]
related: [guide-release, guide-operate, decision-which-hosting]
stage: 6
inputs: [a released image, infrastructure that exists]
outputs: [the new version serving traffic, or the old one restored]
---

# Deploy

## Goal

Put a new version live safely: migrate, switch, verify, and roll back automatically if it fails.

## Inputs and outputs

**Inputs**

- A released image tag
- Infrastructure created by Terraform

**Outputs**

- The new version serving traffic, verified by a smoke test
- Or, on failure, the previous version restored

## Steps

1. Run **database migrations** as a one-off job using the new image, before switching traffic.
   Migrations must be backward-compatible with the version still running.
2. Deploy the new image as a new **revision** (or deployment) alongside the old one.
3. Wait until its **readiness** check passes.
4. Shift traffic: all at once for small apps, or gradually (10% then 100%) for larger ones.
5. Run a **smoke test**: call `/readyz` and one real, read-only user flow.
6. If the smoke test fails, send traffic back to the previous revision and fail the pipeline.
7. Record which image tag is live.

## Files to copy

- `starters/azure/workflows/deploy.yml` (planned)

## Done when

- [ ] Migrations run automatically before traffic moves
- [ ] Readiness gates traffic
- [ ] A smoke test runs after every deploy
- [ ] Rollback has been triggered on purpose at least once and worked
- [ ] Served over HTTPS

## Common mistakes

- Destructive migrations (dropping a column) in the same release that stops using it. Split them
  across two releases.
- No smoke test, so a broken deploy is discovered by users.
- Manual deploys from a laptop "just this once".

## Using an AI agent

**Delegate:** writing the deploy workflow, migration jobs, smoke tests.

**Review yourself:** migration safety, the rollback path, and anything that changes what the
public internet can reach.
