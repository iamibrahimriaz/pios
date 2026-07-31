---
Title: Evaluation
Module: 10-execution
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Give a learner a way to test whether their delivery plan and flows are usable by someone else.
Audience:
  - Product Managers
  - Founders
  - Engineers
Prerequisites:
  - 10-execution/learn/10-Common-Mistakes.md
Outputs:
  - A self-assessment for delivery planning
Related Modules:
  - 08-product
  - 13-operations
Tags:
  - Execution
  - Evaluation
  - Learn
---

# Evaluation

---

# Overview

This module has the most direct assessment available anywhere in the framework: give the
handoff to a stranger and see whether they start.

---

# Exercise 1 — The Stranger Test

Hand your build handoff to someone who was not involved. Ask them to describe what they
would do first, and where they would stop.

**Passing looks like.** They start, and their first stop is a genuine open question you
knew about.

**Failing looks like.** They stop in the first ten minutes on something you consider
obvious. Every such stop is context that exists only in your head.

---

# Exercise 2 — Draw the Cold Start

For any product, draw the first screen of a brand-new account: no data, no history, no
content.

**Passing looks like.** One clear action, and text that explains what will happen.

**Failing looks like.** An empty container with a heading. That screen ends more sessions
than any other in most products.

---

# Exercise 3 — Start Two Steps Earlier

Take a flow you have drawn and add the two steps before the software opens.

**Passing looks like.** At least one of them changes the design — the user's hands are
full, they are talking to someone, they are on a phone in a corridor.

**Failing looks like.** Nothing changes. Then the flow was already designed from the
user's situation, which is uncommon and worth confirming with the person.

---

# Exercise 4 — Demo Every Milestone

For each milestone in a plan, write the one sentence you would say while showing it.

**Passing looks like.** Every milestone produces a sentence a customer would understand.

**Failing looks like.** "The API is complete." That is a layer, and it will be 90% done
for a while.

---

# Exercise 5 — Write a Real Definition of Done

Take one milestone and write done as a checklist derived from module 08's acceptance
criteria.

**Passing looks like.** Six to ten items including edge cases, failure states,
instrumentation, and use by someone other than the builder.

**Failing looks like.** One line restating the milestone.

---

# Exercise 6 — Walk the Keyboard Path

Take a flow and complete it using only a keyboard, naming focus order at each step.

**Passing looks like.** You find a trap or an unreachable control. There is nearly always
one.

**Failing looks like.** You skip the exercise as an audit concern. Focus order is flow
structure, and a deferred audit finds violations rather than fixing designs.

---

# Exercise 7 — Locate Milestone Zero

If the run carries a declared shortfall, point at the milestone that resolves it and
check that nothing substantial is scheduled before it.

**Passing looks like.** It is first.

**Failing looks like.** It is scheduled after a release. Then it cannot change anything,
and the chain from module 04 has quietly terminated.

---

# Rubric

| Level | Description |
| --- | --- |
| **Not yet** | Produces a sequence of technical phases; flows show the happy path |
| **Working** | Vertical milestones; empty states designed after the populated one |
| **Competent** | Cold start designed first; demo test applied; done derived from acceptance criteria |
| **Fluent** | Handoff used successfully by someone who was not there, and validation sequenced ahead of building when the evidence requires it |

---

# A Note on What Cannot Be Assessed Here

Whether the plan is achievable in the time available. Nothing here tests estimation, and
the framework does not attempt to — estimates depend on a team, a codebase and a context
none of these modules can see.

What is assessable is whether the plan is *startable* and whether progress against it
will be visible. Those are the two properties that make a bad estimate survivable.

---

> **Evaluation Principle**
>
> Give it to a stranger. Watch where they stop.
>
> Every other exercise on this page is a way of predicting where that would be.
