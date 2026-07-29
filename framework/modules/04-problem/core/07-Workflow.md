---
Title: Workflow
Module: 04-problem
Section: core
Category: Procedure
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The executable step-by-step procedure for running the Problem module.
Audience:
  - AI Agents
Prerequisites:
  - 04-problem/core/06-Framework.md
  - engine/state-schema.yaml
Outputs:
  - projects/<slug>/research/04-problem.md
  - state.outputs.ranked_problems
Related Modules:
  - 05-competition
  - 07-strategy
Tags:
  - Problem
  - Workflow
  - Procedure
---

# Workflow

---

# Overview

`06-Framework.md` defines the method — the Sieve. This document is the procedure.

This module produces the judgment the rest of the run depends on. It is also the module
most likely to produce a finding the operator does not want: *the problem is not proven.*

Producing that finding cleanly is the module working correctly.

---

# Position in the Run

```
02-market → 03-user → [ 04-problem ] → 05-competition → 06-business → 07-strategy
```

| | |
| --- | --- |
| Stage | `research` |
| Depends on | `03-user` |
| Consumes | `personas`, `jobs_to_be_done`, `current_workflow` |
| Produces | `problem_inventory`, `ranked_problems`, `validation_plan` |
| On fail | return to `03-user` |
| Human checkpoint | none — but see Step 9 |

---

# Step 1 — Verify Upstream

1. Confirm `03-user` is in `state.run.completed_modules`.
2. Read `current_workflow` — this is the primary harvest source.
3. Read `jobs_to_be_done` and `personas`.
4. Read the `NEEDS USER` questions recorded by `03-user`.
5. Note the research mode `03-user` declared. If it was Inferred, almost nothing in this
   module can reach `[verified]` — plan for that honestly rather than discovering it at
   the gate.

> If `current_workflow` has no friction points, stop. Return to `03-user`. A workflow
> documented at too high a level yields no problems, and manufacturing them here is worse
> than returning.

---

# Step 2 — Read Before Writing

1. `engine/evidence-policy.md`
2. `04-problem/core/03-Core-Principles.md`
3. `04-problem/core/06-Framework.md` — the Six Stages
4. `04-problem/core/09-Research-Methodology.md`
5. `04-problem/core/08-Questions-To-Answer.md`
6. `04-problem/knowledge/` — Severity, Frequency, Root-Cause, Problem-Tree
7. `04-problem/knowledge/validation/` — Interviews, Surveys, Prototype, Success-Criteria

---

# Step 3 — Harvest

Work through every harvest source in `06-Framework.md` Stage 1.

Record problems in the person's own framing. Do not filter, merge, or tidy at this stage.

Aim for breadth. A harvest that produces four candidates has not looked at the workflow
carefully — most workflows contain friction at every handoff.

---

# Step 4 — Classify and Score

1. Classify each statement: problem, symptom, or preference.
2. For each symptom, record the problem beneath it and carry that forward.
3. Keep excluded preferences on the page with the reason.
4. Score every surviving problem on frequency, severity and workaround.
5. Show the arithmetic.
6. Record cost per occurrence where it can be established.

---

# Step 5 — Sort

Split into **validated** and **assumed**, and keep them separate in the document.

A problem enters the validated list only with a `[verified]` tag resolving to a retrievable
source. Inference — however reasonable — is not validation.

Count both lists. The counts go in the verdict.

---

# Step 6 — Sharpen

1. Choose the sharpest problem.
2. Defend it against the scoring table.
3. Explain why comparable scorers were not chosen.
4. State its evidence standing explicitly.
5. Run the root cause check.
6. Decide, and state, whether the product addresses the root or a symptom.

---

# Step 7 — Plan

Build the validation plan, ordered by cheapest test of the most load-bearing belief.

Carry forward the `NEEDS USER` questions from `03-user`.

Define the stop-and-rethink trigger.

---

# Step 8 — Assemble and Write to State

