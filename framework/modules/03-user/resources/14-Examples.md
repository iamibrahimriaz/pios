---
Title: Examples
Module: 03-user
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show a user analysis that passes the gate, with gaps recorded rather than filled.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 03-user/core/06-Framework.md
Outputs:
  - A reference user analysis
Related Modules:
  - 04-problem
  - 08-product
Tags:
  - User
  - Examples
  - Reference
---

# Examples

---

# Overview

The run continues. The distinguishing feature of a passing user analysis is that **the observed material and the inferred material are
visibly different**, and the unknown material is listed rather than filled in.

---

# The Worked User Analysis

```
USER ANALYSIS — «Consultation notes for single-handed practices»

MOVE 1 — DIVIDE   (behavioral, not demographic)
  Segment A  No practice manager. GP is user, buyer and approver.
             Size ~«n» [inferred: «basis»]
             Pain intensity: high [reported]
             Ability to pay: unknown [GAP]
             Reachable via: «named association» [verified: membership list]

  Segment B  Has a practice manager. Purchase needs sign-off plus an
             information-governance check.
             Size ~«n» [inferred]
             Pain intensity: high, borne by the GP not the buyer
             Ability to pay: higher
             Reachable via: same association, plus «procurement route»

  These differ on WHO SIGNS, which changes the product, the price and
  the motion. Not on age or geography.

MOVE 2 — CHOOSE
  Prioritized: A
  Why:  fastest to first customer; no procurement; the sufferer is the buyer
  Why not B, which is larger: the sales cycle exceeds the operator's
        runway [06-business input]
  Given up: the larger segment; any multi-clinician requirement.
        Recorded so 08-product cannot reintroduce it quietly.

MOVE 3 — EMBODY
  PERSONA — single-handed GP
    Setting          single-handed practice, ~1,800 patients [verified]
    Sessions/week    8–9 [inferred: contract terms]
    Records system   «named», not replaceable [verified]
    When notes happen  after the last patient [reported: 3 of 4]
    Time taken       UNKNOWN [GAP — 04-problem must quantify]
    Measured on      UNKNOWN [GAP — highest-value missing row]
    Who signs        the GP [verified for segment A by definition]
    Primary voice    NONE LOCATED. No GP outside the operator's network
                     has been interviewed.

  Buyer persona: not needed for segment A — buyer and user coincide.
  Recorded explicitly rather than omitted.

MOVE 4 — OBSERVE   (before Move 5, deliberately)
  1. Opens records system — 20–40s [reported]
  2. Finds patient — duplicates common; checks DOB to confirm
  3. Consultation — 10 min. TOOL: memory + a paper pad
     WORKAROUND: keywords on paper  ← strongest evidence in the analysis
  4. Note deferred to after the session
     FRICTION IS THE TRANSITION: recall degrades; the pad bridges it
  5. After last patient — works through the pad
     Duration UNKNOWN [GAP]; interrupted by phone, results, staff

  Unhappy path: interrupted mid-note → part-written records, and no way
  to tell later which are incomplete.

  SWITCHING COST
    Migration   none — the records stay in their system
    Retraining  one person, minutes
    Disruption  a live consultation is not a safe place to experiment ← the barrier
    Lock-in     none
    Risk        a missed note is clinical and medico-legal
    Bar: must work first time, in a real consultation, unrehearsed.

MOVE 5 — JOB   (after observing)
  J1  When a patient is describing symptoms, I want to capture what they
      said without breaking eye contact, so I can stay present.
      140/week · satisfied today by memory + pad · poorly
      Emotional: not appearing distracted matters as much as accuracy.
  J2  When my last patient leaves, I want the record already complete,
      so I can go home.
      8–9/week · satisfied today by nothing · they stay
  NOT serving: coding, referrals, prescribing.

THE IMMOVABLES
  1. The records system stays → we sit alongside it
  2. The 10-minute appointment → nothing may lengthen a consultation
  3. A clinician signs the record → 14-ai-systems ceiling is "drafts"
  4. Patients can see the screen → nothing sensitive by default
  5. No personal phone at some sites → voice may be unavailable

GATE
  ✓ 2 segments, with a stated reason for prioritizing one
  ✓ Jobs stated as jobs, no solution named
  ✓ Current workflow documented, tools named
  ✓ Cost of switching named
  NEEDS USER: time taken; what they are measured on; ability to pay
```

---

# Example 1 — A Behavioral Segment

## ❌ Poor

```
Segment 1: small practices.  Segment 2: larger practices.
```

## ✅ Good

```
Segment A: no practice manager — the GP signs.
Segment B: has one — sign-off plus governance review, 6–12 weeks.
```

**Why.** Company size is a proxy. Whether anyone's job includes buying software is the mechanism, and it changes the product, the price and
the sales motion.

---

# Example 2 — Observation Before Interpretation

## ❌ Poor

```
GPs want AI to handle their documentation burden.
```

## ✅ Good

```
Observed: keywords written on a paper pad during the consultation,
worked through afterwards.
Interpreted: the friction is the transition between the consultation and
the record — not the typing itself. [inferred]
```

**Why.** Two sentences, kept separate. The first is evidence; the second may be wrong. Merged into one confident sentence, the inference
becomes a finding.

---

# Example 3 — Switching Cost That Names the Real Barrier

## ❌ Poor

```
Switching cost: low. No data to migrate.
```

## ✅ Good

```
Migration: none. Retraining: minutes. Lock-in: none.
DISRUPTION: a live consultation is not a safe place to try new software.
Bar to clear: works first time, unrehearsed, in front of a patient.
```

**Why.** Four dimensions are genuinely low and the fifth is decisive. Averaging them to "low" loses the only one that determines adoption.

---

# Example 4 — Recording a Gap Instead of Filling It

## ❌ Poor

```
Time spent on documentation: approximately 90 minutes per day.
```

## ✅ Good

```
Time spent: UNKNOWN [GAP].
Reported as "an hour or two" by 3 GPs — recollection, not measurement.
04-problem to quantify: ask for a week of actual finish times, or an
export of note timestamps.
```

**Why.** The gap is the actionable output. The approximation would have become `06-business`'s value case with no source.

---

> **Resource Note**
>
> The passing analysis has three rows marked UNKNOWN and one paper pad.
>
> The paper pad is the most valuable thing in it — someone paying a cost,
> repeatedly, to get an outcome.
