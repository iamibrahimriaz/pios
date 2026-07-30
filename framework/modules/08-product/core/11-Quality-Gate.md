---
Title: Quality Gate
Module: 08-product
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
  - 08-product/module.yaml
  - engine/gates.yaml
Outputs:
  - Gate verdict
Related Modules:
  - 09-technology
Tags:
  - Product
  - Quality Gate
  - Verification
---

# Quality Gate

---

# Overview

`module.yaml` states the criteria. This document explains how to evaluate each.

This gate has no human checkpoint behind it. Whatever passes here goes directly into the
PRD and the Feature Spec, and from there to whoever builds the product. There is no operator
review to catch what this gate misses.

---

# Governing Rule

> A gate is failed by default when its status cannot be determined.
>
> Uncertainty is a fail, not a pass.

---

# Criterion 1 — Every feature traces to a ranked problem

**Passes when** every requirement names a parent problem from `04-problem`, **and** every
problem above the MVP line is served by at least one requirement or has its deferral
recorded in the ledger.

**Fails when** either direction has a hole.

Both directions are required, and they fail differently:

| Direction | Failure | What it means |
| --- | --- | --- |
| Requirement → problem | **Orphan** | The requirement came from somewhere other than the research |
| Problem → requirement | **Unserved problem** | The cut was wrong, or the spec is incomplete |

**How to evaluate.** Read §13. Every row in the first table must have a non-empty problem
column. Every row in the second must have either a serving requirement or a ledger
reference.

**The deletion rule.** An orphan is deleted, not justified. An orphan can almost always be
justified — the justification is written after the fact, it sounds entirely reasonable, and
it is the mechanism by which unattached features enter products. If a requirement is genuinely
needed and no problem covers it, the problem was missed: that is a regress to `04-problem`,
not a paragraph here.

| Fails | Passes |
| --- | --- |
| "R7 — Dashboard. Rationale: users need visibility." | "R7 — Dashboard. Serves P2 (cannot tell which items are outstanding), `derived: 04-problem P2`" |

---

# Criterion 2 — Acceptance criteria testable, not aspirational

**Passes when** every criterion can be judged pass or fail by someone with no context,
observing the system.

**Fails when** any criterion requires interpretation, or contains a word that cannot be
observed.

**The banned-word scan.** Mechanical, and it should be run literally:

```
fast · performant · intuitive · easy · user-friendly · seamless
robust · reliable · appropriate · sensible · smooth · clean
```

Any hit fails the criterion until it is replaced with an observable.

**The falsifiability check.** For each criterion, name the observation that would fail it.
If none can be named, it is not a criterion.

| Fails | Passes |
| --- | --- |
| "The list loads quickly" | "Given 500 records, when the list is opened, the first page renders within 2 seconds" |
| "Errors are handled gracefully" | "Given the save fails, when the user retries, then the entered content is still present and no duplicate is created" |
| "The flow is intuitive" | "Given a first-time user, when they complete the flow unaided, then no step is repeated more than once" |

**Coverage.** Criteria must exist for failure states, not only the happy path. A requirement
whose criteria all describe success has verified half of its specification.

---

# Criterion 3 — Edge cases and failure states specified

**Passes when** every MUST requirement has all five categories worked, and the data-loss
position is stated.

**Fails when** any category is blank for any MUST requirement.

| Category | Evaluated by asking |
| --- | --- |
| Empty | Is first use, with no data, described? |
| Invalid | Is the user told something specific, and is their input preserved? |
| Failure | Is it stated whether work can be lost, and whether retry is safe? |
| Permission | Is the refusal behavior stated, and does it avoid revealing what it should not? |
| Limit / conflict | Are volume, size, concurrency and offline addressed? |

"Not applicable — «reason»" passes. A blank does not: a blank cannot be distinguished from
an omission, and the gate cannot determine its status — which by the governing rule is a fail.

**The data-loss position is not optional.** If nothing can be lost, that sentence is itself
the answer and it is worth writing.

---

