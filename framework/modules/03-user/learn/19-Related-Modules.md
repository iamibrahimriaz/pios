---
Title: Related Modules
Module: 03-user
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show how the User module connects to the rest of the framework and what each downstream module inherits.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 03-user/README.md
Outputs:
  - Understanding of the user stage's position in the chain
Related Modules:
  - 02-market
  - 04-problem
  - 10-execution
Tags:
  - User
  - Relationships
  - Learn
---

# Related Modules

---

# Overview

This module sits between a boundary and a ranking. Module 02 says where the market
ends; this module says who is inside it and what they do; module 04 decides which of
their problems is worth solving.

Its outputs are consumed by more downstream modules than any other research stage.

---

# What It Takes In

| Input | From | Used for |
| --- | --- | --- |
| `idea_brief` | `01-idea` | The premise, including the buyer/user distinction |
| `market_definition` | `02-market` | The boundary segments must fall inside |

The gate fails back to `02-market`, and the usual cause is a boundary too loose to
contain distinguishable groups. If a market is defined as "small businesses," any
segmentation of it is arbitrary — so the fix is upstream rather than here.

---

# What It Sends Forward

| Output | Who consumes it | What they do with it |
| --- | --- | --- |
| `segments` | `04-problem`, `06-business`, `11-growth` | Who problems are ranked for; who is priced; where channels point |
| `personas` | `04-problem`, `08-product` | Context for ranking and for requirements |
| `jobs_to_be_done` | `04-problem`, `08-product`, `14-ai-systems` | The root of the requirement trace |
| `current_workflow` | `04-problem`, `05-competition`, `10-execution` | The status quo profile, and the starting point of every flow |
| `switching_cost` | `05-competition`, `07-strategy`, `11-growth` | Why a better product may not displace a worse one |

---

# The Trace Chain

The framework's requirement trace begins here:

```
03-user  job to be done
    ↓
04-problem  problem derived from the job, then ranked
    ↓
07-strategy  approach chosen against the ranked problems
    ↓
08-product  every requirement traces to a ranked problem
```

Module 08's gate — "every feature traces to a ranked problem" — only means something if
the job at the top was stated without a solution in it. A job written as a feature makes
the whole chain self-confirming, which is why the discipline sits in this module rather
than in module 08 where the check happens.

---

# Where the Current Workflow Reappears

| Module | How it is used |
| --- | --- |
| `05-competition` | Scored as the "do nothing" competitor, which the gate requires |
| `10-execution` | Flows start where the user's situation starts, not where the software does |
| `11-growth` | Time to first value is measured against what the workflow already achieves |
| `14-ai-systems` | The non-AI alternative's performance is often just the current workflow, measured |

Module 14's use is the least obvious and among the most useful: the advocate check asks
whether a competent person could argue for the alternative, and the current workflow is
frequently that alternative, already working.

---

# Where Switching Cost Reappears

It is one of the quiet determinants of the whole run:

- `05-competition` uses it to explain why an inferior incumbent holds position
- `07-strategy` weighs it when choosing an approach — a high switching cost favors
  entering at a seam rather than replacing a workflow
- `11-growth` collides with it directly. A conversion rate assumption that ignores
  switching cost is the most common source of **borrowed growth**, the failure that
  module names.

---

# What It Deliberately Does Not Do

| It does not | Because |
| --- | --- |
| Rank problems | That is `04-problem`, and ranking requires evidence this module only gathers |
| Score the incumbent | That is `05-competition` |
| Design flows | That is `10-execution` |
| Decide the segment is worth serving | Assembled across `04`, `05` and `06` |

---

> **Relationships Principle**
>
> Every module that later checks a trace depends on a job that was written honestly
> here.
>
> A trace is only as good as the thing at the top of it, and nothing downstream can
> repair a job that was a feature all along.
