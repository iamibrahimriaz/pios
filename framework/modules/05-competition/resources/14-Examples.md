---
Title: Examples
Module: 05-competition
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show a competitive analysis that reaches a conclusion, including an honest moat verdict.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 05-competition/core/06-Framework.md
Outputs:
  - A reference competitive analysis
Related Modules:
  - 06-business
  - 07-strategy
Tags:
  - Competition
  - Examples
  - Reference
---

# Examples

---

# Overview

The run continues. The distinguishing feature of a passing analysis is that it **concludes something**: a named opening, a defensibility
verdict with a duration, and a positioning sentence only this product could say.

---

# The Worked Competitive Analysis

```
COMPETITIVE ANALYSIS — «Consultation notes for single-handed practices»

MOVE 1–2 — ENUMERATE AND CLASSIFY

  DIRECT (same problem, same segment)
    None. All funded products target 3+ clinician practices, visible in
    their minimum contracts. [inferred: pricing pages, «date»]

  INDIRECT (same problem, different segment)
    MedNote    £4,200/yr min, 5 seats, 3-month implementation +£2,000
               [verified: pricing page + implementation guide, «date»]
    ClinicPro  UNAVAILABLE — "contact us". Signal: sales-led, price floor,
               procurement process.
    NoteFast   £2,900/yr, 3 seats [verified: pricing page, «date»]
    ScribeAI   Free beta, venture funded [verified: «announcement», «date»]
               Predicts: needs revenue; likely moves upmarket.

  SUBSTITUTE
    Human transcription service ~£200/month. Trusted, flexible.
    Sets a quality bar rather than a price ceiling.

  STATUS QUO — the actual incumbent
    Memory + a paper pad. £0.
    Unlisted advantages: no change, no procurement, no training, no risk,
    total trust, fits a 10-minute appointment.

  NON-CONSUMPTION
    Most of segment A uses no software for this. [inferred: 02-market
    Frame 5 — no supplier serves them]
    → 11-growth: the competition is inertia, not a product.

  WHO TRIED AND STOPPED
    One supplier launched a "solo" tier «year», withdrew «year».
    Reason UNKNOWN. Open question — find it before proceeding.

MOVE 3 — TEST   (the central move)

  Ranked problem                     Rank  MedNote  NoteFast  Paper pad  Us
  P1 Notes completed after session    1    partly   partly    partly      —
  P2 Recall degrades before write-up  2    partly   not       partly      —
  P3 Part-written vs complete         3    not      not       not         —

  Who solves P1 best today?
    The paper pad, marginally. It is free, instant and trusted. The paid
    products still capture after the consultation, so they score "partly"
    for the same reason it does.

  Which ranked problems does nobody solve well?
    P1 and P2. That is the opening — if it can be held.

  Table stakes (all competitors have; required, not differentiating):
    templates, export, audit trail, access control.
    → 08-product: requirements, not strategy.

MOVE 4 — PRICE
  All paid options are priced for 3+ clinicians. None competes for a
  single-handed practice at any price — 02-market's economic gap,
  confirmed from the pricing side.
  Our anchor: value from 04-problem, justified against £0. Not their price.

MOVE 5 — LOCATE
  Gap: P1 and P2 unserved for segment A.

  Held? Tested against MedNote (largest):
    Could they build it?     Yes, one quarter.
    Would they sell it here? No. A £600 sale loses money against a motion
      requiring a £4,200 minimum and a 3-month implementation.
    Verdict: MODERATE — structural commercially, weak on product.
    Duration: until the segment justifies building a self-serve motion.
      Unknown, probably years.
    Caveat: a supplier already tried and withdrew. Until the reason is
      known, this verdict is [inferred].

  NOT DEFENSIBLE ON PRODUCT — stated. Speed and focus are the advantage,
  and both are temporary. Carried to 07-strategy as a condition.

MOVE 6 — POSITION
  For a single-handed GP who currently writes notes after their last
  patient, «Product» is a consultation-time capture tool that completes
  the record before the appointment ends — unlike MedNote and ClinicPro,
  whose minimum contracts and three-month implementations are priced for
  practices with three or more clinicians.

  Test: substitute MedNote's name → fails immediately. Only we can say it.
  Category: EXISTING. No education cost; 11-growth funds displacement of
    a paper pad, not category creation.

GATE
  ✓ 5+ competitors, direct and indirect, with sources
  ✓ Pricing captured or explicitly marked unavailable
  ✓ Status quo evaluated as a competitor
  ✓ 1 defensible gap articulated with reasoning
  Note: defensibility is MODERATE and partly [inferred]. Stated, not
  upgraded.
```

---

# Example 1 — Scoring Against Problems

## ❌ Poor

```
We have voice input and they don't. Advantage: us.
```

## ✅ Good

```
P1 (rank 1): MedNote partly · NoteFast partly · paper pad partly
Nobody solves it well. Voice input is a mechanism; the problem is that
capture happens after the consultation in every case.
```

**Why.** A feature comparison tells you what exists. A problem-coverage table tells you where the market fails the person you chose to
serve — which is the only thing that produces a strategy.

---

# Example 2 — Marking a Price Unavailable

## ❌ Poor

```
ClinicPro: ~£300/month (estimated).
```

## ✅ Good

```
ClinicPro: UNAVAILABLE — "contact us".
Signal recorded: sales-led motion, a price floor, a procurement process.
No figure invented.
```

**Why.** The signal is more useful than a number would have been, and inventing one imports a guess into `06-business`'s model where its
origin disappears.

---

# Example 3 — An Honest Defensibility Verdict

## ❌ Poor

```
Our real-time capture is a strong differentiator and a defensible moat.
```

## ✅ Good

```
Could MedNote build it? Yes, one quarter.
Would they sell it to this segment? No — the economics of their motion
forbid it.
Verdict: MODERATE, commercial not technical. Duration: years, unknown.
NOT DEFENSIBLE ON PRODUCT — carried to 07-strategy as a condition.
```

**Why.** "Not defensible" is a legitimate finding that must be stated. Many good businesses start without a moat; what kills them is
discovering it after launch rather than sequencing for it.

---

# Example 4 — Positioning That Survives Substitution

## ❌ Poor

```
The easiest way for clinicians to handle documentation.
```

## ✅ Good

```
…unlike MedNote and ClinicPro, whose minimum contracts and three-month
implementations are priced for practices with three or more clinicians.
```

**Why.** The contrast is a scored limitation from the coverage table, naming real competitors. Substituting their name breaks the sentence,
which is the test.

---

> **Resource Note**
>
> The passing analysis concludes that the moat is moderate, partly
> inferred, and absent on the product side.
>
> That verdict is worth more than a confident one, because `07-strategy`
> can sequence for speed when it knows the clock is running.
