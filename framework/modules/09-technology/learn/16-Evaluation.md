---
Title: Evaluation
Module: 09-technology
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Give a learner a way to test whether their technical design would survive implementation.
Audience:
  - Product Managers
  - Founders
  - Engineers
Prerequisites:
  - 09-technology/learn/10-Common-Mistakes.md
Outputs:
  - A self-assessment for technical design
Related Modules:
  - 08-product
  - 13-operations
Tags:
  - Technology
  - Evaluation
  - Learn
---

# Evaluation

---

# Overview

Technical design is assessable because most of its failures produce a specific question
somebody has to ask. The exercises below try to provoke those questions early.

---

# Exercise 1 — Generate the Schema

Take a data model and write the actual create-table statements, or ask someone else to.

**Passing looks like.** You can write every constraint without inventing anything.

**Failing looks like.** You pause at nullability or at deletion behavior. Every pause is
a decision the model left to whoever implements it.

---

# Exercise 2 — Trace an Obligation

Take one regulatory requirement from a real product's context and follow it to a
mechanism: what code or configuration actually satisfies it, and what evidence it
produces.

**Passing looks like.** A named mechanism and an artifact it leaves behind.

**Failing looks like.** A policy document. Policies are not mechanisms, and an auditor
asking "show me" is asking for the artifact.

---

# Exercise 3 — Date Every Component

Take an architecture diagram and write, next to each box, what it handles and by when,
with the basis for the number.

**Passing looks like.** At least one box has no answer, and is removed.

**Failing looks like.** Every box is justified by "we will need it as we grow." That is
the inflation defense and it fits everything.

---

# Exercise 4 — Cost One User

Compute the infrastructure cost per user at launch scale for something you have built or
planned. Then compare it with a plausible price.

**Passing looks like.** A real number, dated, with the dominant line identified.

**Failing looks like.** A number computed at scale. At launch, fixed costs dominate and
the per-user figure is much worse — which is exactly what module 06's ceiling needs to be
tested against.

---

# Exercise 5 — List the Regulated Columns

For any product handling personal data, write the actual column names that hold regulated
fields.

**Passing looks like.** A list, and the discovery that one of them flows somewhere you
had not considered — a log, an analytics event, an export.

**Failing looks like.** A category description. Three downstream checks need names.

---

# Exercise 6 — Write One Failure Mode Properly

Pick one component. Write what fails, how it is detected, what the user sees, and what
recovers it.

**Passing looks like.** The detection line is honest, including when the answer is "we
would not know."

**Failing looks like.** "Monitoring alerts the team." Which signal, what threshold, and
who specifically — module 13 needs all three.

---

# Exercise 7 — Justify a Stack by Its Weakness

Write a stack choice whose justification names something the technology is genuinely bad
at, and why that is acceptable here.

**Passing looks like.** The weakness is real and specific.

**Failing looks like.** A weakness so minor it functions as praise. "Its only downside is
that it is so flexible" is not a trade-off.

---

# Rubric

| Level | Description |
| --- | --- |
| **Not yet** | Produces an architecture diagram and a stack list; security is a posture |
| **Working** | Entities defined; obligations acknowledged; cost estimated at a convenient scale |
| **Competent** | Passes the schema test; every obligation has a mechanism or a blocker; cost computed at launch scale |
| **Fluent** | Proposes less architecture than expected and can defend it with dates, and reports a blocker rather than softening it into a risk |

---

# A Note on What Cannot Be Assessed Here

Whether the design is *right* for the product's future. Nothing here tests that, and the
framework deliberately does not try — the correct architecture depends on facts that do
not exist yet.

What these exercises test is whether the design is complete enough to build and cheap
enough to run at the scale the product will actually have. A design that passes all of
them can still be wrong in five years, and that is an acceptable trade for not being
wrong in five months.

---

> **Evaluation Principle**
>
> Every question an implementer has to ask is a gap in the design.
>
> The exercises here are ways of asking those questions before someone is blocked by
> them.
