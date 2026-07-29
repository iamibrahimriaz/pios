---
Title: Framework
Module: 07-strategy
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the repeatable method for choosing what to build and what not to build.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 06-business gate passed
  - engine/evidence-policy.md
  - 07-strategy/core/03-Core-Principles.md
Outputs:
  - solution_options
  - chosen_approach
  - mvp_definition
  - non_goals
  - risk_register
  - roadmap
Related Modules:
  - 08-product
  - 09-technology
Tags:
  - Strategy
  - Framework
  - Method
---

# The Commitment

---

# Overview

Every module before this one gathered information. This one spends it.

The output is a set of decisions that later modules execute without revisiting: what to
build, what to leave out, in what order, and what would make the whole thing stop.

Two failures dominate. The first is **choosing without generating** — arriving with one
answer already in mind and manufacturing alternatives to justify it. The second is
**deciding without cutting** — producing a strategy where everything is important, which
is the same as having no strategy.

The module ends at a human checkpoint, because the MVP cut is a commercial commitment
rather than a research finding.

---

# Framework Statement

> A strategy is defined by what it refuses to do.
>
> Everything else is a summary of research.

---

# The Six Moves

```
Ranked Problems (04) + Gap Analysis (05) + Business Model (06)
   ↓
1. Diverge   — generate at least three genuinely different approaches
   ↓
2. Compare   — score against what the research established
   ↓
3. Choose    — commit, and record what was rejected
   ↓
4. Cut       — draw the MVP line and defend it
   ↓
5. Bound     — state the non-goals
   ↓
6. Register  — risks, sequence, and stop conditions
   ↓
Strategy → ⏸ HUMAN CHECKPOINT → 08-product
```

---

# Move 1 — Diverge

Generate at least three approaches to the sharpest problem.

**They must be genuinely different.** The test:

> Would each option produce a **different first build**?

If all three start by building the same thing and differ only in what comes after, they
are one option described three ways.

Deliberately explore different shapes:

| Shape | Question it answers |
| --- | --- |
| Narrow tool | What if we solved only the sharpest problem, completely? |
| Workflow replacement | What if we replaced the whole process? |
| Layer on top | What if we sat on the incumbent instead of replacing it? |
| Service, not software | What if a person did this and software came later? |
| Different segment first | What if we started with the second-priority segment? |

**Guard against the straw man.** Generating one real option and two obviously worse ones
satisfies the count and defeats the purpose. Each option must be one that a competent
person could reasonably choose.

For each option, record: what it is, which problems it solves, what the first build would
be, the price it supports, its defensibility, and its biggest risk.

**Produces:** `solution_options`

---

# Move 2 — Compare

Score the options against criteria the research established — not against preference.

| Criterion | Source |
| --- | --- |
| Solves the sharpest problem | `04-problem` |
| Solves the next-ranked problems | `04-problem` |
| Fits the identified gap | `05-competition` |
| Defensible | `05-competition` |
| Supports the modeled price | `06-business` |
| Buildable by the assumed team | `06-business` cost structure |
| Time to first customer | `06-business` go-to-market |
| Survives if the assumed problem is wrong | `04-problem` evidence standing |

Weight them, and say how. Unweighted scoring lets a strong performance on a minor
criterion outvote a weak one on a decisive criterion.

The last row deserves attention when module 04 declared a shortfall. An approach that
retains some value even if the central problem turns out to be less severe than believed
is worth more than its raw score suggests.

---

# Move 3 — Choose

Commit to one.

Three things must be recorded, and the second is what makes this a decision rather than a
preference:

1. **Why this one** — referencing the comparison and the ranked problems.
2. **What was rejected, and what we lose by rejecting it.** Every option had something to
   offer. Naming it prevents the rejected approach being quietly reintroduced later as a
   feature.
3. **What we are betting on** — the belief this choice depends on.

Then state the **reversal trigger**: what would make us choose differently? A strategy with
no reversal condition cannot be re-examined honestly, because there is no agreed signal
that it should be.

**Produces:** `chosen_approach`

---

# Move 4 — Cut

Draw the MVP line.

**The definition:** the smallest thing that solves the sharpest problem **end to end** for
the primary persona.

Not the smallest buildable thing. Not a demo. The smallest complete solution to one
problem for one person.

**The end-to-end test:**

> Can the primary persona complete the core job using only what is above the line?

If no, the cut is wrong. An MVP that cannot complete a single job teaches nothing when it
ships, because nobody can use it for its actual purpose.

