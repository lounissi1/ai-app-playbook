# Azure starters

## What it creates

When complete, these starters take a containerised application to Azure:

| Area | Folder | Creates | Status |
|---|---|---|---|
| Docker | `docker/` | Dockerfiles for a Python API and a Node web app, a compose file for local development | planned |
| Workflows | `workflows/` | `ci.yml` (test, lint, scan), `build-push.yml` (image to registry), `deploy.yml` (migrate, deploy, smoke test, roll back) | planned |
| Terraform | `terraform/` | `bootstrap/` (state storage, CI identity), `modules/` (foundation, registry, database, storage, container app environment, container app, budget), `envs/example/` | planned |

Target services: Azure Container Apps, Azure Container Registry, Azure Database for PostgreSQL
flexible server, Blob Storage, Key Vault with managed identity, Log Analytics and Application
Insights, Cost Management budgets. CI: GitHub Actions with OIDC.

## Prerequisites

- An Azure subscription with a budget alert already created
- Terraform and the Azure CLI installed
- A GitHub repository created from this template

## How to use

1. Copy the folders you need into your application repository.
2. Replace every placeholder listed below.
3. Follow [the new app checklist](../../docs/checklists/new-app.md).

## Placeholders

| Placeholder | Meaning | Example |
|---|---|---|
| `<app-name>` | Short, lowercase application name | `hello-api` |
| `<region>` | Azure region | `canadacentral` |
| `<subscription-id>` | Azure subscription ID | (never commit the real value) |
| `<github-org>/<repo>` | Repository allowed to sign in with OIDC | `my-org/hello-api` |

## Proven on

not yet verified
