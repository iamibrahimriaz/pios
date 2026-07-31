---
Title: Workflow
Module: 12-metrics
Section: core
Category: Procedure
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The executable step-by-step procedure for running the Metrics module.
Audience:
  - AI Agents
Prerequisites:
  - 12-metrics/core/06-Framework.md
  - engine/state-schema.yaml
Outputs:
  - projects/<slug>/research/12-metrics.md
  - state.outputs.instrumentation_plan
Related Modules:
  - 13-operations
Tags:
  - Metrics
  - Workflow
  - Procedure
---

# Workflow

---

# Overview

`06-Framework.md` defines the method — the Instrument. This document is the procedure.

This module produces the last input the `critical` build handoff is waiting on. Until its
instrumentation plan exists, that deliverable cannot be assembled.

---

# Position in the Run

```
08-product ┐
11-growth  ┴→ [ 12-metrics ] → 13-operations
                             → 12-Build-Handoff.md
```

| | |
| --- | --- |
| Stage | `operationalise` |
| Depends on | `08-product`, `11-growth` |
| Consumes | `feature_spec`, `growth_loops`, `retention_model` |
| Produces | `north_star_metric`, `success_metrics`, `leading_indicators`, `instrumentation_plan`, `targets` |
| On fail | return to `08-product` |
| Human checkpoint | none |

---

# Step 1 — Verify Upstream and Inherit

1. Confirm `08-product` and `11-growth` are in `state.run.completed_modules`.
2. Read `08-product` **§6 goals** — every one must appear here as a goal metric.
3. Read `08-product` §7 requirements — these are what events attach to.
4. Read `11-growth`: the **activation event**, the `retention_model`, and the loops.
5. Read `09-technology` §3 — the **data classification**: which columns are PII and which are
   regulated.
6. Read `02-market` — the regulatory landscape, for what may not be captured.
7. Read `10-execution` §9 — the decision points, each of which needs a metric that answers it.
8. Read `06-business` — the value metric the price is attached to.

Record before defining anything:

| Inherited | Consequence |
| --- | --- |
| PRD goals | Each becomes a goal metric; a goal with no metric fails the gate |
| Activation event | Carried, not redefined |
| Retention mechanism | Determines what "returning" means |
| Regulated columns | May not appear as event properties |
| Decision points | Each needs a metric that can answer its question |
| No baseline | Targets are assumptions, and must be tagged |

---

# Step 2 — Read Before Writing

1. `engine/evidence-policy.md`
2. `12-metrics/core/03-Core-Principles.md`
3. `12-metrics/core/06-Framework.md` — the Six Moves
4. `12-metrics/core/08-Questions-To-Answer.md`
5. `12-metrics/knowledge/` — North-Star, Success-Metrics, Leading-Indicators,
   Lagging-Indicators, Cohorts, Targets, Instrumentation, Analytics
6. `framework/deliverables/templates/11-Success-Metrics.md` and `12-Build-Handoff.md` §9

---

# Step 3 — Choose

Move 1.

1. Identify the unit of value this product delivers — from `06-business`'s value analysis and
   `04-problem`'s sharpest problem.
2. Propose the north star. **Exactly one.**
3. Name two rejected alternatives and why each would mislead.
4. Run the **vanity check**: could this number fall if the product got worse? If not, replace it
   with a rate or a cohort measure.
5. Answer the **gaming question**: what makes this number rise without the product becoming more
   valuable? Keep the answer — it becomes Move 4.

```
Is the candidate a cumulative count?
  ├─ yes → replace with a rate or cohort measure
  └─ no  → is it a company convenience or a user outcome?
             ├─ convenience → find the value it is a consequence of
             └─ outcome     → proceed
```

---

# Step 4 — Define

Move 2. For the north star and every goal metric, write the five-part computation:

| Part | |
| --- | --- |
| Numerator | Exactly what is counted |
| Denominator | Exactly what it is divided by, or "none — this is a count" |
| Time window | Rolling or calendar, and the length |
| Population | Which users are in |
| Exclusions | Internal accounts, test data, anything else |

Then run the **computation test**: read each definition as though you had to produce the number
tomorrow and could not ask a question. Every ambiguity you find is a defect.

Map each goal from `08-product` §6 to a metric. List any goal that cannot be measured, with the
reason — that is a legitimate finding and it belongs in the open questions rather than being
quietly dropped.

---

# Step 5 — Split

Move 3.

1. Sort the metrics into leading and lagging.
2. Per leading indicator: what it predicts, the **basis for believing it does**, its definition,
   target, and warning threshold.
3. State the lead time where known; say it is unknown where it is not.
4. Per lagging indicator: what it confirms, and who it is reported to.

A leading indicator whose link to a lagging metric cannot be articulated is a number that moves
and means nothing.

---

# Step 6 — Carry Activation and Retention

From `11-growth`, made computable here.

**Activation:** the event, the computation (activated ÷ new, within a window), the target rate,
the target time from `10-execution`.

**Retention:** the mechanism being measured, the cohort definition, the measurement point, and —
critically — **what "returning" means as an action**.

> A login is not a return. A user who opens the product and does nothing has not retained, and a
> retention metric built on logins will look healthy while the product is being abandoned.

Carry the **early warning behavior** from `11-growth`. It is the actionable half of retention
measurement.

---

# Step 7 — Guard

Move 4.

1. Turn the gaming answers from Step 3 into counter-metrics with thresholds.
2. Add the operational floor: error rates, time per task, anything whose degradation would make
   the primary metric misleading.
3. Carry the **non-negotiables** from `09-technology` §10, where a violation is observable.

Each counter-metric states what it protects against. A threshold with no stated purpose gets
relaxed the first time it is inconvenient.

