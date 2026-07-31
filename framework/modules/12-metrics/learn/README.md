---
Title: Learn — Metrics
Module: 12-metrics
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Orient a human learner in the Metrics module — one north star, three tests, and the question of what happens when someone games it.
Audience:
  - Product Managers
  - Founders
  - Analysts
Prerequisites:
  - 11-growth/learn/README.md
  - 12-metrics/README.md
Outputs:
  - A reading path through the Metrics module
Related Modules:
  - 08-product
  - 11-growth
  - 09-technology
Tags:
  - Metrics
  - Curriculum
  - Learn
---

# Learn — Metrics

---

# What This Layer Is

The human curriculum for the Metrics module. An executing agent does not read it.

---

# What the Module Does

It defines measurable success and how it will be observed. It produces a north star
metric, success metrics, leading indicators, an instrumentation plan and targets.

Its gate is unusually strict in one place: **exactly one north star metric.** Not a
balanced set. One, with the reasoning for it.

---

# The Three Named Tests

**The computation test.** Can this metric actually be computed from data that will
exist? A metric requiring a field nobody records is a wish with a name.

**The vanity check.** Does this number go up when nothing good has happened? Registered
accounts, page views, total events — all rise with activity that has no relationship to
value.

**The gaming question.** If someone optimized this without caring about the outcome,
what would they do? Every metric can be gamed, and the question is not whether but
whether the gamed behavior is harmful.

---

# The Fourth Discipline

Instrumentation must be specified at event level for the build handoff — and every event
property is checked against **the regulated column list** from module 09.

> Putting a regulated field in an analytics event property is the same class of exposure
> as sending one to a model provider.

This is the third of the four places that list is checked. It is the one most often
skipped, because analytics feels like a reporting concern rather than a data-handling
one.

---

# Reading Order

| Read | File | What you get |
| --- | --- | --- |
| 1 | `01-Why-It-Matters.md` | Why one metric, and why definitions matter more than choices |
| 2 | `02-Learning-Objectives.md` | What you should be able to do afterward |
| 3 | `10-Common-Mistakes.md` | Vanity, gaming, uncomputable metrics |
| 4 | `16-Evaluation.md` | How to check your own metric set |
| 5 | `17-Reflection.md` | Questions after a real run |
| 6 | `19-Related-Modules.md` | Where instrumentation goes and what it inherits |
| 7 | `20-Future-Improvements.md` | What this module still does poorly |

---

# What You Should Read Instead, and When

| If you want | Read |
| --- | --- |
| To run the module | `12-metrics/core/06-Framework.md` |
| To understand a metric type or an indicator | `12-metrics/knowledge/` |
| To see a dashboard of vanity | `12-metrics/resources/15-Anti-Examples.md` |

---

> **Learn Principle**
>
> A metric is an instruction to an organization, whether or not anyone intends it that
> way.
>
> Choosing one is less than half the work. Defining it precisely, checking it can be
> computed, and asking what happens when someone optimizes it — that is the module.
