---
Title: Lagging Indicators
Module: 12-metrics
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Keep the confirming metrics, and stop them being used for steering.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 12-metrics/knowledge/Leading-Indicators.md
Outputs:
  - Lagging set within success_metrics
Related Modules:
  - 06-business
Tags:
  - Metrics
  - Indicators
  - Concept
---

# Lagging Indicators

---

# What It Is

The metrics that **confirm** rather than steer — they arrive late, and by the time they move the cause is months old.

| Lagging metric | What it confirms | Why it cannot steer |
| --- | --- | --- |
| Revenue | The model worked | Reflects decisions from several months ago |
| Churn over a period | Retention held or did not | The customers already decided |
| CAC, actual | The channel's real cost | Measurable only after a full cohort converts |
| Net revenue retention | Expansion is real | Requires a year of accounts |
| The problem's cost, re-measured | `04-problem`'s claim was true | Needs enough usage to observe |

The reason to keep them is the second half of the framework's warning:

> Teams tracking only lagging metrics discover problems a quarter after they could have fixed them. **Teams tracking only leading
> metrics never find out whether any of it mattered.**

The last row is the most valuable and the most neglected: re-measuring the problem's cost is the only way to verify the value claim
`06-business` built the model on.

---

# When It Applies

In Move 3 (Split), as the counterpart to the leading set.

---

# How to Apply It Here

**Label each one as lagging, explicitly.** The label is what stops it being used for a weekly decision it cannot inform.

**Include the re-measured problem cost.** `04-problem` established the baseline and `06-business` claimed a capture share. This is where
the claim is tested, and it is the strongest evidence the product works.

**State the earliest point each becomes meaningful.** Revenue in month two says nothing. Naming the horizon prevents premature
conclusions in both directions.

**Pair each with the leading indicator that predicts it.** That pairing is what makes the leading set verifiable — and
`Cohorts.md` is how the verification is done.

**Keep them off the operational dashboard.** They belong in a periodic review, not in a daily view where their noise gets acted upon.

---

# Where It Misleads

**Lagging metrics are used for steering because they are the ones stakeholders ask about.** Reacting to revenue weekly means reacting to
decisions from last quarter, and the correction arrives out of phase.

**Early lagging figures are over-interpreted.** Small numbers are noisy, and a churn rate computed on eleven customers is arithmetic
rather than information.

**They are dropped because they are slow.** Then nothing ever confirms whether the leading indicators meant anything, and the product
optimizes signals of unknown value indefinitely.

**Revenue is treated as the north star because it is the ultimate lagging metric.** `North-Star.md` rejects it for exactly this reason:
it moves last and measures the company rather than the user.

**The value claim is never re-tested.** `06-business`'s capture share is an assumption until someone measures the problem again. Not
doing so leaves the business case permanently unvalidated.

---

# Related

| | |
| --- | --- |
| `Leading-Indicators.md` | The steering half |
| `Cohorts.md` | Where lead-lag links are verified |
| `Targets.md` | Which need a baseline most |
| `06-business` | The claims these confirm |

---

> **Concept Note**
>
> Label them lagging, and keep them out of weekly decisions.
>
> The most valuable one is the least used: re-measure the problem's cost
> and find out whether the value case was true.
