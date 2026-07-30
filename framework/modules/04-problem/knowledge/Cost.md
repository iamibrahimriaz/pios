---
Title: Cost
Module: 04-problem
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Quantify what the problem costs, because that figure becomes the value case and the metric target.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 04-problem/knowledge/Severity.md
Outputs:
  - Cost per occurrence within ranked_problems
Related Modules:
  - 06-business
  - 12-metrics
Tags:
  - Problem
  - Cost
  - Concept
---

# Cost

---

# What It Is

What each occurrence of the problem costs, in time, money or risk — recorded per problem alongside the score.

This is the single most reused number this module produces:

| Module | What it becomes |
| --- | --- |
| `06-business` | The value case, and the ceiling on what can be charged |
| `12-metrics` | The baseline the target improvement is measured against |
| `07-strategy` | Part of the argument for the MVP line |

```
cost per occurrence × frequency = annual cost of the problem
```

That figure is what a buyer weighs against the price. If it is not larger than the price by a comfortable
margin, `06-business` has a problem no amount of positioning fixes.

---

# When It Applies

In Stage 3 (Score), as a separate record from the 5/3/1 severity grade. The score ranks; the cost quantifies.

---

# How to Apply It Here

**Show the derivation and tag every input.** "Forty minutes per clinic × four clinics a week × forty-four
weeks" is checkable. "£15,000 a year" is not, and it will be quoted without its inputs.

**Use the unit the person feels, then convert once.** Unpaid evenings are the real cost; a monetary
equivalent is a translation for `06-business`, and both should be on the page. Converting straight to money
loses the reason anyone cares.

**Price the risk separately from the time.** A probabilistic cost — one rejected claim in ten, one near-miss a
year — is a different kind of figure and should not be blended into an hourly rate. State the probability and
the consequence side by side.

**Say who pays.** An unpaid hour costs the clinician; a rejected claim costs the practice. Where those are
different parties, `06-business` needs to know which one the price is being justified to.

**Include the cost of the workaround.** If they maintain a spreadsheet to contain the problem, that
maintenance is part of the cost — and it is the part most easily verified.

---

# Where It Misleads

**Cost figures are built from one estimated input and then treated as measurements.** A single
`[assumption]`-tagged minute count propagates into revenue projections four modules later, where its origin is
no longer visible. Round to the precision the weakest input supports.

**An hourly rate applied to saved time overstates the value.** Time recovered from an unpaid evening does not
become revenue; it becomes an evening. Salaried time saved is real value to the person and often no cash
saving to the employer — and the buyer is usually the employer.

**Costs get summed across a market to produce an impressive total.** "£400m of wasted clinician time" is a
`02-market` sizing figure in disguise and says nothing about what one buyer will pay.

**The cost of not solving it is confused with the value of solving it.** A product capturing half the
available benefit is the realistic case; costing the problem at 100% recoverable is the optimistic one and
should be labeled as such.

---

# Related

| | |
| --- | --- |
| `Severity.md` | The graded version of the same cost |
| `Frequency.md` | The multiplier |
| `Impact.md` | How many people bear it |
| `06-business`, `12-metrics` | Where the figure is reused |

---

> **Concept Note**
>
> Cost per occurrence, with its arithmetic shown, is the most reused
> number in the framework.
>
> Everything downstream inherits its weakest input — so name that
> input.
