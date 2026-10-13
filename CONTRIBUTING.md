# Contributing: the data model of this handbook

Every page in `docs/` is exactly **one** of five document types. Each type has a fixed
front-matter schema and a fixed list of sections, in a fixed order. Never mix types on one page.

## Rules that apply to every page

1. **One concept, one place.** If something is explained on another page, link to it with
   `related:`. Never copy the explanation.
2. **Cloud-neutral first.** Use neutral terms in the body ("container registry", "secrets store").
   Name specific services only in the *Provider mapping* section or in `starters/`.
3. **Plain language.** Short sentences, active voice. Define every acronym on first use, or link its card.
4. **No secrets, ever.** Use placeholders like `<subscription-id>`. Never real names, keys or IPs.
5. **Status is honest.** `planned` → `draft` → `reviewed` → `stable`. Only `stable` pages are
   considered complete. A page moves to `reviewed` after it has been used on a real project.
6. **File names** are lowercase, hyphenated, and match the `id` without its prefix
   (`id: card-container-image` → `docs/cards/container-image.md`). Stage guides add their
   loop position in front (`id: guide-build` → `docs/guides/03-build.md`).
7. **`related:` lists only ids that exist.** Planned pages are listed in `docs/cards/index.md`
   until they are written.

## Common front matter (all types)

```yaml
---
id: <type-prefix>-<slug>          # unique; prefixes: cheat, guide, card, decision, checklist
type: cheatsheet | guide | card | decision | checklist
title: <Title Case name>
status: planned | draft | reviewed | stable
updated: YYYY-MM-DD
tags: [<lowercase>, <keywords>]
related: [<id>, <id>]             # ids of other pages; no free text
---
```

Starters (`starters/`) are code, not docs; each starter folder has a `README.md` that follows
the **starter** schema below.

---

## Type 1: Cheat sheet

The whole subject on one page. Exactly one per handbook (`docs/cheatsheet.md`).

Extra front matter: none.

Sections, in order:

1. `## The loop` · one diagram
2. `## Three questions` · where it runs, how resources are created, how code gets there
3. `## One tool per job` · table: job · default · alternatives
4. `## Minimum for production` · list
5. `## Words to know` · term and one-line definition, each linking to its card

## Type 2: Guide

One stage of the delivery loop, or one foundation topic, done step by step.

Extra front matter:

```yaml
stage: 1-8 | foundation          # loop position; foundation = architecture, security, infrastructure, cost, AI agents
inputs: [<what you need before starting>]
outputs: [<what exists when you finish>]
```

Sections, in order:

1. `## Goal` · one sentence
2. `## Inputs and outputs` · two short lists
3. `## Steps` · numbered; each step is one action
4. `## Files to copy` · links into `starters/`
5. `## Done when` · checklist with `- [ ]`
6. `## Common mistakes` · list
7. `## Using an AI agent` · what to delegate, what to review yourself

## Type 3: Card

One concept, tool or pattern. Cards are the reference layer.

Extra front matter:

```yaml
kind: concept | tool | pattern
stages: [<stage numbers where it matters>]
```

Sections, in order:

1. `## In one sentence`
2. `## Why it exists` · the problem it solves
3. `## How it works` · mechanism, with a diagram if useful
4. `## Analogy` · one everyday comparison
5. `## Key terms` · term and definition
6. `## Pitfalls`
7. `## Provider mapping` · table: Azure · AWS · Google Cloud · Open source
8. `## Say it in an interview` · one or two sentences

## Type 4: Decision tree

Choosing between options for one question.

Extra front matter:

```yaml
question: <the question, ending with ?>
default: <the option this handbook picks when nothing else applies>
```

Sections, in order:

1. `## The question`
2. `## Decision tree` · numbered yes/no questions leading to an option
3. `## Options compared` · table with the same columns for every option
4. `## Default and why`
5. `## When to revisit` · signals that the choice should change

## Type 5: Checklist

A gate you pass before moving on.

Extra front matter:

```yaml
gate: <when this checklist is used>
```

Sections, in order:

1. `## When to use`
2. `## Checklist` · `- [ ]` items, grouped with `###` headings; each item links to its guide or card
3. `## If an item fails`

## Starter README schema (`starters/<cloud>/<area>/README.md`)

1. `# <Starter name>`
2. `## What it creates`
3. `## Prerequisites`
4. `## How to use` · copy, replace placeholders, run
5. `## Placeholders` · table: placeholder · meaning · example
6. `## Proven on` · project and date it was last verified; `not yet verified` until then

---

## Workflow for adding a page

1. Copy the matching file from `templates/`.
2. Fill every section. If a section truly doesn't apply, write `Not applicable` and why.
3. Set `status: draft` and today's `updated` date.
4. Add the page to `mkdocs.yml` navigation.
5. Open a pull request using the checklist in `.github/pull_request_template.md`.
