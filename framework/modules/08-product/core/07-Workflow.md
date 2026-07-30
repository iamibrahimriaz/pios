---
Title: Workflow
Module: 08-product
Section: core
Category: Procedure
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The executable step-by-step procedure for running the Product module.
Audience:
  - AI Agents
Prerequisites:
  - 08-product/core/06-Framework.md
  - engine/state-schema.yaml
Outputs:
  - projects/<slug>/research/08-product.md
  - state.outputs.prd_body
Related Modules:
  - 09-technology
  - 10-execution
  - 12-metrics
Tags:
  - Product
  - Workflow
  - Procedure
---

# Workflow

---

# Overview

`06-Framework.md` defines the method — the Translation. This document is the procedure.

This module opens the `specify` stage, immediately after the framework's second human
checkpoint. The operator has approved a cut. This module's job is to make that cut precise
without changing it.

---

# Position in the Run

```
07-strategy → ⏸ CHECKPOINT PASSED → [ 08-product ] → 09-technology
                                                   → 14-ai-systems
```

| | |
| --- | --- |
| Stage | `specify` |
| Depends on | `07-strategy` |
| Consumes | `mvp_definition`, `chosen_approach`, `personas`, `jobs_to_be_done` |
| Produces | `prd_body`, `feature_spec`, `acceptance_criteria`, `prioritization`, `edge_cases` |
| On fail | return to `07-strategy` |
| Human checkpoint | none — the decision was made at the previous stage |

---

# Step 1 — Verify Upstream and Inherit the Boundary

1. Confirm `07-strategy` is in `state.run.completed_modules` **and that its human
   checkpoint was approved**. An unapproved cut is not a boundary.
2. Read `mvp_definition` — the capabilities above the line, the cut principle, what the MVP
   proves and what it does not.
3. Read `chosen_approach` and `non_goals`.
4. Read `personas` and `jobs_to_be_done` from `03-user`, including the numbered workflow.
5. Read `ranked_problems` from `04-problem`, **with each problem's evidence tag**.
6. Check `state.run` for a declared shortfall from module 04.

Record the boundary explicitly before writing anything:

| Inherited | Consequence for this module |
| --- | --- |
| Capabilities above the line | The only things that may be MUST |
| Capabilities below the line | Deferral ledger. Never a MUST |
| Non-goals | Written into §6 as explicit exclusions |
| Sharpest problem **assumed** | Requirements serving it inherit that standing and are marked |

> The cut is not a starting point to refine. It is a boundary this module works inside.

---

# Step 2 — Read Before Writing

1. `engine/evidence-policy.md`
2. `08-product/core/03-Core-Principles.md`
3. `08-product/core/06-Framework.md` — the Six Moves
4. `08-product/core/08-Questions-To-Answer.md`
5. `08-product/knowledge/PRD.md`, `Requirements.md`, `FRD.md`
6. `08-product/knowledge/features/` — Acceptance-Criteria, Edge-Cases, Dependencies,
   Feature-Prioritization, Future-Scope
7. `framework/deliverables/templates/03-PRD.md` and `04-Feature-Spec.md` — know the shape of
   what this feeds

---

# Step 3 — Trace

Move 1. Build the spine.

1. List the ranked problems with their evidence tags.
2. Write out the core job as numbered steps, from `03-user`.
3. For each step, record which problem it belongs to and whether this release serves it.
4. Run both checks:
   - **Orphan check** — any capability above the line with no parent problem. Delete it.
   - **Coverage check** — any problem above the line with no capability. Either the cut was
     wrong (regress) or the spine is incomplete (continue).

Write the spine into §5 and §13 of the template before proceeding. Requirements written
before the spine exists acquire their parents retrospectively.

---

# Step 4 — Specify

Move 2. Write the requirements.

For each capability above the line, write one or more requirements with:

- Priority — **MUST only if above module 07's line**
- Parent problem, job and workflow step
- Basis — `derived: «module» «finding»` or `design decision`
- Dependencies

Then apply the two discipline checks:

| Check | Fails when |
| --- | --- |
| MUST discipline | Any MUST maps to a capability below the line |
| Label meaning | The MUST list is effectively the whole requirement list |

**When a new capability surfaces while specifying** — and it will:

```
Is the core job impossible without it?
  ├─ no  → deferral ledger (§10), with a reason and a revisit trigger
  └─ yes → module 07's end-to-end test has failed
             → regress to 07-strategy, recorded in §10
```

Do not resolve this by adding it quietly. That is the module's characteristic failure.

---

# Step 5 — Behave

Move 3. Describe behavior for every MUST requirement.

Write trigger, input, system response, resulting state, and what the user sees.

Then run the **two-builder test** on each: name the point where two independent engineers
would read this differently. If you can name one, the requirement is not finished.

Keep implementation out. A requirement that names a database, a framework or a screen layout
has taken a decision from `09-technology` or from design.

---

# Step 6 — Break

Move 4. Work the five edge categories for every MUST requirement.

