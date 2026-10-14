---
id: memo-architecture
type: memo
title: App architecture
status: draft
updated: 2026-10-14
tags: [architecture, memo]
hide: [navigation, toc]
related: [card-reference-architecture, guide-architecture, card-background-jobs, decision-when-to-split, memo-playbook]
---

# App architecture

<p class="lead">The seven parts of almost every web app, AI-powered or not, and how they connect.</p>

## In one picture

[![Users reach the frontend, the frontend calls the API, slow work goes through a queue to workers, and only the database and object storage hold data](../assets/memos/architecture.svg)](../assets/memos/architecture.svg)

## Remember

- **Users talk to the frontend; the frontend talks only to the API.**
- **Anything slower than about a second goes to the queue**, and workers do it.
- **Only the database and object storage hold data**, so everything else can restart or scale freely.
- **The cache is a shortcut, never the truth.** It can be emptied at any moment.
- **Heavy AI models get their own service**, so the API stays light and fast.

## Go deeper

- [Reference app architecture](../cards/reference-architecture.md): each layer, its job, provider names
- [Design the architecture](../guides/architecture.md): the step-by-step guide
- [Background jobs and queues](../cards/background-jobs.md) · [When to split a service?](../decisions/when-to-split.md) · [Model serving](../cards/model-serving.md)
