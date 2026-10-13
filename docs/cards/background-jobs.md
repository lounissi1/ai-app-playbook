---
id: card-background-jobs
type: card
title: Background jobs and queues
status: draft
updated: 2026-10-13
tags: [architecture, queue, workers, async, jobs]
related: [card-reference-architecture, guide-architecture, guide-operate]
kind: pattern
stages: [2, 7]
---

# Background jobs and queues

## In one sentence

A background job is work the API hands to a queue so that a separate worker process can do it
later, letting the API answer the user immediately.

## Why it exists

Some work takes seconds to hours: processing an upload, calling a slow external service,
generating a report, running a model over many records. Doing it inside an API request ties up
the API, hits request timeouts and loses the work if the process restarts. A queue decouples
"asking for work" from "doing work".

## How it works

```
 User ──request──▶ API ──message──▶ Queue ──▶ Worker ──result──▶ Database / object storage
   ▲                │                                                    │
   └── job id ──────┘          later: User ──"status of job?"──▶ API ────┘
```

1. The API validates the request, writes a job record (status `queued`) and puts a message on the queue.
2. The API returns the job id at once (HTTP `202 Accepted`).
3. A worker takes the message, does the work, writes the result and sets the status to `done` or `failed`.
4. The frontend polls the job status, or is notified by a webhook or server-sent event.
5. Workers scale on **queue length**, not on web traffic; with nothing queued they can scale to zero.

Scheduled jobs (every night, every hour) follow the same idea, triggered by a timer instead of a message.

## Analogy

Dropping a coat at a dry cleaner. You get a ticket straight away and leave; the cleaning happens
in the back, and you come back with the ticket to collect it.

## Key terms

| Term | Meaning |
|---|---|
| Producer / consumer | Who puts messages on the queue / who takes them off |
| Idempotent | Running the same job twice gives the same result; needed because messages can be delivered twice |
| Retry with backoff | Trying a failed job again after growing delays |
| Dead-letter queue | Where messages go after too many failures, for a human to inspect |
| Visibility timeout | How long a taken message stays hidden before another worker may retry it |

## Pitfalls

- Jobs that are not idempotent; a retry charges a customer twice or writes duplicate rows.
- No dead-letter queue; failing messages retry forever or vanish silently.
- Passing large files inside messages; pass a storage path instead.
- Workers built from a different code version than the API; share one image, different start command.
- No timeout on jobs; one stuck job blocks a worker indefinitely.

## Provider mapping

| Azure | AWS | Google Cloud | Open source |
|---|---|---|---|
| Service Bus or Storage Queues; Container Apps jobs (event-driven or scheduled) | SQS; ECS tasks, Lambda, EventBridge Scheduler | Pub/Sub or Cloud Tasks; Cloud Run jobs, Cloud Scheduler | Celery, RQ, Dramatiq (Python), BullMQ (Node), Temporal |

## Say it in an interview

> Anything slower than a second leaves the request path: the API enqueues a job and returns
> 202 with a job id, idempotent workers scale on queue length, and failures land in a
> dead-letter queue with an alert.
