---
Title: Mental Models
Module: 12-metrics
Section: core
Category: Thinking Framework
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the lenses through which a metrics plan should be examined.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 12-metrics/core/03-Core-Principles.md
Outputs:
  - Multi-perspective examination of the metrics plan
Related Modules:
  - 13-operations
Tags:
  - Metrics
  - Mental Models
---

# Mental Models

---

# Model Statement

> Metrics are how an organization decides what to do next.
>
> These lenses are ways of finding the numbers that would send it
> somewhere nobody intended.

---

# 1. The Vanity Check

**Reveals:** metrics that measure elapsed time.

Could this number fall if the product got worse?

If not, no decision changes its direction. It will rise through a good quarter and a bad one
identically, and it will be quoted in both.

**Hides:** cumulative counts are not useless — they are just not steering instruments. Total users
matters for capacity planning; it does not tell you whether to change anything.

---

# 2. The Gaming Question

**Reveals:** how the product will degrade while the numbers improve.

What would someone do to raise this without making the product more valuable?

The answers are not hypothetical. Organizations find them reliably, without anyone intending to,
because each step toward the number looks locally correct.

**Hides:** it produces counter-metrics, which can themselves be gamed. The regress stops somewhere;
the point is to stop it one step further out than nobody-thought-about-it.

---

# 3. The Two Analysts

**Reveals:** definitions that are descriptions.

Hand the definition to two people who were not involved and ask each for the number. Would they
match?

The lens works because it is the actual failure mode: two teams, two figures, and the difference
attributed to the market rather than to the definition.

**Hides:** two analysts can agree on a precisely defined metric that measures the wrong thing.

---

# 4. Goodhart's Turn

**Reveals:** what happens when the metric becomes the objective.

A measure that becomes a target stops measuring what it measured, because the system reorganizes
around it.

Ask: if every incentive in this organization pointed at this number for a year, what would the
product look like?

**Hides:** it argues for caution, not paralysis. A product with no target is not thereby well run.

---

# 5. The Login That Means Nothing

**Reveals:** retention metrics that measure access rather than use.

Take the definition of "returning". Does it require the user to do something they came to do?

A user who opens the product, looks at it, and closes it has told you nothing except that they
remembered the password.

**Hides:** some products genuinely deliver value passively — monitoring, background sync. There the
qualifying action lives somewhere other than the interface, and it still has to be named.

---

# 6. The Missing Denominator

**Reveals:** counts presented as rates.

For each metric, ask what it is divided by. Then ask whether the answer changes the interpretation.

"Two hundred notes this week" reads as growth until it is divided by users and turns out to be a
decline per user.

**Hides:** some counts are the right measure — total revenue, absolute error count. The lens asks
the question rather than assuming the answer.

---

# 7. The Uncomputable Metric

**Reveals:** definitions with no data behind them.

For each metric, name the events it is computed from. Then check that each event is specified in
§8.

An uncomputable metric does not simply go unreported. It gets **substituted** — replaced with
whatever the available data allows, silently, by whoever builds the dashboard.

**Hides:** an event's existence does not guarantee its quality. A trigger that fires inconsistently
produces a metric that drifts for reasons nobody can find.

---

# 8. The Orphan Event

**Reveals:** instrumentation added by intuition.

For each event, name the metric it feeds. Anything with no answer is cost, noise and — where it
carries user data — a liability held for no benefit.

**Hides:** debugging telemetry is legitimately not metric-feeding. It belongs in
`09-technology`'s observability section rather than here.

---

# 9. The Property Leaving the Building

**Reveals:** compliance exposure.

Read each event property and ask: is this data the security model protects? Then follow it — into a
third-party system, with different retention, different access control, possibly a different
jurisdiction.

**Hides:** nothing. It is mechanical, it has legal consequences, and it is invisible in a document
that reads well.

---

# 10. The Target Nobody Could Miss

**Reveals:** targets set to be met.

For each target, describe the result that would fail it. If no plausible result would, it is a
statement of intent wearing a number.

**Hides:** an ambitious target is not automatically better. A target chosen to be impressive fails
in the opposite direction and gets quietly dropped.

---

# 11. The Quarter With No Data

**Reveals:** what happens if instrumentation slips.

Imagine the first release ships without any of these events. Which decisions in `10-execution` §9
could not be made?

This is the most concrete argument for why §8 belongs in the build handoff, and it makes the case
without anyone needing to be persuaded about measurement culture.

**Hides:** it assumes the events are the only source. Sometimes support conversations answer the
question faster and better.

---

# 12. Reading It as the Dashboard

**Reveals:** what the organization will actually look at.

Imagine only the top three metrics are ever seen. Which three? Do they, together, distinguish a
good quarter from a bad one?

If the answer needs a fourth, the top three are wrong.

**Hides:** it optimizes for a summary. Diagnosis needs depth the dashboard will not have.

---

# Combining Models

| Situation | Model |
| --- | --- |
| Checking a metric can move | The Vanity Check |
| Checking what the metric incentivizes | The Gaming Question |
| Checking definitions | The Two Analysts |
| Checking the target's effect | Goodhart's Turn |
| Checking retention | The Login That Means Nothing |
| Checking counts and rates | The Missing Denominator |
| Checking computability | The Uncomputable Metric |
| Checking instrumentation restraint | The Orphan Event |
| Checking compliance | The Property Leaving the Building |
| Checking targets | The Target Nobody Could Miss |
| Checking why §8 matters | The Quarter With No Data |
| Checking the whole set | Reading It as the Dashboard |

Apply the Vanity Check and the Gaming Question while choosing the north star. Apply The Property
Leaving the Building and Reading It as the Dashboard last, on the finished plan.

---

# Self Assessment

- Could each of my metrics fall if the product got worse?
- What would each incentivize if it became the objective?
- Would two analysts produce the same numbers?
- What would this product look like after a year of optimizing the north star?
- Does "returning" require the user to do something?
- What is each metric divided by, and does it matter?
- Which metric has no event behind it?
- Which event feeds nothing?
- Which property carries protected data?
- What result would fail each target?
- Which decision could not be made if the events slipped?
- Do my top three metrics distinguish a good quarter from a bad one?

---

> **Mental Model Principle**
>
> The Gaming Question is the one to keep if you keep one.
>
> Everything else here protects the document. That one
> protects the product.
