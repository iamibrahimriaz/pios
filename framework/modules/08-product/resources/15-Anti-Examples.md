---
Title: Anti-Examples
Module: 08-product
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show specifications two engineers would build differently, and scope that moved.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 08-product/core/06-Framework.md
Outputs:
  - Recognition of scope laundering and unfailable criteria
Related Modules:
  - 09-technology
  - 10-execution
Tags:
  - Product
  - Anti Examples
  - Reference
---

# Anti-Examples

---

# Overview

Nothing is chosen in this module; something already chosen is made precise. Each example below either fails to be precise or quietly chooses
something new.

---

# Anti-Example 1 — The Orphan With Retrospective Justification

## ❌ Looks specified

```
R-14  Practice dashboard
      The system shall provide a dashboard showing outstanding notes,
      weekly volume and average completion time.
      Priority: MUST
      Rationale: gives GPs visibility into their documentation workload,
      supporting the core value proposition of reducing after-hours work.
```

**Why it fails**

- **No parent problem.** The rationale is a justification written after the requirement, and it sounds entirely reasonable — which is exactly
  why the rule is deletion rather than debate.
- **It traces to the value proposition, not to a ranked problem.** A requirement traced to a vision or a proposition is an orphan with an
  argument attached.
- **MUST, and it is below the cut line.** The chosen approach delivers completed notes; a dashboard is not required to deliver one.
- **It would generate support burden** — `13-operations` staffs for the questions "average completion time" will produce.

## ✅ Passes

```
The spine is built first, so the parent is chosen before the requirement.

Job step (03-user)          Parent problem  Served  Requirement
Consultation happens        P2              yes     R-01, R-02
Note is written after       P1              yes     R-03..R-06
Record is checked complete  P3              NO      deferred, ledger

R-14 dashboard: NO PARENT PROBLEM.
  Deleted, not deferred. Recorded in the ledger as REJECTED with the
  reason, so it is not re-proposed next quarter as an obvious omission.
```

---

# Anti-Example 2 — Everything Is a MUST

## ❌ Looks specified

```
R-01  Audio capture                      MUST
R-02  Secure upload                      MUST
R-03  Transcription workflow             MUST
R-04  GP review and approval             MUST
R-05  Save to record                     MUST
R-06  Audit trail                        MUST
R-07  Access control                     MUST
R-08  Email notifications                MUST
R-09  Search past notes                  MUST
R-10  Export to PDF                      MUST
R-11  Template library                   MUST
R-12  Multi-clinician support            MUST
```

**Why it fails**

- **Twelve MUSTs means the labels are decoration.** A specification whose MUST list equals its requirement list has relabeled rather than
  prioritized.
- **R-12 contradicts a non-goal.** `07-strategy` excluded multi-partner practices explicitly. This is scope laundering: the line moved by one
  reasonable addition.
- **R-08 through R-11 sit below the cut line** and were promoted while specifying, which is the failure the deferral ledger exists to prevent.
- **The boundary check would catch this mechanically** — the list versus module 07's list.

## ✅ Passes

```
BOUNDARY CHECK (mechanical, list vs list)
  07-strategy above the line: capture · upload · transcription workflow ·
    GP review and approval · audit trail · access control · unpopulated states
  This module's MUST list: R-01..R-07
  Difference: NONE. ✓

  MUST  R-01 audio capture · R-02 secure upload · R-03 transcription
        workflow · R-04 GP review and approval · R-05 save to record ·
        R-06 audit trail · R-07 access control
        (R-06 and R-07 are obligations from 09-technology, above the line
         regardless of ranking)

  SHOULD  R-10 export to PDF — ships without it, weaker for it

  COULD   R-09 search past notes

  DEFERRED → ledger, with triggers
    R-08 email notifications — when a GP asks twice
    R-11 template library — this was option B; if C's price is the
      barrier, it returns as a product, not a feature
    R-12 multi-clinician — NON-GOAL from 07-strategy. Not deferred.
      Excluded. Reconsider trigger: a second segment is served.
```

---

# Anti-Example 3 — Behavior Two Engineers Would Build Differently

## ❌ Looks specified

```
R-04  GP review and approval
      The GP reviews the transcribed note and approves it. Once approved,
      the note is saved to the patient record. The system should handle
      this efficiently and provide appropriate feedback.
```

**Why it fails**

- **Apply the two-builder test.** Where does the review happen — in our product or in the records system? Can they edit, or only approve? What
  happens to a rejected note? Is approval reversible? Two engineers diverge at every one of those points.
- **"Efficiently" and "appropriate feedback"** are the banned vocabulary, and neither can be observed.
- **No resulting state.** What is now true that was not before?
- **Asking "is this clear?" will not detect the problem**, because the writer already knows what they meant.

## ✅ Passes

