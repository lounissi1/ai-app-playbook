---
id: guide-architecture
type: guide
title: Architecture
status: draft
updated: 2026-10-13
tags: [architecture, design, adr, layers]
related: [card-reference-architecture, card-background-jobs, decision-when-to-split, decision-which-hosting, guide-plan, guide-infrastructure]
stage: foundation
inputs: [the problem and its users, expected load and data volumes, budget]
outputs: [an architecture diagram, a list of services, ADRs for each major choice]
---

# Architecture

## Goal

Decide the parts of the application, what each one does and how they connect, before writing
infrastructure or deployment code.

## Inputs and outputs

**Inputs**

- What the app does and for whom (one paragraph)
- Rough numbers: users, requests per day, data volume, longest-running task
- Budget and any data-residency or security constraints

**Outputs**

- One architecture diagram in the repository (`docs/architecture.md` or the README)
- A table of services: name, job, image, start command, how it scales
- One ADR (architecture decision record) per major choice

## Steps

1. Write the app's main user journeys as short sentences ("a farmer uploads a field boundary and
   sees a crop-health map").
2. For each journey, list the work it causes and mark each piece **fast** (under about a second)
   or **slow**.
3. Map the work onto the [reference architecture](../cards/reference-architecture.md) layers: fast
   work → API, slow work → queue and workers, records → database, files → object storage,
   repeated expensive reads → cache, models → AI services.
4. Decide where each piece of state lives. Anything not in the database or object storage must be
   safe to lose.
5. For every component that seems to need its own service, run the
   [when to split](../decisions/when-to-split.md) decision tree. Default to fewer services.
6. Choose the hosting with [which hosting](../decisions/which-hosting.md).
7. Draw the diagram: boxes for services and data stores, arrows for calls, labelled with the
   protocol (HTTPS, queue message, SQL).
8. Write the services table and one ADR per major choice (hosting, database, queue, model
   provider), using `templates/adr.md`.
9. Check the design against the [production-ready checklist](../checklists/production-ready.md)
   before building anything.

## Files to copy

- `templates/adr.md`
- `templates/spec.md` (to hand the design to an AI agent for implementation)

## Done when

- [ ] Every user journey maps to named layers
- [ ] Every piece of state has exactly one home (database or object storage)
- [ ] Every slow task goes through a queue
- [ ] Each separate service has a written reason to exist
- [ ] Diagram, services table and ADRs are committed to the repository

## Common mistakes

- Starting with microservices or Kubernetes because large companies use them.
- Designing around a tool ("we use Redis, so…") instead of around the work.
- Forgetting where files go until the first deploy loses them.
- Putting heavy models inside the API.
- Keeping the design only in someone's head or in a slide; it must live next to the code.

## Using an AI agent

**Delegate:** turning user journeys into a first diagram and services table, drafting ADRs,
listing failure modes for each component, checking the design against this guide.

**Review yourself:** every split into a separate service, where state lives, anything that costs
money every month, and whether the design is simpler than it needs to be or not simple enough.
