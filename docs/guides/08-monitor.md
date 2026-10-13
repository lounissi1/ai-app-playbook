---
id: guide-monitor
type: guide
title: Monitor
status: draft
updated: 2026-10-13
tags: [observability, logs, traces, alerts]
related: [guide-operate, guide-plan, guide-cost]
stage: 8
inputs: [a running application]
outputs: [alerts that reach a person, dashboards, input for the next plan]
---

# Monitor

## Goal

Know what users experience, be told when it breaks, and feed what you learn into the next plan.

## Inputs and outputs

**Inputs**

- A running application

**Outputs**

- Logs, metrics and traces in one place
- A small set of alerts that reach a person
- Issues created from what monitoring revealed

## Steps

1. Send all container logs to the cloud's log service. Use structured (JSON) logs.
2. Instrument the application with **OpenTelemetry** so requests are traced across services,
   database calls and external APIs.
3. Track the four golden signals: **latency, traffic, errors, saturation**.
4. Create **three alerts** to start: error rate of the API, failed background jobs, failed deploys.
   Each alert links to its runbook.
5. Build one dashboard with those signals and recent deploys.
6. Set a daily cap on log ingestion and avoid debug-level logging in the cloud.
7. Once a month, turn what you saw into issues: slow endpoints, noisy alerts, cost surprises.

## Files to copy

- `templates/runbook.md`
- `templates/postmortem.md`

## Done when

- [ ] Logs from every part are searchable in one place
- [ ] A single request can be traced end to end
- [ ] Three alerts exist and have reached you at least once in a test
- [ ] A dashboard shows the golden signals
- [ ] Log ingestion has a cap

## Common mistakes

- Dozens of alerts that nobody reads. Start with three that matter.
- Logs containing personal data or secrets.
- Monitoring set up but never feeding back into planning.

## Using an AI agent

**Delegate:** instrumentation code, log queries, dashboards, summaries of incidents from logs.

**Review yourself:** which alerts exist and who receives them, and what data is allowed in logs.
