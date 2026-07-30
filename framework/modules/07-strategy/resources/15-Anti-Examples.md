---
Title: Anti-Examples
Module: 07-strategy
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show strategies where the decision was made before the module ran.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 07-strategy/core/06-Framework.md
Outputs:
  - Recognition of straw-man options and undrawn cut lines
Related Modules:
  - 08-product
  - 10-execution
Tags:
  - Strategy
  - Anti Examples
  - Reference
---

# Anti-Examples

---

# Overview

This module commits money and months. Each example below produces a document that reads like a decision and contains none.

---

# Anti-Example 1 — The Straw-Man Option Set

## ❌ Looks like a decision

```
Options considered

A. Build the AI consultation capture tool  ← RECOMMENDED
   Solves the problem directly with modern technology.

B. Do nothing
   Leaves the problem unsolved. Not viable.

C. Build a simple note-taking app without AI
   Would not differentiate and offers little value over existing tools.
```

**Why it fails**

- **One real option and two obviously worse ones.** The count is satisfied and the purpose defeated. The choice was made before the module
  ran, and the tell is that B and C have visible flaws while A has none.
- **They do not produce different first builds.** B builds nothing; C is A with a feature removed. Only one shape was considered.
- **C fails the advocate check.** No competent person would defend "a simple note app" as phrased — which means the comparison proved nothing.

## ✅ Passes

```
Options — each would produce a DIFFERENT FIRST BUILD

A. In-consultation capture (narrow tool)
   First build: capture during the consultation, one journey, end to end
   Solves: P1, P2 · Price supported: £600/yr · Defensibility: moderate
   Biggest risk: GPs will not accept an unread draft (04-problem T1)

B. Structured template library (no model)
   First build: a fast structured form, keyboard-driven, in-consultation
   Solves: P2 fully, P1 partly · Price supported: £300/yr
   Defensibility: none — trivially copyable
   Biggest risk: does not close the day, so the value case is halved
   ADVOCATE: "The whole problem is recall between consultation and
     write-up. A four-field form solves that today, for £300, with no
     accuracy risk and no inference cost." — a competent person would say
     this. It is a real option.

C. Service first — human transcription for solo practices
   First build: an operations process, not software
   Solves: P1 and P2 fully, at a cost · Price supported: £2,400/yr
   Defensibility: low, but revenue starts this month
   Biggest risk: margin, and it caps at what one person can process
   ADVOCATE: "Prove the problem with revenue before building anything.
     The data collected becomes the training set." — real option.
```

---

# Anti-Example 2 — Unweighted Comparison

## ❌ Looks like a decision

```
Criterion              A   B   C
Solves the problem     5   3   5
Defensibility          3   1   2
Time to first customer 2   4   5
Buildable by team      3   5   2
Novel and interesting  5   2   1
Total                 18  15  15
A wins.
```

**Why it fails**

- **Unweighted, so a minor criterion outvotes a decisive one.** "Novel and interesting" carries the same weight as solving the problem, and it
  is what produces A's margin.
- **"Novel and interesting" is not from the research.** Any added criterion favors something; this one favors the pre-chosen option.
- **The survives-if-the-problem-is-wrong criterion is absent** — and `04-problem` declared a shortfall, which is exactly when it matters most.

## ✅ Passes

```
Weights published BEFORE scoring, derived from the research:
  Solves sharpest problem        ×3  (04-problem rank 1)
  Survives if problem is wrong   ×3  (04-problem declared a shortfall)
  Time to first customer         ×2  (06-business: runway is short)
  Supports the modeled price     ×2  (06-business: conditional viability)
  Defensibility                  ×1  (05-competition: moderate at best,
                                      so it cannot carry much weight)
  Buildable by this team         ×1

  Criterion (weight)          A        B        C
  Solves sharpest (×3)        5→15     3→9      5→15
  Survives if wrong (×3)      2→6      4→12     5→15
  Time to customer (×2)       2→4      4→8      5→10
  Supports price (×2)         4→8      2→4      5→10
  Defensibility (×1)          3→3      1→1      2→2
  Buildable (×1)              3→3      5→5      2→2
  TOTAL                       39       39       54

  C wins on the weighted criteria. This was not the expected result.
```

---

# Anti-Example 3 — No Cut Line

## ❌ Looks like a decision

```
MVP scope
  In-consultation capture · structured note generation · templates ·
  patient history view · coding suggestions · export · audit trail ·
  admin dashboard · mobile app · integrations with two records systems
```

**Why it fails**

- **Everything is MVP, which is a refusal to decide.** This produces six months before first contact with a user, which is the failure the
  module exists to prevent.
- **No cut principle**, so nobody can decide a borderline case without asking.
- **The end-to-end test is not applied.** Ten items and no statement that the persona can complete one job with them.
- **Nothing states what the MVP does not prove.**

## ✅ Passes

