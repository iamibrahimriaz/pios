---
Title: UX Comparison
Module: 05-competition
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Compare competitors on task completion rather than on appearance.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 05-competition/knowledge/Feature-Comparison.md
Outputs:
  - UX assessment within competitor_matrix
Related Modules:
  - 10-execution
Tags:
  - Competition
  - UX
  - Concept
---

# UX Comparison

---

# What It Is

An assessment of how competitors handle the work — measured in steps, decisions and recoveries rather than in visual
quality.

| Compare on | Not on |
| --- | --- |
| Steps to complete the top-ranked job | Visual style |
| Where the flow requires a decision the user cannot make | Whether it looks modern |
| What happens when something goes wrong | Colors and typography |
| Whether it works under `03-user`'s real conditions | How it demos |
| Time to first useful output for a new user | Feature discoverability on the home screen |

The useful comparison is against the **status quo's** step count. If the incumbent process takes four steps and this
product takes six, the interface quality is irrelevant.

---

# When It Applies

Alongside Move 3 (Test), where interaction cost is part of whether a problem is solved "well" or only "partly". It
feeds `10-execution`'s flow design.

---

# How to Apply It Here

**Count steps for the specific job from `03-user`.** A single named task, counted end to end, in both the competitor
and the current workflow. That number is comparable; an impression is not.

**Test under the real conditions.** Interrupted, one-handed, with someone waiting, on the device they actually use.
Products diverge sharply between the demo and the ward, and `03-user`'s environment findings say which conditions
apply.

**Look at the failure paths.** How the product behaves when data is missing, a connection drops, or input is invalid
is where installed tools earn loyalty — and where new ones lose it. These map directly onto `08-product`'s edge
categories.

**Assess time to first useful output.** For a new user with real data, how long until something worth having? That
figure predicts trial abandonment better than any feature comparison, and `11-growth` needs it.

**Record what they got right.** Conventions users already know are an asset to inherit, not a differentiator to
avoid. Novelty in an interface is a cost paid in retraining.

---

# Where It Misleads

**"Their UX is bad" is the most common and least reliable competitive claim.** It usually means unfamiliar or dated.
A product experts use daily is optimized for them, and its density is a feature to the trained user — the same
density that makes it look poor in a five-minute review.

**Interface quality is a fixable weakness.** It sits in `Weaknesses.md`'s bottom rows: closable in a quarter,
therefore not a foundation. A product whose only advantage is a better interface is competing on the dimension
easiest to copy.

**Screenshots and marketing tours get assessed instead of use.** The demo path is optimized. The real assessment
comes from reviews describing daily work, from trial use, and from support forums.

**Aesthetic preference is presented as a finding.** Unless it changes task completion, it is taste. `08-product`
bans the vocabulary — intuitive, clean, seamless — precisely because it cannot be built against.

**Familiarity is undervalued.** An interface staff already know has zero training cost. Beating it requires being
better by more than the retraining it imposes, which is part of `03-user`'s switching cost.

---

# Related

| | |
| --- | --- |
| `Feature-Comparison.md` | Where interaction cost affects the score |
| `Weaknesses.md` | Why interface gaps close fast |
| `03-user` | The conditions and the switching cost |
| `10-execution` | Where the flow is designed against these findings |

---

> **Concept Note**
>
> Count the steps for one named job, under the conditions it is really
> done in.
>
> "Their UX is bad" usually means "I am not the user it was built
> for" — and that is a finding about you.
