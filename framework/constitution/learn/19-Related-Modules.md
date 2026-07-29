---
Title: Related Modules
Module: 00-constitution
Section: learn
Category: Orientation
Version: 2.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Explain how the fourteen modules relate to one another and why the sequence is ordered as it is.
Audience:
  - Product Managers
  - Founders
  - Contributors
  - Students
Prerequisites:
  - constitution/core/00-Purpose.md
Outputs:
  - Understanding of the module sequence and its dependencies
Related Modules:
  - 01-idea
  - 02-market
  - 03-user
Tags:
  - Orientation
  - Modules
  - Sequence
---

# Related Modules

---

# Overview

Product Intelligence OS is fourteen modules governed by one constitution.

The modules are not chapters that can be read in any order. Each one consumes what the
previous ones established. The sequence is the method.

> **Note on scope.** This document is written for humans learning the framework. The
> authoritative, machine-readable version of every relationship lives in each module's
> `module.yaml` — `depends_on`, `consumes`, `produces`. If this document and a
> `module.yaml` disagree, the `module.yaml` is correct.

---

# The Sequence

```
                  constitution
                       │
                       ▼
   FRAME          01-idea
                       │
                  ⏸ human checkpoint
                       │
                       ▼
   RESEARCH       02-market ──┐
                              ├──► 05-competition
                  03-user ────┤
                       │      │
                  04-problem ─┘
                       │
                       ▼
   DECIDE         06-business
                       │
                  07-strategy
                       │
                  ⏸ human checkpoint
                       │
                       ▼
   SPECIFY        08-product
                       │
              ┌────────┴────────┐
              ▼                 ▼
        09-technology     14-ai-systems
              │
              ▼
   OPERATE    10-execution
                       │
              ┌────────┼────────┐
              ▼        ▼        ▼
         11-growth 12-metrics 13-operations
                       │
                  ⏸ human checkpoint
                       │
                       ▼
                  deliverables
```

---

# The Five Stages

| Stage | Modules | Establishes |
| --- | --- | --- |
| **Frame** | 01 | What is actually being proposed |
| **Research** | 02, 03, 04, 05 | The evidence base |
| **Decide** | 06, 07 | A committed direction |
| **Specify** | 08, 09, 14 | Something precise enough to build |
| **Operate** | 10, 11, 12, 13 | Something executable, measurable and runnable |

---

# Module by Module

## 01 — Idea

**Establishes:** what the operator is actually proposing, and what only they can answer.

Takes a loosely described idea, separates the problem from the proposed solution, fixes
the context (jurisdiction, segment, buyer), surfaces assumptions, and asks the questions
that cannot be researched.

| | |
| --- | --- |
| Needs | nothing — this module runs first |
| Feeds | 02, 03 |

Every later module depends on this one being precise. A vague brief here produces
confident research pointed at the wrong target.

---

## 02 — Market

**Establishes:** the boundary of the market, its size, its direction, and the law that
governs it.

| | |
| --- | --- |
| Needs | 01 — the problem statement and the jurisdiction |
| Feeds | 05, 06 |

The regulatory landscape found here is not background reading. It reappears in 09 as
structural constraints on the data model and architecture.

---

## 03 — User

**Establishes:** who is served, what job they are trying to get done, and what they use today.

| | |
| --- | --- |
| Needs | 01, 02 |
| Feeds | 04, 05, 08, 10 |

The "what they use today" finding matters more than it looks — it names the real
competitor, which is usually the status quo rather than a product.

---

## 04 — Problem

**Establishes:** which problems are real and evidenced, and which are merely assumed.

| | |
| --- | --- |
| Needs | 03 |
| Feeds | 05, 07, 08 |

This is the honesty checkpoint of the run. Every requirement in module 08 must trace
back to a problem ranked here. A feature with no problem behind it is scope creep.

---

## 05 — Competition

**Establishes:** who already solves this, how well, and where the opening is.

| | |
| --- | --- |
| Needs | 02, 03, 04 |
| Feeds | 06, 07 |

Requires all three upstream modules because a competitor can only be judged against a
defined market, a named segment, and a real problem.

---

## 06 — Business

**Establishes:** whether a viable business exists around the solution.

| | |
| --- | --- |
| Needs | 02, 05 |
| Feeds | 07, 11 |

