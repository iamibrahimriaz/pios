---
Title: Workflow
Module: 07-strategy
Section: core
Category: Procedure
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The executable step-by-step procedure for running the Strategy module.
Audience:
  - AI Agents
Prerequisites:
  - 07-strategy/core/06-Framework.md
  - engine/state-schema.yaml
Outputs:
  - projects/<slug>/research/07-strategy.md
  - state.outputs.chosen_approach
Related Modules:
  - 08-product
  - 09-technology
Tags:
  - Strategy
  - Workflow
  - Procedure
---

# Workflow

---

# Overview

`06-Framework.md` defines the method — the Commitment. This document is the procedure.

This module closes the `decide` stage and ends at the framework's second mandatory human
checkpoint.

---

# Position in the Run

```
04-problem ┐
05-competition ├→ [ 07-strategy ] → ⏸ HUMAN CHECKPOINT → 08-product
06-business ┘
```

| | |
| --- | --- |
| Stage | `decide` |
| Depends on | `04-problem`, `05-competition`, `06-business` |
| Consumes | `ranked_problems`, `gap_analysis`, `business_model` |
| Produces | `solution_options`, `chosen_approach`, `mvp_definition`, `non_goals`, `risk_register`, `roadmap` |
| On fail | return to `04-problem` |
| Human checkpoint | **mandatory** |

---

# Step 1 — Verify Upstream and Inherit

1. Confirm `04-problem`, `05-competition` and `06-business` are complete.
2. Read `ranked_problems` and the **sharpest problem**, including its evidence standing.
3. Read `gap_analysis` and the **defensibility verdict**.
4. Read `business_model` and the **viability verdict**, price, and load-bearing assumption.
5. Check `state.run` for a **declared shortfall** from module 04.

Record three inherited conditions before doing anything else — they shape every later
move:

| Inherited | Consequence |
| --- | --- |
| Sharpest problem is **assumed** | Milestone Zero is mandatory; add a comparison criterion for surviving a wrong problem |
| Gap is **not defensible** | The strategy needs a speed or focus answer, and a clock in the risk register |
| Viability is **conditional** | The chosen option must fit the conditions module 06 stated |

> If all three are unfavorable, say so at the checkpoint plainly. Three weak foundations
> do not average into a strong one.

---

# Step 2 — Read Before Writing

1. `engine/evidence-policy.md`
2. `07-strategy/core/03-Core-Principles.md`
3. `07-strategy/core/06-Framework.md` — the Six Moves
4. `07-strategy/core/08-Questions-To-Answer.md`
5. `07-strategy/knowledge/solutions/` — Alternative-Solutions, Tradeoffs, MVP-Solution
6. `07-strategy/knowledge/risks/` — the risk categories
7. `07-strategy/knowledge/` — MVP, Milestones, V1, V2

---

# Step 3 — Diverge

Move 1. Generate at least three approaches.

Work the shapes in `06-Framework.md` deliberately — narrow tool, workflow replacement,
layer on top, service first, different segment. Do not generate variations of a single
idea.

Apply the two tests before proceeding:

- **Different first build?** If all three start by building the same thing, generate more.
- **Straw-man check?** Could a competent person reasonably choose each one? If two exist
  only to lose, the choice was already made.

---

# Step 4 — Compare

Move 2. Build the weighted comparison table.

State how weights were assigned. Add the criterion *"survives if the assumed problem is
wrong"* whenever module 04 declared a shortfall.

---

# Step 5 — Choose

Move 3. Commit.

Record the reasoning, the rejected options **and what they would have given us**, the bet,
and the reversal trigger.

Write the rejected column carefully. It is the section that stops a rejected approach
returning six months later as an unexamined feature request.

---

# Step 6 — Cut

Move 4. Draw the MVP line.

Run the end-to-end test explicitly and write the answer:

> Can «primary persona» complete «core job» using only what is above the line?

If the answer is no, do not proceed — redraw the line. An MVP that cannot complete one
job end to end produces no learning when it ships.

Record what the MVP proves and what it does not prove.

---

# Step 7 — Bound

Move 5. Write the non-goals: capabilities, segments, problems, integrations.

Pull the excluded problems from `04-problem` directly — they were already identified as
real and out of scope, and restating them here makes the exclusion deliberate rather than
forgotten.

---

# Step 8 — Register

Move 6. Three outputs.

**Risks.** Differentiate the ratings. Give every risk an early warning sign. Carry forward
the inherited risks from modules 04, 05 and 06 explicitly.

