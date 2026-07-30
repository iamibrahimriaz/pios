---
Title: Framework
Module: 12-metrics
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the method by which success becomes measurable and observable.
Audience:
  - AI Agents
  - Product Managers
Prerequisites:
  - 12-metrics/core/03-Core-Principles.md
  - 08-product and 11-growth gates passed
Outputs:
  - north_star_metric
  - success_metrics
  - leading_indicators
  - instrumentation_plan
  - targets
Related Modules:
  - 13-operations
Tags:
  - Metrics
  - Framework
  - Method
---

# Framework — The Instrument

---

# The Method

> A product that cannot be measured cannot be improved, and a product measured
> by the wrong number gets worse on purpose.
>
> This module decides what one number matters, and makes sure the events behind it
> get built.

Six moves. The first five are definitions; the sixth is the only one that becomes code.

```
   Choose  →  Define  →  Split  →  Guard  →  Target  →  Instrument
     │         │          │        │          │           │
   one       computable  timing   limits    the bar     the events
```

| Move | Question | Produces |
| --- | --- | --- |
| 1. Choose | What one number represents delivered value? | `north_star_metric` |
| 2. Define | Could two analysts compute the same figure? | `success_metrics` |
| 3. Split | Which metrics move first, and which only confirm? | `leading_indicators` |
| 4. Guard | What must not get worse? | Counter-metrics |
| 5. Target | What result would count as failure? | `targets` |
| 6. Instrument | Which events must exist for any of this to be knowable? | `instrumentation_plan` |

---

# Move 1 — Choose

**Exactly one north star, and it represents value delivered to the user.**

One, because the purpose of a north star is to resolve disagreements. Two north stars resolve
nothing; they relocate the argument.

| Usually wrong | Usually right |
| --- | --- |
| Revenue | The unit of value the revenue is paid for |
| Registered users | Users completing the core job in a period |
| Sessions | Jobs completed per active user |
| Page views | Time saved, or output produced |

Revenue is a *consequence* of a north star. Choosing it directly measures the company's
convenience rather than the user's outcome — and it moves last, which makes it useless for
steering.

**Two rejected alternatives, with reasons.** The reasons are the actual content of this move:
naming why the obvious candidate would mislead is what makes the choice reviewable a year later.

## The Vanity Check

> Could this number fall if the product got worse?

If not, it is a cumulative count and it will rise forever regardless of what happens. Replace it
with a **rate** or a **cohort measure**.

Total registered users only goes up. Weekly active users completing the core job can fall, which
is precisely what makes it informative.

## The Gaming Question

> What would someone do to make this number rise without the product becoming more valuable?

Every metric has an answer. Writing it down is what produces the counter-metrics in Move 4, and
skipping it is how a team optimizes a product into a worse one in complete good faith.

---

# Move 2 — Define

**Every metric must be computable by someone who did not write it.**

The standard is objective, and it is this module's defining test:

> **The computation test.** Given only this definition, would two analysts produce the same
> number?

Five parts, all required:

| Part | Without it |
| --- | --- |
| Numerator | Nobody knows what is counted |
| Denominator | A count masquerades as a rate |
| Time window | Rolling seven days and calendar month differ by more than the metric moves |
| Population | Trials, internal users and churned accounts each change the answer |
| Exclusions | Test data inflates every early figure |

"Active users" fails on all five. "Distinct users who saved at least one consultation note in a
rolling 7-day window, excluding internal accounts and test practices" passes.

**Every metric also names its source** — the events it is computed from. A metric with no source
is a metric nobody can compute, and it will be quietly replaced with whatever is available.

---

# Move 3 — Split

**Separate what moves first from what only confirms.**

| | Moves | Actionable | Role |
| --- | --- | --- | --- |
| Leading | Early | Yes | Steer |
| Lagging | Late | No | Confirm |

Teams tracking only lagging metrics discover problems a quarter after they could have fixed them.
Teams tracking only leading metrics never find out whether any of it mattered.

**Each leading indicator must name what it predicts, and the basis for believing it does.** The
link is almost always `[inferred]` before launch — say so. A leading indicator with an unexamined
link is a metric that moves and means nothing.

State the **lead time** where it is known: how far ahead of the lagging metric the indicator
moves. If it is unknown, that is an honest answer and a thing the first cohorts will establish.

