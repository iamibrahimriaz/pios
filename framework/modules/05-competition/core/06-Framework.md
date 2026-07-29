---
Title: Framework
Module: 05-competition
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the repeatable method for mapping competition and locating a defensible opening.
Audience:
  - AI Agents
  - Product Managers
  - Researchers
Prerequisites:
  - 04-problem gate passed
  - engine/evidence-policy.md
  - 05-competition/core/03-Core-Principles.md
Outputs:
  - competitor_matrix
  - feature_comparison
  - pricing_comparison
  - gap_analysis
  - positioning
Related Modules:
  - 06-business
  - 07-strategy
Tags:
  - Competition
  - Framework
  - Method
---

# The Contest

---

# Overview

This module answers two questions, and the second one matters more:

1. Who already solves this?
2. **Is there an opening we could hold?**

Most competitive analysis answers only the first, produces a feature comparison table, and
decides nothing. Everyone ships everything eventually; a checklist of capabilities tells
you what the market considers table stakes, not where you could win.

The distinctive move in this module is comparing competitors against the **ranked problems
from module 04** rather than against a feature list. That is what turns a survey into a
decision.

---

# Framework Statement

> A gap you can enter is not the same as a gap you can hold.
>
> Find the opening, then ask what stops the incumbent closing it in six months.

---

# The Six Moves

```
Ranked Problems (04) + Market Definition (02) + Segments (03)
   ↓
1. Enumerate  — find everyone who competes, including what is not a product
   ↓
2. Classify   — direct, indirect, substitute, status quo, non-consumption
   ↓
3. Test       — score each against the ranked problems
   ↓
4. Price      — capture pricing, or mark it unavailable
   ↓
5. Locate     — find the gap, and test whether it can be held
   ↓
6. Position   — one sentence a competitor could not also claim
   ↓
Competitive Analysis → 06-business, 07-strategy
```

---

# Move 1 — Enumerate

Find everyone who competes for this problem. Minimum five.

Search across all five categories — a list containing only direct competitors has missed
the ones that usually win:

| Where to look | What it yields |
| --- | --- |
| Category search using domain vocabulary from module 02 | Direct competitors |
| Adjacent categories | Indirect competitors |
| `current_workflow` from module 03 | The status quo — the real incumbent |
| Review sites, "alternatives to" pages | Products users actually compare |
| Forums where the problem is discussed | Substitutes and homemade solutions |
| Job postings mentioning tools | What organizations actually run |

Two categories are systematically forgotten and both belong on the list:

- **The status quo.** Whatever they do today — paper, a spreadsheet, an assistant, a
  habit. It is free, already installed, fully trusted, and requires no change. It is
  usually the strongest competitor in the market.
- **Non-consumption.** People who have the problem and have chosen nothing. If most of the
  segment is here, the competition is inertia rather than any product — which changes the
  entire strategy.

**Produces:** raw `competitor_matrix`

---

# Move 2 — Classify

Sort each competitor by type.

| Type | Solves | For |
| --- | --- | --- |
| Direct | The same problem | The same segment |
| Indirect | The same problem, or an adjacent one | A different segment |
| Substitute | The problem, by a different mechanism entirely | Anyone |
| Status quo | Partially, through habit and effort | Everyone |
| Non-consumption | Not at all | — |

The classification matters because each type is displaced differently. A direct competitor
is displaced by being better. The status quo is displaced by being worth the disruption —
a much higher bar, and the one most products fail.

**Produces:** classified `competitor_matrix`

---

# Move 3 — Test

**The central move of this module.**

Take the ranked problems from module 04 and score every competitor against them.

| Problem | Rank | C1 | C2 | Status quo | Us |
| --- | --- | --- | --- | --- | --- |
| P1 | 1 | partly | not | partly | — |

Scoring:

| | Meaning |
| --- | --- |
| **well** | Solves it as the user would define solved |
| **partly** | Addresses it, with meaningful residual pain |
| **not** | Does not address it |

Then answer two questions:

