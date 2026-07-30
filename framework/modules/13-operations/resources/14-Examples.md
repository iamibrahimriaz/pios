---
Title: Examples
Module: 13-operations
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show an operations plan a solo operator can actually run, and a cost check that regresses.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 13-operations/core/06-Framework.md
Outputs:
  - A reference operations plan
Related Modules:
  - 06-business
  - 09-technology
Tags:
  - Operations
  - Examples
  - Reference
---

# Examples

---

# Overview

The run continues, and this is where the arithmetic finally closes. The plan ends by **regressing** — the true cost to serve exceeds the ceiling
`06-business` set, and the module reports it rather than absorbing it.

---

# The Worked Operations Plan

```
OPERATIONS PLAN — «Consultation notes», service-delivered MVP

MOVE 1 — SUPPORT
  COMMITMENTS  [verified: operator]
    Channel   email only. One place, monitored
    Hours     weekday 08:00–18:00 «timezone»
    Response  S1 2 hours in-hours · S2 same working day · S3 3 working days
    Out of hours  no commitment, stated to the customer in writing
    Absence   over one working day unavailable → customers notified
              proactively, transcription pauses.
              A rota of one is not a rota, and saying so is the honest
              version of a coverage table.

  FORECASTS  [assumption]
    ~3 tickets/practice/month at launch → 72/month at 24 practices
    × 15 min = 18 hours/month. Priced in Move 6; sensitivity run.

  BURDEN → PRODUCT CHANGE
    "Where is my note from yesterday?"  → the overnight gap is unclear.
      10-execution: state the expected time in the empty state
    "It says waiting to upload"          → the indicator exists; its
      meaning does not. Add one line
    "Can I edit after approving?"        → R-04's irreversibility is a rule
      the interface never shows. Make it visible before approval
    → all three to the roadmap.

    PERMANENT: onboarding a practice, ~90 min manual. Correct — it is how
    trust is established in this segment, and 06-business prices it.

MOVE 2 — GRADE   (user impact; assignable in ten seconds)
  S1  A GP cannot record, OR a note cannot reach the record, OR ANY
      CLINICAL CONTENT IS LOST.
      Data loss is always S1. 09-technology's position: locally-held audio
      not yet uploaded is the only such point.
      Response 2h in-hours · resolve same day · woken: the operator, and
      there is nobody else. Stated.
  S2  Notes delayed beyond the next working day, OR a draft cannot be
      approved. Same working day · resolve in 2 working days.
  S3  Inconvenience, but the note still reaches the record. 3 working days.

  COMPLIANCE FAILURES are off this scale: a failed retention job, an
  incomplete erasure, a missing audit entry. Each is a defect with a legal
  dimension, handled immediately. 12-metrics holds them as non-negotiables.

MOVE 3 — RESPOND
  Detect → Triage → Communicate → Mitigate → Resolve → Review

  COMMUNICATE — named, because users experience silence as a worse incident
    Who   the operator
    When  within 30 minutes of an S1 being confirmed
    How   email to affected practices, from a pre-written template
    Template lives in «location». Pre-written because at the moment it is
      needed nobody has time to compose it.

  MITIGATE, separately from resolve
    Transcription backlog → notify practices and transcribe the oldest
      first. Stops the harm without diagnosing the cause.
    Upload failures → tell GPs to write manually for now; R-02's manual
      path is a requirement precisely so this mitigation exists.

  REGULATORY NOTIFICATION
    A breach involving clinical data: «n» hours from discovery
    [«citation», 02-market Frame 2].
    The clock starts at discovery. Who starts it: the operator.
    A deadline nobody knows is a deadline that gets missed, and the
    failure is legal rather than technical.

  REVIEW — with an output, or it was a conversation
    Every S1 and S2 produces one of: a runbook change, an alert change, or
    a roadmap item. Also the point where Move 1's burden question is asked
    again.

MOVE 4 — WRITE   (the 3am standard; one runbook shown)

  RUNBOOK — Transcription backlog
  TRIGGER  alert "queue age > 14 hours", or a GP reports a missing note

  ACCESS NEEDED — first, because a credential is the usual 3am blocker
    «admin console» — credentials in «secret store», entry «name»
    Database read — «connection», same store
    Cannot obtain either → stop, contact «operator» directly

  STEPS                     EXPECT                   IF DIFFERENT
  1 Open «console» → Queue  count + oldest timestamp Unreachable → step 6
  2 Note oldest item age    within 24 hours          Older → this is S1
  3 Check reviewer assigned a name, or "unassigned"  Unassigned → step 5
  4 Run «query», count      matches the console      Mismatch → trust the
    unprocessed rows                                 query; console stale
  5 Assign yourself,        count decreases          No decrease in 30 min
    oldest first                                     → step 6
  6 ESCALATE: phone «operator», number in «location»

  RECOVERY VERIFICATION
    Queue oldest under 8 hours AND the reporting GP confirms the note is in
    their record. Both, or it is not resolved.

  DO NOT
    Do not clear or purge the queue to stop the alert. Each item is a
    recorded consultation; clearing destroys clinical content with no
    recovery. This is the tempting action.

  Other runbooks, same standard: retention job failure · upload failure
  rate · restore · suspected cross-practice access · erasure request.

MOVE 5 — COMPLY   (cadence, owner, evidence, location)
  Obligation                Cadence     Owner       Evidence
  Access review             Quarterly   «operator»  signed list, dated
  Restore rehearsal         Quarterly   «operator»  measured time +
                                                    completeness check
  Retention job verified    Daily, auto «operator»  success log, ALERTED
                                                    ON ABSENCE
  Erasure completed         On request  «operator»  record per request,
                                                    stores reached
  Audit log review          Monthly     «operator»  anomalies or none,
                                                    dated
  Dependency scanning       Per build   automated   pipeline results
  Processing agreement      Annually    «operator»  current agreement +
                                                    review date

  ⚠ CARRIED FROM 09-TECHNOLOGY, STILL UNRESOLVED
    Erasure within «n» days vs 90-day backup retention.
    OWNER «operator». Needs legal input. BLOCKS LAUNCH.
    Not softened into a risk. This module runs obligations, and this one
    has no mechanism to run.

  ALERT HYGIENE
    Alert                     Threshold      Person      Runbook
    Queue age                 > 14 hours     «operator»  backlog
    Retention job absent      no success 26h «operator»  retention failure
    Cross-practice access OK  any            «operator»  security incident
    Upload failure rate       > 5% over 1h   «operator»  upload failures
    DELETED: three that fired in testing with no available action.
    NOT ALERTED: individual upload failures — retried; the rate matters.

MOVE 6 — COST   (the third and last arithmetic check)
  Per user per month at 24 practices
    Infrastructure                        £«x»  [09-technology, dated]
    Inference                             £0    service-delivered
    Support 18h ÷ 24 × «£x»/hr            £«x»  [assumption: volume]
    TRANSCRIPTION LABOR                   £«x»  ← the dominant cost
      «n» notes/practice/month × «n» min
    Compliance ops «n»h ÷ 24 × «£x»/hr    £«x»
    ───────────────────────────────────────────
    TRUE COST TO SERVE                    £«x»/user/month
    Ceiling from 06-business              £20/user/month

  ⚠ THE CEILING IS EXCEEDED. This is a REGRESS, not an adjustment.
    → 06-business: £2,400/yr may be too low for a human-delivered service
    → 07-strategy: or the scope changes
    Recommendation: raise the price. 06-business's value calculation
    supports it — the constraint was the free incumbent, not the value.
    Operator decision.

  LOAD-BEARING ASSUMPTION: transcription minutes per note. Dominant,
    unmeasured, and it is the whole verdict.
    Sensitivity: 8 min → «figure» · 20 min → «figure».

  THROUGHPUT CEILING
    One operator transcribes «n» notes/day. At 24 practices that is «n»% of
    capacity. 07-strategy's transition trigger at 15 practices is where
    this binds — it was not arbitrary.

THE ROTA QUESTION, answered
  On call: the operator. Weekday hours. Best effort.
  Sustainable: for a defined period, not indefinitely.
  When unavailable: customers notified, transcription pauses, S1 response
  is not available. Written down, and told to the customer at the sale.

GATE
  ✓ Support channel and response expectation defined
  ✓ Incident and escalation path documented
  ✓ Compliance obligations mapped to an owner and a cadence
  ✓ Running cost estimated at launch scale — and it regresses
```

