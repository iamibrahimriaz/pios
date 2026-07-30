---
Title: Examples
Module: 12-metrics
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show a metric set that passes the computation test and the privacy check.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 12-metrics/core/06-Framework.md
Outputs:
  - A reference metrics plan
Related Modules:
  - 09-technology
  - 11-growth
Tags:
  - Metrics
  - Examples
  - Reference
---

# Examples

---

# Overview

The run continues. Note that most targets are absent, one metric deliberately has none, and the analytics decision is to use the operational
database rather than a third-party service.

---

# The Worked Metrics Plan

```
METRICS PLAN — «Consultation notes», service-delivered MVP

MOVE 1 — CHOOSE

  NORTH STAR: consultations documented before the next working day.

  Vanity check: CAN FALL. If transcription slows, if GPs stop approving,
    if quality drops and they revert to the paper pad, it falls. A rate
    over a population, not a cumulative count.

  Two rejected alternatives, with reasons
    Total notes processed — cumulative, cannot fall, measures elapsed time.
      It would rise during a decline.
    Revenue — a consequence of a north star. It measures what we received
      rather than what the GP got, and it moves last.

  GAMING QUESTION
    Transcribing fragments quickly rather than notes properly.
    Counting drafts as documented before a GP approves them.
    Encouraging GPs to record trivial consultations needing no note.
    → each becomes a counter-metric in Move 4.

MOVE 2 — DEFINE   (five parts, every metric)

  M1  Documentation rate — NORTH STAR
    Numerator    consultations with state='documented' where documented_at
                 is within one working day of occurred_at
    Denominator  consultations with state != 'abandoned', same period
    Window       rolling 7 days
    Population   practices past activation, excluding internal and test
    Exclusions   practices in their first 7 days; GP-abandoned consultations
    Source       consultation_created, note_approved
    Confidence   definition HIGH (a decision) · target LOW (a prediction)

  M2  Approval latency
    Numerator    median hours from transcript_ready to note_approved
    Denominator  n/a — a duration, not a rate. Stated so nobody presents it
                 as a percentage
    Window       rolling 7 days · Population as M1
    Source       transcript_ready, note_approved

  M3  Paper-pad return rate
    Numerator    practices whose weekly recording count fell below 60% of
                 their own trailing 4-week average
    Denominator  practices past activation
    Window       weekly vs a 4-week trailing baseline · Population as M1
    Source       consultation_created

  M4  Transcription accuracy
    Numerator    golden-set cases judged clinically accurate by a clinician
    Denominator  200 golden-set cases
    Window       per evaluation round · Population the golden set
    Source       manual evaluation, not events
    Note: this is the one metric with a real baseline coming (M3 milestone)

MOVE 3 — SPLIT

  LEADING — actionable, and each names what it predicts with its basis
    M2 approval latency → predicts churn. Basis: 11-growth precursor 3,
       drafts sitting unapproved indicate disengagement [inferred]
       Lead time UNKNOWN — the first cohorts establish it
    M3 paper-pad return → predicts churn. Basis: 11-growth precursor 2,
       the workaround returning is the clearest signal [inferred]
       Lead time UNKNOWN

  LAGGING — confirm only, kept off the weekly view
    Revenue — reflects decisions from months earlier
    Churn over a period — the customers already decided
    Actual CAC per channel — measurable only after a cohort converts
    RE-MEASURED PROBLEM COST — the most valuable and least used.
      04-problem's baseline was 60–120 min/day [assumption]. Re-measuring
      it after 3 months of use is the only way to test 06-business's
      50% capture-share claim.

MOVE 4 — GUARD

  Gaming behavior             Counter-metric               Threshold
  Fragments not notes         median words/note vs the     not below 70%
                              4-week baseline              of baseline
  Drafts counted unapproved   share of documented notes    100% — any
                              with an approval audit entry shortfall is a
                                                           DEFECT
  Trivial consultations       share of notes discarded     not above 15%
                              without approval

  NON-NEGOTIABLES from 09-technology — breach is a defect, not a trade-off
    Successful cross-practice access attempts        0
    Regulated fields in analytics properties          0
    Consultations past retention, not deleted         0
    Restore rehearsals overdue                        0

MOVE 5 — TARGET

  Metric  Baseline                    Target
  M1      NONE — no product exists    «figure» [assumption: needs
                                      validation]. Basis: 04-problem says
                                      notes are currently completed after
                                      hours, so the present rate within one
                                      working day is low but unmeasured.
                                      Attributed: operator.
  M2      NONE                        No target. Diagnostic. A target on a
                                      metric nobody would act on is noise
  M3      NONE                        No target. A signal with a response
  M4      The human service's rate,   ≥95% clinician-judged — from
          measured at M3              07-strategy's transition trigger

  NO IMPORTED BENCHMARKS. A published median describes a population this
  product is not in, with definitions nobody publishes.

  FIRST REAL BASELINE: milestone M2, four practices, one week.
  At that point M1 stops being an assumption.

MOVE 6 — INSTRUMENT   (the only move that becomes code)

  consultation_created                                     ships in M1
    Trigger     a consultation row is created
    Properties  consultation_id (uuid) · practice_id (uuid) ·
                occurred_at (timestamp)
    Feeds       M1 denominator, M3
    NOT sent    patient_ref, patient_age, presenting complaint — REGULATED

  transcript_ready                                         ships in M1
    Properties  consultation_id · ready_at (timestamp)
    Feeds       M2

  note_approved                                            ships in M1
    Trigger     state transitions to 'documented'
    Properties  consultation_id · practice_id · approved_at ·
                word_count (integer) · was_edited (boolean)
    Feeds       M1 numerator, words-per-note counter-metric
    NOT sent    note text, excerpts, patient identifiers

  note_discarded                                           ships in M2
    Properties  consultation_id · discarded_at
    Feeds       the discard-rate counter-metric

  COVERAGE, both directions
    Metric → event: M1, M2, M3 and both counter-metrics all have sources.
      M4 is manual, stated.
    Event → metric: every event feeds a named metric. No orphans.

  THE MECHANICAL PRIVACY CHECK
    09-technology §3 regulated columns: patient_ref · audio content ·
      note text · presenting complaint · patient_age
    Compared against every property above: NO OVERLAP ✓
    A list comparison, not a judgment. Any overlap fails the gate.

  IDENTITY RESOLUTION
    practice_id and clinician_id are issued at account creation, which the
    operator performs during the sale. No anonymous-to-known stitching is
    required, because there is no self-serve signup.
    Stated explicitly — its absence would otherwise make every cohort
    metric uncomputable.

  DELIBERATELY NOT INSTRUMENTED
    Page views and navigation. No metric consumes them, and each property
    is a privacy surface. Revisit if a specific question requires them.

  WHERE COMPUTED
    The operational database, queried directly. No third-party analytics
    service in phase one.
    M1–M3 are all computable from records the product already holds
    lawfully. A third-party service would place clinical behavioral data in
    another jurisdiction, requiring assessment under 02-market Frame 2 — a
    cost with no benefit at this volume.
    Reporting queries run against a read path; 09-technology named the
    consultation-list aggregate as the first bottleneck.

GATE
  ✓ Exactly one north star, with the reasoning
  ✓ Every metric has a definition, source and target — or a stated reason
    for having no target
  ✓ Leading indicators distinguished from lagging, with predictive claims
    and their tags
  ✓ Instrumentation specified at event level, per milestone
```

