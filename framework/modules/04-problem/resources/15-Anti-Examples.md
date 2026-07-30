---
Title: Anti-Examples
Module: 04-problem
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show problem analyses where assumptions have been smoothed into facts.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 04-problem/core/06-Framework.md
Outputs:
  - Recognition of manufactured validation
Related Modules:
  - 07-strategy
  - 10-execution
Tags:
  - Problem
  - Anti Examples
  - Reference
---

# Anti-Examples

---

# Overview

This is the framework's honesty checkpoint, which makes it the module where a plausible-looking failure does the most damage. Every example
below produces a document that reads as validated research.

---

# Anti-Example 1 — The Blended List

## ❌ Looks validated

```
Problem Analysis

Single-handed GPs face significant documentation burden. Research shows
clinicians spend up to two hours daily on notes, often completing them
after hours. This causes burnout and reduces time available for patient
care. Practices are actively seeking solutions, and GPs report high
willingness to adopt tools that reduce this burden.
```

**Why it fails**

- **Validated and assumed material are in one paragraph.** "Complete them after hours" may be reported by three people; "practices are
  actively seeking solutions" is invented; "high willingness to adopt" is fabricated. A reader cannot separate them, and this is the module's
  core failure: *not through dishonesty, but through paragraph structure.*
- **"Research shows" with no source** is the phrase that launders everything after it.
- **"Up to two hours" is the upper bound of a recollection**, presented as a figure.

## ✅ Passes

```
VALIDATED  (retrievable source)
  None. No problem in this analysis carries [verified] evidence.
  This is a finding: Milestone Zero is validation, not building.

ASSUMED  (plausible, unevidenced — equal importance, unequal standing)
  P1  Notes are completed after the session ends
      [reported: 3 of 4 GPs known to the operator]
  P2  Recall degrades between consultation and write-up
      [inferred: from the observed paper pad]
  P3  Time cost is 60–120 min/day
      [assumption: recollection, upper bound quoted, unmeasured]

The two lists stay in separate sections for the rest of this document.
```

---

# Anti-Example 2 — Two-Dimensional Scoring

## ❌ Looks validated

```
Problem                        Frequency  Severity  Score
Notes completed after hours    5          5         25
Records system is slow         5          3         15
No dark mode                   3          1          3
```

**Why it fails**

- **The workaround dimension is missing** — the one most often omitted and the most informative. "Records system is slow" scores 15 with no
  acknowledgment that the workaround is *waiting*, which is adequate.
- **A preference is scored alongside a problem.** Dark mode has no cost when unmet; it should have been excluded at Stage 2 and kept visible
  in the excluded list, not ranked.
- **No cost per occurrence.** `06-business` needs it and `12-metrics` needs it as a baseline, and neither can recover it from a score of 25.

## ✅ Passes

```
Classification first
  PROBLEM     notes completed after the session (a cost is paid)
  SYMPTOM     "records system is slow" → why does that matter?
              → it adds to the after-hours time → that is P1
  PREFERENCE  dark mode — excluded. No cost when unmet.
              Kept on the page so it is not re-proposed as an omission.

Scoring: Frequency × Severity × Workaround
  P1  Notes completed after the session
      Frequency  5  daily, 8–9 sessions/week [inferred: contract terms]
      Severity   5  unpaid time + wellbeing; also medico-legal risk if
                    a note is missed [reported]
      Workaround 3  a paper pad exists — poor, but real
      Score      75
      Cost/occurrence: 60–120 min/day [assumption: unmeasured]
                       → 04-problem cannot narrow this. 12-metrics needs
                         a measured baseline.
```

---

# Anti-Example 3 — Manufactured Validation

## ❌ Looks validated

```
Validated problems
1. Documentation takes too long          [verified: user interviews]
2. Clinicians are frustrated with typing [verified: survey]
3. After-hours work causes burnout       [verified: industry research]
```

**Why it fails**

