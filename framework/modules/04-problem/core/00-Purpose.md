---
Title: Purpose
Module: 04-problem
Section: core
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define why the Problem module exists and what it establishes for the rest of the run.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - constitution/core
  - 03-user gate passed
Outputs:
  - Shared understanding of what this module establishes
Related Modules:
  - 07-strategy
  - 08-product
Tags:
  - Problem
  - Purpose
  - Foundation
---

# Purpose

---

# Overview

Every module before this one describes a situation: a market, a person, a workflow.

This module makes a **judgment**.

> Is there a problem here worth solving — and do we actually know that, or are we hoping?

It is the honesty checkpoint of the run, and the point at which a project either gains a
real foundation or acquires a comfortable fiction.

---

# Purpose Statement

> Separate the problems that are real and painful from the ones that are merely
> plausible, and be explicit about which is which.

---

# Why This Module Exists

The expensive failure in product development is not building the wrong solution. A wrong
solution gets discovered in weeks — users try it and do not come back.

The expensive failure is building the **right solution to a problem nobody has**. That can
run for a year. Every review goes well. The product works exactly as specified. Nobody
buys it, and nobody can say why.

That failure is preventable, and this is where it gets prevented — by asking, before
anything is designed, what evidence exists that the problem is real, and by refusing to
let inference dress up as knowledge.

---

# The Judgment This Module Makes

Every module downstream inherits this verdict:

| Verdict | Meaning | Consequence |
| --- | --- | --- |
| `VALIDATED` | The core problem is evidenced | Proceed to design |
| `PARTIALLY VALIDATED` | Some problems evidenced, the central one is not | Proceed, but validate the central one first |
| `UNVALIDATED` | Plausible, entirely assumed | Milestone Zero is validation, not building |
| `INVALIDATED` | Research contradicts the premise | Stop, or return to `01-idea` |

**`UNVALIDATED` is a successful outcome**, not a failure of the module. It tells the
operator exactly what to do next and stops them spending six months on a guess.

A framework that only ever reports `VALIDATED` is a rubber stamp, and worth nothing.

---

# Core Objectives

- Harvest every candidate problem from the observed workflow.
- Separate problems from symptoms and from preferences.
- Score each on frequency, severity and the adequacy of the current workaround.
- Divide the evidenced from the assumed, and keep them visibly apart.
- Choose the one problem the product will be built around, and defend it.
- Produce a validation plan for everything still unproven.

---

# What AI Should Learn Here

- A statement with no cost attached is a preference, not a problem.
- A symptom points at a problem; solving the symptom optimizes the wrong thing.
- A problem with a good workaround is one somebody already solved.
- Agreement is not evidence. People confirm almost any problem is real when asked.
- Behavior costing money or effort is the strongest evidence available.
- Only top-three problems get budget.
- Stating "we do not know yet" is research. Filling the gap is not.

---

# Scope

**This module covers**

- Problem harvesting, classification and scoring
- Cost quantification
- Evidence assessment and the validated/assumed split
- Root cause analysis
- The validation plan and stop conditions

**This module does not cover**

| Not here | Belongs to |
| --- | --- |
| Who the user is and what they do | `03-user` — already established |
| Who else solves these problems | `05-competition` |
| What to build about them | `07-strategy` |
| How to specify it | `08-product` |

The line with `03-user` matters: that module establishes **what they do**, this one
establishes **what hurts**. Redoing the workflow here produces the same table twice.

---

# Position in the Run

```
03-user → [ 04-problem ] → 05-competition → 06-business → 07-strategy
```

---

# What This Module Hands Forward

| Output | Consumed by | Used for |
| --- | --- | --- |
| `ranked_problems` | 05, 07, 08 | **Every requirement in module 08 must trace to one of these** |
| Sharpest problem | 07 | The product is built around it |
| `validation_plan` | 07, 09-Roadmap | Milestone Zero, if the problem is assumed |
| Cost per occurrence | 06, 12 | The value case and the metric targets |

Module 08 is the strictest consumer. A requirement that cannot be traced to a ranked
problem fails module 08's gate — which means anything intended to be buildable must be
identified here.

---

# Success Criteria

- Preferences were excluded, with reasons visible.
- Symptoms were traced to the problems beneath them.
- Every problem carries three scores with visible arithmetic.
- A reader can tell at a glance what is proven and what is believed.
- One problem is named as sharpest, and the reasoning survives scrutiny.
- The validation plan contains tests that could actually fail.
- The verdict is stated first, and is not softer than the evidence allows.

---

# Self Assessment

- Did I make a judgment, or only produce a list?
- Can a reader tell which problems are proven?
- Did I choose one problem, and defend the choice?
- Would someone be able to run my validation plan tomorrow?
- If the honest answer is "unproven", did I say it plainly?

---

> **Purpose Principle**
>
> Every later module assumes this one told the truth.
>
> The most valuable sentence this module can produce is:
> *we believe this, we have not proven it, and here is the cheapest way to find out.*
