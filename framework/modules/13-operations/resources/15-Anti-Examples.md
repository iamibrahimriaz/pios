---
Title: Anti-Examples
Module: 13-operations
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show operations plans nobody could execute at 3am, and ceilings absorbed rather than reported.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 13-operations/core/06-Framework.md
Outputs:
  - Recognition of unrunnable runbooks and unstaffed commitments
Related Modules:
  - 06-business
  - 09-technology
Tags:
  - Operations
  - Anti Examples
  - Reference
---

# Anti-Examples

---

# Overview

> Most blueprints stop at launch. That is why so many products become unmaintainable in month three.

Each example below is what a plan looks like when it was written by someone who will not be the one woken up.

---

# Anti-Example 1 — Commitments Nobody Can Staff

## ❌ Looks like a plan

```
Support model
  Channels     email, in-app chat, phone
  Hours        24/7
  Response     P1 within 1 hour, P2 within 4 hours, P3 within 24 hours
  Escalation   to the on-call engineer
  Expected volume  approximately 2 tickets per practice per month
```

**Why it fails**

- **A single operator cannot provide 24/7 one-hour response.** This is not a commitment; it is a sentence. `06-business` established the operator
  is one person.
- **Three channels for one person** triples the places a request can arrive and be missed.
- **"The on-call engineer"** does not exist. Escalation points at a role nobody holds.
- **Volume is presented as a plan.** It is a forecast, and the staffing conclusion depends entirely on it.
- **No burden analysis**, so no ticket is traced to a fixable product defect.

## ✅ Passes

```
MOVE 1 — SUPPORT

  COMMITMENTS  [verified: operator]
    Channel   email only. One place, monitored.
    Hours     weekday 08:00–18:00 «timezone»
    Response  S1 within 2 hours during hours · S2 same working day ·
              S3 within 3 working days
    Out of hours  no commitment. Stated to the customer in writing.
    Absence   if the operator is unavailable for more than one working day,
              customers are notified proactively and transcription pauses.
              A rota of one is not a rota, and pretending otherwise breaks
              on the first incident.

  FORECASTS  [assumption — the staffing conclusion depends on these]
    ~3 tickets/practice/month at launch, falling as the product settles.
    At 24 practices: ~72/month. At 15 minutes each: 18 hours/month.
    → Cost-Model.md prices this. Sensitivity run, because it is a guess.

  BURDEN → PRODUCT CHANGE   (the reframe that makes this move useful)
    Expected burden                    Product change that removes it
    "Where is my note from yesterday?" the overnight gap is unclear in the
      — anticipated most common         interface. 10-execution: state the
                                        expected time in the empty state
    "It says waiting to upload"         the unsent-recordings indicator is
                                        specified but its meaning is not.
                                        Add a one-line explanation
    "Can I edit after approving?"        R-04's irreversibility is a rule
                                        the interface does not show. Make
                                        it visible before approval
    → all three to the roadmap. A burden accepted without this question
      becomes a permanent staffing line paid for a fixable defect.

    PERMANENT, and why
      Onboarding a new practice: manual account creation and the first
      note walkthrough. ~90 minutes. Correct — it is how trust is
      established in this segment, and 06-business prices it.
```

---

# Anti-Example 2 — Severity by Component

## ❌ Looks like a plan

```
Severity levels
  S1  Database or API outage
  S2  Degraded performance, background job failures
  S3  UI bugs, cosmetic issues
  S4  Feature requests
```

**Why it fails**

- **Every level requires knowing the cause**, which is exactly what is unknown when the incident starts. Component-based severity produces an
  argument during the incident.
- **A user unable to save a note is unclassifiable** until someone diagnoses why.
- **"Background job failures" at S2** — the retention job is a compliance mechanism. Its failure is a legal exposure, not degraded performance.
- **Data loss appears nowhere**, and `09-technology` was required to state the data-loss position.

## ✅ Passes

