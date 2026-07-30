---
Title: MVP
Module: 04-problem
Section: knowledge/validation
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Clarify what an MVP tests, and that module 07 draws the line rather than this one.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 04-problem/knowledge/validation/Prototype.md
Outputs:
  - MVP as a validation method within validation_plan
Related Modules:
  - 07-strategy
  - 10-execution
Tags:
  - Problem
  - MVP
  - Method
---

# MVP

---

# What It Is

The smallest thing that solves the sharpest problem for one segment, well enough that someone will use it
instead of their workaround.

Two properties define it, and both are frequently lost:

| | |
| --- | --- |
| **Minimum** | Nothing in it that is not required to solve the one problem |
| **Viable** | It genuinely solves that problem — a partial solution is not an MVP, it is a demo |

The framework is explicit about ownership: **`07-strategy` draws the MVP line.** This file covers what an MVP
can validate that a prototype cannot, because that is the part belonging to module 04.

| A prototype tests | An MVP tests |
| --- | --- |
| Comprehension, task completion, output acceptability | Whether someone will use it in real work, repeatedly, at a cost |

The difference is that an MVP carries real stakes: real data, real consequences, and usually real money. That is
what makes its signal credible when everything cheaper is not.

---

# When It Applies

As a validation method in Stage 6 only where the load-bearing belief is about **sustained use or willingness to
pay** — the two things nothing cheaper can establish. The scope decision itself belongs to `07-strategy`, and
the sequencing to `10-execution`.

---

# How to Apply It Here

**Say which belief only an MVP can test.** If a prototype or a Wizard of Oz test would answer the question,
it is the wrong method — it costs an order of magnitude more and answers later.

**Keep it to the single sharpest problem.** An MVP addressing three problems tests none of them, because a
negative result cannot be attributed.

**Define what constitutes viable before building.** The bar is the workaround from `Current-Solutions.md`, plus
the switching cost from `03-user`. Below that bar, non-adoption tells you nothing about the problem.

**Set the invalidating result in advance.** How many users, doing what, over what period, for the belief to
survive? Without it, an MVP produces months of ambiguous activity.

**Instrument it.** An MVP with no measurement produces anecdotes. `12-metrics` defines events properly, but even
a validation MVP needs to know who returned and who did not.

---

# Where It Misleads

**"MVP" is the most abused term in product work**, and in practice it usually means "version one, with the
features we ran out of time for". That is not a minimum and it may not be viable.

**Minimum gets optimized against and viable gets quietly dropped.** A product that half-solves the problem
produces a false negative: users reject it and the team concludes the problem was not real. This is the most
expensive error available at this stage.

**An MVP is treated as validation of the whole idea.** It validates one problem, one segment, one price.
Extrapolating from it to a market is `02-market`'s work, and it needs more than one cohort.

**It becomes the product by default.** Decisions made for speed harden into architecture, and `09-technology`
inherits them without having chosen them. If it will not be thrown away, say so, and design accordingly.

**Building one is the most satisfying way to avoid cheaper tests.** The plan should be ordered by cheapest test
of the most load-bearing belief; an MVP proposed first is usually the plan reordered by enthusiasm.

---

# Related

| | |
| --- | --- |
| `Prototype.md` | The cheaper method to exhaust first |
| `Success-Criteria.md` | The invalidating result |
| `07-strategy` | Where the MVP line is actually drawn |
| `10-execution` | Where it becomes Milestone Zero and a sequence |

---

> **Concept Note**
>
> Minimum and viable are both load-bearing words.
>
> A product that half-solves the problem produces a false negative,
> and a false negative here kills a real idea.
