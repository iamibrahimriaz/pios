---
Title: Pricing Models
Module: 06-business
Section: knowledge/pricing
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Choose the pricing model and the unit deliberately, because the unit shapes behavior.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 06-business/knowledge/Pricing.md
Outputs:
  - Model and unit within pricing_strategy
Related Modules:
  - 12-metrics
  - 14-ai-systems
Tags:
  - Business
  - Pricing
  - Concept
---

# Pricing Models

---

# What It Is

The shape of the charge, and the unit it is charged against. The unit is a strategic choice and it changes
behavior more than the amount does.

| Model | Unit | Rewards | Penalizes |
| --- | --- | --- | --- |
| **Per user** | Seats | Small teams; predictable billing | Rollout — the customer pays to spread it internally |
| **Per organization** | The account | Simplicity of sale; internal adoption | Upside — a large customer pays the same as a small one |
| **Per transaction** | Work done | Alignment — revenue rises with the customer's success | Predictability; and the customer's bad quarter is yours |
| **Tiered by capability** | Feature set | Clear upgrade path | Requires genuinely separable value |
| **Usage or consumption** | Volume processed | Cost pass-through for expensive operations | Buyer's budget certainty |
| **Perpetual license** | The install | One-time institutional budgets | Recurring revenue and support funding |

The recurring caution for AI products: if the cost of serving scales with usage and the price does not, margin
falls as the best customers use it more.

---

# When It Applies

In Entry 3 (Price), after the anchors are set. The unit chosen becomes a metric definition in `12-metrics` and a
cost constraint in `14-ai-systems`.

---

# How to Apply It Here

**Pick the unit that grows with the value the customer receives.** If value comes per consultation, price per
consultation or per practice — not per administrator who happens to log in.

**Check the unit against the cost driver.** Where cost scales with usage — inference, processing, storage — a
flat price transfers all volume risk to the operator. `14-ai-systems` computes cost as a share of revenue per
user, and that check is where the mismatch shows.

**Avoid pricing against a unit the customer wants to reduce.** Per-seat pricing on a product that reduces
headcount asks the buyer to pay more for less benefit. That is the commercial conflict `05-competition` looks for
in *competitors* — do not build one in.

**Match the model to the buying process.** Institutional buyers frequently cannot approve variable bills.
Predictability is worth real money to them, and a capped or banded model may command a premium.

**State one model and one unit.** A pricing strategy offering several shapes is a decision deferred, and it makes
every downstream figure ambiguous.

---

# Where It Misleads

**Per-seat pricing is adopted as the default and is wrong for a large class of products.** It is the convention,
so it goes unexamined — and for anything that reduces work or is used occasionally by many people, it prices the
wrong thing.

**Usage-based pricing is presented as fair and transfers uncertainty to the buyer.** Fairness in the abstract does
not survive an unpredictable invoice, and it makes the product hard to budget for — which is fatal in institutional
markets.

**Tiers are drawn by feature count rather than by separable value.** A tier structure only works when each level
serves a distinguishable need. Splitting an indivisible product into three tiers produces one tier that sells and
two that confuse.

**The model gets chosen for revenue maximization at scale**, ignoring that it has to close the first ten deals.
Simplicity is worth more early than optimization.

**Cost-plus pricing anchors to the wrong thing entirely.** What it costs to serve sets the floor. Value sets the
ceiling. Pricing from the floor concedes everything in between.

---

# Related

| | |
| --- | --- |
| `Subscription.md` | Recurring mechanics, tiers and periods |
| `Enterprise.md` | Where variable pricing meets procurement |
| `06-business` `Pricing.md` | The three anchors |
| `14-ai-systems` | Where usage-driven cost is checked against price |

---

> **Concept Note**
>
> Choose the unit that rises with the customer's benefit and with
> your cost.
>
> Per-seat pricing on a product that removes work asks the buyer to
> pay more for getting less.
