---
Title: Upgrade Path
Module: 06-business
Section: knowledge/pricing
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Require a mechanism before counting expansion revenue.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 06-business/knowledge/pricing/Subscription.md
Outputs:
  - Expansion mechanism within pricing_strategy
Related Modules:
  - 08-product
  - 11-growth
Tags:
  - Business
  - Pricing
  - Concept
---

# Upgrade Path

---

# What It Is

The mechanism by which an existing customer comes to pay more — and the test of whether expansion revenue may be
counted at all.

> If nothing in `08-product` produces a reason to pay more, expansion revenue is zero.

Expansion is real only when it is driven by something that grows on the customer's side:

| Driver | Why it works |
| --- | --- |
| **They grow** — more staff, more volume, more sites | The customer's own success raises the bill, with no persuasion required |
| **Usage crosses a band** | Predictable, and visible to them before it happens |
| **A distinct need emerges later** | A genuinely separable capability they did not need on day one |
| A tier that withholds something they always needed | Not expansion — a price increase, delivered as friction |
| A price rise | Not expansion, and it arrives at the renewal conversation |

The bottom two rows are how expansion is most often manufactured, and both damage retention among the customers
least able to absorb them.

---

# When It Applies

In Entry 3 (Price) as a design question, and in Entry 4 (Economics) as the gate on whether any expansion appears in
the model.

---

# How to Apply It Here

**Name the specific requirement in `08-product` that the upgrade unlocks.** If no requirement corresponds to it,
the upgrade path is a pricing-page fiction and the expansion line comes out of the model.

**Prefer growth-linked expansion to capability-linked.** Revenue that rises because the customer grew requires no
sales conversation and no product decision. It is also the only kind that compounds without effort.

**Make the trigger visible to the customer before it fires.** A bill that rises unannounced is a support incident
and a trust cost. `13-operations` will handle the consequence.

**Set expansion to zero in the base case.** State it as an upside with its own assumption, tagged. A model whose
viability depends on unproven expansion has moved its load-bearing assumption somewhere `Financial-Risks.md` should
be testing.

**Check the downgrade path too.** Customers shrink. A structure with no way down produces cancellation instead of
reduction, which converts a smaller customer into no customer.

---

# Where It Misleads

**Net revenue retention above 100% is projected before a single upgrade mechanism exists.** It is a figure from
companies with mature product lines, and borrowing it is the clearest case of `11-growth`'s borrowed growth applied
to revenue.

**Withheld capability is called an upgrade path.** Removing something the customer needs in order to sell it back
raises churn among price-sensitive users — the same population the low tier exists to serve. `Subscription.md`
requires tiers to separate on genuinely separable value.

**Expansion is assumed to be cheap to obtain.** In institutional accounts it frequently requires a new approval, a
new budget line, and a repeat of the procurement process. It is a sale, and `CAC.md`'s logic applies to it.

**Usage-driven expansion is counted without the cost that accompanies it.** More usage means more cost to serve,
and for AI features the marginal cost may consume most of the marginal revenue. `LTV.md` needs margin, not revenue.

**Expansion is used to rescue weak unit economics.** If the model only works with expansion, the model does not
work — it depends on a behavior no customer has yet exhibited.

---

# Related

| | |
| --- | --- |
| `Subscription.md` | Tier structure and separable value |
| `Freemium.md` | The free-to-paid version of the same trigger question |
| `06-business` `Revenue.md` | Where expansion must be justified or excluded |
| `08-product`, `11-growth` | Where the mechanism is built and driven |

---

> **Concept Note**
>
> Point at the requirement that the upgrade unlocks.
>
> If you cannot, expansion revenue is zero — and a model that needs
> it is a model that does not close.
