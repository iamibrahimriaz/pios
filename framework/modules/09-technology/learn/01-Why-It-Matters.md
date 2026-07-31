---
Title: Why It Matters
Module: 09-technology
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Explain why technical design is where obligations become mechanisms and where the first cost check runs.
Audience:
  - Product Managers
  - Founders
  - Engineers
Prerequisites:
  - 09-technology/README.md
Outputs:
  - Understanding of why the technology stage exists
Related Modules:
  - 02-market
  - 06-business
  - 13-operations
Tags:
  - Technology
  - Architecture
  - Learn
---

# Why It Matters

---

# Overview

Technical design is usually treated as an implementation concern that follows the
product decision. In this framework it does two things that are not implementation
concerns at all: it converts obligations into mechanisms, and it is the first place the
business model can be shown to be unaffordable.

---

# Why the Data Model Comes First

The data model is the most durable artifact any product produces. Interfaces get
rewritten, architectures get replaced, teams change — and the data model persists,
because migrating it is expensive and risky in proportion to how much data exists.

That durability is why the **schema test** sets the bar where it does:

> Are the entities, relationships and constraints complete enough that someone could
> generate a schema without asking a question?

The questions that get asked when a model fails this test are always the same:

| Question | What it decides |
| --- | --- |
| Can this be null? | Whether every consumer needs a null branch |
| One or many? | The shape of half the queries |
| What happens when the parent is deleted? | Whether you get orphans or cascading loss |
| Is this unique, and scoped to what? | Whether duplicates are possible |
| Who can see this row? | Whether isolation is enforced or hoped for |

Each of these gets answered during implementation if it is not answered here — quickly,
by one person, without the context that would inform it.

---

# Why the Obligation Chain Lands Here

Module 02 found that a regulation applies. That finding is a sentence. This module is
where it becomes something that exists:

```
02-market      "Erasure must be completed within n days" [citation, date]
    ↓
09-technology  a deletion service that reaches every store, including
               backups and derived data — or a stated blocker if it cannot
    ↓
13-operations  a cadence, an owner, and evidence that it ran
```

The middle step is the one that gets skipped, and skipping it is invisible. A document
can acknowledge a retention obligation, describe a security posture, and contain no
mechanism that would actually delete anything.

The worked example threaded through this framework's resources hits exactly this: an
erasure obligation that collides with a 90-day backup retention window, with no
resolution. The framework's response is to record it as a **blocker**, not a risk — a
distinction that matters because risks get managed and blockers get resolved.

---

# Why "Regulated Fields" Is a List, Not a Posture

The security model has to name which columns hold regulated data. That list is then
checked in three more places:

| Module | Checks |
| --- | --- |
| `09-technology` | That the fields are identified and their handling is designed |
| `12-metrics` | That none appear in analytics event properties |
| `13-operations` | That the review has a cadence and an owner |
| `14-ai-systems` | That none enter a model's input |

**It is the same list every time.** That only works if this module produced an actual
list of columns rather than a paragraph about taking privacy seriously.

---

# Why the First Cost Check Runs Here

Module 06 set a cost ceiling. This module produces the first component of the cost:
infrastructure per user at launch scale.

It runs here because this is the earliest point where the number is knowable, and
because an architecture is the most expensive thing in the framework to change after it
is built. Finding that a design costs three times what the price supports is a
two-hour discovery now and a rewrite later.

The rule is the same as for the other two checks: a breach is a **regress** to module 06
for the price or module 07 for the scope. It is not resolved by assuming the cost falls.

---

# Why Architecture Inflation Is the Characteristic Failure

Inflation is building for a scale that does not exist:

```
Twenty-four customers.  A message queue, a cache layer, three services,
                        an orchestration platform, multi-region replication.
```

Every component is individually defensible. Each solves a real problem — at a scale the
product will not see for years, if ever. The cost is not just the build: it is the
operational surface that module 13 will have to run, with a person's name against every
piece of it.

The corrective is a question with a date in it: **what does this need to handle, by
when, and what is that number based on?** An architecture justified by a growth curve
nobody has evidence for is a bet placed with build time.

---

# Why the Stack Choice Requires Trade-Offs

The gate says the stack is justified with trade-offs stated, not asserted. The
distinction:

```
Asserted:   "We will use «technology» for its performance and scalability."
Justified:  "«Technology», because the team knows it and the operational
             burden is one person. Cost: «specific limitation» — acceptable
             because «specific reason from this product's requirements»."
```

The second names something the choice is bad at. A stack choice with no stated downside
has not been compared with anything.

---

# What Skipping This Stage Costs

| Skipped | Surfaces as |
| --- | --- |
| The schema test | Design decisions made ad hoc during build |
| The obligation mechanism | A compliance posture with nothing behind it |
| The regulated-column list | Regulated data in analytics events and model inputs |
| The cost check | An architecture the business cannot afford, discovered after it is built |
| Stated trade-offs | A stack nobody can explain choosing |

---

# What This Module Does Not Do

It does not decide what to build — module 08 specified it. It does not plan delivery —
module 10 does. It does not schedule the obligations it creates; module 13 does, and
this module's job is to make sure there is something to schedule.

---

> **Why It Matters Principle**
>
> Everything upstream produces statements. This module produces mechanisms.
>
> A regulation without a mechanism is a hope; an architecture without a cost is a bet;
> a data model without constraints is a set of decisions someone else will make quickly.
