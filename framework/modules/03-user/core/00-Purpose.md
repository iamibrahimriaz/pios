---
Title: Purpose
Module: 03-user
Section: core
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define why the User module exists and what it establishes for the rest of the run.
Audience:
  - AI Agents
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - constitution/core
  - 02-market gate passed
Outputs:
  - Shared understanding of what this module establishes
Related Modules:
  - 04-problem
  - 08-product
  - 10-execution
Tags:
  - User
  - Purpose
  - Foundation
---

# Purpose

---

# Overview

Module 02 established a market — a population inside a boundary.

A population cannot be designed for. This module narrows it to one person, and then to
what that person is actually doing today.

The narrowing is not a formality. It is the difference between a product specification and
a description of an average that no real person matches.

---

# Purpose Statement

> Identify who is served, what they are trying to get done, and what they do today —
> precisely enough that the rest of the run can be built for them.

---

# Why This Module Exists

Products fail for users who were never really identified.

The failure has a recognizable shape: a persona that could describe anyone, a job
statement that names the feature the team already wanted to build, and no assessment of
what it would cost the user to change.

Each of those errors is invisible downstream. Module 08 will write requirements for the
imaginary user. Module 10 will design flows for a working day that does not exist. Nobody
re-examines the persona, because by then it reads like established fact.

This module exists to make sure the person is real, and to be honest about how we know.

---

# The Constraint That Shapes This Module

An agent cannot meet the user.

Module 02 can read a regulation. Module 05 can read a pricing page. This module needs to
know what someone does on a Tuesday morning, and no document states that directly.

The temptation is to write a plausible persona anyway. It will read well and be wrong, and
nothing downstream will catch it.

So this module carries an unusual amount of machinery about **honesty**: a declared
research mode, a prohibition on invented quotes, a mandatory gaps section, and a
confidence ceiling when no real user was consulted.

An inferred user, labeled as inferred, is workable. An inferred user presented as observed
is a fabrication that six modules will trust.

---

# Core Objectives

- Divide the market into segments that behave differently.
- Commit to one segment, defensibly.
- Build a persona every row of which can be traced.
- Document what the person does today, with the tools named.
- Assess what it would cost them to change.
- Name the jobs they are trying to get done, independent of any solution.

---

# What AI Should Learn Here

- A segment is only a segment if its members behave differently.
- A persona that could describe anyone describes no one.
- The opportunity is usually in the friction between steps, not in the steps.
- The tool being replaced is usually the real competitor — often paper, or nothing.
- A job survives changes of solution. A feature does not.
- Switching cost decides adoption more often than product quality does.
- What a person will not change defines the shape of what can be built.

---

# Scope

**This module covers**

- Segmentation and prioritization
- Personas, primary and secondary
- Current workflow and its friction
- Switching cost
- Jobs to be done
- Immovable habits and constraints

**This module does not cover**

| Not here | Belongs to |
| --- | --- |
| Ranking and quantifying problems | `04-problem` |
| Competitor comparison | `05-competition` |
| Willingness to pay | `06-business` |
| Screen and interaction design | `10-execution` |
| Acquisition channels | `11-growth` |

This module establishes **who** and **what they do now**. Module 04 establishes **what
hurts**. Keeping that line clear stops the two modules producing the same table twice.

---

# Position in the Run

```
01-idea → 02-market → [ 03-user ] → 04-problem → 05-competition
```

`04-problem` cannot start until this module passes. It is the direct consumer of the
workflow, the personas and the jobs.

---

# What This Module Hands Forward

| Output | Consumed by | Used for |
| --- | --- | --- |
| `segments` | 04, 05, 06 | Scoping problems, competitors and pricing |
| `personas` | 04, 08, 10 | Requirements and flow design |
| `jobs_to_be_done` | 04, 08, 14 | Tracing every requirement to a real need |
| `current_workflow` | 04, 10 | Ranking problems; designing around reality |
| `switching_cost` | 06, 11 | Pricing, onboarding and migration |

`04-problem` is the heaviest consumer. A thin workflow leaves module 04 with nothing to
rank problems against, and it will fail its gate.

---

# Success Criteria

- The segments would clearly behave differently, and the choice between them is obvious.
- The persona could not describe anyone else in the market.
- Every persona row is traceable, or openly marked as inference.
- The workflow names real products, including paper where that is the truth.
- Switching cost is assessed honestly, including what makes adoption hard.
- Every job would survive the product being built a completely different way.
- A reader knows immediately whether a real user was consulted.

---

# Self Assessment

- Can I name one person, not a category?
- Could every claim about them be traced to something?
- Do I know what they do today, step by step, with the tools named?
- Do I know what it costs them to change?
- Have I stated honestly how much of this is inferred?

---

> **Purpose Principle**
>
> The market tells you how many people might buy.
>
> This module tells you what to build — and it only works if the person is real.
