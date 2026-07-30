---
Title: Anti-Examples
Module: 11-growth
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show growth plans built on borrowed playbooks and funnels drawn as loops.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 11-growth/core/06-Framework.md
Outputs:
  - Recognition of borrowed growth and unclosed loops
Related Modules:
  - 06-business
  - 12-metrics
Tags:
  - Growth
  - Anti Examples
  - Reference
---

# Anti-Examples

---

# Overview

> Growth is a property of the product, not an activity performed on it.

Each example below describes activity, and each would pass as a growth plan.

---

# Anti-Example 1 — Borrowed Growth

## ❌ Looks like a plan

```
Growth strategy

Product-led growth. A free tier drives self-serve signups, content
marketing builds organic traffic, and in-product virality drives referral.
We will layer paid acquisition once CAC is understood, targeting a
blended CAC of £120 and a 14-day trial-to-paid conversion of 8%.
```

**Why it fails**

- **This is the playbook of a product with a different model, segment and price.** A £2,400/year service sold to single-handed GPs has no
  self-serve motion, and `06-business` established the sale needs a conversation for trust.
- **Every figure is imported.** £120 CAC and 8% conversion come from a category, not from this market.
- **The payback check was never run.** At £2,400/year with a 52–76% margin, the CAC ceiling is large — but the *implied* CAC of a
  content-and-trial motion for a segment that does not self-serve is unknown and probably higher.
- **A free tier for a service-delivered product means free human transcription.** The marginal cost is a person's time.

## ✅ Passes

```
MOVE 1 — MODEL, and check it against the price

  Model chosen: SALES-LED, founder-delivered.
  Rejected: product-led — the MVP is a human service; there is no product
    to be used without help.
  Rejected: community-led — single-handed GPs are isolated by definition,
    which is the segment's defining property.
  Rejected: referral — see anti-example 4.

  THE PAYBACK CHECK
    Gross margin per user per month  £2,400/12 × 0.52..0.76 = £104–£152
    Acceptable payback               6 months [operator input]
    → CAC CEILING                    £624–£912

    Cost of one unit of the motion   one association meeting: «£x» plus
                                     4 hours of the operator's time at
                                     «£x»/hour = «£x» [cited]
    Conversions per unit             2 [assumption — untested]
    → IMPLIED CAC                    «£x»

    Verdict: inside the ceiling, but the conversion assumption is the whole
    result. At 1 conversion per meeting it breaches.

  A £20/month product could not carry this motion. A £2,400/year one can.
  Neither statement is about execution quality.
```

---

# Anti-Example 2 — Channels Chosen by Convention

## ❌ Looks like a plan

```
Acquisition channels
  1. SEO — target "clinical documentation software" and related terms
  2. Content marketing — a blog on practice efficiency
  3. LinkedIn — organic and paid, targeting GPs
  4. Conferences — presence at major healthcare events
  5. Partnerships — integrations with records system vendors
Projected CAC: £120 blended.
```

**Why it fails**

- **Not one citation of where this segment was observed.** A channel with no citation was chosen by convention, and four of these five are
  conventions.
- **"Major healthcare events" is where multi-partner practices and hospital buyers go.** Single-handed GPs are the least likely attendees, and
  `03-user` would have said so.
- **Partnerships with records vendors** — `05-competition` established their commercial conflict. They will not refer business to a product
  serving a segment they cannot serve profitably.
- **Channels compared on projected CAC**, which is an assumption. The comparable figure is the cost of one test.

## ✅ Passes

