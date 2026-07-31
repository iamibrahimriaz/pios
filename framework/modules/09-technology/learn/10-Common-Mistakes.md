---
Title: Common Mistakes
Module: 09-technology
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Name the recurring failures in technical design and what each costs.
Audience:
  - Product Managers
  - Founders
  - Engineers
Prerequisites:
  - 09-technology/learn/01-Why-It-Matters.md
Outputs:
  - Recognition of technical-design failure patterns
Related Modules:
  - 02-market
  - 13-operations
Tags:
  - Technology
  - Mistakes
  - Learn
---

# Common Mistakes

---

# Overview

Technical design failures are the most expensive in the framework, because they are the
hardest to reverse. Most of them are committed by competent people making individually
sound decisions.

---

# 1. Architecture Inflation

**What it looks like.** A queue, a cache, three services and multi-region replication,
for a product with twenty-four customers.

**Why it is tempting.** Every component solves a real problem, and building for scale
feels like professionalism. The alternative — a single application and a database —
feels naive to propose.

**What it costs.** Build time now, and an operational surface forever. Module 13 will
need a runbook, an alert, an owner and a cadence for each piece, and a solo operator
cannot carry that. The cost is not the architecture; it is the operations of the
architecture.

**Instead.** Attach a date and a number to every component. "This handles n by «date»,
based on «evidence»." Components that cannot answer are removed until they can.

---

# 2. The Obligation With No Mechanism

**What it looks like.** A security section that acknowledges a retention requirement and
contains nothing that deletes anything.

**Why it is tempting.** Acknowledging is fast and reads as responsible. Designing the
mechanism surfaces awkward questions — like what happens to backups.

**What it costs.** The obligation chain breaks in its middle link. Module 13 has nothing
to schedule, so nothing runs, and the gap appears during an audit or a customer's
security review.

**Instead.** For each obligation, name the mechanism. If no mechanism satisfies it,
record a **blocker** with an owner. The worked example's erasure-versus-backup conflict is
exactly this case, and recording it correctly is what stopped it being smoothed over.

---

# 3. The Constraint That Lives Only in Code

**What it looks like.** A uniqueness or ownership rule enforced in the application layer,
with the database permitting the violation.

**Why it is tempting.** It is faster, and the application is the only writer today.

**What it costs.** The application is eventually not the only writer — a migration, an
admin script, a background job, a second service. The invalid rows arrive silently and
are discovered much later, by which time correcting them is a data project.

**Instead.** Constraints that must always hold belong in the schema. The schema test asks
for them for this reason.

---

# 4. The Stack Asserted

**What it looks like.** "«Technology» for its performance and scalability."

**Why it is tempting.** It is true, it is unarguable, and naming a weakness feels like
undermining your own recommendation.

**What it costs.** Nobody can evaluate it, so nobody does. The choice then survives long
after the reasons for it have changed, because the reasons were never written down.

**Instead.** Name what it is bad at and why that is acceptable *here*. A justification
without a cost is an assertion with a paragraph.

---

# 5. Cost Computed at the Wrong Scale

**What it looks like.** Infrastructure cost estimated at a scale the product will reach
in year three.

**Why it is tempting.** Per-unit costs look much better at volume, and the arithmetic is
more flattering.

**What it costs.** The first arithmetic check compares against launch-scale economics.
A cost per user computed at ten thousand users tells you nothing about whether the first
fifty are affordable — and the first fifty are the ones that have to be survived.

**Instead.** Compute at launch scale, dated. Then compute at the next milestone, and note
where the shape changes.

---

# 6. Regulated Fields Described Rather Than Listed

**What it looks like.** "The system handles personal data in accordance with applicable
regulation."

**Why it is tempting.** It is true and it covers everything.

**What it costs.** Three later modules check against a list. A paragraph is not a list,
so module 12 cannot verify that events are clean and module 14 cannot verify that model
inputs are. Both checks silently pass.

**Instead.** Name the columns. It takes ten minutes and it is the single input that makes
three downstream checks possible.

---

# 7. Failure Modes as Error Handling

**What it looks like.** "Errors are logged and surfaced to the user."

**Why it is tempting.** It is what the code does.

**What it costs.** Module 13 derives runbooks from failure modes. "Errors are logged"
produces no runbook, so when the queue backs up at 3am there is nothing to follow.

**Instead.** Enumerate the failures: what fails, how it is detected, what the user sees,
what recovers it. Each one becomes a runbook, and the enumeration is where the design
gaps surface.

---

# 8. Recovery Objectives Without a Rehearsal

**What it looks like.** A stated recovery point and recovery time.

**Why it is tempting.** The numbers are easy to write and hard to test.

**What it costs.** An untested restore is a hypothesis. The most common discovery on the
first real attempt is that the backup was incomplete, or that the restore takes an order
of magnitude longer than stated.

**Instead.** State the objectives and hand module 13 a rehearsal cadence. That is why the
worked example's compliance table has "restore rehearsal, quarterly, measured time" in
it.

---

# The Pattern

| Mistake | Underlying move |
| --- | --- |
| Inflation | Designing for a scale nobody evidenced |
| Obligation unmechanized | Acknowledging instead of building |
| Constraint in code | Choosing speed over durability |
| Stack asserted | Recommending without comparing |
| Wrong-scale cost | Choosing the flattering arithmetic |
| Fields described | A paragraph where a list was needed |
| Failure as error handling | Describing the code rather than the operation |
| Untested recovery | Stating a number that has never been checked |

Five of the eight are the same underlying move: **producing something that reads as
addressed and does not exist.** In a technical document that is unusually easy, because
the vocabulary is credible and the reader is often not equipped to check.

---

> **Mistakes Principle**
>
> This module's outputs are the ones a non-technical reader is least able to challenge.
>
> That is exactly why the framework asks for lists, mechanisms and numbers here rather
> than for postures.