---

# Example 1 — A North Star That Can Fall

## ❌ Poor

```
North star: total notes processed. Target 10,000 by month twelve.
```

## ✅ Good

```
North star: consultations documented before the next working day.
Vanity check: CAN FALL — if transcription slows, if GPs stop approving, if
they revert to the paper pad.
Rejected: total notes processed — it would rise during a decline.
```

**Why.** A cumulative count measures elapsed time. The rejected-alternatives note is the actual content of the move, because it is what makes the
choice reviewable a year later.

---

# Example 2 — The Computation Test Passed

## ❌ Poor

```
Active practices: practices using the product.
```

## ✅ Good

```
Numerator, denominator, window, population, exclusions, source — all five
stated, plus the events it is computed from.
```

**Why.** "Active users" fails all five, and everyone believes they know what it means. Two analysts given the passing definition produce the same
number.

---

# Example 3 — A Metric With No Target, Deliberately

## ❌ Poor

```
Approval latency target: under 12 hours.
```

## ✅ Good

```
No target. Diagnostic only. A target on a metric nobody would act on is
noise with a threshold.
```

**Why.** Not every metric needs one, and inventing targets for diagnostics dilutes the ones that matter. The lead time is also unknown, so any
threshold would be arbitrary.

---

# Example 4 — The Privacy Check as Arithmetic

## ❌ Poor

```
We will not send sensitive data to analytics.
```

## ✅ Good

```
09-technology §3 regulated columns: patient_ref · audio · note text ·
presenting complaint · patient_age
Every event property compared: NO OVERLAP ✓
A list comparison, not a judgment.
```

**Why.** An intention is not a control. The mechanical check is what makes the gate criterion checkable, and the framework applies the same
regulated-column list in modules 09, 12, 13 and 14.

---

# Example 5 — Choosing the Operational Database

## ❌ Poor

```
Analytics: «third-party service» for dashboards, funnels and cohort
analysis.
```

## ✅ Good

```
The operational database, queried directly.
M1–M3 are computable from records already held lawfully. A third-party
service would place clinical behavioral data in another jurisdiction,
requiring Frame 2 assessment — a cost with no benefit at this volume.
```

**Why.** Most early metrics are computable from operational data, and a second store of user behavior is a compliance decision rather than a
tooling one.

---

> **Resource Note**
>
> Three of four metrics have no target and one has none by design.
>
> The plan still passes, because it names the milestone that produces the
> first baseline — which turns an admitted weakness into a schedule.
