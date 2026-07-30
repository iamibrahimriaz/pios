---
Title: Anti-Examples
Module: 05-competition
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show competitive analyses that decide nothing, and the reason each fails.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 05-competition/core/06-Framework.md
Outputs:
  - Recognition of parity thinking and undefended gaps
Related Modules:
  - 06-business
  - 07-strategy
Tags:
  - Competition
  - Anti Examples
  - Reference
---

# Anti-Examples

---

# Overview

Competitive analysis is the section that takes the most effort and changes the fewest decisions. Each example below represents real work
producing no conclusion.

---

# Anti-Example 1 — The Tick Table

## ❌ Looks thorough

```
Feature              Us  MedNote  ClinicPro  NoteFast
Voice input          ✓   ✓        ✗          ✓
Templates            ✓   ✓        ✓          ✓
Mobile app           ✓   ✗        ✓          ✓
Coding suggestions   ✓   ✓        ✓          ✗
Integrations         ✓   ✓        ✓          ✓
API                  ✓   ✗        ✓          ✗
Dark mode            ✓   ✗        ✗          ✓
```

**Why it fails**

- **Features are not problems.** The table shows what exists and says nothing about where the market fails the chosen segment. `04-problem`
  produced a ranked list; none of it appears here.
- **The "Us" column is filled in for a product that does not exist.** Seven ticks for capabilities nobody has built, compared against
  shipping products.
- **No status quo column.** The paper pad from `03-user` holds this market and is absent entirely.
- **It decides nothing.** After all this work, no gap is identified and no position follows.

## ✅ Passes

```
Ranked problem                    Rank  MedNote  ClinicPro  Paper pad  Us
P1 Notes completed after session   1    partly   partly     partly      —
P2 Recall degrades before write-up 2    partly   not        partly      —
P3 Part-written vs complete        3    not      not        not         —

Who solves P1 best today?  The paper pad, marginally — it is free,
  instant, trusted and requires no change. Both products score "partly"
  because their capture still happens after the consultation.

Which ranked problem does nobody solve well?  P1 and P2 both.
  That is the opening, if it can be held.

"Us" left empty — 07-strategy fills it. This module maps the field.
```

---

# Anti-Example 2 — The Missing Incumbent

## ❌ Looks thorough

```
Competitors
1. MedNote — £4,200/year, market leader
2. ClinicPro — £3,800/year, strong integrations
3. NoteFast — £2,900/year, newer entrant
4. ScribeAI — free beta, VC-funded
5. DictateMD — £1,200/year, voice only
```

**Why it fails**

- **Five funded products and no status quo.** The gate requires "do nothing / status quo" evaluated as a competitor, and for
  single-handed practices it is the market leader — it holds nearly all of them.
- **Non-consumption is absent.** If most of the segment uses nothing, the competition is inertia rather than any product, which changes the
  entire strategy.
- **The list came from a category search**, which is an instrument that can only find products. A spreadsheet, an assistant and a paper pad
  are invisible to it.
- **Every price is undated and unsourced.**

## ✅ Passes

```
DIRECT (same problem, same segment)
  None. All five funded products target multi-partner practices —
  visible in their minimum contract sizes. [inferred: pricing pages, «date»]

INDIRECT (same problem, different segment)
  MedNote     £4,200/yr min, 3-month implementation [verified: pricing
              page + implementation doc, accessed «date»]
  ClinicPro   "Contact us" — marked UNAVAILABLE. Signal: sales-led motion,
              a price floor, and a procurement process.

SUBSTITUTE
  A transcription service — ~£200/month, human, trusted, flexible.
  Sets a quality bar rather than a price ceiling.

STATUS QUO — the actual incumbent
  Memory + a paper pad. £0.
  Advantages nobody lists: no change, no procurement, no training,
  no risk, total trust, works in a 10-minute appointment.
  Switching cost to displace it: 03-user's five dimensions — the binding
  one is that a live consultation is not a safe place to experiment.

NON-CONSUMPTION
  Most of segment A uses no software for this. [inferred: absence of any
  supplier serving them — 02-market Frame 5]
  → 11-growth: the competition is inertia. Education, not displacement.

WHO TRIED AND STOPPED
  One supplier launched a "solo" tier in «year», withdrew it in «year».
  Reason unknown. OPEN QUESTION — worth finding before proceeding.
```

---

# Anti-Example 3 — The Silent Price Estimate

## ❌ Looks thorough

```
Pricing
MedNote    ~£350/month
ClinicPro  ~£300/month
NoteFast   ~£240/month
Market average: ~£300/month. We will price at £250 to undercut.
```

