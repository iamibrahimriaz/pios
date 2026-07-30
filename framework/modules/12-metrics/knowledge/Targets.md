---
Title: Targets
Module: 12-metrics
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Set targets a real result could miss, and treat the absent baseline honestly.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 12-metrics/knowledge/Success-Metrics.md
Outputs:
  - targets
Related Modules:
  - 04-problem
  - 06-business
Tags:
  - Metrics
  - Targets
  - Method
---

# Targets

---

# What It Is

The bar per metric — and the framework's central point about them is that **definitions and targets carry different confidence.**
Definitions are decisions; targets are predictions.

For a new product there is no baseline, and that is a fact about the situation rather than a gap to fill with an approximation:

| Situation | Handling |
| --- | --- |
| Baseline exists | State it and its source |
| **No baseline** | Say so. Targets are `[assumption: needs validation]` with a stated basis |
| Target from a comparable product | Cite it, and note the population differs |
| Target from the operator | Attribute it to them |

> **Do not import industry benchmarks as targets.** A published median describes a population this product is not in, measured with
> definitions nobody states.

And the requirement that converts the weakness into a plan:

> Say **which milestone produces the first real baseline.** That is the point at which the targets stop being assumptions.

---

# When It Applies

In Move 5 (Target), after definitions and the split.

---

# How to Apply It Here

**Set a target a real result could miss.** A target every plausible outcome satisfies contains no information, which is the same problem
`04-problem/knowledge/validation/Success-Criteria.md` names about invalidating results.

**Derive from `04-problem`'s baseline where one exists.** The cost per occurrence is a measured or estimated figure about the current
world, and a target expressed as an improvement on it is anchored to something.

**Attribute operator targets to the operator.** A number they chose is legitimate and carries their name rather than the framework's
implied authority.

**Name the milestone that produces the baseline.** Usually the first cohort with enough usage. `Cohorts.md` is how it becomes credible.

**Keep counter-metric thresholds separate from targets.** A target is something to reach; a counter-metric threshold is a line not to
cross, and breaching it is a defect rather than a shortfall.

---

# Where It Misleads

**A plausible-looking number acquires authority it never earned.** `01-idea` made this point about early success metrics: a figure
invented before there are users outlives every caveat attached to it, and by then the business model rests on it.

**Benchmarks are imported as though they were comparable.** Different segment, different price, different definitions — frequently
definitions nobody publishes. It is the clearest case of borrowed confidence in the module.

**Targets are set where they can be hit.** Then they measure the team's estimating rather than the product's performance.

**Missing a target is treated as failure rather than information.** Before a baseline exists, the target was an assumption, and the
result is the first real evidence. That is the correct reading and it needs stating in advance.

**Targets are set for every metric.** Diagnostic metrics do not need one. A target on a metric nobody would act on is noise with a
threshold.

---

# Related

| | |
| --- | --- |
| `Success-Metrics.md` | The definitions targets attach to |
| `Cohorts.md` | Where the baseline becomes credible |
| `04-problem` | The baseline that already exists |
| `06-business` | The figures the model assumed |

---

> **Concept Note**
>
> Definitions are decisions. Targets are predictions. Tag them
> differently.
>
> And name the milestone that produces the first baseline — that is how
> an admitted weakness becomes a plan.
