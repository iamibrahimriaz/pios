---
Title: Learn — Idea
Module: 01-idea
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Orient a human learner in the Idea module — what it teaches, in what order, and what it deliberately leaves to the core layer.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 00-AI-Constitution/README.md
  - 01-idea/README.md
Outputs:
  - A reading path through the Idea module
Related Modules:
  - 02-market
  - 03-user
  - 04-problem
Tags:
  - Idea
  - Curriculum
  - Learn
---

# Learn — Idea

---

# What This Layer Is

This directory is the human curriculum for the Idea module. An executing agent never
reads it. That is deliberate: everything an agent needs in order to run the module
correctly lives in `core/`, and everything it may need to consult lives in `knowledge/`.

What remains here is the part a machine does not need and a person does — why this
stage exists, what goes wrong at it, and how to tell whether you have understood it.

> If something in this directory would change how a run behaves, it is in the wrong
> place. It belongs in `core/`.

---

# What the Module Does

The Idea module turns a vague idea into a precise, testable premise. It produces four
things: an idea brief, the questions that were asked of it, the assumptions it is
resting on, and the boundary of what is in scope.

It does not evaluate the idea. Nothing here decides whether the idea is good — that
verdict is assembled across modules 02 through 07, and no single module owns it.

---

# Reading Order

| Read | File | What you get |
| --- | --- | --- |
| 1 | `01-Why-It-Matters.md` | Why an unexamined idea is expensive |
| 2 | `02-Learning-Objectives.md` | What you should be able to do afterward |
| 3 | `10-Common-Mistakes.md` | The failures that recur at this stage |
| 4 | `16-Evaluation.md` | How to check your own work |
| 5 | `17-Reflection.md` | Questions to sit with after a real run |
| 6 | `19-Related-Modules.md` | What the module hands on, and to whom |
| 7 | `20-Future-Improvements.md` | What this module still does poorly |

The order matters less than the pairing of 3 and 4. Reading the mistakes without
testing yourself against them produces recognition rather than skill.

---

# What You Should Read Instead, and When

| If you want | Read |
| --- | --- |
| To run the module | `01-idea/core/06-Framework.md` |
| To understand a concept it uses | `01-idea/knowledge/` |
| To see it done well and badly | `01-idea/resources/` |
| To know what it produces for the engine | `01-idea/module.yaml` |

The resources directory is worth reading even as a learner. The anti-examples in
`resources/15-Anti-Examples.md` are the fastest available route to understanding what
"precise" means here, because each one looks complete until it is examined.

---

# The Habit This Module Builds

One habit, and it carries through all fourteen modules: **separating what is known from
what is believed, and labeling both.**

The evidence policy is a constitutional rule rather than a module rule, but the Idea
module is where a learner meets it for the first time — and where it is hardest,
because at this stage almost nothing is known. Writing an idea brief in which most
lines are marked as assumptions feels like failure. It is not. It is the accurate
description of a beginning.

---

> **Learn Principle**
>
> This layer explains the module. It never operates it.
>
> A person who reads only `learn/` will understand why the work matters and will not
> be able to do it. A person who reads only `core/` will be able to do it and will not
> know why any of it is there. Both directories exist because both failures are real.