```
MOVE 2 — GRADE   (by user impact; assignable in ten seconds by anyone)

  S1  A GP cannot record a consultation, OR a note cannot reach the
      patient record, OR ANY CLINICAL CONTENT IS LOST.
      Data loss is ALWAYS S1 — 09-technology's data-loss position states
      that locally-held audio not yet uploaded is the only such point.
      First response 2 hours (in hours) · Resolve same day
      Who is woken: the operator. There is nobody else. Stated.

  S2  Notes are delayed beyond the next working day, OR a GP cannot
      approve a draft.
      First response same working day · Resolve within 2 working days

  S3  A GP is inconvenienced but the note still reaches the record.
      First response 3 working days

  COMPLIANCE FAILURES are not on this scale.
    The retention job failing, an erasure not completing, an audit entry
    missing — each is a DEFECT with a legal dimension, handled immediately
    regardless of user impact. 12-metrics holds them as non-negotiables
    whose breach is not a trade-off.

  THE TEN-SECOND TEST
    "A GP called; their note from Monday isn't in the record."
    → S1. Assigned without diagnosis, by whoever answered.
```

---

# Anti-Example 3 — "Investigate the Issue"

## ❌ Looks like a plan

```
Runbook: transcription backlog

1. Investigate the cause of the backlog
2. Check the logs for errors
3. Restart the affected service if needed
4. Monitor to confirm resolution
5. Escalate if the issue persists
```

**Why it fails**

- **Apply the 3am test:** could someone who did not build this follow it, alone, half awake, with nobody to ask? No. Step 1 means "work it out",
  which is precisely what they cannot do.
- **"Check the logs"** — which logs, where, for what string, over what period?
- **"Restart if needed"** — needed based on what observation, and what should happen afterwards?
- **No access requirements**, and the most common 3am blocker is a credential.
- **No recovery verification**, so "done" means "I ran the steps".
- **No "do not do" line.** Every system has a tempting action that makes it worse.

## ✅ Passes

```
RUNBOOK — Transcription backlog

  TRIGGER  Alert "transcription queue age > 14 hours", or a GP reports a
           note missing from the previous working day.

  ACCESS NEEDED — check this first
    «admin console» login — credentials in «secret store», entry «name»
    Database read access — «connection», same store
    If you cannot obtain either: stop and contact «operator» directly.
    A recovery blocked on access nobody has is the avoidable failure.

  STEPS                      EXPECT                    IF DIFFERENT
  1 Open «console» → Queue   A count and an oldest-     Console unreachable
                             item timestamp             → go to step 6
  2 Note the oldest          A timestamp within         Older than 24h →
    item's age               24 hours                   this is S1, not S2
  3 Check whether any        A named reviewer, or       Nobody assigned →
    reviewer is assigned     "unassigned"               go to step 5
  4 Run «query» to count     A number matching the      Mismatch → the queue
    unprocessed rows         console count              view is stale; trust
                                                        the query
  5 Assign yourself and      The count decreases as     No decrease after
    process the oldest       you work                   30 min → step 6
    items first
  6 ESCALATE: contact        —                          —
    «operator» by phone.
    Number in «location».

  RECOVERY VERIFICATION — not optional
    Queue oldest-item age below 8 hours, AND the GP who reported it
    confirms the note is in their record. Both, or it is not resolved.

  DO NOT
    Do not clear or purge the queue to make the alert stop. Each item is a
    recorded consultation, and clearing it destroys clinical content with
    no recovery. This is the tempting action, and it is attempted by
    somebody helpful.
```

---

# Anti-Example 4 — Compliance as a State

## ❌ Looks like a plan

```
Compliance
  We are GDPR compliant. Data is encrypted, access is controlled, audit
  logging is enabled, and we have a data processing agreement in place.
  An annual review is planned.
```

**Why it fails**

- **"We are compliant" is a state**, and `09-technology` forbids the claim. Compliance is a cadence.
- **Not one obligation names an owner or evidence.** A mechanism that exists and is never exercised satisfies an auditor for exactly as long as
  nobody looks.
- **"An annual review is planned"** has no owner, no date and no output.
- **The erasure-versus-backup blocker `09-technology` surfaced is absent**, and it was unresolved.
- **Access review, restore rehearsal and audit-log review are missing** — all recurring, all obligations.

## ✅ Passes

