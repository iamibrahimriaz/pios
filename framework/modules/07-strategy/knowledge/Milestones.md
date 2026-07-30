---
Title: Milestones
Module: 07-strategy
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Require every milestone to teach something, and Milestone Zero where the problem is assumed.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 07-strategy/knowledge/MVP.md
Outputs:
  - roadmap
Related Modules:
  - 04-problem
  - 10-execution
Tags:
  - Strategy
  - Milestones
  - Concept
---

# Milestones

---

# What It Is

The sequence, stated at the level of what each stage **teaches**.

> Every milestone states what it teaches. A milestone that teaches nothing is a schedule entry.

And the requirement that gives this module its teeth:

> **Milestone Zero is required whenever the sharpest problem is assumed rather than verified**, or whenever
> `04-problem` recorded a declared shortfall. It validates before anything is built.

| Milestone | Teaches |
| --- | --- |
| **Zero** — validation | Whether the problem is real, before money is committed |
| **MVP** | Whether this solution solves it end to end for one person |
| **V1** | Whether anyone pays and stays |
| **V2 directions** | Selected by a trigger, not scheduled |

`10-execution` enforces this: a required Milestone Zero recorded as `milestone_zero: ABSENT` is an automatic gate
failure.

---

# When It Applies

In Move 6 (Register), alongside risks and stop conditions. The full artifact is the roadmap deliverable;
`10-execution` turns it into slices and sequence.

---

# How to Apply It Here

**Write the teaching before the content.** "Establishes whether solo GPs will accept AI-drafted notes without
line-by-line checking" is a milestone. "Build the drafting engine" is a task.

**Check the evidence standing of the sharpest problem and act on it.** If `04-problem` marked it assumed, Milestone
Zero is mandatory. This is the single most consequential rule in the module, and skipping it is the failure the
framework exists to prevent.

**Make Milestone Zero cheap and falsifiable.** It comes from `04-problem`'s validation plan — interviews, a data
pull, a Wizard of Oz prototype. If it requires building the product, it is not Milestone Zero.

**State the decision each milestone enables.** Proceed, re-scope, change segment, or stop. A milestone with no
decision attached cannot fail, and a stage that cannot fail teaches nothing.

**Order by what is most load-bearing, not by what is most buildable.** The same principle `04-problem` applies to
validation: cheapest test of the belief everything else rests on.

---

# Where It Misleads

**Milestones become dates and stop being questions.** Once a stage has a deadline attached, hitting the deadline
replaces answering the question, and a milestone that shipped on time while teaching nothing counts as a success.

**Milestone Zero gets skipped because it does not produce a product.** It produces the answer that determines whether
the product is worth producing. Skipping it converts every subsequent milestone into a bet on an untested belief.

**A validation milestone becomes a build milestone.** "Build a prototype to validate" quietly becomes "build the
prototype", and the validation question goes unasked. Naming the invalidating result in advance is the defense —
`04-problem`'s `Success-Criteria.md` covers it.

**Milestones are written for the roadmap's appearance.** Four evenly spaced stages look orderly and reflect nothing
about the work. Uneven stages are the honest shape.

**Durations get attached here.** The framework does not know the team and cannot produce durations. `Timeline.md`
sets out what it can produce instead.

---

# Related

| | |
| --- | --- |
| `Timeline.md` | Why there are no durations |
| `MVP.md`, `V1.md`, `V2.md` | The stages themselves |
| `04-problem` | Where Milestone Zero's content comes from |
| `10-execution` | Where absence of a required Milestone Zero fails the gate |

---

> **Concept Note**
>
> Every milestone names what it teaches and which decision it
> enables.
>
> Where the problem is assumed, Milestone Zero is not optional — it is
> the difference between a plan and a bet.
