---
id: guide-test
type: guide
title: Test
status: draft
updated: 2026-10-13
tags: [testing, ci, quality, scanning]
related: [guide-build, guide-code, decision-which-ci]
stage: 4
inputs: [a pull request]
outputs: [a pass or fail signal on every change]
---

# Test

## Goal

Every change gets an automatic pass or fail signal before it can merge.

## Inputs and outputs

**Inputs**

- A pull request

**Outputs**

- Required status checks that block merging when they fail

## Steps

1. Follow the **test pyramid**: many fast unit tests, fewer integration tests (real database in a
   container), a few end-to-end tests of the most important user flows.
2. Add linters and formatters; run them in CI so style is never discussed in reviews.
3. Turn on **dependency scanning** (for example Dependabot) and **code scanning**.
4. Scan built images for known vulnerabilities.
5. Run the fast checks on every pull request and the slow ones on merge to `main` or nightly.
6. Mark the checks as **required** in branch protection so red means "cannot merge".
7. Make failures readable: the job name and first error line should say what broke.

## Files to copy

- `starters/azure/workflows/ci.yml` (planned)
- `.github/workflows/docs.yml` (example of a required check for this repository)

## Done when

- [ ] Unit tests run on every pull request
- [ ] At least one integration test uses a real database
- [ ] Linting, dependency and code scanning enabled
- [ ] Checks are required in branch protection
- [ ] A typical pull request gets its result in under ten minutes

## Common mistakes

- Test fixtures more permissive than the real system, so tests pass while production breaks.
- Flaky tests that everyone re-runs until green; fix or remove them.
- Scanning turned on but alerts never read.
- Coverage targets chased with tests that assert nothing.

## Using an AI agent

**Delegate:** writing tests from acceptance criteria, generating edge cases, explaining failing
runs from the logs.

**Review yourself:** that each test would fail if the behaviour broke, and that mocks match the
real interfaces they replace.
