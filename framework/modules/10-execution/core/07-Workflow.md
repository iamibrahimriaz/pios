---
Title: Workflow
Module: 10-execution
Section: core
Category: Procedure
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The executable step-by-step procedure for running the Execution module.
Audience:
  - AI Agents
Prerequisites:
  - 10-execution/core/06-Framework.md
  - engine/state-schema.yaml
Outputs:
  - projects/<slug>/research/10-execution.md
  - state.outputs.build_handoff
Related Modules:
  - 12-metrics
  - 13-operations
Tags:
  - Execution
  - Workflow
  - Procedure
---

# Workflow

---

# Overview

`06-Framework.md` defines the method — the Handover. This document is the procedure.

This module opens the `operationalise` stage. It is the last module whose output a builder
reads while working rather than before starting.

---

# Position in the Run

```
08-product ┐
09-technology ┴→ [ 10-execution ] → 11-growth
                                  → 12-metrics
                                  → 13-operations
```

| | |
| --- | --- |
| Stage | `operationalise` |
| Depends on | `08-product`, `09-technology` |
| Consumes | `prd_body`, `data_model`, `api_contract`, `architecture` |
| Produces | `ux_flows`, `delivery_plan`, `milestones`, `build_handoff`, `qa_strategy` |
| On fail | return to `09-technology` |
| Human checkpoint | none |

`12-metrics` runs after this module and feeds instrumentation back into the build handoff. The
handoff is therefore **assembled last**, after `12-metrics` has named the events — which is
why this module writes the handoff inputs and the deliverable is emitted in the `deliver`
stage.

---

# Step 1 — Verify Upstream and Inherit

1. Confirm `08-product` and `09-technology` are both in `state.run.completed_modules` with
   passing gates.
2. Read `08-product`: the MUST requirements, the edge cases, the acceptance criteria, the
   **first shippable slice** and the critical path.
3. Read `09-technology`: the architecture, the data model, the interface contract, the
   **one-way doors**, and the non-negotiables in the security model.
4. Read `07-strategy`: the roadmap, and whether **Milestone Zero** is required.
5. Read `04-problem`: the validation plan, if Milestone Zero is required.
6. Read `03-user`: the numbered workflow and the persona's real operating constraints.
7. Collect every open question and blocker from modules 08 and 09.

Record before planning:

| Inherited | Consequence |
| --- | --- |
| First shippable slice | The first milestone is built around it |
| One-way doors | These determine what must be sequenced early |
| Milestone Zero required | M0 is validation, and nothing builds before it |
| Persona constraints | These become flow requirements, not preferences |
| Open blockers | These go to Blocked Work with owners, never into build instructions |
| Team facts | If absent, no durations are stated anywhere |

---

# Step 2 — Read Before Writing

1. `engine/evidence-policy.md`
2. `10-execution/core/03-Core-Principles.md`
3. `10-execution/core/06-Framework.md` — the Six Moves
4. `10-execution/core/08-Questions-To-Answer.md`
5. `10-execution/knowledge/` — User-Flows, Information-Architecture, Empty-States,
   Error-States, Loading-States, Microcopy, Accessibility, UX-Principles
6. `framework/deliverables/templates/08-UX-Flows.md`, `09-Roadmap.md` and
   `12-Build-Handoff.md` — especially the third, whose standard governs this module

---

# Step 3 — Flow

Move 1.

1. Write three to five design principles, each naming the research finding it derives from.
2. Choose the two or three **critical paths** that carry the product.
3. For each: trigger, persona, frequency, what success means, then the step table — what the
   user sees, does, what the system does, and what can fail.
4. Write the failure and recovery table per path, sourced from `08-product` §8. State whether
   work is preserved.
5. Establish **time to first value** — the moment, the step count, the target in minutes, and
   the longest unavoidable step.
6. Build the screen and state inventory. Every screen gets empty, loading, error and
   permission states.
7. Write the first-run state, the accessibility target, and the persona's context constraints
   as concrete requirements.

A path that stops at the point of success is half a path. The recovery rows are what make it
usable.

---

# Step 4 — Slice

Move 2.

For each candidate milestone, run the **demo test** and write the answer down:

> At the end of this milestone, what can you show a real user doing?

```
Does the answer describe a person doing something?
  ├─ yes → it is a milestone
  └─ no  → it is a layer. Re-slice vertically
```

Then check independence: could delivery stop here and leave something usable? Not complete —
usable.

Build the first milestone around `08-product`'s **first shippable slice**. That slice was
identified precisely so this module would not have to guess.

---

# Step 5 — Sequence

Move 3.

1. State the sequencing principle in one sentence, and why not the alternative.
2. Place **M0** first if the sharpest problem is assumed. Take its content from `04-problem`'s
   validation plan: method, sample, proceed-if, stop-if.
3. Order the remaining milestones by the stated principle, respecting dependencies.
4. Place the **one-way doors** deliberately, and write the reasoning — early enough to build
   on, late enough to be informed.
5. Identify which milestones can ship independently and what could run in parallel.
6. Write the critical path and the longest chain.
7. Write the **decision points** — where the plan is re-evaluated against real data, with the
   data needed and the possible outcomes including "stop".

---

# Step 6 — Define

Move 4. Per milestone:

- What a user can do at the end that they could not before
- The requirements it delivers
- Dependencies and relative size
- **Definition of done**: acceptance criteria from `08-product` listed explicitly, plus the
  non-functional bar
