---
id: card-terraform-state
type: card
title: Terraform state
status: draft
updated: 2026-10-13
tags: [terraform, infrastructure-as-code, state, locking]
related: [guide-infrastructure, decision-which-iac, checklist-teardown]
kind: concept
stages: [foundation]
---

# Terraform state

## In one sentence

Terraform state is the file in which Terraform records which real cloud resources it created and
how they map to the resources in your code.

## Why it exists

Your code says what you **want**. The cloud contains what **exists**. To compute a plan, Terraform
must know which existing resource corresponds to each block of code, including identifiers the
cloud generated. State is that mapping. Without it, Terraform would try to create everything again.

## How it works

```
 .tf files (desired)  ─┐
                       ├─▶ terraform plan ─▶ list of changes ─▶ terraform apply ─▶ cloud updated
 state (recorded)     ─┤                                                            │
 cloud (actual)       ─┘                                       state updated ◀──────┘
```

- `plan` compares three things: the code, the state, and what actually exists in the cloud.
- `apply` makes the changes and writes the new state.
- **Remote state** keeps the file in shared storage (object storage or a managed service) instead
  of on a laptop, so CI and people work from the same record.
- **Locking** ensures only one `plan` or `apply` runs at a time, preventing two runs from
  corrupting the state.
- **Drift** is when reality no longer matches state, usually because someone changed something
  by hand. `plan` shows it.

## Analogy

State is the building company's inventory list of everything it has built on your land. Without
the list, the company cannot tell which buildings are its own, and would build duplicates.

## Key terms

| Term | Meaning |
|---|---|
| Backend | Where state is stored (local file, cloud storage, managed service) |
| Lock | A marker preventing two runs from changing state at once |
| Drift | Differences between state and real resources |
| Import | Bringing an existing, hand-made resource under Terraform management |
| Workspace | A separate state for the same code (some teams use folders per environment instead) |

## Pitfalls

- **State can contain secrets** (generated passwords, connection strings). Keep the storage private
  and accessed by identity, never public, and never commit state to Git.
- Deleting or hand-editing state to "fix" an error; Terraform then loses track of resources that
  still exist and still bill.
- Storing state inside the infrastructure it describes; destroying the environment deletes its own memory.
- Local state on one laptop; lost laptop, lost control.

## Provider mapping

| Azure | AWS | Google Cloud | Open source |
|---|---|---|---|
| `azurerm` backend: Azure Storage blob container, locking by blob lease | `s3` backend: Amazon S3, with S3 lockfile or DynamoDB locking | `gcs` backend: Google Cloud Storage, built-in locking | OpenTofu (same model, adds client-side state encryption); HCP Terraform for managed state |

## In short

> State is Terraform's record of what it manages. It belongs in private, identity-protected remote
> storage with locking, outside the environment it describes, so people and CI share one source of
> truth and a destroy can never delete its own state.
