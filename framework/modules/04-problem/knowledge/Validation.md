---
Title: Validation
Module: 04-problem
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Build a runnable validation plan ordered by cheapest test of the most load-bearing belief.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 04-problem/knowledge/Evidence.md
Outputs:
  - validation_plan
Related Modules:
  - 07-strategy
  - 10-execution
Tags:
  - Problem
  - Validation
  - Method
---

# Validation

---

# What It Is

A plan for testing what is still unproven — one test per assumed problem and per load-bearing assumption.

Each test states five things:

| | |
| --- | --- |
| **What is being tested** | The specific belief, in one sentence |
| **Method** | Interviews, survey, prototype, data pull, landing page |
| **Sample** | How many, and who |
| **Effort** | Days |
| **Would invalidate** | What result kills the assumption |

The last row is what makes it a test rather than an activity. A plan with no invalidating result cannot fail,
and a test that cannot fail produces confirmation regardless of what is true.

---

# When It Applies

In Stage 6 (Plan), last in the module. It feeds `07-strategy`'s stop conditions and becomes Milestone Zero in
`10-execution` where the sharpest problem is unverified.

---

# How to Apply It Here

**Order by cheapest test of the most load-bearing belief.** Not by what is easiest, and not by the order things
were discovered. Load-bearing means: if this is false, what else collapses? Test that first, however
uncomfortable.

**Be concrete enough to run tomorrow.** "Interview 10 solo GPs about consultation-time data entry" is a plan.
"Conduct user research" is not, and the difference is whether anyone can act on it without asking a question.

**Write the invalidating result before running anything.** Defined in advance, it is a test. Defined afterward,
it is an interpretation — and it will be interpreted favorably.

**Carry forward every `NEEDS USER` question from `03-user`.** Those are already a validation list, and dropping
them loses the module's honest gaps.

**Define the stop-and-rethink trigger.** What result would mean this should not be built? Teams almost never
define failure in advance, and that is why doomed products run for years.

**Match the method to the claim.** Behavior claims need observation or a prototype; incidence claims need data
or a survey; willingness-to-pay claims need something closer to a transaction than a conversation. The
`validation/` files cover each method's actual reach.

---

# Where It Misleads

**Validation plans get written to be completed rather than to be informative.** The signal is a plan of
low-risk activities that will all succeed. If no test in the plan could plausibly kill the idea, the plan is
documentation of intent.

**"Talk to more users" absorbs everything.** It is the default method for every claim, and it is genuinely weak
for incidence, for willingness to pay, and for anything predictive. Method selection is most of the quality of
a plan.

**Sample sizes get set by convenience and then reported as findings.** Five interviews can establish that a
problem exists and cannot establish how common it is. Say which question the sample can answer.

**A completed plan is mistaken for validated problems.** Running the tests is what validates; the plan is a
promise. `10-execution` is where it acquires a milestone and an owner, and until then nothing has been proven.

---

# Related

| | |
| --- | --- |
| `Evidence.md` | What the plan is trying to change |
| `validation/Success-Criteria.md` | Defining pass and fail in advance |
| `validation/Interviews.md` and siblings | What each method can and cannot establish |
| `10-execution` | Where validation becomes Milestone Zero |

---

> **Concept Note**
>
> Write the result that would kill the assumption before you gather
> anything.
>
> Afterward, every result confirms — and the plan has validated your
> intent rather than your belief.
