---
Title: References
Module: 02-market
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Route each market question to a source type, and set the discipline for published figures.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 00-AI-Constitution/resources/18-References.md
Outputs:
  - Source routes for market questions
Related Modules:
  - 05-competition
  - 06-business
Tags:
  - Market
  - References
  - Reference
---

# References

---

# Overview

This module makes numeric claims, which makes sourcing discipline load-bearing. A figure here becomes `06-business`'s revenue model, and
by then its origin is invisible.

No citations are listed. What follows is where to look, what each source can support, and how to handle the published market report — the
single most misused source in product work.

---

# Routing Each Frame's Questions

| Question | Source type | What it can support |
| --- | --- | --- |
| How many «units» exist? | **Official registers, government statistics, professional body membership** | `[verified]` — this is the strongest figure in the module |
| Which regimes apply? | **Regulator publications, official guidance** | `[verified]`, and the obligation rather than the regime name |
| Certification cost and duration | Regulator or notified-body published schedules | `[verified]` if published; otherwise `[assumption]` with a basis |
| Realistic price | Competitor pricing pages, dated — `05-competition` | `[verified]` for list price; `[inferred]` for transaction price |
| Is demand growing? | Sector statistics, published operational data | `[verified]` for direction; be careful with rates |
| What are practitioners saying? | Professional press, practitioner forums, bodies' publications | Existence of a concern — never its prevalence |
| Is the gap real? | Absence across competitor offerings, plus the reason | `[inferred]`, with the reason as the finding |

The first row is worth emphasizing: **a population count from an official register is the most reliable number this module will produce.**
Build the sizing on it.

---

# The Published Market Report Problem

A purchased or summarized report is a legitimate source used carefully, and a liability used casually.

**What it can tell you**

- That a category exists and roughly how it is described
- Direction of travel at category level
- Who the recognized suppliers are

**What it cannot tell you**

- The size of *your* market, because its boundary is not yours
- Anything checkable, if the methodology is not published
- A growth rate applicable to a narrow segment

**How to use one honestly**

```
Report figure: £180m, «publisher», «year».
Its boundary:  primary-care software including multi-partner practices,
               hospital primary care, prescribing systems.
Our boundary:  single-handed and two-doctor practices, documentation only.
Difference:    ~37×. Not adopted. Recorded because the divergence is a
               finding about boundary, not about size.
```

That block is the whole discipline. State the figure, state its boundary, state the difference, and say whether it was adopted.

---

# Source Tiers, Applied

| Tier | At the market stage |
| --- | --- |
| **Primary** | Registers, regulator publications, official statistics, standards bodies. Where sizing and regulation should come from |
| **Industry** | Sector press and reports. Good for vocabulary, category names and direction; weak for figures |
| **Academic** | Occasionally establishes incidence at population level, which nothing else does |
| **Product and technical** | Competitor pricing and changelogs — `05-competition` owns these, dated |
| **Community** | Practitioner forums. Strong for the concern, worthless for prevalence |
| **AI-assisted** | Orienting, and generating candidate search routes. **Never a citation, and never a figure** |

The last row is the sharpest risk in this module. A model will produce a plausible market size on request, with plausible precision. It is
`[assumption]` with no basis, and it is indistinguishable from a researched figure once written down.

---

# Verification Discipline

**Date every figure, and record the access date.** Registers are updated, pricing pages are rewritten, and guidance is superseded.

**Round to the precision the weakest input supports.** A TAM derived from one assumed price deserves one significant figure. Precision is
read as accuracy by every downstream reader.

**Run both sizing methods where both are available, and record disagreement as a finding.** Quietly adopting the more attractive number is
the module's characteristic dishonesty.

**Separate population from incidence, always.** 8,200 practices exist `[verified]`. That 70% of them have this problem is `[inferred]` or
`[assumption]`, and the two are frequently merged into one confident sentence.

**Record the searches that found nothing.** An absent category name, an absent competitor, an absent regulation. Frame 5 needs them, and
`05-competition` will re-run them otherwise.

---

# Common Mistakes With Sources Here

| Mistake | Consequence |
| --- | --- |
| Adopting a report's figure | Sizing a market nobody intends to enter |
| A model-generated market size | An invented number with `06-business` built on it |
| Undated pricing | A price anchor for a product that has since changed |
| Category CAGR applied to a segment | An unsupported transfer, presented as a projection |
| Forum volume as incidence | An inflated problem `03-user` cannot reconcile |
| Sizing before checking the regime | A figure wrong by an order of magnitude |

---

> **Resource Note**
>
> The most reliable number in this module is a population count from an
> official register. Build on it.
>
> The least reliable is a market size someone else computed for a boundary
> they did not publish.
