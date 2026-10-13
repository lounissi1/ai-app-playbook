# Definition of done (v1)

Version 1 of this playbook is finished when **every box below is checked**. Nothing else is
required for v1; new ideas go to [IDEAS.md](IDEAS.md).

## Structure

- [x] `README.md`, `CONTRIBUTING.md` (five schemas), `CLAUDE.md`, `IDEAS.md`, `DONE.md`
- [x] Templates for every document type in `templates/`
- [x] Site builds with `mkdocs build --strict`

## Content

- [ ] Cheat sheet at `stable`
- [ ] Eight stage guides (01-plan to 08-monitor) at `reviewed` or better
- [ ] Foundation guides (architecture, security, infrastructure, cost, AI agents) at `reviewed` or better
- [ ] At least 15 cards at `reviewed` or better (see the list in `docs/cards/index.md`)
- [ ] Four decision trees (hosting, infrastructure as code, CI/CD, when to split a service) at `reviewed` or better
- [ ] Architecture cards (reference architecture, background jobs) at `reviewed` or better
- [ ] AI cards (model serving, embeddings and vector search, RAG, AI evaluation) at `reviewed` or better
- [ ] Three checklists (new app, production ready, teardown) at `reviewed` or better

## Starters (Azure)

- [ ] Dockerfiles: Python API and Node web app
- [ ] Workflows: CI (test, lint, scan), build and push, deploy with migration, smoke test and rollback
- [ ] Terraform modules: foundation, registry, database, storage, container app environment, container app, budget
- [ ] Each starter README has `## Proven on` filled in

## Proof

- [ ] A minimal "hello" API created with **Use this template** goes through the whole loop
      (plan to monitor) on Azure in one afternoon, then is torn down with the teardown checklist
- [ ] A small AI feature (RAG over a few documents, with an evaluation set in CI) is added to
      that API and deployed the same way
- [ ] Repository made public
