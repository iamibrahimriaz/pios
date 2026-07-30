---
Title: Problem Tree
Module: 04-problem
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Structure symptoms, problems and causes so the level being addressed is explicit.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 04-problem/knowledge/Problem-Discovery.md
Outputs:
  - Structure within problem_inventory
Related Modules:
  - 07-strategy
  - 08-product
Tags:
  - Problem
  - Structure
  - Method
---

# Problem Tree

---

# What It Is

A structuring device that places observed symptoms above the problem they express, and the problem above
its causes.

```
Symptoms      "notes take too long"   "I forget what was said"
                        ↖              ↗
Problem            Consultation notes are completed after hours
                        ↗              ↖
Causes        No capture during consultation      Records system requires re-entry
```

Its value is that it makes the **level being addressed explicit.** A product can legitimately target a
symptom, a problem, or a cause — but which one it targets changes the scope entirely, and the choice
should be visible rather than implied.

---

# When It Applies

As a working device between Stage 2 (Classify) and Stage 5 (Sharpen). It produces no output of its own;
the inventory and the ranking are what get recorded.

---

# How to Apply It Here

**Build upward from what was observed.** Symptoms are the evidence — they are what people actually said
and did. Problems and causes are inferred from them, and the tags must reflect that: an observed symptom
may be `[verified]` while the problem inferred above it is `[inferred]`.

**Keep one problem per tree.** A tree with three problems in the middle is three trees drawn together, and
it will produce a scope covering all three.

**Mark which level the product will address.** Then check it against `07-strategy`'s eventual MVP line. A
product addressing a cause is usually larger and slower; one addressing a symptom is faster and more
easily displaced. Both are valid, neither is automatic.

**Note causes outside anyone's control.** A cause sitting in another organization's system, in
legislation, or in how a profession is paid is real and immovable. Recording it prevents the tree being
mistaken for a list of things that could be fixed.

**Stop where the answers stop being actionable.** That boundary is `Root-Cause.md`'s subject, and the tree
inherits it.

---

# Where It Misleads

**Trees grow to look complete.** The format invites branches, and branches invite invented causes. Every
node needs the same tagging discipline as any other claim — an unsourced cause in a tidy diagram is an
assumption with a box around it.

**Depth reads as insight.** Four levels down is not more rigorous than two; it is often further from
anything observed. The useful tree is the shallowest one that reaches an actionable cause.

**It implies a single chain of causation.** Most real problems have several contributing causes of unequal
weight, and a tree with no weighting suggests they are equivalent. Where one cause dominates, say so.

**Drawing the tree can substitute for scoring.** Structure is not priority. `Severity.md`, `Frequency.md`
and `Current-Solutions.md` decide what matters; the tree only decides what is above what.

---

# Related

| | |
| --- | --- |
| `Problem-Discovery.md` | The classification the tree arranges |
| `Root-Cause.md` | Where the descent stops |
| `Impact.md` | Weighting the branches |
| `07-strategy` | Where the level chosen becomes scope |

---

> **Concept Note**
>
> The tree's only job is to make the chosen level visible.
>
> Symptom, problem or cause — all three are buildable, and a product
> that has not said which is addressing whichever is cheapest.
