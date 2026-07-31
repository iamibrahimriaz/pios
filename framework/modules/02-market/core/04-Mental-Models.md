---
Title: Mental Models
Module: 02-market
Section: core
Category: Thinking Framework
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the lenses through which a market should be examined.
Audience:
  - AI Agents
  - Product Managers
  - Researchers
Prerequisites:
  - 02-market/core/03-Core-Principles.md
Outputs:
  - Multi-perspective market analysis
Related Modules:
  - 05-competition
  - 07-strategy
Tags:
  - Market
  - ../constitution/core/04-Mental-Models.md
  - Analysis
---

# Mental Models

---

# Overview

A market looks different depending on where you stand.

Each model below reveals something the others hide. None is sufficient alone, and using
only one is how an analysis becomes confidently one-sided.

---

# Model Statement

> Every market model is a simplification chosen for a purpose.
>
> Know what each one hides before you rely on what it shows.

---

# 1. Boundary Thinking

**Reveals:** what is inside and outside, and therefore what any number means.

The foundational lens. Before any other model applies, the market must have edges.

Ask: could a reader use my definition to rule on a borderline case? If not, every
subsequent model is being applied to fog.

**Hides:** nothing — but it is frequently skipped, because drawing edges is harder than
citing a figure.

---

# 2. Top-Down vs Bottom-Up

**Reveals:** whether a market size is your measurement or someone else's.

| | How it works | Risk |
| --- | --- | --- |
| Top-down | Start from a published total, narrow by percentages | Inherits a boundary you did not draw |
| Bottom-up | Count units, multiply by price and adoption | Depends on your own assumptions being visible |

Bottom-up is preferred because its errors are **visible**. Every assumption sits on the
page where a reader can challenge it. Top-down errors hide inside someone else's
methodology.

Where both are available, run both. Disagreement between them is information.

**Hides:** both hide the question of whether the population is actually reachable —
that comes from `03-user` and `11-growth`.

---

# 3. TAM / SAM / SOM

**Reveals:** the difference between everyone who has the need, everyone you could serve,
and everyone you could realistically win.

| | Question |
| --- | --- |
| TAM | Who has this need at all? |
| SAM | Who could we legally and practically serve? |
| SOM | Who could we win in year one? |

The gap between TAM and SAM is usually regulation, geography, or language. The gap
between SAM and SOM is distribution.

**Hides:** it says nothing about whether those people will pay, or how hard they are to
reach. A large SOM with no channel is not a market you can access.

---

# 4. Five Forces

**Reveals:** structural attractiveness — whether profit is possible here, regardless of
how large the market is.

| Force | Question in this module |
| --- | --- |
| New entrants | How hard is it to start competing? |
| Buyer power | Can buyers dictate price? |
| Supplier power | Does anyone control a necessary input? |
| Substitutes | What else solves this, including doing nothing? |
| Rivalry | How intensely do existing players compete? |

Use it at market level. The competitor-specific version belongs to `05-competition`.

**Hides:** it is a static snapshot. A market can be structurally unattractive and still
be worth entering if it is changing fast — which is what the trend lens is for.

---

# 5. PESTEL

**Reveals:** the external forces acting on the market that no participant controls.

Political, Economic, Social, Technological, Environmental, Legal.

Most useful here for surfacing the **legal** and **political** dimensions early — the
ones that determine who may participate, and that engineering will inherit as
constraints in module 09.

**Hides:** it produces breadth, not depth. A PESTEL scan with six shallow bullets is
worse than two well-evidenced forces.

---

# 6. Direction Over Position

**Reveals:** where the market is going, which usually matters more than where it is.

A shrinking large market is a worse place to start than a growing small one. Position is
a snapshot; direction is the trend line.

Ask: if this market continues moving the way it is moving, what does it look like when
the product ships?

**Hides:** trends reverse. A direction is evidence, not a guarantee — and the trend that
argues against the idea deserves the same weight as the ones that support it.

---

# 7. The Persistence Question

**Reveals:** whether an apparent gap is an opportunity or a trap.

When a market leaves an obvious need unserved, ask why. The answer is one of:

| Reason | Implication |
| --- | --- |
| Regulation | Real gap, expensive to enter |
| Economics | The segment may be unprofitable |
| Distribution | Customers are hard to reach |
| Data access | Someone controls a necessary input |
| Incentives | Nobody in the chain benefits from fixing it |
| No reason found | Search again before believing it |

**Hides:** it can be over-applied. Some gaps genuinely open because something recently
changed — a regulation loosened, a technology became cheap. That is a valid answer, but
it must name the change.

---

# 8. Timing

**Reveals:** whether this is early, on time, or late.

| | Problem to solve |
| --- | --- |
| Early | Education and distribution — nobody is looking for this yet |
| On time | Execution and differentiation |
| Late | Displacement — buyers already have something |

All three are survivable. Only the unnamed one is dangerous, because the wrong strategy
gets chosen for it.

**Hides:** timing is a judgment, not a measurement. Tag it accordingly.

---

# 9. The Inversion

**Reveals:** what a skeptic would say.

Instead of asking "is this market attractive?", ask: **"if this market is a bad place to
build, what would the evidence look like?"** — then go and check whether that evidence
exists.

Searches phrased around an idea return material that supports it. This model is the
correction for that.

**Hides:** nothing. It is the most under-used model in this module, and the one that most
improves the analysis.

---

# Combining Models

| Situation | Model |
| --- | --- |
| Defining what counts as this market | Boundary Thinking |
| Producing a defensible number | Bottom-Up |
| Separating need from reachability | TAM/SAM/SOM |
| Judging whether profit is possible | Five Forces |
| Surfacing legal and political constraints | PESTEL |
| Deciding whether size or growth matters more | Direction Over Position |
| Testing whether a gap is real | The Persistence Question |
| Choosing the right strategy shape | Timing |
| Correcting for confirmation bias | The Inversion |

Apply Boundary Thinking first and The Inversion last. The models in between can run in
any order.

---

# Self Assessment

- Did I draw edges before applying any other model?
- Did I size bottom-up, or inherit a boundary?
- Did I distinguish who has the need from who can be reached?
- Did I ask why the gap persists?
- Did I run the inversion, and did it find anything?

If the inversion found nothing, it was not run honestly.

---

> **Mental Model Principle**
>
> Every model makes a market look simpler than it is.
>
> Use several, and pay most attention to the one that makes the idea look hardest.
