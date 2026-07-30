---
Title: Subscription
Module: 06-business
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Explain what recurring revenue requires of a product, as distinct from how it is priced.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 06-business/knowledge/Retention.md
Outputs:
  - Recurring revenue shape within business_model
Related Modules:
  - 11-growth
  - 13-operations
Tags:
  - Business
  - Subscription
  - Concept
---

# Subscription

---

# What It Is

Recurring revenue as a **business shape** — what it demands of the product and the operation. The pricing
mechanics of tiers, units and billing periods are `pricing/Subscription.md`; this file is about what recurrence
obliges.

A subscription is a repeated purchase decision. That produces three obligations most models omit:

| Obligation | Consequence if unmet |
| --- | --- |
| **Recurring value** | A one-time benefit sold monthly churns as soon as the benefit is banked |
| **Ongoing cost to serve** | Support, hosting, compliance and AI operations recur too — `13-operations` prices them |
| **A reason to renew that is visible at renewal** | Value delivered and forgotten does not survive a budget review |

The corresponding property is why it is chosen: revenue compounds, and the lifetime of a customer becomes an
asset rather than a transaction.

---

# When It Applies

In Entry 1 and Entry 4 — the shape affects who signs, and it determines whether lifetime arithmetic is the right
model at all.

---

# How to Apply It Here

**Check that the value recurs.** A migration tool, an annual filing, a one-off setup — these deliver value once.
Charging monthly for them is a financing arrangement, not a subscription, and churn will reflect it.

**Match the billing period to the buyer's budget cycle.** Institutional buyers with annual budgets find monthly
billing administratively awkward; small operators find annual commitments a barrier. `03-user`'s buying-process
findings decide it.

**Model annual contracts as renewals, not as monthly churn.** One decision a year, taken by someone who may not
be the user, with a visible price. That is a different risk profile and `Retention.md` treats it separately.

**Carry the recurring cost of serving into the margin.** Every month of revenue is a month of infrastructure,
support and — for AI features — inference cost. `LTV.md` requires the margin, and this is where the recurrence of
the cost side becomes visible.

**Name what makes renewal visible.** A report, a saved history, an accumulated record, a measurable outcome. If
the product's value is invisible at renewal time, the renewal is decided on price alone.

---

# Where It Misleads

**Subscription is adopted as the default without checking that the value recurs.** It is the conventional
software model, which makes it the unexamined choice — and for one-time value it produces predictable churn that
gets attributed to the product rather than to the model.

**Recurring revenue is treated as more certain than it is.** It is a repeated decision, and each repetition is a
chance to leave. Predictability comes from retention mechanisms, not from the billing arrangement.

**The cost side is not modeled as recurring.** Serving a customer for three years costs three years of
infrastructure and support. A margin computed on year one flatters a model whose costs grow with the installed
base — which is `13-operations`' true-cost-to-serve check.

**Annual prepayment is read as retention.** It is cash flow. The customer's decision arrives at the renewal
regardless, and prepayment can conceal a year of disengagement.

**Usage-based revenue gets called subscription.** Usage revenue moves with the customer's own volume, which means
their bad quarter is your bad quarter. That is a materially different risk, and `pricing/Pricing-Models.md`
covers it.

---

# Related

| | |
| --- | --- |
| `pricing/Subscription.md` | The pricing mechanics — tiers, units, periods |
| `Retention.md` | Churn, renewal and the mechanism |
| `LTV.md` | Where recurrence becomes lifetime value |
| `13-operations` | Where the recurring cost is fully priced |

---

> **Concept Note**
>
> Charge monthly only where the value arrives monthly.
>
> A one-time benefit billed on repeat is a loan, and it is repaid by
> churn.
