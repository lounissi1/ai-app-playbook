---
id: guide-operate
type: guide
title: Operate
status: draft
updated: 2026-10-13
tags: [operations, scaling, backups, jobs]
related: [guide-deploy, guide-monitor, guide-cost, guide-security]
stage: 7
inputs: [a deployed application]
outputs: [a running, recoverable, cost-controlled system]
---

# Operate

## Goal

Keep the system running, recoverable and affordable without someone watching it.

## Inputs and outputs

**Inputs**

- A deployed application

**Outputs**

- Automatic restarts and scaling
- Scheduled work running as jobs
- Tested backups
- Known monthly cost

## Steps

1. Configure **health probes** so unhealthy instances restart automatically.
2. Set **scaling rules** per part: by HTTP load for web parts, by queue length for workers.
   Allow scale to zero where cold starts are acceptable.
3. Run scheduled and one-off work as **jobs** that start, finish and stop, not as always-on processes.
4. Keep the containers **stateless**: files in object storage, records in the database,
   nothing important on container disk.
5. Use a **managed database** with automatic backups. Restore a backup into a test database once
   to prove it works.
6. Keep secrets in the secrets store; rotate any that must exist.
7. Write a **runbook** for each alert with `templates/runbook.md`.
8. Review cost monthly, and scale down or tear down anything unused.

## Files to copy

- `templates/runbook.md`
- `starters/azure/terraform/` (planned: container app and job modules)

## Done when

- [ ] Health probes restart a broken instance automatically
- [ ] Scaling rules set; idle parts scale down
- [ ] Scheduled work runs as jobs
- [ ] A backup restore has been tested
- [ ] Each alert has a runbook

## Common mistakes

- A minimum of one always-on replica for parts that are idle most of the day.
- Two schedulers running the same job, so everything happens twice.
- Backups that have never been restored.

## Using an AI agent

**Delegate:** scaling rules, job definitions, first drafts of runbooks.

**Review yourself:** minimum replica counts (they set your baseline cost) and the backup restore test.
