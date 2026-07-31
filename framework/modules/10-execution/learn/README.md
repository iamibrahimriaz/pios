---
Title: Learn — Execution
Module: 10-execution
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Orient a human learner in the Execution module — where a specification becomes something someone can start today.
Audience:
  - Product Managers
  - Founders
  - Engineers
Prerequisites:
  - 09-technology/learn/README.md
  - 10-execution/README.md
Outputs:
  - A reading path through the Execution module
Related Modules:
  - 08-product
  - 09-technology
  - 13-operations
Tags:
  - Execution
  - Curriculum
  - Learn
---

# Learn — Execution

---

# What This Layer Is

The human curriculum for the Execution module. An executing agent does not read it.

---

# What the Module Does

It converts the specification into something a team or an agent can start building
today. It produces UX flows, a delivery plan, milestones, a build handoff, and a QA
strategy.

Its knowledge layer is entirely about user experience, which surprises people who expect
project management. That is deliberate: sequencing work is the easy half. Knowing what
the first screen shows when there is no data yet is the half that decides whether
anything gets used.

---

# The Two Named Tests

**The demo test.** Can this milestone be shown to someone? A milestone that cannot be
demonstrated is a work package, not a milestone — and work packages hide slippage
because there is nothing to look at.

**The cold-start test.** What is on screen the very first time, before any data exists?
This is the most-used screen in a new product and the least designed. Every flow drawn
from a populated state is a flow nobody's first session will match.

---

# Where Milestone Zero Is Sequenced

If module 04 declared a shortfall and module 07 made it binding, this is where it gets
sequenced **first** — before any feature work. The chain then continues into module 11,
which withholds acquisition spend until it resolves.

> A validation milestone scheduled after the build is not Milestone Zero. It is a
> retrospective.

---

# Reading Order

| Read | File | What you get |
| --- | --- | --- |
| 1 | `01-Why-It-Matters.md` | Why flows and sequencing are the same problem |
| 2 | `02-Learning-Objectives.md` | What you should be able to do afterward |
| 3 | `10-Common-Mistakes.md` | Where handoffs and milestones fail |
| 4 | `16-Evaluation.md` | How to check your own plan |
| 5 | `17-Reflection.md` | Questions after a real run |
| 6 | `19-Related-Modules.md` | What this module hands to build and to operations |
| 7 | `20-Future-Improvements.md` | What this module still does poorly |

---

# What You Should Read Instead, and When

| If you want | Read |
| --- | --- |
| To run the module | `10-execution/core/06-Framework.md` |
| UX concepts — flows, states, accessibility, error recovery | `10-execution/knowledge/` |
| To see a handoff that needs its author present | `10-execution/resources/15-Anti-Examples.md` |

---

> **Learn Principle**
>
> The measure of a build handoff is whether an agent or a new engineer with no prior
> context can start.
>
> Everything in this module is written against that standard, including the parts that
> look like project management.
