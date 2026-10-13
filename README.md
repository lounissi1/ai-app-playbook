# AI App Playbook

*Architect, build, deploy and run AI-powered apps, one clear step at a time. Works on any cloud, with real examples on Azure.*

This repository is one documented, repeatable way, a *golden path*, to take an application from
first design to production and keep it running: the architecture it should have, the AI
components it may need, and the delivery loop that ships it.

- **Architecture first.** A reference app architecture (frontend, API, queue and workers, cache,
  database, object storage, AI services) and a decision tree for when to split a service.
- **AI inside the app.** Cards on model serving, embeddings and vector search, retrieval-augmented
  generation (RAG) and AI evaluation.
- **AI building the app.** A guide and a `CLAUDE.md` that let AI coding agents do the typing
  while humans keep control of design, security and cost.
- **The whole delivery loop.** Plan → code → build → test → release → deploy → operate → monitor.
- **Cloud-neutral concepts, one proven implementation.** Every card maps the concept to Azure,
  AWS, Google Cloud and open source. Real, copyable files live in `starters/azure/`.
- **Normalized.** Every page is one of five document types with a fixed schema.
  See [CONTRIBUTING.md](CONTRIBUTING.md).

> **Status:** early draft. See [DONE.md](DONE.md) for the definition of done and progress.

---

## The playbook in one picture

```
 ARCHITECTURE    frontend · API · queue + workers · cache ·
                 database · object storage · AI services

 DELIVERY LOOP   Plan → Code → Build → Test → Release →
                 Deploy → Operate → Monitor → back to Plan

 AI              in the app: model serving · embeddings · RAG · evaluation
                 building the app: agents · CLAUDE.md · specs · human review

 FOUNDATION      infrastructure as code · identity and secrets ·
                 managed data · cost guardrails
```

## Four questions that sort every tool

| Question | Default answer here | Alternatives |
|---|---|---|
| What are the parts of my app? | The [reference architecture](docs/cards/reference-architecture.md) | Split further only with a [reason](docs/decisions/when-to-split.md) |
| Where does my code run? | Managed container platform (Azure Container Apps) | VMs, App Service, Kubernetes / AKS, Functions |
| How are the cloud resources created? | Terraform | Bicep, OpenTofu, Pulumi, portal clicks |
| How does new code get there? | GitHub Actions | Azure DevOps Pipelines, GitLab CI, Jenkins |

## How to navigate

| You want to… | Go to |
|---|---|
| See everything on one page | [docs/cheatsheet.md](docs/cheatsheet.md) |
| Design an app's architecture | [docs/guides/architecture.md](docs/guides/architecture.md) |
| Add AI to an app | [model serving](docs/cards/model-serving.md), [RAG](docs/cards/rag.md), [evaluation](docs/cards/ai-evaluation.md) |
| Build with AI coding agents | [docs/guides/ai-agents.md](docs/guides/ai-agents.md) and [CLAUDE.md](CLAUDE.md) |
| Follow one delivery stage step by step | [docs/guides/](docs/guides/) |
| Understand one concept | [docs/cards/](docs/cards/) |
| Choose between options | [docs/decisions/](docs/decisions/) |
| Check you're ready | [docs/checklists/](docs/checklists/) |
| Copy real files | [starters/](starters/) |
| Write a new page | [templates/](templates/) and [CONTRIBUTING.md](CONTRIBUTING.md) |

## Start a new app from this template

1. Click **Use this template** on GitHub to create your app's repository.
2. Design it with [the architecture guide](docs/guides/architecture.md).
3. Follow [docs/checklists/new-app.md](docs/checklists/new-app.md) from top to bottom.
4. Copy what you need from `starters/azure/`.
5. Before going live, pass [docs/checklists/production-ready.md](docs/checklists/production-ready.md).
6. When you're done experimenting, follow [docs/checklists/teardown.md](docs/checklists/teardown.md).

## Read it as a website

**Online:** https://lounissi1.github.io/ai-app-playbook/ (published automatically from `main`).

To preview locally, the docs build with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/):

```bash
pip install -r requirements-docs.txt
mkdocs serve        # open http://127.0.0.1:8000
```

## Scope

This repository covers **how an AI-powered app is designed, built, shipped and run**. Deeper
handbooks (data science, agentic AI, remote sensing, precision agriculture, mathematics) are
parked in [IDEAS.md](IDEAS.md) and will live in separate repositories that reuse the same schemas.

## Author

Created and maintained by **Lamjed Lounissi** ([@lounissi1](https://github.com/lounissi1)),
drawing on experience in data science, satellite data and GIS, and scientific software.
Suggestions and corrections are welcome: open an issue or a pull request.

To cite this playbook, use **Cite this repository** on GitHub (from [CITATION.cff](CITATION.cff)).

## License

Documentation: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Reuse it freely with credit.
Code in `starters/` and workflows: [MIT](LICENSE-CODE). Details in [LICENSE](LICENSE).
