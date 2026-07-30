---
Title: Cohorts
Module: 12-metrics
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Group users by when they arrived, so improvement is distinguishable from growth.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 12-metrics/knowledge/Success-Metrics.md
Outputs:
  - Cohort definitions within success_metrics
Related Modules:
  - 11-growth
Tags:
  - Metrics
  - Cohorts
  - Method
---

# Cohorts

---

# What It Is

Grouping users by when they started, then measuring each group over its own lifetime rather than in calendar time.

It solves one specific and severe problem:

> An aggregate figure that mixes users of different ages cannot distinguish improvement from growth. A retention rate that rises because
> many new users joined this month looks identical to one that rises because the product got better.

| Aggregate says | A cohort says |
| --- | --- |
| 60% of users were active this week | 60% of the March cohort was active in its fourth week; the April cohort was 72% |
| Churn is 4% | Month-one churn is 30% and month-six is 2% — two different problems |
| Activation is improving | The change happened in the cohort after the onboarding change shipped |

The second row is the one that reframes a product: a single churn number hides that most departures are failures to activate, which
`11-growth/knowledge/Churn.md` insists is a different problem with a different fix.

---

# When It Applies

Throughout Moves 2 to 5, and it is the mechanism that eventually verifies `Leading-Indicators.md`'s predictive claims.

---

# How to Apply It Here

**Define the cohort by the activation event, not by sign-up.** `11-growth` named the moment value arrived. Cohorting on sign-up mixes
users who never received value with users who did.

**Measure in periods since joining, not calendar periods.** Week four of the March cohort compared to week four of the April cohort.
That comparison is what makes a change attributable.

**Use it to separate the two churn problems.** Early churn is activation; late churn is retention. `11-growth` gave them different
mechanisms and they need different measures.

**Say which cohort produced the first real baseline.** `Targets.md` requires it, and cohorts are how the baseline becomes credible rather
than an average across mixed populations.

**Require identity resolution to make it computable.** `Instrumentation.md` covers it — without stable identity across sessions and
devices, no cohort metric can be computed at all.

---

# Where It Misleads

**Aggregate figures are used because they are simpler, and they mislead in a growing product.** Rapid growth makes almost every ratio
look better, because recent joiners dominate and have not had time to leave.

**Cohorts are too small to conclude from.** A cohort of eight is anecdote with a chart. Early on, the honest presentation is the raw
count rather than a percentage.

**Cohorts are cut only by date.** Segment, channel and plan cohorts frequently answer the more useful question — which channel produces
users who stay. `11-growth` needs that answer per channel.

**A cohort improvement is attributed to the most recent change.** Several things ship in a month. Attribution needs either a controlled
comparison or explicit acknowledgment that it is `[inferred]`.

**The first cohort is treated as representative.** It came from a personal network, which `06-business/knowledge/CAC.md` says behaves
unlike every subsequent cohort.

---

# Related

| | |
| --- | --- |
| `Leading-Indicators.md` | The claims cohorts verify |
| `Instrumentation.md` | Identity resolution, without which none of this computes |
| `11-growth` | Activation and the two churn problems |
| `Targets.md` | The cohort that sets the baseline |

---

> **Concept Note**
>
> Group by when they arrived and measure each group's own lifetime.
>
> In a growing product, almost every aggregate ratio improves for
> reasons that have nothing to do with the product.
