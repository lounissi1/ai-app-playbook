---
id: guide-plan
type: guide
title: Plan
status: draft
updated: 2026-10-13
tags: [planning, issues, specs, adr]
related: [guide-code, guide-monitor, checklist-new-app]
stage: 1
inputs: [a goal or problem, feedback from monitoring]
outputs: [issues on a board, specs for larger work, ADRs for decisions]
---

# Plan

## Goal

Turn a goal into small, testable pieces of work that each have a clear finish line.

## Inputs and outputs

**Inputs**

- A goal, a user need or a problem report
- What monitoring and incidents taught you in the previous loop

**Outputs**

- Issues on a project board, each small enough to finish in a day or two
- A written spec for any change bigger than one issue
- An architecture decision record (ADR) for every choice that would be costly to reverse

## Steps

1. Write the goal in one sentence: what will exist, and for whom.
2. For larger work, write a spec with `templates/spec.md`: requirements, constraints,
   acceptance criteria, and what is out of scope.
3. Split the spec into issues with `.github/ISSUE_TEMPLATE/task.md`. Each issue has a
   "Done when" list.
4. Put the issues on one project board with columns *To do → In progress → In review → Done*.
5. Label issues by area and type (for example `infra`, `backend`, `bug`, `docs`).
6. For each significant choice (hosting, database, framework), write an ADR with
   `templates/adr.md` before building.
7. Pick the next issue only when the current one is done. Limit work in progress.

## Files to copy

- `templates/spec.md`
- `templates/adr.md`
- `.github/ISSUE_TEMPLATE/task.md`

## Done when

- [ ] The goal is written in one sentence
- [ ] Every issue has a "Done when" list
- [ ] Issues are on a board and ordered
- [ ] Costly-to-reverse choices have an ADR

## Common mistakes

- Issues that say *what to work on* but not *when it is finished*.
- Planning in a separate document that never links to code. Use issues so pull requests can
  close them (`Closes #42`).
- Starting new ideas mid-stream. Park them in an ideas list instead.
- Skipping ADRs, then forgetting months later why a choice was made.

## Using an AI agent

**Delegate:** drafting specs from your notes, splitting a spec into issues, first drafts of ADRs
with the options laid out.

**Review yourself:** the goal, the scope boundary, the acceptance criteria and the final decision
in each ADR. These are judgments, and you are accountable for them.
