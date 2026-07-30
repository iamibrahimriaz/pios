---
Title: Backend
Module: 09-technology
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Choose the server-side layer by where the rules and the obligations are enforced.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/Tech-Stack.md
Outputs:
  - Backend choice within tech_stack
Related Modules:
  - 08-product
  - 13-operations
Tags:
  - Technology
  - Backend
  - Concept
---

# Backend

---

# What It Is

The layer that holds the operations, the rules and the enforcement points.

What decides the choice is not language preference but what has to happen here:

| Requirement of the backend | Consequence for the choice |
| --- | --- |
| Enforce authorization at a single located point | The framework must make that point unavoidable, not optional |
| Encode constraints alongside the schema | Migration and validation tooling matter more than syntax |
| Run scheduled obligations — retention, compliance jobs | A job runner is part of the choice, not an addition |
| Produce audit entries reliably | Writing an audit record must be as hard to omit as the write itself |
| Be operable by whoever is on call | `13-operations` inherits this directly |

---

# When It Applies

In Move 5 (Choose), against the operations derived in Move 1 and the controls designed in Move 4.

---

# How to Apply It Here

**Locate authorization in one place and choose accordingly.** Move 4 requires the enforcement point to be *named*. A
backend where permission checks are scattered across handlers cannot satisfy that, whatever its other merits.

**Match the runtime to the workload shape.** Long-running requests, streaming responses, background processing and
scheduled work each impose different constraints, and AI operations frequently need the first two.

**Include the job runner in the decision.** Retention, compliance evidence and cleanup are scheduled obligations from Move
4. A backend with no scheduling story defers a legal requirement to improvisation.

**State the trade-off in ecosystem terms where that is the real reason.** Available libraries for the domain — payment,
health-record standards, document handling — are a legitimate deciding factor and should be named as such.

**Check it against the cost ceiling.** Runtime, hosting model and idle cost all feed the per-user arithmetic against
`06-business`.

---

# Where It Misleads

**The choice is made on language preference and justified on performance.** For almost every product at launch scale, the
runtime is not the constraint — the database and the network are.

**Framework conventions become the data model.** A backend whose ORM shapes the schema inverts Move 2, where the data
model is derived from requirements before technology is chosen.

**Business rules end up in three places** — the database, the application and the interface — because no layer was
designated. Move 2's constraint discipline exists to prevent it: where a rule can be a `CHECK`, it should be.

**Scheduled work is treated as operational tooling.** Retention and compliance jobs are mechanisms satisfying
obligations, and their absence is a blocker rather than a gap.

**Operability is assumed.** A backend requiring skills the operator does not have is an unrunnable design, and it fails
Move 5's operability check regardless of how well it fits on paper.

---

# Related

| | |
| --- | --- |
| `Tech-Stack.md` | The justification format every choice needs |
| `api/Endpoints.md` | The surface the backend implements |
| `security/Authorization.md` | The enforcement point that must be locatable |
| `13-operations` | Who runs it |

---

> **Concept Note**
>
> Choose the backend by where authorization is enforced and how
> scheduled obligations run.
>
> The runtime is rarely the constraint. The scattered permission check
> always is.
