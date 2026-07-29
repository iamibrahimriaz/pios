---
Title: Workflow
Module: 03-user
Section: core
Category: Procedure
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The executable step-by-step procedure for running the User module.
Audience:
  - AI Agents
Prerequisites:
  - 03-user/core/06-Framework.md
  - engine/state-schema.yaml
Outputs:
  - projects/<slug>/research/03-user.md
  - state.outputs.segments
Related Modules:
  - 04-problem
  - 05-competition
Tags:
  - User
  - Workflow
  - Procedure
---

# Workflow

---

# Overview

`06-Framework.md` defines the method — the Five Moves. This document is the procedure.

This module may run in parallel with `02-market` once `01-idea` has passed, but it is
better run **after** `02-market`, because the market definition bounds which segments are
in scope.

---

# Position in the Run

```
01-idea → 02-market → [ 03-user ] → 04-problem → 05-competition
```

| | |
| --- | --- |
| Stage | `research` |
| Depends on | `01-idea`, `02-market` |
| Consumes | `idea_brief`, `market_definition` |
| Produces | `segments`, `personas`, `jobs_to_be_done`, `current_workflow`, `switching_cost` |
| On fail | return to `02-market` |
| Human checkpoint | none |

`04-problem` cannot start until this module passes. It is the direct consumer of almost
everything produced here.

---

# Step 1 — Verify Upstream

1. Confirm `01-idea` and `02-market` are in `state.run.completed_modules`.
2. Read `idea_brief` — specifically the context block: segment, user, buyer, setting.
3. Read `market_definition` — the boundary constrains which segments are in scope.
4. Check whether the brief already names a segment. If it does, this module **validates
   and refines** that choice rather than starting fresh — but it must still be defended
   against criteria, not accepted because the operator said it.

> If the brief distinguished buyer from user, carry that distinction through every move.
> Losing it here means rediscovering it at module 06.

---

# Step 2 — Read Before Writing

1. `engine/evidence-policy.md`
2. `03-user/core/03-Core-Principles.md`
3. `03-user/core/06-Framework.md` — the Five Moves
4. `03-user/core/09-Research-Methodology.md` — **read this carefully**; it defines how to
   research users without access to users
5. `03-user/core/08-Questions-To-Answer.md`
6. `03-user/knowledge/` — Jobs-To-Be-Done, Personas, User-Segments, Empathy-Map
7. `framework/packs/<vertical>/` if loaded

---

# Step 3 — Establish Research Mode

Before generating anything, determine and record which mode applies:

| Mode | Condition | Consequence |
| --- | --- | --- |
| **Primary** | Real users can be consulted | Findings may be tagged `[verified]` |
| **Proxy** | Retrieval available, no user access | Findings tagged from the source, never as observation |
| **Inferred** | No retrieval | Everything tagged `[assumption: needs validation]`, confidence `low` |

Write the mode into the analysis header. It is the most important metadata in the
document — it tells every downstream reader how much weight the personas can carry.

An agent operating in Proxy or Inferred mode has not met a user. Say so at the top.

---

# Step 4 — Run the Five Moves

| Move | Writes to |
| --- | --- |
| 1. Divide | draft — segments table |
| 2. Choose | draft — prioritization with reasoning |
| 3. Embody | draft — personas |
| 4. Observe | draft — current workflow, switching cost |
| 5. Job | draft — jobs to be done |

Then complete the **Immovables** section — what this person would not change.

Do not reorder. Observing before interpreting is the point of the sequence.

---

# Step 5 — Assemble

Fill `13-Template.md` into `projects/<slug>/research/03-user.md`.

Two checks specific to this module:

- **No invented quotes.** Every quoted user voice resolves to a source in §11. If none
  was found, the document says so.
- **No untraceable persona rows.** Each row carries a tag or is explicitly marked as an
  inference.

---

# Step 6 — Write to State

```yaml
outputs:
  segments:          # list with priority and reasoning
  personas:          # primary + secondary, with evidence standing
  jobs_to_be_done:   # each with frequency and current satisfier
  current_workflow:  # steps, tools, friction, timing
  switching_cost:    # five dimensions with magnitudes
```

Append to `state.evidence_log`, `state.assumptions`, and `state.open_questions`.

Every persona attribute that could not be evidenced becomes an assumption with a
validation method — usually "interview N users of type X".

---

# Step 7 — Review

Run all four passes of `engine/review-loop.md`.

The adversarial pass for this module asks:

- Did I choose this segment because it is best, or because it was easiest to research?
- Could my persona describe anyone in this market?
- Which persona attribute did I infer and present as observed?
- Did I invent any quote, name, or detail?
- Does any job statement name the solution I already had in mind?
- What would make this user refuse to switch, and did I record it honestly?

The coherence pass: does the prioritized segment sit inside `market_definition`? A segment
that has drifted outside the market boundary is a defect that will surface in module 05
as competitors who do not actually compete.

---

# Step 8 — Gate

Evaluate against `11-Quality-Gate.md` and universal gates U1–U6.

| Verdict | Action |
| --- | --- |
| Pass | Continue to Step 9 |
| Fail | Revise, or `return to 02-market` if the boundary is the problem. Three attempts, then halt |

---

# Step 9 — Hand Off

1. Append `03-user` to `state.run.completed_modules`.
2. Record any user vocabulary learned — the words this person uses for their own problem.
   It improves search quality in `04-problem` and `05-competition`.
3. Hand to `04-problem` and `05-competition`.

---

# Handoff Contract

| Consumer | Reads | Uses it for |
| --- | --- | --- |
| `04-problem` | `personas`, `jobs_to_be_done`, `current_workflow` | Ranking problems by frequency and severity |
| `05-competition` | `segments` | Judging who actually competes for this buyer |
| `06-business` | `segments`, `switching_cost` | Pricing and go-to-market |
| `08-product` | `personas`, `jobs_to_be_done` | Tracing requirements to jobs |
| `10-execution` | `personas`, `current_workflow` | Designing flows around the real working context |
| `11-growth` | `switching_cost` | Onboarding and migration strategy |

`04-problem` is the heaviest consumer. If `current_workflow` is thin, module 04 has
nothing to rank problems against and will fail its gate.

---

# Failure Modes

| Symptom | Cause | Fix |
| --- | --- | --- |
| Two personas that are the same person | Demographic segmentation | Re-segment by behavior |
| Segment chosen with no comparison | Move 2 skipped | Score against the criteria table |
| Persona reads like a character sketch | No evidence base | Tag each row or mark it inferred |
| A quote with no source | Fabrication | Remove it. Never invent a user voice |
| Job names a solution | Move 5 rushed | Rewrite in When/I want/So I can form |
| No switching cost section | Move 4 incomplete | Assess all five dimensions |
| Segment outside the market boundary | Coherence not checked | Reconcile with `market_definition` |

---

# When No User Can Be Reached

This is the normal case for an agent, not an exception.

Run in Proxy mode: reviews, forums, published studies, support documentation, job
postings, and competitor complaint threads. `09-Research-Methodology.md` explains how.

State the mode. Tag from the source. Set confidence honestly. Add "interview N users of
type X" to `state.open_questions` as the first validation task.

An inferred persona that says so is workable. One presented as observed is a fabrication
that every downstream module will trust.

---

> **Workflow Principle**
>
> Six modules build on the person described here.
>
> Be precise about who they are, and honest about how you know.
