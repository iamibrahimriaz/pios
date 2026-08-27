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

# Criterion 6 — The expected winner recorded before scoring begins, with its independence marked

**Passes when:** the option the author expected to win is written down before any score is
assigned, **and `independence` is set to `independent` or `contaminated` in the same
entry** — with `independence_reason` naming what pre-committed the answer whenever it is
`contaminated`.

**Fails when:** the expectation is added afterward, or `independence` is left unset, or a
contamination is recorded after the result is known.

**What this is for.** Confidence laundering cannot be detected in a single document — the
laundered and honest versions are identical. It can be detected across runs. If the
expected winner always wins, the comparison is recording a decision rather than making
one, and this field is what makes that pattern visible.

A pre-registered expectation that turns out wrong is the strongest evidence available that
the comparison did real work.

**Why independence is part of the criterion.** The common case is not a clean prediction.
It is a prediction the run had already been pushed toward — by four upstream modules that
converged on the answer, by an operator instruction that pre-committed the direction, or by
the agent's own previous run reaching a conclusion it found easy to defend. **A contaminated
expectation that is confirmed looks identical, in the state file, to an independent one that
is confirmed**, and a reader comparing runs cannot tell them apart.

**Mark it `contaminated` when you are unsure.** The cost of a false `contaminated` is that
one honest prediction is discounted. The cost of a false `independent` is that the only
cross-run check in the framework reports a clean record it has not earned.

**It is recorded now, not later.** A contamination noticed after the scoring is an excuse
written by whoever disliked the result, and it is worth nothing as a control.

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

# Criterion 8 — Each option marked carried_from_research or generated_here, and a generated winner states what its missing research would have tested

**Passes when:** every entry in `state.outputs.solution_options` carries `provenance`, and
any option marked `generated_here` lists under `unresearched` which modules never examined
it and what each would have tested.

**Fails when:** provenance is absent, or when a generated option is scored alongside
researched ones with no statement of the asymmetry.

## What this criterion is protecting

**Modules 02–06 research one direction.** This module then generates options — and sometimes
the option that wins is one it invented, because the evidence pointed somewhere the earlier
modules never looked.

> **That is the framework working.** A run whose recommendation cannot change under evidence
> decided before it started, and the whole point of generating options here is to let the
> answer move.

**What must not happen is the comparison pretending to be even.** A researched option arrives
with a market, a competitor set, a segment and a problem ranking. A generated option arrives
with whatever was found while writing this module — frequently two data points. **Scoring
them side by side produces a table in which those two things look identical**, because a
score is a number either way.

**On the run that produced this criterion it happened twice**: the winning option was
generated inside this module, and a later validation test overturned the problem ranking and
produced a second winner that had never been researched at all. **Both redirections were
correct.** Neither was comparably evidenced, and nothing required anyone to say so.

## The re-score test, when a generated option wins

**Mechanical, and it takes a minute.** Re-score the generated option with every criterion it
was never researched on set to **the lowest value any researched option scored on that
criterion.**

| Result | What to record in `asymmetry_effect` |
| --- | --- |
| It still wins | The win is robust to the missing research. Say so — this is a strong result |
| It no longer wins | **The win rests on the gap, not on the evidence.** Say that, plainly, in the section that presents the scores |

**Then choose a path and record which:** either a research pass through the modules it
skipped before the recommendation stands, or **a validation milestone that closes its
specific unresearched claims, placed first in the roadmap and blocking the first build
milestone.** The second is usually correct and always cheaper. It is a choice that gets
named, not a default.

## Two arguments that are not arguments

**"It fits the evidence better."** It was written after the evidence. Fit is not
independent confirmation, and a generated option will always fit better for that reason
alone.

**"The researched options are refuted anyway."** Then say which of their evidence still
stands. **Evidence does not stop being true because the recommendation moved**, and a
refuted option's market sizing, competitor set and user research frequently survive intact
and apply to whatever replaced it.

| Fails | Passes |
| --- | --- |
| Four options scored, no provenance recorded | Each marked; B and D `generated_here` |
| "Option D wins on every criterion" with D generated here | "Option D wins at 4.20. **It was generated in this module and has no market research behind it** — 02 and 05 examined a different product. Re-scored with its unresearched criteria at the lowest observed value it scores 3.6 and still leads. Path: Milestone Zero closes its distribution claim before any build" |

---

# Criterion 9 — If 01-idea recorded stance `category`, the option supplying the differentiation is named, or the research is stated to have found none

**Passes when:** `state.project.differentiation_stance` is `category` and
`differentiation_resolved_by` is set — either to the option that supplies the position, or
to `not found` with the finding stated.

**Not applicable when:** the stance was `committed`. Record it as not applicable rather than
as a pass; the two mean different things and the verdict should say which.

**Fails when:** the stance was `category` and this module ends without addressing it.

## Why it lands here and not earlier

**An operator is allowed to say "I don't know the differentiation yet; find it."** `01-idea`
records that as a valid starting state rather than a defective idea. **What makes it valid is
that something eventually closes it** — otherwise it is a deferral that no gate ever collects,
and the run delivers a recommendation for a product with no stated reason to exist.

**This is the module that can close it**, because it is the first one holding options,
competitors and a problem ranking at the same time.

## "The research found none" is a pass, and often the most valuable one

**A category with no available differentiating position is a real finding**, and it is the
finding that saves the most money. It must be stated as a conclusion with its evidence — not
left as an empty field.

| Fails | Passes |
| --- | --- |
| Stance was `category`; module ends, nobody mentions it | "Stance was `category`. Option C supplies it: no competitor reconciles X against Y — 211 products searched, zero. `differentiation_resolved_by: 07-strategy`" |
| "The differentiation is that we execute better" | "`not found`. Four incumbents hold the positions this category supports and all four are adequately executed. **Recorded as a finding, and it is the reason the recommendation is not to build**" |

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

U1–U7 apply. Most relevant here:

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
6. Evaluate universal gates and criteria 1–9. **All of them.** The count here must equal the
   number in `module.yaml`; `validate.py` fails the build when it does not.
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
    expected_winner_pre_registered: pass
    shortfall_weight_named: pass
    option_provenance_marked: pass
    differentiation_resolved: not_applicable   # stance was `committed`, not `category`
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
