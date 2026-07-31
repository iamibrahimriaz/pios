---
Title: Mental Models
Module: 06-business
Section: core
Category: Thinking Framework
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the lenses through which a business model should be examined.
Audience:
  - AI Agents
  - Founders
  - Product Managers
Prerequisites:
  - 06-business/core/03-Core-Principles.md
Outputs:
  - Multi-perspective business analysis
Related Modules:
  - 07-strategy
  - 11-growth
Tags:
  - Business
  - ../constitution/core/04-Mental-Models.md
---

# Mental Models

---

# Model Statement

> Every business model is a story about money told in advance.
>
> These lenses are ways of checking which parts of the story are load-bearing.

---

# 1. Value Capture

**Reveals:** whether the price is defensible.

```
value delivered  >  price  >  cost to serve
```

Both inequalities must hold, and the gaps must be large enough to survive being wrong.
A price close to value leaves no reason to buy; a price close to cost leaves no business.

**Hides:** it assumes value is felt. An absorbed cost of the same size is worth less
commercially than an invoiced one, because nobody is looking for a solution to it.

---

# 2. Willingness, Ability, Authority

**Reveals:** which of the three ways a sale fails applies here.

| Fails on | Sounds like | Fix |
| --- | --- | --- |
| Willingness | "Interesting, but we're fine" | Value is invisible or too small |
| Ability | "We love it, we can't afford it" | Price exceeds segment budget |
| Authority | "I'd have to take this to the partners" | Wrong buyer targeted |

**Hides:** in solo or consumer contexts all three collapse into one person — which
simplifies the sale but concentrates all three risks in a single decision.

---

# 3. The Free Anchor

**Reveals:** the real price ceiling.

The status quo costs nothing, requires no approval, and carries no implementation risk.
Every price is therefore compared against zero, not against a competitor.

```
price  <  value delivered − switching cost
```

If that inequality fails, no amount of competitive positioning rescues it.

**Hides:** some free alternatives carry hidden costs the user has normalized. Surfacing
those is a sales strategy, not a modeling shortcut.

---

# 4. Unit Economics

**Reveals:** whether growth helps or hurts.

```
LTV = price × gross margin × (1 / churn)
LTV : CAC  and  payback period
```

A business with LTV:CAC below 1 gets worse with every customer acquired. Growth is not a
fix for bad unit economics; it is an accelerant.

**Hides:** the model assumes churn is constant and customers are homogeneous. Early
customers are usually better than later ones, which flatters early data.

---

# 5. Sensitivity Over Point Estimates

**Reveals:** how much the verdict depends on things nobody knows.

Vary the two unknowable inputs — CAC and churn — across a plausible range and watch what
happens to the verdict.

| If the verdict... | Then... |
| --- | --- |
| Holds across the range | The business is robust to its unknowns |
| Flips within the range | The verdict is `INSUFFICIENT EVIDENCE`, not `VIABLE` |
| Only works at the optimistic end | State that plainly |

**Hides:** sensitivity on two inputs while four others stay fixed still overstates
confidence. Vary what matters, and say what you held still.

---

# 6. Backwards Solving

**Reveals:** the budget, when the estimate is unavailable.

Instead of guessing CAC, compute what CAC the model can tolerate:

```
For LTV:CAC ≥ 3, CAC must stay below LTV / 3.
```

This converts an unknowable input into an actionable constraint that module 11 can work
against.

**Hides:** it produces a target, not a prediction. Undeclared, it reads as research — and
that is the misuse this model most invites.

---

# 7. Cost to Serve

**Reveals:** whether margin survives the product actually working.

Build it from components rather than assuming a percentage:

| Component | Grows with |
| --- | --- |
| Infrastructure | Usage |
| Support | Customer count and product complexity |
| Third-party / AI operations | Usage, often superlinearly |
| Compliance | Fixed, allocated across customers |

Per-operation AI costs deserve particular attention: they scale with engagement, which
means the most valuable customers can be the least profitable.

**Hides:** cost to serve usually falls with scale — but the point at which it does may be
beyond the customer count the business can reach.

---

# 8. The Sales Motion Ladder

**Reveals:** whether the price and the sales method match.

| Annual price | Motion that pays for itself |
| --- | --- |
| Under ~$1k | Self-serve; any human involvement destroys margin |
| ~$1k–10k | Founder-led or inside sales |
| Over ~$10k | Field sales, procurement, committees |

A product priced for self-serve that requires a demo to sell has a structural mismatch, and
so does the reverse.

**Hides:** thresholds vary by market and are conventions rather than laws. State the ones
being used.

---

# 9. Cycle Against Runway

**Reveals:** a timing risk that no financial ratio surfaces.

A nine-month sales cycle with twelve months of funding means roughly one attempt. That is a
strategic constraint, not a scheduling detail.

**Hides:** it depends on the operator's runway, which is an **OPERATOR** input and may not
be known. If unknown, record the cycle length and flag the dependency.

---

# 10. The Inversion

**Reveals:** what the model is avoiding.

Ask: **if this business cannot work, which number would be the reason?**

Then look at that number and ask honestly where it came from. It is usually CAC, churn, or
a price nobody in the segment has been asked about.

**Hides:** nothing. It is the correction for a module whose output naturally looks
authoritative.

---

# Combining Models

| Situation | Model |
| --- | --- |
| Testing whether the price can hold | Value Capture |
| Diagnosing how a sale would fail | Willingness, Ability, Authority |
| Setting the price ceiling | The Free Anchor |
| Judging whether growth helps | Unit Economics |
| Handling unknowable inputs | Sensitivity, Backwards Solving |
| Protecting the margin | Cost to Serve |
| Matching price to selling method | The Sales Motion Ladder |
| Surfacing timing risk | Cycle Against Runway |
| Checking yourself | The Inversion |

Apply Value Capture and The Free Anchor before pricing. Apply Sensitivity before writing
any verdict. Apply The Inversion last.

---

# Self Assessment

- Does value exceed price by enough to survive being wrong?
- Do I know which of the three payment capacities is weakest?
- Can the price clear the free anchor after switching cost?
- Would growth improve or worsen this business?
- Did I show sensitivity on the inputs nobody can know?
- Did I derive cost to serve from components?
- Do the price and the sales motion match?
- If this cannot work, which number is the reason?

---

> **Mental Model Principle**
>
> A financial model is most dangerous when it is internally consistent
> and externally unchecked.
>
> Every lens here is a way of checking it from outside.
