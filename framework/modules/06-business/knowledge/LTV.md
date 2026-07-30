---
Title: LTV
Module: 06-business
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Compute lifetime value from margin rather than revenue, and expose the churn assumption inside it.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 06-business/knowledge/CAC.md
Outputs:
  - LTV within unit_economics
Related Modules:
  - 09-technology
  - 11-growth
Tags:
  - Business
  - LTV
  - Concept
---

# LTV

---

# What It Is

The margin a customer produces over their lifetime.

```
lifetime = 1 / churn
LTV      = price × gross margin × lifetime
```

Two properties make it the most misused figure in the module:

**It is built on margin, not revenue.** Cost to serve has to be subtracted first, and cost to serve is the input
this framework insists on deriving rather than assuming — because for AI-based products it can consume the
margin entirely.

**It contains a division by churn.** Small changes in an assumed churn rate produce large changes in LTV. At 2%
monthly churn the lifetime is 50 months; at 5% it is 20. Neither figure has evidence behind it before launch, and
the difference is a factor of two and a half in the headline number.

---

# When It Applies

In Entry 4 (Economics), and again at Entry 6 (Test) against the LTV:CAC threshold.

---

# How to Apply It Here

**Derive cost to serve rather than assuming a margin.** Infrastructure per customer, support time per customer,
third-party and per-transaction fees, and **AI operating cost per active user**. `09-technology` will later have
to live inside the figure produced here, and its own cost check reconciles against it.

**State the churn assumption as a range and show LTV at each end.** This is the honest presentation, and it is
more useful than a point estimate because it shows what the verdict depends on.

**Cap the lifetime at something defensible.** `1 / churn` at low churn rates produces lifetimes of five or ten
years, which no pre-launch product can claim. Capping at 24 or 36 months is a conservative convention worth
stating.

**Use the price net of expected discounting.** `pricing/Discounts.md` covers why list price overstates, and LTV
built on list price overstates by the same margin.

**Include expansion only if a mechanism exists.** If nothing in `08-product` gives a customer a reason to pay
more, expansion revenue is zero regardless of what comparable companies achieve.

---

# Where It Misleads

**LTV computed on revenue rather than margin overstates by whatever the cost to serve is** — and in AI products
that can be most of it. A product with a 30% margin has an LTV a third of the revenue-based figure, and it is the
revenue-based figure that usually appears.

**Churn is the least evidenced and most leveraged input in the framework.** It is assumed, then divided into,
which magnifies the error. When the verdict is sensitive to churn, the honest statement is that the verdict is
unknown.

**A long lifetime is claimed for a product with no retention mechanism.** `Retention.md` and `11-growth` require
a named mechanism; without one, the lifetime assumption is a hope with a reciprocal.

**LTV:CAC above 3 is treated as a law.** It is a convention. A capital-efficient business works at 2; a
well-funded one tolerates less. State the threshold used and why, as Entry 6 requires.

**LTV justifies present spending on future money.** Even a sound LTV arrives over years while CAC is paid now.
Payback period, not LTV:CAC, is what governs whether the business survives to collect it.

---

# Related

| | |
| --- | --- |
| `CAC.md` | The cost side, and the payback pairing |
| `Retention.md` | Where the churn assumption comes from |
| `Financial-Risks.md` | Sensitivity on churn and margin |
| `09-technology` | Where cost to serve is confirmed |

---

> **Concept Note**
>
> LTV is margin, not revenue — and it contains a division by a number
> nobody has measured.
>
> Show it at two churn rates, and let the reader see the business
> change shape.
