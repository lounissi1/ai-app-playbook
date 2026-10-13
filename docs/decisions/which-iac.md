---
id: decision-which-iac
type: decision
title: Which infrastructure as code?
status: draft
updated: 2026-10-13
tags: [infrastructure-as-code, terraform, bicep, opentofu]
related: [guide-infrastructure, card-terraform-state, decision-which-hosting]
question: Which tool should define and create the cloud resources?
default: Terraform
---

# Which infrastructure as code?

## The question

Which tool should describe the cloud resources in code and create, change and destroy them?

## Decision tree

1. Does the organisation already standardise on a tool?
   - **Yes** → use it.
   - **No** → go to 2.
2. Will you use more than one cloud, or manage third-party services (DNS, monitoring SaaS, GitHub) as code?
   - **Yes** → go to 4.
   - **No** → go to 3.
3. Is the work Azure-only, with a small team that prefers the provider's native tool?
   - **Yes** → *Bicep* is a reasonable choice (AWS-only equivalent: CloudFormation or CDK).
   - **No** → go to 4.
4. Do you need an open-source licence or built-in state encryption?
   - **Yes** → *OpenTofu*
   - **No** → **Terraform** (default)
5. Does the team strongly prefer a general-purpose programming language over a configuration language?
   - **Yes** → consider *Pulumi*.

## Options compared

| Option | Clouds | Language | State | Ecosystem and hiring | Notes |
|---|---|---|---|---|---|
| **Terraform** | All major clouds and many services | HCL | You manage (remote backend) | Largest; most job postings | Business Source Licence since 2023; owned by IBM since late 2024 |
| OpenTofu | Same as Terraform | HCL | You manage; optional encryption | Smaller, growing | Open-source fork; largely compatible |
| Bicep | Azure only | Bicep | Managed by Azure | Azure-focused | Simplest for Azure-only teams |
| CloudFormation / CDK | AWS only | YAML/JSON / programming languages | Managed by AWS | AWS-focused | Native to AWS |
| Pulumi | All major clouds | Python, TypeScript, Go, C# | Managed service or self-managed | Smaller | Real programming languages |

## Default and why

Terraform works on every major cloud, has the largest module ecosystem, and is what most job
postings ask for. Its language and concepts transfer directly to OpenTofu, and the same skills
cover Azure, AWS and Google Cloud, which keeps this playbook cloud-neutral.

## When to revisit

- Licensing terms matter for how you distribute or host the tooling: consider OpenTofu.
- The work becomes permanently single-cloud and the team prefers native tooling: consider Bicep or CloudFormation.
- The team builds complex logic that is awkward in a configuration language: consider Pulumi.
