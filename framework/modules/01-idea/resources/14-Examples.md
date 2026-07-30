---
Title: Examples
Module: 01-idea
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show a completed idea brief that passes the gate, and the moves that produced it.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 01-idea/core/06-Framework.md
Outputs:
  - A reference idea_brief
Related Modules:
  - 02-market
  - 04-problem
Tags:
  - Idea
  - Examples
  - Reference
---

# Examples

---

# Overview

One worked brief, threaded through the Six Passes. The domain — solo GP clinical documentation — continues through every module's
`resources/` so the outputs can be read as one run.

The brief below would pass this module's gate. Note how much of it is admitted uncertainty.

---

# The Worked Idea Brief

```
IDEA BRIEF — «Consultation notes for single-handed practices»

Origin
  Lived experience. The operator's partner is a single-handed GP.
  [01-idea/knowledge/Idea-Discovery.md: origin = lived experience.
   Knows the problem intimately; missing whether it generalizes.]

Problem statement
  Single-handed GPs complete consultation notes after their last patient
  leaves, in unpaid time.
  [inferred: three of four GPs the operator knows describe this]

Hypothesis
  If notes could be completed during the consultation, GPs would finish
  at their scheduled time.
  [assumption: needs validation]

Segment
  Single-handed general practices in «named jurisdiction».
  Deliberately not: multi-partner practices, hospital settings,
  other jurisdictions.

Operator goal
  Replace a salary within two years. Single operator. No external funding.
  [verified: operator]

Vision
  Nobody writes up notes after hours.

Mission
  We help single-handed GPs complete consultation notes during the
  appointment.

Value proposition
  For a single-handed GP who finishes notes after hours, this completes
  the note during the consultation, so the working day ends when the
  clinic does.

North star candidate
  Consultations documented before the patient leaves.
  [candidate only — 12-metrics ratifies]

Success indications
  Observable: notes reaching a completed state before the appointment ends.
  Failure: GPs revert to their previous method within two weeks.
  No targets set here.

Scope boundaries
  Not solving: note quality, clinical coding, referral letters,
  prescriptions, multi-clinician workflows.
  Not yet decided: mechanism. 14-ai-systems will compare alternatives.

Clarifying questions — NEEDS USER
  1. Which jurisdiction? (blocks 02-market Frame 2 entirely)
  2. Is there an existing records system that cannot be replaced?
  3. What is the operator's available runway?

Confidence: Low
  The problem is reported by four people known to the operator. Nothing is
  observed, nothing is quantified, no jurisdiction is set.
```

---

# Example 1 — Separating the Idea from the Solution

## ❌ Poor

```
The idea is an AI scribe for doctors.
```

## ✅ Good

```
Problem:   notes are completed after hours, unpaid.
Mechanism: undecided. Candidates include speech capture, a structured
           form, and a template library. 14-ai-systems compares them.
```

**Why.** Pass 2 (Separate) exists to hold these apart. Naming the mechanism in the idea removes four modules' worth of comparison, and
`07-strategy` cannot generate genuinely different options if every option requires the same first build.

---

# Example 2 — A Falsifiable Hypothesis

## ❌ Poor

```
Clinicians will love a tool that saves them time.
```

## ✅ Good

```
If notes could be completed during the consultation, GPs would finish at
their scheduled time.
Would be false if: GPs completed notes in-session and still stayed late
for other reasons.
```

**Why.** The second version names a condition under which it is wrong, which is what makes `04-problem` able to test it. The first cannot
be disproved by any observation.

---

# Example 3 — The Operator Goal, Asked

## ❌ Poor

```
Goals: build a large, category-defining business.
```

## ✅ Good

```
Operator goal: replace a salary in two years, solo, unfunded.
               [verified: operator]
Consequence:   a narrow tool at a real price to 40 practices may be
               sufficient. Market size is not decisive.
```

**Why.** `01-idea/knowledge/Goals.md`: the same idea built for a salary and built for scale is two different products. This answer
reshapes modules 06 and 11, and it cannot be inferred.

---

# Example 4 — Bounding the Idea

## ❌ Poor

```
Scope: clinical documentation and related workflows.
```

## ✅ Good

```
Not solving: note quality, coding, referrals, prescriptions,
             multi-clinician workflows.
Reason:      each is a separate job with a separate buyer conversation.
Reconsider:  coding, if 04-problem ranks it above note completion.
```

**Why.** Pass 6 (Bound) produces `scope_boundaries`, and `08-product` will check its requirement list against them. An unbounded idea
becomes an unbounded feature list four modules later.

---

# Example 5 — Honest Confidence

## ❌ Poor

```
Confidence: High — the problem is well understood.
```

## ✅ Good

```
Confidence: Low.
Basis:      four people known to the operator, reported not observed,
            one jurisdiction unstated, no quantification.
What would raise it: observed workflow with timestamps; 10 interviews
            outside the operator's network.
```

**Why.** The second version tells `04-problem` exactly what to do. The first tells it nothing and will be inherited as settled.

---

> **Resource Note**
>
> The passing brief is mostly caveats, boundaries and questions.
>
> That is not an incomplete brief — it is a brief whose weaknesses are
> visible to every module downstream.
