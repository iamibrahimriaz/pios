---
Title: Anti-Examples
Module: 02-market
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show market analyses that look rigorous and are wrong, with the reason each fails.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 02-market/core/06-Framework.md
Outputs:
  - Recognition of inflated or unfounded sizing
Related Modules:
  - 06-business
  - 07-strategy
Tags:
  - Market
  - Anti Examples
  - Reference
---

# Anti-Examples

---

# Overview

Market sections are the most confidently written and least checkable part of most product documents. Each example below would pass a
board review. Each is wrong in a way that propagates into `06-business`'s revenue model.

---

# Anti-Example 1 — The Adjective Market

## ❌ Looks rigorous

```
Market:  The global healthcare software market.
Size:    $89.4bn (2024), growing at 12.3% CAGR.
Source:  Industry report.
```

**Why it fails**

- **"The global healthcare software market" cannot be measured**, because nobody can say what is inside it. Run the boundary test: is a
  hospital bed-management system in or out? A pharmacy stock tool? A wearable? If the boundary cannot rule one borderline product in or
  out, it has not been drawn.
- **The figure measures a different market than the one being entered.** Adopting it imports the report's boundary silently — the
  borrowed-sizing failure.
- **Precision implies accuracy.** `$89.4bn` is more persuasive and no more true than "large".

## ✅ Passes

```
Boundary
  Who:   single-handed and two-doctor general practices
  Need:  clinical documentation during consultations
  Where: «named jurisdiction»
Outside: hospital settings, multi-partner practices, allied health.
Boundary test: a practice with a shared records system across three sites
  is OUT — the need and the buying process differ.
Category name: practitioners say "clinical documentation" or "note-taking".
  No settled vendor category name exists. [finding]
```

---

# Anti-Example 2 — Sized Before Regulated

## ❌ Looks rigorous

```
TAM: 8,200 practices × £600/year = £4.9m
SAM: £4.2m (85% reachable)
SOM: £245k (5% of SAM in year one)
```

**Why it fails**

- **Frame 2 was skipped.** Regulation determines who may participate at all. If a licensed entity or a certification is required to sell
  clinical software here, the addressable count is not 8,200 — and the whole table is wrong by an order of magnitude.
- **SAM at 85% of TAM is a cosmetic haircut.** Geography, regulation, price and channel rarely combine to remove only 15% of a market. No
  constraint was named.
- **SOM is a round share with no mechanism.** 5% is arithmetic performed backward from a comfortable answer. There is no channel, no
  contact volume and no conversion assumption inside it.

## ✅ Passes

```
Frame 2 first
  Regime «X» applies. Suppliers must hold «certification»: ~£40k, 9–12 months.
  This does not exclude the segment, but it is a precondition — 07-strategy.

TAM  8,200 practices [verified: «register», accessed «date»]
     × £600/year [assumption: derived from competitor pricing, 05-competition]
     = £4.9m [assumption — one input unsourced]

SAM  − certification not yet held → 0 until cleared
     − post-certification, «jurisdiction» only → 8,200
     − practices with no existing records system to integrate → 5,900
       [inferred: «basis»]
     = £3.5m [assumption]

SOM  Route: «named professional association», 60 members in «county».
     40 contacts/month × 10% conversion × 6 months = 24 practices
     × £600 = £14k year one [assumption: conversion unevidenced]
     Note: this is 0.4% of SAM. The round 5% was not derivable.
```

---

# Anti-Example 3 — The Selective Trend List

## ❌ Looks rigorous

```
Trends
1. AI adoption in healthcare is accelerating.
2. Clinician burnout is at record levels.
3. Practices are investing in digital tools.
4. Regulatory support for digital health is increasing.
```

**Why it fails**

- **Every trend supports the idea.** The gate requires at least one that argues against. Its absence means the research was selective
  rather than thorough — every market has forces pushing both ways.
- **No directions, no evidence, no dates.** "AI adoption is accelerating" is an observation, not a trend, and it is true of every
  competitor equally.
- **Broad technology trends favor the incumbent with the distribution** as much as the entrant. They change nothing about who wins.

## ✅ Passes

```
Trends
1. DEMAND ↑ Consultation volume per clinician rose 3 years running
   [verified: «published statistics», «date»]
   → the problem is worsening, and the urgency is real.

2. SUPPLY ↓ AGAINST THE IDEA. Three of four incumbent records suppliers
   shipped in-consultation capture in the last 24 months
   [verified: product changelogs, «date»]
   → the gap is closing, and they own the integration.

3. TECHNOLOGY → Inference cost fell materially; the capability is
   commoditizing [verified: provider pricing history]
   → whatever we build, the mechanism will not be the differentiator.

4. REGULATORY ↑ Tightening on automated clinical decision support
   [verified: «consultation document», «date»]
   → constrains autonomy — 14-ai-systems.

Timing: LATE. The distinguishing change happened 2 years ago and
  incumbents responded. Wedge must be a segment they will not serve.
```

---

# Anti-Example 4 — The Unexplained Gap

## ❌ Looks rigorous

```
Gap: No supplier serves single-handed practices well. This is a
     significant underserved segment.
```

**Why it fails**

- **No reason is given for why the gap persists**, which is the only content this frame produces. A gap with no explanation is usually not
  a gap — it is a search that stopped early.
- **Markets are searched constantly.** If nobody serves a visibly needy group, someone probably tried, and the reason they stopped is the
  most valuable thing available here.
- **"Significant" and "underserved" are the adjectives the module bans** in its own definition frame.

## ✅ Passes

```
Gap: single-handed practices are not served by the four main suppliers.

Why it persists — economics.
  Each of the four sells per-site with a minimum contract of ~£4k/year
  and a 3-month implementation. A single-handed practice cannot absorb
  either. [inferred: pricing pages + implementation timelines, «date»]

Implication
  The gap is real and structural — closing it would require them to build
  a different sales motion, not a feature. Moderate defensibility.
  05-competition to test against a named supplier.

Counter-note
  One supplier launched a "solo" tier in «year» and withdrew it in «year».
  Reason unknown — worth finding before proceeding. [open question]
```

---

# The Pattern Across All Four

| Failure | How it presents |
| --- | --- |
| Adjective market | A category name where a boundary should be |
| Sizing before regulating | A clean table that omits who may legally sell |
| Cosmetic SAM | A haircut with no constraint named |
| Round-share SOM | A percentage with no channel inside it |
| Selective trends | Four supporting trends and no opposing one |
| Unexplained gap | An opportunity with no reason for existing |

---

> **Resource Note**
>
> Every one of these produces a number `06-business` will build a revenue
> model on.
>
> The honest version is smaller, uglier, and traceable — and it is the
> only kind anyone can correct.
