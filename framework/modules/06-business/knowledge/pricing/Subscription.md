---
Title: Subscription Pricing
Module: 06-business
Section: knowledge/pricing
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Set tiers, periods and packaging for a recurring price.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 06-business/knowledge/pricing/Pricing-Models.md
Outputs:
  - Tier and period structure within pricing_strategy
Related Modules:
  - 08-product
Tags:
  - Business
  - Pricing
  - Concept
---

# Subscription Pricing

---

# What It Is

The mechanics of a recurring price: how many tiers, what separates them, which billing period, and what is
included.

This is the pricing-page decision. Whether recurring revenue is the right *shape* for the business is
`06-business/knowledge/Subscription.md`.

| Decision | The rule that applies |
| --- | --- |
| **Number of tiers** | Two or three. One is often right early; four or more is a menu nobody reads |
| **What separates tiers** | A dimension the customer can locate themselves on — size, volume, or a capability they know they need |
| **Billing period** | Matched to the buyer's budget cycle, not to cash-flow preference |
| **What is included at every tier** | Anything required for the product to work at all, and anything with a safety or compliance function |

The last row is the one that matters most in regulated products: audit trails, access controls and data-export
paths are never a paid upgrade.

---

# When It Applies

In Entry 3 (Price), after the model and unit are chosen. Tier boundaries then become requirement groupings in
`08-product`.

---

# How to Apply It Here

**Separate tiers on a dimension the buyer already knows about themselves.** Number of clinicians, monthly claim
volume, single site versus multi-site. A buyer who cannot tell which tier they are in does not choose one.

**Start with fewer tiers than feels complete.** Early pricing exists to close the first ten deals and to learn.
Three tiers with unclear boundaries produce three conversations about which one applies.

**Keep the safety floor free of tiering.** Access control, audit logging, export and erasure paths derive from
`09-technology`'s obligations. Selling a compliance obligation as a premium feature is a liability, not a tier.

**Match the period to the budget cycle.** `03-user`'s buying-process findings decide it. Annual billing suits
institutional budgets and blocks small operators; monthly does the reverse.

**Price the annual discount deliberately.** It buys cash and commitment at a real cost. `Discounts.md` covers why
the discounted figure, not the list price, is the one every downstream calculation must use.

---

# Where It Misleads

**Tiers get drawn to create an upgrade path that the product does not support.** Withholding capability the
customer needs to succeed produces a deliberately weakened low tier — which increases churn among exactly the
customers who were most price-sensitive.

**A middle tier is added to make the top one look reasonable.** It sometimes works and it also produces a tier
nobody wants and everyone asks about. If it has no coherent user, it is a presentation device carrying real
support cost.

**Usage caps are set from cost rather than from behavior.** A cap that the median customer hits is a price
increase delivered as a surprise, and it arrives as a support conversation. `03-user`'s frequency findings say
where the median sits.

**Grandfathering is not planned for.** Early customers are on early prices. Deciding in advance whether they move
is cheaper than deciding under pressure with a public pricing change pending.

**Feature lists substitute for tier logic.** A tier defined by an arbitrary bundle asks the buyer to work out
what they need. A tier defined by their own size asks them nothing.

---

# Related

| | |
| --- | --- |
| `Pricing-Models.md` | The model and unit this structures |
| `Upgrade-Path.md` | Whether moving up is real |
| `Discounts.md` | What the price actually becomes |
| `06-business` `Subscription.md` | Whether recurrence fits the value |

---

> **Concept Note**
>
> Split tiers on something the buyer already knows about
> themselves.
>
> And never put a compliance obligation behind a paid tier — that is
> not packaging, it is exposure.
