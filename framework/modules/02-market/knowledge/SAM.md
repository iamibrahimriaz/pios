---
Title: SAM
Module: 02-market
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define serviceable addressable market and the constraints that reduce TAM to it.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 02-market/knowledge/TAM.md
Outputs:
  - SAM within tam_sam_som
Related Modules:
  - 06-business
  - 11-growth
Tags:
  - Market
  - SAM
  - Concept
---

# SAM

---

# What It Is

**Serviceable addressable market** — the portion of TAM this product could legally and practically
serve, given the jurisdiction, the chosen segment, the delivery model and the price.

SAM is where the reductions are recorded. TAM says the need exists; SAM says how much of it is
actually available to this product as conceived.

Each step from TAM to SAM must name its **constraint**:

| Constraint | Effect |
| --- | --- |
| Regulation | Excludes entities that may not buy, or that require certification to sell to |
| Geography | Only the named jurisdiction |
| Segment | Only the segment the idea addresses |
| Channel | Only those reachable through an existing route |
| Price | Only those for whom the price is plausible |
| Technical | Only those with the prerequisite in place — connectivity, an existing system, a data source |

---

# When It Applies

In Frame 3 (Size), second of the three, after TAM and downstream of Frame 2's regulatory findings.

---

# How to Apply It Here

**Write it as a reduction, not a new calculation.**

```
TAM
  − «constraint»  → «figure»
  − «constraint»  → «figure»
  = SAM
```

Each line names the constraint and the resulting figure. A reader can then dispute one step
instead of the whole number.

**Apply Frame 2 first.** Regulatory exclusion is the largest and most frequently omitted
reduction, and it is the one that can end the module.

**Include the technical prerequisite.** If the product needs an existing system to integrate with,
those without it are not serviceable — however much they need the outcome. This constraint tends
to be invisible until `09-technology`, which is far too late for it to change the sizing.

**Keep SAM consistent with the chosen segment.** If `Customer-Segments.md` names one target
segment, SAM is that segment. A SAM covering all segments is TAM with a different label.

---

# Where It Misleads

**SAM is most often TAM with a small haircut applied for appearance.** If SAM is 80–90% of TAM,
the constraints have not been taken seriously — geography, regulation, price and channel rarely
combine to remove only a tenth of a market.

**"Serviceable" gets read as "eventually serviceable".** A segment reachable after a certification
that costs eighteen months is not in SAM today. Put it in `scope_boundaries` as a later phase, with
the cost and time from Frame 2 attached.

**The channel constraint is skipped because channels are `11-growth`'s subject.** They are — but if
no route to a group exists, they are not serviceable now, and sizing them as if they were pushes
an unsupportable number into `06-business`.

**A single unsourced percentage can carry the whole reduction.** "We estimate 30% are reachable"
tagged `[assumption]` makes SAM an assumption. That is honest, and it should be visible rather
than buried in the arithmetic.

---

# Related

| | |
| --- | --- |
| `TAM.md` | The starting figure |
| `SOM.md` | The winnable share of SAM |
| `Customer-Segments.md` | Which segment SAM covers |
| `11-growth` | Whether a channel to SAM actually exists |

---

> **Concept Note**
>
> SAM is a list of subtractions, each with a named cause.
>
> If it is TAM minus a round number, no constraint was examined.
