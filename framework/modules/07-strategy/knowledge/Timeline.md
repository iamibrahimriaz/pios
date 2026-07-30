---
Title: Timeline
Module: 07-strategy
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: State the estimate boundary — sequence and relative size, never durations.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 07-strategy/knowledge/Milestones.md
Outputs:
  - Sequence within roadmap
Related Modules:
  - 06-business
  - 10-execution
Tags:
  - Strategy
  - Timeline
  - Concept
---

# Timeline

---

# What It Is

The boundary on what this framework may claim about time.

> **The framework does not know the team. It cannot produce durations.**

What it can produce:

| Can | Cannot |
| --- | --- |
| Order — what must precede what | Dates |
| Dependencies — what blocks what | Weeks or months per milestone |
| Relative size — larger, comparable, smaller | Hours or story points |
| The critical path through the sequence | A delivery forecast |
| What is parallelizable | A team's velocity |

This is a limit on the framework, not a gap in it. A duration requires knowing who is building, how many of them,
how experienced they are in this domain, and what else they are doing. None of that is available here, and inventing
it produces a plan against which real progress will be measured.

---

# When It Applies

Throughout Move 6, and inherited by `10-execution`, which restates the same boundary when it sequences work.

---

# How to Apply It Here

**Express size relatively and mark the basis.** "Larger than the MVP, smaller than the integration work" is
defensible. Anything in weeks is not.

**Show dependencies explicitly, because they are the real constraint.** What cannot start until something else
finishes is a fact about the work rather than about the team, and it is the most useful scheduling content available.

**Identify what is parallelizable.** It changes the shape of a plan more than any estimate, and it is derivable from
dependencies alone.

**Let the operator add durations.** They know the team. The framework's job is to hand them a correctly ordered
sequence with sizes and dependencies; converting that into dates is theirs, and the human checkpoint is where it
happens.

**Where time genuinely constrains, name the external clock.** A regulatory deadline, a budget window, a contract
renewal, a runway limit from `06-business`. Those are dated facts about the world, not estimates, and they belong in
the plan.

---

# Where It Misleads

**An invented duration acquires authority immediately.** "Six weeks for the MVP" written by a framework that has
never met the team becomes the number the team is held to. It is the same laundering problem as an invented market
figure, with a deadline attached.

**Relative sizes get read as durations.** "Small" becomes a week in the reader's head. Stating the basis — relative to
what — limits the drift.

**Absence of dates is read as absence of planning.** Sequence, dependencies and relative size are the plan. Dates are
a projection layered on top, and layering them on badly makes the plan worse rather than more complete.

**The runway constraint gets omitted because it is uncomfortable.** `06-business` established the money and the sales
cycle. If the sequence cannot fit inside the runway, that is the most important finding in the module and it belongs
in the risk register.

**Padding is added to make estimates safe.** Padding an invented number produces a larger invented number. The
correct response to not knowing is to say what is known — the order — and stop.

---

# Related

| | |
| --- | --- |
| `Milestones.md` | What each stage teaches |
| `risks/Financial.md` | Runway against sequence |
| `06-business` | Where the money and the sales cycle are established |
| `10-execution` | Where the same boundary is restated |

---

> **Concept Note**
>
> Order, dependencies and relative size. No dates.
>
> A duration invented by something that has never met the team is a
> deadline someone else will be held to.
