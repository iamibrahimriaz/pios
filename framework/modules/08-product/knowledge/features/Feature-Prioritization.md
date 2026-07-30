---
Title: Feature Prioritization
Module: 08-product
Section: knowledge/features
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Score consistently, and record where the score disagrees with the cut.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 08-product/knowledge/features/Feature-Discovery.md
Outputs:
  - prioritization
Related Modules:
  - 04-problem
  - 07-strategy
Tags:
  - Product
  - Prioritization
  - Method
---

# Feature Prioritization

---

# What It Is

Scoring every requirement on four factors, then sequencing.

| Factor | Meaning |
| --- | --- |
| **Problem weight** | Rank of the problem it serves — from `04-problem` |
| **Reach** | Share of the primary segment affected |
| **Confidence** | Evidence standing of the underlying problem |
| **Effort** | Build cost |

Scoring makes the ordering arguable rather than asserted. One method, applied to every row — **an inconsistently
applied method is worse than none, because it looks like analysis.**

And the rule that keeps the arithmetic subordinate:

> Where the score and the tier disagree, say so. A high-scoring requirement below the line is legitimate —
> `07-strategy`'s cut outranks this module's arithmetic — but the disagreement is recorded, not hidden by adjusting the
> score until it agrees.

---

# When It Applies

In Move 5 (Order), after behavior and edge states exist — because estimating effort without the unhappy paths estimates
about half the work.

---

# How to Apply It Here

**Take problem weight and confidence from module 04 unchanged.** They are already tagged and ranked. Re-deriving them
here replaces evidence with a fresh opinion that outranks it.

**Score effort after Move 4.** The five edge categories are most of the implementation. Effort estimated from
happy-path behavior is systematically low, and it is low by more for the requirements that matter.

**Record the score-versus-tier disagreements as a list.** They are the most informative output of this move: they show
where the cut is costing something identifiable, which is exactly what `07-strategy` needs at a later review.

**Let low confidence lower the score.** A requirement serving an assumed problem is a bet. Scoring it as though the
problem were verified hides the risk `07-strategy` registered.

**Do not add factors.** Four applied consistently beats six applied variably. Any additional factor favors something,
and its inclusion needs justifying from the research.

---

# Where It Misleads

**Effort dominates when it is the only well-understood factor.** Ordering drifts toward cheap work, and the sharpest
problem — usually the hardest — never gets solved. `07-strategy`'s end-to-end test is the counterweight.

**Scores get adjusted until the ordering matches intuition.** The tell is a score that changed after the sequence was
drafted. Recording disagreement rather than resolving it is the honest alternative.

**Inconsistent application looks like rigor.** Some rows scored, others assigned, all presented in one table. That is
worse than an unscored list, because the table implies a method.

**Prioritization is confused with the cut.** Module 07 decided what is in. This move decides the order of what is in,
and produces the first shippable slice. It does not admit anything new.

**Reach is estimated from the market rather than the segment.** The share affected is a share of the *primary segment*
from `03-user`. Using the whole market inflates every row equally and discriminates between none.

---

# Related

| | |
| --- | --- |
| `Feature-Discovery.md` | The spine that admits requirements |
| `Dependencies.md` | What must precede what |
| `08-product` `Roadmap.md` | Where disagreements are recorded |
| `07-strategy` | The cut, which outranks this arithmetic |

---

> **Concept Note**
>
> One method, every row — and when the score disagrees with the cut,
> write the disagreement down.
>
> A score adjusted to agree with the answer has stopped being a
> score.
