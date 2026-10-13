---
id: decision-when-to-split
type: decision
title: When to split a service?
status: draft
updated: 2026-10-13
tags: [architecture, services, microservices, scaling]
related: [card-reference-architecture, card-model-serving, card-background-jobs, guide-architecture, decision-which-hosting]
question: Should this component run as its own service?
default: Keep it in the existing service
---

# When to split a service?

## The question

Should a component (a module, a model, a feature) keep running inside an existing service, or
become its own separately deployed and scaled service?

## Decision tree

1. Is the work slow (more than about a second) but uses the same code and libraries as the API?
   - **Yes** → *Background job*: same image, run as a worker with a different start command.
     See [background jobs](../cards/background-jobs.md).
   - **No** → go to 2.
2. Does it need very different resources: several GB of memory, a GPU, or a long warm-up such as
   loading a large model?
   - **Yes** → **Split it.** Otherwise every replica of the host service pays that cost.
   - **No** → go to 3.
3. Does its load differ sharply from the host's (bursty batch versus steady traffic, or idle
   most of the day)?
   - **Yes** → **Split it**, so each scales on its own signal, ideally down to zero.
   - **No** → go to 4.
4. Does it need a different language or runtime, or a release cycle owned by another team?
   - **Yes** → **Split it.**
   - **No** → go to 5.
5. Must it be isolated for security or compliance (handles secrets, untrusted input, regulated data)?
   - **Yes** → **Split it.**
   - **No** → **Keep it in the existing service** (default).

## Options compared

| Option | Deploys | Scales | Extra cost | Extra complexity | Best for |
|---|---|---|---|---|---|
| **Module in the same service** | With the host | With the host | None | None | Most features |
| Worker from the same image | With the host image | On queue length | Small | Low: a queue | Slow work, same code |
| Separate service | On its own | On its own | One more service | Medium: network calls, versioning, auth between services | Heavy models, different load or runtime |
| Managed AI API instead | Not at all | By the provider | Per call or token | Low, plus vendor dependence | Standard models where data may leave your boundary |

## Default and why

Keep code together until a concrete reason appears. Every split adds a network hop, a deployment,
monitoring, and a contract that must stay compatible. A well-structured single service (a
"modular monolith") is easier to run and can still be split later along its module boundaries.

**Typical split worth making:** an API that loads a 2 GB embedding model at start-up. Inside the
API, every replica needs that memory and starts slowly. As its own *embedder service*, the API stays
small, the embedder scales from zero to one on demand, and both use the same pinned model
version, checked by a test that compares their outputs.

## When to revisit

- One part of the service dominates memory, CPU or start-up time.
- Deploys of one feature keep blocking or breaking another.
- A component's traffic pattern makes the whole service over-provisioned.
- A different team needs to own and release it.
- Conversely: two services always change and deploy together; consider merging them back.