**Why it fails**

- **Every figure is estimated with no source and no date.** "Around" is doing enormous work: these numbers will become `06-business`'s
  revenue model and by then their origin is invisible.
- **An average of three guesses is presented as a market rate.**
- **Undercutting is adopted as a strategy**, which is the least defensible position available — particularly when the real incumbent charges
  zero.
- **What the price includes is absent.** Seats, caps, implementation fees and contract length can differ threefold at the same headline
  figure.

## ✅ Passes

```
MedNote    £4,200/year minimum, 5 seats included, 3-month implementation
           at £2,000 [verified: pricing page + implementation guide,
           accessed «date»]
           → effective first-year cost £6,200. Not a monthly product.
ClinicPro  UNAVAILABLE — "contact us". Signal recorded, no figure invented.
NoteFast   £2,900/year, 3 seats [verified: pricing page, «date»]
ScribeAI   Free beta. Funded by venture capital [verified: «announcement»].
           Predicts: will need revenue, likely moving upmarket.
Paper pad  £0. The price to beat.

Reading it
  All paid options are priced for practices with 3+ clinicians. None is
  competing for a single-handed practice at any price — which is
  02-market's economic gap, confirmed from the pricing side.

Our anchor: value (04-problem's cost/occurrence), not their price.
  06-business will justify against £0, not against £4,200.
```

---

# Anti-Example 4 — The Undefended Gap

## ❌ Looks thorough

```
Gap: no competitor offers real-time in-consultation capture for solo
practices. This is our differentiation and the basis of our positioning.
```

**Why it fails**

- **The six-month question was never asked.** If this works, what stops an incumbent shipping it? Finding the gap is satisfying; testing it is
  not, so the test gets omitted — and the result is a product an incumbent copies in a quarter.
- **"Differentiation" is claimed for a capability, which is the most copyable kind.**
- **No named competitor.** Defensibility is a claim about what a specific company can and cannot do.

## ✅ Passes

```
Gap: P1 and P2 unserved for segment A.

Can it be held? Test against MedNote, the largest.
  Could they build it?        Yes, in a quarter. Nothing technical stops them.
  Would they sell it here?    No, and this is the answer.
    Their motion requires a £4,200 minimum and a 3-month implementation.
    Serving a single-handed practice at £600 loses money on every sale.
    Closing this gap requires a different sales motion, not a feature.
  Verdict: MODERATE. Structural on the commercial side, weak on the
    product side. Duration: until the segment becomes large enough to
    justify building the motion. Unknown, probably years.

  Counter-note: one supplier already tried and withdrew. Until we know
  why, this defensibility claim is [inferred] at best.

NOT DEFENSIBLE ON PRODUCT — stated plainly, and carried to 07-strategy
as a condition. Speed and focus are the advantage. Both are temporary.
```

---

# Anti-Example 5 — Positioning a Competitor Could Claim

## ❌ Looks thorough

```
For clinicians who value their time, «Product» is the easiest and most
intuitive way to handle clinical documentation, unlike legacy systems
that are slow and outdated.
```

**Why it fails**

- **Run the test:** put MedNote's name in front of it. It still reads true. That makes it a description of the category, not a position.
- **"Easiest", "most intuitive"** are the adjectives every competitor uses and `08-product` bans from criteria.
- **"Legacy systems that are slow"** is a generic contrast, not a scored limitation from the coverage table.
- **No segment.** "Clinicians who value their time" is everyone.

## ✅ Passes

```
For a single-handed GP who currently writes notes after their last
patient, «Product» is a consultation-time capture tool that completes the
record before the appointment ends — unlike MedNote and ClinicPro, whose
minimum contracts and three-month implementations are priced for
practices with three or more clinicians.

Test: "MedNote is a consultation-time capture tool… unlike MedNote,
whose minimum contract…" — fails immediately. Only we can say this.

Category: EXISTING (clinical documentation), entered at a segment
  nobody serves. No education cost — 11-growth funds displacement of a
  paper pad, not category creation.
```

---

# The Pattern Across All Five

| Failure | How it presents |
| --- | --- |
| Tick table | Features compared, no conclusion, "Us" column pre-filled |
| Missing incumbent | Only funded products; no status quo, no non-consumption |
| Silent price estimate | "~£350" with no source, becoming a revenue model |
| Undefended gap | An opening found, the six-month question unasked |
| Category-level positioning | A sentence the market leader could also say |

---

> **Resource Note**
>
> The competitor that beats you in this market costs nothing, is already
> installed, and was never sold to anyone.
>
> If the paper pad has no column, the table describes a different
> contest.
