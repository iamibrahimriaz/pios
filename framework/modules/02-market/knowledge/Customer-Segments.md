---
Title: Customer Segments
Module: 02-market
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define what a market-level segment is, and where segmentation stops being this module's job.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 02-market/knowledge/Market-Definition.md
Outputs:
  - Segments within market_definition
Related Modules:
  - 03-user
  - 11-growth
Tags:
  - Market
  - Segments
  - Concept
---

# Customer Segments

---

# What It Is

Divisions of the bounded market into groups that **behave differently as buyers** — different
needs, different constraints, different willingness to pay, or different routes to reach.

A segment is useful when it changes a decision. If two groups would get the same product at the
same price through the same channel, they are one segment with two labels.

| Weak segment | Useful segment |
| --- | --- |
| Small clinics | Single-handed practices with no practice manager — nobody to run a procurement process |
| Enterprise | Trusts where purchase requires an information-governance review |

The second column names the thing that makes the group behave differently. That is what a segment
is for.

---

# When It Applies

In Frame 1 (Bound), as the internal structure of the market definition. `03-user` then does the
work this module cannot: who these people are, what their day looks like, and what they actually
do instead today.

---

# How to Apply It Here

**Segment by a countable attribute.** Size, structure, jurisdiction, regulatory status, buying
process. This module has to be able to *count* each segment in Frame 3, and an attribute that
cannot be counted cannot be sized.

**Keep the number small.** Three or four at most. A market split into nine segments has usually
been split by adjective.

**Say which segment the idea is aimed at, and mark the rest.** SAM in Frame 3 depends on it, and
`06-business` needs to know which segment the pricing addresses.

**Check each segment against Frame 2.** Regulation frequently excludes one segment entirely, and
that is the finding that returns this module to `01-idea`.

**Leave personas alone.** A persona is `03-user`'s output and requires research this module has not
done. A segment invented here and elaborated into a person becomes a fictional user with a name,
which is harder to dislodge than an honest gap.

---

# Where It Misleads

**Segments are usually drawn by firmographics because those are available, not because they
predict behavior.** Company size is a proxy; the thing that actually varies is whether there is
someone whose job it is to buy software. Prefer the mechanism over the proxy where both are
visible.

**A segment can be defined into existence.** "Mid-market practices seeking digital
transformation" contains an intent nobody has measured. Segment on what is true of the
organization, not on what it is presumed to want.

**Serving all segments is the default and it is nearly always wrong.** Undifferentiated
segmentation makes SAM look like TAM, hides the fact that the segments need different products,
and pushes the decision into `07-strategy` with no information attached.

---

# Related

| | |
| --- | --- |
| `Market-Definition.md` | The boundary these divide |
| `SAM.md` | Where the chosen segment becomes a figure |
| `03-user` | Where segments become researched people |
| `11-growth` | Where a segment must be reachable, not just definable |

---

> **Concept Note**
>
> A segment that would receive the same product, at the same price,
> through the same channel is not a segment.
>
> It is a label on a group you have not distinguished.
