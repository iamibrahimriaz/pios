---
Title: Purpose
Module: 02-market
Section: core
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define why the Market module exists and what it establishes for the rest of the run.
Audience:
  - AI Agents
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - core/00-Purpose.md
  - 01-idea gate passed
Outputs:
  - Shared understanding of what this module establishes
Related Modules:
  - 01-idea
  - 05-competition
  - 06-business
Tags:
  - Market
  - Purpose
  - Foundation
---

# Purpose

---

# Overview

Module 01 established what is being proposed.

This module establishes whether there is a place in the world for it to exist — a
definable market, of a knowable size, governed by identifiable rules, moving in a
particular direction.

The question is not "is this a good idea?" That comes later, and it comes from several
modules combined. The question here is narrower and more mechanical:

> What is the container this product would live inside, and what shape is it?

---

# Purpose Statement

> Draw the boundary of the market, measure what is inside it, and identify the rules
> that govern who may participate.

---

# Why This Module Exists

An idea without a market is a hobby.

But the more common failure is subtler than having no market. It is having an
**undefined** market — one described by adjective rather than boundary, sized by a
number lifted from a report that measured something else.

That failure is invisible downstream. Module 05 will find competitors inside the wrong
boundary. Module 06 will price against the wrong population. Module 07 will commit to a
strategy for a market that was never actually described.

None of those modules will detect the error, because none of them re-examines the
boundary. They inherit it.

This module exists to make sure the boundary is worth inheriting.

---

# Core Objectives

- Define the market by boundary, so borderline cases can be ruled on.
- Establish the regulatory regime before assuming who can be served.
- Size the market with visible arithmetic that a reader can disagree with.
- Identify which way the market is moving, including the ways that are unfavorable.
- Find where the market is underserved, and why it has stayed that way.

---

# What AI Should Learn Here

- A market size means nothing without the boundary it was measured inside.
- Regulation is not background; it determines who may participate at all.
- A number with no derivation cannot be challenged, and cannot be trusted.
- Every market has forces pushing against it. An analysis without one is incomplete.
- A gap with no explanation for its persistence is usually not a gap.

---

# Scope

**This module covers**

- Market definition and boundary
- Regulatory landscape for the named jurisdiction
- TAM, SAM and SOM with derivations
- Trends and their direction
- Market-level gaps and why they persist
- Market structure and maturity

**This module does not cover**

| Not here | Belongs to |
| --- | --- |
| Naming and comparing competitors | `05-competition` |
| Segment prioritization and personas | `03-user` |
| Problem validation | `04-problem` |
| Pricing strategy and willingness to pay | `06-business` |
| Compliance implementation | `09-technology` |

The distinction matters. This module establishes the container; later modules populate it.
Work done here that belongs elsewhere is done without the context those modules will have,
and has to be redone.

---

# Position in the Run

```
01-idea → [ 02-market ] → 03-user → 04-problem → 05-competition → 06-business
```

Runs first in the research stage. `03-user` may run alongside it. `05-competition`
cannot start until this module has passed its gate.

---

# What This Module Hands Forward

| Output | Consumed by | Used for |
| --- | --- | --- |
| `market_definition` | 03, 05, 06 | Bounding segments, competitors and revenue |
| `tam_sam_som` | 06 | Revenue modeling |
| `trends` | 05, 07 | Positioning and timing |
| `regulatory_landscape` | 09 | Structural constraints on data and architecture |
| `market_gaps` | 05, 07 | Where the opening might be |

The handoff to `09-technology` is the one most often under-served. It is consumed seven
modules later, by a reader who will not return to this document. Compliance findings must
be written as obligations an engineer can act on, not as regime names.

---

# Success Criteria

This module has succeeded when:

- A practitioner in the domain would recognize the category name.
- The boundary decides borderline cases without further judgment.
- Every figure shows arithmetic a reader could argue with.
- The regulatory section reads as a specification, not a list of acronyms.
- At least one finding makes the idea look harder than it did before.
- A reader can tell exactly what is established and what is believed.

---

# Self Assessment

- Can I state the market as a boundary rather than an adjective?
- Did I check regulation before I reached for a number?
- Can someone challenge my sizing, or only believe it?
- Did I find something that argues against this market?
- Have I stayed inside this module's scope?

---

> **Purpose Principle**
>
> Four modules will inherit the boundary drawn here, and none of them will question it.
>
> Draw it as though it will never be checked again — because it will not be.