Separates the payer from the user. Where they differ, every later module carries two
audiences.

---

## 07 — Strategy

**Establishes:** what to build, in what order, and what deliberately not to build.

| | |
| --- | --- |
| Needs | 04, 05, 06 |
| Feeds | 08, 09, 10 |

Generates several options before choosing one, draws the MVP line, and registers the
risks. Ends at a human checkpoint — the MVP cut is a commercial commitment, not a
research finding.

---

## 08 — Product

**Establishes:** the product specification.

| | |
| --- | --- |
| Needs | 07 |
| Feeds | 09, 10, 11, 12, 14 |

The hinge of the run. Everything before it is research; everything after it is
construction.

---

## 09 — Technology

**Establishes:** the data model, interfaces, architecture and security model.

| | |
| --- | --- |
| Needs | 08 |
| Feeds | 10, 14 |

Absorbs what were once five separate concerns — architecture, database, API, security
and scalability — because in practice they are decided together and constrain each other.

---

## 10 — Execution

**Establishes:** how the specification becomes work a team or agent can start today.

| | |
| --- | --- |
| Needs | 08, 09 |
| Feeds | 13, and the Build Handoff |

Produces the UX flows and the build handoff — the artifact that makes the whole run
actionable.

---

## 11 — Growth

**Establishes:** how the product reaches, converts and retains users.

| | |
| --- | --- |
| Needs | 06, 08 |
| Feeds | 12 |

---

## 12 — Metrics

**Establishes:** what success means, measurably, and how it will be observed.

| | |
| --- | --- |
| Needs | 08, 11 |
| Feeds | the Build Handoff |

Instrumentation defined here must be built alongside the features. Retrofitted analytics
rarely happen, and the product ships blind.

---

## 13 — Operations

**Establishes:** how the product is run, supported and kept compliant after launch.

| | |
| --- | --- |
| Needs | 10 |
| Feeds | the Operations Plan |

The module most frameworks omit, which is why so many products become unmaintainable in
month three.

---

## 14 — AI Systems

**Establishes:** where AI genuinely improves the product, and how it will be evaluated.

| | |
| --- | --- |
| Needs | 08, 09 |
| Feeds | the Build Handoff |

Runs after the product is specified, deliberately. AI decided before the product is
understood becomes decoration.

---

# Dependency Rules

1. A module may not begin until every module in its `depends_on` has passed its gate.
2. A failed gate follows that module's `on_fail` target. The run does not proceed.
3. Re-entering a module appends to the evidence log. It never overwrites earlier findings.
4. A module never reads another module's prose. It reads `state.yaml`.

---

# Why the Order Is What It Is

| Ordering choice | Reason |
| --- | --- |
| User before Problem | You cannot rank a problem without knowing whose it is |
| Problem before Competition | A competitor is only relevant to a problem someone has |
| Competition before Business | Pricing without competitor pricing is guesswork |
| Strategy before Product | Deciding what to build precedes specifying it |
| Product before Technology | Architecture serves requirements, not the reverse |
| Product before AI | AI chosen before the product is understood becomes decoration |
| Metrics after Growth | Retention mechanics determine which metrics matter |

---

# Where Modules Feed the Deliverables

| Deliverable | Fed by |
| --- | --- |
| Executive Summary | 01, 02, 05, 06, 07 |
| Research Dossier | 02, 03, 04, 05 |
| Problem Validation | 04 |
| PRD | 07, 08, 12 |
| Feature Spec | 07, 08 |
| Data Model | 09 |
| API Contract | 09 |
| Architecture | 09, 10 |
| UX Flows | 03, 10 |
| Roadmap | 07, 10 |
| Risks and Assumptions | 07, and every module's assumptions |
| Success Metrics | 12 |
| Build Handoff | 08, 09, 10, 12 |

The full specification is `framework/deliverables/manifest.yaml`.

---

# Self Assessment

- Can I explain why 04 comes after 03?
- Do I know which module owns the regulatory landscape, and which module consumes it?
- Do I know where a failed gate sends the run?
- Can I name what module 08 needs before it can start?

---

> **Relationship Principle**
>
> The modules are not a table of contents.
>
> They are a dependency chain, and the order is the argument.
