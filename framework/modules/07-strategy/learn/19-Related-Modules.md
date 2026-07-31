---
Title: Related Modules
Module: 07-strategy
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show how the Strategy module connects to the framework and which chains pass through it.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 07-strategy/README.md
Outputs:
  - Understanding of the strategy stage's position in the chain
Related Modules:
  - 04-problem
  - 06-business
  - 08-product
Tags:
  - Strategy
  - Relationships
  - Learn
---

# Related Modules

---

# Overview

Everything upstream feeds this module and everything downstream elaborates it. It is
the only module in the framework with that property, and it is why its failures are the
most expensive.

---

# What It Takes In

| Input | From | Used for |
| --- | --- | --- |
| `ranked_problems` | `04-problem` | The criterion the choice is justified against |
| The declared shortfall, if any | `04-problem` | A weighting in the comparison |
| `gap_analysis` | `05-competition` | The opening the approach aims at |
| `business_model` | `06-business` | The economic constraints the choice must fit |

The gate fails back to `04-problem`, because a choice that cannot be justified against
the ranking usually means the ranking was not real — either reverse-engineered, or
built on inference that will not carry a decision.

---

# What It Sends Forward

| Output | Who consumes it | What they do with it |
| --- | --- | --- |
| `chosen_approach` | `08-product`, `09-technology` | The thing being specified and built |
| `mvp_definition` | `08-product`, `10-execution` | The scope of the first release |
| `non_goals` | `08-product`, `14-ai-systems` | What must not re-enter, and what not to propose |
| `risk_register` | `10-execution`, `13-operations` | What is being watched, by whom |
| `roadmap` | `10-execution`, `11-growth` | The sequence, and what growth can assume exists |

---

# The Four Chains

Three of the framework's four chains pass through this module.

**Milestone Zero.** Declared in `04-problem`, made **binding here**, sequenced first in
`10-execution`, and gating spend in `11-growth`. This module is where an uncertainty
becomes a commitment to resolve it before anything else.

**The declared shortfall.** Declared in `04-problem` and weighted here. This is the
only place the shortfall does work, and if it does none, the mechanism has failed
silently.

**The economic constraints.** Set in `06-business`, honored here, tested in `09`, `11`
and `13`. When one of those checks fails, the regress lands either on `06-business` for
the price or on this module for the scope — so this module is one of the two places a
downstream failure comes back to.

The fourth chain — the obligation chain from `02-market` through `09-technology` to
`13-operations` — passes around this module rather than through it. That is worth
knowing: a regulatory constraint is not a strategic choice, and treating it as one is
how obligations become negotiable.

---

# Where the Non-Goals Reappear

| Module | How |
| --- | --- |
| `08-product` | Anything out of MVP scope moves to the roadmap, not silently dropped — non-goals are the boundary between "not now" and "not ever" |
| `10-execution` | Milestones are sequenced within the cut line drawn here |
| `11-growth` | Expansion paths cannot assume a non-goal |
| `14-ai-systems` | A capability that is a non-goal is rejected rather than deferred, so it stops being re-proposed |

Module 14's use is the sharpest example of why the deferred/rejected distinction
matters. Without it, every quarter's capability review re-proposes the same orphan.

---

# What It Deliberately Does Not Do

| It does not | Because |
| --- | --- |
| Specify requirements | That is `08-product` |
| Design the architecture | That is `09-technology` |
| Plan delivery | That is `10-execution`, from this module's roadmap |
| Change the economics | It chooses within `06-business`'s constraints, or regresses to it |

---

> **Relationships Principle**
>
> Everything before this module is input. Everything after it is elaboration.
>
> That makes it the one place where being wrong is cheap to fix and being unexamined is
> not.
