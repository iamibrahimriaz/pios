---
Title: Template
Module: 12-metrics
Section: core
Category: Output
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The working template for the Metrics Plan — this module's primary output.
Audience:
  - AI Agents
Prerequisites:
  - 12-metrics/core/06-Framework.md
Outputs:
  - projects/<slug>/research/12-metrics.md
Related Modules:
  - 13-operations
Tags:
  - Metrics
  - Template
  - Output
---

# Template — Metrics Plan

---

# Usage

Copy everything below the line into `projects/<slug>/research/12-metrics.md` and fill it.

This is a **working document**. It feeds three deliverables, one of them the `critical` one:

| Deliverable | Fed by |
| --- | --- |
| `11-Success-Metrics.md` | all sections |
| `03-PRD.md` | §3 goal metrics |
| `12-Build-Handoff.md` | §8 instrumentation — **critical**, and the last input it waits on |

| Marker | Meaning |
| --- | --- |
| `«placeholder»` | Replace with real content |
| `<!-- guidance -->` | Instructions for you. Remove before completing |
| `[tag]` | Evidence tag per `engine/evidence-policy.md` |

**The rule that governs this module:** an event not specified here will not be built. Metrics
are not retrofitted — the feature ships, the instrumentation does not, and the product runs
blind for a quarter while someone schedules the work.

---
---

# Metrics Plan — «Project Name»

| | |
| --- | --- |
| Module | 12-metrics |
| Date | «ISO date» |
| Activation event | «from 11-growth» |
| Regulated data present | «yes — regime / no» |
| Baseline available | «no — new product / yes — «source»» |
| Status | draft / reviewed / gated |

---

## 1. What We Are Measuring, in One Paragraph

<!-- Write last. What the north star is, why it represents value, and the two or three
     indicators that will move before it does. -->

«One paragraph.»

---

## 2. North Star

<!-- Move 1. EXACTLY ONE. It must represent value delivered to the user, not convenience
     to the company. Revenue is usually a consequence of a north star, not one. -->

## «Metric name»

| | |
| --- | --- |
| Definition | «precise enough to compute — see the computation block below» |
| Why this one | «what it captures that alternatives do not» |
| Rejected alternative | «metric» — «why it would mislead» |
| Rejected alternative | «metric» — «why it would mislead» |
| Source | «where the number comes from — which events» |
| Baseline | «value, or "new product — none"» |
| Target | «figure by date» `[tag]` |
| Review cadence | «weekly / monthly» |

**Computation**

| | |
| --- | --- |
| Numerator | «exactly what is counted» |
| Denominator | «exactly what it is divided by, or "none — this is a count"» |
| Time window | «rolling 7 days / calendar month / since signup» |
| Population | «which users are included» |
| Exclusions | «internal accounts, test data, «other»» |

**The gaming question:** «what would someone do to make this number rise without the product
becoming more valuable — and which counter-metric in §6 catches it»

**The vanity check:** «could this number fall if the product got worse? If no, it is a
cumulative count and must be replaced by a rate or a cohort measure»

---

## 3. Goal Metrics

<!-- One per goal in `08-product` §6. Every PRD goal must appear here — that is a gate
     criterion. A goal with no metric was never a goal. -->

| Goal | Metric | Definition | Baseline | Target | By | Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | «metric» | «how computed» | «value / none» | «value» `[tag]` | «date» | «events» |

**Goals with no metric:** «none, or list them — and say why the goal cannot be measured»

---

## 4. Leading Indicators

<!-- Move first, and are actionable. Each must name which lagging metric it predicts,
     and the basis for believing it does. -->

| Metric | Predicts | Basis for the link | Definition | Target | Warning threshold |
| --- | --- | --- | --- | --- | --- |
| «metric» | «which lagging metric» | `[inferred: reasoning]` | «how computed» | «value» | «when to worry» |

**The lead time:** «how far ahead of the lagging metric each one moves — if unknown, say so»

---

## 5. Lagging Indicators

<!-- Confirm, but arrive too late to steer by. Necessary, and not sufficient. -->

| Metric | Confirms | Definition | Target | Reported to |
| --- | --- | --- | --- | --- |
| «metric» | «what» | «how computed» | «value» `[tag]` | «audience» |

---

## 6. Activation and Retention

<!-- Carried from `11-growth`. These two are the most important early metrics for a
     product with no users. -->

### Activation

| | |
| --- | --- |
| Event | «from 11-growth — the action that proves value» |
| Computation | «activated users ÷ new users, within «window»» |
| Target rate | «percentage» `[assumption: needs validation]` |
| Target time | «minutes, from 10-execution» |

### Retention

| | |
| --- | --- |
| Mechanism being measured | «from 11-growth §6» |
| Cohort definition | «grouped by «signup week / first activation»» |
| Measured at | «day 7 / day 30 / «period»» |
| Return means | «the specific action that counts as "still using it"» |
| Target | «percentage» `[assumption: needs validation]` |
| **Early warning behavior** | «from 11-growth — the behavior that precedes leaving» |

<!-- "Return" must be an action, not a login. A user who opens the product and does nothing
     has not retained. -->

---

## 7. Counter-Metrics

<!-- Move 4. What must NOT get worse while the primary metrics improve. Without these, a
     team optimizes the north star into a worse product — and does so in good faith. -->

