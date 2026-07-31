---
Title: Quality Gate
Module: 04-problem
Section: core
Category: Gate
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define how the Problem module's gate is evaluated, criterion by criterion.
Audience:
  - AI Agents
Prerequisites:
  - 04-problem/module.yaml
  - engine/gates.yaml
Outputs:
  - Gate verdict recorded in state.run
Related Modules:
  - 03-user
  - 07-strategy
Tags:
  - Problem
  - Quality
  - Gate
---

# Quality Gate

---

# Overview

`module.yaml` states the criteria. This document explains how to evaluate each.

**The gate checks whether the analysis was done honestly — not whether the news is good.**

A module reporting `UNVALIDATED` with a clear validation plan **passes**. A module
reporting `VALIDATED` on inference **fails**. Getting this the right way round is the
whole point.

---

# Governing Rule

> A gate is failed by default when its status cannot be determined.
>
> Uncertainty is a fail, not a pass.

---

# Criterion 1 — Each problem scored on frequency, severity and current workaround

**Passes when:** every problem surviving classification carries all three scores, the
scales are stated, and the arithmetic is visible.

**Fails when:** any dimension is missing — most often the workaround.

The workaround dimension is not optional. A problem scored 5×5 with no workaround
assessment is indistinguishable from a problem somebody already solved adequately.

**Also required:** classification happened first. If preferences appear in the scoring
table, Stage 2 was skipped and this criterion fails.

| Fails | Passes |
| --- | --- |
| "P1: high priority" | "P1: frequency 5 (daily), severity 5 (unpaid hours), workaround 5 (none — they simply stay late). Score 125" |

---

# Criterion 2 — >= 3 problems carrying [verified] evidence, not inference

**Passes when:** three or more problems have `[verified]` tags resolving to retrievable
sources at evidence ladder ranks 1–3.

**Fails when:** the count is met by promoting inferred problems, or by tagging expert
assertion and reasoning as verified.

**The honest shortfall clause.** If fewer than three problems can be verified — which is
common, and normal when no primary research was possible — the criterion is **not**
satisfied by pretending otherwise. Instead:

1. State the actual count plainly.
2. Set the verdict to `PARTIALLY VALIDATED` or `UNVALIDATED`.
3. Set confidence to `low`.
4. Make the validation plan the document's centerpiece.
5. Record the shortfall in the gate verdict.

A run may proceed past this criterion **unsatisfied but declared**. It may not proceed
with the shortfall concealed. The gate verdict records `shortfall_declared: true`, and
module 09 must then produce a Milestone Zero.

This is the one criterion in the framework that can be consciously waived — because
demanding verification an agent cannot obtain would only produce fabricated verification.

---

# Criterion 3 — The single sharpest problem identified and defended

**Passes when:** exactly one problem is named as sharpest, the choice references the
scoring table, comparable scorers are addressed, and the evidence standing is stated
explicitly as verified or assumed.

**Fails when:** no single problem is chosen, or the choice is asserted without reference
to the scores.

**Test:** if the highest-scoring problem was not chosen, is there a stated reason? Passing
over the top scorer requires more defense than choosing it, not less.

**Also required:** the root cause check. If the product addresses a symptom rather than the
root, that must be a stated decision.

---

# Criterion 4 — Unvalidated problems explicitly listed as such

**Passes when:** validated and assumed problems appear in **visually separate sections**,
the assumed section carries an explicit warning, and no assumed problem appears in the
validated list.

**Fails when:** the two are blended in prose, or the distinction is made only through
tagging inside a shared narrative.

Structural separation matters more than tagging here. A reader skimming a blended section
absorbs assumed problems as established ones, however carefully each sentence was tagged.

---

# Universal Gates

U1–U6 apply. Most often missed here:

| | |
| --- | --- |
| **U1** | Cost claims are the usual offenders — "costs about two hours a day" needs a source or a tag |
| **U3** | Problems must be attributable to the persona from `03-user`, not a different user |
| **U4** | The sharpest-problem choice is a decision; the alternatives rejected must be recorded |

---

# Evaluation Procedure

1. Run the four passes of `engine/review-loop.md`.
2. Verify every `[verified]` problem sits at evidence ladder rank 1–3.
3. Verify validated and assumed sections are structurally separate.
4. Evaluate universal gates U1–U6.
5. Evaluate criteria 1–4.
6. Record the verdict.

```yaml
gate:
  module: 04-problem
  attempt: 1
  verdict_reported: PARTIALLY VALIDATED
  criteria:
    all_scored_three_dimensions: pass
    three_verified_problems: fail
    shortfall_declared: true          # verified count 1, stated plainly
    sharpest_identified_defended: pass
    unvalidated_listed_separately: pass
  universal: [U1 pass, U2 pass, U3 pass, U4 pass, U5 pass, U6 pass]
  verdict: pass_with_declared_shortfall
  note: "Only P1 reaches verified. Milestone Zero required before build."
  action: "Flag to 07-strategy and 09-Roadmap."
```

---

# On Failure

`module.yaml` sets `on_fail: return to 03-user`.

| Kind | Example | Action |
| --- | --- | --- |
| **Local** | Workaround dimension unscored | Revise here |
| **Upstream** | No friction in `current_workflow` to harvest from | Return to `03-user` |
| **Fundamental** | Every candidate is a preference | Return to `03-user`; the persona or workflow may be wrong |

A run that harvests nothing painful has learned something important. Returning upstream is
correct. Manufacturing a problem to justify continuing is the one failure this module
exists to prevent.

| Attempt | Action |
| --- | --- |
| 1–2 | Revise or regress |
| 3 | Halt. Escalate with the specific finding |

---

# What a Passing Module 04 Looks Like

- Preferences were identified and excluded, with reasons on the page.
- Symptoms were traced to the problems beneath them.
- Every problem carries three scores and visible arithmetic.
- A reader can tell at a glance which problems are proven and which are believed.
- One problem is named as sharpest, and the reasoning survives scrutiny.
- The validation plan contains tests that could actually fail.
- The verdict is stated first, and is not softer than the evidence supports.

---

> **Gate Principle**
>
> This gate is not asking whether the problem is real.
>
> It is asking whether the analysis is honest about how much we know.
