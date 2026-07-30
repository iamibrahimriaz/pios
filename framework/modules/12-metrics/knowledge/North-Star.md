---
Title: North Star
Module: 12-metrics
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Ratify exactly one metric, run the vanity check and the gaming question.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 12-metrics/core/06-Framework.md
Outputs:
  - north_star_metric
Related Modules:
  - 01-idea
  - 11-growth
Tags:
  - Metrics
  - North Star
  - Method
---

# North Star

---

# What It Is

Exactly **one** number representing value delivered to the user. `01-idea` nominated a candidate; this module ratifies, defines,
guards and targets it.

One, because the purpose is to resolve disagreements. Two north stars resolve nothing; they relocate the argument.

| Usually wrong | Usually right |
| --- | --- |
| Revenue | The unit of value the revenue is paid for |
| Registered users | Users completing the core job in a period |
| Sessions | Jobs completed per active user |
| Page views | Time saved, or output produced |

Two tests, both required:

> **The vanity check.** Could this number fall if the product got worse?
>
> If not, it is a cumulative count and it will rise forever regardless of what happens. Replace it with a **rate** or a **cohort
> measure**.

> **The gaming question.** What would someone do to make this number rise without the product becoming more valuable?

Every metric has an answer. Writing it down produces the counter-metrics in Move 4.

---

# When It Applies

In Move 1 (Choose), first — defining before choosing produces careful definitions of the wrong metric.

---

# How to Apply It Here

**Record two rejected alternatives with reasons.** The reasons are the actual content of this move: naming why the obvious candidate
would mislead is what makes the choice reviewable a year later.

**Check the `01-idea` candidate rather than inheriting it.** `03-user` and `04-problem` may have established that the valuable outcome
is something else entirely. Changing it is expected, not a reversal.

**Do not choose revenue.** It is a consequence of a north star, it measures the company's convenience rather than the user's outcome,
and it moves last — which makes it useless for steering.

**Answer the gaming question honestly and in writing.** The plausible degenerate behavior, named. That answer is the input to
`Success-Metrics.md`'s counter-metrics.

**Tie it to the value claim.** `04-problem`'s cost per occurrence and `06-business`'s capture share describe what the product claims to
change. The north star should measure that.

---

# Where It Misleads

**Two or three north stars are chosen to avoid excluding anything.** The result is that no disagreement is settled, which was the only
reason to have one.

**A cumulative count passes review because it is easy to compute.** Total users, total records, total revenue to date — each measures
elapsed time and cannot be steered by. The vanity check exists precisely because these look like progress.

**Activity is chosen over outcome.** `01-idea` made the same point: a product can be used heavily by someone it is failing.

**The gaming answer is treated as an insult to the team.** It is a property of the metric, not of anyone's integrity — and the failure it
predicts happens in complete good faith.

**One number is expected to describe the product.** It arbitrates; it does not explain. Counter-metrics and leading indicators are what
make it safe to use.

---

# Related

| | |
| --- | --- |
| `Success-Metrics.md` | Definitions and counter-metrics |
| `Leading-Indicators.md` | What moves before it |
| `01-idea` `North-Star.md` | The candidate, and why it was only a candidate |
| `11-growth` | The activation event, carried not redefined |

---

> **Concept Note**
>
> One number, representing what the user gets, that could go down.
>
> Then write what someone would do to raise it dishonestly — that
> sentence is where the counter-metrics come from.
