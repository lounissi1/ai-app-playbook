---
id: card-rag
type: card
title: Retrieval-augmented generation (RAG)
status: draft
updated: 2026-10-13
tags: [ai, rag, llm, retrieval, grounding]
related: [card-embeddings-vector-search, card-model-serving, card-ai-evaluation, card-reference-architecture]
kind: pattern
stages: [2, 4, 8]
---

# Retrieval-augmented generation (RAG)

## In one sentence

RAG answers a question by first retrieving relevant passages from your own data, then asking a
language model to answer using only those passages, with citations.

## Why it exists

A language model knows only what was in its training data, which is generic and dated, and it
will confidently invent answers it does not know. Retraining it on your documents is slow and
expensive. RAG gives the model the right facts at question time, keeps answers current, and lets
users check the sources.

## How it works

```
 question ─▶ retrieve top-k chunks ─▶ build prompt:            ─▶ language model ─▶ answer + citations
             (vector + keyword       "Answer only from these
              search, filtered        sources. Cite them. If
              by user)                the answer is not there,
                                      say so." + chunks + question
```

1. **Ingest** (worker): load documents, split into chunks, embed, store with metadata.
2. **Retrieve** (API): embed the question, search, filter by permissions, keep the top few chunks;
   optionally re-rank them with a more precise model.
3. **Generate**: send instructions, the retrieved chunks and the question to the language model.
4. **Cite**: return the answer with links to the chunks it used.
5. **Refuse well**: if retrieval finds nothing relevant, say so instead of guessing.
6. **Evaluate** retrieval and answers separately (see [AI evaluation](ai-evaluation.md)).

## Analogy

An open-book exam. The student (the model) is not expected to remember everything; a librarian
(retrieval) hands over the right pages, and the student must answer from them and cite the page.

## Key terms

| Term | Meaning |
|---|---|
| Retrieval | Finding the passages most relevant to the question |
| Grounding | Basing the answer only on supplied sources |
| Hallucination | A fluent answer not supported by any source |
| Top-k | How many passages are passed to the model |
| Re-ranking | A second, more precise scoring of retrieved passages |
| Context window | The maximum amount of text the model can read at once |
| Prompt injection | Text inside a document that tries to give the model instructions |

## Pitfalls

- Blaming the model when retrieval returned the wrong passages; measure retrieval first.
- Stuffing too many chunks into the prompt; quality and cost both get worse.
- No permission filter at retrieval time; the model leaks documents the user may not see.
- Trusting document text as instructions; treat retrieved text as data (prompt injection).
- No "I don't know" path, so the model fills gaps with invention.
- No evaluation set, so every prompt change is a guess.

## Provider mapping

| Azure | AWS | Google Cloud | Open source |
|---|---|---|---|
| Azure AI Search with Microsoft Foundry models (or PostgreSQL pgvector) | Bedrock Knowledge Bases (or pgvector, OpenSearch) | Vertex AI RAG Engine, Vertex AI Search (or pgvector) | LlamaIndex, LangChain, Haystack; pgvector, Qdrant |

## Say it in an interview

> Our assistant uses RAG: permission-filtered hybrid retrieval over pgvector, a short grounded
> prompt that must cite sources or say it doesn't know, and an evaluation set that scores
> retrieval and answers separately on every change.
