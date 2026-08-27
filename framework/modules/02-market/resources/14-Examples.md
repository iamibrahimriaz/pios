---
Title: Examples
Module: 02-market
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show a market analysis that passes the gate, with the arithmetic shown.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 02-market/core/06-Framework.md
Outputs:
  - A reference market analysis
Related Modules:
  - 05-competition
  - 06-business
Tags:
  - Market
  - Examples
  - Reference
---

# Examples

---

# Overview

The same run continued from `01-idea`. Note that the passing version is **smaller than the plausible-looking wrong version** in every
figure, and that the disagreement between two sizing methods is recorded rather than resolved.

---

# The Worked Market Analysis

```
MARKET ANALYSIS — «Consultation notes for single-handed practices»

FRAME 1 — BOUND
  Who:   single-handed and two-doctor general practices
  Need:  clinical documentation during the consultation
  Where: «named jurisdiction» [from idea_brief — never inferred]

  Outside the market, and why:
    Multi-partner practices — different buying process, existing contracts
    Hospital settings       — different records systems entirely
    Allied health           — different documentation obligations
    Other jurisdictions     — different regime; candidates for later

  Boundary test: a two-site practice sharing one records system is OUT.
    The need is the same; the buying process and integration are not.

  Category name: practitioners say "note-taking" or "documentation".
    No settled vendor category. [finding — new-category education cost
    applies in 11-growth if we position as one]

FRAME 2 — REGULATE   (before sizing, deliberately)
  Regimes applying: «regime A» (data protection), «regime B» (clinical
    software classification) [verified: «regulator publication», «date»]

  Concrete obligations, not regime names:
    - Personal and special-category data: erasable on request, and
      auditable on read → 09-technology
    - Data residency: «jurisdiction» only
    - Clinical software classification: if the product suggests clinical
      content, «classification» applies → certification, ~£40k, 9–12 months
      [verified: «guidance», «date»]

  Barrier to entry: the certification above. Real, purchasable, slow.
    Also excludes competitors — 06-business/knowledge/Moat.md.

  Direction of travel: TIGHTENING on automated clinical decision support.
    [verified: «consultation», «date»] → 14-ai-systems autonomy ceiling.

  Does regulation exclude a named segment?  No. Proceed.

FRAME 3 — SIZE   (bottom-up preferred; both methods run)

  Bottom-up
    8,200 single-handed practices [verified: «register», «date»]
    × £600/year realistic price [assumption: derived from 05-competition]
    = TAM £4.9m [assumption — the price input is unsourced]

    SAM  − certification not held → £0 until cleared
         − practices with an integratable records system → 5,900
           [inferred: «basis»]
         = £3.5m [assumption]

    SOM  Route: «named association», 60 members in «county»
         40 contacts/month × 10% conversion [assumption] × 6 months
         = 24 practices × £600 = £14k year one [assumption]

  Top-down
    A published report gives «jurisdiction» primary-care software at £180m.
    Its boundary includes multi-partner practices, hospital primary care
    and prescribing systems. NOT our market.
    Not adopted. Recorded because the divergence is the finding:
    the report's market is ~37× ours, which is a boundary difference,
    not a disagreement about size.

  Rounded to one significant figure: TAM ~£5m. Every figure downstream
  inherits the unsourced price assumption.

FRAME 4 — TREND  (≥3, with ≥1 against)
  1. DEMAND ↑ consultation volume per clinician rose 3 years running
     [verified: «statistics», «date»]
  2. SUPPLY ↓ AGAINST — 3 of 4 incumbents shipped in-consultation capture
     in 24 months [verified: changelogs, «date»]
  3. TECHNOLOGY → inference cost falling; mechanism commoditizing
     [verified: provider pricing history]
  4. REGULATORY ↑ tightening on clinical decision support
     [verified: «consultation», «date»]

  Timing: LATE. The enabling change happened ~2 years ago and incumbents
  responded. A late entry needs a wedge they will not defend.

FRAME 5 — GAP
  Gap: single-handed practices unserved by the four main suppliers.
  Why it persists: ECONOMICS. Minimum contracts ~£4k/year and 3-month
    implementations, neither absorbable by a solo practice.
    [inferred: pricing pages + implementation docs, «date»]
  Implication: structural — closing it needs a different sales motion,
    not a feature. Moderate defensibility. 05-competition to test.
  Open question: one supplier launched and withdrew a solo tier.
    Reason unknown. Worth finding.

GATE
  ✓ Bounded, not adjectival
  ✓ TAM/SAM/SOM each sourced or marked [assumption]
  ✓ 4 trends with direction and evidence, including one against
  ✓ Regulatory constraints for the named jurisdiction identified, including its general data-protection regime
```

---

# Example 1 — Bottom-Up Beats Borrowed

## ❌ Poor

```
TAM: £180m (industry report, 2024).
```

## ✅ Good

```
TAM: 8,200 practices × £600/year = ~£5m
     [count verified: «register», «date»; price assumption]
Report figure of £180m describes a market including multi-partner and
hospital primary care — ~37× ours. Boundary difference, not a
disagreement. Not adopted.
```

**Why.** A bottom-up figure has separately checkable inputs, so it can be corrected. A borrowed figure can only be accepted or rejected
whole — and it carries someone else's boundary.

---

# Example 2 — The Trend That Argues Against

## ❌ Poor

```
The market is moving toward AI-assisted documentation, which validates
our approach.
```

## ✅ Good

```
AGAINST: three of four incumbents shipped in-consultation capture within
24 months [verified: changelogs, «date»]. They own the records
integration. Our window is the segment they cannot serve profitably,
not the capability.
```

**Why.** This is a gate condition, and it is the trend that changes the strategy. A list where everything supports the idea documents the
search rather than the market.

---

# Example 3 — A Gap With a Reason

## ❌ Poor

```
Nobody serves solo practices — a clear opportunity.
```

## ✅ Good

```
Nobody serves them because minimum contracts are ~£4k and implementation
is 3 months. Economics, not oversight. Structural, because closing it
requires a different sales motion.
```

**Why.** The reason is the finding. It also tells `05-competition` what to test and `06-business` what price the market has already
demonstrated it cannot absorb.

---

> **Resource Note**
>
> The passing analysis produces a £5m TAM where the careless one produced
> £89bn.
>
> Both took the same afternoon. Only one of them can be argued with.
