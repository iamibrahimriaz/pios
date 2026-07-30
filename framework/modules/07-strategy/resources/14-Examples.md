---
Title: Examples
Module: 07-strategy
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show a strategy whose weighted comparison changes the answer, and a human checkpoint.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 07-strategy/core/06-Framework.md
Outputs:
  - A reference strategy
Related Modules:
  - 08-product
  - 10-execution
Tags:
  - Strategy
  - Examples
  - Reference
---

# Examples

---

# Overview

The run continues, and this is where it turns. The weighted comparison — with `04-problem`'s declared shortfall given real weight — selects the
**service-first option**, not the AI product the idea started as.

That reversal is what a working strategy module looks like.

---

# The Worked Strategy

```
STRATEGY — «Consultation notes for single-handed practices»

MOVE 1 — DIVERGE   (each produces a different first build)

A. In-consultation capture (narrow tool)
   First build  capture in-session → draft → GP edits → saves to record
   Solves       P1, P2 · Price £600/yr · Defensibility moderate
   Risk         GPs will not accept an unread draft (04-problem T1)

B. Structured template library (no model)
   First build  a fast keyboard-driven form, used in-consultation
   Solves       P2 fully, P1 partly · Price £300/yr · Defensibility none
   Risk         does not close the day; the value case halves
   ADVOCATE     "The problem is recall between consultation and write-up.
                A four-field form solves that today, for £300, with no
                accuracy risk and no inference cost."

C. Service first — human transcription for solo practices
   First build  an operations process, not software
   Solves       P1, P2 fully · Price £2,400/yr · Defensibility low
   Risk         margin; caps at what one person can process
   ADVOCATE     "Prove the problem with revenue before building. The
                transcripts become the training and evaluation set."

MOVE 2 — COMPARE   (weights published first)
  Solves sharpest problem      ×3   04-problem rank 1
  Survives if problem is wrong ×3   04-problem DECLARED A SHORTFALL
  Time to first customer       ×2   06-business: short runway
  Supports the modeled price   ×2   06-business: conditionally viable
  Defensibility                ×1   05-competition: moderate at best
  Buildable by this team       ×1

  Criterion (weight)        A      B      C
  Solves sharpest (×3)      15      9     15
  Survives if wrong (×3)     6     12     15
  Time to customer (×2)      4      8     10
  Supports price (×2)        8      4     10
  Defensibility (×1)         3      1      2
  Buildable (×1)             3      5      2
  TOTAL                     39     39     54

  C wins. This was not the expected result, and the reason is the second
  criterion: if GPs will not accept an unread draft, A is worthless and C
  still works — a human transcript needs no trust in a model.

MOVE 3 — CHOOSE
  Chosen: C, with a stated transition to A.

  Why this one
    It solves P1 and P2 fully. It produces revenue in weeks rather than
    months. And it survives the failure of the load-bearing belief, which
    04-problem flagged as unverified.

  What was rejected, and what we lose
    A — we lose the margin and the scalability. Real losses, recorded so
        A is not quietly reintroduced as a feature.
    B — we lose the low price point that might reach practices unable to
        afford £2,400. Reconsider if C's price proves to be the barrier.

  What we are betting on
    That single-handed GPs will pay for completed notes at all — a
    proposition C tests directly, with money, in weeks.

  TRANSITION TRIGGER (C → A)
    When 15 practices are served and 300+ transcript pairs are collected,
    evaluate whether a model reaches the accuracy the service delivers.
    14-ai-systems runs that comparison then, with real data.

  REVERSAL TRIGGER
    If a competitor announces a solo tier under £1,200/yr, the price
    advantage of C disappears and A's timeline must compress.

MOVE 4 — CUT
  CUT PRINCIPLE: in scope only if a note cannot be delivered without it.

  ABOVE THE LINE
    Audio capture in the consultation · secure upload · a transcription
    workflow the operator performs · GP review and approval in the record ·
    audit trail and access control (obligations) · the four unpopulated
    states per screen

  END-TO-END TEST
    Can a single-handed GP get a completed note using only this? YES.
    Capture, upload, human transcription, review, save.

  WHAT THE MVP PROVES
    Whether GPs will pay for completed notes, and what accuracy the
    service actually achieves — which becomes A's evaluation bar.

  WHAT IT DOES NOT PROVE
    Whether a model can match it · whether it scales past one operator ·
    whether the margin works at volume.

MOVE 5 — BOUND   (non-goals)
  Capabilities  no coding, no referrals, no prescribing
  Segments      not multi-partner practices (procurement exceeds runway)
  Problems      not P3 (part-written records) — real, low frequency
  Integrations  «one records system» only
  Automation    NOT automating transcription in this phase.
                Reconsider at the transition trigger above.

MOVE 6 — REGISTER
  Risks (inherited first, ratings spread)
    R1 sharpest problem assumed — fatal impact, Milestone Zero mitigates
    R2 inference cost — DEFERRED. C has no inference cost. A risk that
       arrives with the transition, not now
    R3 gap not defensible on product — high, ACCEPTED, shapes the sequence
    R4 no repeatable channel — high, 11-growth after activation
    R5 NEW: the service caps at one operator's throughput — high, and it
       is the reason the transition trigger exists

  Sequence
    M0  VALIDATION — 04-problem T1 and T2. Required: the problem is
        assumed. Teaches whether the problem is real and quantified.
    M1  Serve four practices manually. Teaches: will they pay?
    M2  Serve fifteen. Teaches: does the channel repeat, and what accuracy
        does the human service achieve?
    M3  Decision point: transition to A, or stay a service.
    No durations. 07-strategy/knowledge/Timeline.md.

  Stop conditions — written «date»
    S1 3+ of 5 re-read every draft in full → the time saving does not
       exist. Note: this stops A, not C. C is unaffected, which is why
       C was chosen.
    S2 median after-session time under 20 min → problem too small. STOP.
    S3 no conversion outside the operator's network within four months →
       no channel. Return to 06-business.

⏸ HUMAN CHECKPOINT
  1. What we propose to build
     A transcription service for single-handed practices, delivered
     manually, transitioning to software once the data exists.

  2. What we are deliberately not doing
     Not building the AI capture tool first. Not serving multi-partner
     practices. Not automating anything in phase one.

  3. The load-bearing assumption
     That GPs will pay £2,400/year for completed notes. C tests this
     with money in weeks — which is why it beat the AI option.

  4. Decisions needed, with recommendations
     a) Approve the service-first sequence?  RECOMMEND YES — it survives
        the failure of the belief the AI option depends on.
     b) Accept the throughput ceiling of one operator?  RECOMMEND YES for
        phase one; the transition trigger addresses it.
     c) Price at £2,400/yr?  RECOMMEND testing at that price with the
        first four. It is above the £600 modeled in 06-business, so that
        model needs revisiting — a REGRESS, recorded.

  Waiting. The cut commits money and months, and it is the operator's call.
```

