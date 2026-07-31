---
Title: References
Module: 06-business
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Route each economic input to a source, and mark which ones have none.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - ../constitution/resources/18-References.md
Outputs:
  - Source routes for business-model inputs
Related Modules:
  - 05-competition
  - 13-operations
Tags:
  - Business
  - References
  - Reference
---

# References

---

# Overview

This module's outputs are numbers, and most of its inputs have no source. That combination is what produces false rigor, so the useful thing
a references file can do here is say **which inputs are researchable and which are structurally unknowable before launch.**

---

# Input → Source

| Input | Source | Standing available |
| --- | --- | --- |
| **Competitor prices** | Pricing pages, dated — `05-competition` | `[verified]` for list price |
| **Value at stake** | `04-problem`'s cost per occurrence × frequency | Inherits module 04's tag |
| **Capture share** | Judgment about what the product addresses | `[assumption]`, always — state it |
| **Infrastructure cost** | Provider pricing calculators, dated | `[verified]` for rates, `[inferred]` for volume |
| **Inference cost** | Provider pricing × operations per user | `[verified]` rate, `[assumption]` volume |
| **Support cost** | `13-operations`' forecast | `[assumption]` until launch |
| **Segment size** | Registers — `02-market` | `[verified]` |
| **Channel reachability** | Membership lists, association directories | `[verified]` for the list |
| **CAC** | — | **`[assumption]`. No source exists before launch** |
| **Churn** | — | **`[assumption]`. No source exists before launch** |
| **Conversion rate** | — | **`[assumption]`. No source exists before launch** |
| **Willingness to pay** | — | **`[assumption]`. Stated intent overstates by an unpredictable margin** |

The bottom four rows are the module's honest position. They are unknowable, they are load-bearing, and the framework's response is a
sensitivity table rather than a figure.

---

# The Benchmark Problem

Published SaaS benchmarks are the most tempting and least applicable source in this module.

**Why they mislead**

- They average across markets, price points, buyer types and contract shapes that have nothing in common with this product.
- The definitions are rarely stated. "Churn" in a published median may be logo, revenue, monthly or annual.
- The population is self-selecting — companies that report metrics are companies with metrics worth reporting.

**How to use one, if at all**

```
Comparable: «product», «segment», «price point», «source», «date».
Their churn: «figure», defined as «definition».
Population differs from ours in: «respects».
Used as: the upper bound of our sensitivity range, not as an estimate.
```

If that block cannot be filled in, the benchmark is not usable. `12-metrics/knowledge/Targets.md` makes the same point about imported
targets: a published median describes a population this product is not in.

---

# Sourcing the Cost Side

Cost is the one part of this module that is genuinely researchable now:

| Cost | Route |
| --- | --- |
| Compute, storage, bandwidth | Provider pricing pages and calculators, with the date |
| Model inference | Provider pricing per unit × operations per user — `14-ai-systems` computes the second half |
| Third-party services | Their pricing pages, and their minimums |
| Certification | Regulator or notified-body schedules — `02-market` Frame 2 |
| Support hours | `13-operations`' burden forecast × a real hourly rate |
| The operator's own time | A real rate. Excluding it is the standard omission |

**Price the operator's time.** `CAC.md` and `13-operations/knowledge/Cost-Model.md` both insist on it, and for the same reason: a model that
treats founder effort as free collapses on the first hire, which is exactly when it is being relied upon.

---

# Source Tiers, Applied

| Tier | At the business stage |
| --- | --- |
| **Primary** | The operator, for goals, runway and appetite. Provider pricing. Registers |
| **Industry** | Sector pricing norms — useful context, weak as a benchmark |
| **Academic** | Rarely relevant |
| **Product and technical** | Competitor pricing and packaging — `05-competition`, dated |
| **Community** | Practitioner discussion of what they pay for and resent paying for |
| **AI-assisted** | Structuring the model and checking arithmetic. **Never a CAC, churn or conversion figure** |

The last row is where this module is most exposed. A model asked for typical SaaS churn will supply a confident number with no population
attached, and it will be indistinguishable from research once it is in a spreadsheet.

---

# Documenting the Model

Three habits make the arithmetic auditable:

**Show the formula, not the total.** A reader must be able to change one input and see the consequence. A single figure can only be accepted
or rejected.

**Round to the precision the weakest input supports.** Four significant figures on a model containing three assumptions is the form in which
guesses become plans.

**State the verdict as conditional, with thresholds.** "Viable if inference is under £8, CAC under £400 and churn under 3%" is a watch list.
"LTV:CAC 7.6" is a claim nobody can act on.

---

# Common Mistakes With Sources Here

| Mistake | Consequence |
| --- | --- |
| An assumed margin | The largest variable cost is never examined |
| A benchmark churn rate | A borrowed number decides the verdict |
| Undated competitor pricing | An anchor for a price that has changed |
| Founder time excluded from CAC | The model breaks on the first hire |
| List price used instead of effective price | Every downstream figure optimistic by the discount rate |
| A model-generated conversion rate | An invented input at the center of the arithmetic |

---

> **Resource Note**
>
> CAC, churn, conversion and willingness to pay have no source before
> launch. That is a fact about the situation.
>
> The honest response is a range and a named threshold — not a benchmark
> borrowed from a population you are not in.