# Criterion 4 — Anything out of MVP scope moved to roadmap, not dropped silently

**Passes when** every capability considered anywhere in the run appears in exactly one
place: a requirement in §7, or a row in the §10 ledger with a reason and a revisit trigger.

**Fails when** something discussed in module 07 or in the research is absent from both.

**How to evaluate.** Reconstruct the list from three sources — module 07's below-the-line
capabilities, module 04's excluded problems, and anything that surfaced during this module —
then check each against §7 and §10. A capability present in module 07 and absent from both
sections here was dropped silently.

**Also required:** confirmation in §10 that every Fast-follow and Deferred row is carried to
the roadmap output. The ledger is only worth writing if something reads it.

---

# Module-Specific Checks

These are not in `module.yaml`. They fail the gate independently, because each is a known
mechanism by which this module produces a document that satisfies all four criteria and is
still wrong.

## The Boundary Check — scope laundering

Compare every MUST requirement against module 07's `mvp_definition`.

**Fails when** any MUST maps to a capability below the line.

> Module 07 drew a line and an operator approved it. This module quietly moves it, one
> reasonable addition at a time, and the cut being built is no longer the cut approved.

Every addition is individually defensible. That is exactly why the check has to be mechanical
rather than judgmental: compare lists, do not evaluate reasonableness.

Where the core job genuinely cannot complete without an addition, the correct outcome is a
recorded **regress to 07-strategy** — not an entry in the MUST list.

## The Two-Builder Check

For each MUST requirement, ask: where would two independent engineers, given only this text,
build something different?

**Fails when** a divergence point can be named.

This replaces "is it clear?", which the author cannot answer — they already know what they
meant. Naming the divergence is checkable.

## The Confidence Check

**Fails when** §15's confidence exceeds the confidence of the problems the requirements
serve, or when a requirement derived from an assumed problem is presented as resting on an
established one.

A precise requirement built on an assumption is precise and still an assumption. This module
translates; it cannot promote.

## The Invented-Number Check

Every number, limit, retention period, regulated field and code in the document must be one
of: a cited external standard, derived from a finding, or a registered design decision.

**Fails when** a figure exists because a figure was needed.

## The Implementation-Leak Check

**Fails when** a requirement names a database, framework, library, component or screen
layout. Those decisions belong to `09-technology` and to design, and a requirement that
makes them has taken them.

---

# Universal Gates

| | |
| --- | --- |
| U1 | Every factual claim carries exactly one evidence tag |
| U2 | `prd_body`, `feature_spec`, `acceptance_criteria`, `prioritization`, `edge_cases` all in `state.outputs` |
| U3 | No claim contradicts the evidence log without superseding it |
| U4 | Every design decision records the alternative it rejected |
| U5 | Every load-bearing design decision is in `state.assumptions` with a validation method |
| U6 | Written for a reader with no access to this conversation |

U6 carries unusual weight here. This module's output is read by a builder who cannot ask
anything. Every sentence requiring context that exists only in the run is a defect.

---

# Verdict

```yaml
gate:
  module: 08-product
  criteria:
    traceability_both_directions: pass | fail
    criteria_testable: pass | fail
    edge_states_complete: pass | fail
    nothing_dropped_silently: pass | fail
  module_checks:
    boundary_no_laundering: pass | fail
    two_builder: pass | fail
    confidence_not_promoted: pass | fail
    no_invented_numbers: pass | fail
    no_implementation_leak: pass | fail
  universal: [U1, U2, U3, U4, U5, U6]
  verdict: pass | fail
  regressed_to_07: true | false
  notes: «what failed and what was done»
```

| Verdict | Action |
| --- | --- |
| Pass | Hand to `09-technology` and `14-ai-systems` |
| Fail | Revise, or `return to 07-strategy`. Three attempts, then halt |

A regress recorded here must be surfaced to the operator, even though this module has no
checkpoint. They approved a cut; if specification moved it, that is theirs to know.

---

> **Gate Principle**
>
> Nobody reviews this document before it becomes a product.
>
> This gate is the last honest reader it will have.
