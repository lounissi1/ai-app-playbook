---
id: guide-ai-agents
type: guide
title: Working with AI agents
status: draft
updated: 2026-10-13
tags: [ai, agents, specs, claude-md, agents-md, spec-driven]
related: [guide-plan, guide-code, guide-test, guide-architecture, guide-security]
stage: foundation
inputs: [a repository created from this template, an AI coding agent]
outputs: [an instruction file for agents, specs for each task, reviewed pull requests written with AI help]
---

# Working with AI agents

## Goal

Let AI coding agents do most of the typing while a human keeps control of design, security,
cost and what gets merged.

## Inputs and outputs

**Inputs**

- A repository created from this template
- An AI coding agent that can read the repository and open pull requests

**Outputs**

- An instruction file the agent reads on every task (`CLAUDE.md`, `AGENTS.md` or the tool's equivalent)
- One spec per task, linked to its issue
- Pull requests written with AI help and reviewed by a human

## Steps

1. **Write the instruction file.** Start from this repository's `CLAUDE.md`. It tells the agent
   the project's rules: schemas to follow, hard rules (no secrets, plan before apply, pull
   requests only, ask before anything that bills) and how to report its work. If your tool reads
   `AGENTS.md` instead, keep one file and point the other to it, rather than two copies drifting apart.
2. **Add project facts** the agent cannot guess: how to run, test and lint locally; folder
   layout; naming conventions; what not to touch.
3. **Plan before coding.** For each issue, write a spec with `templates/spec.md`: goal, context
   links, requirements, constraints, acceptance criteria, out of scope. Ask the agent to
   critique the spec and list open questions before it writes code.
4. **Ask for a plan, then approve it.** The agent proposes the files it will change and how; you
   approve or correct before it starts.
5. **Keep tasks small**: one issue, one branch, one pull request that a human can review in
   under 30 minutes.
6. **Let CI judge.** The agent must run tests, linters and evaluations locally; CI runs them again.
   Red CI means not done, whatever the agent says.
7. **Review like a senior engineer**: read the diff, check that tests assert real behaviour, look
   for secrets, new dependencies, permission changes and anything that creates cost.
8. **Keep humans on irreversible actions**: production deploys, `terraform apply` and `destroy`,
   database migrations on real data, deleting storage, changing access rights.
9. **Feed lessons back.** When an agent repeats a mistake, add a rule to the instruction file.

## Files to copy

- `CLAUDE.md`
- `templates/spec.md`
- `templates/adr.md`
- `.github/pull_request_template.md`

## Done when

- [ ] The instruction file exists, lists the hard rules and the local run and test commands
- [ ] Every agent task starts from an issue with a spec
- [ ] The agent's plan was approved before it wrote code
- [ ] CI is green and a human reviewed every merged pull request
- [ ] No agent has credentials that allow production changes without human approval

## Common mistakes

- Vague prompts ("make it production-ready") instead of a spec with acceptance criteria.
- Huge tasks producing pull requests nobody can review properly.
- Accepting tests the agent wrote that pass but assert nothing meaningful.
- Giving the agent long-lived cloud credentials or owner rights.
- Letting the agent "fix" CI by deleting or skipping failing tests.
- Two instruction files that contradict each other.

## Using an AI agent

**Delegate:** drafting specs from issues, implementing a reviewed spec, writing tests and docs,
explaining unfamiliar code, proposing refactors, summarising what changed for the pull request.

**Review yourself:** the spec's acceptance criteria, the agent's plan, every diff before merge,
anything touching security, money, data deletion or production, and whether the change was needed at all.
