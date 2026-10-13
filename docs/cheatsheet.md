---
id: cheat-playbook
type: cheatsheet
title: AI App Playbook on one page
status: draft
updated: 2026-10-13
tags: [overview, architecture, devops, ai, lifecycle]
related: [card-reference-architecture, card-container-image, card-terraform-state, card-rag, decision-which-hosting, decision-which-iac, decision-which-ci, decision-when-to-split, checklist-production-ready]
---

# AI App Playbook on one page

## The loop

```
        ┌──────────── DEV ────────────┐   ┌──────────── OPS ─────────────┐
 Plan → Code → Build → Test ──────────→ Release → Deploy → Operate → Monitor
  ↑                                                                    │
  └──────────────── what you learn becomes the next plan ──────────────┘

 Foundation under every stage: architecture · infrastructure as code · identity & secrets ·
                                managed data · cost guardrails · AI agents with human review
```

| Stage | What happens | Output |
|---|---|---|
| 1 · Plan | Turn goals into small issues with a clear "done" | Issues on a board, specs, ADRs |
| 2 · Code | Branch, write, open a pull request, get a review | Merged, reviewed code on `main` |
| 3 · Build | CI packages the code into a container image | One image per commit |
| 4 · Test | CI runs tests, linters and security scans | A green or red signal on every change |
| 5 · Release | A tested image becomes a named, stored version | Image in the registry; approval if required |
| 6 · Deploy | Migrate the database, switch traffic, verify, roll back if needed | New version live |
| 7 · Operate | Scale, schedule jobs, back up, manage secrets and cost | A running, recoverable system |
| 8 · Monitor | Logs, traces, metrics, alerts | Problems found early; input for the next plan |

## Three questions

| Question | Answered by | Default here |
|---|---|---|
| **Where does my code run?** | The hosting platform | A managed container platform |
| **How are the cloud resources created?** | Infrastructure as code | Terraform |
| **How does new code get there?** | The CI/CD pipeline | GitHub Actions |

Most confusion comes from comparing tools that answer *different* questions. Terraform and
Kubernetes are not alternatives: one creates resources, the other runs containers.

## One tool per job

| Job | Default | Alternatives |
|---|---|---|
| Version control and code home | Git + GitHub | GitLab, Azure Repos |
| Planning | GitHub Issues + Projects | Jira, Azure Boards, Linear |
| CI/CD | GitHub Actions | Azure DevOps Pipelines, GitLab CI, Jenkins, CircleCI |
| Packaging | Docker | Podman |
| Image storage | Cloud container registry | Docker Hub, GitHub Packages |
| Running containers | Managed container platform | Kubernetes, VMs, platform-as-a-service |
| Infrastructure as code | Terraform | Bicep, OpenTofu, Pulumi, CloudFormation |
| Database | Managed PostgreSQL | Managed SQL Server, MySQL |
| Files | Object storage | Network file shares |
| Secrets | Cloud secrets store + managed identity | HashiCorp Vault |
| Background jobs | Queue + workers from the app image | Scheduled jobs, workflow engines (Temporal) |
| Cache | Managed Redis | Valkey, in-process cache |
| Language models | Managed model API behind one internal client | Self-hosted (vLLM, Ollama) |
| Embeddings and vector search | Pinned embedding model + PostgreSQL with pgvector | Managed search service, Qdrant, Weaviate |
| AI quality | Versioned evaluation set run in CI | Managed evaluation services |
| AI coding agents | Agent + `CLAUDE.md` / `AGENTS.md` + specs + human review | — |
| Monitoring | Cloud monitoring + OpenTelemetry | Prometheus + Grafana, ELK |
| Code scanning | GitHub Dependabot + code scanning | SonarQube |

Learn one tool per job deeply. Know the alternatives by name and by job.

## Minimum for production

- Reviewed pull requests and CI on every change
- One immutable image per version, built by CI
- HTTPS, health checks, automatic restarts
- Rollback in minutes
- Migrations run before each deploy
- Managed database with a **tested** backup restore
- Files in object storage, nothing important on container disk
- Secrets in a secrets store; apps and CI use identities, not passwords
- All infrastructure in code, rebuilt from scratch at least once
- Monitoring with at least one alert that reaches a person
- Budget alert and tags on every resource

Full list: [production-ready checklist](checklists/production-ready.md).

## Words to know

| Term | One line |
|---|---|
| [Container image](cards/container-image.md) | A sealed package of an app and everything it needs to run |
| Container | A running copy of an image |
| Registry | Private storage for images, addressed by tag |
| Replica | One running instance of an app; more replicas, more capacity |
| Revision | An immutable version of a deployed app; enables rollback |
| Orchestrator | Software that runs, restarts and scales containers (Kubernetes is the best known) |
| Infrastructure as code | Cloud resources described in files and created by a tool |
| [Terraform state](cards/terraform-state.md) | Terraform's record of what it created |
| CI / CD | Integrate and test every change / deliver every passing change the same way |
| OIDC federation | CI gets short-lived cloud credentials per run instead of stored secrets |
| Managed identity | An identity the cloud gives a resource so it needs no password |
| Least privilege | Each identity gets only the permissions it needs |
| Health check | An endpoint the platform calls to know if the app is alive and ready |
| Rollback | Returning to the previous working version |
| Observability | Logs, metrics and traces that explain what a system is doing |
| [Reference architecture](cards/reference-architecture.md) | The default layers of an app and how they connect |
| [Background job](cards/background-jobs.md) | Slow work handed to a queue and done by a worker |
| [Model serving](cards/model-serving.md) | How the app gets answers from a model: managed API or own service |
| [Embedding](cards/embeddings-vector-search.md) | A vector of numbers representing meaning; similar meaning, nearby vectors |
| [RAG](cards/rag.md) | Retrieve your own passages, then let the model answer from them with citations |
| [AI evaluation](cards/ai-evaluation.md) | Fixed test cases and scores for model-powered features |
| Golden path | One documented, supported way to build and deploy software |
