---
Title: Root Cause
Module: 04-problem
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Ask why until the answers stop being actionable, and make the stopping point a decision.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 04-problem/knowledge/Problem-Tree.md
Outputs:
  - Root cause check within the sharpest problem
Related Modules:
  - 07-strategy
  - 09-technology
Tags:
  - Problem
  - Root Cause
  - Method
---

# Root Cause

---

# What It Is

Repeated questioning — "why does this happen?" — until the answer stops being something anyone could act
on.

```
Notes are completed after hours
  → because nothing is captured during the consultation
    → because typing breaks eye contact
      → because the record system requires structured entry at the point of care
        → because the data model was designed for billing, not consultation
          → (no longer actionable by this product)
```

The purpose is not to reach the deepest cause. It is to know **where the chain leaves this product's
reach**, so that the level being solved is chosen rather than defaulted to.

> Solving a symptom is sometimes correct — the root cause may be outside anyone's control.
>
> But it must be a decision, not an oversight.

---

# When It Applies

In Stage 5 (Sharpen), once the single problem has been chosen. It is a check on that choice, run before
the module hands to `07-strategy`.

---

# How to Apply It Here

**Stop at actionability, not at depth.** The last useful node is the deepest one this product could
plausibly change. Everything below it is context for the risk register.

**Name what is out of reach and why.** Another organization's system, a payment structure, legislation, a
profession's norms. These become constraints in `09-technology` and assumptions in the risk register, and
they explain why the problem persisted — which is `02-market`'s gap question answered from the other
direction.

**Say which level the product addresses, in one sentence.** `07-strategy` needs it to draw the MVP line,
and `08-product` needs it to know which requirements are in scope.

**Distinguish a cause from a constraint.** A cause explains the problem; a constraint limits the solution.
"Typing breaks eye contact" is a cause. "The record system cannot be replaced" is a constraint, and it
belongs in `03-user`'s immovables.

**Check each why against evidence.** A chain of five plausible causal steps with no source is a chain of
five assumptions, and its confidence is that of its weakest link — not its average.

---

# Where It Misleads

**Root-cause analysis reliably terminates in something nobody can fix**, and the framework's discipline is
to notice that rather than to be defeated by it. "The health system is underfunded" is true, deep, and
useless as a product decision.

**Each why is an inference, and they compound.** Five steps of reasonable-sounding causation can arrive
somewhere entirely wrong while every individual step looked sound. Tag the chain, and prefer the shallow
node you can evidence over the deep one you cannot.

**Chains get run until they reach a cause the product happens to address.** That is the analysis performed
backward, and the tell is a chain that stops at exactly the level the intended solution operates at.

**Depth is confused with rigor.** A product solving a well-evidenced symptom for people who are suffering
now is worth more than one solving a deep cause nobody asked about.

---

# Related

| | |
| --- | --- |
| `Problem-Tree.md` | The structure this descends |
| `Current-Solutions.md` | Why the cause has survived |
| `Evidence.md` | Tagging each link in the chain |
| `07-strategy` | Where the chosen level becomes scope |

---

> **Concept Note**
>
> Ask why until the answer is no longer yours to act on — then say
> where you stopped.
>
> An unstated stopping point means the level was chosen by
> convenience.
