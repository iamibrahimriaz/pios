---
Title: Anti-Examples
Module: 14-ai-systems
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show AI proposals that skip the comparison, the data check or the wrongness cost.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 14-ai-systems/core/06-Framework.md
Outputs:
  - Recognition of capability theater and unjustified autonomy
Related Modules:
  - 08-product
  - 09-technology
Tags:
  - AI
  - Anti Examples
  - Reference
---

# Anti-Examples

---

# Overview

> The module succeeds when it drops most of what it proposed.

Each example below keeps everything, and each does so by skipping one of the six moves.

---

# Anti-Example 1 — The Straw-Man Comparison

## ❌ Looks justified

```
AI capability: automated note generation

Non-AI alternative considered: manual typing.
Assessment: manual typing is exactly the problem we are solving. It is slow,
breaks eye contact, and forces after-hours work. AI generation is clearly
superior.
Decision: build the AI capability.
```

**Why it fails**

- **The alternative is the status quo restated as the problem.** Of course it loses — the whole run exists because it loses. That is not a
  comparison; it is a restatement.
- **Apply the advocate check:** could a competent person argue for manual typing in one honest sentence? No. So the alternative was a straw man
  and **the comparison proved nothing.**
- **The real alternatives were never considered.** A structured form. A template library. A human transcription service — which `07-strategy`
  actually chose.
- **This is capability theater**: a model added because it is expected rather than because it wins.

## ✅ Passes

```
MOVE 2 — COMPARE   (a genuine alternative, argued by its advocate)

  Capability: generate a draft note from a consultation recording.
  Job served: J1 and J2 from 03-user. Requirement: R-03.

  ALTERNATIVE 1 — human transcription (what 07-strategy chose)
    ADVOCATE: "A person produces a clinically accurate note today, with no
      evaluation harness, no accuracy risk, no inference cost, and no
      trust problem. The GP can rely on it unread from week one."
    A competent person would say this. It is a real option, and it WON —
    which is why the MVP has no model in it.

  ALTERNATIVE 2 — structured form, four fields, keyboard-driven
    ADVOCATE: "The problem is recall between consultation and write-up.
      A form filled during the consultation solves that, for a third of
      the price, with zero accuracy risk."
    Real option. Loses on completeness — a form does not produce a
    narrative note — but it is the cheapest thing that addresses P2.

  VERDICT AT THIS STAGE: the AI capability is DROPPED for the MVP.
    Kept as a transition candidate, triggered at 15 practices and 300+
    transcript pairs (07-strategy). At that point the comparison re-runs
    with real data and a real accuracy baseline.

  Proposed: 3 capabilities. Kept for the MVP: 0. That is the module
  working, and the dropped rows are recorded with the simpler thing
  adopted instead — so this does not get re-proposed next quarter as an
  obvious omission.
```

---

# Anti-Example 2 — Data Assumed, Not Confirmed

## ❌ Looks justified

```
Data requirements
  Training data      consultation recordings and their corresponding notes
  Volume needed      approximately 1,000 pairs
  Availability       we will accumulate this from usage
  Quality            high — notes are written by clinicians
  Rights             covered by our terms of service
```

**Why it fails**

- **"We will accumulate this" is a projection.** The framework requires availability **confirmed, not assumed** — and an unconfirmed data need is
  a **blocker, not a risk.** A capability resting on data nobody has checked for cannot be estimated, scheduled or built.
- **The cold-start question is unanswered.** Before any pairs exist the capability is at its worst, and that is exactly when users are least
  tolerant.
- **"Covered by our terms of service" is not a legal basis.** Consent for treatment is not consent for model input, and whether the data may be
  used this way is a legal determination.
- **Whether provider training on the data is disabled** — contracted or assumed — is not addressed.

## ✅ Passes

```
MOVE 3 — GROUND

  Data need        consultation audio paired with the clinician-approved
                   final note
  Source           our own service delivery — 07-strategy's phase one
  Available NOW    NO. Zero pairs exist. CONFIRMED, not projected.
                   → this is why the capability is dropped for the MVP
  Available WHEN   at the M3 milestone, ~300 pairs [projected, and labeled]
  Volume needed    UNKNOWN. Depends on the approach. To be established at
                   the transition, not guessed now
  Quality          the notes are clinician-approved, which is the highest
                   quality label available. Genuine advantage of the
                   service-first sequence
  COLD START       not applicable to the MVP, because the capability is not
                   in it. This is the cold-start problem solved by
                   sequencing rather than by tolerating a bad first period

  DATA RIGHTS — legal claims, not access
    Do we have the right? UNRESOLVED.
      Clinical audio and notes are special-category data. A processing
      agreement covering service delivery does not automatically cover
      model training. [«citation», 02-market Frame 2]
      OWNER «operator». Needs legal input. BLOCKS the transition, not the MVP.
    Does the data leave our systems? At the transition, yes — to a model
      provider. Whose infrastructure, in which jurisdiction, must be
      established before then. Residency obligations apply.
    Regulated fields in the input? YES — the audio and the note text are
      both regulated. Checked against 09-technology §3.
    Provider training on our data disabled? MUST BE CONTRACTED, not assumed.
      An unconfirmed answer here is a blocker.
```

