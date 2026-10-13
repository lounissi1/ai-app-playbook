---
id: guide-security
type: guide
title: Security
status: draft
updated: 2026-10-13
tags: [security, identity, secrets, least-privilege]
related: [guide-infrastructure, guide-code, guide-release, checklist-production-ready]
stage: foundation
inputs: [a cloud account, a repository]
outputs: [identities instead of passwords, secrets in a store, least-privilege access, scanning]
---

# Security

## Goal

No passwords in code or CI, every identity limited to what it needs, and problems found automatically.

## Inputs and outputs

**Inputs**

- A cloud account and a code repository

**Outputs**

- A managed identity for the application, and OIDC federation for CI
- All remaining secrets in a secrets store
- Roles scoped to specific resources
- Dependency, code and image scanning turned on

## Steps

1. **Application identity.** Give the application a managed identity. It uses that identity to
   read secrets, pull images and write to storage; no keys in configuration.
2. **CI identity.** Set up OIDC federation between CI and the cloud, scoped to this repository and
   (for production) to a protected environment. Store no cloud credentials in CI.
3. **Secrets store.** Put any secret that must exist (database password, third-party API key) in
   the cloud secrets store. The platform injects it as an environment variable at runtime.
4. **Least privilege.** Grant each identity only the roles it needs, on the smallest scope
   (one vault, one storage account, one resource group).
5. **Scanning.** Turn on dependency alerts, code scanning and image scanning. Review findings weekly.
6. **Network exposure.** Expose only the public entry point. Keep internal services internal.
   Require TLS for the database.
7. **Branch protection.** Require pull requests and passing checks on `main`.
8. **Data.** Keep personal data out of logs. Know which region data lives in.

## Files to copy

- `starters/azure/terraform/` (planned: identity, vault and role assignment modules)

## Done when

- [ ] `grep` for keys, passwords and tokens in the repository returns nothing real
- [ ] CI deploys with OIDC; no cloud secrets stored in CI
- [ ] Application reads secrets through its managed identity
- [ ] Every role assignment is scoped to a specific resource or group
- [ ] Scanning is on and findings are triaged

## Common mistakes

- "Temporary" keys committed and left in Git history. Rotate them; deleting the file is not enough.
- Owner or contributor rights on the whole subscription for CI or apps.
- Infrastructure state files readable by anyone; they can contain secrets.

## Using an AI agent

**Delegate:** writing identity and role assignments in Terraform, finding hard-coded secrets,
explaining scanner findings.

**Review yourself:** every role assignment and its scope, anything made public, and the agent's own
access. Never give an agent more cloud rights than the task needs.