---

# Move 4 — Guard

**Name what must not get worse.**

Counter-metrics are the answer to Move 1's gaming question, made into thresholds.

| North star | Degenerate behavior | Counter-metric |
| --- | --- | --- |
| Notes saved per week | Encouraging many short fragmentary notes | Notes per consultation; time per note |
| Consultations completed | Rushing consultations | Error or correction rate |
| Active users | Nagging notifications | Notification opt-out rate |

Without counter-metrics, an organization improves its primary number and degrades the product,
and every individual decision along the way looks defensible.

**Carry the non-negotiables** from `09-technology`'s security model. Where a violation of a
security or regulatory rule can be observed in the metrics, it belongs here — a threshold whose
breach is a defect rather than a trade-off.

---

# Move 5 — Target

**Every metric gets a target a real result could miss.**

And for a new product, there is no baseline. That is not a gap to fill with an approximation — it
is a fact about the situation, and the honest handling is the framework's standard one:

| Situation | Handling |
| --- | --- |
| Baseline exists | State it and its source |
| No baseline | Say so. Targets are `[assumption: needs validation]` with a stated basis |
| Target from a comparable product | Cite it, and note the population differs |
| Target from the operator | Attribute it to them |

**Do not import industry benchmarks as targets.** A published median describes a population this
product is not in, measured with definitions nobody states.

Say **which milestone produces the first real baseline**. That is the point at which the targets
stop being assumptions, and naming it converts an admitted weakness into a plan.

---

# Move 6 — Instrument

**Specify the events, or none of the above will ever be known.**

This is the only move whose output becomes code, and it is consumed directly by the `critical`
build handoff.

> An event not specified here will not be built. Instrumentation is not retrofitted — the feature
> ships, the events do not, and the product runs blind while someone schedules the work that was
> supposed to be free.

**Per event:** the precise trigger, every property with its type, the metric it feeds, and the
milestone it ships in.

**Coverage, both directions** — the same discipline modules 08 and 09 apply:

| Direction | Failure | Consequence |
| --- | --- | --- |
| Metric → event | Uncomputable metric | It will be silently replaced with whatever is available |
| Event → metric | Orphan event | Noise, cost, and a privacy liability with no benefit |

**Identity resolution.** How a user is identified across sessions, across devices, and before
signup. It is the most commonly omitted part of an instrumentation plan and without it every
cohort and retention metric is uncomputable.

**Privacy exclusions.** From `02-market`'s regulatory landscape and `09-technology`'s data
classification: what must not be captured, and the mechanism that prevents it.

> Analytics on regulated data is a compliance exposure, not a data-quality question. A regulated
> column appearing as an event property means the regulated data is now in a third-party system
> with different retention, different access control and a different jurisdiction.

The check is mechanical: list the regulated columns from `09-technology` §3, then check them
against every event property. Any overlap fails the gate.

---

# Why the Order Is What It Is

| If you… | You get |
| --- | --- |
| Define before choosing | Careful definitions of the wrong metric |
| Split before defining | Leading indicators nobody can compute |
| Guard before choosing | Counter-metrics for a metric that changed |
| Target before defining | A number attached to an ambiguous measure |
| Instrument first | Events for the metrics that were easy to log |
| Skip instrumenting | Definitions nobody can ever compute |

---

# What This Module Does Not Decide

| Not here | Belongs to |
| --- | --- |
| What the product does | `08-product` — settled |
| The activation event | `11-growth` — carried, not redefined |
| Retention mechanisms | `11-growth` — measured, not chosen |
| System health monitoring | `09-technology`, `13-operations` |
| Alert routing and on-call | `13-operations` |
| Build sequence | `10-execution` |

---

# Self Assessment

- Is there exactly one north star, and does it represent user value?
- Could it fall if the product got worse?
- Do I know how it would be gamed, and what catches that?
- Could two analysts compute every metric identically?
- Does every leading indicator name what it predicts, and why?
- Does every counter-metric have a threshold?
- Could every target be missed?
- Does every metric trace to an event, and every event to a metric?
- Is identity resolution specified?
- Does any event property carry regulated data?

---

> **Framework Principle**
>
> Five of these moves produce definitions, which can be revised
> at any time.
>
> The sixth produces events, which can only be built once — and
> only while somebody is already building.
