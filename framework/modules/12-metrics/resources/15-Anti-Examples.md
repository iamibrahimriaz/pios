---
Title: Anti-Examples
Module: 12-metrics
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show metric sets that cannot be computed, cannot fall, or leak regulated data.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 12-metrics/core/06-Framework.md
Outputs:
  - Recognition of vanity metrics and uncomputable definitions
Related Modules:
  - 09-technology
  - 11-growth
Tags:
  - Metrics
  - Anti Examples
  - Reference
---

# Anti-Examples

---

# Overview

> A product measured by the wrong number gets worse on purpose.

Each example below produces a dashboard that looks like instrumentation and measures nothing usable.

---

# Anti-Example 1 — The Vanity North Star

## ❌ Looks measurable

```
North star metric: Total notes processed

Secondary metrics
  Total registered practices
  Cumulative hours saved
  Total recordings uploaded
Target: 10,000 notes processed by month twelve.
```

**Why it fails**

- **Apply the vanity check:** could this fall if the product got worse? No. Every one of these is cumulative and rises forever regardless of what
  happens. They measure elapsed time.
- **Three north stars is not one.** The purpose is to resolve disagreements; several relocate the argument.
- **"Cumulative hours saved" compounds an assumption.** It multiplies an unmeasured time-saving estimate by a growing count, and it can only
  increase.
- **The gaming question was never asked.** Notes processed rises if the service transcribes fragments, encourages more consultations to be
  recorded than reviewed, or counts drafts nobody approved.

## ✅ Passes

```
NORTH STAR
  Consultations documented before the next working day.

  Vanity check: CAN FALL. If transcription slows, if GPs stop approving,
  if quality drops and they revert to the paper pad — the number falls.
  It is a rate over a population, not a cumulative count.

  Two rejected alternatives, with reasons — this is the content of the move
    Total notes processed — rejected: cumulative, cannot fall, measures
      elapsed time. It would rise during a decline.
    Revenue — rejected: a consequence of a north star, not one. It measures
      what we received rather than what the GP got, and it moves last.

  GAMING QUESTION
    What would raise this without the product becoming more valuable?
      Transcribing fragments quickly rather than notes properly.
      Counting drafts as documented before a GP approves them.
      Encouraging GPs to record trivial consultations that need no note.
    → Each answer becomes a counter-metric in Move 4.
```

---

# Anti-Example 2 — Definitions Nobody Can Compute

## ❌ Looks measurable

```
Metrics
  Active practices      — practices using the product
  Engagement            — how frequently users interact
  Activation rate       — percentage of signups who activate
  Retention             — percentage of users who stay
  Note quality          — accuracy of transcriptions
```

**Why it fails**

- **Apply the computation test:** given only these, would two analysts produce the same number? No, on all five.
- **"Active practices" fails all five required parts.** No numerator, no denominator, no window, no population, no exclusions. It is the
  canonical example.
- **Internal accounts are not excluded**, and early on the operator's test practices are frequently the largest group in the data.
- **No sources named**, so each metric will be quietly replaced with whatever the tool can produce.

## ✅ Passes

```
M1  Documentation rate — THE NORTH STAR
  Numerator    consultations with state = 'documented' where
               documented_at is within one working day of occurred_at
  Denominator  consultations with state != 'abandoned' in the same period
  Window       rolling 7 days
  Population   practices past activation (first approved note), excluding
               internal and test practices
  Exclusions   practices in their first 7 days (no full window yet);
               consultations marked abandoned by the GP
  Source       events consultation_created, note_approved
  Confidence   DEFINITION high (a decision) · TARGET low (a prediction)

M2  Approval latency — leading indicator
  Numerator    median hours between transcript_ready and note_approved
  Denominator  n/a — this is a duration, not a rate. Stated, so nobody
               presents it as a percentage
  Window       rolling 7 days
  Population   as M1
  Predicts     churn. Basis: 11-growth's precursor 3 — drafts sitting
               unapproved indicate disengagement [inferred: no data yet]
  Lead time    UNKNOWN. The first cohorts will establish it.

M3  Paper-pad return rate — leading indicator, the strongest one
  Numerator    practices whose recording count fell below 60% of their own
               trailing 4-week average
  Denominator  practices past activation
  Window       weekly, compared to a 4-week trailing baseline
  Population   as M1
  Predicts     churn. Basis: 11-growth's precursor 2 — the workaround
               returning is the clearest signal available [inferred]
```

---

# Anti-Example 3 — No Counter-Metrics

## ❌ Looks measurable

```
We will track our north star weekly and optimize for growth. The team is
aligned on driving documentation rate as the primary objective.
```

**Why it fails**

- **The gaming answers exist and nothing guards them.** Without counter-metrics, an organization improves its primary number and degrades the
  product — and **every individual decision along the way looks defensible.**
- **"Optimize for growth"** invites exactly the degenerate behaviors the gaming question identified.
- **The non-negotiables from `09-technology` are absent.** Where a security or regulatory violation is observable in the metrics, it belongs here
  as a threshold whose breach is a defect rather than a trade-off.

## ✅ Passes

```
MOVE 4 — GUARD   (each counter-metric answers a gaming behavior)

  Gaming behavior              Counter-metric              Threshold
  Fragments transcribed fast   median words per note vs    not below 70%
  rather than notes properly   the 4-week baseline         of baseline
  Drafts counted before        share of documented notes    100% — any
  the GP approves them         with an approval audit       shortfall is a
                               entry                        DEFECT
  Trivial consultations        share of notes the GP        not above 15%
  recorded to raise the count  discards without approving

  NON-NEGOTIABLES from 09-technology — breach is a defect, not a trade-off
  Cross-practice access attempts that succeed          must be 0
  Regulated fields appearing in analytics properties   must be 0
  Consultations past their retention date, not deleted must be 0
  Restore rehearsals overdue                           must be 0

  These are not balanced against the north star. They are limits.
```

