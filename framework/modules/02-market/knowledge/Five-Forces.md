---
Title: Five Forces
Module: 02-market
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Use structural analysis to explain why a market behaves as it does, without duplicating module 05.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 02-market/knowledge/Market-Definition.md
Outputs:
  - Structural context for market_gaps
Related Modules:
  - 05-competition
  - 06-business
Tags:
  - Market
  - Structure
  - Method
---

# Five Forces

---

# What It Is

A structural analysis of a market: five pressures that determine whether anyone in it can earn a
durable margin.

| Force | The question here |
| --- | --- |
| **Buyer power** | Can customers dictate price or terms? Who signs, and do they have alternatives? |
| **Supplier power** | Does anyone control an input you need — a data source, a model provider, an integration? |
| **Substitutes** | What do people use instead, including spreadsheets, staff and doing nothing? |
| **New entrants** | How cheap is it to arrive? What actually stops the next team? |
| **Rivalry** | Do incumbents compete on price, on features, or not much at all? |

Its use in this framework is explanatory. It answers *why* the market looks the way Frames 1–5
found it — most usefully, why a gap in Frame 5 persists.

---

# When It Applies

As reference during Frame 5 (Gap), and as input to `06-business` on whether margin is defensible.
It is not a required output of this module.

---

# How to Apply It Here

**Run it to explain a gap, not to produce a matrix.** One or two forces usually account for a
persistent gap; those are the ones worth writing. A full five-force table where three cells say
"moderate" has recorded nothing.

**Take supplier power seriously in AI products.** A product built on a single model provider has a
supplier who sets prices, changes terms and deprecates versions. That is a structural exposure —
`14-ai-systems` costs it, `09-technology` pins the version, and this is where it is first named.

**Count doing nothing as a substitute.** In most markets the leading alternative is the status quo,
and it is free. `04-problem` measures its cost; naming it here prevents the market being described
as if the only options were vendors.

**Ask who signs versus who suffers.** Where the buyer is not the user, buyer power runs through
someone who does not feel the problem. That single fact reshapes `08-product`, `06-business` and
`11-growth`, and it is easiest to see from here.

**Do not name competitors.** Structure here, companies in `05-competition`.

---

# Where It Misleads

**It describes established markets better than emerging ones.** In a market that barely exists,
rivalry and entrant barriers are indeterminate — and "low barriers to entry" is nearly always the
honest answer for software, which makes it uninformative.

**It is a snapshot presented as a structure.** Cheap models, new regulation, or one acquisition can
move two forces at once. Pair it with `Trends.md` or it reads as more permanent than it is.

**Every cell filled in is treated as analysis complete.** A five-cell summary with no consequence
attached changes no decision. If a force does not alter scope, price, or the choice of segment,
leave it out.

**It says nothing about whether the problem is worth solving.** A structurally attractive market
full of people who are content is not an opportunity. `04-problem` holds that answer.

---

# Related

| | |
| --- | --- |
| `Market-Gaps.md` | What this is most useful for explaining |
| `PESTEL.md` | The external environment, by contrast with structure |
| `05-competition` | Where named rivals are analyzed |
| `06-business` | Where margin defensibility is decided |

---

> **Concept Note**
>
> Use it to answer one question: why has this stayed as it is?
>
> A completed matrix is not a finding. An explained gap is.