1. **Who solves P1 best today?** Including the status quo, if that is the honest answer.
2. **Which ranked problems does nobody solve well?** That is where the opening is, if
   there is one.

This table is what makes the analysis decide something. A feature comparison tells you
what exists. A problem-coverage table tells you where the market is failing the person you
chose to serve.

**Produces:** `feature_comparison` (table stakes) and the coverage assessment

---

# Move 4 — Price

Capture pricing for every competitor, or mark it explicitly unavailable.

Never estimate silently. `"Around $50/month"` with no source imports a guess into module
06's revenue model, where it becomes a business case.

| Capture | Record |
| --- | --- |
| Public pricing page | Figure, what is included, **and the date accessed** |
| Enterprise "contact us" | Mark unavailable; note the signal — it implies a sales motion and a price floor |
| Free product | Record how it is funded; that determines what it will do next |

Then read what pricing reveals. A product at ten times the price of another is not
competing for the same buyer, whatever its feature list says. The price tells you who it
was built for.

**Produces:** `pricing_comparison`

---

# Move 5 — Locate

Find the gap — then test whether it can be held.

**Finding it** comes from Move 3: which ranked problem does nobody solve well, for the
segment chosen in module 03?

**Holding it** is the harder question, and the one usually skipped:

> If this works, what stops the incumbent shipping it in six months?

| Answer | Defensibility |
| --- | --- |
| Nothing | Not defensible — a feature, not a company |
| It conflicts with their business model | Strong — they would cannibalize themselves |
| It requires data they do not have | Strong while it lasts |
| It requires a different sales motion | Moderate — they can build it, but not sell it |
| Their existing customers would object | Moderate |
| We would simply be faster | Weak, but sometimes sufficient |

**"Not defensible" is a legitimate finding and must be stated.** Many good businesses start
without a moat. But it must be a known condition carried into module 07, not something
discovered after launch.

**Produces:** `gap_analysis`

---

# Move 6 — Position

One sentence:

> For «segment» who «need», «product» is a «category» that «benefit», unlike
> «alternative», which «limitation».

**The test: could the leading competitor make the same claim?**

If yes, it is not positioning — it is a description of the category. Rewrite until it is
something only this product could say.

Also state whether the product enters an **existing category** or creates a **new** one:

| | Cost |
| --- | --- |
| Existing category | Competing on comparison — buyers already know what to compare |
| New category | Paying for education — buyers must first understand why this exists |

Both are valid. The cost differs, and module 11 needs to know which one it is funding.

**Produces:** `positioning`

---

# When This Module Returns to 02-market

`on_fail: return to 02-market`. Common triggers:

| Trigger | What it means |
| --- | --- |
| Competitors found do not serve the defined market | The boundary is wrong |
| No competitors and no status quo can be identified | The market may be theoretical |
| Every competitor serves a different segment | The market and segment disagree |
| The gap found sits outside the market boundary | Module 02 or 03 needs revisiting |

---

# Common Failures

| Failure | What it looks like | Cost |
| --- | --- | --- |
| Feature-checklist analysis | A large tick table, no conclusion | Decides nothing |
| Status quo omitted | Only funded products listed | The strongest competitor is invisible |
| Non-consumption ignored | Assumes everyone uses something | The real barrier is inertia, unaddressed |
| Silent price estimate | "Around $50" with no source | A guess becomes module 06's revenue model |
| Gap without defensibility | An opening found, never tested | Builds a feature an incumbent copies |
| Positioning a competitor could claim | "The easiest way to..." | No differentiation |
| Comparing on features, not problems | Table stakes mistaken for strategy | Parity thinking |

---

# Self Assessment

- Did I include the status quo, and take it seriously?
- Did I consider people who have the problem and use nothing?
- Did I score competitors against ranked problems, not just features?
- Is every price sourced and dated, or explicitly marked unavailable?
- Did I ask what stops an incumbent closing this gap?
- Could a competitor make my positioning claim?
- Did I search for who tried this and stopped?

---

> **Framework Principle**
>
> The competitor that beats most new products is not a company.
>
> It is what the user already does, for free, without changing anything.