```
CUT PRINCIPLE
  In scope only if the primary persona cannot complete one consultation
  note without it.

ABOVE THE LINE
  Capture during the consultation · produce a draft note · GP edits and
  saves it to the record · the four unpopulated states for each screen ·
  audit trail and access control (obligations, not ranked)

END-TO-END TEST
  Can a single-handed GP complete a consultation note using only what is
  above the line?  YES — capture, draft, edit, save. One whole job.

WHAT THE MVP PROVES
  Whether a GP will accept a drafted note without reading it line by line.
  (04-problem T1, the load-bearing belief.)

WHAT IT DOES NOT PROVE
  Willingness to pay · retention past two weeks · whether the channel
  repeats · whether accuracy holds outside the first practice.
  Stated so nobody concludes the wrong thing when it ships.

BELOW THE LINE → deferral ledger, with triggers
  Coding suggestions — when P1 is confirmed solved
  Patient history view — when a GP asks twice
  Mobile app — when a site prohibits the desktop
  Integrations beyond «system» — when a second records system appears
```

---

# Anti-Example 4 — Uniform Risk Ratings

## ❌ Looks like a decision

```
Risk                              Likelihood  Impact  Mitigation
Users may not adopt               Medium      Medium  Monitor closely
Competitors may respond           Medium      Medium  Move fast
Technical challenges              Medium      Medium  Careful planning
Costs may exceed estimates        Medium      Medium  Track spending
Regulatory changes                Medium      Medium  Stay informed
```

**Why it fails**

- **Everything is medium, so nothing has been assessed.** A register where all rows are equal is a register nobody will use.
- **Every mitigation is an intention.** "Monitor closely" and "move fast" reduce nothing and name nobody.
- **No early warning signs**, which is what makes a register operational rather than decorative.
- **The three inherited risks are missing** — the assumed problem, the moderate moat, and the load-bearing economic assumption.

## ✅ Passes

```
Inherited risks first — these are the largest.

R1  The sharpest problem is ASSUMED, not verified. Everything rests on it.
    Likelihood that it is wrong: unknown — that is the point
    Impact: fatal. The product solves nothing
    Mitigation: Milestone Zero. 04-problem T1, 3 days, before any build
    Owner: «operator»
    Early warning: T1 result itself
    → 10-execution: milestone_zero must not be ABSENT

R2  Inference cost per user exceeds £10/user/month
    Likelihood: medium-high — the range is £6–14
    Impact: gross margin falls below 60%; the model needs a price rise
    Mitigation: 14-ai-systems to compare cheaper mechanisms; cache
      identical requests
    Owner: «operator»
    Early warning: measured cost per user on the first three practices

R3  The gap is not defensible on product — a clock is running
    Likelihood: high. MedNote could build it in a quarter
    Impact: the window closes; the advantage becomes distribution, not
      capability
    Mitigation: none available. ACCEPTED, and it shapes the sequence
    Early warning: MedNote's changelog; a "solo" tier announcement

R4  No repeatable channel for customer eleven onward
    Likelihood: high — none has been tested
    Impact: growth stops at the operator's network, ~4 practices
    Mitigation: 11-growth to test one channel after activation works
    Early warning: cost per customer for numbers 5–10 versus 1–4

Note the spread: two high, one medium-high, one unknown. Not five mediums.
```

---

# Anti-Example 5 — No Stop Condition

## ❌ Looks like a decision

```
Success criteria
  Ship the MVP within three months
  Onboard 20 practices in the first six months
  Achieve positive user feedback
  Reach £12,000 ARR by month twelve
```

**Why it fails**

- **These are targets, not stop conditions.** None of them defines a result meaning this should not continue.
- **"Positive user feedback" cannot fail.**
- **Missing all four would still not stop the project**, because no threshold was designated as the end. That is why doomed products run for
  years.

## ✅ Passes

```
STOP-AND-RETHINK TRIGGERS — written «date», before anything is built

S1  If 3 or more of 5 GPs in Milestone Zero re-read every drafted note in
    full, the time saving does not exist. STOP as conceived.
    Next step is not iteration — it is option B, the structured form.

S2  If measured after-session note time has a median under 20 minutes, the
    problem is not severe enough to displace a free paper pad. STOP.

S3  If no practice outside the operator's network converts within four
    months of activation working, there is no channel. Return to
    06-business — the segment may be unreachable at this price.

REVERSAL TRIGGER for the chosen approach
  If MedNote or ClinicPro announces a solo tier at under £1,200/year,
  the defensibility verdict changes and the sequence must compress.
```

---

# The Pattern Across All Five

| Failure | How it presents |
| --- | --- |
| Straw-man options | One option with no flaws, two with obvious ones |
| Unweighted comparison | A criterion from nowhere deciding the result |
| No cut line | Everything is MVP, no principle, no end-to-end test |
| Uniform risk ratings | Five mediums and five intentions |
| No stop condition | Targets presented as criteria, failure undefined |

---

> **Resource Note**
>
> In the passing version, the weighted comparison picks the option nobody
> expected.
>
> That is the sign the scoring was real. When the favorite always wins,
> the module documented a decision rather than making one.
