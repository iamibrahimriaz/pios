---
Title: Framework
Module: 01-idea
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the repeatable method for turning a raw idea into a precise, testable premise.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - constitution/core
  - engine/evidence-policy.md
  - 01-idea/core/03-Core-Principles.md
Outputs:
  - idea_brief
  - clarifying_questions
  - initial_assumptions
  - scope_boundaries
Related Modules:
  - 02-market
  - 03-user
  - 04-problem
Tags:
  - Idea
  - Framework
  - Method
---

# The Idea Framework

---

# Overview

The principles in `03-Core-Principles.md` explain how to think about ideas.

This document explains what to **do**.

It is the operative method for this module. Follow it in order. Each pass produces
something concrete, and the passes are ordered because each one depends on the last.

---

# Framework Statement

> An idea arrives as a solution wearing the costume of a requirement.
>
> The work of this module is to undress it.

---

# The Six Passes

```
Raw Idea
   ↓
1. Capture      — record it exactly as given
   ↓
2. Separate     — pull the problem out of the solution
   ↓
3. Locate       — establish the context that changes everything
   ↓
4. Surface      — name what is being assumed
   ↓
5. Interrogate  — ask what only a human can answer
   ↓
6. Bound        — state what is in and what is out
   ↓
Idea Brief → 02-market
```

---

# Pass 1 — Capture

Record the operator's idea **verbatim** into `state.project.raw_idea`.

Do not tidy it. Do not improve it. Do not summarize it.

The raw idea is immutable for the life of the run. Every later refinement lives in
`idea_brief`, never here. When a run goes wrong six months later, the first useful
question is "what did they actually ask for?" — and this is the only place that answer
survives.

**Produces:** `state.project.raw_idea`

---

# Pass 2 — Separate

Almost every idea arrives as a solution. The job is to find the problem underneath it.

Take the idea and ask, repeatedly: **"so that what?"**

```
"A tool for doctors to write prescriptions"
   so that what?
"...so they can prescribe faster"
   so that what?
"...so they spend less time on admin during a consultation"
   so that what?
"...so they can look at the patient instead of the screen"
```

The last answer is closer to the problem than the first. Keep going until the answer
stops changing, or until it becomes a human value rather than a task.

Write both:

| | |
| --- | --- |
| **Solution as proposed** | «the operator's framing» |
| **Problem it implies** | «what the solution suggests is wrong today» |

If the implied problem sounds trivial when stated plainly, that is a finding. Record it.
Do not soften it into something that sounds more important.

**Produces:** the problem statement inside `idea_brief`

---

# Pass 3 — Locate

An idea has no meaning without context. The same sentence describes five different
products depending on the answers below.

| Dimension | Why it changes the product |
| --- | --- |
| **Jurisdiction** | Determines the regulatory regime, and therefore the data model and architecture |
| **Segment** | Solo operator, small team and enterprise are different products with different buyers |
| **Buyer vs user** | If they differ, the product must satisfy two audiences with different criteria |
| **Incumbent** | Replacing a system, sitting beside one, or greenfield are different builds |
| **Setting** | Where and under what conditions the product is used |

Every dimension is either **answered** or **asked** in Pass 5. None may be guessed.

Guessing here is the most expensive error available in the entire run. A wrong
jurisdiction produces a correct-looking blueprint for the wrong product, and nothing
downstream will catch it — every later module will faithfully build on the wrong
foundation.

**Produces:** `state.project.jurisdiction`, context fields in `idea_brief`

---

# Pass 4 — Surface

Every idea contains beliefs presented as facts. Name them.

Work through the categories deliberately — assumptions hide in the ones that get skipped:

| Category | The question that surfaces it |
| --- | --- |
| User | What are we assuming people *do* today? |
| Problem | What are we assuming *hurts*, and how much? |
| Demand | What are we assuming people *want*? |
| Willingness to pay | What are we assuming someone will *fund*? |
| Behavior | What are we assuming people will *change*? |
| Technical | What are we assuming is *possible*? |
| Access | What are we assuming we can *reach* or *obtain*? |

