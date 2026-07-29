---
Title: Workflow
Module: 06-business
Section: core
Category: Procedure
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The executable step-by-step procedure for running the Business module.
Audience:
  - AI Agents
Prerequisites:
  - 06-business/core/06-Framework.md
  - engine/state-schema.yaml
Outputs:
  - projects/<slug>/research/06-business.md
  - state.outputs.business_model
Related Modules:
  - 07-strategy
  - 11-growth
Tags:
  - Business
  - Workflow
  - Procedure
---

# Workflow

---

# Overview

`06-Framework.md` defines the method — the Ledger. This document is the procedure.

This is the first module in the `decide` stage. The research is finished; from here the
run commits to positions that later modules build on.

---

# Position in the Run

```
02-market ┐
          ├→ [ 06-business ] → 07-strategy → ⏸ HUMAN CHECKPOINT
05-competition ┘
```

| | |
| --- | --- |
| Stage | `decide` |
| Depends on | `02-market`, `05-competition` |
| Consumes | `tam_sam_som`, `pricing_comparison`, `segments` |
| Produces | `business_model`, `pricing_strategy`, `unit_economics`, `go_to_market`, `revenue_model` |
| On fail | return to `05-competition` |
| Human checkpoint | not here — the stage checkpoint follows `07-strategy` |

---

# Step 1 — Verify Upstream

1. Confirm `02-market` and `05-competition` are complete.
2. Read `pricing_comparison`. **If competitor pricing was marked unavailable across the
   board, Entry 3 has no anchor** — note it now rather than discovering it mid-model.
3. Read `tam_sam_som` — SOM bounds the break-even customer count.
4. Read `segments` and the buyer/blocker mapping from `03-user`.
5. Read `switching_cost` from `03-user` — it is subtracted from value in Entry 3.
6. Read cost per occurrence figures from `04-problem` — they are the value basis.
7. Read the regulatory cost estimate from `02-market` — it belongs in the cost structure.

---

# Step 2 — Read Before Writing

1. `engine/evidence-policy.md`
2. `06-business/core/03-Core-Principles.md`
3. `06-business/core/06-Framework.md` — the Six Entries
4. `06-business/core/09-Research-Methodology.md` — **read carefully**; this module is
   where invented numbers are hardest to detect
5. `06-business/core/08-Questions-To-Answer.md`
6. `06-business/knowledge/` — CAC, LTV, Pricing, GTM, Retention
7. `06-business/knowledge/pricing/` — Pricing-Models, Freemium, Trials, Enterprise

---

# Step 3 — Establish the Payer

Entry 1. Identify who signs, distinguish from the user, and assess willingness, ability
and authority separately.

Find the purchase trigger. Record who could block.

---

# Step 4 — Establish Value

Entry 2. **Before touching price.**

Take cost per occurrence and frequency from `04-problem`. Compute annual value at stake.
Estimate the share the product captures.

Flag whether the cost is visible or absorbed, and whether the payer bears it.

---

# Step 5 — Set Price

Entry 3. Anchor to value, to competitor pricing, and to free.

Write all three justifications. The free justification is mandatory whenever the status
quo costs nothing — which module 05 will almost always have established.

Subtract switching cost from value before concluding the price is affordable.

---

# Step 6 — Model Economics

Entry 4. Build the table. **Tag every input.**

Derive cost to serve rather than assuming a margin. Include:

- infrastructure per customer
- support per customer
- third-party and AI operation costs

Name the load-bearing assumption. Run the sensitivity table.

> If more than half the inputs are assumed, the output is a sensitivity analysis, not a
> forecast. Present it as one.

---

# Step 7 — Route to Market

Entry 5. Name the first ten customers, or profile them specifically enough to find.

If this step cannot be completed concretely, that is a finding — record it plainly rather
than substituting channel categories.

State the sales motion and cycle length.

---

# Step 8 — Test Viability

Entry 6. Run the thresholds. State which fails first as assumptions worsen.

Write the verdict, and write what would have to be true.

---

