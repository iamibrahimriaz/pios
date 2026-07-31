---
Title: Evaluation
Module: 12-metrics
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Give a learner a way to test whether their metrics can be computed, gamed, or acted on.
Audience:
  - Product Managers
  - Founders
  - Analysts
Prerequisites:
  - 12-metrics/learn/10-Common-Mistakes.md
Outputs:
  - A self-assessment for measurement design
Related Modules:
  - 09-technology
  - 11-growth
Tags:
  - Metrics
  - Evaluation
  - Learn
---

# Evaluation

---

# Overview

Metrics are assessable by simulation: run the definition, imagine the gaming, and check
the fields exist.

---

# Exercise 1 — The Two-Analysts Test

Write a metric definition, then give it to two people and ask each to describe the query
they would write.

**Passing looks like.** The same query, including the same exclusions.

**Failing looks like.** They differ on the window or the population — the two places
almost every disagreement lives.

---

# Exercise 2 — Trace to the Schema

Take five metrics and, for each, name the table and field each input comes from.

**Passing looks like.** All five trace, or you identify precisely which field would need
adding and treat it as a product requirement.

**Failing looks like.** "We'll get that from analytics." Analytics records what it was
told to record.

---

# Exercise 3 — Describe the Empty Week

For each metric, describe a week where it improved and the business did not.

**Passing looks like.** Difficult for your north star, easy for at least one other metric
— which correctly identifies the vanity ones.

**Failing looks like.** Easy for the north star. That is the most consequential finding
available in this module.

---

# Exercise 4 — Game It Deliberately

Take your north star and write down how you would move it in a month without improving
anything.

**Passing looks like.** The gamed behavior is close to what you actually want. That is a
well-chosen metric.

**Failing looks like.** The gamed behavior damages the product. Then either change the
metric, or add a guardrail with a threshold.

---

# Exercise 5 — Find the Leading Indicator

For a lagging outcome you care about, propose something observable in the first session
that would predict it.

**Passing looks like.** A specific first-session behavior with a stated hypothesis for
why it predicts.

**Failing looks like.** Another lagging metric with a shorter window. A weekly report of
last week is still a report.

---

# Exercise 6 — Audit the Event Properties

Take an instrumentation plan and check each property against a list of regulated fields.

**Passing looks like.** You find one — usually free text, an email in a user identifier,
or a record reference.

**Failing looks like.** You skip it because analytics is internal. It is a transfer to a
third party.

---

# Exercise 7 — Derive a Target

Take a business model and derive the target that has to be met for it to work. Compare
with whatever target was previously stated.

**Passing looks like.** They differ, and the derived one is more informative when missed.

**Failing looks like.** No derivation is possible, which means module 06's model was not
specific enough to produce one.

---

# Rubric

| Level | Description |
| --- | --- |
| **Not yet** | Chooses metrics by name; definitions implicit; several vanity numbers |
| **Working** | Definitions written; computation assumed rather than traced |
| **Competent** | All three tests applied; leading indicator present; event properties audited |
| **Fluent** | North star chosen partly because its gamed version is acceptable, and targets derived rather than set |

---

# A Note on What Cannot Be Assessed Here

Whether the metric captures what actually matters. No test on this page can tell you
that — a metric can be computable, non-vanity, hard to game, and still measure something
peripheral.

The only real check is time: after two quarters, does moving this number correspond to
the product being better? That is unavailable now, which is why the reasoning behind the
north star is a required output. It is what makes the metric revisitable rather than
inherited.

---

> **Evaluation Principle**
>
> A metric that cannot be computed, that rises for free, or whose gamed version damages
> the product will do harm regardless of how well chosen it was.
>
> Three questions, an hour each, and they are the only three that can be answered before
> anyone starts measuring.
