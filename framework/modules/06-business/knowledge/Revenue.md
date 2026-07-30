---
Title: Revenue
Module: 06-business
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Build a revenue model whose inputs remain visible and whose precision is honest.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 06-business/knowledge/Pricing.md
Outputs:
  - revenue_model
Related Modules:
  - 02-market
  - 07-strategy
Tags:
  - Business
  - Revenue
  - Concept
---

# Revenue

---

# What It Is

The arithmetic connecting customers to money, with every input tagged and traceable.

```
customers × price × billing periods = revenue
```

Its inputs come from elsewhere and none of them are invented here:

| Input | Source | Typical standing |
| --- | --- | --- |
| Customer count | `02-market`'s SOM | `[assumption]` before launch |
| Price | Entry 3 | Justified, but unvalidated |
| Retention | Competitor benchmarks or assumption | `[assumption]` |
| Expansion | Upgrade path, if one exists | `[assumption]` |

A revenue model before launch is arithmetic on assumptions. That is legitimate; presenting it as a forecast is
not.

---

# When It Applies

Assembled through Entry 4 (Economics) and stated as `revenue_model` at Entry 6 (Test).

---

# How to Apply It Here

**Show the model as a formula with named inputs, not as a total.** A reader must be able to change one input and
see the consequence. A single figure cannot be argued with, only accepted or rejected.

**Use `02-market`'s SOM, and inherit its standing.** If SOM was derived from a channel and a conversion
assumption, revenue is as strong as that derivation. If SOM was a round share of SAM, this model is a
restatement of a guess.

**Separate new revenue from retained revenue.** They behave differently and are driven by different mechanisms —
one by `11-growth`'s channels, the other by its retention model. A single growth rate hides both.

**Round to the precision the weakest input supports.** Four significant figures on a model containing three
assumptions is false rigor, and it is the form in which guesses become plans.

**State the break-even customer count.** It is the most useful single number this module produces — a concrete,
checkable target, and `Financial-Risks.md` tests whether it sits inside SOM.

---

# Where It Misleads

**A precise total reads as knowledge.** "£214,000 in year one" carries an authority that "somewhere between 30
and 90 customers, so £90k–£270k" does not, and only the second is true. The framework's own principle applies: a
model built on six assumptions is not wrong because it is assumed — it is wrong when it hides that it is.

**Revenue models grow smooth curves nobody has earned.** Monthly compounding growth applied for thirty-six
months produces a number with no mechanism behind it. `11-growth` requires a named channel for every user, and
that requirement is what exposes it.

**Retention assumptions are the quietest large error.** A model at 2% monthly churn and the same model at 5% are
different businesses, and before launch neither figure has any evidence. `Retention.md` covers why.

**Expansion revenue is counted before an upgrade path exists.** If nothing in `08-product` produces a reason to
pay more, expansion is zero. `pricing/Upgrade-Path.md` is where it becomes real.

**The model gets built for the plan rather than the decision.** Its purpose is to answer whether a viable
business exists and what has to be true for it. A model that only produces an attractive total has answered
neither.

---

# Related

| | |
| --- | --- |
| `Pricing.md` | Where the price comes from |
| `LTV.md`, `CAC.md` | The per-customer arithmetic |
| `Financial-Risks.md` | Sensitivity and the break-even check |
| `02-market` | Where the customer count originates |

---

> **Concept Note**
>
> State a range and name the inputs, or state a number and hide
> them.
>
> The break-even customer count is worth more than the total —
> somebody can go and count it.
