---
id: guide-cost
type: guide
title: Cost
status: draft
updated: 2026-10-13
tags: [cost, finops, budget, cleanup]
related: [guide-infrastructure, guide-operate, checklist-teardown]
stage: foundation
inputs: [a cloud account]
outputs: [a budget with alerts, tagged resources, a known monthly cost]
---

# Cost

## Goal

Know what you will pay before you pay it, get warned before surprises, and stop charges when done.

## Inputs and outputs

**Inputs**

- A cloud account

**Outputs**

- A budget with alerts, created before any other resource
- Tags on every resource
- An estimated monthly cost per environment
- A teardown routine

## Steps

1. **Budget first.** Create a monthly budget with alerts at 50%, 80% and 100% of actual spend,
   and at 100% of forecast. Do this before creating anything else.
2. **Understand the meter.** Most cloud services bill while they **run**, not while they are
   **used**. An idle server or a minimum replica of 1 bills around the clock.
3. **Know the free tiers** of your provider and their limits (hours, storage, duration).
   Write them down with the date you checked; they change.
4. **Estimate before creating:** use the provider's pricing calculator for each new resource and
   record the monthly figure in the pull request.
5. **Scale to zero** where idle time is acceptable.
6. **Tag everything** and review cost grouped by tag monthly.
7. **Cap logs:** set a daily ingestion limit on logging.
8. **Tear down** finished environments with the teardown checklist.

## Files to copy

- `starters/azure/terraform/` (planned: budget module)
- [Teardown checklist](../checklists/teardown.md)

## Done when

- [ ] Budget and alerts exist and have been tested
- [ ] Every resource is tagged
- [ ] Monthly cost estimated and written down
- [ ] Idle parts scale down
- [ ] Teardown has been done once

## Common mistakes

- Assuming a budget **stops** spending. Usually it only alerts; stopping requires an action you
  wire up yourself.
- Free-trial credit that ends quietly while resources keep running.
- Paid add-ons accepted from setup wizards (premium security, firewalls, private endpoints).
- Container registries and log storage, which are rarely free.

## Using an AI agent

**Delegate:** pricing estimates, finding untagged resources, writing budget and cleanup scripts.

**Review yourself:** any change that adds a resource or raises a minimum, and the final cost report.
