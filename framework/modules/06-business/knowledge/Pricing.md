---
Title: Pricing
Module: 06-business
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Anchor price to value, to competitors, and to free — never to instinct.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 06-business/knowledge/ROI.md
Outputs:
  - pricing_strategy
Related Modules:
  - 05-competition
  - 03-user
Tags:
  - Business
  - Pricing
  - Method
---

# Pricing

---

# What It Is

A price with three anchors, none of which is judgment.

| Anchor | Rule |
| --- | --- |
| **Value** | A fraction of the annual value delivered. Above roughly a third, the price has to argue hard; below a tenth, it leaves money on the table and may signal low value |
| **Competitors** | From `05-competition`'s `pricing_comparison`. Position above, below or at market — and say why |
| **Free** | The status quo costs nothing, and the price must be justifiable against nothing at all |

The third is the one that gets skipped, and it is the hardest objection in the market:

> Why does someone pay «figure» when what they do today costs zero?

The answer must reference the value from Entry 2 and the switching cost from `03-user`. **If the price exceeds the
value net of switching cost, the model fails here** — not later in the economics.

---

# When It Applies

In Entry 3 (Price), after value and before economics. The figure produced becomes the input to CAC ceilings,
LTV, and `11-growth`'s payback check.

---

# How to Apply It Here

**Show the price as a share of value delivered.** That ratio is the justification, and it travels better than the
number. It also makes the price correctable when the value estimate changes.

**Choose the unit deliberately — it is a strategic decision.** Per user rewards small teams and penalizes
rollout; per transaction scales with the customer's success; per organization simplifies the sale and caps
upside. The unit shapes behavior more than the amount does.

**Check the unit against the frequency from `03-user`.** A per-use price on a monthly job produces a bill too
small to bother with; on a daily job it produces one large enough to be scrutinized.

**Position against competitors explicitly.** At, above or below, with the reason. Pricing below the market as a
strategy is the least defensible position available, particularly when the status quo is already free.

**Use the same price everywhere.** The figure in `02-market`'s sizing, in the LTV arithmetic, and here must be
one number. If it changes, the sizing changes with it.

---

# Where It Misleads

**Price gets chosen first and justified afterward**, which inverts the module and turns the analysis into
rationalization. The tell is a value calculation that lands conveniently at three times the chosen price.

**The free incumbent is answered only against paid competitors.** Justifying £40 a month against a rival's £60
ignores that most of the segment currently pays nothing. That comparison is the real one.

**Switching cost is left out of the price justification.** The buyer weighs price *plus* disruption against
value. A price that works on value alone can fail once migration and retraining are added, and `03-user`
quantified both.

**Willingness-to-pay research overstates by an unpredictable margin.** Stated price acceptance exceeds real
behavior consistently, which is why `04-problem`'s `Surveys.md` warns against resting a model on it.

**Discounting is planned into the price without being modeled.** A list price nobody pays makes every downstream
figure optimistic. `pricing/Discounts.md` covers the consequence.

---

# Related

| | |
| --- | --- |
| `ROI.md` | The value anchor |
| `pricing/Pricing-Models.md` | Choosing the model and the unit |
| `05-competition` | The competitor anchor, sourced and dated |
| `LTV.md`, `CAC.md` | What the price has to support |

---

> **Concept Note**
>
> Justify the price against zero, because that is what the
> competition charges.
>
> Value net of switching cost is the real ceiling — and it is lower
> than the value.
