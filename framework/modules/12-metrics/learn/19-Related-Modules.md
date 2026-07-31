---
Title: Related Modules
Module: 12-metrics
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show how the Metrics module connects to the framework and where it sits in the regulated-field chain.
Audience:
  - Product Managers
  - Founders
  - Analysts
Prerequisites:
  - 12-metrics/README.md
Outputs:
  - Understanding of the metrics stage's position in the chain
Related Modules:
  - 08-product
  - 09-technology
  - 11-growth
Tags:
  - Metrics
  - Relationships
  - Learn
---

# Related Modules

---

# Overview

This module sits at an intersection: it needs the product's capabilities, the growth
model's claims, and the data model's fields. Missing any one of the three produces a
metric set that reads well and cannot be implemented.

---

# What It Takes In

| Input | From | Used for |
| --- | --- | --- |
| `feature_spec` | `08-product` | What can be observed at all |
| `growth_loops` | `11-growth` | What the north star has to express |
| `retention_model` | `11-growth` | The lagging outcomes leading indicators point at |
| `data_model` | `09-technology` | The computation test |
| The regulated column list | `09-technology` | The event-property check |
| `revenue_model` | `06-business` | Where targets are derived from |

The gate fails back to `08-product`, usually because a metric requires something the
product does not record — which is a specification gap rather than a measurement one.

---

# The Regulated Field Check

This module is the third of four places module 09's list is checked:

```
09-technology   produces the list of regulated columns
    ↓
12-metrics      no regulated field in an analytics event property   ← here
13-operations   the access and audit review, with a cadence and an owner
14-ai-systems   no regulated field in a model input
```

The framework treats an analytics event and a model prompt as the same class of exposure.
Both leave your systems, both go to a third party, and both frequently land in another
jurisdiction under a retention policy nobody selected.

This is the check most often skipped, because analytics is culturally an internal
concern.

---

# The Growth Dependency

The north star must express what module 11's model claims compounds. That makes the
loop-versus-funnel distinction directly consequential here:

| Module 11 concluded | The north star tends to be |
| --- | --- |
| A closed loop | Something that measures the loop's throughput |
| A funnel | Something that measures value delivered per customer |

A funnel mislabeled as a loop in module 11 produces a north star measuring viral behavior
that does not exist, and the team spends a year trying to move it.

---

# What It Sends Forward

| Output | Who consumes it | What they do with it |
| --- | --- | --- |
| `instrumentation_plan` | `10-execution` build handoff | Events implemented during build |
| `north_star_metric` | The operator | The standing priority |
| `leading_indicators` | `11-growth`, `13-operations` | Early signals; some become alerts |
| `success_metrics` | `13-operations` | Compliance non-negotiables are held here |
| `targets` | `06-business` feedback | Whether the model's assumptions are holding |

---

# The Operations Connection

Two links matter and neither is obvious:

**Compliance failures are held here as non-negotiables.** Module 13's severity scale
grades by user impact, and compliance failures sit off that scale — a failed retention
job harms nobody visibly and is still a defect with a legal dimension. This module holds
them as metrics that must be zero.

**Some leading indicators become alerts.** A metric with a threshold, a named person and
a runbook is an alert. Module 13 requires all three; this module supplies the metric and
the threshold.

---

# What It Deliberately Does Not Do

| It does not | Because |
| --- | --- |
| Decide what the product does | `08-product` did |
| Set the business model's assumptions | `06-business` did; this module measures against them |
| Build dashboards | Implementation, and outside the framework |
| Analyze results | There are none yet |

---

> **Relationships Principle**
>
> This module needs three upstream inputs to produce anything implementable: what the
> product does, what the growth model claims, and which fields exist.
>
> Metric sets that fail at launch are almost always missing the third.
