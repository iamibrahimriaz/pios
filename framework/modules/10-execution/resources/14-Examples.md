---
Title: Examples
Module: 10-execution
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show a handoff that passes the cold-start test, with blocked work owned.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 10-execution/core/06-Framework.md
Outputs:
  - A reference build handoff
Related Modules:
  - 08-product
  - 13-operations
Tags:
  - Execution
  - Examples
  - Reference
---

# Examples

---

# Overview

The run continues. The build handoff is the only deliverable the manifest marks `critical`, and its standard is the strictest in the framework:

> **The cold-start test.** Could an agent or engineer open this file, with no access to the research and no other document, and start writing
> correct code today?

Not "could understand the project". Could **start**.

---

# The Worked Execution Plan

```
EXECUTION PLAN — «Consultation notes», service-delivered MVP

MOVE 1 — FLOW   (two critical paths only)

  PATH A — the GP records and files a note
    Trigger  a consultation begins
    1  Opens the product on the practice desktop
       Sees: today's consultations; the unsent-recordings count
    2  Selects the patient, starts recording
       System: creates the consultation, state = recording
       CONSTRAINT: nothing here may lengthen the consultation (principle 2)
    3  Consultation happens. The product is not touched.
    4  Ends the recording
       System: uploads; if offline, retains locally and shows the count
       FAILURE: connection lost → audio retained, retried, GP continues
    5  Overnight: a human transcribes it
       This gap is a property of the service model and is stated in the
       interface, not discovered.
    6  Next morning: opens the draft, edits freely, approves
       System: writes to «records system», audits, marks documented
       IRREVERSIBLE from our product — corrections happen in their system
    7  Sees the note as it appears in the record, with the patient named

  PATH B — the reviewer transcribes  (the operator's own path)
    Included because it is a critical path in a service-delivered product,
    and 13-operations staffs it.

  FAILURE AND RECOVERY  (from 08-product's five categories, made
  experiential rather than left as status codes)
    No audio captured      → "No recording for this consultation" +
                             record now / write manually. Not an error.
    Recording too short    → "This recording appears empty — record again
                             or write manually." Audio retained until
                             dismissed.
    Upload cannot complete → "Waiting to upload — 1 recording."
                             GP continues working. Retried automatically.
    Another practice's id  → the same as not-found. Never "not permitted".
    Offline over «n» hours → notified that recordings are queued and unsent

  TIME TO FIRST VALUE
    4 GP steps. Elapsed: overnight, because transcription is human.
    Counted, stated, and surfaced in the empty state.

  PRINCIPLES — each with its finding
    1 Every action survives being abandoned halfway
      FINDING: constant interruption (03-user)
    2 Nothing lengthens a consultation, even slightly
      FINDING: the 10-minute appointment is immovable
    3 Nothing sensitive is displayed by default
      FINDING: patients can see the screen
    4 The GP can always complete the note manually
      FINDING: a missed note is a clinical and medico-legal event

  SCREEN STATES — all four, per screen
    Consultation list · Review screen · Recording view
    (Empty–first-use, Empty–cleared, Loading, Error, Permission each
     specified. The first-use empty state is the most-seen screen.)

MOVE 2 — SLICE   (demo test applied to each)
  M0  Validation. Demo: five GPs' responses to hand-written drafts.
  M1  One GP, one note, end to end. Demo: a real consultation lands in
      the patient record.
  M2  Four practices for a week. Demo: used without operator intervention.
  M3  Fifteen practices, 300+ transcript pairs. Demo: the accuracy the
      human service achieves.
  Each is independently shippable — it could stop there and leave a usable
  product. Not a complete one; a usable one.

MOVE 3 — SEQUENCE
  Principle: LEARN EARLIEST. Stated, and applied consistently.
  Reason: the sharpest problem is assumed (04-problem declared a
  shortfall), so feedback outranks value delivery until it is verified.

  MILESTONE ZERO IS FIRST. Required — the problem is assumed.
  Building before it completes is the expensive mistake the framework
  exists to prevent.

  ONE-WAY DOORS, placed deliberately
    The datastore choice (09-technology: reversibility LOW).
    Committed at M1 — early enough to build on, late enough to be informed
    by M0's result. If M0 invalidates the approach, no schema work is lost.

MOVE 4 — DEFINE   (per milestone, including what is not done)
  M1 DONE
    ✓ record, upload, queued and visible
    ✓ draft opened, edited, approved
    ✓ note written to «records system» with an audit entry
    ✓ four unpopulated states on every screen
    ✓ cross-practice access test passes in the pipeline
    ✓ retention job runs, alerted on absence of success
    NOT DONE — stated so "done" is not disputed
    ✗ export · search · notifications · templates
    ✗ any automation of transcription
    ✗ a second records system
    ✗ multi-clinician support (non-goal)
    TEACHES: whether review-and-approve works in a live practice.

MOVE 5 — VERIFY
  Every MUST requirement has a verification; each traces to a criterion or
  an edge case. (See 15-Anti-Examples.md's passing block for the mapping.)
  DELIBERATELY NOT TESTED, declared: the manual transcription workflow ·
  load beyond target · «records system» under its own failure.

MOVE 6 — HAND OVER   (the critical deliverable)
  See below.

THE ESTIMATE BOUNDARY
  Sequence, dependencies, relative size and the critical path: established.
  Dates, durations, velocity: NOT established. The framework does not know
  the team. The operator adds durations, with the assumed team stated.
```

---

# The Build Handoff

