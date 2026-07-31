---
Title: Related Modules
Module: 11-growth
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show how the Growth module connects to the framework, and where the Milestone Zero chain ends.
Audience:
  - Product Managers
  - Founders
  - Marketers
Prerequisites:
  - 11-growth/core/00-Purpose.md
Outputs:
  - Understanding of the growth stage's position in the chain
Related Modules:
  - 03-user
  - 06-business
  - 12-metrics
Tags:
  - Growth
  - Relationships
  - Learn
---

# Related Modules

---

# Overview

This module consumes from further back in the framework than most. Its two most important
inputs — switching cost and the payer distinction — were established in modules 03 and
06, and both are routinely forgotten by the time anyone plans acquisition.

---

# What It Takes In

| Input | From | Used for |
| --- | --- | --- |
| `go_to_market` | `06-business` | The starting point this module elaborates |
| The payback ceiling | `06-business` | The second arithmetic check |
| `segments` | `03-user` | Who the channels must reach |
| `switching_cost` | `03-user` | Why conversion will not match borrowed benchmarks |
| `feature_spec` | `08-product` | What the product can actually promise |
| `ux_flows` | `10-execution` | Where time to first value is measured |
| The positioning and status quo profile | `05-competition` | What the message has to displace |

The gate fails back to `06-business`, because an unaffordable acquisition plan is an
economics problem rather than a marketing one.

---

# The Second Arithmetic Check

```
06-business  payback ceiling — what a customer returns in n months
    ↓
11-growth    implied CAC from the channel plan and conversion assumptions
    ↓
  breach → REGRESS to 06-business (price) or 07-strategy (scope)
```

The characteristic absorption here is assuming conversion improves with optimization. It
might. It has not yet, and the check is against what the plan currently implies.

---

# Where the Milestone Zero Chain Ends

```
04-problem     declares the shortfall
07-strategy    makes resolving it binding on the approach
10-execution   sequences it first
11-growth      WITHHOLDS acquisition spend until it resolves
```

This is the fourth and final link. It is also the one with real teeth — the others change
documents; this one changes what gets spent.

---

# The Switching-Cost Connection

One relationship explains most growth surprises:

| Module | Contribution |
| --- | --- |
| `03-user` | Measures what it costs a user to leave their current way |
| `05-competition` | Profiles the status quo, whose switching cost is zero |
| `11-growth` | Discovers that conversion is a function of both |

A conversion assumption that ignores switching cost is **borrowed growth** in its purest
form, and the fix is usually a product change — a migration path, a parallel-running
mode, a narrower entry point — rather than a campaign change.

---

# What It Sends Forward

| Output | Who consumes it | What they do with it |
| --- | --- | --- |
| `growth_loops` | `12-metrics` | What the north star has to express |
| `retention_model` | `12-metrics`, `13-operations` | Leading indicators; expected load over time |
| `acquisition_channels` | `12-metrics` | What gets instrumented |
| `onboarding_strategy` | `10-execution` feedback | Product changes that shorten time to first value |
| `expansion_paths` | `06-business` feedback | Revenue paths beyond the first purchase |

Module 12's dependency is the tight one. A north star metric must express the value the
growth model claims to compound — so a funnel honestly labeled produces a very different
north star from a loop, and mislabeling here produces a metric that measures the wrong
thing for a year.

---

# What It Deliberately Does Not Do

| It does not | Because |
| --- | --- |
| Set the price | `06-business` did; this module tests against it |
| Define metrics | `12-metrics` does, from this module's model |
| Design onboarding | `10-execution` did; this module measures it |
| Execute campaigns | Outside the framework's scope |

---

> **Relationships Principle**
>
> This module inherits two things nobody remembers by the time they plan growth: what it
> costs a user to switch, and who actually signs.
>
> Almost every growth surprise is one of those two, arriving late.
