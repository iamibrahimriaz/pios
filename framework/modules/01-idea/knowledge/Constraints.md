---
Title: Constraints
Module: 01-idea
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the constraint classes that shape an idea before any research begins.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 01-idea/core/06-Framework.md
Outputs:
  - Constraints recorded in the idea brief
Related Modules:
  - 02-market
  - 06-business
  - 09-technology
Tags:
  - Idea
  - Constraints
  - Concept
---

# Constraints

---

# What It Is

A limit the product must be built inside, whether or not anyone likes it.

Constraints differ from preferences in one respect: a preference can be traded away, and a
constraint cannot. Recording them separately is what stops a run producing a plan that could
never have been executed.

Five classes matter at this stage:

| Class | Example | Discovered by |
| --- | --- | --- |
| Regulatory | Records must be retained seven years | `02-market` |
| Professional | Only a registered practitioner may sign this | `02-market`, `03-user` |
| Environmental | Poor connectivity, shared devices, gloves | `03-user` |
| Commercial | The buyer's budget cycle is annual | `06-business` |
| Operator | Team of two, no infrastructure experience | The operator, and nobody else |

---

# When It Applies

In Pass 3 (Locate) and Pass 6 (Bound). Locate establishes the jurisdiction and setting, which is
where most regulatory and professional constraints come from; Bound records what the product will
not attempt.

Operator constraints are asked for here and nowhere else. If they are not asked at the start,
they arrive in module 09 as a redesign or in module 13 as an unstaffable rota.

---

# How to Apply It Here

**Never guess a regulatory constraint.** Name the jurisdiction and record the constraint as an
open question if it cannot be established. An invented regulation is worse than an admitted gap
— it reads as authoritative and gets designed around.

**Distinguish the constraint from its consequence.** "The product must be HIPAA compliant" is not
a constraint; it is a regime. The constraints are the specific obligations that regime imposes,
and `09-technology` will need each one traced to a mechanism.

**Ask the operator, explicitly.** Team size, existing systems, technologies they will not adopt,
who will run it after launch, what hours can be covered. Every one of those changes a later
module, and none can be inferred.

**Record what a constraint rules out.** A constraint with no stated consequence gets forgotten.
"Annual budget cycle" means little; "cannot be sold mid-year without a discretionary spend route"
is actionable in module 06.

---

# Where It Misleads

**Constraints are frequently assumed rather than checked.** "Doctors cannot adopt software
without trust approval" may be true in one health system and false in another. The jurisdiction
determines it, which is why Pass 3 comes before anything is bounded.

**A constraint can be invented to justify a decision already made.** "We cannot do X because of
regulation" is a convenient sentence, and it is sometimes wrong in a way nobody checks.

**Some constraints dissolve under examination.** A limit imposed by an incumbent's design, a
convention of the profession, or a technical assumption from five years ago may not be a
constraint at all — and `05-competition` and `07-strategy` are where that gets tested.

---

# Related

| | |
| --- | --- |
| `Stakeholders.md` | Who imposes each constraint |
| `Questions.md` | Where unresolved constraints go |
| `02-market` | Establishes regulatory and professional constraints properly |

---

> **Concept Note**
>
> The constraints nobody wrote down are the ones that cancel the plan.
>
> The operator's constraints are the ones nobody asks for.