Fill `13-Template.md` into `projects/<slug>/research/04-problem.md`.

```yaml
outputs:
  problem_inventory:  # full list including classified-out preferences
  ranked_problems:    # scored, with the validated/assumed split
  validation_plan:    # ordered tests with methods and samples
```

Append to `state.evidence_log`, `state.assumptions`, `state.open_questions`.

Record the sharpest problem and its evidence standing prominently — module 07 reads it
directly, and module 09 needs to know whether a Milestone Zero is required.

---

# Step 9 — Review

Run all four passes of `engine/review-loop.md`.

The adversarial pass for this module is the most important one in the run:

- Did I promote an assumed problem to validated because the section looked thin?
- Is my sharpest problem sharp, or just the one I find most interesting?
- Am I solving a symptom and calling it a problem?
- Did I score the workaround honestly, or generously?
- If this problem is not real, which claim in my analysis is the giveaway?
- Would a practitioner in this domain say I have described their actual pain?

**If the verdict is UNVALIDATED, do not soften it.** That verdict is the most valuable
output this module can produce. A run that reports "the problem is plausible but unproven,
here is the cheapest way to find out" has saved more money than one that reports a
confident fiction.

---

# Step 10 — Gate

Evaluate against `11-Quality-Gate.md` and universal gates U1–U6.

| Verdict | Action |
| --- | --- |
| Pass | Continue to Step 11 |
| Fail | Revise, or `return to 03-user` if the workflow was too thin. Three attempts, then halt |

Note: a gate **pass** with an `UNVALIDATED` verdict is a legitimate outcome. The gate
checks whether the analysis was done honestly, not whether the news is good.

---

# Step 11 — Hand Off

1. Append `04-problem` to `state.run.completed_modules`.
2. If the sharpest problem is assumed, flag it in state so `07-strategy` and `09-Roadmap`
   both see it.
3. Hand to `05-competition`.

---

# Handoff Contract

| Consumer | Reads | Uses it for |
| --- | --- | --- |
| `05-competition` | `ranked_problems` | Judging which competitors address which problems |
| `07-strategy` | `ranked_problems`, sharpest problem, `validation_plan` | Choosing the approach and drawing the MVP line |
| `08-product` | `ranked_problems` | **Every requirement must trace to one of these** |
| `09-Roadmap` (deliverable) | `validation_plan`, evidence standing | Deciding whether Milestone Zero is required |
| `12-metrics` | Cost per occurrence | Setting metric targets |

Module 08 is the strictest consumer: a requirement that cannot be traced to a problem in
`ranked_problems` fails module 08's gate. Anything that should be buildable must appear
here.

---

# Failure Modes

| Symptom | Cause | Fix |
| --- | --- | --- |
| Only three or four problems harvested | Workflow read too shallowly | Re-harvest from every handoff |
| Preferences scored as problems | Stage 2 skipped | Classify before scoring |
| High score for a solved problem | Workaround not scored | Score all three dimensions |
| Validated and assumed blended in prose | Stage 4 not respected | Keep them visually separate |
| Validated list padded | Inference treated as evidence | Only `[verified]` qualifies |
| No sharpest problem chosen | Stage 5 skipped | Module 07 cannot proceed without it |
| "Conduct user research" as a plan | Stage 6 rushed | Name method, sample, effort |

---

# When Evidence Is Thin

Common, and workable — provided it is stated.

1. Verdict is `PARTIALLY VALIDATED` or `UNVALIDATED`.
2. The validated list contains only what genuinely qualifies, even if that is nothing.
3. The assumed list carries everything else, clearly marked.
4. The validation plan becomes the most important section in the document.
5. Confidence is set honestly.

Then say plainly in the verdict: **validate before building.** Module 09 will turn that
into Milestone Zero.

---

> **Workflow Principle**
>
> This module is where a run either tells the truth or starts lying to itself.
>
> An honest "we do not know yet" is worth more than a confident answer nobody checked.