---

# Example 1 — The Support Burden as a Product Signal

## ❌ Poor

```
Expected volume: 3 tickets per practice per month. Staff accordingly.
```

## ✅ Good

```
"Where is my note from yesterday?" — the overnight gap is unclear in the
interface. Product change: state the expected time in the empty state.
→ roadmap.
PERMANENT: 90-minute manual onboarding. Correct, and priced.
```

**Why.** The most common support request is usually a design defect with a queue attached. Accepting it without asking produces a permanent
staffing line paid for something fixable.

---

# Example 2 — A Step Someone Can Follow

## ❌ Poor

```
1. Investigate the cause of the backlog
2. Check the logs
```

## ✅ Good

```
ACCESS NEEDED FIRST — «console» credentials in «store», entry «name»
1 Open «console» → Queue | EXPECT count + oldest timestamp | IF unreachable
  → step 6
DO NOT clear the queue to stop the alert — each item is a recorded
consultation.
```

**Why.** Access at the top because a credential is the usual 3am blocker; three columns so a stranger can proceed without diagnosing; and the
"do not do" line because every system has a tempting action that makes it worse.

---

# Example 3 — Compliance as a Cadence

## ❌ Poor

```
We are GDPR compliant. An annual review is planned.
```

## ✅ Good

```
Access review · quarterly · «operator» · signed list, dated, in «location»
Restore rehearsal · quarterly · «operator» · measured time + completeness
Retention job · daily, automated · ALERTED ON ABSENCE OF SUCCESS
```

**Why.** Being compliant and being able to *show* you were compliant are different achievements, and only the second survives an audit. The
absence-alerting matters because a stopped job raises no error.

---

# Example 4 — Reporting the Breach Instead of Absorbing It

## ❌ Poor

```
Total £6/user/month against a £20 ceiling. Comfortable margin. Support
costs are expected to decrease as the product matures.
```

## ✅ Good

```
⚠ THE CEILING IS EXCEEDED. This is a REGRESS.
→ 06-business for the price, or 07-strategy for the scope.
Recommendation: raise the price — the value calculation supports it; the
constraint was the free incumbent, not the value. Operator decision.
Load-bearing assumption: transcription minutes per note. Unmeasured.
```

**Why.** The check exists to force a decision. Absorbing it by assuming support takes less time than the plan just stated is the failure it was
written against — and it is individually defensible every time it happens.

---

# Example 5 — The Rota Question Answered Honestly

## ❌ Poor

```
Escalation: to the on-call engineer.
```

## ✅ Good

```
On call: the operator. Weekday hours. Best effort.
When unavailable: customers notified, transcription pauses, S1 response is
not available. Written down, and told to the customer at the sale.
```

**Why.** For a solo operator this is the most important section in the document. A coverage table nobody can staff is a promise that breaks
during the first incident, in front of the first customer.

---

> **Resource Note**
>
> This plan ends by regressing to modules 06 and 07, and by carrying an
> unresolved blocker that stops launch.
>
> That is the framework closing its own loop. The arithmetic was never
> complete until support and compliance had a schedule attached.
