---
id: card-reference-architecture
type: card
title: Reference app architecture
status: draft
updated: 2026-10-13
tags: [architecture, layers, frontend, api, workers, cache, database, storage]
related: [guide-architecture, card-background-jobs, decision-when-to-split, card-model-serving, decision-which-hosting]
kind: pattern
stages: [1, 2, 6, 7]
---

# Reference app architecture

## In one sentence

Most web applications, AI-powered or not, are built from the same seven layers: a web frontend,
an API, background workers with a queue, a cache, a database, object storage, and (for AI apps)
model services. Each layer has one job and talks to the others in a fixed direction.

## Why it exists

Without a shared picture, every new app is designed from scratch, responsibilities blur (the API
renders PDFs, the frontend talks straight to the database, files live on container disk) and the
app becomes hard to scale, secure and deploy. A reference architecture gives a default shape that
fits most apps, so design time goes to what is actually different.

## How it works

```
                     Users (browser, mobile, other systems)
                                     │ HTTPS
                           ┌─────────▼─────────┐
                           │   Web frontend    │
                           └─────────┬─────────┘
                                     │ HTTPS + JSON
 ┌───────────┐  fast reads ┌─────────▼─────────┐  model calls  ┌──────────────┐
 │   Cache   │◀───────────▶│        API        │──────────────▶│ AI services  │
 └───────────┘             └──┬─────────────┬──┘               └──────▲───────┘
                              │ enqueue     │ read / write            │
                        ┌─────▼─────┐       │                         │
                        │   Queue   │       │                         │
                        └─────┬─────┘       │                         │
                        ┌─────▼─────┐       │      model calls        │
                        │  Workers  │───────┼─────────────────────────┘
                        └─────┬─────┘       │
                              │ read / write│
                 ┌────────────▼─────────────▼────────────┐
                 │    Database         Object storage    │
                 └───────────────────────────────────────┘
```

| Layer | Job | Holds state? | Scales on |
|---|---|---|---|
| Web frontend | Shows pages; calls the API only | No | Visitors |
| API | Validates requests, enforces auth, reads and writes data, answers fast (< 1 s) | No | Requests |
| Queue | Holds work to be done later, so the API can answer immediately | Briefly | Messages waiting |
| Workers | Do slow or heavy work: imports, reports, image processing, AI batch jobs | No | Queue length |
| Cache | Keeps hot or expensive results in memory for fast reads | Disposable | Memory |
| Database | The source of truth for records; also vectors when using a vector extension | **Yes** | Data size, queries |
| Object storage | Files: uploads, images, rasters, model files, exports | **Yes** | Data size |
| AI services | Generate text, compute embeddings, run models (see [model serving](model-serving.md)) | No | Requests, tokens |

Four rules keep the layers clean:

1. **State lives only in the database and object storage.** Everything else can be restarted,
   replaced or scaled at any time.
2. **The frontend talks only to the API.** It never connects to the database, queue or storage
   directly (signed upload URLs issued by the API are the exception).
3. **Anything slower than about a second goes through the queue** to a worker. The API returns a
   job id; the frontend asks for the result later.
4. **Each layer is configured by environment variables**, so the same image runs locally and in
   the cloud.

## Analogy

A restaurant. The dining room is the frontend, the waiter is the API, order tickets are the
queue, cooks are the workers, the pass where ready dishes wait is the cache, the pantry ledger is
the database, the cold room is object storage, and the specialist pastry chef you call for
desserts is the AI service. Waiters never cook, and nothing important is kept in a waiter's pocket.

## Key terms

| Term | Meaning |
|---|---|
| Stateless | Keeps nothing between requests that cannot be lost; safe to restart or copy |
| Source of truth | The one place a fact is stored; every other copy can be rebuilt from it |
| Synchronous | The caller waits for the answer (API request) |
| Asynchronous | The caller gets a receipt now and the result later (queue and worker) |
| Signed URL | A short-lived link that lets a browser upload or download one file directly |
| Broker | The software that runs the queue; often the same product as the cache |

## Pitfalls

- Doing slow work inside API requests; requests time out and the API stops answering.
- Saving uploads to container disk; they disappear on the next restart or deploy.
- Treating the cache as a database; it can be emptied at any moment.
- Loading a large model into every API replica; memory and start-up time explode
  (see [when to split a service](../decisions/when-to-split.md)).
- Splitting into many small services on day one; start with these layers and split only for a reason.

## Provider mapping

| Layer | Azure | AWS | Google Cloud | Open source |
|---|---|---|---|---|
| Web frontend | Static Web Apps or Container Apps | Amplify or S3 + CloudFront | Firebase Hosting or Cloud Run | Next.js, Nginx |
| API and workers | Container Apps (apps and jobs) | ECS on Fargate | Cloud Run (services and jobs) | FastAPI, Express, Docker |
| Queue | Service Bus, Storage Queues | SQS | Pub/Sub, Cloud Tasks | Redis, RabbitMQ |
| Cache | Azure Managed Redis | ElastiCache | Memorystore | Redis, Valkey |
| Database | Database for PostgreSQL flexible server | RDS or Aurora PostgreSQL | Cloud SQL or AlloyDB | PostgreSQL (+ pgvector, PostGIS) |
| Object storage | Blob Storage | S3 | Cloud Storage | MinIO |
| AI services | Microsoft Foundry, Container Apps | Bedrock, SageMaker AI | Vertex AI | vLLM, Ollama |

## In short

> Most apps fit a standard layered shape: a stateless frontend, API and workers, a queue for
> anything slow, and state only in a managed database and object storage. AI capabilities sit
> behind their own service boundary so heavy models scale independently of the API.