---

# Anti-Example 3 — Autonomy From Accuracy

## ❌ Looks justified

```
Autonomy

Once the model reaches 95% accuracy, notes will be generated and filed
automatically, with the GP notified. This removes the review step entirely
and delivers the full time saving. Below 95% we will keep the GP in the
loop.
```

**Why it fails**

- **Autonomy is derived from accuracy, which is the wrong axis.** The decisive question is whether the user can **detect** an error.
- **A wrong clinical note filed automatically is undetectable by the GP** — they were not shown it. And it is consequential: the record is
  clinical and medico-legal.
- **The rule is explicit:** where the user bears the cost and cannot detect the error, autonomy above "suggests" is not permitted without a
  mechanism that makes the error visible.
- **`03-user`'s immovable 3 is violated.** A clinician signs the record. Automation that removes the review without removing the accountability
  creates exposure for the user, which means for the product.
- **The 5% is not distributed evenly.** It will concentrate in a recognizable subset — accents, noisy rooms, unusual presentations.

## ✅ Passes

```
MOVE 4 — BOUND

  THE WRONGNESS COST
    What does one wrong output cost?
      A clinically inaccurate record. Consequences: a wrong future
      treatment decision, a failed audit, a medico-legal exposure for the
      GP personally.
    Who bears it?
      The GP. Personally and professionally. Not the operator.
    CAN THE USER DETECT IT IS WRONG?
      Only by reading the note against their own memory of the
      consultation — which is the work the product exists to remove.
      So: NO, not without re-doing the task.

  AUTONOMY CEILING: DRAFTS.
    The model produces; the GP edits and approves. Never higher.
    Not because accuracy is insufficient, but because the error is
    undetectable without redoing the work, and the cost falls on the user.

    99% accurate with an undetectable, consequential 1% is more dangerous
    than 90% accurate and visibly wrong.

  VISIBILITY MECHANISMS — required, because detectability is the constraint
    The draft always displays the recording it came from, playable.
    Spans the model marked low-confidence are visibly highlighted.
    Numbers, drug names and dosages are highlighted as
      must-verify regardless of confidence.
    → these are 08-product requirements and 10-execution interaction design.
      They are the guardrails. A better prompt is not one.

  OVERSIGHT
    Who reviews quality: a clinician. NOT the build team — they cannot
      assess clinical correctness, and their confidence in an output is
      not evidence about it.
    Override recorded: YES. Every edit is captured, and the edit rate is
      12-metrics' strongest signal about accuracy in production.
    AI involvement disclosed: YES, to the GP. Whether disclosure to the
      patient is required is a Frame 2 question. [OPEN]
    03-user immovable 3 respected: a clinician signs. Unchanged.
```

---

# Anti-Example 4 — Evaluation as an Intention

## ❌ Looks justified

```
Evaluation

We will evaluate transcription quality continuously and iterate on prompts
to improve accuracy. Initial testing shows promising results. We will
monitor user feedback and edit rates post-launch to identify areas for
improvement.
```

**Why it fails**

- **"We will evaluate it" is not a plan.** No metric, no method, no bar, no sample size, no cadence, no ship gate.
- **The bar is set after building**, which means it will be set to whatever was achieved.
- **"Promising results" on unstated cases** is a demo, and demos are curated. The distribution real work produces is messier.
- **No statement of what happens if the bar is missed.** Without it, the capability ships regardless.
- **No regression check.** A prompt or model-version change alters behavior invisibly.

## ✅ Passes

```
MOVE 5 — EVALUATE   (before commitment)

  Metric        clinical accuracy of the draft, judged case by case
  Method        golden set of 200 real consultation recordings with their
                clinician-approved notes, drawn from phase-one service
                delivery. NEVER used for tuning.
  Judge         a clinician, not the build team
  PASSING BAR   ≥95% judged clinically accurate
                AND ≥99% on a designated subset containing numbers, drug
                names and dosages — because those errors are the
                consequential ones and an average hides them
  Sample size   200, stratified to include: noisy recordings, accented
                speech, short consultations, unusual presentations.
                A golden set of clear, quiet, native-speaker cases measures
                a population we do not serve.
  Cadence       every model version change, every prompt change, and
                quarterly regardless
  SHIP GATE     the bar above, met before any GP sees model output
  IF MISSED     the capability does not ship. The service continues.
                Stated in advance, so the result cannot be reinterpreted.
  Regression    the golden set runs in the pipeline on every prompt or
                version change — 09-technology/knowledge/CI-CD.md

  ACCEPTANCE CRITERIA — both kinds, because the output is nondeterministic
    STATISTICAL
      Given the 200-case golden set, when transcribed, then ≥95% are
      judged clinically accurate by a clinician.
    PER-INSTANCE — always true, every time
      The draft is always editable before saving.
      The draft always displays its source recording.
      The draft can always be discarded.
      Nothing writes to the record without explicit GP approval.
      Numbers and drug names are always highlighted as must-verify.
    → handed back to 08-product, where they are conventional requirements.
      Most of the real safety lives here rather than in the 95%.
```

