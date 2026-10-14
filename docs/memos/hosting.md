---
id: memo-hosting
type: memo
title: "Where does my code run?"
status: draft
updated: 2026-10-14
tags: [hosting, containers, memo]
hide: [navigation, toc]
related: [decision-which-hosting, card-container-image, guide-deploy, memo-architecture]
---

# Where does my code run?

<p class="lead">Four yes-or-no questions pick the hosting. Most apps end at the default.</p>

## In one picture

[![Four questions lead to PaaS web app, serverless functions, managed Kubernetes or virtual machines; if all answers are no, use a managed container platform](../assets/memos/hosting.svg)](../assets/memos/hosting.svg)

## Remember

- **The default is a managed container platform:** it runs your containers and scales to zero.
- **Kubernetes is for when you need Kubernetes itself**, not for every app.
- **The same container image runs everywhere:** your laptop, CI and the cloud.
- **Ops effort grows as you go down the list.** Pick the least you can live with.
- **Revisit the choice** when you outgrow it, not before.

## Go deeper

- [Which hosting?](../decisions/which-hosting.md): the full decision tree and comparison table
- [Container image](../cards/container-image.md) · [6 Deploy](../guides/06-deploy.md) · [7 Operate](../guides/07-operate.md)
