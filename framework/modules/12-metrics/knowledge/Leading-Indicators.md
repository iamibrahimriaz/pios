---
Title: Leading Indicators
Module: 12-metrics
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Require each early metric to name what it predicts and the basis for believing it.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 12-metrics/knowledge/Success-Metrics.md
Outputs:
  - leading_indicators
Related Modules:
  - 11-growth
Tags:
  - Metrics
  - Indicators
  - Concept
---

# Leading Indicators

---

# What It Is

The metrics that move **early** and can be acted on.

| | Moves | Actionable | Role |
| --- | --- | --- | --- |
| **Leading** | Early | Yes | Steer |
| Lagging | Late | No | Confirm |

And the requirement that separates a real leading indicator from a metric that simply moves:

> Each leading indicator must name **what it predicts**, and **the basis for believing it does.** The link is almost always
> `[inferred]` before launch — say so. A leading indicator with an unexamined link is a metric that moves and means nothing.

Where they come from, for most products:

| Indicator | Predicts |
| --- | --- |
| Activation rate — `11-growth`'s event | Retention, and therefore revenue |
| Time to first value | Activation rate |
| Frequency against the job's natural rate | Churn — `11-growth/knowledge/Churn.md`'s precursors |
| Drop-off per onboarding step | Activation rate |
| Correction rate on AI output | Trust, and eventual abandonment |

State the **lead time** where it is known. If it is unknown, that is an honest answer and something the first cohorts will establish.

---

# When It Applies

In Move 3 (Split), after definitions exist — splitting before defining produces leading indicators nobody can compute.

---

# How to Apply It Here

**Write the predictive claim as a sentence, with its tag.** "Activation within the first session predicts 90-day retention
`[inferred: no data yet]`" is honest and usable.

**Take the activation event from `11-growth` unchanged.** It is carried, not redefined. Redefining it here breaks the link to the
onboarding work module 11 planned around it.

**Prefer indicators that are already precursors.** `11-growth/knowledge/Churn.md` listed the observable behaviors preceding departure.
Those are leading indicators with a mechanism behind them.

**Say what action each one would trigger.** An indicator with no intended response is a chart. The same point
`07-strategy/knowledge/risks/Mitigation.md` makes about early warnings.

**Plan to verify the link.** The first cohorts establish whether the prediction holds. Naming the milestone that tests it converts an
inference into a plan.

---

# Where It Misleads

**Anything that moves early is called leading.** Movement is not prediction. Without a stated causal claim, an indicator produces
activity rather than steering.

**Vanity metrics are relabeled as leading.** Sign-ups move early and predict nothing about value. `North-Star.md`'s vanity check applies
to indicators too.

**The predictive link is assumed to be established.** Before launch it is an inference, and the whole set of them may be wrong together
— which is worth stating once, plainly.

**Lead time is asserted without evidence.** "Activation predicts retention 30 days out" is a specific claim requiring 30 days of data
nobody has.

**Only leading indicators are tracked.** Then the product optimizes early signals and never learns whether any of it mattered. That is
why `Lagging-Indicators.md` exists.

---

# Related

| | |
| --- | --- |
| `Lagging-Indicators.md` | The confirmation half |
| `Cohorts.md` | How the link is eventually verified |
| `11-growth` | Activation, and the churn precursors |
| `Success-Metrics.md` | Definitions these must satisfy |

---

> **Concept Note**
>
> Name what it predicts and why you believe it — then tag the belief.
>
> An indicator that moves early with no causal claim behind it produces
> activity, not steering.
