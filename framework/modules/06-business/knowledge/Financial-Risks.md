---
Title: Financial Risks
Module: 06-business
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Name the load-bearing assumption, run sensitivity, and say which threshold fails first.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 06-business/knowledge/LTV.md
Outputs:
  - Sensitivity and verdict within unit_economics
Related Modules:
  - 07-strategy
  - 09-technology
Tags:
  - Business
  - Risk
  - Method
---

# Financial Risks

---

# What It Is

The test of whether the arithmetic survives its own assumptions.

Three questions, in order:

**1. Which single input, wrong by half, changes the verdict?** That is the load-bearing assumption. It is usually
CAC or churn, both of which are pure assumption before launch.

**2. What happens at the edges?** With mostly-assumed inputs, a point estimate is false precision. A table
showing the verdict when CAC doubles and churn doubles is more honest and more useful than any single figure.

**3. Which threshold fails first?**

| Test | Conventional threshold |
| --- | --- |
| LTV : CAC | Above 3 |
| Payback period | Under 12 months |
| Gross margin | Above 60% for software |
| Price as share of value delivered | Under 30% |
| Break-even customer count | Reachable within SOM in year one |

Thresholds are conventions, not laws. State the one used and why.

---

# When It Applies

At Entry 6 (Test), producing the viability verdict. The output is what the operator watches after launch.

---

# How to Apply It Here

**Present a sensitivity table, not a scenario narrative.** Rows for the load-bearing inputs, columns for
pessimistic / expected / optimistic. The verdict in each cell. It takes less space than the prose version and
cannot be read selectively.

**Answer the framework's question plainly: what would have to be true for this to work?** That sentence is the
module's most useful output — it converts an uncertain model into a watch list.

**Check the break-even count against SOM.** If break-even requires more customers than `02-market` said were
reachable in year one, the model does not close. That is a finding, and it usually sends the run back to pricing
or to the segment.

**Include the cost risks from downstream modules.** Per-user AI operating cost, infrastructure at scale, support
staffing, and compliance operations. `09-technology` and `13-operations` each run an arithmetic check against
this module's figures, and a margin assumed here has to survive both.

**Set the runway against the sales cycle.** A nine-month institutional cycle with twelve months of money is a
risk with a date, not a general concern.

---

# Where It Misleads

**Sensitivity gets run on the inputs that are known and not on the ones that matter.** Varying the price by 10%
while leaving an invented churn rate fixed produces a reassuring table about nothing.

**The load-bearing assumption gets adjusted until the verdict passes.** Each adjustment is individually
defensible, and the result is a model that proves what was already intended. Naming the assumption *before*
testing it is the defense.

**Thresholds are treated as pass marks rather than conventions.** LTV:CAC of 2.8 is not a failure; it is a
capital-efficiency requirement. The framework asks for the threshold and the reason, not compliance.

**A single optimistic case is presented and labeled conservative.** The word is used to describe whatever case was
produced. Only a stated range makes the claim checkable.

**Risk is listed without consequence.** "CAC may be higher than assumed" changes nothing. "If CAC exceeds £900,
payback passes 18 months and the model requires funding" is a decision.

---

# Related

| | |
| --- | --- |
| `CAC.md`, `LTV.md` | The two usual load-bearing inputs |
| `Revenue.md` | Where the break-even count is stated |
| `09-technology`, `13-operations` | The cost checks run against this module |
| `07-strategy` | Where the verdict shapes the plan |

---

> **Concept Note**
>
> Name the assumption that decides the verdict, then test it — in
> that order.
>
> A model built on six assumptions is not wrong because it is
> assumed. It is wrong when it hides that it is.
