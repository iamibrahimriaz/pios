---
Title: Core Principles
Module: 12-metrics
Section: core
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the principles that govern judgment when defining metrics.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - constitution/core/03-Core-Principles.md
Outputs:
  - Consistent measurement judgment
Related Modules:
  - 13-operations
Tags:
  - Metrics
  - Principles
---

# Core Principles

---

# Principle Statement

> A product measured by the wrong number gets worse on purpose,
> and every individual decision along the way looks defensible.

---

# Principle 1 — Exactly One North Star

The purpose of a north star is to resolve disagreements between teams about what progress means.

Two north stars resolve nothing. They relocate the argument and give each side a number to hold.

---

# Principle 2 — The North Star Measures User Value, Not Company Convenience

Revenue is a consequence of a north star, not one. It measures what the company received rather
than what the user got, and it moves last, which makes it useless for steering.

Measure the unit of value the revenue is paid for.

---

# Principle 3 — A Number That Cannot Fall Measures Elapsed Time

Total registered users, cumulative records, revenue to date. No decision changes their direction.

The check is one question: could this number fall if the product got worse? If not, replace it with
a rate or a cohort measure.

---

# Principle 4 — Every Metric Can Be Gamed, So Write Down How

Every metric has a degenerate behavior that raises it without making the product more valuable, and
organizations reliably find it.

Writing the answer down is what produces the counter-metrics. Skipping it is how a team optimizes a
product into a worse one in complete good faith.

---

# Principle 5 — A Definition Must Survive Its Author's Absence

Numerator, denominator, time window, population, exclusions. Five parts, all required.

"Active users" states none of them, which is why two teams report two figures and the difference
gets attributed to the market.

---

# Principle 6 — Every Metric Names Its Source Events

A metric with no source cannot be computed, and it will be quietly replaced by whatever number is
available.

---

# Principle 7 — Every Goal Gets a Metric

Every goal in the PRD appears here as a measured thing.

A goal with no metric was never a goal. Where something genuinely cannot be measured, that is a
finding to record — not a reason to remove the goal.

---

# Principle 8 — Distinguish What Moves Early From What Only Confirms

Leading indicators steer. Lagging indicators confirm and arrive too late to act on.

Teams tracking only lagging metrics discover problems a quarter after they could have fixed them.
Teams tracking only leading metrics never learn whether any of it mattered.

---

# Principle 9 — A Leading Indicator's Link Is an Inference

*This moves, therefore that will follow* is a causal claim with no data behind it before launch.

State the basis. An indicator whose link cannot be articulated is a number that moves and means
nothing — and it will be acted on anyway, because it moves early.

---

# Principle 10 — A Login Is Not a Return

A user who opens the product and does nothing has not retained.

Retention built on logins looks healthy while a product is being abandoned, and it is the single
most common way a retention number misleads the people relying on it.

---

# Principle 11 — Name What Must Not Get Worse

Counter-metrics with thresholds, and a stated purpose for each.

A threshold with no stated purpose is relaxed the first time it is inconvenient, and by then nobody
remembers what it protected.

---

# Principle 12 — A Target That Cannot Be Missed Is Not a Target

Every figure must be one a real result could fail.

---

# Principle 13 — Definitions and Targets Do Not Share a Confidence

A definition is a decision and can be certain. A target is a prediction about people who have not
used the product yet.

Reporting one figure for both always reports the definition's, and the targets inherit a certainty
nothing supports.

---

# Principle 14 — No Baseline Is a Fact, Not a Gap

For a new product there is no baseline. Say so, tag every target as an assumption with its basis,
and name the milestone that produces the first real one.

Do not fill the gap with an industry benchmark: it describes a different population, measured with
definitions nobody discloses.

---

# Principle 15 — An Event Not Specified Now Will Not Exist

Instrumentation is never retrofitted. The feature ships, the events do not, and the product runs
blind while somebody schedules work everyone assumed was free.

This is the one part of the module that becomes code, and it is written once.

---

# Principle 16 — Every Event Has a Metric; Every Metric Has Events

An orphan event is cost, noise and a privacy liability with no benefit.

An uncomputable metric is worse: it will be silently replaced by whatever the data allows, and
nobody will note the substitution.

---

# Principle 17 — Every Event Names a Milestone

That is what puts it in a definition of done in `10-execution`, and it is the mechanism by which
instrumentation ships with the feature rather than after it.

An event with no milestone is an event nobody is building.

---

# Principle 18 — Identity Resolution Is Part of the Specification

Across sessions, across devices, before signup.

Without it, every cohort and retention metric is uncomputable — and it is the section most often
left out of an instrumentation plan.

---

# Principle 19 — An Event Property Is Data Leaving the System

A regulated column captured as a property means regulated data now lives in a third-party system
with different retention, different access control and possibly a different jurisdiction.

This is a compliance exposure, not a data-quality question, and "we will be careful with PII" is
not a mechanism.

---

# Principle Hierarchy

```
One north star, representing user value
   ↓
Defined so anyone could compute it
   ↓
Split into leading and lagging
   ↓
Guarded by counter-metrics
   ↓
Targeted, with baselines or an admitted absence
   ↓
Instrumented, event by event, per milestone
```

Each level depends on the one above. A careful definition of the wrong metric is wasted precision;
events specified before the metrics exist are events chosen for being easy to log.

---

# Common Violations

- Two north stars.
- Revenue as the north star.
- A cumulative count as a primary metric.
- The gaming question never asked.
- "Active users" as a definition.
- A metric with no source events.
- A PRD goal with no metric.
- Leading and lagging mixed together.
- A leading indicator link asserted with no basis.
- Retention measured by logins.
- No counter-metrics, or thresholds with no purpose.
- Targets that cannot be missed.
- One confidence figure for definitions and targets.
- An industry benchmark presented as this product's target.
- Metrics with no events, or events with no metrics.
- Events with no milestone.
- Identity resolution unspecified.
- A regulated column as an event property.

---

# Self Assessment

- Is there one north star, and does it measure user value?
- Could it fall if the product got worse?
- Do I know how each metric would be gamed?
- Does every definition state all five parts?
- Does every goal have a metric?
- Does every leading indicator state its basis?
- Is "returning" an action?
- Does every counter-metric have a threshold and a purpose?
- Could every target be missed?
- Did I report two confidences?
- Does every event have a metric and a milestone?
- Is identity resolution specified?
- Did I check every property against the regulated columns?

---

> **Core Principle**
>
> Definitions can be corrected for as long as the product exists.
>
> The events can only be built while somebody is building — which
> makes one section of this module permanent and the rest advisory.
