---
Title: GTM
Module: 06-business
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Align the sales motion with the price, the buyer and the cycle length.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 06-business/knowledge/Customer-Acquisition.md
Outputs:
  - go_to_market
Related Modules:
  - 11-growth
  - 13-operations
Tags:
  - Business
  - GTM
  - Concept
---

# GTM

---

# What It Is

The motion by which the product reaches buyers — and whether that motion is consistent with the price, the buyer
and the cycle.

The four motions are not interchangeable; each has a price range it can sustain:

| Motion | Works when | Breaks when |
| --- | --- | --- |
| **Self-serve** | The buyer is the user, price is low, value is provable in minutes | Procurement is involved, or setup requires data migration |
| **Founder-led** | Deal sizes justify hours of the founder's time | The founder becomes the bottleneck — always, eventually |
| **Inside sales** | Deal size supports a salaried salesperson's quota | The price is too low to cover the cost of the conversation |
| **Partner or reseller** | Someone already sells to this buyer and is trusted | The partner's incentive is smaller than their effort |

The mismatch to watch for: a low price with an institutional buying process. The sale costs more than the contract
is worth, and no volume of marketing fixes it.

---

# When It Applies

In Entry 5 (Route), alongside the first-ten path. Its outputs constrain `11-growth`'s channel choices and
`13-operations`' onboarding load.

---

# How to Apply It Here

**Check the motion against the price.** Divide the annual contract value by the hours the motion requires. If a
£400-a-year product needs six hours of selling, the motion is wrong or the price is.

**Check the motion against the buyer.** `03-user` established whether the user can sign. Where they cannot,
self-serve does not exist as an option regardless of how simple the product is.

**State the sales cycle length, and set it against runway.** This interaction is one of the most consequential
facts the module produces, and it belongs in `Financial-Risks.md` as a stated risk rather than an implication.

**Include onboarding in the motion.** Where a customer needs data migrated or staff trained, that effort is part
of acquisition. It sets a floor on price and it becomes a real load in `13-operations`.

**Name what happens after the founder.** Every founder-led motion has a transition point. Naming when — at what
customer count or revenue — makes it a plan rather than a surprise.

---

# Where It Misleads

**Self-serve is assumed because it is the cheapest to imagine.** For any product where the buyer is not the user,
or where value requires setup, it does not work — and the discovery arrives after the pricing page is built.

**Founder-led selling looks free and is the most expensive channel in the model.** `CAC.md` requires it costed. Its
real problem is not cost but ceiling: it stops at whatever one person can do.

**Partner channels are planned without the partner's economics.** A reseller needs a margin worth their effort and
a reason to prefer this product over their existing lines. Both are commonly assumed rather than checked.

**Marketing is treated as a motion.** It generates attention; the motion is what converts it. A model with
marketing and no motion has no mechanism between interest and revenue.

**One motion is assumed to serve all segments.** Where two segments buy differently, either the model addresses one
or it funds two motions — and `03-user` already required a single prioritized segment.

---

# Related

| | |
| --- | --- |
| `Customer-Acquisition.md` | The first-ten route |
| `CAC.md` | What the motion costs per customer |
| `pricing/Enterprise.md` | Where an institutional motion is priced |
| `11-growth`, `13-operations` | Channels and onboarding load |

---

> **Concept Note**
>
> Divide the contract value by the hours the sale takes.
>
> A low price with an institutional buying process is the one
> mismatch no amount of marketing repairs.
