---
id: memo-ai-in-app
type: memo
title: AI inside the app
status: draft
updated: 2026-10-14
tags: [ai, rag, embeddings, memo]
hide: [navigation, toc]
related: [card-rag, card-embeddings-vector-search, card-model-serving, card-ai-evaluation, memo-architecture]
---

# AI inside the app

<p class="lead">How an app answers questions from its own documents: retrieval-augmented generation (RAG).</p>

## In one picture

[![Documents are split into chunks, embedded and stored once; each question is embedded with the same model, searched with a user filter, and answered by a language model with citations, or it says I don't know](../assets/memos/ai-in-app.svg)](../assets/memos/ai-in-app.svg)

## Remember

- **Index once, answer many times:** documents are embedded in a worker, questions in the API.
- **Same embedding model, same version, everywhere.** Otherwise search returns noise.
- **Filter by user at search time,** so nobody sees documents that aren't theirs.
- **No good match? Say “I don't know”** instead of guessing.
- **Measure it:** a fixed set of test questions runs in CI on every change.

## Go deeper

- [Retrieval-augmented generation](../cards/rag.md) · [Embeddings and vector search](../cards/embeddings-vector-search.md)
- [Model serving](../cards/model-serving.md) · [AI evaluation](../cards/ai-evaluation.md)
