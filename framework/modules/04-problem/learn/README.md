---
Title: Learn — Problem
Module: 04-problem
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Orient a human learner in the Problem module — the framework's evidence checkpoint and the only place a declared shortfall is permitted.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 03-user/learn/README.md
  - 04-problem/README.md
Outputs:
  - A reading path through the Problem module
Related Modules:
  - 03-user
  - 07-strategy
Tags:
  - Problem
  - Curriculum
  - Learn
---

# Learn — Problem

---

# What This Layer Is

The human curriculum for the Problem module. An executing agent does not read it.

---

# What the Module Does

It separates problems that are real, painful and frequent from problems that were
assumed. It produces a problem inventory, a ranking, an evidence log, and a validation
plan for whatever remains unproven.

This is the framework's **evidence checkpoint**. Modules 01 through 03 collect; this
is where the collection is tested and where the honest answer is sometimes that there
is not enough.

---

# The Thing That Makes This Module Different

Its gate requires at least three problems carrying `[verified]` evidence — real
evidence, not inference. And it is the only module in the framework permitted to pass
that criterion **unmet**, by invoking `declared_shortfall`.

That mechanism exists because the alternative is worse. A run that cannot produce
verified problems will otherwise do one of two things: halt, which is often
disproportionate, or quietly reclassify inference as verification, which is fatal and
invisible.

> A declared shortfall is not a failure. It is a finding that travels — and downstream
> modules are required to weight it.

Module 07 is where the weighting happens. A run that declares a shortfall here should
see it change the strategy comparison there, and if it does not, the declaration was
decorative.

---

# Reading Order

| Read | File | What you get |
| --- | --- | --- |
| 1 | `01-Why-It-Matters.md` | Why this is the checkpoint |
| 2 | `02-Learning-Objectives.md` | What you should be able to do afterward |
| 3 | `10-Common-Mistakes.md` | How evidence gets manufactured |
| 4 | `16-Evaluation.md` | How to check your own ranking |
| 5 | `17-Reflection.md` | Questions after a real run |
| 6 | `19-Related-Modules.md` | Where the shortfall travels |
| 7 | `20-Future-Improvements.md` | What this module still does poorly |

---

# The Three Things Worth Learning Here

**Frequency, severity and workaround are the three axes.** A problem that is severe and
annual loses to one that is mild and daily, more often than product teams expect —
because the mild daily one has already produced a workaround, and a workaround is
evidence of demand.

**The workaround is the strongest signal available before launch.** Somebody built a
spreadsheet. That is not a complaint; it is a purchase, paid in time.

**Inference is not evidence, and the distinction is the whole module.** "Users must
find this frustrating" is a reasonable inference and it is not a verified problem. The
framework's central prohibition applies most sharply here: an assumption must never be
smoothed into a fact.

---

# What You Should Read Instead, and When

| If you want | Read |
| --- | --- |
| To run the module | `04-problem/core/06-Framework.md` |
| To understand scoring, evidence or root causes | `04-problem/knowledge/` |
| To understand what validation actually proves | `04-problem/knowledge/validation/` |
| To see manufactured evidence | `04-problem/resources/15-Anti-Examples.md` |

---

> **Learn Principle**
>
> This is the module where a run finds out whether it knows anything.
>
> Every module before it produces description. This one asks for proof, and it is
> built to make the answer "not yet" survivable — but only if it is said out loud.
