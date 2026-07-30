---
Title: Prioritization
Module: 07-strategy
Section: knowledge/solutions
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Order work by the ranked problems, and keep the deferral ledger honest.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 07-strategy/knowledge/solutions/Tradeoffs.md
Outputs:
  - Order within mvp_definition and roadmap
Related Modules:
  - 04-problem
  - 08-product
Tags:
  - Strategy
  - Prioritization
  - Method
---

# Prioritization

---

# What It Is

The ordering of everything the chosen approach implies — driven by `04-problem`'s ranking rather than by a scoring
framework invented here.

The ranking already exists. `04-problem` scored every problem on frequency, severity and workaround adequacy, and
identified the sharpest. Prioritization here is the application of that order, not a re-derivation of it.

| Above the line | Below the line |
| --- | --- |
| Required to solve the sharpest problem end to end | Everything else, recorded with a reason |
| The compliance floor from `09-technology`'s obligations | Capabilities for the second segment |
| The failure paths for the core journey | The second-ranked problem, unless the first is confirmed solved |

Everything below the line enters the **deferral ledger**: what, why, and what would bring it back. Nothing is dropped
silently.

---

# When It Applies

In Move 4 (Cut) and Move 6 (Sequence). `08-product` inherits the order as requirement priority, and its boundary
check compares its list against this one mechanically.

---

# How to Apply It Here

**Use the existing ranking and say when you depart from it.** Departures are legitimate — a lower-ranked problem may be
a dependency of the higher one — but an unexplained reordering means the ranking has been replaced by preference.

**Prioritize by problem, not by feature.** Features are `08-product`'s unit. Ordering features here produces a
requirements list before the requirements exist, and it breaks the trace.

**Record the reason and the reconsider trigger for every deferral.** "Deferred until a second segment is served" is a
ledger entry. A missing item with no record is scope that will be re-argued from scratch.

**Put the compliance floor above the line regardless of rank.** Obligations are not prioritizable — `09-technology`
derives them from the jurisdiction and `06-business` established they cannot be a paid tier.

**Keep dependencies visible.** Something low-value that unblocks something high-value is high priority. That is a
sequencing fact, not a re-ranking, and it should be labeled as such.

---

# Where It Misleads

**A new prioritization framework gets introduced and quietly overrides the research.** Scoring schemes applied here
re-rank problems using criteria that are not evidence, and the result outranks `04-problem`'s tagged, sourced ordering.

**Effort gets weighted until cheap work wins.** Ordering by ease produces a product made of easy things, and the
sharpest problem — usually the hardest — never gets solved. `MVP.md`'s end-to-end test is the guard.

**Deferral becomes deletion.** Items leave the document rather than the scope, and the reasoning is lost. Six weeks
later the same item is proposed as a new idea.

**Priority is assigned to everything, which assigns it to nothing.** If most items are high priority, the ordering has
no information in it. The ledger's value is the line, not the labels.

**The order gets set by who asked.** A customer request, an investor comment, or a partner's requirement arrives with
social weight and no evidence. `08-product` requires a trace to a ranked problem for exactly this reason.

---

# Related

| | |
| --- | --- |
| `Tradeoffs.md` | The choice this orders the consequences of |
| `07-strategy` `MVP.md` | Where the line is drawn |
| `04-problem` | Where the ranking comes from |
| `08-product` | Where the order becomes requirement priority |

---

> **Concept Note**
>
> The ranking already exists — apply it, and justify any departure.
>
> A new scoring scheme at this point outranks evidence with
> arithmetic, and nobody notices the substitution.
