---
Title: Success Criteria
Module: 04-problem
Section: knowledge/validation
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define pass, fail and the stop-and-rethink trigger before any evidence is gathered.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 04-problem/knowledge/Validation.md
Outputs:
  - Criteria within validation_plan
Related Modules:
  - 07-strategy
  - 10-execution
Tags:
  - Problem
  - Criteria
  - Concept
---

# Success Criteria

---

# What It Is

The result that would confirm a belief, the result that would kill it, and the threshold between them — all
written **before** the test is run.

Three things, and the third is the one almost nobody writes:

| | |
| --- | --- |
| **Pass** | The result that lets the run proceed as planned |
| **Fail** | The result that invalidates the assumption |
| **Stop-and-rethink trigger** | The result that means this should not be built at all |

> Teams almost never define failure in advance, and it is why doomed products run for years.

---

# When It Applies

In Stage 6 (Plan), attached to every test. The stop trigger propagates to `07-strategy` as a stop condition and to
`10-execution` as the gate on Milestone Zero.

---

# How to Apply It Here

**Write the number, the population and the window.** "At least 6 of 10 solo GPs report completing notes after
hours in the last week" is a criterion. "Most GPs confirm the problem" is a sentence that will be satisfied by
any outcome.

**Set the threshold from what the decision requires, not from what seems achievable.** Ask what result would
justify building, then write that. Setting it from the expected result guarantees a pass and teaches nothing.

**Make fail a genuine possibility.** If no plausible outcome falls below the threshold, the test has no
information content. A criterion that cannot fail is a formality with a percentage in it.

**Write it before gathering anything, and timestamp it.** After the data arrives, every threshold becomes
negotiable and every result becomes interpretable. This is not a matter of honesty — it is how interpretation
works.

**State the consequence of each branch.** Pass → proceed to `07-strategy` with the problem verified. Fail →
return to `03-user` or re-sharpen. Stop → the run ends, and that is a legitimate outcome the framework treats as
success.

---

# Where It Misleads

**Criteria get rewritten quietly after the result.** The threshold moves a little, the population is
reinterpreted, the window extends. Each adjustment is individually defensible and the sum is a test that proved
whatever was already believed. The timestamp is the only real defense.

**Vague criteria feel flexible and are simply unfalsifiable.** "Positive signal from users" cannot be failed,
which means the test cannot inform the decision it was written to inform.

**Pass is defined and fail is left implicit as "not pass".** They are different: a result can miss the pass
threshold without invalidating the belief, and the honest response to that is another test rather than either
verdict.

**The stop trigger gets omitted as pessimistic.** Its absence is what makes a project unstoppable — without it,
every disappointing result becomes a reason to try a different approach, indefinitely, because no result was ever
designated as the end.

**Criteria for the sharpest problem get set loosest**, because the cost of failing them is highest. That is
exactly inverted: the load-bearing belief deserves the strictest threshold in the plan.

---

# Related

| | |
| --- | --- |
| `Validation.md` | The plan these attach to |
| `Evidence.md` | What a passed criterion changes |
| `MVP.md` | Where viable must be defined in advance |
| `07-strategy`, `10-execution` | Where the stop trigger takes effect |

---

> **Concept Note**
>
> Write the result that would stop the project, and write it first.
>
> A project with no defined failure cannot be stopped rationally — it
> can only be abandoned, years later, by exhaustion.
