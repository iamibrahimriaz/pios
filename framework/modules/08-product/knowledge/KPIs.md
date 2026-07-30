---
Title: KPIs
Module: 08-product
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Identify what each requirement implies about measurement, without defining metrics here.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 08-product/knowledge/Requirements.md
Outputs:
  - Measurement implications for 12-metrics
Related Modules:
  - 12-metrics
Tags:
  - Product
  - Metrics
  - Concept
---

# KPIs

---

# What It Is

What this module contributes to measurement: the **observable behavior** each requirement produces, handed to
`12-metrics` to define properly.

The division is strict, because a metric defined without module 12's method is a metric nobody can compute:

| This module supplies | `12-metrics` produces |
| --- | --- |
| The behavior that occurs — a note completed, a claim submitted | The event definition and its properties |
| Which outcome the requirement is meant to change | Numerator, denominator, window, population, exclusions |
| Whether the behavior is observable at all | The target, and its confidence |
| Which requirement delivers a retention mechanism | The counter-metric and the gaming question |

Module 12 also runs the privacy check — every event property compared mechanically against `09-technology`'s regulated
and PII columns. That check cannot run against metrics invented here.

---

# When It Applies

Alongside Move 3 (Behave). The behavior description already states what becomes true; noting its measurability costs
nothing at that point.

---

# How to Apply It Here

**Note the observable outcome per MUST requirement, in one line.** "The note reaches a completed state before the
appointment ends." That is enough for module 12 to build an event from.

**Flag requirements whose value is not observable.** If nothing detectable changes, the requirement cannot be measured and
its contribution cannot be verified. That is a finding worth stating early.

**Name the requirement that delivers each retention mechanism.** `11-growth` requires retention mechanisms tied to a
requirement identifier, and this is the module that knows which one.

**Do not write targets.** A target invented here is a number with no baseline, and `12-metrics` treats definitions and
targets as separately confident for exactly this reason — definitions are decisions, targets are predictions.

**Watch for the outcome that could be satisfied badly.** A requirement that reduces time by producing output requiring
careful review has moved work rather than removed it. Module 12's counter-metrics catch it; naming the risk here helps
them.

---

# Where It Misleads

**Metrics get defined in the PRD because they feel like part of the specification.** Without module 12's computation test
they are labels — "adoption rate", "engagement" — that nobody can turn into a query.

**A target written here acquires authority it has not earned.** `01-idea` made the same point about early success
metrics: a figure invented before there are users outlives every caveat attached to it.

**Activity gets named instead of outcome.** "Feature used" is the easiest measurement to imagine and the least
informative. `12-metrics`' vanity check is the guard, and the phrasing chosen here is where the drift starts.

**Measurement implications are recorded for requirements that will not ship.** Only the MUST list matters at this
stage; the rest is effort spent below the line.

**Privacy is not considered at all.** An event property naming a regulated field is a compliance problem discovered in
module 12, and it is cheaper to notice while the behavior is being written.

---

# Related

| | |
| --- | --- |
| `Success-Metrics.md` | The same boundary, stated for outcomes |
| `features/Acceptance-Criteria.md` | Observability at requirement level |
| `12-metrics` | Where definitions, targets and counter-metrics are produced |
| `11-growth` | Where retention mechanisms need a requirement identifier |

---

> **Concept Note**
>
> Say what becomes observable. Do not say what number it should
> reach.
>
> A metric without a denominator and a window is a label, and a target
> without a baseline is a guess with authority.
