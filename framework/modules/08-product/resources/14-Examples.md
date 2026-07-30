---
Title: Examples
Module: 08-product
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show a specification that passes the two-builder test, with the spine visible.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 08-product/core/06-Framework.md
Outputs:
  - A reference specification
Related Modules:
  - 09-technology
  - 10-execution
Tags:
  - Product
  - Examples
  - Reference
---

# Examples

---

# Overview

The run continues with the service-first approach `07-strategy` chose. Note that the spine is built before any requirement is written, and that
the requirement list matches module 07's cut exactly.

---

# The Worked Specification

```
SPECIFICATION — «Consultation notes», MVP (service-delivered)

INHERITED, not re-argued
  Approach   transcription service for single-handed practices, delivered
             manually, transitioning to software at 15 practices
  Cut        07-strategy, binding
  Non-goals  no coding, no referrals, no prescribing, no multi-clinician,
             one records system only
  The bet    GPs will pay £2,400/yr for completed notes
             [assumption — declared shortfall from 04-problem]

MOVE 1 — TRACE   (the spine, built first)

  Job step (03-user)              Parent  Served  Requirements
  Consultation happens            P2      yes     R-01, R-02
  Note is produced                P1      yes     R-03
  GP checks and files it          P1      yes     R-04, R-05
  Record confirmed complete       P3      NO      ledger, trigger: a GP
                                                  reports a missing note
  Obligations (not job steps)     —       yes     R-06 audit, R-07 access

  Both directions checked:
    Orphans: none. Every requirement names a parent.
    Unserved above-line problems: none. P3 is below the line, recorded.

MOVE 2 — SPECIFY
  MUST    R-01 record the consultation
          R-02 upload the recording securely
          R-03 produce a transcribed draft
          R-04 GP reviews and approves
          R-05 the note reaches the patient record
          R-06 audit trail
          R-07 access control
  SHOULD  R-10 export a note as PDF
  COULD   R-09 search past notes

  BOUNDARY CHECK: MUST list vs 07-strategy's above-the-line list.
    Difference: NONE. ✓

  Discovered while specifying, sent to the ledger not the MUST list:
    email notifications · template library · a dashboard (no parent —
    REJECTED, recorded so it is not re-proposed)

MOVE 3 — BEHAVE   (R-04 shown in full)

  R-04  GP review and approval    Parent: P1    MUST
  Trigger      a transcribed draft is available for a consultation
  Input        the GP may edit any part of the draft. No field mandatory.
  System       on approval: writes final text to «records system» via
               «operation»; records an audit entry (actor, timestamp,
               note id, "approved"); marks the draft consumed
  State after  the note exists in the patient record; the draft is retained
               «n» days then deleted; the consultation is marked documented
  User sees    the saved note as it appears in the record, with a
               confirmation naming the patient
  Reversibility  NOT reversible from our product. Corrections happen in the
               records system under its own audit rules.
               Stated because two engineers would answer this differently.
  Rejection    the GP may discard a draft. The audio is retained until the
               retention period expires. The discard is audited.

  No technology named. No screens described. 09-technology and design own
  those, and a requirement naming either removes their decision.

MOVE 4 — BREAK   (R-02 shown in full)

  Empty       no audio captured. "No recording for this consultation" +
              record now / write manually. Not an error.
  Invalid     under 5 seconds or silent. Rejected: "This recording appears
              empty — record again or write manually." Audio retained until
              the GP dismisses it.
  Failure     connection lost mid-upload. AUDIO RETAINED LOCALLY, retried
              automatically. "Waiting to upload — 1 recording". The GP
              continues working.
  Permission  another practice's recording → "Not found", per
              09-technology's disclosure policy. Never "not permitted".
  Limit       over «n» minutes: proceeds, with a warning that transcription
              may take longer. Offline over «n» hours: the GP is notified
              that recordings are queued.

  DATA-LOSS POSITION
    Audio held locally and not yet uploaded is lost if the device is lost
    or cleared. It is the only point at which clinical content can be lost.
    Mitigation: unsent recordings are visible at all times.
    → 10-execution must surface this state. Not optional.

MOVE 5 — ORDER
  Factor            R-01  R-02  R-03  R-04  R-05  R-06  R-07
  Problem weight     2     2     1     1     1     —     —
  Reach              5     5     5     5     5     5     5
  Confidence         2     2     2     2     2     5     5
  Effort             S     M     L     M     M     S     S

  R-06 and R-07 score oddly because they are obligations rather than
  problem-serving requirements. Noted rather than forced into the scheme.

  Score/tier disagreement: none this time. Recorded as checked.

  Dependencies (functional test applied)
    R-02 requires R-01 — real: nothing to upload otherwise
    R-04 requires R-03 — real: nothing to review otherwise
    R-05 requires R-04 — real
    R-06, R-07 independent — can be built first, and should be
    R-03 is the operator's manual workflow, not software. It blocks R-04
      operationally, not technically.

  FIRST SHIPPABLE SLICE
    R-01 + R-02 + R-03(manual) + R-04 + R-05, plus R-06/R-07.
    A GP records, we transcribe by hand, they approve, it files.
    One whole job. Cut vertically — 10-execution's demo test.

MOVE 6 — PROVE   (R-03 shown, both kinds)
  STATISTICAL
    Given 200 real consultation recordings from the golden set,
    when transcribed by the service,
    then ≥95% are judged clinically accurate by a «domain expert».
  PER-INSTANCE — always true
    the draft is always editable before saving
    the draft always displays the recording it came from
    the draft can always be discarded
    nothing writes to the record without explicit GP approval

  Note: the per-instance guarantees are conventional requirements and carry
  most of the real safety. 14-ai-systems will need the same pair when the
  transition to software happens.

GATE
  ✓ Every requirement traces to a ranked problem
  ✓ Acceptance criteria testable, not aspirational
  ✓ Edge cases and failure states specified
  ✓ Out-of-MVP items in the ledger, not dropped
```

