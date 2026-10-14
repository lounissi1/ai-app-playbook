---
id: card-embeddings-vector-search
type: card
title: Embeddings and vector search
status: draft
updated: 2026-10-13
tags: [ai, embeddings, vectors, search, pgvector]
related: [card-rag, card-model-serving, card-ai-evaluation, card-reference-architecture]
kind: concept
stages: [2, 4, 7]
---

# Embeddings and vector search

## In one sentence

An embedding model turns a piece of text (or an image) into a list of numbers, a vector, so that
similar meanings get nearby vectors; vector search then finds the stored items closest to a question.

## Why it exists

Keyword search only finds exact words: "crop disease" misses a document about "leaf blight".
Embeddings capture meaning, so search can match ideas across wording and even across languages.
They are the retrieval half of most AI assistants (see [RAG](rag.md)).

## How it works

```
 Indexing (once per document, in a worker):
   document ─▶ split into chunks ─▶ embedding model ─▶ vector [0.12, -0.40, …] ─▶ stored with the chunk

 Searching (per question, in the API):
   question ─▶ same embedding model ─▶ query vector ─▶ nearest stored vectors ─▶ top-k chunks
```

1. **Chunk** documents into passages of a few hundred words, with a little overlap.
2. **Embed** each chunk with an embedding model and store the vector next to the text and its
   metadata (source, date, owner).
3. At question time, embed the question with **the same model and version**.
4. Find the nearest vectors by **cosine similarity**, usually through an approximate index (HNSW)
   for speed.
5. Often combine with keyword search (**hybrid search**) and filter on metadata (for example,
   only this user's documents).

Mathematically, cosine similarity is `cos θ = (a · b) / (‖a‖ ‖b‖)`: 1 means the same direction
(same meaning), 0 means unrelated.

## Analogy

A library where books are shelved by topic on a map rather than alphabetically. To find books
about your question, you stand at the spot on the map where your question belongs and pick the
nearest books.

## Key terms

| Term | Meaning |
|---|---|
| Embedding | A fixed-length vector representing meaning |
| Dimension | Length of the vector (for example 384, 1024, 3072) |
| Chunk | A passage of a document embedded as one unit |
| Cosine similarity | Similarity of direction between two vectors, from −1 to 1 |
| ANN index (HNSW, IVF) | Approximate nearest-neighbour index; fast search with tiny accuracy loss |
| Hybrid search | Vector search combined with keyword (BM25) search |
| Re-indexing | Re-embedding every chunk, required whenever the embedding model changes |

## Pitfalls

- Embedding documents and questions with **different models or versions**; results become noise.
  Pin the model and test that every service using it produces the same vectors.
- Changing the model without re-indexing everything.
- Chunks too large (vague matches) or too small (no context).
- No metadata filters, so one user's search returns another user's documents.
- Adding a separate vector database when the existing PostgreSQL with a vector extension is enough.

## Provider mapping

| Azure | AWS | Google Cloud | Open source |
|---|---|---|---|
| Database for PostgreSQL with pgvector; Azure AI Search; Cosmos DB vector search; embedding models in Microsoft Foundry | RDS or Aurora PostgreSQL with pgvector; OpenSearch Service; S3 Vectors; embedding models in Bedrock | Cloud SQL or AlloyDB with pgvector; Vertex AI Vector Search; Vertex AI embeddings | pgvector, Qdrant, Weaviate, Milvus, FAISS; models such as BGE-M3 via Sentence Transformers |

## In short

> Chunks and their embeddings live together, often in PostgreSQL with a vector extension and an
> approximate index. Searches filter by owner in the same query, and indexing and querying use one
> pinned model version, checked automatically.
