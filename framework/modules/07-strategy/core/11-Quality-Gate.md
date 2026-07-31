---
Title: Quality Gate
Module: 07-strategy
Section: core
Category: Gate
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define how the Strategy module's gate is evaluated, criterion by criterion.
Audience:
  - AI Agents
Prerequisites:
  - 07-strategy/module.yaml
  - engine/gates.yaml
Outputs:
  - Gate verdict recorded in state.run
Related Modules:
  - 04-problem
  - 08-product
Tags:
  - Strategy
  - Quality
  - Gate
---

# Quality Gate

---

# Overview

`module.yaml` states the criteria. This document explains how to evaluate each.

This gate precedes a human checkpoint. Passing it does not authorize proceeding — it
authorizes **asking**.

---

# Governing Rule

> A gate is failed by default when its status cannot be determined.
>
> Uncertainty is a fail, not a pass.

---

# Criterion 1 — >= 3 solution options generated before one is chosen

**Passes when:** three or more options exist, each states what would be built first, and
those first builds differ.

**Fails when:** the options differ only in feature scope, or when any option exists only
to lose.

**The different-first-build test.** Read the "first build would be" line for each option.
If two match, those are one option.

**The advocate test.** For each rejected option, can a one-sentence honest case *for* it be
written? If not, it was decoration and the criterion fails.

| Fails | Passes |
| --- | --- |
| "Full platform / medium platform / minimal platform" | "Narrow capture tool, first build is the consultation recorder / Workflow replacement, first build is the records layer / Service-first, first build is a human transcription operation with a booking form" |

---

# Criterion 2 — Choice justified against the ranked problems, not preference

**Passes when:** the comparison table cites its sources per criterion, weights are stated,
and the chosen option's justification references ranked problems from module 04.

**Fails when:** scoring appears without citation, or when the justification reads as
qualitative preference.

**Also required:** the rejected options record **what we lose by rejecting them**. An
option dismissed without naming its value returns later as an unexamined feature request.

**Trace test:** pick any scoring cell. Does it resolve to a finding in modules 04, 05 or
06? A score that traces to nothing is a preference with a number.

---

# Criterion 3 — MVP cut line drawn with the reasoning recorded

**Passes when:** capabilities are explicitly above or below the line, the cut principle is
stated in one sentence, and the **end-to-end test is answered yes**.

**Fails when:** everything important is above the line, the principle is missing, or the
end-to-end test fails or is unanswered.

**The end-to-end test is objective.** Walk the `current_workflow` from module 03 against
the included capabilities. Can the primary persona complete the core job? An asserted yes
without the walk fails.

**The minimality check.** If more than roughly a third of identified capabilities sit above
the line, examine whether a cut was actually made. "Everything that scored well" is a
ranked list, not an MVP.

**Also required:** what the MVP proves, and what it does **not** prove. The second is
regularly omitted and is what stops the wrong conclusion being drawn from weak adoption.

---

# Criterion 4 — Explicit non-goals listed

**Passes when:** non-goals cover capabilities, segments and problems, each with a reason.

**Fails when:** the section is absent, or lists only capabilities.

**Coverage check:** the real problems module 04 identified and excluded must appear here.
They were already established as real; restating them as non-goals makes the exclusion
deliberate rather than forgotten.

---

# Criterion 5 — Risks registered with likelihood, impact and mitigation

**Passes when:** every risk carries a likelihood, an impact, a mitigation, and an **early
warning sign**, and the inherited risks from modules 04, 05 and 06 appear.

**Fails when:** any field is blank, or when the ratings are undifferentiated.

**The distribution check.** If every risk is rated medium, the register was filled in
rather than assessed. Expect a spread.

**The early-warning check.** A risk with no observable precursor has usually not been
thought through. This field is what makes the register operational.

**Inherited risks are mandatory:**

| If | Must appear |
| --- | --- |
| Sharpest problem assumed | "The product rests on an untested belief" |
| Gap not defensible | A risk with a timescale |
| Viability conditional | Module 06's conditions as risks or stop conditions |

---

# Criterion 6 — The expected winner recorded before scoring begins

**Passes when:** the option the author expected to win is written down before any score is
assigned.

**Fails when:** it is added afterward.

**What this is for.** Confidence laundering cannot be detected in a single document — the
laundered and honest versions are identical. It can be detected across runs. If the
expected winner always wins, the comparison is recording a decision rather than making
one, and this field is what makes that pattern visible.

