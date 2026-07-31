---
Title: Related Modules
Module: 08-product
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show how the Product module connects to the framework and what each downstream module inherits.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 08-product/README.md
Outputs:
  - Understanding of the product stage's position in the chain
Related Modules:
  - 07-strategy
  - 09-technology
  - 12-metrics
Tags:
  - Product
  - Relationships
  - Learn
---

# Related Modules

---

# Overview

This module has more direct consumers than any other. Five modules build directly on its
outputs, and each one depends on a different part of them.

---

# What It Takes In

| Input | From | Used for |
| --- | --- | --- |
| `mvp_definition` | `07-strategy` | The scope being specified |
| `chosen_approach` | `07-strategy` | What kind of thing is being built |
| `personas` | `03-user` | Who each requirement is for |
| `jobs_to_be_done` | `03-user` | The root of the trace |

The gate fails back to `07-strategy`, and the most useful cause is the one that feels
like a failure of this module: specification revealing that the MVP cut was not real.
Returning it is correct.

---

# What It Sends Forward

| Output | Who consumes it | What they do with it |
| --- | --- | --- |
| `feature_spec` | `09-technology`, `10-execution`, `11-growth`, `14-ai-systems` | What to build, sequence, promote, and consider automating |
| `acceptance_criteria` | `09-technology`, `10-execution` | The definition of done, and the basis of the QA strategy |
| `edge_cases` | `09-technology`, `13-operations` | Failure modes to design for and runbooks to write |
| `prd_body` | `10-execution` | The handoff |
| `prioritization` | `10-execution` | Milestone sequencing |

---

# The Five Consumers

**`09-technology`** takes the feature spec and asks whether every capability has a
supporting endpoint or interface. Its **schema test** — are the entities and constraints
complete enough to generate a schema — depends on this module having specified what data
each requirement implies.

**`10-execution`** turns requirements into flows and milestones. Its **demo test** asks
whether a milestone can be shown to someone; that is only answerable if the acceptance
criteria were observable.

**`12-metrics`** instruments the requirements. Its **computation test** asks whether each
metric can actually be computed from what exists, and the answer depends on this module
having specified what gets recorded.

**`13-operations`** derives runbooks from this module's edge cases and module 09's
failure modes. A specification with no edge cases produces an operations plan with
nothing to write runbooks about.

**`14-ai-systems`** checks proposed capabilities against the requirement list. A
capability with no requirement is an orphan by the same definition this module uses —
and in the worked example, that check is what rejected code suggestion outright.

---

# The Acceptance-Criteria Chain

One relationship deserves tracing, because it is where "done" is actually defined:

```
08-product   observable acceptance criteria
    ↓
10-execution  definition of done per milestone; QA strategy
    ↓
13-operations severity definitions reference user impact from here
```

An aspirational criterion breaks all three. Module 10 cannot state a definition of done,
module 13 cannot grade an incident by user impact, and both fall back to judgment at the
moment judgment is least available.

---

# Where the Non-Goals Bind

Module 07's non-goals are enforced here, and this module's gate adds the mechanism:
anything out of scope moves to the roadmap rather than disappearing. The two together
are what stop scope from re-entering — module 07 says what is out, this module says
where it went.

---

# What It Deliberately Does Not Do

| It does not | Because |
| --- | --- |
| Choose what to build | `07-strategy` chose; this module writes it down |
| Design the interface | `10-execution` owns flows |
| Design the data model | `09-technology` does, from what this module implies |
| Define success metrics | `12-metrics` does; this module contributes only what a requirement makes observable |

The last row is why five of this module's knowledge files are deliberately scoped down.
KPIs, success metrics, milestones, vision and mission all belong elsewhere, and each is
documented here only to the extent that module 08 contributes to it.

---

> **Relationships Principle**
>
> Five modules build directly on this one, and each depends on a different part of it.
>
> That is why an underspecified section does not fail here — it fails somewhere else,
> as a question nobody can answer.
