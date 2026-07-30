---
Title: User Segments
Module: 03-user
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the behavioral test for a segment and how one is chosen defensibly.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 03-user/core/06-Framework.md
Outputs:
  - segments
Related Modules:
  - 02-market
  - 07-strategy
Tags:
  - User
  - Segments
  - Concept
---

# User Segments

---

# What It Is

Groups within the market whose members would **buy, use, or reject the product for different
reasons.** That is the entire test.

Where `02-market` segments to make the market countable, this module segments to make it
*buildable* — the split has to change what gets designed, not just what gets tallied.

| Not a segment | A segment |
| --- | --- |
| Practices in the north vs the south | Solo practices vs practices with shared records |
| Users aged 30–40 vs 40–50 | Those who own the budget vs those who must request it |
| Large vs small, with no behavioral difference | Those replacing a system vs those with none |

A demographic split that changes no behavior produces the appearance of segmentation without its
value — and two personas who turn out to be the same person.

---

# When It Applies

In Move 1 (Divide) and Move 2 (Choose), before any persona exists. If no coherent segment can be
found, or every segment behaves identically, the module returns to `02-market`: the boundary was
drawn around a non-market.

---

# How to Apply It Here

**Record four columns per segment, each tagged.** Approximate size, pain intensity, ability to pay,
and how they could be reached. A segment with an untagged pain-intensity claim is a guess in a
table.

**Choose against the criteria, not against preference.** Pain intensity, ability to pay,
reachability, speed to first customer. The failure this guards against is choosing the segment the
research happened to find the most material on — which serves the best-documented user rather than
the best one.

**State why not the larger segment.** If a bigger group was passed over, that reasoning is the
single most frequently skipped and most frequently needed line in the module. `07-strategy` will
ask for it.

**State what choosing costs.** Every commitment gives something up. Naming it is what stops the
choice being quietly reversed in `08-product` when a requirement for the other segment appears.

**Split the buyer from the user where they differ.** Where the person who signs is not the person
who suffers, that is a segment boundary with consequences in `06-business`, `08-product` and
`11-growth`.

---

# Where It Misleads

**Firmographics get used because they are available, not because they predict anything.** Company
size is a proxy; what actually varies is whether anyone's job includes buying software. Prefer the
mechanism over the proxy whenever both are visible.

**Prioritizing feels like excluding, so it gets softened.** "We will focus on X but also serve Y"
is a refusal to choose, and it propagates as an unbounded requirement list two modules later.

**Segments drawn here can drift outside `02-market`'s boundary.** If the prioritized segment is not
inside `market_definition`, one of the two is wrong, and the gate returns the run to module 02.

**A segment can be behaviorally distinct and commercially irrelevant.** Different behavior is
necessary, not sufficient — the four columns exist so that a genuinely distinct group with no pain
and no budget is visible as such.

---

# Related

| | |
| --- | --- |
| `Personas.md` | What the chosen segment becomes |
| `Behaviors.md` | The evidence the split should rest on |
| `02-market` | The boundary segments must sit inside |
| `07-strategy` | Where the choice is defended again |

---

> **Concept Note**
>
> If two segments would receive the same product for the same
> reasons, you have one segment and two names for it.
>
> A split that changes no decision has cost you a persona and bought
> nothing.
