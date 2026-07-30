---
Title: Tradeoffs
Module: 07-strategy
Section: knowledge/solutions
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Weight the comparison criteria and record what rejecting an option costs.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 07-strategy/knowledge/solutions/Solution-Exploration.md
Outputs:
  - chosen_approach
Related Modules:
  - 04-problem
  - 06-business
Tags:
  - Strategy
  - Decision
  - Method
---

# Tradeoffs

---

# What It Is

The comparison, and the record of what the choice costs.

The criteria come from the research, not from preference:

| Criterion | Source |
| --- | --- |
| Solves the sharpest problem | `04-problem` |
| Solves the next-ranked problems | `04-problem` |
| Fits the identified gap | `05-competition` |
| Defensible | `05-competition` |
| Supports the modeled price | `06-business` |
| Buildable by the assumed team | `06-business` cost structure |
| Time to first customer | `06-business` go-to-market |
| Survives if the assumed problem is wrong | `04-problem` evidence standing |

**Weight them, and say how.** Unweighted scoring lets a strong performance on a minor criterion outvote a weak one on
a decisive criterion.

Then three records, of which the second is what makes this a decision rather than a preference: **why this one**,
**what was rejected and what we lose by rejecting it**, and **what we are betting on.**

---

# When It Applies

In Move 2 (Compare) and Move 3 (Choose). It closes with the **reversal trigger** — what would make us choose
differently.

---

# How to Apply It Here

**Publish the weights before scoring.** Weights chosen after the scores are the scores rewritten. Stating them first
is what makes the comparison auditable.

**Give the last criterion real weight where `04-problem` declared a shortfall.** An approach retaining some value even
if the central problem is less severe than believed is worth more than its raw score suggests. That is the framework's
explicit instruction, and it is the criterion most often set to zero.

**Name what each rejected option offered.** Every option had something. Naming it prevents the rejected approach
returning later as a feature — which is how scope creep enters with a justification already attached.

**State the bet in one sentence.** "We are betting that solo GPs will trust an AI draft enough not to re-read it
line by line." That sentence is the load-bearing assumption for the human checkpoint and the first entry in the risk
register.

**Write the reversal trigger.** A strategy with no reversal condition cannot be re-examined honestly, because there
is no agreed signal that it should be.

---

# Where It Misleads

**Scoring is performed to confirm a choice already made.** The signals are unweighted criteria, uniform scores, and a
winner that was obvious from the first paragraph. The gate's ordering — options before choice — exists to make this
visible.

**Criteria get added until the preferred option wins.** Any new criterion favors something. If a criterion is not in
the framework's list, its inclusion needs justifying from the research.

**The cost of rejection is recorded as zero.** "We rejected the workflow replacement because it was too large" states
the reason and not the loss. The loss is what someone will later try to recover as a feature.

**Ties are broken by preference and presented as analysis.** `Vision.md` is the legitimate tiebreaker, and it must be
recorded as having been used.

**Reversibility is not weighed.** Two options with equal scores where one is easy to unwind are not equal. Where
evidence is thin — and it usually is at this point — the reversible option is worth more than the score shows.

---

# Related

| | |
| --- | --- |
| `Solution-Exploration.md` | The options being compared |
| `Prioritization.md` | Ordering what survives the choice |
| `Vision.md` | The legitimate tiebreaker |
| `risks/Mitigation.md` | Where the bet becomes a registered risk |

---

> **Concept Note**
>
> Weight the criteria before you score, and write down what rejecting
> each option costs.
>
> An unrecorded rejection returns in six months as a feature request
> with an argument already prepared.
