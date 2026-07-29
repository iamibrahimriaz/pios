---
Title: Framework
Module: 04-problem
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the repeatable method for separating real problems from assumed ones.
Audience:
  - AI Agents
  - Product Managers
  - Researchers
Prerequisites:
  - 03-user gate passed
  - engine/evidence-policy.md
  - 04-problem/core/03-Core-Principles.md
Outputs:
  - problem_inventory
  - ranked_problems
  - validation_plan
Related Modules:
  - 05-competition
  - 07-strategy
  - 08-product
Tags:
  - Problem
  - Framework
  - Method
---

# The Sieve

---

# Overview

This is the honesty checkpoint of the run.

Every module before this one describes a situation. This module makes a judgment: **is
there a problem here worth solving, and do we actually know that, or are we hoping?**

Everything after this inherits the answer. Module 08 traces every requirement back to a
problem ranked here. If a problem is wrong, the product built on it is wrong — and no
later module re-examines it.

The method is a sieve. Many candidate problems go in. One sharp, defended problem comes
out, with everything else either ranked below it or explicitly excluded.

---

# Framework Statement

> The expensive mistake is not building the wrong solution.
>
> It is building the right solution to a problem nobody actually has.

---

# The Six Stages

```
User Analysis (from 03-user)
   ↓
1. Harvest    — collect every candidate problem
   ↓
2. Classify   — problem, symptom, or preference?
   ↓
3. Score      — frequency × severity × workaround
   ↓
4. Sort       — validated on one side, assumed on the other
   ↓
5. Sharpen    — choose the one the product is built around
   ↓
6. Plan       — how to test what is still unproven
   ↓
Problem Analysis → 05-competition, 07-strategy, 08-product
```

---

# Stage 1 — Harvest

Collect every candidate problem, without filtering.

The sources are already in hand from `03-user`:

| Source | What it yields |
| --- | --- |
| `current_workflow` friction points | The most reliable problems — observed behavior |
| Jobs served poorly | Gaps between what they want and what they get |
| The step they most want removed | Usually the sharpest candidate |
| Switching cost pain | Problems with the incumbent |
| Review and forum complaints | Stated frustration, self-selected |
| Immovables | Constraints that create problems downstream |

Record each in the person's own framing, not a cleaned-up version. "I end up doing notes
at home after clinic" is more useful than "documentation burden".

Do not filter yet. Filtering during collection loses the problem you were not looking for.

**Produces:** raw `problem_inventory`

---

# Stage 2 — Classify

Sort every statement into one of three categories. This stage prevents most of the damage
this module can do.

| Type | Definition | Test |
| --- | --- | --- |
| **Problem** | Something costs them time, money, risk, or wellbeing | Is there a cost when it is not solved? |
| **Symptom** | A visible effect of a problem underneath | Ask "why does that happen?" — if there is an answer, it is a symptom |
| **Preference** | A wish with no cost attached | Nothing bad happens if it is never satisfied |

Examples:

| Statement | Type | Reasoning |
| --- | --- | --- |
| "The export takes four clicks" | Symptom | Why does that matter? → they miss their accountant's deadline. *That* is the problem |
| "I do notes at home after clinic" | Problem | Costs unpaid hours and family time |
| "I wish it had dark mode" | Preference | No cost when unmet |

For every symptom, record the problem beneath it and carry that forward instead.

Keep the excluded preferences on the page. They will be re-proposed later, and a written
record of why they were excluded saves that argument.

**Produces:** classified `problem_inventory`

---

# Stage 3 — Score

Score every surviving problem on three dimensions. Show the arithmetic.

```
Score = Frequency × Severity × Workaround
```

| | 5 | 3 | 1 |
| --- | --- | --- | --- |
| **Frequency** | Daily or more | Weekly | Monthly or less |
| **Severity** | Costs money, risk, or reputation | Costs significant time | Mildly annoying |
| **Workaround** | None — they simply suffer | Exists but poor | Exists and works |

**The workaround dimension is the one most often omitted, and the most informative.**

A problem with a good workaround is a problem somebody already solved. It may still be
worth improving, but it is not urgent, and displacing a working workaround is harder than
solving something with no answer at all.

A problem with **no** workaround is one of two things: extremely valuable, or not painful
enough to have provoked one. Deciding which is a judgment worth making explicitly.