---

# Anti-Example 4 — Targets From Benchmarks

## ❌ Looks measurable

```
Targets
  Activation rate      60%   (industry standard for vertical SaaS)
  Monthly retention    97%   (SaaS benchmark)
  NPS                  50+   (best-in-class)
  Documentation rate   85%   (our goal)
```

**Why it fails**

- **Three imported benchmarks describing a population this product is not in**, measured with definitions nobody states.
- **No baseline for any of them**, and the framework's handling of that is explicit: say so, tag them, and name the milestone that produces the
  first real baseline.
- **"Our goal" is not attributed.** If the operator chose 85%, it carries their name; if nobody did, it is invented.
- **Definitions and targets are presented at the same confidence.** Definitions are decisions; targets are predictions.

## ✅ Passes

```
MOVE 5 — TARGET

  Metric              Baseline              Target
  Documentation rate  NONE — no product     [assumption: needs validation]
                      exists yet            «figure», basis: 04-problem's
                                            claim that notes are currently
                                            completed after hours, i.e. the
                                            current rate within one working
                                            day is effectively unknown but
                                            low. Attributed: operator.
  Approval latency    NONE                  No target. Diagnostic only —
                                            a target on a metric nobody
                                            would act on is noise
  Paper-pad return    NONE                  No target. It is a signal
                                            with a response, not a bar
  Transcription       The human service's    ≥95% clinician-judged, from
  accuracy            measured rate at M3    07-strategy's transition
                                            trigger. This is the one real
                                            baseline the plan will produce.

  NO IMPORTED BENCHMARKS. A published median describes a population this
  product is not in, with definitions nobody publishes.

  FIRST REAL BASELINE: milestone M2 (four practices, one week).
  At that point documentation rate stops being an assumption.
  Naming the milestone converts an admitted weakness into a plan.
```

---

# Anti-Example 5 — Instrumentation That Leaks

## ❌ Looks measurable

```
Analytics events
  consultation_created  { practice_id, clinician_id, patient_ref,
                          patient_age, presenting_complaint }
  note_approved         { note_id, draft_text_length, note_excerpt,
                          edit_count }
  page_viewed           { path, referrer, user_agent, session_id }
Sent to «third-party analytics service» for dashboards and funnels.
```

**Why it fails**

- **`patient_ref`, `patient_age`, `presenting_complaint` and `note_excerpt` are regulated fields.** The mechanical check against
  `09-technology` §3's regulated-column list fails, and **any overlap fails the gate.**
- **This is not a data-quality issue.** It means regulated clinical data is now in a third-party system with different retention, different
  access control and a different jurisdiction — a compliance exposure.
- **`page_viewed` is an orphan event.** No metric consumes it. That is cost, noise and a privacy surface with no benefit.
- **Identity resolution is absent**, so every cohort and retention metric is uncomputable regardless of the events.
- **The third-party service was adopted without assessment** — `Analytics.md` requires it treated as a data processor.

## ✅ Passes

```
MOVE 6 — INSTRUMENT

  consultation_created   ships in M1
    Trigger     a consultation row is created
    Properties  consultation_id (uuid) · practice_id (uuid) ·
                occurred_at (timestamp)
    Feeds       M1 denominator
    NOT sent    patient_ref, patient_age, presenting_complaint — REGULATED

  note_approved          ships in M1
    Trigger     state transitions to 'documented'
    Properties  consultation_id (uuid) · practice_id (uuid) ·
                approved_at (timestamp) · word_count (integer) ·
                was_edited (boolean)
    Feeds       M1 numerator, and the words-per-note counter-metric
    NOT sent    note text, excerpts, patient identifiers

  transcript_ready       ships in M1
    Properties  consultation_id · ready_at
    Feeds       M2 approval latency

  THE MECHANICAL CHECK
    09-technology §3 regulated columns: patient_ref, audio content,
      note text, presenting complaint, patient_age
    Every event property listed above, compared: NO OVERLAP ✓
    This is a list comparison, not a judgment.

  IDENTITY RESOLUTION
    Practices are identified by practice_id, issued at account creation by
    the operator. Clinicians by clinician_id. There is no pre-signup
    identity to resolve — accounts are created during a sales conversation,
    so no anonymous-to-known stitching is required. Stated, because its
    absence would otherwise make cohorts uncomputable.

  DELIBERATELY NOT INSTRUMENTED
    Page views and navigation. No metric consumes them, and each property
    is a privacy surface. Revisit if a specific question needs them.

  WHERE IT IS COMPUTED
    The operational database, queried directly. No third-party analytics
    service in phase one.
    Reason: M1–M3 are all computable from consultation and note records
    the product already holds lawfully. A third-party service would be a
    second copy of clinical behavioral data in another jurisdiction,
    requiring assessment under 02-market Frame 2 — a cost with no benefit
    at this volume.
```

---

# The Pattern Across All Five

| Failure | How it presents |
| --- | --- |
| Vanity north star | Cumulative counts; three of them; no gaming question |
| Uncomputable definitions | Familiar names, none of the five required parts |
| No counter-metrics | "Optimize for growth", with the gaming answers unguarded |
| Benchmark targets | Imported medians, no baseline, definitions and targets at one confidence |
| Leaking instrumentation | Regulated fields as event properties, orphan events, no identity resolution |

---

> **Resource Note**
>
> The regulated-column check is a list comparison, and any overlap fails
> the gate.
>
> A note excerpt in an event property is not a data-quality problem. It is
> clinical data in someone else's jurisdiction.
