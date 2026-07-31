---
Title: Quality Gate
Module: 12-metrics
Section: core
Category: Verification
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define how each gate criterion for this module is evaluated.
Audience:
  - AI Agents
Prerequisites:
  - 12-metrics/module.yaml
  - engine/gates.yaml
Outputs:
  - Gate verdict
Related Modules:
  - 13-operations
Tags:
  - Metrics
  - Quality Gate
  - Verification
---

# Quality Gate

---

# Overview

`module.yaml` states the criteria. This document explains how to evaluate each.

This gate stands in front of the last input the `critical` build handoff is waiting on. An event
that does not pass through here does not get built, and the metric behind it cannot be computed
for the lifetime of the first release.

---

# Governing Rule

> A gate is failed by default when its status cannot be determined.
>
> Uncertainty is a fail, not a pass.

---

# Criterion 1 — Exactly one north star metric, with the reasoning for it

**Passes when** there is one north star, it represents value delivered to the user, at least one
rejected alternative is named with why it would mislead, and both mechanical checks are answered
in writing.

**Fails when** there are two, when the metric is a company convenience, or when either check is
missing.

**One, not two.** The purpose of a north star is to resolve disagreements between teams. Two north
stars resolve nothing — they relocate the argument and give each side a number.

| Fails | Passes |
| --- | --- |
| "Revenue and active users" | "Consultations documented per active clinician per week" |
| "Monthly recurring revenue" | The unit of value the revenue is paid for |
| "Total registered users" | Weekly active users completing the core job |

**The vanity check.** Could this number fall if the product got worse? If not, it is a cumulative
count, it measures elapsed time, and no decision changes its direction.

**The gaming question.** What would make it rise without the product becoming more valuable? Every
metric has an answer, organizations reliably find it, and the answer must appear as a
counter-metric in §7. An unanswered gaming question fails this criterion.

**Also required:** the north star must measure the same unit of value `06-business` attached the
price to. A product priced on one unit and measured on another will be optimized away from its own
business model, gradually and with no one decision to blame.

---

# Criterion 2 — Every metric has a definition, source and target

**Passes when** every metric states numerator, denominator, time window, population and
exclusions; names the events it is computed from; and carries a target a real result could miss.

**Fails when** any of the five parts is missing, any metric has no source, or any target cannot be
missed.

> **The computation test.** Given only this definition, would two analysts produce the same number?

| Fails | Passes |
| --- | --- |
| "Active users" | "Distinct users who saved ≥1 consultation note in a rolling 7-day window, excluding internal accounts and test practices" |
| "Retention" | "Of users activated in week W, the share performing ≥1 qualifying action in week W+4" |
| "Improve engagement" | A named metric with a figure and a date |

**Also required:** every goal in `08-product` §6 appears as a goal metric. A goal with no metric
was never a goal — and where a goal genuinely cannot be measured, that must be recorded as an open
question rather than quietly dropped.

**On targets with no baseline.** For a new product there is none. The criterion is satisfied by an
honest target — `[assumption: needs validation]` with a stated basis — not by omitting the target.
A missing target fails; an admitted assumption passes. What also fails is a target imported from an
industry benchmark and presented as this product's number.

---

# Criterion 3 — Leading indicators distinguished from lagging ones

**Passes when** metrics are sorted, each leading indicator names the lagging metric it predicts and
**the basis for believing the link exists**, and warning thresholds are set.

**Fails when** the split is absent, or when a leading indicator's link is asserted with no basis.

| | Moves | Actionable | Role |
| --- | --- | --- | --- |
| Leading | Early | Yes | Steer |
| Lagging | Late | No | Confirm |

**Why the basis matters.** Before launch, every link between a leading and a lagging metric is an
inference. Stated as one, it can be tested and revised. Stated as a fact, it gets acted on early
and confidently, which is the worst combination available.

**Also required:** the **lead time**, or an explicit statement that it is unknown. An indicator
that moves one day before the metric it predicts is not an early warning, and nobody discovers that
until they have needed it.

**Also evaluated here:** whether "returning" is defined as an **action**. A retention metric built
on logins will look healthy while the product is being abandoned, and it is the single most common
way a retention number misleads.

---

# Criterion 4 — Instrumentation specified at event level for the build handoff

**Passes when** every event states its precise trigger, every property with its type, the metric it
feeds and the milestone it ships in; coverage is complete in both directions; identity resolution
is specified; and privacy exclusions are stated with a mechanism.

**Fails when** any of those is absent.

> An event not specified here will not be built. Instrumentation is not retrofitted — the feature
> ships, the events do not, and the product runs blind while somebody schedules work that was
> supposed to be free.

