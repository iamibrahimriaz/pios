---
Title: Examples
Module: 04-problem
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show a problem analysis that passes the gate with an empty validated list.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 04-problem/core/06-Framework.md
Outputs:
  - A reference problem analysis
Related Modules:
  - 07-strategy
  - 10-execution
Tags:
  - Problem
  - Examples
  - Reference
---

# Examples

---

# Overview

The run continues. This example is deliberately the hard case: **the validated list is empty**, and the analysis passes anyway — because
saying so is what the gate requires and what changes the roadmap.

---

# The Worked Problem Analysis

```
PROBLEM ANALYSIS — «Consultation notes for single-handed practices»

VERDICT: UNVALIDATED
  The central problem is plausible and entirely unevidenced by any
  retrievable source. Consequence: Milestone Zero is validation.

STAGE 1–2 — HARVEST AND CLASSIFY
  From 03-user's workflow, jobs and immovables.

  PROBLEMS (a cost is paid when unsolved)
    P1  Notes are completed after the session ends
    P2  Recall degrades between consultation and write-up
    P3  Part-written records cannot be distinguished from complete ones

  SYMPTOMS (carry the problem beneath forward)
    "The records system is slow"  → adds to after-hours time → P1
    "Typing breaks eye contact"   → nothing captured in session → P2

  PREFERENCES (excluded, kept visible)
    Dark mode. A nicer interface. Mobile app.
    Excluded because nothing bad happens if unmet.
    Recorded so they are not re-proposed in 08-product as omissions.

STAGE 3 — SCORE   (Frequency × Severity × Workaround)

  P1  Notes completed after the session
      F 5  daily [inferred: 8–9 sessions/week from contract terms]
      S 5  unpaid time, wellbeing, and medico-legal risk if one is missed
      W 3  a paper pad — poor but real
      = 75
      Cost/occurrence: 60–120 min/day [assumption: recollection]
      Who bears it: the GP personally. Not the practice.
        → 06-business: the sufferer is the buyer in segment A. Good.
        → but an absorbed cost is harder to sell against than an invoiced
          one — carry that forward.

  P2  Recall degrades between consultation and write-up
      F 5 · S 3 · W 3 (the pad) = 45
      Cost: unquantified. Manifests as less complete notes [inferred]

  P3  Part-written records indistinguishable from complete ones
      F 1  occasional [reported]
      S 5  a missing note is a clinical and medico-legal event
      W 1  none — they simply check manually
      = 5
      Note: low score, high severity. Worth flagging to 08-product as an
      edge case even though it is below any MVP line.

STAGE 4 — SORT

  ┌─ VALIDATED ─────────────────────────────────────────────┐
  │ (empty)                                                 │
  │                                                         │
  │ No problem here carries a retrievable source.            │
  │ Stated rather than populated. This is the finding.       │
  └─────────────────────────────────────────────────────────┘

  ┌─ ASSUMED ───────────────────────────────────────────────┐
  │ P1  [reported: 3 of 4 GPs known to the operator]         │
  │ P2  [inferred: from the observed paper pad]              │
  │ P3  [reported: 1 GP]                                     │
  │                                                         │
  │ Not lesser problems. Unproven ones.                      │
  └─────────────────────────────────────────────────────────┘

STAGE 5 — SHARPEN
  Sharpest: P1 — notes completed after the session ends.

  Why this one
    Highest score. Daily. Costs unpaid time and carries risk. The
    workaround (a paper pad) is real evidence of effort and clearly
    inadequate — someone maintaining it is paying repeatedly.

  Why not P2, which scored 45
    P2 is a cause of P1 rather than a separate problem. Solving P1
    necessarily addresses it. Recorded so it is not counted twice.

  Evidence standing: ASSUMED, not verified.
    CRITICAL FINDING. It propagates:
      07-strategy → Milestone Zero binding
      10-execution → milestone_zero must not be ABSENT
      11-growth → no acquisition spend before it completes

  Root cause check
    P1 ← nothing captured in session ← capture breaks eye contact
       ← the records system requires structured entry at point of care
       ← its data model was built for billing ← NOT ACTIONABLE
    Level addressed: "nothing captured in session".
    A decision, not an oversight — deeper causes sit inside an
    immovable system (03-user).

STAGE 6 — PLAN   (cheapest test of the most load-bearing belief)

  T1  Belief: GPs will accept a drafted note without reading it in full
      LOAD-BEARING. If false, no time is saved.
      Method: Wizard of Oz — hand-written drafts from 10 real consultations
      Sample: 5 single-handed GPs outside the operator's network
      Effort: 3 days
      Would invalidate: 3+ re-read every draft in full
      Criteria written «date», before gathering

  T2  Belief: after-session note time is 60+ minutes
      Method: ask for last week's finish times; request a timestamp export
      Sample: 3 practices
      Effort: 1 day
      Would invalidate: median under 20 minutes

  T3  Belief: a GP in segment A can authorize £40/month alone
      Method: ask who signs
      Sample: 5
      Effort: hours
      Would invalidate: 3+ describe an approval step

  Carried from 03-user: time taken; what they are measured on;
    ability to pay. All are NEEDS USER, all are in this plan.

  STOP-AND-RETHINK TRIGGER
    If T1 fails, this should not be built as conceived. A draft nobody
    trusts unread saves nothing, and a structured form may be the answer
    — 14-ai-systems will compare them.

GATE
  ✓ Each problem scored on frequency, severity, workaround
  ✗ ≥3 problems with [verified] evidence — NOT MET, declared
  ✓ Sharpest problem identified and defended
  ✓ Unvalidated problems explicitly listed as such

  declared_shortfall: verified-problem criterion.
  Permitted here uniquely, and it propagates.
```

---

# Example 1 — Classifying Before Scoring

## ❌ Poor

```
Problems: slow system, typing burden, no dark mode, after-hours work.
```

## ✅ Good

```
PROBLEM     after-hours work (a cost is paid)
SYMPTOM     slow system → why? → adds to after-hours work
SYMPTOM     typing burden → why? → nothing captured in session
PREFERENCE  dark mode → nothing bad happens if unmet → excluded, kept visible
```

**Why.** Stage 2 prevents most of the damage this module can do. Scoring an unclassified list ranks a preference alongside unpaid overtime.

---

# Example 2 — The Workaround Column

## ❌ Poor

```
P1: after-hours notes. Frequency 5, Severity 5. Score 25. Top priority.
```

## ✅ Good

```
P1: F 5 × S 5 × W 3 = 75
W 3 = a paper pad exists. Poor, but real.
Meaning: someone is already paying a repeated cost to contain this —
strong evidence of demand, and evidence the current tool does not solve it.
```

**Why.** The workaround is the most informative dimension. It also supplies `05-competition` with a competitor no feature matrix will list.

---

# Example 3 — Declaring the Shortfall

## ❌ Poor

```
Validated: after-hours documentation burden [verified: interviews].
```

## ✅ Good

```
VALIDATED: (empty)
declared_shortfall: verified-problem criterion not met.
Consequence: Milestone Zero is validation. No build, no spend, until T1
completes.
```

**Why.** This is the framework's only permitted `declared_shortfall`, and it exists so that an honest run can proceed without pretending.
Manufacturing the validated list would have removed Milestone Zero and started the build on an untested belief.

---

> **Resource Note**
>
> This analysis passes its gate while failing one criterion, openly.
>
> That is the mechanism working: the shortfall is declared, it propagates
> to three modules, and nothing downstream can mistake belief for
> evidence.
