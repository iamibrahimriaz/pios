---
Title: Related Modules
Module: 04-problem
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show how the Problem module connects to the framework and where a declared shortfall travels.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 04-problem/core/00-Purpose.md
Outputs:
  - Understanding of the problem stage's position in the chain
Related Modules:
  - 03-user
  - 07-strategy
  - 08-product
Tags:
  - Problem
  - Relationships
  - Learn
---

# Related Modules

---

# Overview

This module converts description into ranking, and the ranking is consumed by nearly
everything that follows. It is also the origin of one of the framework's four chains —
the one that starts with a declared shortfall and ends in a strategic weighting.

---

# What It Takes In

| Input | From | Used for |
| --- | --- | --- |
| `personas` | `03-user` | Who has the problem |
| `jobs_to_be_done` | `03-user` | What the problem obstructs |
| `current_workflow` | `03-user` | Where workarounds are found — the strongest evidence available |

The gate fails back to `03-user`, and the usual cause is jobs stated as features. A job
containing a solution cannot generate a problem statement; it generates a feature
request wearing one.

---

# What It Sends Forward

| Output | Who consumes it | What they do with it |
| --- | --- | --- |
| `ranked_problems` | `05-competition`, `07-strategy`, `08-product` | What competitors are scored against; what strategy chooses against; what every requirement traces to |
| `problem_inventory` | `07-strategy` | The full set, including what was not ranked highly |
| `evidence_log` | Everything downstream | The record of what is actually known |
| `validation_plan` | The operator, and `10-execution` | What would resolve the uncertainty, and when it can be run |

---

# Milestone Zero

The framework's **Milestone Zero chain** begins here, and it appears in four places:

```
04-problem     declares it — the one thing that must be learned first
    ↓
07-strategy    makes it binding on the chosen approach
    ↓
10-execution   sequences it first, before anything else is built
    ↓
11-growth      gates spending on it — no acquisition budget until it resolves
```

Milestone Zero exists because a run with genuine uncertainty should spend its first
effort removing it, rather than building on it. When module 04 declares a shortfall,
Milestone Zero is usually the validation step that would fill it.

---

# Where the Shortfall Travels

A declared shortfall is not a note. It has an obligation attached:

| Module | What it must do with a declared shortfall |
| --- | --- |
| `07-strategy` | Weight the solution comparison — approaches that survive the problem being wrong gain value |
| `10-execution` | Sequence the validation as Milestone Zero |
| `11-growth` | Withhold acquisition spend until it resolves |

If none of those changed, the shortfall was declared and not carried. That outcome is
worth checking for explicitly, because it produces a document that looks rigorous and
behaved as though nothing was unknown.

---

# The Requirement Trace

```
03-user       job to be done
    ↓
04-problem    problem, ranked with evidence
    ↓
07-strategy   approach chosen against the ranking
    ↓
08-product    every requirement traces back to a ranked problem
```

Module 08's gate depends entirely on this module's output being real. A ranking built
to justify a solution makes that gate self-confirming — the requirement traces to the
problem that was written to justify it.

---

# What It Deliberately Does Not Do

| It does not | Because |
| --- | --- |
| Propose solutions | That is `07-strategy`, three modules later, deliberately |
| Score competitors | That is `05-competition`, which consumes this ranking |
| Run the validation | It produces the plan; execution is scheduled in `10-execution` |
| Decide viability | Assembled across `05` and `06` |

The three-module gap before solutions is one of the framework's few pieces of
deliberate friction. It exists because a solution proposed here would immediately begin
shaping the ranking that is supposed to judge it.

---

> **Relationships Principle**
>
> This module hands forward two things: what is known, and what is not.
>
> The second one is easy to drop, and the framework's four-place Milestone Zero chain
> exists specifically to stop it being dropped.
