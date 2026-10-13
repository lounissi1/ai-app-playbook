---
id: card-ai-evaluation
type: card
title: AI evaluation
status: draft
updated: 2026-10-13
tags: [ai, evaluation, testing, quality, llm]
related: [card-rag, card-embeddings-vector-search, card-model-serving, guide-test, guide-monitor]
kind: pattern
stages: [4, 8]
---

# AI evaluation

## In one sentence

AI evaluation measures how good a model-powered feature is, using a fixed set of test cases and
scores, so that every change to prompts, models or data can be compared with the last version.

## Why it exists

Normal tests check exact outputs; AI outputs vary and can be fluent but wrong. Without
measurement, teams change a prompt, try three examples, and ship a regression. Evaluation turns
"it seems better" into numbers that run in CI like any other test.

## How it works

```
 evaluation set ─▶ run the feature ─▶ score each output ─▶ compare with baseline ─▶ pass / fail in CI
 (questions,                           (exact checks,
  expected sources,                     metrics, LLM judge,
  reference answers)                    human review)
```

1. **Build an evaluation set**: 30–200 realistic cases with expected sources or reference answers,
   including hard and "should refuse" cases. Version it in the repository.
2. **Choose scores** that match the feature:
    - Retrieval: did the right passage appear in the top k (recall@k, MRR)?
    - Answers: faithful to sources, relevant, complete, correct citations, refuses when it should.
    - Operational: latency, tokens, cost per answer.
3. **Score** with code checks where possible, a judging model for fuzzy qualities (checked
   against human labels), and periodic human review.
4. **Gate in CI**: fail the pull request if a score drops below the baseline by more than an agreed margin.
5. **Monitor in production**: sample real traffic, collect user feedback, and add failures to the
   evaluation set.

## Analogy

A teacher's standard exam. The same questions are given to every version of the student, so
progress is measurable instead of anecdotal.

## Key terms

| Term | Meaning |
|---|---|
| Evaluation set (golden set) | Fixed, versioned test cases with expected results |
| Baseline | The scores of the current production version |
| Faithfulness | The answer is supported by the retrieved sources |
| Recall@k | Share of cases where a correct passage appears in the top k results |
| LLM-as-judge | Using a model to grade outputs against a rubric |
| Online evaluation | Scoring samples of real production traffic |

## Pitfalls

- Evaluating with a handful of hand-picked examples.
- Only scoring final answers, so retrieval problems stay hidden.
- Trusting a judging model without checking it against human labels.
- An evaluation set that never grows; production failures must become new cases.
- Tuning prompts until the evaluation set passes (overfitting); keep a held-out set.

## Provider mapping

| Azure | AWS | Google Cloud | Open source |
|---|---|---|---|
| Microsoft Foundry evaluations; Application Insights for tracing | Bedrock evaluations; CloudWatch | Vertex AI Gen AI evaluation service; Cloud Trace | Ragas, DeepEval, promptfoo, Inspect; Langfuse or Arize Phoenix for tracing |

## Say it in an interview

> Every AI feature has a versioned evaluation set; CI scores retrieval recall and answer
> faithfulness against the production baseline and blocks regressions, and sampled production
> failures are added back to the set.
