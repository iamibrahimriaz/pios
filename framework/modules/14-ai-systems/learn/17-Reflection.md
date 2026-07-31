---
Title: Reflection
Module: 14-ai-systems
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Prompt a learner to examine why they wanted to build the capability.
Audience:
  - Product Managers
  - Founders
  - Engineers
Prerequisites:
  - 14-ai-systems/learn/16-Evaluation.md
Outputs:
  - Examined assumptions about your own AI instincts
Related Modules:
  - 07-strategy
  - 08-product
Tags:
  - AI
  - Reflection
  - Learn
---

# Reflection

---

# Overview

This module asks you to argue against something you proposed. These questions are about
how that went.

---

# On the Proposal

**Why did you want to build this?** The honest answers include: it solves a ranked
problem, it is interesting, it is expected, and I wanted to learn it. Only the first is a
justification, and the others are not disqualifying provided they are named.

**Would you propose it if nobody ever knew the product used AI?** A useful test for
capability theater.

**Which ranked problem does it serve?** If none, it is an orphan and the honest disposition
is rejection.

---

# On the Alternative

**Could you argue for it in front of someone who prefers it?** If not, you have not
understood it.

**What would the form field cost, in total?** Build, maintenance, evaluation, failure
surface. Compare honestly. The form field usually wins on everything except quality, and
sometimes on that too.

**Did the alternative win?** If it never does, the check is decorative. In the worked
example all three alternatives won, and that run produced a better product than the one
that started it.

---

# On Wrongness

**Who bears the cost of a wrong output?** If the answer is the user rather than you, the
bar is higher and the autonomy ceiling is lower.

**Would they know?** Sit with this one. The honest answer is frequently no, and it changes
the design more than any accuracy target.

**What is the worst realistic outcome?** Write it without softening. In the worked example
it is a wrong dosage entering a clinical record and a future decision resting on it —
stated plainly, which is what made the drafts-only ceiling obviously correct.

---

# On the Data

**Does it exist today?** Not will exist. Does.

**Do you have the right to use it this way?** And is that a legal answer or an assumption?

**Is the provider's training on your data contracted off, or assumed?** These are different
answers and only one of them survives a customer's security review.

---

# On the Bar

**What happens if you miss it?** Decide now. Afterwards, the answer is negotiated by
people who have spent a quarter building.

**Who judges quality?** If it is the build team, the evaluation measures satisfaction
rather than accuracy. A domain expert produces a different number.

---

# On Your Own Pattern

| Look for | What it suggests |
| --- | --- |
| Your alternatives never win | The comparison is decorative |
| You reach for a model before a rule | Determinism is being undervalued |
| Your autonomy ceilings follow accuracy | Detectability is not yet operating |
| Your golden sets are clean | You measure where it works |
| You have never rejected a capability | The module is confirming rather than deciding |

---

# The Question Worth Returning To

> If this capability were removed tomorrow, what would the user do instead — and how much
> worse would it be?

If the answer is "use the form" and "slightly," the alternative should have won. If the
answer is "they could not do this at all," you have something worth the evaluation
infrastructure.

Most proposed capabilities are the first. Finding that out costs an afternoon, and the
alternative is finding out after two quarters of building an evaluation harness for
something a checklist would have done deterministically.

---

> **Reflection Principle**
>
> The pressure to include AI comes from outside the product and is resolved inside it.
>
> The reflection that matters is separating what your ranked problems need from what
> everybody expects you to have built.