Each surfaced assumption is written to `state.assumptions` with:

- the statement, in one sentence
- why it is currently believed
- what would happen to the product if it is false
- how it could be validated

Tag everything per `engine/evidence-policy.md`. At this stage almost everything is
`[assumption: needs validation]`, and that is the correct and honest state. A module 01
output full of `[verified]` tags is a sign the agent invented sources.

**Produces:** `initial_assumptions`, entries in `state.assumptions`

---

# Pass 5 — Interrogate

Generate the questions that only the operator can answer. Minimum five.

Good questions share three properties:

1. **The answer changes the work.** If both answers lead to the same product, do not ask.
2. **It cannot be researched.** Ask the human for intent, not for facts that can be looked up.
3. **It is specific.** "Who is the user?" is weak. "Is this for a solo practitioner or a
   clinic with shared records?" is answerable.

Rank them: **blocking** questions must be answered before research begins; **deferrable**
questions can carry an assumption into the next module, provided it is recorded.

Then stop. Module 01 ends at a human checkpoint. Do not proceed past a blocking question
by choosing the more plausible answer — that converts the operator's decision into a
silent guess.

**Produces:** `clarifying_questions`, entries in `state.open_questions`

---

# Pass 6 — Bound

State what this product is and is not.

| | |
| --- | --- |
| **In scope** | «what the product addresses» |
| **Out of scope** | «what it deliberately does not, and why» |
| **Adjacent** | «what it might become later, deliberately parked» |

Scope stated at this stage is worth more than scope discovered at module 08. An
unbounded idea expands quietly through every later module until the MVP is a platform.

**Produces:** `scope_boundaries`

---

# The Idea Brief

The six passes assemble into one document — the module's primary output.

Its structure is defined in `13-Template.md`. It carries forward to every later module,
and it is the first thing a reader of the final blueprint encounters in the Executive
Summary.

---

# When to Return to This Module

Later modules will send work back here. Expect it, and treat it as the framework
functioning rather than failing:

| Trigger | Why it returns |
| --- | --- |
| Market research finds no definable market | The idea was not bounded |
| User research finds no coherent segment | The idea was not located |
| Problem module finds nothing painful | The separation pass was too shallow |
| Two modules contradict each other | The brief was ambiguous |

Re-entry appends. It never overwrites `raw_idea`, and it never silently deletes an
assumption — mark it superseded, with a reason.

---

# Applying the Framework

| Pass | Effort | Output | Skippable? |
| --- | --- | --- | --- |
| 1. Capture | seconds | `raw_idea` | never |
| 2. Separate | minutes | problem statement | never |
| 3. Locate | minutes | context | never |
| 4. Surface | minutes | assumptions | never |
| 5. Interrogate | minutes | questions | never |
| 6. Bound | minutes | scope | never |

No pass is optional. A module 01 that took thirty seconds produced a restatement, not
a brief.

---

# Common Failures

| Failure | What it looks like | Cost |
| --- | --- | --- |
| Accepting the solution | The brief restates the idea in better words | Every later module researches the wrong thing |
| Guessing context | Jurisdiction chosen because it seemed likely | An entire blueprint for the wrong regime |
| Polite questions | Questions whose answers change nothing | The human checkpoint wastes everyone's time |
| Assumption blindness | Fewer than five assumptions surfaced | They surface later, as defects |
| Unbounded scope | No "out of scope" section | The MVP becomes a platform by module 08 |

---

# Self Assessment

Before submitting to the gate:

- Is the raw idea recorded exactly as given?
- Have I separated the problem from the proposed solution?
- Is every context dimension either answered or asked?
- Have I surfaced at least one assumption in every category?
- Would each of my questions actually change the work?
- Have I stated what is out of scope?

If any answer is **No**, the framework has not been applied.

---

> **Framework Principle**
>
> The idea you were given is a hypothesis about a solution.
>
> The brief you produce is a hypothesis about a problem.
>
> Everything downstream depends on that exchange having actually happened.
