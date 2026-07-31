---
Title: Quality Gate
Module: 10-execution
Section: core
Category: Verification
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define how each gate criterion for this module is evaluated.
Audience:
  - AI Agents
Prerequisites:
  - 10-execution/module.yaml
  - engine/gates.yaml
Outputs:
  - Gate verdict
Related Modules:
  - 12-metrics
Tags:
  - Execution
  - Quality Gate
  - Verification
---

# Quality Gate

---

# Overview

`module.yaml` states the criteria. This document explains how to evaluate each.

This gate stands in front of the only deliverable the manifest marks `critical`. What passes
here is what a builder starts from.

---

# Governing Rule

> A gate is failed by default when its status cannot be determined.
>
> Uncertainty is a fail, not a pass.

---

# Criterion 1 — Critical user paths mapped end to end

**Passes when** each critical path has a step table covering trigger to outcome, a failure and
recovery table, a stated work-preservation position per failure, and a step count; and every
screen has empty, loading, error and permission states.

**Fails when** a path stops at success, or a screen exists only in its populated state.

**End to end includes the failures.** A path that describes only the successful route is half a
path. Products are lost at the first error, not at the last feature.

| Fails | Passes |
| --- | --- |
| "The doctor dictates the note and it is saved." | Six steps, each with what the user sees and does; dictation-fails row showing the text retained and a manual entry offered |
| Screen list with purposes | Each screen's empty state naming what shows and which action is offered |

**Also required:** design principles that cite the finding they came from. A principle traced
to nothing constrains nothing — it passes every review and changes no decision.

**Also required:** time to first value, in steps and in minutes, with the longest unavoidable
step named. It is the number most predictive of adoption, and it cannot be improved while it is
unstated.

---

# Criterion 2 — Work broken into sequenced, independently shippable milestones

**Passes when** every milestone passes the demo test, could be shipped alone, and sits in an
order governed by a stated principle.

**Fails when** any milestone is a layer, or when the sequencing principle is absent or applied
inconsistently.

**The demo test — how to evaluate.** Read the milestone's stated outcome. Does it describe a
person doing something?

| Fails | Passes |
| --- | --- |
| "Data layer complete" | "A doctor can open a patient, dictate a note, and see it in that patient's history" |
| "Authentication implemented" | "A doctor can sign in on the clinic tablet and see only their own patients" |
| "API endpoints for consultations" | "A doctor can review last week's consultations and correct one" |

Horizontal slicing is the failure this criterion exists to catch. It feels efficient, defers
all learning to the end, and produces nothing demonstrable until everything is done — which
means the first honest feedback arrives after the budget is spent.

**Also required:**

| Check | Fails when |
| --- | --- |
| First milestone | It is not built around `08-product`'s first shippable slice |
| **Milestone Zero** | The sharpest problem is assumed and M0 is absent |
| One-way doors | An irreversible decision from `09-technology` is committed late, or its placement is unreasoned |
| Decision points | None exists, or "stop" is not among the possible outcomes |

Milestone Zero is checked here for the third time in the framework — declared in `04-problem`,
made binding in `07-strategy`, and now required to be the first row of the plan. This is the
last gate that can catch its absence.

---

# Criterion 3 — Build handoff readable by an agent with no prior context

**Passes when** every row of the cold-start check in §16 is yes.

**Fails when** any is no, or cannot be determined.

> **The cold-start test.** Could an agent or engineer open this file, with no access to the
> research and no other document, and start writing correct code today?

Not "could understand the project" — could **start**.

| Check | Fails when |
| --- | --- |
| First task nameable in one sentence | Day one is spent deciding what to do |
| References resolvable | The reader is sent to a document that does not exist |
| **No unresolved assumption in a build-blocking position** | Someone guesses, and never mentions it |
| Definition of done for M1 | "Done" is whoever's opinion prevails |
| Instrumentation identified | The product ships blind — retrofitting does not happen |
| Non-negotiables present | Security and regulatory rules become preferences |

**The blocked-work rule.** Everything genuinely undecided appears in Blocked Work with a
**named owner** and the milestone that needs it. "The team" is not an owner. This is the
mechanism by which the framework's honesty about evidence does not become a silently stalled
team: the builder can see exactly what cannot start and who owns it.