---

# Anti-Example 5 — Generic Failure Modes

## ❌ Looks justified

```
Risks and limitations
  The model may hallucinate or produce inaccurate output.
  Output quality may vary depending on input quality.
  The model may not handle edge cases well.
  Users should review all output before relying on it.
  We will monitor for issues and improve over time.
```

**Why it fails**

- **Every line is generic and generates no design work.** "May hallucinate" as a listed risk produces nothing; the specific version produces a
  guardrail.
- **No detection column and no guardrail column** — the two the framework requires, because likelihood and consequence alone do not tell you
  whether you would ever know.
- **"Users should review all output" is a disclaimer, not a mechanism.** It moves the obligation to the person the product was meant to help.
- **The worst realistic outcome is softened** into "inaccurate output".
- **No non-AI fallback.** The provider will have an outage and the model will be deprecated; what the GP does then is part of the product.

## ✅ Passes

```
MOVE 6 — FAIL   (specific to this product, with detection and guardrail)

  Failure                      Detection            Guardrail
  The model invents a symptom   NONE by the GP       source recording always
  or finding the patient did    unless they replay   displayed and playable;
  not describe. It reads        the audio            low-confidence spans
  exactly like the rest of                          highlighted
  the note
  Extraction drops silently     NONE — a missing     word-count comparison
  to partial on a noisy         section looks like   against the recording
  recording; the missing part   a short              duration; flagged if
  looks like a short            consultation         anomalous
  consultation
  A drug name is transcribed    Possible, if the GP  ALL drug names and
  as a similar-sounding one     reads carefully.     dosages highlighted
                                Not reliable         must-verify, always,
                                                     regardless of
                                                     confidence
  Accented or atypical speech   The GP sees a poor   golden set stratified
  produces materially worse     draft — detectable   to include these cases;
  output for a subset of GPs                         per-GP edit rate
                                                     monitored (12-metrics)
  Provider outage               Immediate            NON-AI FALLBACK: the
                                                     human service path
                                                     remains operational.
                                                     A requirement, not a
                                                     contingency
  Model version deprecated      Provider notice      version pinned; the
                                                     previous version's
                                                     golden-set result
                                                     retained for comparison

  WORST REALISTIC OUTCOME — stated, not softened
    A GP approves a draft containing an invented finding or a wrong dosage,
    it enters the patient record, and a future clinical decision is taken
    on it. The GP is professionally accountable and the record is
    medico-legal evidence.

  WOULD WE KNOW IT HAPPENED?
    NO. Not unless the GP or a later clinician noticed. That answer is
    itself the finding, and it is why the autonomy ceiling is "drafts" and
    why the must-verify highlighting is a per-instance requirement rather
    than a nice-to-have.

  MODEL STRATEGY  (mostly about failure)
    Version pinned: «provider» «version» [verified: «date»]
    Deprecation exposure: the provider deprecated the previous version «n»
      months after release. Registered — 07-strategy/risks/Technical.md
    Fallback model: «alternative», evaluated against the same golden set
    Vendor lock-in: the prompt and the harness are portable; the accuracy
      baseline is version-specific and would need re-establishing

THE COST RATIO
  cost per operation «£x» × «n» operations/user/month = «£x»/user/month
  ÷ revenue per user «£x» = «n»% of revenue
  → forwarded to 09-technology §12 and 13-operations §11, where the
    framework's three cost checks will find it.
  At the transition this REPLACES the transcription labor cost, which
  13-operations found to be the dominant expense. That is the entire
  economic case for the transition, and it is why the trigger exists.
```

---

# The Pattern Across All Five

| Failure | How it presents |
| --- | --- |
| Straw-man comparison | The status quo restated as the alternative |
| Data assumed | "We will accumulate this", and rights covered by terms of service |
| Autonomy from accuracy | "Once we hit 95%, file automatically" |
| Evaluation as intention | "We will evaluate continuously and iterate" |
| Generic failure modes | "May hallucinate", plus a disclaimer instead of a guardrail |

---

> **Resource Note**
>
> In the passing version, three capabilities are proposed and none ships in
> the MVP.
>
> That is not the module failing to find an application for AI. It is the
> module doing the only job it has.