**Coverage, both directions**

| Direction | Failure | Consequence |
| --- | --- | --- |
| Metric → event | Uncomputable metric | Silently replaced with whatever is available |
| Event → metric | Orphan event | Cost, noise, and a privacy liability with no benefit |

Both answers must be written, even when they are "none".

**Identity resolution.** Across sessions, across devices, before signup. Omitted, every cohort and
retention metric is uncomputable — and it is the section most often left out.

**Milestone assignment.** Every event names the milestone it ships in, so it appears in that
milestone's definition of done in `10-execution`. An event with no milestone is an event nobody is
building, which is the same as an event that does not exist.

## The Privacy Check

**Fails when** any regulated or PII column from `09-technology` §3 appears as an event property, or
when exclusions are stated without an enforcement mechanism.

The check is mechanical:

```
List regulated and PII columns from 09-technology §3
For each event property, check membership
  ├─ overlap → FAIL
  └─ none    → record "none — verified"
```

> A regulated column as an event property means regulated data is now in a third-party system with
> different retention, different access control, and possibly a different jurisdiction.

This is a compliance exposure rather than a data-quality issue, and "we will be careful with PII"
is the same class of non-statement as "the system will be compliant" — which `09-technology`
prohibits for the same reason.

---

# Criterion 5 — Every metric states what someone optimizing it without caring about the outcome would do

**Passes when:** each metric carries its gamed behavior, and metrics whose gamed behavior is
harmful either changed or acquired a guardrail with a threshold.

**Fails when:** metrics are justified only by what they mean.

**Why meaning is not enough.** Most metric gaming is honest. People are told a number
matters and they move it — by shortening notes, closing tickets faster, prompting more
often. The damage arrives as a side effect of exactly the behavior that was asked for, and
the responsibility sits with whoever chose the number.

---

# Module-Specific Checks

## The Confidence Separation Check

**Fails when** one confidence figure covers both definitions and targets.

Definitions are decisions and can be high-confidence. Targets for a product with no users cannot
be. Reporting a single figure always reports the definition's, and the targets inherit a certainty
nothing supports.

## The Counter-Metric Check

**Fails when** the gaming answers from Criterion 1 have no corresponding counter-metric, or when a
counter-metric has no threshold or no stated purpose.

A threshold with no stated purpose is relaxed the first time it is inconvenient, and nobody
remembers what it protected.

## The Decision Point Check

**Fails when** a decision point in `10-execution` §9 has no metric that can answer its question.

A decision point exists to be decided with data. If the data will not exist, either the metric is
missing here or the decision point is theatre.

## The Measurement Cost Check

**Fails when** the cost of measurement is unstated, or breaches `09-technology`'s cost model.

Event volume, retention period and tooling tier make this a real line, occasionally a large one,
and it is routinely omitted from a cost model that was otherwise carefully checked.

---

# Universal Gates

| | |
| --- | --- |
| U1 | Every factual claim carries exactly one evidence tag |
| U2 | `north_star_metric`, `success_metrics`, `leading_indicators`, `instrumentation_plan`, `targets` all in `state.outputs` |
| U3 | No claim contradicts the evidence log without superseding it |
| U4 | The north star choice records the alternatives it rejected |
| U5 | Every target without a baseline is in `state.assumptions` with a validation method |
| U6 | Written for a reader with no access to this conversation |
| U7 | Every control declared load-bearing names where it executes, and that place exists |

---

# Verdict

```yaml
gate:
  module: 12-metrics
  criteria:
    one_north_star_with_reasoning: pass | fail
    definitions_source_and_targets: pass | fail
    leading_lagging_distinguished: pass | fail
    instrumentation_at_event_level: pass | fail
  module_checks:
    privacy_no_regulated_properties: pass | fail
    confidence_separated: pass | fail
    counter_metrics_present: pass | fail
    decision_points_answerable: pass | fail
    measurement_cost_within_model: pass | fail
  universal: [U1, U2, U3, U4, U5, U6, U7]
  events_specified: «count, all assigned to milestones»
  baseline_available: yes | no
  verdict: pass | fail
  notes: «what failed and what was done»
```

| Verdict | Action |
| --- | --- |
| Pass | Hand to `13-operations`; `12-Build-Handoff.md` can now be assembled |
| Fail | Revise, or `return to 08-product`. Three attempts, then halt |

A failure of the privacy check must be surfaced to the operator regardless of what else passes. It
is the only defect in this module that carries legal consequences, and it is invisible once the
events are live.

---

> **Gate Principle**
>
> Three of these criteria govern documents that can be rewritten
> next quarter.
>
> The fourth governs events, which are only ever built once —
> and only while somebody is already building.