---

# Example 1 — An Option That Survives Being Wrong

## ❌ Poor

```
Survives if the problem is wrong: not applicable — we have validated
the problem.
```

## ✅ Good

```
Weight ×3, because 04-problem declared a shortfall.
A scores 2: if GPs will not accept an unread draft, A is worthless.
C scores 5: a human transcript needs no trust in a model.
This criterion is why C wins.
```

**Why.** The framework's instruction is explicit — this criterion deserves attention when module 04 declared a shortfall, and it is the one most
often set to zero.

---

# Example 2 — Recording What Rejection Costs

## ❌ Poor

```
Option A was rejected as too risky for phase one.
```

## ✅ Good

```
A rejected. What we lose: the margin and the scalability. Both real.
Recorded so A is not quietly reintroduced as a feature in 08-product.
```

**Why.** Every option had something to offer. Naming it is what stops the rejected approach returning later with an argument already prepared.

---

# Example 3 — A Regress Instead of a Fudge

## ❌ Poor

```
Price: £2,400/year, above our earlier £600 model but justified by the
higher value of a complete service.
```

## ✅ Good

```
£2,400/yr is above the £600 modeled in 06-business. That model needs
revisiting — a REGRESS, recorded, and raised at the checkpoint as a
decision for the operator.
```

**Why.** The price changed, so the sizing and the economics change with it. Quietly carrying the new figure forward would leave two
incompatible models in the same run.

---

> **Resource Note**
>
> The strategy that survives contact with `04-problem`'s shortfall is not
> the AI product the idea began as.
>
> A module that never changes the answer is not comparing options — it is
> documenting a preference.
