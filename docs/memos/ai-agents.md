---
id: memo-ai-agents
type: memo
title: Building with AI agents
status: draft
updated: 2026-10-14
tags: [ai, agents, specs, memo]
hide: [navigation, toc]
related: [guide-ai-agents, guide-plan, guide-code, memo-delivery-loop]
---

# Building with AI agents

<p class="lead">The agent types; you decide. Two approvals keep you in control.</p>

## In one picture

[![The human writes the issue and spec, the agent plans, the human approves, the agent codes with tests, CI checks, the human reviews and merges](../assets/memos/ai-agents.svg)](../assets/memos/ai-agents.svg)

## Remember

- **Start every task from a spec:** goal, limits and what “done” means.
- **Approve the plan before any code is written.**
- **Small tasks:** one issue, one branch, one pull request you can review in 30 minutes.
- **Red CI means not done,** whatever the agent says.
- **Irreversible actions stay human:** production deploys, infrastructure changes, deleting data, access.

## Go deeper

- [Working with AI agents](../guides/ai-agents.md): the step-by-step guide
- [CLAUDE.md](https://github.com/lounissi1/ai-app-playbook/blob/main/CLAUDE.md) · [Spec template](https://github.com/lounissi1/ai-app-playbook/blob/main/templates/spec.md) · [2 Code](../guides/02-code.md)
