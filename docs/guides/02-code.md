---
id: guide-code
type: guide
title: Code
status: draft
updated: 2026-10-13
tags: [git, branches, pull-requests, configuration]
related: [guide-plan, guide-build, guide-security]
stage: 2
inputs: [an issue with a clear finish line]
outputs: [reviewed code merged to main]
---

# Code

## Goal

Change the code in small, reviewed steps, with all configuration coming from the environment.

## Inputs and outputs

**Inputs**

- An issue with a "Done when" list

**Outputs**

- A merged pull request that closes the issue
- Code that runs the same way locally and in the cloud

## Steps

1. Create a branch from `main` named after the issue, for example `42-health-endpoints`.
2. Read every setting that differs between places from **environment variables**: database
   address, storage location, API keys, feature switches. Give each a safe local default.
3. Keep a committed `.env.example` listing every variable with placeholder values. Never commit `.env`.
4. Add two health endpoints:
   - `/healthz`: the process is alive (no dependency checks)
   - `/readyz`: dependencies are reachable (database, cache); used before sending traffic
5. Write or update tests next to the code you change.
6. Commit in small steps with clear messages.
7. Open a pull request. Write `Closes #<issue>` in the description and fill in the checklist.
8. Get a review. Fix what the review and CI report. Merge only when CI is green.

## Files to copy

- `.github/pull_request_template.md`
- `templates/spec.md` (when handing the issue to an AI agent)

## Done when

- [ ] No hard-coded hosts, ports, paths or credentials
- [ ] `.env.example` lists every variable
- [ ] `/healthz` and `/readyz` respond
- [ ] Pull request reviewed, CI green, issue closed by the merge

## Common mistakes

- `localhost` hidden in code or in front-end build variables that are frozen at build time.
- Writing files to local disk that must survive a restart. Use object storage instead.
- Large pull requests that mix several changes; reviewers miss things.
- Merging with red CI "just this once".

## Using an AI agent

**Delegate:** writing the change from a spec, writing tests, explaining unfamiliar code, finding
every hard-coded host or path.

**Review yourself:** the diff, line by line for security-sensitive parts; that tests actually
assert the behaviour; that no secret or real identifier slipped in.
