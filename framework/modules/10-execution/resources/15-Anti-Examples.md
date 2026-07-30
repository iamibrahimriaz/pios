---
Title: Anti-Examples
Module: 10-execution
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show plans and handoffs nobody could start from, and milestones that demo nothing.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 10-execution/core/06-Framework.md
Outputs:
  - Recognition of horizontal slicing and failed cold starts
Related Modules:
  - 08-product
  - 13-operations
Tags:
  - Execution
  - Anti Examples
  - Reference
---

# Anti-Examples

---

# Overview

This module's only real test is whether someone who was never here could start work today. Each example below fails it while looking like a plan.

---

# Anti-Example 1 — Horizontal Slicing

## ❌ Looks like a plan

```
Milestones
M1  Data layer complete — schema, migrations, repositories
M2  API complete — all endpoints, validation, error handling
M3  UI complete — all screens implemented
M4  Integration — records system connection
M5  Polish and launch
```

**Why it fails**

- **Apply the demo test:** at the end of M1, what can you show a real user doing? Nothing. Same for M2 and M3. The first demonstrable moment is
  after M4, which is after the budget.
- **Horizontal slicing defers all learning to the end.** Nothing is demonstrable until everything is, so the first honest feedback arrives when
  it is most expensive to act on.
- **No milestone teaches anything.** Each is a layer, which makes it a stage of one milestone rather than a milestone.
- **"Polish and launch" is where the unspecified work hides** — the edge states, the empty screens, the error copy.

## ✅ Passes

```
M0  VALIDATION — required, the problem is assumed
    Deliver: 04-problem T1 and T2 run. Nothing built.
    Demo test: you can show five GPs' responses to hand-written drafts.
    Teaches: whether GPs accept a draft unread, and the real time cost.
    Decision it enables: proceed, re-scope to option B, or stop (S1/S2).

M1  ONE GP, ONE NOTE, END TO END
    Deliver: record → upload → we transcribe by hand → GP reviews →
      saves to the record. Plus the four unpopulated states per screen,
      audit trail and access control.
    Demo test: a GP records a real consultation and the note lands in the
      patient record. One whole job.
    Teaches: whether the review-and-approve flow works in a live setting.
    Not done at this point: export, search, notifications, any automation.

M2  FOUR PRACTICES
    Deliver: the same path, hardened. Unsent-recording visibility.
      The retention job. The restore rehearsal.
    Demo test: four practices using it for a week without the operator
      intervening in the product.
    Teaches: whether they pay, and what the manual workflow costs per note.

M3  FIFTEEN PRACTICES
    Demo test: fifteen practices, and 300+ transcript pairs collected.
    Teaches: the accuracy the human service achieves — which becomes
      14-ai-systems' evaluation bar at the transition decision.
```

---

# Anti-Example 2 — The Handoff That Fails the Cold Start

## ❌ Looks like a plan

```
BUILD HANDOFF

As discussed, we are building the consultation notes product per the
research. The PRD covers the requirements and the architecture document
covers the technical approach. Start with the data layer as agreed.

Key decisions are documented in the strategy section. Note the outstanding
questions on pricing and the records system integration — we'll resolve
those as we go.

The team should aim for an MVP in roughly three months.
```

**Why it fails**

- **"As discussed", "as agreed", "per the research"** — the reader was not there. Every one of these is a reference to a conversation that does
  not exist for them.
- **It requires opening three other documents before writing a line of code.** The essentials must be carried inline.
- **The outstanding questions are in a build-blocking position**, phrased as things to resolve later. Someone will guess, and never say so.
- **"Three months" is a duration the framework cannot produce.** No team is stated, so it is a number that will be treated as a commitment.
- **The first task is a layer**, so day one is spent deciding what to actually do.

## ✅ Passes

```
BUILD HANDOFF — «Consultation notes», M1

WHAT THIS IS
  A transcription service for single-handed GP practices. A GP records the
  consultation; a human transcribes it; the GP reviews and approves; the
  note is written to their records system. The transcription is performed
  manually by the operator in this milestone — there is no model.

THE FIRST TASK, in one sentence
  Build the consultation record and the audio upload path, with the five
  edge cases in R-02 and the unsent-recordings indicator.

DEFINITION OF DONE FOR M1
  ✓ A GP can record, upload, and see the recording queued
  ✓ A reviewer can open a draft, edit it, and approve it
  ✓ On approval the note is written to «records system» via «operation»
  ✓ Every write produces an audit entry (actor, timestamp, id, action)
  ✓ Every screen has its empty, loading, error and permission states
  ✓ Cross-practice access test passes in the pipeline
  ✓ Retention job runs and is alerted on absence of success

  NOT DONE at this point — stated so "done" is not disputed
  ✗ Export · search · notifications · templates
  ✗ Any automation of transcription
  ✗ A second records system
  ✗ Multi-clinician support (non-goal, 07-strategy)

ESSENTIALS, CARRIED INLINE
  Entities and constraints: «the Consultation and Recording tables from
    09-technology, reproduced here in full»
  The three operations with request and response bodies: «reproduced»
  The disclosure policy: 404 for anything the caller may not see. Always.
  The data-loss position: locally-held audio not yet uploaded can be lost.
    The unsent count must be visible at all times. Not optional.

BLOCKED WORK — with owners
  B1  Erasure versus 90-day backup retention conflict.
      OWNER: «operator». Needs legal input.
      BLOCKS: nothing in M1. Blocks launch.
  B2  Which «records system» operation writes a note, and whether it
      accepts free text.
      OWNER: «operator» — has the vendor relationship.
      BLOCKS: R-05, which is in M1. **Start with R-01 and R-02.**
  B3  Price point: £2,400/yr contradicts 06-business's £600 model.
      OWNER: «operator». Decision, not research.
      BLOCKS: nothing technical.

  No unresolved assumption sits in a build-blocking position. B2 blocks a
  requirement, and the handoff says what to build instead.

SEQUENCE — no dates
  R-06, R-07 (audit, access) → independent, build first
  R-01 → R-02 → R-04 → R-05 (R-05 blocked on B2)
  Relative size: R-01 S · R-02 M · R-04 M · R-05 M · R-06 S · R-07 S
  Parallelizable: R-06/R-07 alongside R-01.
  Durations: the framework does not know the team. Operator to add.
```

