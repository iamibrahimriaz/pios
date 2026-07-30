---
Title: Purpose
Module: 12-metrics
Section: core
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define why the Metrics module exists and what it establishes for the rest of the run.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - constitution/core
  - 08-product and 11-growth gates passed
Outputs:
  - Shared understanding of what this module establishes
Related Modules:
  - 13-operations
Tags:
  - Metrics
  - Purpose
  - Foundation
---

# Purpose

---

# Overview

The product is specified, planned, and has a growth motion. Nothing about it can yet be observed.

This module decides what one number represents success, defines every metric precisely enough for
someone else to compute it, and — the part that actually matters — specifies the events that must
be written for any of it to be knowable.

It is the last input the `critical` build handoff waits on. Until this module runs, that document
cannot be assembled.

---

# Purpose Statement

> Define measurable success, and make sure the events behind it get built —
> because instrumentation is never retrofitted.

---

# Why This Module Exists

Three failures dominate metrics work.

**The metric that only rises.** Total registered users, cumulative records created, revenue to
date. They measure elapsed time. No decision changes their direction, so nothing can be steered by
them — and they are the most commonly reported numbers in software.

**The definition that requires its author.** "Active users." Nobody knows the window, the
population, or what counts as active, so two teams report two figures and the difference gets
attributed to the market.

**The plan that ships without its events.** Every metric defined, no event specified. The feature
ships, the instrumentation does not, and the product runs blind for a quarter while somebody
schedules work everybody assumed was free.

The module's structure — a vanity check and a gaming question on the north star, a five-part
computation standard, and an event-level plan assigned to milestones — exists to make each of these
visible.

---

# The Judgment This Module Makes

| Output | What it commits |
| --- | --- |
| `north_star_metric` | The one number that resolves disagreements about progress |
| `success_metrics` | What each goal means numerically |
| `leading_indicators` | What moves early enough to act on |
| `targets` | What would count as failure |
| `instrumentation_plan` | The events that must be built, and when |

---

# Core Objectives

- Choose exactly one north star, representing user value rather than company convenience.
- Define every metric so two analysts would compute the same number.
- Give every goal in the PRD a metric.
- Separate what moves early from what only confirms.
- Name what must not get worse.
- Set targets a real result could miss, and admit which are guesses.
- Specify every event, its properties, and the milestone it ships in.

---

# What AI Should Learn Here

- A definition is a decision. A target is a prediction. They do not carry the same confidence.
- A number that cannot fall measures elapsed time.
- Every metric can be gamed; writing down how is what produces the counter-metrics.
- "Active users" is not a metric until five things are stated about it.
- A login is not a return.
- Cohort metrics are uncomputable without identity resolution.
- A regulated column as an event property is a compliance exposure, not a data-quality issue.
- An event with no milestone is an event nobody is building.

---

# The Two Confidences

Every other module in the framework reports one confidence. This one must report two, because it
contains two kinds of statement:

| | Nature | Standing |
| --- | --- | --- |
| Definitions | Decisions about what to count | Can be high — they are chosen |
| Targets | Predictions about behavior | Cannot be, for a product with no users |

> Confidence in these definitions: high. Confidence in these targets: low — there is no baseline,
> and every figure is an assumption with a stated basis.

A single confidence figure always reports the definition's, and the targets quietly inherit a
certainty nothing supports. That is this module's version of the laundering problem `07-strategy`
and `11-growth` each guard against.

---

# The Instrumentation Consequence

This module has an unusual property: five sixths of it can be revised at any time, and one sixth
cannot.

> An event not specified here will not be built.

Definitions can be rewritten next quarter. Events are written once, by someone who is already
building, and only if they were asked. Everything else in this document is a description of
intent; §8 is a build instruction, and it is the reason the module exists rather than being a
section of the PRD.

That is also why every event names a **milestone**: it then appears in that milestone's definition
of done in `10-execution`, which is the mechanism that makes instrumentation ship with the feature
rather than after it.

---

# Scope

**This module covers**

- The north star, its alternatives, and how it could be gamed
- Metric definitions, sources and targets
- Leading and lagging indicators, and their links
- Activation and retention measurement
- Counter-metrics and thresholds
- Baselines, or their honest absence
- Event-level instrumentation, identity resolution and privacy exclusions
- Reporting, review cadence and metric review triggers

**This module does not cover**

| Not here | Belongs to |
| --- | --- |
| What the product does | `08-product` — settled |
| The activation event itself | `11-growth` — carried, not redefined |
| Retention mechanisms | `11-growth` — measured, not chosen |
| System health monitoring | `09-technology`, `13-operations` |
| Alert routing and on-call | `13-operations` |
| Build sequence | `10-execution` |

---

# Position in the Run

```
08-product ┐
11-growth  ┴→ [ 12-metrics ] → 13-operations
                             → 12-Build-Handoff.md
```

---

# What This Module Hands Forward

| Output | Consumed by | Used for |
| --- | --- | --- |
| `instrumentation_plan`, per milestone | 10 | Instrumentation enters each definition of done |
| Counter-metrics and thresholds | 13 | Alerts, reviews, and what a breach means |
| Goal metrics | `03-PRD.md` | The PRD's success metrics |
| All outputs | `11-Success-Metrics.md` | The shipped metrics artifact |
| `instrumentation_plan` §8 | `12-Build-Handoff.md` | The events built with the first milestone |

---

# The Check With Legal Consequences

One check in this module is different in kind from the rest:

> A regulated column appearing as an event property means regulated data is now in a third-party
> system with different retention, different access control, and possibly a different jurisdiction.

It is evaluated mechanically — the regulated and PII columns from `09-technology` §3, checked
against every event property — because it is invisible in a document that reads well, and
irreversible once the events are live. A failure is surfaced to the operator regardless of what
else passes.

---

# Success Criteria

- One north star, representing user value, surviving the vanity check.
- The gaming question answered, with counter-metrics that follow from it.
- Every metric computable by someone who did not write it.
- Every PRD goal measured, or its immeasurability recorded.
- Leading indicators naming what they predict, and why.
- Targets that could be missed, with guesses admitted.
- Every metric traced to an event, every event to a metric, every event to a milestone.
- No regulated data in any event property.

---

# Self Assessment

- Is there one north star, and could it fall if the product got worse?
- Do I know how each metric would be gamed?
- Could someone else compute every number from what I wrote?
- Is any target one that cannot be missed?
- Does every event have a metric and a milestone?
- Did I check every property against the regulated column list?
- Did I report one confidence, or two?

---

> **Purpose Principle**
>
> Eleven modules decided what to build and why.
>
> This one decides whether anybody will ever know if it worked —
> and that is settled by a list of events, not by a definition.
