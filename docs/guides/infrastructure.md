---
id: guide-infrastructure
type: guide
title: Infrastructure
status: draft
updated: 2026-10-13
tags: [infrastructure-as-code, terraform, state]
related: [card-terraform-state, decision-which-iac, guide-security, checklist-teardown]
stage: foundation
inputs: [a cloud account, the architecture decided in ADRs]
outputs: [every cloud resource defined in code, recreatable from scratch]
---

# Infrastructure

## Goal

Every cloud resource is defined in code, reviewed as a plan, and can be destroyed and rebuilt at will.

## Inputs and outputs

**Inputs**

- A cloud account with a budget alert already set
- The architecture choices recorded in ADRs

**Outputs**

- Terraform code in the repository
- Remote, locked state storage
- CI that plans on pull requests and applies after approval

## Steps

1. **Bootstrap once, by hand or with a small separate configuration:** a storage location for
   Terraform state, and the OIDC identity CI will use. Keep this outside the main configuration
   so destroying the app never destroys its own state.
2. **Layout:**

   ```
   infra/terraform/
   ├── bootstrap/        # state storage + CI identity (run once)
   ├── modules/          # reusable building blocks
   └── envs/<name>/      # one folder per environment, composing modules
   ```

3. **Modules:** foundation (resource group, logging, secrets store, identity), registry, database,
   storage, container platform environment, container app, budget.
4. **Pin versions** of Terraform and providers.
5. **Plan on pull requests:** CI runs `fmt`, `validate` and `plan`, and posts the plan for review.
6. **Apply after approval:** a protected environment requires a person to approve.
7. **Tag everything** (`project`, `env`, `owner`) so cost and leftovers can be found.
8. **Let the pipeline own image versions.** Terraform creates the apps; the deploy workflow sets
   which image runs. Tell Terraform to ignore image changes so it never rolls back a deploy.
9. **Prove it:** run `destroy`, then `apply` again from scratch, at least once.

## Files to copy

- `starters/azure/terraform/` (planned)
- [Terraform state](../cards/terraform-state.md)

## Done when

- [ ] Nothing in the environment was created by portal clicks
- [ ] State is remote, locked and private
- [ ] CI plans on pull requests and applies only after approval
- [ ] Every resource is tagged
- [ ] Destroy and rebuild has been done once

## Common mistakes

- Creating something in the portal "to test" and forgetting it; it bills and drifts.
- Local state on a laptop; it gets lost or conflicts.
- Applying without reading the plan, especially lines marked *destroy* or *replace*.
- Putting the state storage inside the configuration it stores.

## Using an AI agent

**Delegate:** writing modules, translating examples between clouds, explaining plan output.

**Review yourself:** every plan before apply, especially deletions, replacements, public access and
anything with a monthly price.