| Metric | Must not exceed / fall below | Protects against | Source |
| --- | --- | --- | --- |
| «error rate» | «threshold» | «what it protects» | «events» |
| «time per task» | «threshold» | «the north star being gamed by adding steps» | «events» |

**Non-negotiables carried from `09-technology`:** «any security or regulatory rule whose
violation must be visible in the metrics»

---

## 8. Instrumentation Plan

<!-- Move 6. Event level. This section is consumed directly by the build handoff.

     If an event is not specified here it will not exist, and the metric above cannot be
     computed. Name every property and its type. -->

| Event | Fires when | Properties | Feeds metric | Milestone |
| --- | --- | --- | --- | --- |
| `«event_name»` | «the precise trigger» | `«prop»: «type»` | «metric» | M«n» |

**Coverage, both directions**

| Check | Answer |
| --- | --- |
| Metrics with no event behind them | «none, or list — these are uncomputable» |
| Events feeding no metric | «none, or list — these are noise and a privacy liability» |

### Identity

| | |
| --- | --- |
| How a user is identified | «mechanism» |
| Across sessions | «how» |
| Across devices | «how, or "not resolved — cohort metrics are per-device"» |
| Before signup | «anonymous identifier, and how it is joined on signup» |

<!-- Without this, every cohort and retention metric is uncomputable. It is the most
     commonly omitted part of an instrumentation plan. -->

### Privacy Exclusions

<!-- From `02-market`'s regulatory landscape and `09-technology`'s data classification.
     Analytics on regulated data is a compliance exposure, not a data-quality question. -->

| Must not be captured | Regime or reason | Enforced how |
| --- | --- | --- |
| «field or content» | «regime» | «mechanism — e.g. property allowlist» |

| | |
| --- | --- |
| Regulated columns from `09-technology` §3 | «list» |
| Any appearing as event properties | «none — required / list them, which fails the gate» |
| Event data retention | «period, per regulation» |

---

## 9. Measurement Infrastructure

| Concern | Approach |
| --- | --- |
| Analytics tool | «tool» |
| How events reach it | «pipeline» |
| Where the team sees this | «dashboard» |
| Event data retention | «period» |
| Who reviews, how often | «role / cadence» |

**Cost of measurement:** «figure» `[tag]` — «and whether it fits inside `09-technology`'s cost
model»

---

## 10. Reporting

| Report | Audience | Cadence | Contains |
| --- | --- | --- | --- |
| «name» | «who» | «weekly» | «which metrics» |

**What is reported at each decision point in `10-execution` §9:** «the metric that answers each
decision point's question»

---

## 11. Baselines and Targets

<!-- Move 5. For a new product there is no baseline. A target with no baseline is an
     assumption, and it must look like one. -->

| | |
| --- | --- |
| Baseline available | «yes — source / no — new product» |
| Basis for targets | «comparable product / operator expectation / assumption» |
| Targets that are guesses | «list them — they belong in `state.assumptions`» |
| First real baseline expected | «which milestone produces it» |

> A target that cannot be missed is not a target. Every figure above must be one a real result
> could fail.

---

## 12. Metric Review Triggers

<!-- Metrics that made sense at launch stop making sense at scale. Say when to revisit. -->

| Trigger | Reconsider |
| --- | --- |
| «after «n» active accounts» | «whether the north star still reflects delivered value» |
| «after the first cohort reaches day 90» | «whether the retention window is right» |

---

## 13. Open Questions

| # | Question | Blocks | Who answers |
| --- | --- | --- | --- |
| Q1 | «question» | «metric or event» | operator / legal / analytics |

---

## 14. Confidence

| | |
| --- | --- |
| Confidence in these definitions | high / medium / low |
| Confidence in these targets | «usually low for a pre-launch product — say so» |
| Weakest element | «what, and why» |

<!-- Definitions can be high-confidence: they are decisions. Targets for a product with no
     users cannot be. Separating the two is the honest position. -->

---

## 15. Handoff

| Consumer | What it takes from here |
| --- | --- |
| `13-operations` | Counter-metrics, alert thresholds, review cadence |
| `10-execution` | Instrumentation per milestone — added to each definition of done |
| `11-Success-Metrics.md` | All sections |
| `03-PRD.md` | §3 goal metrics |
| `12-Build-Handoff.md` | §8 — the events to build with the first milestone |

---

<!-- ACCEPTANCE — remove before completing
- [ ] Exactly one north star, with at least one rejected alternative and the reasoning
- [ ] The north star represents user value, not company convenience
- [ ] Every metric has a definition precise enough for two analysts to compute identically
- [ ] Every definition states numerator, denominator, window, population and exclusions
- [ ] Every metric has a source and a target
- [ ] Every goal in `08-product` §6 appears as a goal metric
- [ ] Leading and lagging indicators distinguished, with the predicted metric named
- [ ] The gaming question answered for the north star
- [ ] The vanity check passed — no cumulative counts as primary metrics
- [ ] Counter-metrics defined with thresholds
- [ ] Every metric traces to an event; every event feeds a metric
- [ ] Identity resolution specified
- [ ] Privacy exclusions specified, with no regulated column as an event property
- [ ] Targets with no baseline recorded as assumptions
- [ ] Every «placeholder» replaced and every guidance comment removed
-->

---

> **Template Principle**
>
> §8 is why this module exists.
>
> Everything above it is a definition. Only the events get built,
> and only what gets built can ever be known.
