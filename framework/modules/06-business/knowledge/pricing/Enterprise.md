---
Title: Enterprise
Module: 06-business
Section: knowledge/pricing
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Price for institutional buying, where the process costs more than the product.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 06-business/knowledge/GTM.md
Outputs:
  - Enterprise terms within pricing_strategy
Related Modules:
  - 09-technology
  - 13-operations
Tags:
  - Business
  - Pricing
  - Concept
---

# Enterprise

---

# What It Is

Pricing for buyers whose **process** is the dominant cost — procurement, security review, information governance,
legal, and a budget cycle with fixed dates.

The characteristic feature is that the product is a small part of the transaction:

| The buyer requires | Which costs |
| --- | --- |
| A security and data-protection review | Documentation, and sometimes certification — `09-technology` |
| Contract negotiation and liability terms | Legal time, on both sides |
| A named support commitment, often with response times | A rota — `13-operations` |
| Onboarding, migration and training | Weeks of someone's time |
| Purchase within a budget window | Waiting, sometimes most of a year |

That total effort sets a **price floor**. Below it, each sale loses money regardless of margin on the software
itself — which is the mismatch `GTM.md` warns about, in its most concrete form.

---

# When It Applies

In Entry 3 (Price) wherever `03-user` found that the user cannot sign. It is not a tier name; it is a different
transaction.

---

# How to Apply It Here

**Compute the floor from the process, not from the software.** Sum the hours the sale and onboarding require, price
them, and divide by the contract term. Anything below that is a subsidized sale.

**Price the commitments separately from the capability.** Response-time guarantees, uptime commitments, dedicated
support and audit cooperation are recurring obligations with a real cost, and `13-operations` will staff them. They
are legitimate premium content; features usually are not.

**Anticipate the security review as a deliverable.** In regulated markets it arrives every time. Preparing the
documentation once — from `09-technology`'s obligations table — converts a recurring blocker into a repeatable
asset.

**Set the term against the sales cycle.** A nine-month cycle for a one-year contract means perpetual selling.
Multi-year terms are how institutional economics work, and `Discounts.md` prices what they cost.

**Say what is not on offer.** Custom development, bespoke deployment and unlimited support are the requests that
turn a product company into a consultancy. Declining them in advance is a pricing decision.

---

# Where It Misleads

**"Enterprise: contact us" is adopted as a tier without the motion behind it.** It implies a sales capability,
security documentation and a support commitment. Publishing it without those produces conversations that cannot be
closed.

**The cost of the sale is omitted from CAC.** Institutional acquisition is measured in months of someone's
attention, and it is the largest CAC component in the model. `CAC.md` requires the cycle length costed.

**A high price is assumed to make the sale worthwhile.** It only does if the process cost is genuinely covered and
the cycle fits the runway. A large contract arriving after the money runs out is not revenue.

**One large customer is treated as validation.** It is one buyer with idiosyncratic requirements, and building for
them can produce a product only they want. `02-market`'s honest description is a consulting engagement.

**Custom requirements are absorbed to win the deal.** Each one becomes a permanent maintenance obligation
`13-operations` inherits, and none of them appears in the pricing.

---

# Related

| | |
| --- | --- |
| `GTM.md` | The motion this requires |
| `Discounts.md` | Where negotiation is normal |
| `09-technology` | Security documentation and obligations |
| `13-operations` | Support commitments as recurring cost |

---

> **Concept Note**
>
> The floor is set by the process, not by the product.
>
> If the security review, the contract and the onboarding cost more
> than the license, the price is already wrong.
