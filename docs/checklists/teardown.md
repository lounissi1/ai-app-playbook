---
id: checklist-teardown
type: checklist
title: Teardown
status: draft
updated: 2026-10-13
tags: [cost, cleanup]
related: [guide-cost, guide-infrastructure, card-terraform-state]
gate: When an experiment, demo or learning environment is finished
---

# Teardown

## When to use

When you stop using a cloud environment and want charges to stop. Everything you need to
rebuild it stays in Git, so tearing down loses nothing that matters.

## Checklist

### Before destroying

- [ ] Code, Terraform files and workflows are committed and pushed · [Infrastructure](../guides/infrastructure.md)
- [ ] Any data you want to keep is exported (database dump, important files) · [Operate](../guides/07-operate.md)
- [ ] Scheduled jobs and pipelines that would recreate resources are disabled

### Destroy

- [ ] `terraform plan -destroy` reviewed: only the expected resources are listed · [Terraform state](../cards/terraform-state.md)
- [ ] `terraform destroy` completed without errors
- [ ] Resources created outside Terraform (portal clicks) found and deleted by tag or resource group
- [ ] Soft-deleted items purged where the provider keeps them (for example secrets vaults)

### Verify

- [ ] The provider's resource list filtered by your project tag returns nothing
- [ ] Cost dashboard checked the next day shows no running charges · [Cost](../guides/cost.md)
- [ ] State storage kept (pennies) or deleted last, if you are completely finished

## If an item fails

If `destroy` fails, read the error, fix the dependency it names, and run it again. Never
delete the state file to "force" a teardown; Terraform would then lose track of what still
exists and still bills.