Then record:

| | |
| --- | --- |
| **The cut principle** | One sentence: what makes something MVP in this product |
| **What the MVP proves** | The specific belief it tests |
| **What it does not prove** | What remains unknown after shipping it |

The last one matters. Teams routinely ship an MVP and conclude the wrong thing from it,
because nobody wrote down in advance which question it was answering.

Everything below the line goes to the roadmap. Nothing is dropped silently.

**Produces:** `mvp_definition`

---

# Move 5 — Bound

State what this product deliberately does not do.

| Type | Example |
| --- | --- |
| Capabilities | Features that will not be built, and why |
| Segments | Users we are not serving |
| Problems | Real problems from module 04 we are not addressing |
| Integrations | Systems we will not connect to |

Each non-goal carries a reason and, where relevant, a reconsider trigger.

This section prevents months of argument. Scope creep rarely arrives as a decision — it
arrives as a series of small additions that nobody remembers agreeing to exclude.

**Produces:** `non_goals`

---

# Move 6 — Register

Three outputs: risks, sequence, and stop conditions.

## Risks

Rate honestly. A register where everything is "medium" is a register nobody will act on.

Each risk carries a likelihood, an impact, a mitigation, and an **early warning sign** —
what you would observe *before* it fully materializes. The early warning is what makes a
register operational rather than decorative.

Carry forward the inherited risks explicitly:

| From | Risk |
| --- | --- |
| `04-problem` | If the sharpest problem is assumed, the entire product rests on it |
| `05-competition` | If the gap is not defensible, there is a clock on the opportunity |
| `06-business` | The load-bearing economic assumption |

## Sequence

High-level milestones only — `09-Roadmap.md` is the full artifact.

**Milestone Zero is required whenever the sharpest problem is assumed rather than
verified**, or whenever module 04 recorded a declared shortfall. It validates before
anything is built.

Every milestone states what it **teaches**. A milestone that teaches nothing is a schedule
entry.

## Stop Conditions

What result would mean this should not continue?

Define it now, while the thinking is cheap and nothing has been invested. Teams almost
never do this in advance, and by the time the evidence arrives, too much has been spent to
read it honestly.

**Produces:** `risk_register`, `roadmap`

---

# The Human Checkpoint

This module ends by handing control back.

Present:

1. What we propose to build, in one sentence.
2. What we are deliberately not doing.
3. The load-bearing assumption.
4. The decisions needed — with a recommendation for each.

Then wait. The MVP cut commits money and months. It is the operator's call, and presenting
it as a research conclusion removes their opportunity to make it.

---

# When This Module Returns to 04-problem

`on_fail: return to 04-problem`. Common triggers:

| Trigger | What it means |
| --- | --- |
| No approach solves the sharpest problem | The problem may be intractable as framed |
| Every option scores the same | The criteria are not discriminating; the problems may be poorly ranked |
| The best option cannot support the price | Return via `06-business` |
| The MVP cannot complete any job end to end | The problem may be too large to solve incrementally |

---

# Common Failures

| Failure | What it looks like | Cost |
| --- | --- | --- |
| Straw-man options | One real option and two obviously worse ones | The choice was made before the module ran |
| Same-shape options | Three feature scopes of one product | No genuine alternative considered |
| Unweighted comparison | A minor criterion outvotes a decisive one | The wrong option wins on points |
| No rejection record | Only the chosen option documented | Rejected approaches return as features |
| Everything is MVP | No line drawn | Six months before first contact with a user |
| No non-goals | Scope implicitly unbounded | Creep with no agreed baseline |
| Uniform risk ratings | Everything "medium" | The register is never used |
| No Milestone Zero on an assumed problem | Building begins on an untested belief | The failure this framework exists to prevent |
| No stop conditions | Failure undefined | The project cannot end rationally |

---

# Self Assessment

- Would each of my options produce a different first build?
- Could a competent person reasonably choose any of them?
- Did I score against the research, or against what I preferred?
- Did I record what the rejected options would have given us?
- Can the persona complete one whole job with only what is above the line?
- Did I write what the MVP does *not* prove?
- Are my risk ratings differentiated, or all the same?
- Does Milestone Zero exist if the problem is assumed?
- Have I defined what would stop this?

---

> **Framework Principle**
>
> The research told you what is true.
>
> This module is where someone has to decide what to do about it —
> and deciding means writing down what you are not going to do.
