# AI App Playbook

*Architect, build, deploy and run AI-powered apps, one clear step at a time. Works on any cloud, with real examples on Azure.*

One documented, repeatable way to take an application from first design to production.

```
 ARCHITECTURE    frontend · API · queue + workers · cache ·
                 database · object storage · AI services

 DELIVERY LOOP   Plan → Code → Build → Test → Release →
                 Deploy → Operate → Monitor → back to Plan

 AI              in the app: model serving · embeddings · RAG · evaluation
                 building the app: agents · CLAUDE.md · specs · human review
```

## Start here

- **New to the subject?** Read the [cheat sheet](cheatsheet.md) first.
- **Designing an app?** Follow the [architecture guide](guides/architecture.md) and the
  [reference architecture](cards/reference-architecture.md).
- **Adding AI?** Read [model serving](cards/model-serving.md),
  [embeddings and vector search](cards/embeddings-vector-search.md), [RAG](cards/rag.md) and
  [AI evaluation](cards/ai-evaluation.md).
- **Building with AI agents?** Follow [working with AI agents](guides/ai-agents.md).
- **Starting an app?** Follow the [new app checklist](checklists/new-app.md).
- **Working on one stage?** Open its guide: [Plan](guides/01-plan.md) ·
  [Code](guides/02-code.md) · [Build](guides/03-build.md) · [Test](guides/04-test.md) ·
  [Release](guides/05-release.md) · [Deploy](guides/06-deploy.md) ·
  [Operate](guides/07-operate.md) · [Monitor](guides/08-monitor.md)
- **Choosing?** See the decisions: [hosting](decisions/which-hosting.md) ·
  [infrastructure as code](decisions/which-iac.md) · [CI/CD](decisions/which-ci.md) ·
  [when to split a service](decisions/when-to-split.md)
- **Going live?** Pass the [production-ready checklist](checklists/production-ready.md).
- **Finished experimenting?** Follow the [teardown checklist](checklists/teardown.md).

## How the pages are organised

Every page is one of five types, each with a fixed structure:

| Type | Purpose |
|---|---|
| Cheat sheet | The whole subject on one page |
| Guide | One stage of the loop or one foundation topic, step by step |
| Card | One concept, with a provider mapping |
| Decision tree | Choosing between options |
| Checklist | A gate you pass before moving on |

Status labels: **planned**, **draft**, **reviewed** (used on a real project), **stable**.

---

*Written and maintained by [Lamjed Lounissi](https://github.com/lounissi1). Suggestions are welcome through
[issues and pull requests](https://github.com/lounissi1/ai-app-playbook).*