- **`[verified]` means a retrievable source**, not a convincing one. "User interviews" is not retrievable — how many, who, when, asked what?
- **Row 2 is a stated preference wearing a verification tag.** A survey of opinions verifies that opinions were expressed.
- **Row 3 is a population-level claim used to verify a segment-level problem.** True of clinicians generally, unverified for
  single-handed GPs in this jurisdiction.
- **The validated list was populated to avoid an empty section**, which is the failure the framework names explicitly.

## ✅ Passes

```
VALIDATED
  (empty)

Stated plainly: no problem in this inventory has a retrievable source.
Consequence, per 07-strategy and 10-execution: Milestone Zero is
mandatory and it is validation, not building. No acquisition spend
until it completes — 11-growth.

What would move P1 into this list
  A week of actual finish times from one practice, or a timestamp export
  from the records system. One question, one afternoon.
```

---

# Anti-Example 4 — Solving the Symptom

## ❌ Looks validated

```
Sharpest problem: typing during consultations is slow and breaks eye
contact. Solution direction: faster input.
```

**Why it fails**

- **This is a symptom.** Ask why it matters: because notes get deferred; because they are completed after hours; because the day does not
  end. The problem is three levels down.
- **The chain stops exactly where the intended solution operates**, which is the analysis run backward.
- **Faster typing does not close the day.** A product optimizing input speed would ship, work, and leave the GP staying late.

## ✅ Passes

```
Root cause chain
  Notes completed after hours
    ← because nothing is captured during the consultation
      ← because capturing breaks eye contact
        ← because the records system requires structured entry at the
          point of care
          ← because its data model was designed for billing
            ← NOT ACTIONABLE BY THIS PRODUCT

Level addressed: "nothing is captured during the consultation."
Chosen deliberately — the deeper causes sit inside a system we cannot
change (03-user immovable 1). Recorded as a decision, not an oversight.
```

---

# Anti-Example 5 — The Validation Plan That Cannot Fail

## ❌ Looks validated

```
Validation plan
1. Conduct user research with GPs
2. Build a prototype and gather feedback
3. Validate willingness to pay
4. Iterate based on findings
```

**Why it fails**

- **No invalidating result anywhere.** A plan with no result that kills the assumption cannot fail, and a test that cannot fail produces
  confirmation regardless of what is true.
- **Nobody could run it tomorrow.** "Conduct user research" is an activity, not a plan — no method, no sample, no question.
- **No stop-and-rethink trigger.** Failure is undefined, which is why doomed products run for years.
- **Ordered by convenience, not by load-bearing belief.**

## ✅ Passes

```
Ordered by cheapest test of the most load-bearing belief.

T1  Belief: GPs will accept a drafted note without reading it line by line
    LOAD-BEARING — if false, no time is saved and the product has no value
    Method: Wizard of Oz. Hand-write drafts from 10 real consultations.
    Sample: 5 single-handed GPs, outside the operator's network
    Effort: 3 days
    Would invalidate: 3 or more re-read every draft in full
    Written «date», before any data gathered

T2  Belief: notes are completed outside session time, and it costs 60+ min
    Method: ask for last week's actual finish times; request a timestamp
      export from the records system
    Sample: 3 practices
    Effort: 1 day
    Would invalidate: median under 20 minutes

STOP-AND-RETHINK TRIGGER
  If T1 fails, this should not be built as conceived. A draft nobody
  trusts unread saves no time, and the alternative (a structured form —
  see 14-ai-systems) may be the whole product.
```

---

# The Pattern Across All Five

| Failure | How it presents |
| --- | --- |
| Blended lists | One fluent paragraph containing both facts and guesses |
| Two-dimensional scoring | Frequency × Severity, no workaround column |
| Manufactured validation | `[verified: user interviews]` with nothing retrievable |
| Solving the symptom | A chain that stops where the intended product operates |
| Unfailable plan | Activities with no invalidating result and no stop trigger |

---

> **Resource Note**
>
> An empty validated list is a finding, and it changes the roadmap.
>
> Filling it to make the section look populated is the most expensive
> sentence anyone writes in this framework.
