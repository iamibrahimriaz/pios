---
Title: Purpose
Module: 09-technology
Section: core
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define why the Technology module exists and what it establishes for the rest of the run.
Audience:
  - AI Agents
  - Engineers
  - Founders
Prerequisites:
  - constitution/core
  - 08-product gate passed
Outputs:
  - Shared understanding of what this module establishes
Related Modules:
  - 10-execution
  - 13-operations
  - 14-ai-systems
Tags:
  - Technology
  - Purpose
  - Foundation
---

# Purpose

---

# Overview

Module 08 said what the product does. This module says what exists.

Entities, columns, constraints, operations, controls, components, limits. None of it is
invented — all of it is implied by the requirements, and the work is finding it and making it
exact.

This module produces four of the framework's sixteen deliverables, more than any other. It is
also the last module whose output becomes code rather than plans.

---

# Purpose Statement

> Define the technical shape precisely enough to build from, sized to the business
> the research described — and no larger.

---

# Why This Module Exists

Three failures dominate technical design work.

**The document that requires its author.** A design full of prose and short of types.
Relationships without cardinality, columns without nullability, endpoints described rather
than specified. It reads as complete and cannot be built from without a conversation.

**Compliance as intention.** "The system will be compliant with «regime»." An obligation
restated as a commitment, with no mechanism, no enforcement point, and no citation. It reads
as an answer and specifies nothing.

**Architecture inflation.** A design sized for a scale the business does not project, built
from components each of which is individually defensible. It costs more than the business
model can carry and takes longer to build than the roadmap allows.

The module's structure — derive before modeling, technology chosen last, obligations traced to
mechanisms, and two arithmetic checks against the business model — exists to make each of
these visible.

---

# The Judgment This Module Makes

| Output | What it commits |
| --- | --- |
| `data_model` | What exists, in what shape, with what rules — the hardest thing to change later |
| `api_contract` | How every capability is reached, and what happens when it fails |
| `architecture` | The shape of the system and its boundaries |
| `security_model` | What is prevented, by what mechanism, enforced where |
| `scalability_plan` | The load it is built for, what breaks first, and what it is not built for |
| `tech_stack` | What it is built with, and what each choice is worse at |

---

# Core Objectives

- Derive entities and operations from the requirements, inventing nothing.
- Model the data to the point where a schema could be generated with no questions asked.
- Give every capability a reachable operation, and every operation a capability.
- Turn every regulatory obligation into a named mechanism at a named enforcement point.
- Choose technology last, with the trade-off of each choice stated.
- Size to the business model's own figures, and say what is not built for.
- Keep the cost per user inside the ceiling the business model set.

---

# What AI Should Learn Here

- Technology is chosen last. Every failure in this module comes from choosing early.
- A constraint is a business rule enforced where it cannot be forgotten.
- Forbidden state transitions matter more than legal ones — that is where the bugs live.
- "Compliant" is not a control. Obligation, mechanism, enforcement point, citation.
- Authorization described but not located is the same as absent.
- Version-specific claims are the most reliably wrong statements in technical writing.
- Most decisions are cheap to reverse. The few that are not deserve most of the evidence.
- A design the business cannot afford to run has invalidated the business model, not the
  budget.

---

# The Register Problem

Each module in the specify stage has a characteristic way of quietly exceeding its mandate.
Module 08's was scope laundering. This module's is its scale equivalent:

> **Architecture inflation.** Designing for a scale that does not exist. Every component is
> individually justifiable; together they exceed what the business can carry and what the
> roadmap allows.

It is difficult to argue against in prose, because each element has a real justification —
resilience, separation of concerns, future flexibility. So the module does not argue. It
checks arithmetic:

| Check | Against |
| --- | --- |
| **Load check** | The launch and target figures from `06-business` |
| **Cost check** | The cost-to-serve ceiling from `06-business` |

The cost check is the sharper one, and it has a consequence beyond this module. A design whose
cost per user exceeds what the business model can carry has invalidated the business model —
and this is the first module positioned to notice. The resolution is a regress to
`06-business` or `07-strategy`, not a quietly absorbed inconsistency.

---

# Scope

**This module covers**

- Entities, columns, constraints, indexes, relationships, state machines
- Data classification, retention and audit requirements
- The interface contract, error taxonomy and failure responses
- Authentication, authorization, encryption, secrets, audit, backup and deletion
- The regulatory obligation trace
- Architecture shape, components and boundaries
- Technology choices and their trade-offs
- Capacity, bottlenecks, reliability and cost
- Environments and system observability

**This module does not cover**

| Not here | Belongs to |
| --- | --- |
| What the product does | `08-product` — settled |
| What is in the MVP | `07-strategy` — binding |
| Model prompting, evaluation, fallback behavior | `14-ai-systems` |
| Build sequence, resourcing, dates | `10-execution` |
| On-call, runbooks, support processes | `13-operations` |
| Product metric definitions and targets | `12-metrics` |
| Visual design | Design, from module 08's behavior |

---

# Position in the Run

```
08-product → [ 09-technology ] → 10-execution
                               → 13-operations
           → 14-ai-systems ────→
```

`14-ai-systems` runs alongside and reads from this module. Where a requirement is served by a
model rather than by deterministic logic, this module still owns the data it touches and its
position in the architecture.

---

# What This Module Hands Forward

| Output | Consumed by | Used for |
| --- | --- | --- |
| One-way doors | 10 | What must be right first, and what can wait |
| `architecture` | 10, 13, 14 | Sequencing, operations, model placement |
| `security_model` | 13 | Runbooks, incident response, access management |
| `data_model` | 14 | What data a model may touch |
| Observability points | 12 | Where instrumentation goes |
| `data_model` | `05-Data-Model.md` | The shipped data model |
| `api_contract` | `06-API-Contract.md` | The shipped API contract |
| `architecture`, `security_model`, `scalability_plan`, `tech_stack` | `07-Architecture.md` | The shipped architecture |
| Stack, first slice, starting points | `12-Build-Handoff.md` | The shipped build handoff |

The **one-way doors** are the most important thing this module tells `10-execution`.
Decisions that cannot be cheaply reversed determine what must be sequenced early; everything
else can be deferred with confidence.

---

# The Reader

Module 08 was written for a builder who cannot ask questions. This one is read by that builder
at the moment they start typing.

> Every question this document leaves open is answered by whoever is holding the keyboard,
> without any of the research, and then filled with real data.

That is why the data model's bar is "schema-generatable with no follow-up questions" rather
than "clear", and why an entity invented here to paper over a vague requirement is more
damaging than an admitted gap. The invented entity is indistinguishable from a derived one
once it is written down.

---

# Success Criteria

- A data model from which a schema could be generated with no questions asked.
- Both traceability directions clean: no orphan entities, no unmodeled requirements.
- Every MUST requirement reachable; every operation serving one.
- Every edge case from module 08 present as a failure response.
- Every regulatory obligation traced to a mechanism and an enforcement point.
- Every technology choice stating what it is worse at.
- Cost per user inside the ceiling, with the arithmetic shown.
- What is deliberately not built, and not built for, stated.

---

# Self Assessment

- Did I derive from the requirements, or model from a picture of the product?
- Could a builder generate the schema without asking me anything?
- Does every obligation name a mechanism and a place?
- Did I choose the technology before or after writing the justification?
- Is this design sized for the business the research described?
- Is the cost inside the ceiling?
- What did I invent to cover a gap?

---

> **Purpose Principle**
>
> Eight modules of judgment arrive here and leave as a schema,
> a contract and a set of controls.
>
> After this, the framework stops describing the product and
> starts planning the work.