# Step 9 — Assemble and Write to State

Fill `13-Template.md` into `projects/<slug>/research/06-business.md`.

```yaml
outputs:
  business_model:    # payer, value, structure
  pricing_strategy:  # price, model, unit, justifications
  unit_economics:    # inputs with tags, ratios, sensitivity
  go_to_market:      # first 10, channels, motion, cycle
  revenue_model:     # type, projection, break-even
```

Record the **cost-to-serve constraint** for module 09 — the per-customer infrastructure
budget the architecture must stay inside. This is easy to omit and expensive to discover
later.

Append every assumed input to `state.assumptions` with a validation method.

---

# Step 10 — Review

Run all four passes of `engine/review-loop.md`.

The adversarial pass for this module:

- Did I choose a price and then justify it?
- How many of my economics inputs are actually sourced?
- Would this price survive a conversation with someone in the segment?
- If the status quo is free, have I genuinely answered why anyone pays?
- Is my CAC assumption a number, or a hope?
- Could I name a single real organization that would buy this?
- If the verdict is favorable, which assumption is carrying it?

The coherence pass: does the price fit inside the segment's plausible budget, given what
module 03 established about who they are? A price that exceeds a solo practitioner's
entire annual software spend is a contradiction, not a positioning choice.

---

# Step 11 — Gate

Evaluate against `11-Quality-Gate.md` and universal gates U1–U6.

| Verdict | Action |
| --- | --- |
| Pass | Continue to Step 12 |
| Fail | Revise, or `return to 05-competition` if pricing anchors are missing. Three attempts, then halt |

A `NOT VIABLE AS MODELED` verdict can still pass the gate. The gate checks whether the
analysis was honest, not whether the business works.

---

# Step 12 — Hand Off

1. Append `06-business` to `state.run.completed_modules`.
2. Ensure the cost-to-serve constraint is visible to module 09.
3. Hand to `07-strategy`.

---

# Handoff Contract

| Consumer | Reads | Uses it for |
| --- | --- | --- |
| `07-strategy` | `business_model`, `unit_economics` | Whether the chosen approach can pay for itself |
| `08-product` | `pricing_strategy` | Packaging and tier boundaries |
| `09-technology` | Cost-to-serve constraint | Architecture must fit the per-customer budget |
| `11-growth` | `go_to_market`, CAC assumptions | Channel strategy and acquisition targets |
| `12-metrics` | `revenue_model`, unit economics | Metric targets and break-even tracking |

The cost-to-serve constraint is the most frequently dropped handoff in the framework.
Module 09 designs an architecture; without a budget it designs whatever is technically
best, and the margin disappears.

---

# Failure Modes

| Symptom | Cause | Fix |
| --- | --- | --- |
| Price appears before value | Steps 4 and 5 reversed | Recompute value first |
| Precise LTV, no tags | Step 6 shortcut | Tag every input; add sensitivity |
| Payer = user, unexamined | Step 3 skipped | State it explicitly either way |
| No answer to "why pay when free exists" | Step 5 incomplete | Mandatory whenever status quo is free |
| Margin assumed | Cost to serve not derived | Build it from components |
| Channels instead of customers | Step 7 rushed | Name ten, or record that you cannot |
| Verdict softer than the numbers | Step 8 avoided | State which threshold fails |

---

# When Most Inputs Are Assumed

Normal, and workable — provided the document says so.

1. Tag every assumed input.
2. Replace the point estimate with the sensitivity table as the primary output.
3. Set confidence to `low`.
4. Name the two or three inputs most worth establishing, and add them to
   `state.open_questions`.
5. Set the verdict to `INSUFFICIENT EVIDENCE` if the outcome flips across plausible
   assumption ranges.

A model that says "viable if CAC stays under «figure»; we have not established CAC" is
useful. One that says "LTV:CAC is 4.2" without saying every input was guessed is not.

---

> **Workflow Principle**
>
> This module produces the most convincing-looking output in the framework.
>
> Its main discipline is refusing to let arithmetic pass for evidence.
