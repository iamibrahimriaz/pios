---
Title: Why It Matters
Module: 03-user
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Explain why the user stage is about observed behavior rather than described audiences.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 03-user/README.md
Outputs:
  - Understanding of why the user stage exists
Related Modules:
  - 04-problem
  - 05-competition
  - 10-execution
Tags:
  - User
  - Jobs to Be Done
  - Learn
---

# Why It Matters

---

# Overview

Nearly every product document contains a section about users, and nearly all of those
sections are decorative. They describe an audience, give it a name and a photograph,
and are never consulted again.

This module exists because three of its outputs are genuinely load-bearing, and
because they are the three that decorative user research never produces.

---

# The Difference Between Describing and Observing

| Describing | Observing |
| --- | --- |
| "Busy professionals who value efficiency" | "Writes the note at the end of the day from memory, on a paper pad" |
| "Frustrated by manual processes" | "Re-enters the same reference number in three systems" |
| "Tech-savvy early adopters" | "Uses the mobile app for lookups and the desktop for anything they have to type" |

The left column can be written without meeting anyone. That is its appeal and its
defect. Nothing in it constrains a design decision, so nothing in it can be wrong.

The right column constrains everything. It tells module 08 what a requirement has to
accommodate, module 10 where a flow starts, and module 05 what the product is actually
competing with.

---

# Why the Current Workflow Is the Most Valuable Output

Before launch, almost every input to a product decision is a claim about the future.
The current workflow is the one input that is a fact about the present.

It carries information nothing else does:

- **What the real constraints are.** A step that looks inefficient often exists because
  of a rule, a habit with a reason, or an interaction with someone outside the process.
- **What the status quo actually costs.** Module 05 evaluates "do nothing" as a
  competitor, and it can only do that if somebody wrote down what "do nothing" involves.
- **Where the seam is.** Products succeed at the joint between two steps far more often
  than by replacing a whole workflow.

> A workflow that looks irrational usually contains a constraint you have not found
> yet. Assuming irrationality is the fastest way to build something nobody can adopt.

---

# Why Jobs Beat Features

A job is what someone is trying to accomplish, stated without reference to any
solution. The discipline is unnatural and the payoff is specific.

```
Feature framing:  "They want a search function"
Job framing:      "They need to find the one previous case that resembles this one,
                   using a detail they half-remember"
```

The feature framing permits exactly one design. The job framing permits several — and
makes it possible to notice that the best one might not be search at all.

More importantly, module 08's gate requires every feature to trace to a ranked problem,
and problems are derived from jobs. A job stated as a feature produces a trace that is
circular: the feature exists because the user wanted the feature.

---

# Why Switching Cost Decides Adoption

This is the finding that most changes what a team builds, and it is the one most often
omitted.

A user switches when the pain of the current state exceeds the cost of leaving it. Both
sides of that inequality are real quantities, and the right-hand side has five parts:

| Component | Frequently underestimated because |
| --- | --- |
| Data migration | The incumbent's data is messier than anyone assumes |
| Retraining | The user is fluent in the bad tool; they will be slow in the good one for weeks |
| Workflow disruption | Other people depend on the current output's shape |
| Contractual lock-in | Renewal dates and termination terms are nobody's favorite question |
| Perceived risk | The current thing has never lost anything. The new thing is unproven |

A product that is twice as good and carries a switching cost of three weeks of reduced
output will lose to an incumbent that is merely adequate. This is not irrational
behavior by the user; it is correct arithmetic that the product team did not do.

---

# What Skipping This Stage Costs

| Skipped | Surfaces as |
| --- | --- |
| Real segments | Module 04 ranks problems for a population that does not exist |
| Observed workflow | Module 10 designs flows starting from a screen instead of from a situation |
| Jobs | Module 08's feature-to-problem trace becomes circular |
| Switching cost | A launch where everyone agrees the product is better and nobody moves |

The last row is the expensive one, and it usually gets diagnosed as a marketing
problem.

---

# What This Module Does Not Do

It does not rank problems — that is module 04, and it needs this module's jobs and
workflow first. It does not evaluate the incumbent competitively — that is module 05.
It does not design anything.

Its entire contribution is an accurate description of the present.

---

> **Why It Matters Principle**
>
> A user section written from imagination cannot be wrong, and therefore cannot be
> useful.
>
> The value of this module is proportional to how much of it came from watching
> somebody, and the fastest way to assess a run is to ask which lines could only have
> been written by someone who had.
