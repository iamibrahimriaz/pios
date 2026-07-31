---
Title: Why It Matters
Module: 02-market
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Explain why market work is about boundaries, timing and constraints rather than about producing a large number.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 02-market/core/00-Purpose.md
Outputs:
  - Understanding of why the market stage exists
Related Modules:
  - 01-idea
  - 06-business
  - 13-operations
Tags:
  - Market
  - Sizing
  - Learn
---

# Why It Matters

---

# Overview

Market sizing has a bad reputation, and it deserves most of it. The typical market
slide exists to reassure rather than to inform, and everyone in the room knows the
number was reverse-engineered from the conclusion.

This module exists because the underlying questions are genuinely load-bearing — and
because they are not the sizing question.

---

# The Three Questions That Matter

**Where does this market end?** Not how big it is. Where it stops. A boundary is what
makes every later claim checkable: a competitor is inside or outside it, a segment is
in scope or not, a regulation applies or does not.

**Is the timing right, and why now?** Markets have states. Something that failed five
years ago may work now because a cost fell, a behavior changed, or a rule was
introduced — and something obvious now may be five years late. This is the finding
most often skipped and most often decisive.

**What is legally true here?** Which jurisdiction, which regime, which obligations.
This is the least glamorous output of the module and the one with the longest life.

---

# Why the Boundary Does the Work

An unbounded market cannot be checked, and an unchecked claim cannot be wrong — which
is exactly why unbounded markets are so popular.

Compare:

| Claim | What can be checked |
| --- | --- |
| "The healthcare software market" | Nothing. Every competitor and no competitor is in it |
| "Single-handed general practices in England" | Countable. Competitors, regulations and segments are all determinable |

The second is smaller in every sense, and it is the one you can do work with. The
first cannot be entered, only described.

> Narrowing does not shrink the opportunity. It makes the opportunity addressable —
> which is the only property that matters before launch.

---

# Why the Number Is Weaker Than It Looks

Every market figure is a chain: a population, a fraction of it, a price, a period.
Each link is an estimate, and the errors multiply. A TAM built from four estimates
each accurate within a factor of two is accurate within a factor of sixteen.

This is not an argument against sizing. It is an argument for **showing the chain**.
A number whose derivation is visible can be argued with, adjusted when one input
turns out to be wrong, and used for a sensitivity check. A number that arrives whole
can only be believed or disbelieved.

The framework's requirement follows from this: each of TAM, SAM and SOM is sourced or
explicitly marked as an assumption. Not because the tag makes the number better, but
because it makes the number *usable*.

---

# Why the Regulatory Finding Outlives Everything Else

A market figure is consumed once — by the decision about whether to keep going. A
regulatory constraint is consumed four more times:

```
02-market finds the obligation
   ↓
09-technology builds the mechanism that satisfies it
   ↓
12-metrics checks that regulated fields do not leak into events
   ↓
13-operations gives it a cadence, an owner and evidence
   ↓
14-ai-systems checks that regulated fields do not enter a model
```

This is the framework's **obligation chain**, and this module is where it starts. A
constraint that is not found here has no mechanism, no schedule and no owner — and its
absence is invisible until an audit, a breach, or a customer's procurement team asks.

That asymmetry is why the module's gate names the jurisdiction explicitly. "The
regulatory context" is not an answer. A country is.

---

# What Skipping This Stage Costs

| Skipped | Surfaces as |
| --- | --- |
| The boundary | Module 05 cannot decide who is a competitor; module 07 has no natural cut line |
| Timing | A product built for a market state that ended, or has not yet arrived |
| Regulation | An obligation discovered after launch, when it is a legal event rather than a design decision |
| The sizing chain | A number that cannot be corrected when one input proves wrong |

Only the last of these is cheap to fix later.

---

# What This Module Does Not Do

It does not decide whether the market is attractive. It does not compare you to
competitors — that is module 05. It does not price anything — that is module 06.

It establishes the field of play, and it is unusual among market exercises in
declining to render a verdict on it.

---

> **Why It Matters Principle**
>
> A large market that nobody has bounded is not an opportunity. It is a sentence.
>
> This module exists to replace that sentence with a boundary, a timing claim, and a
> list of the rules — because those three things are what every module after it
> actually consumes.
