---
Title: Success Metrics
Module: 12-metrics
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Make every metric computable by someone who did not write it, and guard what must not get worse.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 12-metrics/knowledge/North-Star.md
Outputs:
  - success_metrics
Related Modules:
  - 08-product
  - 09-technology
Tags:
  - Metrics
  - Definitions
  - Method
---

# Success Metrics

---

# What It Is

The full metric set, each one **computable by someone who did not write it**.

> **The computation test.** Given only this definition, would two analysts produce the same number?

Five parts, all required:

| Part | Without it |
| --- | --- |
| Numerator | Nobody knows what is counted |
| Denominator | A count masquerades as a rate |
| Time window | Rolling seven days and calendar month differ by more than the metric moves |
| Population | Trials, internal users and churned accounts each change the answer |
| Exclusions | Test data inflates every early figure |

"Active users" fails on all five. "Distinct users who saved at least one consultation note in a rolling 7-day window, excluding internal
accounts and test practices" passes.

Plus the **counter-metrics** — the gaming answer made into thresholds:

| North star | Degenerate behavior | Counter-metric |
| --- | --- | --- |
| Notes saved per week | Many short fragmentary notes | Notes per consultation; time per note |
| Consultations completed | Rushing consultations | Error or correction rate |
| Active users | Nagging notifications | Notification opt-out rate |

---

# When It Applies

In Move 2 (Define) and Move 4 (Guard).

---

# How to Apply It Here

**Write all five parts for every metric, without exception.** A metric missing one will be computed differently by two people and the
disagreement will surface as a dispute about the product.

**Name the source events per metric.** A metric with no source is one nobody can compute, and it will be quietly replaced with whatever
is available.

**Set counter-metric thresholds as limits, not observations.** A counter-metric with no threshold is a chart nobody acts on.

**Carry the non-negotiables from `09-technology`'s security model.** Where a violation of a security or regulatory rule is observable in
the metrics, it belongs here — as a threshold whose breach is a **defect rather than a trade-off**.

**Keep the set small.** A dashboard of forty metrics has no priority in it. The north star, its counter-metrics, and the leading
indicators that predict it.

---

# Where It Misleads

**Familiar metric names are used as definitions.** "Engagement", "adoption", "retention" each mean four different things, and everyone
assumes their own version.

**A login is not a return.** Presence is not value. `North-Star.md`'s vanity logic applies to every metric in the set, not only to the
primary one.

**Counter-metrics are listed and never thresholded.** Then the primary number is optimized, the counter-metric drifts, and every
individual decision along the way looked defensible.

**Definitions change without a note.** A metric redefined mid-quarter makes the trend meaningless, and nobody notices because the name
stayed the same. Version the definition.

**The population is left implicit.** Including trials, internal accounts and churned users each shift the figure materially, and early on
the internal accounts are frequently the largest group.

---

# Related

| | |
| --- | --- |
| `North-Star.md` | The one metric this set surrounds |
| `Leading-Indicators.md`, `Lagging-Indicators.md` | The split by timing |
| `Instrumentation.md` | The events every metric names |
| `09-technology` | The non-negotiables carried as thresholds |

---

> **Concept Note**
>
> Numerator, denominator, window, population, exclusions — five parts,
> every metric, no exceptions.
>
> "Active users" fails all five, and everyone thinks they know what it
> means.
