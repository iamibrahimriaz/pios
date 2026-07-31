---
Title: Learn — Business
Module: 06-business
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Orient a human learner in the Business module — the source of the three arithmetic checks the rest of the framework runs against.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 05-competition/learn/README.md
  - 06-business/core/00-Purpose.md
Outputs:
  - A reading path through the Business module
Related Modules:
  - 09-technology
  - 11-growth
  - 13-operations
Tags:
  - Business
  - Curriculum
  - Learn
---

# Learn — Business

---

# What This Layer Is

The human curriculum for the Business module. An executing agent does not read it.

---

# What the Module Does

It establishes whether a viable business exists around the solution. It produces a
business model, a pricing strategy, unit economics, a go-to-market approach, and a
revenue model.

Its gate asks four things, and the first one catches most failures: **the payer must be
identified and distinguished from the user.**

---

# Why This Module Reaches Further Than Any Other

The numbers set here become ceilings that three later modules are required to check
themselves against:

```
06-business sets the economics
    ↓
09-technology   checks infrastructure cost per user against it
11-growth       checks implied CAC against the payback ceiling
13-operations   checks the true cost to serve against it
```

These are the framework's **three arithmetic checks**. Each one is a place where a
downstream module can discover that the business does not work — and where the correct
response is to **regress** to this module rather than to revise the estimate that just
failed.

> A cost check that gets absorbed by lowering the forecast is the failure these checks
> exist to prevent. It is individually defensible every single time it happens.

---

# The Three Things Worth Learning Here

**Who pays is a different question from who benefits.** In business software they are
routinely different people with different criteria, and a product designed for one and
sold to the other fails at the last meeting.

**Price is set against value and constrained by the alternative.** Module 05 supplies
the constraint. The value calculation supplies the ceiling. When they conflict — as in
the worked example, where a free incumbent constrained a genuinely valuable service —
that conflict is the finding, not an inconvenience.

**Unit economics before launch are assumptions with arithmetic around them.** CAC,
churn, conversion and willingness to pay have no source before you have customers. The
discipline is naming the load-bearing one and running a sensitivity, not producing a
confident table.

---

# Reading Order

| Read | File | What you get |
| --- | --- | --- |
| 1 | `01-Why-It-Matters.md` | Why the payer question comes first |
| 2 | `02-Learning-Objectives.md` | What you should be able to do afterward |
| 3 | `10-Common-Mistakes.md` | How a model becomes a wish with arithmetic |
| 4 | `16-Evaluation.md` | How to check your own economics |
| 5 | `17-Reflection.md` | Questions after a real run |
| 6 | `19-Related-Modules.md` | The three arithmetic checks in detail |
| 7 | `20-Future-Improvements.md` | What this module still does poorly |

---

# What You Should Read Instead, and When

| If you want | Read |
| --- | --- |
| To run the module | `06-business/core/06-Framework.md` |
| To understand a model or a metric | `06-business/knowledge/` |
| To compare pricing structures | `06-business/knowledge/pricing/` |
| To see a model that cannot fail | `06-business/resources/15-Anti-Examples.md` |

---

> **Learn Principle**
>
> Every number in this module is an assumption until somebody pays.
>
> The skill is not producing better numbers. It is producing numbers that show you
> which one to worry about.