A pre-registered expectation that turns out wrong is the strongest evidence available that
the comparison did real work.

---

# Criterion 7 — If 04-problem declared a shortfall, the weight it changed is named, and whether the winner would differ without it

**Passes when:** the specific criterion whose weight changed is named, and the counterfactual
is stated — would the same option have won without the shortfall.

**Fails when:** a shortfall was declared upstream and the comparison is identical to what it
would have been otherwise, with no explanation.

**Not applicable** when module 04 declared no shortfall. Say so explicitly rather than
leaving the criterion unaddressed.

**Why this criterion exists.** `declared_shortfall` is the framework's most distinctive
mechanism and its value depends entirely on something happening here. A shortfall declared
and then ignored is worse than one never declared — it produces documentation of rigor
without the rigor.

---

# Module-Specific Check — Milestone Zero

Not in `module.yaml`, but enforced by `engine/gates.yaml` under `declared_shortfall`.

> **If the sharpest problem is assumed rather than verified, or module 04 recorded a
> declared shortfall, the sequence must open with Milestone Zero — validation before
> building.**

Its absence fails the gate. This is the mechanism by which module 04's honesty about
evidence becomes a change in what actually gets done first.

---

# Module-Specific Check — Confidence Laundering

Strategy documents are written in a decisive register. That register is borrowed, and it
must not upgrade inherited uncertainty.

| Check | Fails when |
| --- | --- |
| Problem standing carried forward | An assumed problem is discussed as established |
| Defensibility carried forward | A non-defensible gap is described as an advantage |
| Viability conditions carried forward | Conditional viability reads as viable |

Compare the language here against the source modules. If this document is more confident
than they were, the gate fails.

---

# Universal Gates

U1–U6 apply. Most relevant here:

| | |
| --- | --- |
| **U4** | Every decision records alternatives rejected — this is the module where U4 does its real work |
| **U3** | The chosen approach must not contradict the price or gap it inherited |
| **U5** | Every bet is an assumption and needs a validation method |

---

# Evaluation Procedure

1. Run the four passes of `engine/review-loop.md`.
2. Apply the different-first-build and advocate tests.
3. Walk the workflow for the end-to-end test.
4. Check Milestone Zero against the inherited evidence standing.
5. Compare confidence language against source modules.
6. Evaluate universal gates and criteria 1–5.
7. Record the verdict.

```yaml
gate:
  module: 07-strategy
  attempt: 1
  inherited:
    problem_standing: assumed
    defensibility: moderate
    viability: conditional
  criteria:
    three_distinct_options: pass
    choice_traced_to_problems: pass
    mvp_cut_with_reasoning: fail
    non_goals_explicit: pass
    risks_rated_and_mitigated: pass
  milestone_zero_present: pass
  confidence_laundering: none detected
  verdict: fail
  reason: "End-to-end test unanswered; 9 of 12 capabilities sit above the line."
  action: "Walk the workflow; cut to the minimum that completes J1."
```

---

# On Failure

`module.yaml` sets `on_fail: return to 04-problem`.

| Kind | Example | Action |
| --- | --- | --- |
| **Local** | Cut too broad, options too similar | Revise here |
| **Upstream (problem)** | No option solves the sharpest problem | Return to `04-problem` |
| **Upstream (business)** | The best option cannot support the price | Return via `06-business` |

| Attempt | Action |
| --- | --- |
| 1–2 | Revise or regress |
| 3 | Halt. Escalate to the checkpoint with the unresolved question |

---

# What Passing Authorizes

Passing this gate authorizes **presenting to the operator** — nothing more.

The MVP cut commits money and months. It is a commercial decision, and module 08 may not
begin until the operator has approved it.

---

# What a Passing Module 07 Looks Like

- Three options that a competent person could genuinely choose between.
- A choice whose every scoring row traces to a research finding.
- Rejected options recorded with what they would have given us.
- An MVP small enough that the end-to-end test passes, and honest about what it does not
  prove.
- Non-goals covering capabilities, segments and problems.
- A risk register with differentiated ratings and observable early warnings.
- Milestone Zero present when the problem is unproven.
- Language no more confident than the modules it inherited from.

---

> **Gate Principle**
>
> Everything before this was reversible.
>
> This gate is the last automated check before a human commits money —
> so its job is to make sure they are committing with their eyes open.