| Category | Must be answered |
| --- | --- |
| Empty | First use, no data |
| Invalid | Wrong or incomplete input |
| Failure | Operation cannot complete — and whether work is lost |
| Permission | User not allowed — and what is not revealed |
| Limit / conflict | Too many, too large, concurrent, offline, interrupted |

"Not applicable — «reason»" is acceptable. A blank fails the gate.

State the **data-loss position** per requirement. If nothing can be lost, say that
explicitly; it is a claim worth making.

---

# Step 7 — Order

Move 5. Score and sequence.

1. Score every requirement with one consistent method.
2. Record every case where the score and the tier disagree, with the reason.
3. Build the dependency graph and state the critical path.
4. Name the **first shippable slice** — the smallest subset a real user could use.

---

# Step 8 — Prove

Move 6. Write acceptance criteria.

Use `Given / when / then`. Then run two mechanical checks:

- **Banned-word scan.** fast, performant, intuitive, easy, user-friendly, seamless, robust,
  reliable, appropriate, sensible. Any hit is rewritten as an observable.
- **Falsifiability check.** For each criterion, name the observation that would fail it. If
  none exists, it is not a criterion.

---

# Step 9 — Assemble and Write to State

Fill `13-Template.md` into `projects/<slug>/research/08-product.md`. Write §1 last.

```yaml
outputs:
  prd_body:             # §2-§6, §9, §12 — problem, users, goals, non-goals, constraints
  feature_spec:         # §7 requirements with behavior and dependencies
  acceptance_criteria:  # §7 criteria, per requirement
  prioritization:       # §11 scores, tiers, build order, first shippable slice
  edge_cases:           # §8 five categories per requirement
```

Append every **design decision** in §12 to `state.assumptions` with a validation method —
U5. Append every design decision to `state.decisions` with the alternative it rejected — U4.
Append every `NEEDS USER` question to `state.open_questions`.

---

# Step 10 — Review

Run all four passes of `engine/review-loop.md`.

The adversarial pass for this module:

- Which requirement has no real parent, only a plausible one?
- Which MUST is actually a SHOULD that I did not want to demote?
- Where did the spec grow past the cut the operator approved?
- Which behavior description would two engineers read differently?
- Which requirement has only happy-path criteria?
- Which acceptance criterion cannot fail?
- Which edge category did I mark "not applicable" to avoid thinking about it?
- Am I writing about an assumed problem as though the requirement makes it real?

The coherence pass: does this specification fit the price and cost-to-serve constraint from
`06-business`, and the operating context from `03-user`? A requirement set that needs a
different cost structure than the business model assumed is a contradiction, not a detail.

---

# Step 11 — Gate

Evaluate against `11-Quality-Gate.md` and universal gates U1–U6.

| Verdict | Action |
| --- | --- |
| Pass | Continue to Step 12 |
| Fail | Revise, or `return to 07-strategy`. Three attempts, then halt |

A **regress to 07-strategy** is the correct outcome — not a failure of this module — when
specification proved the cut cannot complete the core job. Record it plainly; the operator
approved a cut and needs to know it moved.

---

# Step 12 — Hand Off

1. Append `08-product` to `state.run.completed_modules`.
2. Confirm every Fast-follow and Deferred row in §10 is carried to the roadmap output.
3. Hand to `09-technology` and `14-ai-systems`.

---

# Handoff Contract

| Consumer | Reads | Uses it for |
| --- | --- | --- |
| `09-technology` | `feature_spec`, `edge_cases`, constraints | Architecture and the data model — the entities are implied by the requirements here |
| `14-ai-systems` | `feature_spec` | Which requirements are served by a model, and what happens when it is wrong |
| `10-execution` | `prioritization` | Build order, critical path, first shippable slice |
| `12-metrics` | Goals in §6 | Metric definitions and targets |
| `03-PRD.md` | `prd_body`, `acceptance_criteria` | The shipped PRD |
| `04-Feature-Spec.md` | `feature_spec`, `prioritization`, deferral ledger | The shipped feature spec |

`09-technology` is the strictest consumer: it derives entities and relationships from the
behavior written here. A requirement that leaves the data it touches implicit forces the
architecture module to invent it.

---

# Failure Modes

| Symptom | Cause | Fix |
| --- | --- | --- |
| Requirements with no parent problem | Spine not built first | Return to Move 1 and delete orphans |
| A ranked problem serves nothing | Coverage check skipped | Serve it or record its deferral |
| Everything is a MUST | Priority labels not applied | Re-derive MUST from the MVP line only |
| Spec exceeds the approved cut | Scope laundering | Move additions to the ledger, or regress |
| Two engineers would build differently | Behavior underspecified | Name the divergence and remove it |
| Only happy paths specified | Move 4 skipped | Work all five categories per requirement |
| "Intuitive and fast" as a criterion | Aspiration in criterion form | Replace with an observable |
| Nothing in the deferral ledger | Things dropped silently | Reconstruct it from 07-strategy and the research |
| Requirement names a database or framework | Implementation leaked in | Remove it; that belongs to 09-technology |

---

> **Workflow Principle**
>
> The measure of this module is a builder who never speaks to you
> and still builds the right thing.
>
> Everything that reads as "they will work it out" is where it fails.