**Sequence.** High-level milestones. **Add Milestone Zero if the sharpest problem is
assumed** — take the validation plan from `04-problem` and make it the first milestone.
State what each milestone teaches.

**Stop conditions.** Specific thresholds, defined now.

---

# Step 9 — Assemble and Write to State

Fill `13-Template.md` into `projects/<slug>/research/07-strategy.md`.

```yaml
outputs:
  solution_options:  # all options, including rejected, with reasons
  chosen_approach:   # the choice, the bet, the reversal trigger
  mvp_definition:    # the cut, the principle, what it proves
  non_goals:         # explicit exclusions
  risk_register:     # rated, mitigated, with early warnings
  roadmap:           # milestones including M0 if required
```

Append every strategic bet to `state.assumptions`. Append every decision to
`state.decisions` with the alternatives rejected — universal gate U4 requires it, and this
is the module where it matters most.

---

# Step 10 — Review

Run all four passes of `engine/review-loop.md`.

The adversarial pass for this module:

- Did I decide before I generated, and build the options backwards?
- Are two of my three options actually straw men?
- Is my MVP genuinely minimal, or is it everything that scored above average?
- If the assumed problem turns out to be minor, what survives of this strategy?
- If the incumbent ships this next quarter, what do we still have?
- Which risk did I rate "medium" because rating it "high" would be uncomfortable?
- Am I about to ask for approval on a decision I have already made?

The coherence pass: does the chosen approach fit the price from module 06 and the gap from
module 05? A strategy that requires a different price than the business model assumed is a
contradiction, not a refinement.

---

# Step 11 — Gate

Evaluate against `11-Quality-Gate.md` and universal gates U1–U7.

| Verdict | Action |
| --- | --- |
| Pass | Continue to Step 12 |
| Fail | Revise, or `return to 04-problem`. Three attempts, then halt |

---

# Step 12 — Human Checkpoint

**Stop. This is mandatory.**

Present §12 of the template:

1. What we propose to build — one sentence.
2. What we are deliberately not doing.
3. The load-bearing assumption.
4. The decisions needed, each with a recommendation.

Include plainly, where they apply:

- The problem is assumed, not verified, and Milestone Zero validates it first.
- The gap is not defensible, and here is the clock.
- The business model is viable only under stated conditions.

Then wait.

> Do not proceed to module 08 without approval. The MVP cut commits money and months. It
> is the operator's decision, and presenting it as a completed research finding takes that
> decision away from them.

---

# Step 13 — Incorporate and Hand Off

1. Apply the operator's decisions.
2. Where they change the cut, update `mvp_definition` and re-run the end-to-end test.
3. Where they reject the chosen option, return to Step 5 with their reasoning recorded.
4. Record the approved decisions in `state.decisions`.
5. Append `07-strategy` to `state.run.completed_modules`.
6. Hand to `08-product`.

---

# Handoff Contract

| Consumer | Reads | Uses it for |
| --- | --- | --- |
| `08-product` | `mvp_definition`, `chosen_approach`, `non_goals` | Every requirement traces to the cut |
| `09-technology` | `chosen_approach` | The architecture serves this approach |
| `10-execution` | `roadmap` | Milestone sequencing |
| `09-Roadmap` (deliverable) | `roadmap`, Milestone Zero | The shipped roadmap artifact |
| `10-Risks` (deliverable) | `risk_register` | The shipped risk artifact |

Module 08 is the strictest consumer: anything not above the MVP line must not appear as a
MUST requirement. The cut is binding.

---

# Failure Modes

| Symptom | Cause | Fix |
| --- | --- | --- |
| Three options, one obviously best | Straw men | Regenerate with genuinely viable alternatives |
| Options differ only in scope | Same shape | Work the shape list in the framework |
| No rejected-option record | Move 3 incomplete | Record what each would have given us |
| MVP includes everything important | No cut made | Apply the end-to-end test and cut to it |
| No non-goals | Move 5 skipped | Pull excluded problems from module 04 |
| All risks rated medium | Rating avoided | Differentiate honestly |
| No Milestone Zero on an assumed problem | Inherited condition ignored | Add it from module 04's validation plan |
| Checkpoint presented as a summary | Decision already made | Present options, not conclusions |

---

> **Workflow Principle**
>
> Everything before this module was reversible.
>
> From here, other modules build on the choice — so the choice belongs
> to the human, and this module's last job is to give it to them cleanly.
