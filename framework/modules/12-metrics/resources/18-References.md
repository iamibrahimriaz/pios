---
Title: References
Module: 12-metrics
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Separate definitions from targets by confidence, and forbid imported benchmarks.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 00-AI-Constitution/resources/18-References.md
Outputs:
  - Source routes for metric definitions and targets
Related Modules:
  - 09-technology
  - 11-growth
Tags:
  - Metrics
  - References
  - Reference
---

# References

---

# Overview

This module produces two kinds of statement with completely different standing, and conflating them is its characteristic sourcing failure:

> **Definitions are decisions. Targets are predictions.**

A definition needs no external source — it needs internal precision. A target needs a baseline, and before launch there is none.

---

# Input → Source

| Input | Source | Standing |
| --- | --- | --- |
| **Metric definitions** | This module. A decision, not a finding | `[verified: decision]`, high confidence |
| The activation event | `11-growth` — carried, not redefined | Inherits module 11's tag |
| Retention mechanisms to measure | `11-growth` — measured, not chosen here | Inherits |
| Churn precursors | `11-growth`'s observable behaviors | Inherits |
| The problem's baseline cost | `04-problem`'s cost per occurrence | Inherits — usually `[assumption]` |
| Capture-share claim to test | `06-business` | Inherits |
| **Regulated columns** | `09-technology` §3 | `[verified]` — and the privacy check is a list comparison against it |
| Event sources | The data model — `09-technology` | `[verified]` |
| **Targets** | An operator decision, or `[assumption: needs validation]` | Never derived |
| Baseline, once it exists | The first cohort with enough usage | `[verified]` from that milestone onward |

---

# The Benchmark Prohibition

> **Do not import industry benchmarks as targets.** A published median describes a population this product is not in, measured with definitions
> nobody states.

Three specific failures:

| Problem | Detail |
| --- | --- |
| **Undefined** | "Churn 3%" may be logo or revenue, monthly or annual, gross or net |
| **Wrong population** | Averaged across price points, buyer types and segments with nothing in common |
| **Self-selected** | Companies that publish metrics are companies with metrics worth publishing |

The only legitimate use is as a stated bound with the difference named:

```
Comparable: «product», «segment», «price», «source», «date».
Their figure: «n», defined as «definition».
Population differs in: «respects».
Used as: the upper bound of a range, not as a target.
```

`06-business` requires the same block, for the same reason.

---

# Sourcing a Target Honestly

Four situations, four handlings:

| Situation | Handling |
| --- | --- |
| A baseline exists | State it and its source |
| **No baseline** | Say so. `[assumption: needs validation]` with a stated basis |
| A comparable product's figure | Cite it, note the population differs |
| The operator chose the number | **Attribute it to them** |

And the requirement that converts the weakness into a plan:

> Say **which milestone produces the first real baseline.**

For the worked run that is the four-practice milestone, at which the documentation rate stops being an assumption. Naming it is what makes the
absent baseline a schedule item rather than a permanent gap.

---

# The Regulated-Column Check

This is the fourth appearance of one list in the framework:

| Module | What it checks against `09-technology` §3 |
| --- | --- |
| `09-technology` | Traces each obligation to a mechanism |
| **`12-metrics`** | **Every event property, mechanically** |
| `13-operations` | Schedules the review that keeps it true |
| `14-ai-systems` | Model inputs |

It is a **list comparison, not a judgment**, and any overlap fails the gate.

> Analytics on regulated data is a compliance exposure, not a data-quality question. A regulated column appearing as an event property means the
> regulated data is now in a third-party system with different retention, different access control and a different jurisdiction.

---

# Source Tiers, Applied

| Tier | At the metrics stage |
| --- | --- |
| **Primary** | The data model. The prior modules' outputs. The operator, for targets |
| **Industry** | Only as a bounded comparable, with the population difference named |
| **Academic** | Occasionally relevant for a measurement method; not for a target |
| **Product and technical** | Analytics tooling documentation — for what a tool can compute, not for definitions |
| **Community** | Not relevant |
| **AI-assisted** | Drafting definitions and stress-testing the gaming question. **Never a target, never a benchmark** |

The AI-assisted row has one genuinely valuable use here: asking how a given metric could be raised without the product improving. That is the
gaming question run adversarially, and it produces counter-metrics reliably. What it must not supply is a target, because it will produce a
plausible industry figure with no population attached.

---

# Documenting the Plan

**Tag definitions and targets separately.** Definition confidence high; target confidence low. Presenting both at one confidence is how an
invented number acquires authority.

**Name the source events per metric.** A metric with no source is one nobody can compute, and it will be silently replaced with whatever the
tool produces.

**State the predictive claim for every leading indicator, with its tag.** Before launch these are `[inferred]`, and the whole set may be wrong
together — worth saying once, plainly.

**Version the definitions.** A metric redefined mid-quarter makes the trend meaningless while the name stays the same.

---

# Common Mistakes With Sources Here

| Mistake | Consequence |
| --- | --- |
| A benchmark used as a target | Another population's number decides what counts as success |
| Definitions and targets at one confidence | An invented figure inherits a decision's authority |
| A regulated field as an event property | Clinical data in a third-party jurisdiction |
| No source events named | The metric is silently replaced by whatever is available |
| Identity resolution omitted | Every cohort and retention metric uncomputable, with plausible-looking output |
| A tool's built-in metric adopted | "Active users" as the tool defines it, not as this module did |

---

> **Resource Note**
>
> Definitions are decisions and need no source. Targets are predictions and
> need a baseline you do not have.
>
> Name the milestone that produces it, and the gap becomes a plan rather
> than a number someone invented.
