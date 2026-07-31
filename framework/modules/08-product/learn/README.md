---
Title: Learn — Product
Module: 08-product
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Orient a human learner in the Product module — where a decision becomes something two people would build the same way.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 07-strategy/learn/README.md
  - 08-product/README.md
Outputs:
  - A reading path through the Product module
Related Modules:
  - 07-strategy
  - 09-technology
  - 10-execution
Tags:
  - Product
  - Curriculum
  - Learn
---

# Learn — Product

---

# What This Layer Is

The human curriculum for the Product module. An executing agent does not read it.

---

# What the Module Does

It specifies the product precisely enough to be built. It produces the PRD body, a
feature specification, acceptance criteria, prioritization, and edge cases.

Module 07 chose. This module writes down what was chosen, in a form that does not
require the author to be in the room.

---

# The Named Test

**The two-builder test.** Give the specification to two competent builders who have never
spoken to each other. If they produce materially different things, the specification is
underspecified — regardless of how complete it looks.

That test is more demanding than it sounds, and most of what this module teaches is the
set of habits that pass it: acceptance criteria that are observable, edge cases that are
enumerated rather than gestured at, and requirements that say what happens when the
thing goes wrong.

---

# The Two Requirements That Do the Work

**Every feature traces to a ranked problem.** This is the framework's requirement trace,
and it terminates here. A requirement with no trace is an orphan — and an orphan
requirement always arrives with the most persuasive rationale in the document, because
it needs one.

**Anything out of MVP scope moves to the roadmap, not into silence.** Dropping is a
decision. Silence is an omission that reappears as a surprise.

---

# The Named Failure

**Scope laundering** — an MVP cut where nothing is actually cut, and everything remains
under a phase label. Module 07 is where it starts; this module is where it becomes
concrete, because a phase-two list of everything is inherited as a requirement set.

---

# Reading Order

| Read | File | What you get |
| --- | --- | --- |
| 1 | `01-Why-It-Matters.md` | Why specification is a distinct skill |
| 2 | `02-Learning-Objectives.md` | What you should be able to do afterward |
| 3 | `10-Common-Mistakes.md` | Orphans, aspirational criteria, missing edges |
| 4 | `16-Evaluation.md` | How to check your own spec |
| 5 | `17-Reflection.md` | Questions after a real run |
| 6 | `19-Related-Modules.md` | What modules 09, 10 and 12 inherit |
| 7 | `20-Future-Improvements.md` | What this module still does poorly |

---

# What You Should Read Instead, and When

| If you want | Read |
| --- | --- |
| To run the module | `08-product/core/06-Framework.md` |
| To understand a specification concept | `08-product/knowledge/` |
| To understand feature-level concerns | `08-product/knowledge/features/` |
| To see a spec that fails the two-builder test | `08-product/resources/15-Anti-Examples.md` |

Five files in this module's knowledge layer are named after things the module does not
own — KPIs, success metrics, milestones, vision, mission. Each is scoped to state only
what module 08 contributes. `Mission.md` is the interesting one: a present-tense mission
can be *falsified* by the requirement list, which is the only operational use a mission
statement has.

---

> **Learn Principle**
>
> A specification is not a description of a product. It is a set of constraints tight
> enough that two people building independently converge.
>
> Everything in this module is in service of that one property.
