---
Title: Related Modules
Module: 02-market
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show how the Market module connects to the rest of the framework, and trace the obligation chain it starts.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 02-market/core/00-Purpose.md
Outputs:
  - Understanding of the market stage's position in the chain
Related Modules:
  - 01-idea
  - 09-technology
  - 13-operations
Tags:
  - Market
  - Relationships
  - Learn
---

# Related Modules

---

# Overview

This module has one upstream dependency and an unusually long downstream reach. Its
regulatory output is consulted by four later modules, which is more than any other
single artifact in the framework.

---

# What It Takes In

| Input | From | What it is used for |
| --- | --- | --- |
| `idea_brief` | `01-idea` | The premise the market is defined around |
| `scope_boundaries` | `01-idea` | The starting point for the boundary this module sharpens |

When the gate fails — most often on "market defined by boundary, not by adjective" —
the run returns to `01-idea`. That path exists because an unbounded market is nearly
always an unbounded idea, and fixing it here would mean inventing a boundary the
operator never stated.

---

# What It Sends Forward

| Output | Who consumes it | What they do with it |
| --- | --- | --- |
| `market_definition` | `03-user`, `05-competition` | Who is in scope; who counts as a competitor |
| `tam_sam_som` | `06-business` | The ceiling on the revenue model |
| `trends` | `05-competition`, `07-strategy` | Direction to position against and sequence around |
| `regulatory_landscape` | `09-technology`, and onward | The obligation chain |
| `market_gaps` | `05-competition` | Candidate openings, to be tested rather than trusted |

---

# The Obligation Chain

This is the module's most important relationship and the one most often missed.

```
02-market  Frame 2 finds the obligation, with a jurisdiction and a citation
    ↓
09-technology  builds the mechanism — retention, erasure, audit, residency
    ↓
13-operations  gives it a cadence, a named owner, and evidence produced
```

Two further modules check against the same finding: `12-metrics` verifies that
regulated fields do not appear in event properties, and `14-ai-systems` verifies that
they do not enter a model's input. **The regulated column list is the same list in all
four places** — which only works if this module produced it.

An obligation missed here is not caught later. There is no module whose job is to
notice a rule nobody wrote down.

---

# The Quieter Chain — Timing

The timing verdict travels less visibly and matters more than learners expect:

| Module | Effect of the timing verdict |
| --- | --- |
| `05-competition` | An EARLY market has few competitors for a reason; a LATE one has many with established positions |
| `07-strategy` | Timing weights the solution comparison — an early market rewards optionality, a late one rewards sharpness |
| `11-growth` | An EARLY market frequently has no functioning acquisition channel at all, which is a channel finding rather than a growth failure |

Module 11 is where an unexamined RIGHT verdict does the most damage, because the growth
plan borrows channels from a market state that has not arrived.

---

# What It Deliberately Does Not Do

| It does not | Because |
| --- | --- |
| Analyze competitors | That is `05-competition`, and it needs this boundary first |
| Identify users | That is `03-user` |
| Price anything | That is `06-business` |
| Recommend entry | No module renders that verdict alone |

The last is the important one. A large TAM is not a recommendation, and this module
is careful never to phrase it as one.

---

# Where the Return Paths Point Here

Two modules fail back to this one:

- `03-user` returns to `02-market` when segments cannot be drawn — usually because the
  market was never bounded tightly enough to contain distinguishable groups.
- `05-competition` returns here when the competitor set cannot be assembled, which has
  the same root cause.

Both are the same defect surfacing in different places, and both are why the boundary
criterion sits in this module's gate rather than being left to judgment.

---

> **Relationships Principle**
>
> The market number leaves this module and is used once.
>
> The regulatory finding leaves this module and becomes somebody's Tuesday, every
> quarter, indefinitely. Weight your effort accordingly.