---

# Anti-Example 3 — Design Principles From Nowhere

## ❌ Looks like a plan

```
UX principles
  Keep it simple and intuitive
  Delight the user at every step
  Consistency across the product
  Mobile-first, responsive design
```

**Why it fails**

- **None derives from a finding**, and none constrains a decision. Two designers could build opposite things and both claim compliance.
- **"Mobile-first" contradicts `03-user`'s findings** — some sites prohibit personal phones, and the work happens at a practice desk.
- **"Delight at every step"** is a consumer heuristic applied to a tool used dozens of times a day, where every added moment is a tax.

## ✅ Passes

```
PRINCIPLES — each with its finding

1. Every action survives being abandoned halfway.
   FINDING: 03-user — the GP is interrupted constantly by phone, results
   and staff. A part-written note must persist and be identifiable.

2. Nothing lengthens a consultation, even slightly.
   FINDING: 03-user immovable 2 — the 10-minute appointment is structural.
   This rules out any in-consultation confirmation dialog.

3. Nothing sensitive is displayed by default.
   FINDING: 03-user immovable 4 — patients can see the screen.

4. The GP can always complete the note manually.
   FINDING: 03-user — a missed note is a clinical and medico-legal event.
   The fallback is a requirement, not a contingency.

Each can be violated visibly, which is the test.
```

---

# Anti-Example 4 — Screens Specified Only When Full

## ❌ Looks like a plan

```
Screens
  Consultation list — shows all consultations with status
  Review screen — shows the draft with an approve button
  Settings — practice details and preferences
```

**Why it fails**

- **The unpopulated states are absent.** Empty, loading, error and permission — for every screen. The populated state is the one that occurs
  least often at the beginning.
- **A new GP's first experience is a blank consultation list**, which is unspecified and will ship as whatever the framework renders.
- **Time to first value is not counted**, and it is the number that predicts adoption better than any feature comparison.

## ✅ Passes

```
CONSULTATION LIST
  Populated    today's consultations, most recent first, state visible
  Empty — first use   "No consultations yet. Record your first one."
                      plus the single action that starts a recording.
                      This is the most-seen screen in the product.
  Empty — cleared     "Nothing outstanding." Distinguishable from broken.
  Loading             inline on the list region only; nothing under 300ms
  Error               "Could not load your consultations. Retry."
                      The unsent-recordings count still displays.
  Permission          another practice's id → the same as not-found

TIME TO FIRST VALUE
  Arrive → record → upload → (human transcription, «n» hours) → review →
  save.  Steps to first value: 4 for the GP. Elapsed: overnight.
  The overnight gap is a product property of the service model and must be
  stated in the empty state, not discovered.
```

---

# Anti-Example 5 — Untested and Undeclared

## ❌ Looks like a plan

```
QA strategy
  Unit tests for business logic
  Integration tests for the API
  End-to-end tests for critical paths
  Manual testing before each release
  Target: 80% code coverage
```

**Why it fails**

- **Nothing traces to a criterion or an edge case.** `08-product` wrote acceptance criteria in a testable form precisely so they could become
  tests, and the five edge categories per requirement are most of the work.
- **Coverage percentage is not a coverage claim.** A suite testing implementation details resists refactoring and proves little.
- **Nothing is declared as deliberately not tested**, which is the only version of this section that survives a real schedule.
- **The cross-practice access test is missing**, and `09-technology` required it as the verification of its threat answer.

## ✅ Passes

```
COVERAGE — every MUST requirement has at least one verification

  R-01  unit: the UNIQUE constraint rejects a duplicate consultation
        integration: POST twice returns 409 with the existing id
  R-02  unit: duration CHECK rejects under 5 seconds
        integration: all five edge cases from 08-product §8
        e2e: upload interrupted at 50%, resumes, completes
  R-04  e2e: record → transcribe → review → approve → appears in record
  R-06  integration: every write produces an audit entry
  R-07  integration: CROSS-PRACTICE ACCESS DENIED via the API, the export
        operation and the search endpoint.
        (09-technology's threat answer, verified. Runs every pipeline.)

DELIBERATELY NOT TESTED — declared
  ✗ The manual transcription workflow. It is a human process in M1;
    13-operations owns its quality, not the test suite.
  ✗ Load beyond «n» concurrent uploads. The first bottleneck is named in
    09-technology; testing beyond target is effort spent where the
    constraint is not.
  ✗ «Records system» behavior under its own failure. We cannot reproduce
    it. The failure path is specified; the dependency is not simulated.

An honest exclusion is worth more than an implied claim of full coverage.
```

---

# The Pattern Across All Five

| Failure | How it presents |
| --- | --- |
| Horizontal slicing | Milestones named after layers; nothing demonstrable until the end |
| Failed cold start | "As discussed", references to other documents, a duration with no team |
| Principles from nowhere | Simplicity, delight, consistency — unviolatable |
| Populated states only | Screens described full; the first-use screen unspecified |
| Undeclared coverage | A percentage target and no traced verifications |

---

> **Resource Note**
>
> The cold-start test is not "could they understand this" — it is "could
> they start."
>
> A handoff with an unresolved assumption in a build-blocking position gets
> guessed, and nobody will ever mention that they guessed.
