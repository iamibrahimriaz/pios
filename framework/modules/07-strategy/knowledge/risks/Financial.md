---
Title: Financial Risks
Module: 07-strategy
Section: knowledge/risks
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Register runway against sequence, and treat cash timing as a dated fact.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 07-strategy/knowledge/risks/Business.md
Outputs:
  - Financial risks within risk_register
Related Modules:
  - 06-business
  - 13-operations
Tags:
  - Strategy
  - Risk
  - Concept
---

# Financial Risks

---

# What It Is

The risks about money and time — distinguished from `Business.md` by being about **cash**, not about whether the model
is sound.

| Risk | Early warning sign |
| --- | --- |
| **The sequence does not fit inside the runway** | Arithmetic, available now — no observation needed |
| **The sales cycle consumes the runway before revenue arrives** | Cycle length on the first two deals |
| **Break-even requires more customers than SOM allows** | `06-business`'s check; also available now |
| **Costs grow with usage faster than revenue** | Per-user cost as usage rises |
| **A fixed cost arrives before revenue** — certification, audit, insurance | The obligation's date, from `02-market` Frame 2 |
| **Funding is assumed and unsecured** | The plan's dependency on it, stated or unstated |

The first and third rows are unusual in a risk register: they are **calculable today**. A sequence that cannot fit the
runway is not a risk, it is a finding, and it should be resolved rather than monitored.

---

# When It Applies

In Move 6 (Register), against `Timeline.md`'s sequence and `06-business`'s runway. Recurring operational costs are
confirmed later by `13-operations`.

---

# How to Apply It Here

**Do the runway arithmetic and state the result.** Money available, burn rate, and the sequence's dependencies. If the
sequence exceeds the runway, that changes the cut — which is a Move 4 decision, not a risk entry.

**Treat external deadlines as dated facts.** A regulatory date, a budget window, a contract renewal, a certification
lead time. `Timeline.md` allows these because they are not estimates about the team.

**Register the pre-revenue fixed costs.** Certification, insurance, legal review and audit preparation frequently
arrive before the first customer. `02-market` Frame 2 costed them and they are easy to omit.

**Name any assumed funding.** A plan depending on money not yet secured has a dependency, and it belongs in the
register with the consequence if it does not arrive.

**Watch cost per user as usage grows.** For AI products the risk is that success increases cost faster than revenue.
`14-ai-systems` requires cost as a share of revenue per user, and rising usage is the early warning.

---

# Where It Misleads

**Calculable shortfalls get registered as risks instead of being resolved.** Putting "runway may be insufficient" in a
register when the arithmetic already says it is defers a decision that should be made at the cut.

**Runway is stated without the sales cycle.** Twelve months of money and a nine-month institutional cycle leaves three
months of revenue. That interaction is the single most consequential financial fact for an institutional product.

**Revenue timing is assumed to follow the milestone.** Contracts sign after procurement, and payment follows invoicing
terms. The gap between shipping and being paid is months in institutional markets.

**Cost estimates are taken from the plan rather than from the obligations.** `09-technology`'s infrastructure check and
`13-operations`' support and compliance staffing are the three arithmetic checks the framework runs against
`06-business`. All three land here.

**Financial risk is folded into a general "we may run out of money" entry.** That is true of every venture and
monitorable by nobody. The useful entries name a threshold and a date.

---

# Related

| | |
| --- | --- |
| `Business.md` | Whether the model's assumptions hold |
| `07-strategy` `Timeline.md` | Sequence, and why there are no durations |
| `06-business` | Runway, break-even and the sales cycle |
| `13-operations` | Recurring cost, confirmed |

---

> **Concept Note**
>
> If the arithmetic already says the sequence does not fit, that is
> not a risk — it is a decision waiting at the cut.
>
> Register thresholds and dates. Everything else is anxiety with a
> heading.