```
MOVE 2 — LOCATE   (find where they are; do not choose where to market)

  Channel                    Where the segment was OBSERVED
  «Named association»        60 single-handed members in «county»
                             [verified: published membership list, «date»]
  «Named practitioner forum» threads on documentation burden, «n» posters
                             identifiably single-handed
                             [verified: forum, accessed «date»]
  Local GP education events  attendance list published; «n» single-handed
                             [verified: «source», «date»]

  Compared on LEARNING COST, not projected CAC
    Channel              Cost of one test    Time to an answer
    Association meeting  «£x» + 4 hours      2 weeks
    Forum participation  0 + 6 hours         4 weeks
    Education event      «£x» + 6 hours      6 weeks

  FIRST CHANNEL: the association meeting. Cheapest test, fastest answer,
  strongest observation.

  DELIBERATELY NOT USED
    SEO — the segment does not search for a category that has no name
      (02-market Frame 1 found no settled category term)
    Records-vendor partnerships — 05-competition: commercial conflict
    Major conferences — the audience is multi-partner and hospital

  CANNOT BE EVIDENCED — open questions, not plans
    Paid social. No evidence this segment is reachable there. Untested.

  SEQUENCE RULE OBSERVED
    No channel test until activation works for the first ten.
    No acquisition spend at all before Milestone Zero completes —
    the problem is assumed.
```

---

# Anti-Example 3 — Sign-Up as Activation

## ❌ Looks like a plan

```
Activation
  Users activate when they complete signup and connect their records
  system. Target: 60% of signups activate within 7 days. Onboarding
  includes a product tour, a setup wizard and an email sequence.
```

**Why it fails**

- **Sign-up plus configuration is not value received.** The user has invested and got nothing. Activation must be the moment they get something
  they wanted.
- **"Connect their records system"** is the hardest step in the product placed before any value — the switching cost `03-user` priced, front-loaded.
- **A tour, a wizard and an email sequence are three explanations** where the work is removing steps. Explanation is the weakest option and the
  usual choice.
- **Acquisition spend implied before activation is proven** — the sequence rule forbids it.

## ✅ Passes

```
MOVE 3 — ACTIVATE

  ACTIVATION EVENT
    The GP approves their first transcribed note and it lands in the
    patient record.

  Why that action proves value
    It is the whole job, completed. Everything before it is investment
    with no return. This is also what 04-problem's P1 describes as solved.

  Biggest friction before it
    The overnight gap. The GP records on Monday and cannot activate until
    Tuesday morning. That is a property of the service model, and it means
    activation cannot happen in one session — which every onboarding
    decision must accommodate.

  SWITCHING COST PAID FIRST, INSIDE ACTIVATION
    03-user's binding dimension: a live consultation is not a safe place
    to experiment. So the first recording is deliberately NOT in a live
    consultation — the GP records a dictated summary after a consultation
    for their first use. Value arrives without the risk.
    Migration: none (notes stay in their system). Retraining: minutes.

  ONBOARDING — remove, defer, pre-fill; explain last
    Removed   no account setup — the operator creates it during the sale
    Removed   no records-system connection at first use; the first note is
              copied manually, and the integration is configured later
    Deferred  preferences, templates, additional clinicians
    Pre-filled practice details, from the sales conversation
    Explained one sentence in the empty state. No tour.

    Steps from arrival to activation: 3 (record, wait, approve).
    10-execution counted 4 for the full path; onboarding adds none.

  ACQUISITION AND ACTIVATION SEQUENCE
    Activation must work for the first ten before any channel is tested.
    Acquisition without activation is churn with extra steps.
```

---

# Anti-Example 4 — The Funnel Drawn as a Loop

## ❌ Looks like a plan

```
Growth loop

    Content ──▶ Traffic ──▶ Signups ──▶ Happy users
        ▲                                    │
        └──────── Referrals ◀────────────────┘

Each satisfied user refers colleagues, driving compounding growth. We
project 1.3 viral coefficient by month twelve.
```

**Why it fails**

- **The arrow back to the top is drawn, not earned.** This is a funnel: content produces users while it is published, and stops when it stops.
- **Referral requires users who benefit from other users joining.** Single-handed GPs in the same county compete for the same patients. A
  referral gives away an advantage, which makes this structurally unavailable.
- **A 1.3 viral coefficient is a fabricated figure** for a mechanism that cannot operate in this segment.
- **The diagram changes how the operator thinks about spend, hiring and valuation** — which is why drawing it this way is not a presentational
  choice.

## ✅ Passes