---

# Step 8 — Target

Move 5.

1. State whether a baseline exists.
2. Where none does, say so and tag every target as an assumption with its basis.
3. Attribute operator-supplied targets to the operator.
4. Name which milestone produces the **first real baseline**.
5. Check every target is one a real result could miss.

Do not import industry benchmarks as targets. They describe a different population, measured with
definitions nobody states.

---

# Step 9 — Instrument

Move 6. The move that becomes code.

1. For each metric, list the events required. Per event: precise trigger, every property with its
   type, the metric it feeds, and the milestone it ships in.
2. Run the **coverage check both ways** and write both answers, even when they are "none":
   - Metrics with no event — uncomputable.
   - Events feeding no metric — noise, cost and privacy liability.
3. Specify **identity**: across sessions, across devices, before signup.
4. Write the **privacy exclusions**: what must not be captured, the regime, and the mechanism.
5. Run the regulated-property check:

```
List regulated and PII columns from 09-technology §3
Check each against every event property
  ├─ overlap → FAIL. Remove it or the gate fails
  └─ none    → record "none — verified"
```

6. Confirm each event is assigned to a milestone, so it appears in that milestone's definition of
   done in `10-execution`.

Step 9.6 is what makes instrumentation happen. An event with no milestone is an event nobody is
building.

---

# Step 10 — Assemble and Write to State

Fill `13-Template.md` into `projects/<slug>/research/12-metrics.md`. Write §1 last.

```yaml
outputs:
  north_star_metric:     # §2 — one, with rejected alternatives
  success_metrics:       # §3, §5, §6 — goal, lagging, activation, retention
  leading_indicators:    # §4 — with predicted metrics and thresholds
  targets:               # §11 — with baselines or an honest absence
  instrumentation_plan:  # §8 — events, properties, identity, exclusions
```

Append every target without a baseline to `state.assumptions` with a validation method — U5.
Append the north star choice to `state.decisions` with the alternatives rejected — U4. Append
unmeasurable goals and unresolved definition questions to `state.open_questions`.

---

# Step 11 — Review

Run all four passes of `engine/review-loop.md`.

The adversarial pass for this module:

- Is my north star a user outcome, or a number the company likes?
- Could it fall if the product got worse?
- Which metric did I define loosely because defining it exactly would be awkward?
- Which leading indicator's link to a lagging metric is actually a guess?
- What would a team do to hit these numbers that would make the product worse?
- Which target did I set where it cannot be missed?
- Which metric has no event behind it?
- Which event exists because it seemed useful?
- Does any event property carry data the security model protects?
- Is "returning" defined as a login?

The coherence pass: does the north star measure the value `06-business` attached the price to, and
does the activation metric match `11-growth`'s event and `10-execution`'s time to first value? A
product priced on one unit of value and measured on another will be optimized away from its own
business model.

---

# Step 12 — Gate

Evaluate against `11-Quality-Gate.md` and universal gates U1–U7.

| Verdict | Action |
| --- | --- |
| Pass | Continue to Step 13 |
| Fail | Revise, or `return to 08-product`. Three attempts, then halt |

---

# Step 13 — Hand Off

1. Append `12-metrics` to `state.run.completed_modules`.
2. Hand each event to `10-execution`, to be added to its milestone's definition of done.
3. Hand counter-metrics, thresholds and review cadence to `13-operations`.
4. Confirm `12-Build-Handoff.md` now has its instrumentation section and can be assembled.

---

# Handoff Contract

| Consumer | Reads | Uses it for |
| --- | --- | --- |
| `10-execution` | `instrumentation_plan`, per milestone | Instrumentation enters each definition of done |
| `13-operations` | Counter-metrics, thresholds, cadence | Alerts, reviews, what a breach means |
| `11-Success-Metrics.md` | All outputs | The shipped metrics artifact |
| `03-PRD.md` | Goal metrics | The PRD's success metrics section |
| `12-Build-Handoff.md` | `instrumentation_plan` §8 | The events built with the first milestone |

`12-Build-Handoff.md` is the strict consumer, and this is the last module it waits on. An event
missing here is an event missing from the build, and a metric that cannot be computed for the
lifetime of the product's first release.

---

# Failure Modes

| Symptom | Cause | Fix |
| --- | --- | --- |
| Two north stars | Choice avoided | Choose one; the others are goal metrics |
| North star is revenue | Company convenience over user value | Measure the value the revenue is paid for |
| A number that only rises | Vanity check skipped | Replace with a rate or cohort measure |
| "Active users" | Computation test not run | Write all five parts |
| A goal with no metric | `08-product` §6 not mapped | Add it, or record why it cannot be measured |
| Leading indicators with no predicted metric | Move 3 half done | Name the link and its basis |
| No counter-metrics | Gaming question never asked | Ask it; the answers are the counter-metrics |
| Targets that cannot be missed | Target set to be met | Set a bar a real result could fail |
| Industry benchmark as target | Different population imported | Tag it, or drop it |
| Metric with no event | Coverage check skipped | Add the event or drop the metric |
| Event with no metric | Instrumentation by intuition | Remove it — it is cost and liability |
| Retention measured by login | "Return" undefined | Define it as an action |
| Cohorts uncomputable | Identity unspecified | Specify session, device and pre-signup identity |
| Regulated field as an event property | Privacy exclusions skipped | Remove it; this is a compliance exposure |
| Events with no milestone | Nobody is building them | Assign each to a milestone |

---

> **Workflow Principle**
>
> Step 9 is the only step in this module that survives contact
> with the build.
>
> Everything else can be redefined next quarter. The events either
> exist by then or the quarter cannot be measured at all.
