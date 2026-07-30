---
Title: Examples
Module: 14-ai-systems
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show an AI analysis that drops everything it proposed, and the transition that reinstates it.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 14-ai-systems/core/06-Framework.md
Outputs:
  - A reference AI strategy
Related Modules:
  - 07-strategy
  - 09-technology
Tags:
  - AI
  - Examples
  - Reference
---

# Examples

---

# Overview

The run ends here, and it ends with an AI module that ships no AI. Three capabilities were proposed; all three are dropped for the MVP, one is
kept as a triggered transition candidate.

The product this framework produced from an idea that began as "an AI scribe for doctors" is a human transcription service.

---

# The Worked AI Strategy

```
AI STRATEGY — «Consultation notes»

MOVE 1 — PROPOSE   (generously; the discipline is in Move 2)

  C1  Generate a draft note from a consultation recording
      Job J1, J2 (03-user) · Requirement R-03
  C2  Suggest clinical codes from the note text
      No job. No requirement. → orphan, and 07-strategy made it a non-goal
  C3  Flag notes likely to be clinically incomplete
      No job. Arrived from what is possible, not from the research

MOVE 2 — COMPARE   (each against a genuine alternative)

  C1 — draft note generation
    ALT 1: human transcription
      ADVOCATE: "A person produces a clinically accurate note today, with
        no evaluation harness, no accuracy risk, no inference cost and no
        trust problem. The GP can rely on it unread from week one."
      A competent person would say this.
    ALT 2: structured form, four fields, keyboard-driven, in-consultation
      ADVOCATE: "The problem is recall between consultation and write-up.
        A form filled during the consultation solves that, for a third of
        the price, with zero accuracy risk."
      Also real. Loses on producing a narrative note.
    VERDICT: ALT 1 WINS for the MVP. C1 DROPPED, kept as a transition
      candidate. Where the alternative wins on quality but loses on
      effort, that is a legitimate reason to build the model version —
      later, with data. Not now, with none.

  C2 — code suggestion
    DROPPED. Orphan: no ranked problem, and a 07-strategy non-goal.
    Recorded as rejected, not deferred, so it is not re-proposed as an
    obvious omission.

  C3 — completeness flagging
    ALT: a required-fields check in the form
      ADVOCATE: "Completeness is a rule, not a judgment. A checklist
        catches a missing section deterministically, auditably, and for
        nothing."
    VERDICT: the alternative wins outright. DROPPED permanently.

  PROPOSED 3 · KEPT FOR MVP 0 · KEPT AS TRIGGERED CANDIDATE 1
  The dropped rows are recorded with the simpler thing adopted instead.

MOVE 3 — GROUND   (C1 only, since the others are gone)

  Data need      consultation audio paired with the clinician-approved note
  Source         our own phase-one service delivery
  Available NOW  NO. Zero pairs. CONFIRMED, not projected.
                 → this is the reason C1 is dropped, not a risk to manage
  Available WHEN ~300 pairs at the M3 milestone [projected, labeled]
  Volume needed  UNKNOWN, approach-dependent. Established at the
                 transition, not guessed now
  Quality        clinician-APPROVED notes — the highest-quality label
                 available, and a genuine advantage of sequencing the
                 service first
  COLD START     solved by sequencing rather than tolerated. The MVP has no
                 model, so there is no bad first period

  DATA RIGHTS — legal claims, not access
    Right to use for training? UNRESOLVED. A processing agreement covering
      service delivery does not automatically cover model training.
      Special-category data. [«citation», 02-market Frame 2]
      OWNER «operator». Needs legal input. BLOCKS THE TRANSITION.
    Data leaves our systems? At the transition, yes. Which provider, which
      jurisdiction — residency obligations apply, unresolved.
    Regulated fields in the input? YES — audio and note text both.
      Checked mechanically against 09-technology §3.
    Provider training on our data disabled? MUST BE CONTRACTED.
      An assumed answer is a blocker.

MOVE 4 — BOUND   (for the transition, decided now)

  THE WRONGNESS COST
    One wrong output costs: a clinically inaccurate record → a wrong future
      treatment decision, a failed audit, medico-legal exposure.
    Who bears it: the GP. Personally and professionally.
    CAN THE USER DETECT IT? Only by replaying the audio against their own
      memory — which is the work the product exists to remove. So NO.

  AUTONOMY CEILING: DRAFTS. Permanently.
    Not because accuracy will be insufficient, but because the error is
    undetectable without redoing the task and the cost falls on the user.
    03-user immovable 3 (a clinician signs) is unchanged.

  VISIBILITY MECHANISMS — required, and they are 08-product requirements
    source recording always displayed and playable
    low-confidence spans highlighted
    numbers, drug names and dosages always highlighted must-verify,
      regardless of confidence

  OVERSIGHT
    Quality judged by a clinician, never the build team.
    Every edit captured — the edit rate is 12-metrics' strongest production
      signal about accuracy.
    AI involvement disclosed to the GP. Disclosure to the patient: OPEN,
      a Frame 2 question.

MOVE 5 — EVALUATE   (the bar, set now, before any commitment)

  Metric      clinical accuracy, case by case
  Method      200-case golden set from phase-one delivery. NEVER tuned against
  Judge       a clinician
  BAR         ≥95% clinically accurate
              AND ≥99% on the subset containing numbers, drugs and dosages —
              because an average hides exactly the consequential errors
  Sample      200, stratified: noisy recordings, accented speech, short
              consultations, unusual presentations. A golden set of clear,
              quiet, native-speaker cases measures a population we do not
              serve
  Cadence     every version change, every prompt change, quarterly regardless
  SHIP GATE   the bar, met before any GP sees model output
  IF MISSED   the capability does not ship. The service continues.
              Stated now, so the result cannot be reinterpreted later
  Regression  golden set in the pipeline on every change

  ACCEPTANCE CRITERIA — both kinds
    STATISTICAL   ≥95% of 200 golden-set cases judged accurate by a clinician
    PER-INSTANCE  always editable · always shows its source · always
                  discardable · never writes without approval · numbers and
                  drug names always highlighted
    → handed to 08-product as conventional requirements. Most of the real
      safety is here, not in the 95%.

MOVE 6 — FAIL   (specific, with detection and guardrail)

  Failure                     Detection           Guardrail
  Invents a finding the       NONE unless the GP  source recording always
  patient did not describe    replays the audio   playable; low-confidence
                                                  spans highlighted
  Silently partial on a       NONE — looks like   word count vs recording
  noisy recording             a short             duration; flagged if
                              consultation        anomalous
  A drug name becomes a       Unreliable          ALL drugs and dosages
  similar-sounding one                            highlighted must-verify
  Materially worse for        The GP sees a poor  stratified golden set;
  accented speech             draft               per-GP edit rate monitored
  Provider outage             Immediate           NON-AI FALLBACK: the human
                                                  service path stays
                                                  operational. A requirement
  Version deprecated          Provider notice     version pinned; prior
                                                  golden-set result retained

  WORST REALISTIC OUTCOME — not softened
    A GP approves a draft containing an invented finding or a wrong dosage;
    it enters the record; a future clinical decision rests on it. The GP is
    professionally accountable.

  WOULD WE KNOW? NO. That answer is the finding, and it is why the ceiling
    is "drafts" and why must-verify highlighting is a requirement.

  MODEL STRATEGY
    Version pinned «provider» «version» [verified: «date»]
    Deprecation exposure registered — 07-strategy/risks/Technical.md
    Fallback model «alternative», same golden set
    Lock-in: prompt and harness portable; the accuracy baseline is
      version-specific and would need re-establishing

THE COST RATIO
  «£x»/operation × «n» operations/user/month = «£x»/user/month
  ÷ «£x» revenue/user = «n»% of revenue
  → 09-technology §12 and 13-operations §11.
  At the transition this REPLACES the transcription labor that
  13-operations found to be the dominant cost. That substitution is the
  entire economic case for the transition, and it is why 07-strategy set
  the trigger at 15 practices.

GATE
  ✓ Each capability justified against a non-AI alternative — all three
    lost, and that is recorded
  ✓ Data availability CONFIRMED, not assumed — zero pairs exist
  ✓ Evaluation method defined before commitment
  ✓ Failure modes and human fallback specified
  proposed: 3 · kept: 0 (MVP), 1 (triggered)
  ⚠ Two blockers carried: training-data rights, provider residency.
    Both block the transition. Neither blocks the MVP.
```

