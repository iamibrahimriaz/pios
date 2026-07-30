---
Title: Technology Comparison
Module: 05-competition
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Compare competitors' technology only where it produces a user-visible difference.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 05-competition/knowledge/Feature-Comparison.md
Outputs:
  - Technology notes within competitor_matrix
Related Modules:
  - 09-technology
Tags:
  - Competition
  - Technology
  - Concept
---

# Technology Comparison

---

# What It Is

An assessment of competitors' technology, narrowly scoped: **only where it produces a difference the user or buyer
can perceive.**

| Worth recording | Not worth recording |
| --- | --- |
| Where their data is hosted, if the buyer's regime cares | Which framework they use |
| Whether they offer an API, and what it exposes | Whether their stack is modern |
| Which systems they integrate with | Their choice of database |
| Whether they work offline, if the environment requires it | Their language |
| Certifications and audit evidence they hold | Their deployment tooling |
| Whether they can be self-hosted, where that is demanded | How elegant it appears |

The right-hand column is invisible to buyers, unverifiable from outside, and irrelevant to whether a ranked problem
is solved. The left-hand column is procurement criteria.

---

# When It Applies

Alongside Move 3 (Test) and Move 5 (Locate). Findings feed `09-technology` as market expectations rather than as
design decisions.

---

# How to Apply It Here

**Record integrations as competitive assets.** An existing connection to the system of record is one of the highest
switching costs in institutional software, and it is `Strengths.md`'s "integration depth" row made concrete.

**Capture certifications and audit evidence.** In regulated markets these are entry requirements, and a competitor
holding them has already paid a cost this product must plan for. `02-market` Frame 2 established which apply.

**Note data residency and hosting.** Where the regime constrains it, this is a procurement gate rather than a
technical detail, and it may exclude a competitor from the segment entirely — which is an opening.

**Treat an API as a market expectation.** If every competitor exposes one, it is table stakes for `08-product`; if
none does, it may be differentiation, and `Gap-Analysis.md` should test whether it is held.

**Keep architectural speculation out.** What is inferable from the outside is limited, and inference stated as fact
about a competitor's architecture is a fabricated finding. `Architecture-Comparison.md` sets the limits.

---

# Where It Misleads

**A modern stack is claimed as an advantage and is not a customer benefit.** No buyer has ever chosen a product for
its framework. It may make the team faster, which is an internal advantage, and it belongs nowhere in a competitive
position.

**Technology is claimed as a moat, which it almost never is.** The same tools are available to everyone, including
the incumbent with the distribution. `Gap-Analysis.md` lists what actually defends: commercial conflict, data,
distribution, sales motion.

**Legacy technology is read as weakness.** An older system that is deeply integrated, certified and trusted is
stronger competitively than a modern one that is none of those. Age correlates with entrenchment.

**Public technical claims are taken at face value.** Marketing describes intent. Certifications, status pages,
documentation and integration listings are verifiable; assertions about scale and speed are not.

**It becomes an excuse to design here.** This module maps the field. Choosing this product's technology is
`09-technology`'s work, and it chooses technology fifth of six deliberately.

---

# Related

| | |
| --- | --- |
| `Architecture-Comparison.md` | The limits of external inference |
| `AI-Comparison.md` | Where the mechanism does matter competitively |
| `Strengths.md` | Integration depth and certification as assets |
| `09-technology` | Where these become constraints, not decisions |

---

> **Concept Note**
>
> Record technology only where a buyer could notice it.
>
> A better stack has never won an account. An existing integration
> wins them routinely.