```
R-04  GP review and approval    Parent: P1    MUST

  Trigger      A transcribed draft is available for a consultation
  Input        The GP may edit any part of the draft text. No field is
               mandatory. Edits are free text.
  System       On approval: writes the final text to «records system» via
               «operation», records an audit entry (actor, timestamp,
               note id, "approved"), marks the draft as consumed.
  State after  The note exists in the patient record. The draft is
               retained «n» days then deleted (retention: 09-technology).
               The consultation is marked documented.
  User sees    The saved note as it appears in the record, with a
               confirmation naming the patient.

  Reversibility  Approval is NOT reversible from our product. Corrections
                 happen in the records system, per its own audit rules.
                 Stated because it is the question two engineers would
                 answer differently.
  Rejection      The GP may discard a draft. The audio is retained until
                 the retention period expires. A discarded draft is
                 recorded in the audit trail.
```

---

# Anti-Example 4 — Happy Path Only

## ❌ Looks specified

```
R-02  Secure upload
      Audio recorded during the consultation is uploaded to the platform
      over an encrypted connection and queued for transcription.
      Acceptance: audio uploads successfully and appears in the queue.
```

**Why it fails**

- **Roughly half specified**, and the missing half is where products fail in front of real users.
- **The five edge categories are absent.** Empty, invalid, failure, permission, limit — and "not applicable — reason" would be acceptable
  where one genuinely does not apply. A blank is indistinguishable from not having considered it.
- **The data-loss position is unstated**, which is the single most consequential edge answer in most products and is never written down until
  it happens.

## ✅ Passes

```
R-02  Secure upload    Parent: P1    MUST

  EDGE CATEGORIES
  Empty       No audio captured (recording never started). The GP sees
              "No recording for this consultation" with the option to
              record now or write manually. Not an error.
  Invalid     Audio under 5 seconds, or silent. Rejected with "This
              recording appears empty — record again or write manually."
              The audio is retained until the GP dismisses it.
  Failure     Upload cannot complete (connection lost mid-transfer).
              THE AUDIO IS RETAINED LOCALLY and retried automatically.
              The GP sees "Waiting to upload — 1 recording". They may
              continue working.
  Permission  A GP attempting to access another practice's recording sees
              "Not found" — per 09-technology's disclosure policy. Not
              "not permitted", which would confirm existence.
  Limit       Recording exceeds «n» minutes: upload proceeds; the GP is
              warned that transcription may take longer.
              Offline for more than «n» hours: the GP is notified that
              recordings are queued and unsent.

  DATA-LOSS POSITION — stated plainly
    Audio held locally and not yet uploaded is lost if the device is lost
    or cleared. This is the only point at which clinical content can be
    lost, and the mitigation is that the GP can see unsent recordings at
    all times. 10-execution must surface this state; it is not optional.
```

---

# Anti-Example 5 — Criteria That Cannot Fail

## ❌ Looks specified

```
Acceptance criteria
  - Upload works reliably and quickly
  - The interface is intuitive for clinicians
  - Transcription quality is high
  - The system handles errors gracefully
  - Performance is acceptable under normal load
```

**Why it fails**

- **Every one contains a banned word.** Reliably, intuitive, high, gracefully, acceptable — none can be observed, and no plausible observation
  could fail any of them.
- **A criterion that cannot fail is not a criterion.** It is a hope in checkbox form.
- **For the transcription capability, an average would also be insufficient** — a statistical bar accepts total failure on a recognizable
  subset, which is why `14-ai-systems` requires per-instance criteria too.

## ✅ Passes

```
R-02 ACCEPTANCE
  Given a 10-minute recording and a connection of «n» Mbps,
  when the GP ends the consultation,
  then the upload completes within 90 seconds.
  (90s from 09-technology's budget: the GP has ~2 min between patients.)

  Given the connection drops at 50% of an upload,
  when connectivity returns,
  then the upload resumes and completes without the GP acting.

  Given an upload is pending,
  when the GP opens the product,
  then the count of unsent recordings is visible on the first screen.

R-03 TRANSCRIPTION — both kinds required
  STATISTICAL
    Given 200 real consultation recordings from the golden set,
    when transcribed by the service,
    then ≥95% are judged clinically accurate by a «domain expert».
    (Judged by a clinician. The build team cannot assess clinical
     correctness, and their confidence is not evidence.)

  PER-INSTANCE — always true, every time
    The draft is always editable before saving.
    The draft always displays the recording it came from.
    The draft can always be discarded.
    Output never writes to the record without explicit GP approval.
    (These are ordinary requirements, testable conventionally — and most
     of the real safety lives here rather than in the 95%.)
```

---

# The Pattern Across All Five

| Failure | How it presents |
| --- | --- |
| Orphan requirement | A rationale where a parent problem belongs |
| Everything a MUST | Twelve MUSTs, one of them contradicting a non-goal |
| Two-builder failure | Prose that reads clearly and answers nothing |
| Happy path only | One acceptance line, no edge categories, no data-loss position |
| Unfailable criteria | Reliably, intuitive, high, gracefully, acceptable |

---

> **Resource Note**
>
> Every one of these reads well. The orphan's rationale is the most
> persuasive paragraph in the document.
>
> That is why the rule is deletion, and why the boundary check is a list
> comparison rather than a judgment.
