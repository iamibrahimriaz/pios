---
Title: Learn — Market
Module: 02-market
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Orient a human learner in the Market module — what it establishes, and why sizing is the smallest part of it.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 01-idea/learn/README.md
  - 02-market/core/00-Purpose.md
Outputs:
  - A reading path through the Market module
Related Modules:
  - 01-idea
  - 05-competition
  - 09-technology
Tags:
  - Market
  - Curriculum
  - Learn
---

# Learn — Market

---

# What This Layer Is

The human curriculum for the Market module. An executing agent does not read it.
Nothing here changes how a run behaves — the operating instructions are in `core/`,
the concepts are in `knowledge/`, and the worked artifacts are in `resources/`.

---

# What the Module Does

It answers a narrower question than its name suggests: **what boundary is this product
entering, and what is true about that boundary.**

It produces five things — a market definition, TAM/SAM/SOM, trends with direction and
evidence, the regulatory landscape, and the gaps. Learners expect the sizing to be the
centerpiece. It is not. The two outputs that do the most downstream work are the
**boundary** and the **regulatory landscape**.

> A market number is consumed once, by a decision about whether to continue. A
> regulatory finding is consumed by modules 09, 12, 13 and 14, and it becomes an
> obligation somebody has to run on a schedule.

---

# Reading Order

| Read | File | What you get |
| --- | --- | --- |
| 1 | `01-Why-It-Matters.md` | Why a boundary beats a number |
| 2 | `02-Learning-Objectives.md` | What you should be able to do afterward |
| 3 | `10-Common-Mistakes.md` | Where market work goes wrong |
| 4 | `16-Evaluation.md` | How to check your own sizing |
| 5 | `17-Reflection.md` | Questions after a real run |
| 6 | `19-Related-Modules.md` | The obligation chain, and where it starts |
| 7 | `20-Future-Improvements.md` | What this module still does poorly |

---

# The Two Things Worth Learning Here

**Sizing is an argument, not a lookup.** Every TAM number is a chain of assumptions
with a figure at the end. The number's usefulness is entirely in whether the chain is
visible. A sourced number with a hidden step is less useful than a rough one with the
steps shown.

**The obligation chain starts here.** A regulatory constraint found in this module
becomes a mechanism in `09-technology` and a scheduled obligation with a named owner
in `13-operations`. That chain is one of the four that hold the framework together,
and this is its origin. A constraint missed here is missed everywhere.

---

# What You Should Read Instead, and When

| If you want | Read |
| --- | --- |
| To run the module | `02-market/core/06-Framework.md` |
| To understand timing, TAM, or a specific frame | `02-market/knowledge/` |
| To see a sized market done badly | `02-market/resources/15-Anti-Examples.md` |
| To know what it produces | `02-market/module.yaml` |

---

> **Learn Principle**
>
> Most people come to this module wanting to know how big the market is.
>
> The more valuable question it answers is where the market ends — because that is the
> answer every later module actually uses.
