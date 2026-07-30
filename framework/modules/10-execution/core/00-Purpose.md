---
Title: Purpose
Module: 10-execution
Section: core
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define why the Execution module exists and what it establishes for the rest of the run.
Audience:
  - AI Agents
  - Delivery Leads
  - Founders
Prerequisites:
  - constitution/core
  - 08-product and 09-technology gates passed
Outputs:
  - Shared understanding of what this module establishes
Related Modules:
  - 11-growth
  - 12-metrics
  - 13-operations
Tags:
  - Execution
  - Purpose
  - Foundation
---

# Purpose

---

# Overview

Everything is specified. Nothing has been started.

Modules 08 and 09 produced a complete description of a product — what it does, what exists,
what is prevented. None of it says what to do on Monday morning.

This module produces the first task, the order, and the definition of finished. It also
produces the only deliverable the manifest marks `critical`, because it is the one a person
opens when they begin to build.

---

# Purpose Statement

> Turn a complete specification into a first task, a sequence, and a definition of done —
> for someone who was never part of the run.

---

# Why This Module Exists

Three failures dominate execution planning.

**Horizontal slicing.** Milestones named after layers: the data model, then the API, then the
interface. It feels efficient. Nothing is demonstrable until everything is, so the first honest
feedback arrives after the budget is spent.

**"Done" as an opinion.** A milestone marked complete while one reader assumed it included
error handling and another did not. The dispute is unsettleable after the fact and entirely
preventable before it.

**The plan that reads well and cannot be started.** Dates with no team behind them,
assumptions sitting in build instructions, references to documents that do not exist, and a
first day spent deciding what the first task is.

The module's structure — flows before slices, the demo test, definitions of done that state
what is *not* done, an explicit estimate boundary, and a cold-start check on the handoff —
exists to make each of these visible.

---

# The Judgment This Module Makes

| Output | What it commits |
| --- | --- |
| `ux_flows` | The route the user actually walks, including where it breaks |
| `milestones` | The independently shippable units of work |
| `delivery_plan` | The order, why that order, and where the plan is re-examined |
| `qa_strategy` | What is verified, at what level, and what is not |
| `build_handoff` | The document someone opens to start |

---

# Core Objectives

- Map the two or three paths that carry the product, failures included.
- State time to first value in steps and minutes.
- Slice the work vertically, so each milestone ends with something a person can do.
- Sequence by a stated principle, with Milestone Zero first where the problem is assumed.
- Define done per milestone — including what is explicitly not done.
- Give every MUST requirement a verification, and name what is not tested.
- Make the handoff startable by someone with no context.

---

# What AI Should Learn Here

- A requirement list is not a route. Users experience sequences, not requirements.
- A milestone that cannot be demonstrated is a stage of one.
- Every definition of done needs its absences named, or "done" is negotiable afterwards.
- Sequencing principles conflict; a plan that switches between them silently is incoherent.
- The framework does not know the team, so it cannot know durations.
- An unresolved assumption in build instructions becomes an invisible decision.
- Unowned blocked work is unstarted work. "The team" is not an owner.

---

# The Estimate Boundary

Each module in this stage has a way of overreaching. This one's is the most tempting, because
plans are *expected* to carry dates:

> The framework does not know the team. It cannot produce durations.

| Establishable here | Not establishable |
| --- | --- |
| Sequence | Calendar dates |
| Dependency | Durations |
| Relative size — S / M / L | Team velocity |
| Critical path | Delivery commitments |

A duration is either operator input, with the assumed team stated, or an
`[assumption: needs validation]`. Never a derived figure, and never produced by analogy to
unnamed projects — "a feature like this usually takes two weeks" is a sentence with no
subject.

This matters when the number proves wrong. An estimate the operator gave is a plan to revise.
An estimate the framework invented is a document nobody trusts again.

---

# Scope

**This module covers**

- Design principles derived from research findings
- Critical paths, failure and recovery, time to first value
- Screens and their unpopulated states
- Milestone definition, slicing and sequencing
- Definitions of done, and decision points
- Verification strategy and coverage
- Blocked work, non-negotiables, and the build handoff

**This module does not cover**

| Not here | Belongs to |
| --- | --- |
| What the product does | `08-product` — settled |
| Schema, contract, architecture | `09-technology` — settled |
| Metric definitions and targets | `12-metrics` |
| Instrumentation event names | `12-metrics`, fed back into the handoff |
| Channels, launch marketing, pricing pages | `11-growth` |
| On-call, support, incident response | `13-operations` |
| Visual design | Design, from the flows here |

---

# Position in the Run

```
08-product ┐
09-technology ┴→ [ 10-execution ] → 11-growth
                                  → 12-metrics
                                  → 13-operations
```

This module opens the `operationalise` stage. The **build handoff deliverable is assembled
after `12-metrics`**, because its instrumentation section cannot be written before the events
are named — this module produces its inputs, the `deliver` stage emits it.

---

# What This Module Hands Forward

| Output | Consumed by | Used for |
| --- | --- | --- |
| `milestones`, decision points | 12 | What must be measurable, and by when |
| Activation moment | 11 | The event growth work is built around |
| `qa_strategy`, non-negotiables | 13 | Readiness, runbooks, support |
| `ux_flows` | `08-UX-Flows.md` | The shipped flows artifact |
| `milestones`, `delivery_plan` | `09-Roadmap.md` | The shipped roadmap |
| `build_handoff` | `12-Build-Handoff.md` | The critical deliverable |

`11-growth` needs the **activation moment** specifically — the point where a user first gets
value. This module defines it while mapping first value, and everything growth does is
organized around it.

---

# The Reader

Module 08 was written for a builder who cannot ask questions. Module 09 was read at the moment
they start typing. This module is read *while* they work.

> **The cold-start test.** Could an agent or engineer open the handoff, with no access to the
> research and no other document, and start writing correct code today?

Not "could understand the project" — could start. That is why "as discussed" fails on sight,
why essentials are carried inline rather than referenced, and why everything genuinely
undecided moves to Blocked Work with a named owner rather than sitting in the instructions
where somebody will quietly guess.

---

# Success Criteria

- Critical paths mapped end to end, with recovery and a work-preservation position.
- Every screen specified in its empty, loading, error and permission states.
- Every milestone passing the demo test and independently shippable.
- Milestone Zero first, where the problem is assumed.
- Definitions of done that two readers could not disagree about.
- Every MUST requirement verified, or its exclusion stated.
- No duration without a stated team.
- Every row of the cold-start check answered yes.

---

# Self Assessment

- Did I map routes, or reorder requirements?
- Does every milestone end with something a person can do?
- Would two people agree on whether each milestone is done?
- Did I state a single duration without knowing the team?
- Is there an assumption sitting in the build instructions?
- Could someone start tomorrow morning without a meeting?

---

> **Purpose Principle**
>
> Nine modules of research and specification are worth exactly as much
> as this one's last section is honest.
>
> If a builder cannot start from it, none of it was delivered.