Also record what each problem **costs per occurrence** — in time, money, or risk. That
number becomes the value case in module 06 and the metric target in module 12.

**Produces:** `ranked_problems`

---

# Stage 4 — Sort

Divide the scored problems into two lists, and keep them **visually separate** for the
rest of the document.

| List | Contains |
| --- | --- |
| **Validated** | Problems with `[verified]` evidence — a retrievable source |
| **Assumed** | Problems that are plausible but unevidenced |

This separation is the module's core output. Blending the two in prose is how an assumed
problem becomes an established one — not through dishonesty, but through paragraph
structure.

If the validated list is empty, **say so explicitly.** Do not promote assumed problems to
make the section look populated. An empty validated list is a finding that changes the
roadmap: it means Milestone Zero is validation, not building.

Assumed problems are not lesser problems. They may be the most important ones. They are
simply unproven, and the reader must be able to tell at a glance.

**Produces:** the validated / assumed split

---

# Stage 5 — Sharpen

Choose **one** problem. The product is built around it.

The choice is defended against the scoring table. Three things must be stated:

1. **Why this one** — referencing frequency, severity, and workaround inadequacy.
2. **Why not the others** that scored comparably. If the highest scorer was passed over,
   that requires a stronger defense than choosing it would have.
3. **Its evidence standing** — verified or assumed, stated plainly.

If the sharpest problem is **assumed rather than verified**, that is a critical finding.
It does not stop the run, but it must propagate: module 09 will require a Milestone Zero
that validates the belief before any building starts.

Then run the **root cause check**. Ask "why does this happen?" repeatedly until the answer
stops being actionable.

Solving a symptom is sometimes correct — the root cause may be outside anyone's control.
But it must be a decision, not an oversight.

**Produces:** the sharpest problem, defended

---

# Stage 6 — Plan

Every assumed problem and every load-bearing assumption gets a test.

Order by **cheapest test of the most load-bearing belief.** Not by what is easiest, and not
by the order they were discovered.

Each test states:

| | |
| --- | --- |
| What is being tested | The specific belief |
| Method | Interviews, survey, prototype, data pull, landing page |
| Sample | How many, and who |
| Effort | Days |
| Would invalidate | What result kills the assumption |

Be concrete. "Interview 10 solo GPs about consultation-time data entry" is a plan.
"Conduct user research" is not.

Carry forward every `NEEDS USER` question inherited from `03-user` — those are already a
validation list.

Finally, define the **stop-and-rethink trigger**: what result would mean this should not
be built? Teams almost never define failure in advance, and it is why doomed products run
for years.

**Produces:** `validation_plan`

---

# When This Module Returns to 03-user

`on_fail: return to 03-user`. Common triggers:

| Trigger | What it means |
| --- | --- |
| No problems can be harvested | The workflow in `03-user` was too thin |
| Every candidate is a preference | There may be no problem here at all |
| Problems cannot be attributed to a persona | The persona was too vague |
| The workflow has no friction points | It was documented at too high a level |

A run that reaches this module and finds nothing painful has learned something valuable —
provided it says so rather than manufacturing a problem to justify continuing.

---

# Common Failures

| Failure | What it looks like | Cost |
| --- | --- | --- |
| Solving a symptom | The product optimizes four clicks, not the missed deadline | Builds the wrong thing efficiently |
| Preference as problem | Dark mode ranked alongside unpaid overtime | Dilutes the MVP |
| Workaround ignored | A high score for something already solved | Displacing a working solution is much harder |
| Blended lists | Validated and assumed problems in one narrative | Assumptions become facts silently |
| Manufactured validation | Assumed problems promoted to fill the section | The blueprint rests on fiction |
| No sharpest problem | A ranked list with no choice made | Module 07 has nothing to build strategy around |
| Vague validation plan | "Conduct user research" | Nobody can act on it |
| No stop condition | Failure never defined | The project cannot be stopped rationally |

---

# Self Assessment

- Did I classify every statement before scoring it?
- Did I score the workaround dimension, not just frequency and severity?
- Are validated and assumed problems visually separate on the page?
- Did I state honestly whether the sharpest problem is verified?
- Did I ask why the problem happens, or accept it at face value?
- Would someone else be able to run my validation plan tomorrow?
- Have I defined what result would stop this project?

---

> **Framework Principle**
>
> Every later module assumes this one was honest.
>
> The most useful thing this module can produce is a clear statement that the
> problem is not yet proven.