```
MOVE 5 — LOOP   (the closure test: does the output become the next input?)

  Candidate 1 — REFERRAL
    Closure test: FAILS on the precondition.
    Single-handed practices in one county compete for patients. A referral
    gives away an advantage. [03-user: the segment is isolated and
    competitive by structure]
    Available only WITHIN an organization — and segment A has one clinician.
    Verdict: not available. Not a weak loop; an absent one.

  Candidate 2 — TRANSCRIPT DATA IMPROVING THE SERVICE
    Closure test: PARTIAL. Each transcribed note improves the eventual
    model's training set, which lowers cost, which lowers price, which
    could widen the segment.
    But: the model does not exist yet (07-strategy's transition trigger),
    and the cycle time is months.
    Verdict: a loop in principle, not operative in this phase.

  Candidate 3 — ASSOCIATION REPUTATION
    Closure test: FAILS. Each meeting produces leads; the next meeting
    requires attending again. Output does not become input.
    Verdict: FUNNEL. Legitimate, and it is what we have.

  compounding: FUNNEL

  Stated plainly, because it changes everything downstream:
    Growth is linear in the operator's effort. 06-business's CAC arithmetic
    IS the growth model. There is no compounding to project, no viral
    coefficient, and hiring is the only way to increase throughput.
    Evidence that any loop works: NONE. All three are hypotheses.
```

---

# Anti-Example 5 — Retention Without a Mechanism

## ❌ Looks like a plan

```
Retention
  Our product delivers exceptional value by saving clinicians hours every
  week. This creates strong natural retention. We project 3% monthly churn
  based on industry benchmarks for vertical SaaS.
```

**Why it fails**

- **"A great product" is not a retention mechanism.** Users leave good products constantly, because nothing in them made leaving costly or
  forgetting them difficult.
- **No mechanism names a requirement.** The check is mechanical, and nothing here points at one.
- **3% from a benchmark** — `06-business` already established that averages across markets, price points and contract shapes are not a benchmark
  for anything specific.
- **No observable precursor to leaving**, which is the only actionable half of retention.

## ✅ Passes

```
MOVE 4 — RETAIN   (mechanism, traced to a requirement)

  Mechanism             Requirement that delivers it       At launch?
  Habit                 R-01 recording is part of every     YES — the job
                        consultation; 03-user frequency      recurs daily
                        is daily
  Workflow dependency   R-05 the note reaches the record.    YES
                        Once the practice relies on this
                        path, reverting means a backlog
  Accumulated data      NONE. Notes live in THEIR system,    NO — and this
                        not ours. We accumulate nothing      is a real
                        the GP would miss                    weakness
  Switching cost        LOW. There is nothing to migrate     NO
                        back. That cuts both ways
  Network               Not available — segment A is one     NO
                        clinician

  Honest summary: habit and workflow dependency are real and present at
  launch. Accumulated data — usually the strongest mechanism — is absent
  by design, because the notes belong in the records system.
  → 07-strategy should know: retention rests on habit alone in phase one.

  CHURN
    A number is 06-business's, and it is an assumption there.
    What this module supplies is the OBSERVABLE PRECURSOR:
      1. Recording frequency falls below the job's natural rate
         (8–9 sessions/week from 03-user). The strongest early signal.
      2. THE PAPER PAD RETURNS — a GP recording some consultations and
         writing others by hand. Directly observable in the data.
      3. Approval latency rises — drafts sitting unapproved for days.
      4. An export or data request.
    → 12-metrics defines each with a numerator, denominator and window.
    Response per signal stated, so it is monitoring with a purpose.
```

---

# The Pattern Across All Five

| Failure | How it presents |
| --- | --- |
| Borrowed growth | A playbook from a different model, segment and price |
| Channels by convention | Five channels, no citation of where the segment was seen |
| Sign-up as activation | Investment counted as value received |
| Funnel drawn as a loop | An arrow back to the top, and a viral coefficient |
| Retention without mechanism | "Exceptional value", plus a benchmark churn rate |

---

> **Resource Note**
>
> The honest answer here is `compounding: funnel`, retention resting on
> habit alone, and referral structurally unavailable.
>
> None of that is a failure. It is the information `07-strategy` needs to
> stop projecting growth the business cannot produce.