```
MOVE 5 — COMPLY   (schedule, owner, evidence, location)

  Obligation             Cadence    Owner      Evidence produced
  Access review —        Quarterly  «operator» signed list of who has
  who can read customer                        access, with date, in
  data                                         «location»
  Restore rehearsal      Quarterly  «operator» measured restore time and a
                                               completeness check.
                                               restore_tested: «date»
  Retention job          Daily,     «operator» job success log. ALERTED ON
  verification           automated             ABSENCE OF SUCCESS — a
                                               stopped job raises no error
  Erasure requests       On request «operator» a record per request, with
  completed                                    the stores reached
  Audit log review        Monthly    «operator» a note of anomalies found,
                                               or none, dated
  Dependency scanning     Every      automated pipeline results, retained
                          build
  Data processing         Annually   «operator» the current agreement, and
  agreement review                             its review date

  ⚠ CARRIED FROM 09-TECHNOLOGY — STILL UNRESOLVED
    Erasure must complete within «n» days; backups are held 90 days.
    OWNER «operator». Needs legal input. BLOCKS LAUNCH.
    Recorded here because this module runs obligations, and this one has
    no mechanism to run. It has not been softened into a risk.

  ALERT HYGIENE  (also this move)
    Alert                      Threshold        Person      Runbook
    Queue age                  > 14 hours       «operator»  Transcription
                                                            backlog
    Retention job absent       no success in    «operator»  Retention job
                               26 hours                     failure
    Cross-practice access      any              «operator»  Security
    succeeded                                               incident
    Upload failure rate        > 5% over 1h     «operator»  Upload failures

    DELETED: three alerts that fired in testing with no action available.
    An alert nobody acts on is deleted, not ignored — a tolerated alert
    teaches the team to tolerate all of them.

    NOT ALERTED ON, deliberately: individual upload failures (retried
    automatically; the rate is what matters).
```

---

# Anti-Example 5 — Absorbing the Ceiling

## ❌ Looks like a plan

```
Cost model
  Infrastructure  £4/user/month
  Support         £2/user/month (estimated, expected to decrease)
  Total           £6/user/month against a £20 ceiling. Comfortable margin.
```

**Why it fails**

- **Support at £2 contradicts the plan's own forecast.** 18 hours/month across 24 practices at any real rate exceeds this several times over.
- **"Expected to decrease" is the assumption being adjusted to make the arithmetic pass** — and `Support-Model.md` requires a named product
  change for any reduction, not an expectation.
- **Compliance operations are missing entirely.** Seven recurring obligations with an owner is real recurring time.
- **The operator's own hours are unpriced**, which is the standard omission and the largest cost in most small products.

## ✅ Passes

```
MOVE 6 — COST   (the third and last arithmetic check)

  Per user per month, at 24 practices
    Infrastructure                          £«x»  [09-technology, dated]
    Inference                               £0    service-delivered MVP
    Support: 18 hours/month ÷ 24 practices
      × «£x»/hour operator rate             £«x»  [assumption: volume]
    TRANSCRIPTION LABOR — the service itself
      «n» notes/practice/month × «n» min
      × «£x»/hour                           £«x»  [the dominant cost]
    Compliance operations: «n» hours/month
      ÷ 24 × «£x»/hour                      £«x»
    ─────────────────────────────────────────────
    TRUE COST TO SERVE                      £«x»/user/month

    Against 06-business's ceiling of £20/user/month: «verdict».

  If it exceeds the ceiling — and for a service-delivered product with
  human transcription it plausibly does — THIS IS A REGRESS:
    → 06-business for the price (£2,400/yr may be too low)
    → 07-strategy for the scope
    NOT absorbed by assuming support takes less time than this plan just
    stated.

  LOAD-BEARING ASSUMPTION: transcription minutes per note.
    It is the dominant cost, it is unmeasured, and it is the whole verdict.
    Sensitivity: at 8 min/note «figure» · at 20 min/note «figure».

  THE RATE QUESTION
    Throughput ceiling: one operator can transcribe «n» notes/day.
    At 24 practices × «n» notes/month that is «n»% of capacity.
    → 07-strategy's transition trigger (15 practices) is not arbitrary.
      It is where this ceiling binds.
```

---

# The Pattern Across All Five

| Failure | How it presents |
| --- | --- |
| Unstaffable commitments | 24/7 one-hour response from one person; escalation to a role nobody holds |
| Severity by component | Levels requiring the cause, which is unknown at the start |
| "Investigate the issue" | Steps that mean "work it out", no access list, no verification |
| Compliance as a state | "We are compliant", no owner, no cadence, no evidence |
| Absorbed ceiling | Support priced below the plan's own forecast, "expected to decrease" |

---

> **Resource Note**
>
> The honest support model says "weekday hours, email only, and here is
> what happens when I am unavailable."
>
> That is worth more than a coverage table, because it is the only version
> that survives the first incident.
