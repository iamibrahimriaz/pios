---
Title: Core Principles
Module: 10-execution
Section: core
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the principles that govern judgment when planning delivery.
Audience:
  - AI Agents
  - Delivery Leads
  - Founders
Prerequisites:
  - constitution/core/03-Core-Principles.md
Outputs:
  - Consistent delivery judgment
Related Modules:
  - 12-metrics
Tags:
  - Execution
  - Principles
---

# Core Principles

---

# Principle Statement

> A plan is not a description of the work.
>
> It is an instruction that someone who was never here can follow.

---

# Principle 1 — Every Milestone Ends With Something a Person Can Do

The demo test: at the end of this milestone, what can you show a real user doing?

If the answer names a layer — the schema, the API, the design system — it is not a milestone.
It is a stage of one, and it teaches nothing when it completes.

---

# Principle 2 — Slice Vertically, Even Though It Repeats Work

Horizontal slicing is more efficient per layer and defers every piece of learning to the end.

Vertical slicing revisits some work across milestones and is still faster, because information
starts arriving in week two rather than after the budget is spent.

---

# Principle 3 — Independently Shippable Means It Could Stop There

Not that the product would be complete. That it would be **usable**.

A milestone that leaves the product in a state nobody could use is a dependency, and it should
be inside another milestone rather than beside it.

---

# Principle 4 — State the Sequencing Principle, Then Hold It

De-risk earliest, learn earliest, value earliest, dependency order. These conflict.

A plan that switches between them silently looks deliberate and cannot be re-examined, because
no one can tell what it was optimizing for.

---

# Principle 5 — Validate Before Building, Where the Problem Is Assumed

Milestone Zero is first, built from `04-problem`'s validation plan.

This is the third module in which the mechanism appears — declared in 04, made binding in 07,
and here it becomes the first row of the actual plan. It is the framework's last chance to stop
work starting on an unproven problem.

---

# Principle 6 — Commit One-Way Doors Early, and Say Why There

`09-technology` named the decisions that cannot be cheaply reversed. Each must be committed
early enough to be built on and late enough to be informed.

A plan that commits an irreversible decision in its last milestone has sequenced backwards, and
usually nobody noticed because the reasoning was never written.

---

# Principle 7 — Done Includes What Is Not Done

Acceptance criteria, the non-functional bar, and the absences.

Without the third, a milestone is marked complete while one reader assumed it covered error
handling and another did not — a dispute nobody can settle afterwards and one line prevents.

---

# Principle 8 — A Definition of Done Two People Read Differently Is Not One

The test is not whether it sounds clear. It is whether two readers could disagree about whether
it has been met.

---

# Principle 9 — The Framework Does Not Know the Team

Sequence, dependency and relative size can be established from the documents. Duration,
velocity and dates cannot.

An estimate with no stated team is not an estimate. It is a number that will be treated as one,
by someone reading it a month later with the caveat long forgotten.

---

# Principle 10 — Paths Include Their Failures

A critical path that stops at success is half a path.

Products are lost at the first error, not at the last feature — and for every failure, whether
the user's work is preserved is the question that decides whether they return.

---

# Principle 11 — Every Screen Has Unpopulated States

Empty, loading, error, permission.

A screen specified only in its populated state ships broken, because the populated state is the
one that occurs least often at the beginning of a product's life.

---

# Principle 12 — Design Principles Cite Their Findings

"The user is interrupted constantly" produces "every action must survive being abandoned
halfway", which constrains real decisions.

"Keep it simple" derives from nothing, constrains nothing, and survives every review.

---

# Principle 13 — Never Invent a Step

A plausible step inserted into a flow becomes a screen, then a requirement in the next revision,
and the product acquires a process nobody actually follows.

Where a step is genuinely unknown, mark it as an assumption. An admitted gap can be validated;
an invented step cannot, because nobody knows which step to doubt.

---

# Principle 14 — Name What Is Not Tested

Every MUST requirement gets a verification, or its exclusion is stated.

Do not claim a coverage level. "Comprehensive coverage" is unobservable and reassuring, which is
the same combination as "intuitive interface".

---

# Principle 15 — Blocked Work Has a Person's Name Against It

Everything genuinely undecided goes to Blocked Work, with a named owner and the milestone that
needs it.

"The team" is not an owner. Unowned blocked work is unstarted work that nobody is waiting for.

---

# Principle 16 — Nothing Unresolved Sits in the Build Instructions

An assumption in the instructions becomes a decision made by whoever is building, in the dark,
and never mentioned again.

That is the mechanism by which nine modules of careful evidence tracking are silently discarded
in a single afternoon.

---

# Principle 17 — The Handoff Assumes No Context and No Other Document

"As discussed", "per the research", "as we agreed" — the reader was not there.

References for depth are fine. Essentials are carried inline, because nobody opens five
documents before starting.

---

# Principle Hierarchy

```
Paths mapped, failures included
   ↓
Sliced vertically into demonstrable units
   ↓
Sequenced by a stated principle, M0 first if required
   ↓
Done defined, absences named
   ↓
Verification assigned, exclusions stated
   ↓
Blocked work owned, instructions clean
   ↓
Startable by a stranger
```

Each level depends on the one above. Slicing before mapping produces milestones that miss parts
of the route; defining done before slicing applies "done" to layers.

---

# Common Violations

- Milestones named after layers.
- Nothing demonstrable until the end.
- A milestone that leaves nothing usable.
- No stated sequencing principle.
- Building before validating an assumed problem.
- An irreversible decision committed last.
- Definitions of done with no absences.
- "Done" that two readers interpret differently.
- Durations with no team behind them.
- Paths with no failure rows.
- Screens with only their populated state.
- Generic design principles.
- Invented workflow steps.
- Claimed coverage levels.
- Blockers owned by "the team".
- Assumptions inside build instructions.
- "As discussed" in a handoff.

---

# Self Assessment

- Does every milestone pass the demo test?
- Could delivery stop after any milestone and leave something usable?
- Is my sequencing principle stated and consistently applied?
- Is M0 first, where the problem is assumed?
- Are the one-way doors early, with reasoning?
- Does every definition of done name its absences?
- Did I state a duration without knowing the team?
- Does every failure row say whether work is preserved?
- Does every screen have four states?
- Does every design principle cite a finding?
- Did I invent any step?
- Does every blocker have a name against it?
- Is anything unresolved still in the instructions?

---

> **Core Principle**
>
> Every earlier module could be reread by whoever needed it.
>
> This one is read once, by someone who then starts typing.
