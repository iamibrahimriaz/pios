---
Title: Related Modules
Module: 10-execution
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show how the Execution module connects to the framework and where the build handoff goes.
Audience:
  - Product Managers
  - Founders
  - Engineers
Prerequisites:
  - 10-execution/core/00-Purpose.md
Outputs:
  - Understanding of the execution stage's position in the chain
Related Modules:
  - 08-product
  - 09-technology
  - 13-operations
Tags:
  - Execution
  - Relationships
  - Learn
---

# Related Modules

---

# Overview

This module is the framework's exit point for building. Everything before it produces
decisions; this produces work. Only one module comes after it in the delivery line —
operations — and it consumes this module's plan directly.

---

# What It Takes In

| Input | From | Used for |
| --- | --- | --- |
| `prd_body` | `08-product` | What is being built |
| `acceptance_criteria` | `08-product` | The definition of done, and the QA strategy |
| `edge_cases` | `08-product` | Which states the flows must cover |
| `data_model` | `09-technology` | What the build starts from |
| `api_contract` | `09-technology` | The interface flows are built against |
| `architecture` | `09-technology` | What is being assembled |
| `current_workflow` | `03-user` | Where flows actually start |
| `roadmap` | `07-strategy` | The sequence's outer shape |

The last two are the ones people forget. Module 03's workflow is what stops a flow
starting at a screen, and it is six modules upstream by the time it is needed.

The gate fails back to `09-technology`, usually because a flow requires something the
interface contract does not provide.

---

# What It Sends Forward

| Output | Who consumes it | What they do with it |
| --- | --- | --- |
| `build_handoff` | The builder or agent | The thing that gets acted on |
| `ux_flows` | `11-growth`, `12-metrics` | Time to first value; where events fire |
| `delivery_plan` | `13-operations` | What is being launched and when |
| `milestones` | `11-growth` | What growth can assume exists |
| `qa_strategy` | `13-operations` | What was tested, and what was not |

---

# The Milestone Zero Chain, Completed

```
04-problem     declares the shortfall
07-strategy    makes resolving it binding on the approach
10-execution   SEQUENCES IT FIRST
11-growth      withholds acquisition spend until it resolves
```

This module is the third of the four. It is where the chain becomes a date rather than a
commitment, and it is the last place the chain can be honored — module 11 can only
withhold spend against a milestone that exists.

---

# Where the Flows Reappear

| Module | How |
| --- | --- |
| `11-growth` | Time to first value is measured along a flow drawn here, in minutes |
| `12-metrics` | Instrumentation is specified at points in these flows |
| `13-operations` | Support burden analysis traces complaints back to a flow's unclear state |

Module 13's use is the feedback loop. When the most common support request is "where is
my note from yesterday," that is a flow problem discovered in operations and returned
here as a product change. The worked example carries three such items to the roadmap.

---

# The Handoff Standard

The gate's requirement — readable by an agent with no prior context — is what makes this
module's output usable by an automated builder as well as by a person. That is not an
incidental property of the framework; it is why the standard is written that way.

A handoff meeting that standard also survives the author leaving, a six-month pause, and
a change of team. Those are the same problem.

---

# What It Deliberately Does Not Do

| It does not | Because |
| --- | --- |
| Specify the product | `08-product` did |
| Choose the architecture | `09-technology` did |
| Design the visual appearance | Flows are structure; appearance is a craft this framework does not cover |
| Run the product | `13-operations` takes over at launch |

---

> **Relationships Principle**
>
> This module's output is the only one in the framework that somebody acts on directly.
>
> Everything upstream is judged by whether it made this document possible; everything
> downstream is judged by whether it survived contact with what this document produced.
