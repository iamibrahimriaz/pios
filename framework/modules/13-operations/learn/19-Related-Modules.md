---
Title: Related Modules
Module: 13-operations
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show how the Operations module connects to the framework and which chains terminate here.
Audience:
  - Product Managers
  - Founders
  - Operators
Prerequisites:
  - 13-operations/core/00-Purpose.md
Outputs:
  - Understanding of the operations stage's position in the chain
Related Modules:
  - 02-market
  - 06-business
  - 09-technology
Tags:
  - Operations
  - Relationships
  - Learn
---

# Related Modules

---

# Overview

Three of the framework's chains terminate in this module, and all three terminate with
something concrete: a name, a schedule, or a number that has to clear a ceiling.

---

# What It Takes In

| Input | From | Used for |
| --- | --- | --- |
| `delivery_plan` | `10-execution` | What is being launched, and when |
| `security_model` | `09-technology` | The obligations and the regulated list |
| Failure modes | `09-technology` | The source of every runbook |
| Recovery objectives | `09-technology` | The rehearsal cadence |
| Infrastructure cost | `09-technology` | A line in the cost model |
| Inference cost | `14-ai-systems` | Another line |
| `regulatory_landscape` | `02-market` | Notification deadlines, with citations |
| The cost ceiling | `06-business` | The third arithmetic check |
| `edge_cases` | `08-product` | Severity definitions by user impact |

The gate fails back to `10-execution`, usually because the plan cannot be operated as
sequenced.

---

# The Obligation Chain, Completed

```
02-market      the obligation, with jurisdiction, citation and date
09-technology  the mechanism that satisfies it
13-operations  CADENCE · NAMED OWNER · EVIDENCE · LOCATION
```

This is the end of the framework's longest chain. It ends with a person's name, which is
the only form in which an obligation actually gets performed.

When module 09 recorded a **blocker** rather than a mechanism, this module carries it
forward unresolved rather than softening it. In the worked example, the erasure-versus-
backup conflict appears in the compliance table marked as blocking launch, with an owner
and a note that it needs legal input — because this module runs obligations, and that one
has no mechanism to run.

---

# The Third Arithmetic Check

```
06-business    the cost ceiling per user
09-technology  infrastructure cost      ─┐
14-ai-systems  inference cost           ─┤
13-operations  support + compliance +   ─┼─→ TRUE COST TO SERVE
               human delivery time      ─┘        vs the ceiling
    ↓
  breach → REGRESS to 06-business (price) or 07-strategy (scope)
```

This is the last and the cumulative one. Because it aggregates modules 09 and 14, both of
those figures have to be honest for this check to mean anything — and because it adds
human time, it is the check most likely to fail.

---

# The Regulated Field Check

This module is the fourth place module 09's list is used: the access and audit review,
with a cadence and an owner. Modules 12 and 14 check that regulated fields do not leak
into events or model inputs; this module checks that somebody is looking, on a schedule,
and leaving evidence.

---

# The Feedback Loop to Product

The only systematic backward flow in the framework runs from here:

```
13-operations  support burden analysis
    ↓
10-execution / 08-product  a flow's unclear state becomes a roadmap item
```

The worked example produces three: an unclear overnight gap, a status indicator whose
meaning is not stated, and an irreversible action the interface never signals. All three
were product defects discovered in a support queue.

---

# What It Sends Forward

| Output | Who consumes it | What they do with it |
| --- | --- | --- |
| `cost_model` | `06-business` | The check, and the regress if it fails |
| `runbooks`, `incident_process` | The operator | Operations |
| `compliance_operations` | The operator, and any auditor | Evidence of practice |
| `support_model` | `11-growth` | What can be promised in the sale |
| Support-derived findings | `08-product`, `10-execution` | Roadmap items |

---

# What It Deliberately Does Not Do

| It does not | Because |
| --- | --- |
| Build mechanisms | `09-technology` designed them |
| Set the price | `06-business` did; this module reports when it does not work |
| Change the scope | `07-strategy` does, on a regress |
| Decide what to measure | `12-metrics` did; this module consumes thresholds |

---

> **Relationships Principle**
>
> Three chains end here, and each ends with something that cannot be deferred: a name, a
> cadence, or a number.
>
> That is why this module produces more regressions than any other — it is the first
> place where the accumulated plan has to be carried by somebody.
