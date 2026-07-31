---
Title: Related Modules
Module: 14-ai-systems
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show how the AI Systems module connects to the framework and what it checks against.
Audience:
  - Product Managers
  - Founders
  - Engineers
Prerequisites:
  - 14-ai-systems/core/00-Purpose.md
Outputs:
  - Understanding of the AI stage's position in the chain
Related Modules:
  - 08-product
  - 09-technology
  - 13-operations
Tags:
  - AI
  - Relationships
  - Learn
---

# Related Modules

---

# Overview

This module is last, and its position is the point. Everything it needs in order to
evaluate a capability honestly was produced by the thirteen modules before it.

---

# What It Takes In

| Input | From | Used for |
| --- | --- | --- |
| `feature_spec` | `08-product` | Whether a capability has a requirement, or is an orphan |
| `data_model` | `09-technology` | What data exists |
| The regulated column list | `09-technology` | Whether regulated fields would enter a model input |
| `jobs_to_be_done` | `03-user` | Which job the capability serves |
| `non_goals` | `07-strategy` | What must not be proposed |
| `ranked_problems` | `04-problem` | The trace every capability needs |
| Revenue per user | `06-business` | The cost ratio's denominator |

The gate fails back to `08-product`, because a capability with no requirement is a
specification question rather than an AI one.

---

# The Fourth Regulated Field Check

```
09-technology   produces the regulated column list
12-metrics      no regulated field in an event property
13-operations   the review, with a cadence and an owner
14-ai-systems   no regulated field in a MODEL INPUT     ← here
```

The framework treats a model prompt and an analytics event as the same class of exposure.
Both leave your systems, both go to a third party, both frequently land in another
jurisdiction under a retention policy you did not choose.

Two extra questions belong to this module alone: whether the provider trains on your data
— **contracted, not assumed** — and where the inference endpoint physically is, because
residency obligations from module 02 apply to it.

---

# The Cost Ratio

```
14-ai-systems  cost/operation × operations/user ÷ revenue/user
    ↓
09-technology  §12 infrastructure cost check
13-operations  §11 true cost to serve
```

This module does not run an arithmetic check of its own; it supplies a line to two others.
That makes an inaccurate cost figure here a corruption of both — and model pricing is the
most volatile input in the framework, which is why version-and-date citation is required.

---

# Where Non-Goals Bind

Module 07's non-goals apply directly here, and the deferred-versus-rejected distinction
matters more in this module than anywhere else. A capability rejected but filed as
deferred returns every quarter as an obvious omission, because AI capability lists are
reviewed more often than any other part of a product plan.

The worked example records a code-suggestion capability as **rejected, not deferred**, for
exactly this reason.

---

# What It Sends Forward

| Output | Who consumes it | What they do with it |
| --- | --- | --- |
| Per-instance acceptance criteria | `08-product` | Conventional requirements — editable, source shown, never writes without approval |
| Visibility mechanisms | `08-product`, `10-execution` | Requirements and flow states |
| Inference cost | `09-technology`, `13-operations` | Two cost checks |
| `failure_modes` | `13-operations` | Runbooks and alerts |
| The non-AI fallback | `08-product` | A requirement, not a contingency |
| `evaluation_plan` | The operator | The ship gate |

The first row is where most of the real safety lives. A statistical bar of 95% is one
requirement; "always editable, always shows its source, never writes without approval,
numbers and drug names always highlighted" is four, and they are the ones that protect a
user on the day the model is wrong.

---

# The Transition Relationship

When a capability is kept as a triggered candidate rather than rejected, it creates a
forward dependency:

```
07-strategy    sets the transition trigger
10-execution   the manual delivery that generates the data
14-ai-systems  the capability, when data and rights both exist
13-operations  the cost line that the transition replaces
```

In the worked example this loop is the whole economic case for the transition: inference
cost replaces the human transcription labor that module 13 identified as the dominant
cost, and module 07's trigger at fifteen practices was set from that arithmetic rather
than arbitrarily.

---

# What It Deliberately Does Not Do

| It does not | Because |
| --- | --- |
| Specify the product | `08-product` did; this module hands it requirements |
| Design the architecture | `09-technology` did |
| Set the price | `06-business` did |
| Train or tune anything | This is a decision module, not an implementation one |

---

> **Relationships Principle**
>
> This module is last so that its proposals can be checked against thirteen modules of
> evidence rather than against enthusiasm.
>
> That ordering is why its most common correct output is a rejection.
