---
Title: Milestones
Module: 08-product
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Produce the first shippable slice, and leave sequencing and dates to module 10.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 08-product/knowledge/features/Dependencies.md
Outputs:
  - First shippable slice within prioritization
Related Modules:
  - 07-strategy
  - 10-execution
Tags:
  - Product
  - Milestones
  - Concept
---

# Milestones

---

# What It Is

What this module contributes to milestone planning — which is narrower than it appears.

| Owned here | Owned elsewhere |
| --- | --- |
| **The first shippable slice** — the smallest subset a real user could actually use | Milestone definitions and what each teaches — `07-strategy` |
| Dependency order between requirements | Sequence, parallelization and blocked work — `10-execution` |
| Which requirements are inseparable | Dates and durations — nobody; the framework does not produce them |

The first shippable slice is the load-bearing output. It is derived from behavior and dependencies, and it is what
`10-execution` plans around.

---

# When It Applies

At the end of Move 5 (Order), once scoring and dependencies exist.

---

# How to Apply It Here

**Define the slice by completeness, not by size.** A real user completing a real job with only what is in the slice.
That is the same standard as `07-strategy`'s end-to-end test, applied to a subset of the MVP.

**Cut vertically.** A slice containing three half-built capabilities cannot be used by anyone. `10-execution`'s demo
test is the check, and it is easier to pass if the slice was cut this way to begin with.

**Name what is inseparable, and why.** Two requirements that cannot ship apart are one unit for sequencing purposes.
Recording it prevents `10-execution` planning a split that does not exist.

**State the dependency order, not the schedule.** What must exist before what is a fact about the requirements. When it
happens is not this module's, and `07-strategy`'s `Timeline.md` explains why it is nobody's.

**Carry Milestone Zero forward untouched.** If `07-strategy` required it because the sharpest problem is assumed, it
precedes everything here — including the first slice.

---

# Where It Misleads

**Milestone planning gets done here because the requirements are freshest.** It produces a plan without knowledge of the
team, and `10-execution` then either discards it or inherits its assumptions.

**Dates attach themselves to the first slice.** The moment a slice acquires a duration it becomes a commitment made by a
document that has never met the builders.

**The slice is defined as the easiest requirements.** Easy and complete are different sets. A slice of cheap work that
completes no job teaches nothing when it ships.

**Dependencies are asserted rather than derived.** A claimed dependency that does not exist serializes work
unnecessarily. `features/Dependencies.md` distinguishes real dependencies from assumed ones.

**Milestone Zero gets folded into the first slice.** Validation is not a build increment. Merging them means the
question goes unanswered while the building starts, which is the exact failure the requirement exists to prevent.

---

# Related

| | |
| --- | --- |
| `features/Dependencies.md` | What genuinely blocks what |
| `features/Feature-Prioritization.md` | The scoring the order rests on |
| `07-strategy` | Milestone definitions, Milestone Zero, the estimate boundary |
| `10-execution` | Sequencing, slicing and the demo test |

---

> **Concept Note**
>
> Produce one thing: the smallest subset a real user could actually
> use.
>
> Not the cheapest subset — the smallest complete one.
