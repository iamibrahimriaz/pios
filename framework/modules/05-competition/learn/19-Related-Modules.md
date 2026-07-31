---
Title: Related Modules
Module: 05-competition
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show how the Competition module connects to the framework and what each downstream module inherits.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 05-competition/core/00-Purpose.md
Outputs:
  - Understanding of the competition stage's position in the chain
Related Modules:
  - 02-market
  - 06-business
  - 07-strategy
Tags:
  - Competition
  - Relationships
  - Learn
---

# Related Modules

---

# Overview

This module consumes from three upstream modules and is the last research stage before
the framework begins committing. Its gap analysis is what module 07 aims at.

---

# What It Takes In

| Input | From | Used for |
| --- | --- | --- |
| `market_definition` | `02-market` | The boundary that decides who counts as a competitor |
| `market_gaps` | `02-market` | Candidate openings, to be tested rather than trusted |
| `trends` | `02-market` | Direction — who is moving toward the gap |
| `segments` | `03-user` | Whose alternatives are being compared |
| `ranked_problems` | `04-problem` | The dimensions the comparison should be scored on |

The last row is the one most often ignored, and it is the defense against a matrix
scored on rows you win. The comparison dimensions should come from module 04's ranking,
not from your feature list.

The gate fails back to `02-market`, because an unassemblable competitor set almost
always means an unbounded market.

---

# What It Sends Forward

| Output | Who consumes it | What they do with it |
| --- | --- | --- |
| `pricing_comparison` | `06-business` | The price is justified against these figures |
| `gap_analysis` | `07-strategy` | The opening the chosen approach aims at |
| `positioning` | `06-business`, `11-growth` | Who the payer compares against; what the message must overcome |
| `competitor_matrix` | `07-strategy`, `08-product` | What the MVP has to beat, and on what |
| The status quo profile | `07-strategy`, `11-growth` | The adoption barrier, paired with module 03's switching cost |

---

# The Status Quo Pairing

One relationship in the framework matters more than its visibility suggests:

```
03-user       switching_cost — what it costs to leave the current way
    ↓
05-competition  status quo profiled as a competitor with zero switching cost
    ↓
07-strategy   the approach must beat the status quo by more than that cost
    ↓
11-growth     conversion assumptions collide with the same arithmetic
```

Module 11 names the failure that occurs when this pairing is ignored: **borrowed
growth** — conversion rates taken from a market where the switching cost was different.

---

# Where the Gap Analysis Binds

Module 07's gate requires the chosen approach to be justified against the ranked
problems, and its solution comparison weighs each option against the opening found
here. A gap that was not classified — nobody has, nobody can, nobody should — produces
a strategy aimed at something that may not be an opening at all.

That is why the reasoning clause is in this module's gate rather than being left to
module 07 to work out. By the time module 07 has an option list, the gap is an
assumption in all of them.

---

# What It Deliberately Does Not Do

| It does not | Because |
| --- | --- |
| Set a price | That is `06-business`, using this comparison |
| Choose an approach | That is `07-strategy` |
| Specify features | That is `08-product`, and a matrix is not a specification |
| Conclude the market is enterable | No module renders that verdict alone |

The third row is worth stating plainly. A competitor matrix converted directly into a
requirement list produces a product defined entirely by what other people built —
which is the most reliable way to arrive second at everything.

---

> **Relationships Principle**
>
> The comparison dimensions should come from module 04's ranked problems, not from
> your own roadmap.
>
> That single connection is what separates a competitive analysis from a self-portrait
> with competitors in the background.