- **What is explicitly not done at this point**
- What this milestone teaches

Durations only where the operator supplied team facts, and then tagged.

---

# Step 7 — Verify

Move 5.

1. Assign each verification level what it covers.
2. Build the coverage table: every MUST requirement to at least one verification.
3. List unverified requirements explicitly, with reasons.
4. Confirm the five edge categories per requirement are covered, or name the gaps.
5. State **what is deliberately not tested, and why**.

---

# Step 8 — Prepare the Handover

Move 6. Assemble the inputs the build handoff needs, and run the **cold-start check** in §16:

| Check | Fails when |
| --- | --- |
| First task nameable in one sentence | The first day would be spent deciding what to do |
| Every reference resolvable | The reader is sent to a document that does not exist |
| No unresolved assumption in a build-blocking position | Someone will guess and never mention it |
| Definition of done present for M1 | "Done" becomes whoever's opinion prevails |
| Instrumentation identified | The product ships blind; retrofitting does not happen |
| A builder with no context could start today | The handoff is a summary, not a handover |

Every answer must be yes. A no is either a gap to close here or a regress — say which.

Move everything unresolved into **Blocked Work** with a named owner and the milestone that
needs it. Nothing unresolved may remain in the build instructions.

---

# Step 9 — Assemble and Write to State

Fill `13-Template.md` into `projects/<slug>/research/10-execution.md`. Write §1 last.

```yaml
outputs:
  ux_flows:       # §3-§6 — paths, first value, screens and states
  milestones:     # §7 — vertical slices with definitions of done
  delivery_plan:  # §8, §9 — sequence, critical path, decision points
  qa_strategy:    # §10 — levels, coverage, deliberate exclusions
  build_handoff:  # §2, §8, §10, §12, §13 — assembled for the critical deliverable
```

Append every planning judgment to `state.decisions` with the alternative rejected — U4. Append
every duration not supported by team facts to `state.assumptions` — U5. Append every blocker
to `state.open_questions` with its owner.

---

# Step 10 — Review

Run all four passes of `engine/review-loop.md`.

The adversarial pass for this module:

- Which milestone is a layer wearing a milestone's name?
- Which milestone could not actually ship on its own?
- Which "definition of done" would two people read differently?
- Where did I state a duration without knowing the team?
- Which requirement has no verification, and did I notice or hide it?
- Which unresolved assumption did I leave in the build instructions because moving it to
  Blocked Work looked bad?
- If the problem is assumed and M0 is missing, why?
- Would a builder with no context actually be able to start, or only to understand?

The coherence pass: does the plan's first milestone match `08-product`'s first shippable
slice, and does the sequence respect `09-technology`'s one-way doors? A plan that commits an
irreversible decision in the last milestone has sequenced backwards.

---

# Step 11 — Gate

Evaluate against `11-Quality-Gate.md` and universal gates U1–U6.

| Verdict | Action |
| --- | --- |
| Pass | Continue to Step 12 |
| Fail | Revise, or `return to 09-technology`. Three attempts, then halt |

---

# Step 12 — Hand Off

1. Append `10-execution` to `state.run.completed_modules`.
2. Hand to `11-growth`, `12-metrics` and `13-operations`.
3. Note that the **build handoff deliverable is assembled after `12-metrics`**, because the
   instrumentation section cannot be written before the events are named.

---

# Handoff Contract

| Consumer | Reads | Uses it for |
| --- | --- | --- |
| `12-metrics` | `milestones`, decision points | What must be measurable, and by when |
| `13-operations` | Launch milestone, `qa_strategy`, non-negotiables | Runbooks, support readiness |
| `11-growth` | Time to first value, the activation moment | The activation definition and channel timing |
| `08-UX-Flows.md` | `ux_flows` | The shipped flows artifact |
| `09-Roadmap.md` | `milestones`, `delivery_plan` | The shipped roadmap |
| `12-Build-Handoff.md` | `build_handoff` + instrumentation from `12-metrics` | The critical deliverable |

`11-growth` needs the **activation moment** specifically — the point in §5 where a user first
gets value. That is the event growth work is built around, and this module is where it is
defined.

---

# Failure Modes

| Symptom | Cause | Fix |
| --- | --- | --- |
| Milestones named after layers | Horizontal slicing | Re-slice vertically; run the demo test |
| Nothing demonstrable until the end | Same | Rebuild the sequence around the first shippable slice |
| Sequence with no stated principle | Move 3 skipped | State it, and check it was applied consistently |
| No Milestone Zero on an assumed problem | Inherited condition ignored | Add it from `04-problem`'s validation plan |
| One-way door committed late | Sequencing ignored `09-technology` | Move it earlier and state why |
| "Done" meaning different things to different readers | Definition of done vague | List the acceptance criteria explicitly |
| Milestone marked done, three weeks remain | "Not done" absent | State the exclusions |
| Durations with no team | Estimate boundary crossed | Remove them or attribute them to the operator |
| Requirements with no verification | Coverage table skipped | Complete it, or list the exclusions honestly |
| Flows for the happy path only | Recovery tables missing | Add them from `08-product` §8 |
| Screens with only populated states | State inventory incomplete | Empty, loading, error, permission — each one |
| Assumptions inside build instructions | Blocked Work avoided | Move them, with named owners |

---

> **Workflow Principle**
>
> The framework's last chance to be honest is the Blocked Work table.
>
> Everything unresolved either appears there, with a name against it,
> or gets guessed at by someone who will never mention that they guessed.
