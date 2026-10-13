# Instructions for AI coding agents

This repository is the AI App Playbook: how to architect, build, deploy and run AI-powered apps.
When you work in this repository, or in an application created from it, follow these rules.

## When editing the playbook itself

- Every page in `docs/` must follow its schema in `CONTRIBUTING.md` exactly: front matter fields,
  section names and section order. Start new pages by copying from `templates/`.
- Keep concepts cloud-neutral in guides, cards and decision trees. Put provider-specific
  service names only in `## Provider mapping` sections and in `starters/<cloud>/`.
- One concept lives in one place. Link with `related:` instead of repeating text.
- Never change a page's `status` to `reviewed` or `stable`. Only the maintainer does that.
- Add every new page to `mkdocs.yml` navigation.

## When building an application from this template

Start with `docs/guides/architecture.md`, then work through the loop in order and use the matching
guide as your specification. Follow `docs/guides/ai-agents.md` for how specs, plans and reviews work:

| Stage | Guide |
|---|---|
| Plan | `docs/guides/01-plan.md` |
| Code | `docs/guides/02-code.md` |
| Build | `docs/guides/03-build.md` |
| Test | `docs/guides/04-test.md` |
| Release | `docs/guides/05-release.md` |
| Deploy | `docs/guides/06-deploy.md` |
| Operate | `docs/guides/07-operate.md` |
| Monitor | `docs/guides/08-monitor.md` |
| Foundation | `docs/guides/architecture.md`, `security.md`, `infrastructure.md`, `cost.md`, `ai-agents.md` |

Before declaring work finished, check it against the guide's `## Done when` list and
`docs/checklists/production-ready.md`.

## Hard rules (never break these)

- **No secrets** in code, config files, Terraform variables files, workflow files or commit messages.
  Use the secrets store and managed identities. Use placeholders in examples.
- **No long-lived cloud credentials in CI.** Use OIDC federation.
- **Read the infrastructure plan before applying.** Show the full `terraform plan` output and
  wait for human approval before any `apply` or `destroy`.
- **Nothing important on container disk.** Files go to object storage, records to the database.
- **Every change goes through a pull request.** Do not push directly to `main`.
- **Pin model versions** and never send personal or confidential data to an external model
  provider unless the spec explicitly allows it.
- **Ask before creating anything that bills** (new resources, larger SKUs, extra replicas),
  and state the expected monthly cost.

## Explaining your work

After each task, write a short summary a human can present in an interview:
what you built, why this option, what you deliberately left out, and how to roll it back.
