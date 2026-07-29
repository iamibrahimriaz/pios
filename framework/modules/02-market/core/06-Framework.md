---
Title: Framework
Module: 02-market
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the repeatable method for bounding, sizing and characterizing a market.
Audience:
  - AI Agents
  - Product Managers
  - Researchers
Prerequisites:
  - 01-idea gate passed
  - engine/evidence-policy.md
  - 02-market/core/03-Core-Principles.md
Outputs:
  - market_definition
  - tam_sam_som
  - trends
  - regulatory_landscape
  - market_gaps
Related Modules:
  - 05-competition
  - 06-business
  - 09-technology
Tags:
  - Market
  - Framework
  - Method
---

# The Market Framework

---

# Overview

This module answers one question: **is there a market here, and what shape is it?**

The failure mode is not producing a wrong number. It is producing a plausible number for
a market that was never properly defined — which is undetectable downstream, because
every later module will use the figure without questioning the boundary it came from.

Define the boundary first. Everything else follows from it.

---

# Framework Statement

> A market size is only as meaningful as the boundary it was measured inside.
>
> Draw the boundary before reaching for a number.

---

# The Five Frames

```
Idea Brief (from 01-idea)
   ↓
1. Bound      — where the market starts and stops
   ↓
2. Regulate   — what the law permits and requires
   ↓          (may return to Bound)
3. Size       — TAM, SAM, SOM
   ↓
4. Trend      — which way it is moving
   ↓
5. Gap        — what is underserved, and why it stayed that way
   ↓
Market Analysis → 05-competition, 06-business
```

---

# Frame 1 — Bound

Define the market by **boundary**, not by adjective.

"The healthcare software market" is an adjective. It cannot be measured, because nobody
can say what is inside it.

A boundary states three things:

| | Example |
| --- | --- |
| **Who** | solo and two-doctor general practices |
| **What need** | clinical documentation during consultations |
| **Where** | «named jurisdiction» |

**The boundary test:** take a borderline company or product and rule it in or out, with
the reason. If you cannot, the boundary is not drawn.

Then record what is explicitly **outside** the market and why. Exclusions are as
informative as inclusions, and they prevent the market quietly expanding in module 05
when a competitor is found that does not really compete.

Finally, find the **category name** — what practitioners in the domain call this. If
the category has no name, record that. A market nobody has named may be a market nobody
has funded.

**Produces:** `market_definition`

---

# Frame 2 — Regulate

This frame runs **before** sizing, deliberately.

Regulation determines who may participate at all. A market of 100,000 practices where
only licensed entities may sell is not a market of 100,000 — and sizing it before
checking would produce a figure that is wrong by an order of magnitude.

Take the jurisdiction from `idea_brief`. Never infer it. If it is unset, the run should
not have reached this module.

Establish:

| | |
| --- | --- |
| **Which regimes apply** | and what triggers each one |
| **What they require** | concrete obligations, not regime names |
| **Barriers to entry** | certification, licensing, audit — with cost and time to clear |
| **Direction of travel** | tightening, stable, or loosening |

Then ask the question that can end this module early:

> **Does regulation exclude a segment named in the idea brief?**

If yes, this returns to `01-idea`. Better to discover it here than in module 09, after
four modules of research on a segment that cannot be legally served.

Everything found here reappears in module 09 as structural constraints on the data model
and architecture. Write it so that a future reader building the schema can act on it.

**Produces:** `regulatory_landscape`

---

# Frame 3 — Size

Produce TAM, SAM and SOM — each with its derivation shown.

| | Meaning |
| --- | --- |
| **TAM** | Everyone who has this need, ignoring reachability |
| **SAM** | The portion you could legally and practically serve |
| **SOM** | What you could realistically win in year one |

**Prefer bottom-up.**

```
unit count × realistic price × reachable share = figure
```

A top-down figure lifted from a market report is almost always measuring a *different*
market than the one bounded in Frame 1. Using it imports someone else's boundary without
noticing.

Where both methods are available, run both. If they disagree materially, **that
disagreement is a finding** — record it and say which is more trustworthy here. Do not
quietly adopt the more attractive number.

Every input carries a tag. An unsourced input makes the whole figure an assumption,
regardless of how precise the arithmetic looks.

**Produces:** `tam_sam_som`

---

# Frame 4 — Trend

Minimum three trends. Each needs a **direction** and **evidence** — a trend without a
direction is an observation.

Cover:

| Type | Question |
| --- | --- |
| Demand | Is the need growing or shrinking? |
| Supply | Are new entrants arriving or leaving? |
| Technology | What has recently become possible or cheap? |
| Regulatory | What is changing in the rules? |
| Behavioral | What are buyers doing differently? |

Then find **at least one trend that works against the idea.**

If none was found, the research was selective rather than thorough. Every market has
forces pushing both ways, and the ones pushing against are the ones worth knowing early.

Close with a timing assessment: is this early, on time, or late — and why? Being early is
a different risk from being late, and both are survivable if named.

**Produces:** `trends`

---

# Frame 5 — Gap

Identify where the market is underserved.

For each gap, the critical column is **why it persists**:

| Reason a gap persists | What it implies |
| --- | --- |
| Regulation | The gap is real but expensive to enter |
| Economics | The segment may be unprofitable to serve |
| Distribution | The customers are hard to reach |
| Data access | Someone else controls the necessary input |
| Incentives | Nobody in the value chain benefits from closing it |
| **No reason found** | Be suspicious of the gap, not excited by it |

A gap with no explanation is usually not a gap — it is a search that stopped early.

Keep this frame at market level. Naming individual competitors and comparing their
features belongs to `05-competition`. Doing it here duplicates that work and does it
worse, without the segment and problem context module 05 will have.

**Produces:** `market_gaps`

---

# When This Module Returns to 01-idea

`on_fail: return to 01-idea`. The common triggers:

| Trigger | What it means |
| --- | --- |
| The market cannot be bounded | The idea was never specific enough |
| Regulation excludes the named segment | The context in the brief is not viable |
| No definable category exists | The idea may not address a recognized need |
| Sizing is impossible in every method | The market may not be identifiable |

Returning is the framework working. Proceeding with an undefined market is the framework
failing quietly.

---

# Common Failures

| Failure | What it looks like | Cost |
| --- | --- | --- |
| Adjective market | "The healthcare software market" | Every figure downstream is meaningless |
| Borrowed sizing | A report's TAM adopted without checking its boundary | Sizing a different market than the one being entered |
| Sizing before regulating | A figure that ignores who may legally sell | Wrong by an order of magnitude |
| Selective trends | Every trend supports the idea | The adversarial pass was not run |
| Unexplained gaps | "Nobody serves solo practices" with no reason | The gap is probably imaginary |
| Doing module 05's work | A competitor matrix appears here | Duplicated, and worse than 05 will do it |

---

# Self Assessment

- Could a reader use my boundary to rule a borderline company in or out?
- Did I check regulation before I reached for a number?
- Does every figure show its derivation?
- Did I find a trend that argues against this idea?
- Does every gap explain why it persists?
- Have I stayed out of module 05's territory?

If any answer is **No**, the framework has not been applied.

---

> **Framework Principle**
>
> Anyone can find a large number and attach it to an idea.
>
> The work is defining the boundary that makes a number mean something.
