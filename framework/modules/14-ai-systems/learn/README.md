---
Title: Learn — AI Systems
Module: 14-ai-systems
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Orient a human learner in the AI Systems module — where every capability must beat a non-AI alternative and detectability governs autonomy.
Audience:
  - Product Managers
  - Founders
  - Engineers
Prerequisites:
  - 09-technology/learn/README.md
  - 14-ai-systems/README.md
Outputs:
  - A reading path through the AI Systems module
Related Modules:
  - 08-product
  - 09-technology
  - 07-strategy
Tags:
  - AI
  - Curriculum
  - Learn
---

# Learn — AI Systems

---

# What This Layer Is

The human curriculum for the AI Systems module. An executing agent does not read it.

---

# What the Module Does

It decides where AI genuinely improves the product, and how it will be evaluated. It
produces AI opportunities, a model strategy, data requirements, an evaluation plan, and
failure modes.

It is last in the framework deliberately. A capability proposed before the problem is
ranked, the product is specified and the data model exists is a capability proposed from
what is possible rather than from what is needed.

---

# The Two Named Checks

**The advocate check.** Could a competent person argue for the non-AI alternative in one
honest sentence? If not, it was a straw man and the comparison proved nothing.

**The wrongness cost.** What does one wrong output cost, who bears it, and — the decisive
question — **can the user detect it?**

---

# The Principle That Governs Everything

> **Detectability governs autonomy, not accuracy.**

A 1% error rate that is undetectable and consequential is more dangerous than a 10% rate
that is visibly wrong. When a user could only catch an error by redoing the work the
product exists to remove, the autonomy ceiling is drafts — permanently, regardless of how
good the model becomes.

---

# The Named Failure

**Capability theater** — AI added because it is expected, justified against an alternative
nobody argued for. It is detectable by one symptom: the alternative in the comparison is
described in a way its own advocate would not recognize.

---

# What the Worked Example Shows

The run threaded through this framework's resources ends here, and it ships no AI. Three
capabilities proposed: one orphan rejected outright, one lost to a form field, one lost to
a human — and kept as a triggered transition candidate for when data exists.

The product that began as "an AI scribe for doctors" ends as a human transcription
service with a path to automation. Nothing was suppressed to get there.

---

# Reading Order

| Read | File | What you get |
| --- | --- | --- |
| 1 | `01-Why-It-Matters.md` | Why the alternative wins more often than expected |
| 2 | `02-Learning-Objectives.md` | What you should be able to do afterward |
| 3 | `10-Common-Mistakes.md` | Theater, benchmarks, projected data |
| 4 | `16-Evaluation.md` | How to check your own proposals |
| 5 | `17-Reflection.md` | Questions after a real run |
| 6 | `19-Related-Modules.md` | What this module inherits and what it checks |
| 7 | `20-Future-Improvements.md` | What this module still does poorly |

---

# What You Should Read Instead, and When

| If you want | Read |
| --- | --- |
| To run the module | `14-ai-systems/core/06-Framework.md` |
| Concepts — evaluation, guardrails, data requirements | `14-ai-systems/knowledge/` |
| To see capability theater | `14-ai-systems/resources/15-Anti-Examples.md` |

---

> **Learn Principle**
>
> This module's most valuable output is frequently a decision not to build something.
>
> A run that proposes three capabilities and ships none has not failed. It has spent an
> afternoon instead of two quarters.