---

# Example 1 — An Alternative With a Real Advocate

## ❌ Poor

```
Alternative considered: manual typing. This is the problem we are solving.
```

## ✅ Good

```
ADVOCATE: "A person produces a clinically accurate note today, with no
evaluation harness, no accuracy risk, no inference cost and no trust
problem. The GP can rely on it unread from week one."
```

**Why.** The advocate check asks whether a competent person could argue for the alternative in one honest sentence. If not, it was a straw man and
the comparison proved nothing. Here the alternative wins.

---

# Example 2 — Data Confirmed Rather Than Projected

## ❌ Poor

```
Availability: we will accumulate this from usage.
```

## ✅ Good

```
Available NOW: NO. Zero pairs. CONFIRMED, not projected.
→ this is the reason C1 is dropped, not a risk to manage.
```

**Why.** An unconfirmed data need is a **blocker, not a risk**. Recognizing that turns a capability that cannot be scheduled into a sequencing
decision — and the service-first path exists partly because of it.

---

# Example 3 — Autonomy From Detectability

## ❌ Poor

```
At 95% accuracy, notes are filed automatically with the GP notified.
```

## ✅ Good

```
Can the user detect it is wrong? Only by replaying the audio against their
memory — which is the work the product removes. So NO.
CEILING: DRAFTS. Permanently. Not because accuracy is insufficient.
```

**Why.** Detectability governs autonomy more than accuracy does. A 1% error rate that is undetectable and consequential is more dangerous than a
10% rate that is visibly wrong.

---

# Example 4 — A Bar That Cannot Be Reinterpreted

## ❌ Poor

```
We will evaluate quality continuously and iterate on prompts.
```

## ✅ Good

```
BAR ≥95%, AND ≥99% on the numbers-and-drugs subset.
IF MISSED: the capability does not ship. The service continues.
Stated now, so the result cannot be reinterpreted later.
```

**Why.** Evaluating after building sets the bar to whatever was achieved. The second threshold exists because an average hides exactly the errors
that matter.

---

# Example 5 — The Fallback as a Requirement

## ❌ Poor

```
In the event of a provider outage, the feature will be temporarily
unavailable.
```

## ✅ Good

```
NON-AI FALLBACK: the human service path stays operational.
A requirement, not a contingency.
```

**Why.** The provider will have an outage and the model will be deprecated. What the user does then is part of the product, and it belongs in
`08-product`'s requirements rather than in an operational note. Here the sequencing gave the product that fallback for free.

---

> **Resource Note**
>
> The run started as "an AI scribe for doctors" and ends as a human
> transcription service with a triggered path to automation.
>
> Nothing was suppressed to reach that. Module 04 declared its shortfall,
> module 07 weighted it, module 13's arithmetic named the dominant cost, and
> this module found no data. The framework simply did not smooth any of it
> over.
