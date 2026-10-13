---
id: card-model-serving
type: card
title: Model serving
status: draft
updated: 2026-10-13
tags: [ai, llm, inference, models, gpu]
related: [card-reference-architecture, decision-when-to-split, card-embeddings-vector-search, card-rag, card-ai-evaluation]
kind: concept
stages: [2, 6, 7, 8]
---

# Model serving

## In one sentence

Model serving is how an application gets answers from a machine-learning model: either by calling
a managed model API, or by running the model yourself behind your own endpoint.

## Why it exists

A trained model is only a file of weights. To be useful it must be loaded into memory (often a GPU),
kept warm, given a network interface, protected, scaled with demand and watched for cost and
quality. Serving is that operational layer between "we have a model" and "the app can use it".

## How it works

```
 App ──HTTPS──▶  Option A: managed model API   (provider runs the model; you pay per token or call)
     ──HTTPS──▶  Option B: your model service  (your container loads the weights; you pay for compute)
```

| | Managed model API | Self-hosted model service |
|---|---|---|
| You manage | Prompts, keys or identity, quotas | Container, weights, hardware, scaling, updates |
| Cost shape | Per token or call; zero when idle | Per second of compute; GPUs are expensive when idle |
| Data | Leaves your service boundary (check the provider's terms and region) | Stays where you run it |
| Best for | Large language models, quick start | Small or specialised models (embeddings, classifiers), strict data rules |

Either way, the app should:

1. Call models through **one internal client or gateway**, so the provider can change without
   touching business code.
2. **Pin the model version** (name plus version or weights hash). An unpinned model changes behind
   your back.
3. Set **timeouts, retries and token limits** on every call.
4. Log **latency, tokens and cost** per request, without logging sensitive prompt content by default.
5. Load self-hosted weights from object storage or bake them into the image, never download them
   from the internet at every start.

## Analogy

Electricity. You can buy it from the grid (managed API: pay per use, no maintenance) or run your
own generator (self-hosted: full control, but you buy fuel, maintain it and pay even when idle).

## Key terms

| Term | Meaning |
|---|---|
| Inference | Running a trained model to get an output |
| Endpoint | The network address that accepts requests for a model |
| Token | A piece of text (about ¾ of a word) used to count model input and output |
| Latency / throughput | Time per answer / answers per second |
| Cold start | Delay while a scaled-to-zero model loads its weights |
| Quantization | Storing weights with fewer bits to cut memory, at a small quality cost |
| Gateway | A layer that routes, limits and logs calls to one or more model providers |

## Pitfalls

- Hard-coding one provider's SDK throughout the code.
- Unpinned model versions; quality changes with no code change.
- No token limits or budget alerts; one loop can spend a month's budget in an hour.
- Loading a large model inside every API replica (see [when to split](../decisions/when-to-split.md)).
- Ignoring cold starts when scaling to zero; warm one replica if users wait on it.
- Sending personal or confidential data to a provider without checking terms and data residency.

## Provider mapping

| Azure | AWS | Google Cloud | Open source |
|---|---|---|---|
| Microsoft Foundry (model catalog and deployments); Container Apps (including serverless GPUs) for self-hosting | Amazon Bedrock; SageMaker AI endpoints; ECS for self-hosting | Vertex AI (Model Garden, endpoints); Cloud Run with GPUs | vLLM, SGLang, Ollama, llama.cpp; Hugging Face Text Embeddings Inference; LiteLLM as a gateway |

## Say it in an interview

> Large language models come from a managed API behind one internal client with pinned versions,
> timeouts and token budgets; small specialised models such as the embedder run as our own
> container that scales to zero, so we pay for GPUs or memory only when they work.
