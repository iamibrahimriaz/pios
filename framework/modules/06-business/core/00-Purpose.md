---
Title: Purpose
Module: 06-business
Section: core
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define why the Business module exists and what it establishes for the rest of the run.
Audience:
  - AI Agents
  - Founders
  - Product Managers
Prerequisites:
  - constitution/core
  - 05-competition gate passed
Outputs:
  - Shared understanding of what this module establishes
Related Modules:
  - 07-strategy
  - 11-growth
Tags:
  - Business
  - Purpose
  - Foundation
---

# Purpose

---

# Overview

The research stage established that a market exists, a person has a problem, and nobody
serves them well.

None of that means a business exists.

This module asks the separate question: **can this be sold, at a price someone will pay,
for more than it costs to acquire and serve them?**

It is the first module in the `decide` stage. From here the run stops describing and
starts committing.

---

# Purpose Statement

> Establish whether a viable business exists around the solution — and be explicit
> about how much of that conclusion is arithmetic performed on assumptions.

---

# Why This Module Exists

Products fail commercially for reasons that have nothing to do with product quality:

- The person who wants it cannot authorize the purchase.
- The price exceeds what the segment spends on software at all.
- The cost to serve consumes the margin.
- Acquiring a customer costs more than the customer is worth.
- The sales cycle is longer than the runway.

Each of these is knowable, or at least modelable, before anything is built. This module
is where they are examined.

---

# The Characteristic Danger

This module produces the most convincing-looking output in the framework and the least
verifiable.

A unit economics table is arithmetic, and arithmetic reads as rigor. But `LTV:CAC = 4.2`
derived from an assumed price, an assumed margin, an assumed acquisition cost and an
assumed churn rate is a guess carried to one decimal place.

> **Arithmetic does not create evidence.**

Two of the model's load-bearing inputs — acquisition cost and churn — **cannot be known
before launch.** Not by any amount of research. The correct response is to tag them,
present sensitivity rather than a point estimate, and let the reader see the range.

Most of this module's machinery exists to make that honesty structural rather than
optional.

---

# Core Objectives

- Identify who signs, and whether they can.
- Establish what the problem costs today, before deciding what to charge.
- Set a price anchored to value, to competitors, and to free.
- Derive cost to serve rather than assuming a margin.
- Model the economics with every input tagged.
- Name a route to the first ten customers.
- State plainly whether the model survives its own assumptions.

---

# What AI Should Learn Here

- Willingness, ability and authority to pay are three different things.
- Value comes before price. A price justified afterward is a preference.
- The status quo is free; a price must be defensible against nothing at all.
- Gross margin is derived from cost to serve, never assumed.
- A benchmark is evidence about other companies, not about this one.
- Ten named customers beat any channel strategy.
- A model whose verdict flips across a plausible assumption range is not a forecast.

---

# Scope

**This module covers**

- Payer identification and purchase authority
- Value quantification and price setting
- Cost to serve and gross margin
- Unit economics and sensitivity
- Go-to-market and the first ten customers
- Revenue model and break-even
- The viability verdict

**This module does not cover**

| Not here | Belongs to |
| --- | --- |
| Market sizing | `02-market` |
| Competitor pricing capture | `05-competition` |
| What to build | `07-strategy` |
| Infrastructure design | `09-technology` — this module gives it a budget |
| Channel execution | `11-growth` |
| Metric instrumentation | `12-metrics` |

---

# Position in the Run

```
02-market ┐
          ├→ [ 06-business ] → 07-strategy → ⏸ HUMAN CHECKPOINT
05-competition ┘
```

---

# What This Module Hands Forward

| Output | Consumed by | Used for |
| --- | --- | --- |
| `business_model` | 07 | Whether the chosen approach can pay for itself |
| `pricing_strategy` | 07, 08, 11 | Packaging, tiers, messaging |
| `unit_economics` | 07, 12 | Viability and metric targets |
| `go_to_market` | 11 | Channels and acquisition targets |
| `revenue_model` | 12 | Break-even tracking |
| **Cost-to-serve constraint** | 09 | The per-customer budget the architecture must fit |

The cost-to-serve constraint is the handoff most often dropped. Without it, module 09
designs whatever is technically best and the margin quietly disappears.

---

# Success Criteria

- The payer is a specific role with a mapped approval path.
- Value was computed before price, from module 04's cost figures.
- The price is defended against free, not only against paid competitors.
- Margin is derived, not asserted.
- Every number carries a tag, and assumed inputs are openly the majority when they are.
- Ten plausible first customers exist on the page.
- The verdict is no more confident than the inputs allow.

---

# Self Assessment

- Do I know who signs, and whether they can?
- Did value come before price?
- Can I answer why anyone pays when the alternative is free?
- Did I derive the margin?
- Do I know which assumption the verdict rests on?
- Could I go and find the first ten customers?

---

> **Purpose Principle**
>
> A good product with no viable business is a hobby with a roadmap.
>
> This module is where that gets said out loud, before anything is built.