**Phrases that fail this criterion on sight:** "as discussed", "per the research", "as we
agreed", "the team will decide". The reader was not there and is not the team.

---

# Criterion 4 — Definition of done stated per milestone

**Passes when** each milestone lists the acceptance criteria that must pass, the
non-functional bar, and **what is explicitly not done**.

**Fails when** any of the three is missing.

| Fails | Passes |
| --- | --- |
| "Consultation notes working" | Four named criteria from `08-product` §7, tests passing, deployed to staging, reviewed |
| Criteria only | Criteria, plus "not done: bulk export, offline mode, audit view" |

**The third part is the one that matters in practice.** A milestone marked complete while a
reader assumed it included error handling, or migration, or an admin view, produces a dispute
no one can settle after the fact. Naming the absences settles it in advance, and it takes one
line.

**Ambiguity test.** Read each definition of done and ask whether two people could disagree
about whether it had been met. If they could, it is not a definition.

---

# Module-Specific Checks

## The Estimate Boundary Check

**Fails when** any duration appears without a stated assumed team, or when an operator's
estimate is presented as the framework's own finding.

> An estimate with no stated team is not an estimate. It is a number that will be treated as
> one.

Where team facts were not supplied, the plan carries sequence, dependency and relative size
only — and §14 says so plainly. That is not a gap in the plan; it is the honest limit of what
this framework can know.

## The Verification Coverage Check

**Fails when** a MUST requirement has no verification and its absence is not stated, or when
the plan claims a coverage level rather than listing coverage.

"Comprehensive test coverage" is the same class of claim as "intuitive interface" —
unobservable and reassuring. What is checkable: which requirements are verified, at what level,
and which are not.

**Also:** the five edge categories per requirement from `08-product` §8 must appear in the
verification strategy, or their absence must be named. Otherwise they exist in three documents
and in no running system.

## The Invented-Step Check

**Fails when** a critical path contains a step the user was never observed performing and it
is not marked as an assumption.

A plausible invented step becomes a screen, then a requirement in the next revision, and the
product acquires a process nobody actually follows.

## The Deferred-Scope Check

**Fails when** a capability deferred in `08-product` §10 appears nowhere, or when deferred
scope carries dates rather than triggers.

Dates on unvalidated scope are fiction, and they are the mechanism by which a deferral becomes
an implied commitment.

---

# Universal Gates

| | |
| --- | --- |
| U1 | Every factual claim carries exactly one evidence tag |
| U2 | `ux_flows`, `delivery_plan`, `milestones`, `build_handoff`, `qa_strategy` all in `state.outputs` |
| U3 | No claim contradicts the evidence log without superseding it |
| U4 | Every planning judgment records the alternative it rejected |
| U5 | Every unsupported duration is in `state.assumptions` with a validation method |
| U6 | Written for a reader with no access to this conversation |
| U7 | Every control declared load-bearing names where it executes, and that place exists |

U6 is not merely satisfied here — it is this module's central criterion, restated as Criterion
3. Everywhere else in the framework it protects a future reader. Here it protects the person
who starts the work.

---

# Verdict

```yaml
gate:
  module: 10-execution
  criteria:
    paths_mapped_end_to_end: pass | fail
    milestones_sliced_and_sequenced: pass | fail
    handoff_cold_start_ready: pass | fail
    definition_of_done_per_milestone: pass | fail
  module_checks:
    estimate_boundary_respected: pass | fail
    verification_coverage_stated: pass | fail
    no_invented_steps: pass | fail
    deferred_scope_carried: pass | fail
  universal: [U1, U2, U3, U4, U5, U6, U7]
  milestone_zero: required | not_required | present | ABSENT
  blocked_work: «count, all with named owners»
  verdict: pass | fail
  notes: «what failed and what was done»
```

| Verdict | Action |
| --- | --- |
| Pass | Hand to `11-growth`, `12-metrics`, `13-operations` |
| Fail | Revise, or `return to 09-technology`. Three attempts, then halt |

`milestone_zero: ABSENT` where it was required is an automatic fail. It is the framework's
last opportunity to prevent building on an unvalidated problem, and by design it is not a
judgment call.

---

> **Gate Principle**
>
> Three criteria here are about slicing, sequencing and done.
>
> The fourth is about whether a stranger can start — and it is
> the one the whole framework has been building toward.
