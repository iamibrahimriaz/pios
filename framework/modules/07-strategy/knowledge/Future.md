---
Title: Future
Module: 07-strategy
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Keep the far horizon as direction, and state the cost of planning it.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 07-strategy/knowledge/V2.md
Outputs:
  - Long-range direction within roadmap
Related Modules:
  - 09-technology
Tags:
  - Strategy
  - Roadmap
  - Concept
---

# Future

---

# What It Is

The horizon beyond the next release — recorded as **direction only**, and deliberately not planned.

The framework's position is that beyond V2 the useful output is a short statement of where this is going and what
would have to be true, because everything more specific will be wrong in a way that costs money now:

| Legitimate content | Not legitimate |
| --- | --- |
| The direction the product is heading | Features with dates |
| Which constraints would have to lift | A phased plan of releases |
| What would need to be true about the market | Revenue projections by year three |
| Which architectural decisions would foreclose it | Architecture built for it today |

The last row is the one that matters. A far horizon is free to hold and expensive to build for.

---

# When It Applies

Optionally, closing Move 6. It also connects back to `01-idea`'s vision — the far horizon should be recognizably the
same destination, or one of the two has drifted.

---

# How to Apply It Here

**Write two or three sentences and stop.** The question is which direction, not which features. Anything longer
invites the specificity the evidence cannot support.

**Name the decisions that would foreclose it.** If a likely long-term direction requires multi-tenancy, a different
data model, or a second jurisdiction, `09-technology` should know it as *context*. Knowing costs nothing; building
costs immediately.

**Check it against `01-idea`'s vision.** If the far horizon here is a different destination from the one recorded at
the start, that is a real finding — the strategy has moved, and either the vision should be updated or the drift
questioned.

**State the market conditions it depends on.** A direction requiring a regulatory change, a technology cost falling,
or a behavior shifting is contingent, and `02-market`'s trends say how plausible each is.

**Keep it out of the deliverables that drive building.** It belongs in the roadmap's horizon section and in the
executive summary. It does not belong anywhere `08-product` or `09-technology` reads as a requirement.

---

# Where It Misleads

**A far horizon is the most common justification for present scope.** Every unargued capability can be defended by
pointing at a sufficiently large future, and each defense is individually reasonable. `01-idea`'s `Vision.md` names
this as the framework's primary scope-creep vector; this is where it lands.

**Detailed long-range plans read as strategic maturity.** They are the least evidenced content in the document and
the most likely to be quoted externally. Fidelity should fall with distance, visibly.

**Building for the future is called future-proofing.** It is speculative complexity with an immediate cost —
`09-technology`'s architecture inflation, sourced from here. Recording a direction is the correct amount of
preparation.

**The horizon expands to justify the operator's ambition rather than describing the product.** `01-idea`'s
operator-goal question already established the ambition, and it belongs there rather than smuggled into the roadmap.

**It gets promised.** A direction repeated to a customer or an investor becomes a commitment, and it was written with
the least information the project will ever have.

---

# Related

| | |
| --- | --- |
| `V2.md` | The nearest horizon still held as direction |
| `Vision.md` | The strategic frame this sits inside |
| `solutions/Long-Term-Vision.md` | Where the chosen approach eventually leads |
| `09-technology` | Where building for it becomes inflation |

---

> **Concept Note**
>
> Two sentences, no dates, no features.
>
> A large future is free to describe and ruinous to build for — and
> almost every unargued feature arrives holding one.
