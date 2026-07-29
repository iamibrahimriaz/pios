---
Title: Framework
Module: 03-user
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the repeatable method for moving from a market to one person's working reality.
Audience:
  - AI Agents
  - Product Managers
  - Researchers
Prerequisites:
  - 02-market gate passed
  - engine/evidence-policy.md
  - 03-user/core/03-Core-Principles.md
Outputs:
  - segments
  - personas
  - jobs_to_be_done
  - current_workflow
  - switching_cost
Related Modules:
  - 04-problem
  - 08-product
  - 10-execution
Tags:
  - User
  - Framework
  - Method
---

# The Narrowing

---

# Overview

Module 02 established a market — a population defined by a boundary.

This module narrows that population to one person, and then to what that person is
actually doing on a Tuesday morning.

The narrowing is the method. Each step trades breadth for specificity, and specificity is
what makes everything downstream buildable. A PRD written for "healthcare professionals"
produces a product for nobody.

---

# Framework Statement

> A market tells you how many people might buy.
>
> A user tells you what to build.
>
> The distance between those two is this module.

---

# The Five Moves

```
Market Definition (from 02-market)
   ↓
1. Divide     — split the market into groups that behave differently
   ↓
2. Choose     — commit to one, defensibly
   ↓
3. Embody     — build a persona grounded in evidence
   ↓
4. Observe    — document what they do today, and what leaving it costs
   ↓
5. Job        — name what they are actually trying to get done
   ↓
User Analysis → 04-problem, 08-product, 10-execution
```

Note the order. **Observe before Job.** What people do is evidence; what they are trying
to achieve is interpretation. Interpreting before observing produces a job statement that
describes the product you already wanted to build.

---

# Move 1 — Divide

Split the market into segments.

A group is only a segment if its members would **buy, use, or reject the product for
different reasons.** That is the test.

| Not a segment | A segment |
| --- | --- |
| Practices in the north vs the south | Solo practices vs practices with shared records |
| Users aged 30–40 vs 40–50 | Users who own the budget vs users who must request it |
| Large vs small, with no behavioral difference | Those replacing a system vs those with none |

Demographic splits that do not change behavior create the appearance of segmentation
without its value. They also produce two personas that are the same person.

For each segment record: approximate size, pain intensity, ability to pay, and how they
could be reached. Every column carries a tag.

**Produces:** `segments`

---

# Move 2 — Choose

Commit to one segment to serve first.

The commitment must be **defended against the criteria**, not against preference,
interest, or which segment was easiest to find information about.

Score each segment on:

| Criterion | Why it matters |
| --- | --- |
| Pain intensity | Determines whether they will act at all |
| Ability to pay | Determines whether a business exists |
| Reachability | Determines whether you can find them |
| Speed to first customer | Determines how fast you learn |

Then state three things:

1. **Which segment** and why.
2. **Why not the larger one**, if a bigger segment was passed over. This is the answer
   most often skipped and most often needed later.
3. **What is given up** by choosing. Every choice costs something; naming it prevents
   the choice being quietly reversed in module 08.

**Produces:** priority within `segments`

---

# Move 3 — Embody

Build the persona.

Every row must be traceable to evidence. A persona is a compression of research, not a
character sketch.

> **The test:** could this persona describe anyone in the market?
>
> If yes, it describes no one, and it will not constrain a single product decision.

Include what is **not** known. A persona with an honest gaps section is more useful than
one that appears complete — because the gaps tell the next module what to validate.

If the buyer differs from the user, build a secondary persona for them. Where they differ,
every later module carries two sets of criteria, and discovering that at module 06 means
re-running this one.

**Never invent a quote.** A fabricated user voice is the most damaging output this module
can produce — it reads as primary evidence, propagates into the PRD, and nobody
downstream can tell it was invented. If no real voice can be found, write that no primary
voice was located.

**Produces:** `personas`

---

# Move 4 — Observe

Document what actually happens today, step by step, with the tools named.

This move produces more product insight than any other in the module. The opportunity is
usually **in the friction between steps**, not in the steps themselves.

For each step: what they do, which tool, how long it takes, and what is annoying about it.

Then assess **switching cost** across five dimensions:

| Cost | Question |
| --- | --- |
| Data migration | What has to move, and how much of it? |
| Retraining | Who has to learn, and for how long? |
| Workflow disruption | What stops working while the change happens? |
| Contractual lock-in | What are they tied into, and until when? |
| Risk | What do they fear going wrong? |

Switching cost is the most underestimated number in product work. A better tool that costs
two weeks of disruption loses to a worse tool already installed. State the bar the product
must clear to be worth the switch.

**Produces:** `current_workflow`, `switching_cost`

---

# Move 5 — Job

Name what the person is actually trying to get done.

```
When «situation», I want to «motivation», so I can «outcome».
```

**The test: if the sentence names a solution, it is not a job.**

| Not a job | A job |
| --- | --- |
| "I want a prescription-writing tool" | "When a patient describes symptoms, I want to capture what they said without breaking eye contact, so I can stay present in the consultation" |
| "I want a dashboard" | "When I start my week, I want to know which accounts are at risk, so I can act before they churn" |

A job is stable. Solutions change; the job outlives them. That is what makes jobs the
right thing to build against.

For each job record how often it occurs, what satisfies it today, and how well.

Then state explicitly which jobs the product will **not** serve. Unbounded job lists
become unbounded feature lists in module 08.

**Produces:** `jobs_to_be_done`

---

# The Immovables

Before finishing, ask one more question:

> **What would this person not change, no matter how good the product is?**

Habits, tools, rituals, and constraints that are effectively fixed define the shape any
successful product must take. A product that requires an immovable to move does not get
adopted — however good it is.

This question is under-asked and highly predictive.

---

# When This Module Returns to 02-market

`on_fail: return to 02-market`. Common triggers:

| Trigger | What it means |
| --- | --- |
| No coherent segment can be found | The market boundary is too broad |
| Every segment behaves identically | The boundary was drawn around a non-market |
| The prioritized segment falls outside the market definition | The boundary and the segment disagree |
| No user of any kind can be located | The market may be theoretical |

---

# Common Failures

| Failure | What it looks like | Cost |
| --- | --- | --- |
| Demographic segmentation | Two personas who are the same person | No real prioritization happens |
| Choosing by interest | The segment the agent found most material on | The product serves the best-documented user, not the best one |
| Invented persona | Every row plausible, none traceable | The PRD is built on fiction |
| Fabricated quote | A user voice with no source | Undetectable downstream, poisons everything |
| Job that names a solution | "They want an app that…" | Locks in the solution before the problem is understood |
| Switching cost ignored | No migration or retraining assessment | The product loses to an inferior installed tool |
| Interpreting before observing | Jobs written before the workflow | The job describes the intended product |

---

# Self Assessment

- Do my segments differ by behavior, or only by description?
- Did I defend the prioritized segment against the criteria, or against preference?
- Could every row of my persona be traced to a source?
- Did I invent any quote or detail?
- Did I document what they do before deciding what they want?
- Does any job statement name a solution?
- Did I assess what it costs them to switch?
- Did I ask what they would not change?

---

> **Framework Principle**
>
> The market says how many.
>
> The user says what.
>
> Skip this module and every later module will be built for an average that does not exist.
