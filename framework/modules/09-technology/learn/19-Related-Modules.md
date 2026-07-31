---
Title: Related Modules
Module: 09-technology
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show how the Technology module connects to the framework, and trace the obligation chain through it.
Audience:
  - Product Managers
  - Founders
  - Engineers
Prerequisites:
  - 09-technology/README.md
Outputs:
  - Understanding of the technology stage's position in the chain
Related Modules:
  - 02-market
  - 08-product
  - 13-operations
Tags:
  - Technology
  - Relationships
  - Learn
---

# Related Modules

---

# Overview

This module is the middle link in the framework's longest chain and the first of its
three arithmetic checks. It also produces the list that three other modules check
themselves against.

---

# What It Takes In

| Input | From | Used for |
| --- | --- | --- |
| `feature_spec` | `08-product` | Every capability needs a supporting interface |
| `acceptance_criteria` | `08-product` | What the design must make achievable |
| `edge_cases` | `08-product` | Failure modes to design for |
| `regulatory_landscape` | `02-market` | Obligations that must become mechanisms |
| The cost ceiling | `06-business` | The first arithmetic check |

The gate fails back to `08-product`, usually because a capability has no data behind it —
which is a specification gap surfacing as a design problem.

---

# The Obligation Chain

This module is the middle link:

```
02-market      the obligation, with jurisdiction, citation and date
    ↓
09-technology  the MECHANISM — retention job, erasure path, audit log,
               residency decision — or a recorded BLOCKER
    ↓
13-operations  cadence, named owner, evidence produced, where it is kept
```

Break the middle link and the chain fails silently. Module 13 schedules what exists;
nothing in the framework schedules a mechanism that was never designed.

---

# The Regulated Column List

This module produces it. Three other modules consume it:

| Module | Check |
| --- | --- |
| `12-metrics` | No regulated field appears in an analytics event property |
| `13-operations` | The access and audit review has a cadence and an owner |
| `14-ai-systems` | No regulated field enters a model input |

**It is the same list in all four places.** That is only true if this module produced
actual column names — which is why the module's common-mistakes page treats a
descriptive paragraph as a failure rather than a stylistic choice.

---

# The First Arithmetic Check

```
06-business    sets the cost ceiling per user
    ↓
09-technology  infrastructure cost per user at launch scale, dated
    ↓
  breach → REGRESS to 06-business (price) or 07-strategy (scope)
```

This is the first of three. Module 11 runs the second against CAC, and module 13 runs the
third against the true cost to serve — which includes this module's figure plus human
time plus module 14's inference cost.

Because module 13's check is cumulative, this module's number has to be honest for the
final check to mean anything.

---

# What It Sends Forward

| Output | Who consumes it | What they do with it |
| --- | --- | --- |
| `data_model` | `10-execution`, `12-metrics`, `14-ai-systems` | Build handoff; what can be computed; what data exists |
| `api_contract` | `10-execution` | The interface the flows are built against |
| `architecture` | `10-execution`, `13-operations` | What gets built, and what gets operated |
| `security_model` | `12`, `13`, `14` | The regulated list and the obligations |
| Failure modes | `13-operations` | The source of every runbook |
| Recovery objectives | `13-operations` | The rehearsal cadence |
| Infrastructure cost | `13-operations` | A line in the third check |
| `scalability_plan` | `10-execution` | What is deferred and to when |

---

# Where Failure Modes Become Runbooks

```
09-technology  failure mode: queue depth grows unbounded
    ↓
13-operations  runbook: transcription backlog, with trigger, access,
               steps, verification and a "do not do" line
```

Every runbook in module 13 corresponds to a failure mode enumerated here. A runbook with
no corresponding failure mode means either this module missed something — worth raising —
or it is not a real failure.

That two-way check is one of the framework's better internal consistencies, and it only
works because failure modes are enumerated rather than described as error handling.

---

# What It Deliberately Does Not Do

| It does not | Because |
| --- | --- |
| Decide what to build | `08-product` specified it |
| Schedule obligations | `13-operations` does; this module makes something schedulable |
| Decide AI capabilities | `14-ai-systems` does, using this module's data model |
| Plan delivery | `10-execution` sequences from this module's outputs |

---

> **Relationships Principle**
>
> This module converts three kinds of statement into three kinds of object: obligations
> into mechanisms, requirements into interfaces, and an architecture into a number.
>
> Every downstream check depends on that conversion having actually happened.