---

# Example 1 — The Spine Before the Requirements

## ❌ Poor

```
R-01 through R-12, each with a rationale explaining its value.
```

## ✅ Good

```
Job step → parent problem → served? → requirement id
Built first. The parent is chosen before the requirement exists, so a
retrospective justification has nowhere to attach.
```

**Why.** An orphan can almost always be justified, and the justification is written afterwards and sounds reasonable. Building the spine first
removes the opportunity.

---

# Example 2 — Passing the Two-Builder Test

## ❌ Poor

```
The GP reviews and approves the note, which is then saved.
```

## ✅ Good

```
Reversibility: NOT reversible from our product. Corrections happen in the
records system under its own audit rules.
```

**Why.** That is the point where two engineers diverge, named explicitly. The test is not "is this clear" — it is "where would two readings
differ", and then answering it.

---

# Example 3 — Stating the Data-Loss Position

## ❌ Poor

```
Uploads are retried on failure.
```

## ✅ Good

```
Audio held locally and not yet uploaded is lost if the device is lost or
cleared. It is the only point at which clinical content can be lost.
Mitigation: unsent recordings are visible at all times.
```

**Why.** This is the most consequential edge answer in most products and it is almost never written down until it happens. Written here, it
becomes a `10-execution` requirement and a `13-operations` S1 definition.

---

# Example 4 — Both Kinds of Criterion

## ❌ Poor

```
Transcription accuracy: 95%.
```

## ✅ Good

```
STATISTICAL   ≥95% of 200 golden-set cases judged accurate by a clinician
PER-INSTANCE  always editable · always shows its source · always
              discardable · never writes without approval
```

**Why.** 95% is compatible with catastrophic failure on a recognizable subset. The per-instance guarantees hold every time, and they are
conventionally testable.

---

> **Resource Note**
>
> The boundary check found no difference this time — and that is worth
> recording as a checked result rather than an unstated assumption.
>
> Scope laundering does not announce itself. Only the list comparison
> catches it.