```
BUILD HANDOFF — «Consultation notes», M1

WHAT THIS IS
  A transcription service for single-handed GP practices. A GP records the
  consultation; a human transcribes it overnight; the GP reviews and
  approves; the note is written to their records system. Transcription is
  performed manually by the operator in this milestone. There is no model.

THE FIRST TASK, in one sentence
  Build the consultation record and the audio upload path, including R-02's
  five edge cases and the unsent-recordings indicator.

ESSENTIALS, INLINE  (you should not need another document to start)
  Consultation table
    id uuid pk · practice_id uuid not null fk RESTRICT ·
    clinician_id uuid not null fk RESTRICT · patient_ref text not null
    (REGULATED) · occurred_at timestamptz not null · state enum not null
    default 'recording' · documented_at timestamptz null ·
    created_at timestamptz not null default now()
    CHECK documented_at is not null IFF state = 'documented'
    UNIQUE (clinician_id, occurred_at)   ← this enforces idempotency
    INDEX (practice_id, occurred_at desc)
    Forbidden transitions: documented → anything · transcribed → recording

  Recording table
    id uuid pk · consultation_id uuid not null fk CASCADE ·
    storage_key text null · duration_secs integer not null
    CHECK duration_secs >= 5 · uploaded_at timestamptz null ·
    audio_deleted_at timestamptz null
    CHECK storage_key is null IFF audio_deleted_at is not null

  Operations
    POST /consultations → 201 {id, state}
      idempotent: a retry returns 409 with the existing id
    POST /consultations/{id}/recording → 202 {state}
      413 recording_too_large · 422 recording_too_short · 404 not_found

  DISCLOSURE POLICY  404 for anything the caller may not see. Always,
    on every path including export and search. Inconsistency is a defect.

  DATA-LOSS POSITION  Locally-held audio not yet uploaded can be lost if
    the device is lost or cleared. It is the only point at which clinical
    content can be lost. The unsent count must be visible at all times.
    NOT OPTIONAL.

DEFINITION OF DONE  — as in Move 4 above, including the ✗ list.

BLOCKED WORK — every item owned
  B1  Erasure versus 90-day backup retention conflict.
      OWNER «operator». Needs legal input.
      BLOCKS: nothing in M1. Blocks launch.
  B2  Which «records system» operation writes a note, and whether it
      accepts free text.
      OWNER «operator» — holds the vendor relationship.
      BLOCKS R-05, which is in M1.
      → START WITH R-01 and R-02. Do not guess the integration.
  B3  Price: £2,400/yr contradicts 06-business's £600 model.
      OWNER «operator». A decision, not research. Blocks nothing technical.

  No unresolved assumption sits in a build-blocking position. B2 blocks a
  requirement and the handoff says what to build instead.

SEQUENCE — no dates
  R-06, R-07 first (independent, and they are obligations)
  R-01 → R-02 → R-04 → R-05 (R-05 blocked on B2)
  Relative size  R-01 S · R-02 M · R-04 M · R-05 M · R-06 S · R-07 S
  Parallelizable R-06/R-07 alongside R-01
  Durations: operator to add, with the assumed team stated.
```

---

# Example 1 — The Demo Test Applied

## ❌ Poor

```
M1: complete the data layer and API.
```

## ✅ Good

```
M1: a GP records a real consultation and the note lands in the patient
record. One whole job.
```

**Why.** If the answer describes a layer, it is not a milestone — it is a stage of one. Vertical slicing repeats some work and is still faster,
because it produces information immediately.

---

# Example 2 — Blocked Work With an Owner

## ❌ Poor

```
Outstanding: the records system integration details need confirming.
We'll resolve this during development.
```

## ✅ Good

```
B2  Which operation writes a note, and whether it accepts free text.
    OWNER «operator» — holds the vendor relationship.
    BLOCKS R-05, which is in M1.
    → START WITH R-01 and R-02. Do not guess the integration.
```

**Why.** This is the mechanism that keeps the framework's honesty about evidence from stalling the team. The builder sees what cannot start, who
owns it, and what to do instead. Left as an assumption in the instructions, someone guesses and never says so.

---

# Example 3 — Milestone Zero First

## ❌ Poor

```
Sequence: begin with the core capture flow, validate with users in
parallel.
```

## ✅ Good

```
MILESTONE ZERO IS FIRST. Required — the sharpest problem is assumed.
Sequencing principle: LEARN EARLIEST, because 04-problem declared a
shortfall.
The one-way door (the datastore) is committed at M1, after M0's result.
```

**Why.** This is the fourth place Milestone Zero has consequences — declared in `04-problem`, made binding in `07-strategy`, sequenced first
here, and gating spend in `11-growth`. "In parallel" is how it becomes optional.

---

# Example 4 — The Estimate Boundary Held

## ❌ Poor

```
M1: 3 weeks. M2: 4 weeks. M3: 6 weeks. Launch in month four.
```

## ✅ Good

```
Sequence, dependencies, relative size and the critical path: established.
Durations: the framework does not know the team. Operator to add, with the
assumed team stated.
R-01 S · R-02 M · R-04 M — relative to each other, basis stated.
```

**Why.** An estimate with no stated team is not an estimate — it is a number that will be treated as one, by people who were not told where it
came from.

---

> **Resource Note**
>
> The handoff reproduces the schema and the operations inline, and it says
> "do not guess the integration."
>
> Both exist for the same reason: the reader was not here, and they will
> otherwise fill the gap silently.
