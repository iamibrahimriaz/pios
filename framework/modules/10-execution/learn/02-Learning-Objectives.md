---
Title: Learning Objectives
Module: 10-execution
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define what a learner should know and be able to do after the Execution module.
Audience:
  - Product Managers
  - Founders
  - Engineers
Prerequisites:
  - 10-execution/learn/01-Why-It-Matters.md
Outputs:
  - Delivery and UX competencies
Related Modules:
  - 08-product
  - 13-operations
Tags:
  - Execution
  - Objectives
  - Learn
---

# Learning Objectives

---

# Overview

> After this module you should be able to draw a flow that starts where the user's
> situation starts, sequence work into milestones somebody could watch, and write a
> handoff that survives your absence.

---

# Knowledge Objectives

You should understand:

- What a flow contains beyond the happy path: entry points, empty states, in-progress
  states, failure states, and where the user lands afterward
- What the **demo test** requires of a milestone
- What the **cold-start test** covers — no data, no history, no other users, no content
- Why a milestone should be a vertical slice rather than a layer
- What a definition of done contains, and where it comes from
- Where Milestone Zero sits and why it is first

---

# Thinking Objectives

The shift is from *what are we building* to *what can someone start, and what will they
see*.

Instead of asking:

> "What order should we build this in?"

ask:

- Where does the user arrive from, and what were they doing a moment before?
- What does this screen show before anything exists?
- Can I show this milestone to someone who is not on the team?
- What would a builder with no context have to ask me?
- What must be learned before anything else is built?

---

# Skill Objectives

You should be able to:

- Map a critical path end to end, starting outside the software
- Specify empty, loading, partial and error states for every screen that has them
- Break work into independently shippable, demonstrable milestones
- Write a definition of done per milestone, derived from module 08's criteria
- Produce a handoff that names the contract, the sequence and the decisions
- Sequence a validation milestone ahead of feature work when the run requires one

---

# Analytical Objectives

You should develop the ability to:

- Notice a flow that begins at a screen rather than at a situation
- Recognize a milestone that is a layer — "the API," "the database"
- Spot a definition of done that restates the task
- Tell an accessible flow from one that merely has no known violations

---

# Judgment Objectives

**How thin to slice.** A milestone should be demonstrable and independently shippable.
Slicing thinner than that produces overhead; thicker produces the two-month 90%.

**What the handoff includes.** Everything a builder needs and nothing that re-litigates a
settled decision. The reasoning belongs, briefly — a builder who does not know why
something was decided will eventually re-decide it.

---

# You Have Learned This When

| Signal | What it indicates |
| --- | --- |
| Your flows start before the software opens | Module 03's workflow is being used |
| You design the empty state first | The cold-start test is habitual |
| Your milestones are things you could show a customer | The demo test is applied |
| Your handoff has been used by someone who was not there | It meets the standard |
| A validation milestone comes before feature work when it should | The Milestone Zero chain is carried |

---

# What This Module Does Not Teach You

It does not teach visual design — flows are structure, not appearance. It does not teach
engineering estimation beyond sequencing. It does not teach operations; module 13 takes
over at launch.

---

> **Objectives Principle**
>
> The skill is producing something a stranger can act on.
>
> Every other property of a delivery plan — completeness, elegance, ambition — is
> secondary to that one.
