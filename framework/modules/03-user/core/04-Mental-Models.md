---
Title: Mental Models
Module: 03-user
Section: core
Category: Thinking Framework
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the lenses through which users and their behavior should be examined.
Audience:
  - AI Agents
  - Product Managers
  - Researchers
Prerequisites:
  - 03-user/core/03-Core-Principles.md
Outputs:
  - Multi-perspective user analysis
Related Modules:
  - 04-problem
  - 10-execution
Tags:
  - User
  - Mental Models
---

# Mental Models

---

# Model Statement

> A user is not one thing. They are a role, a day, a set of constraints, and a habit —
> and each of those reveals something the others hide.

---

# 1. Jobs To Be Done

**Reveals:** what the person is trying to achieve, independent of any solution.

```
When «situation», I want to «motivation», so I can «outcome».
```

The value of the model is its **stability**. Solutions change constantly; the underlying
job rarely does. Building against jobs produces products that survive their own
redesigns.

**Hides:** it says nothing about feasibility, willingness to pay, or how the job ranks
against the person's other jobs. A job can be real and still not worth serving.

**Common misuse:** writing the intended feature in job grammar. The test is whether the
statement would still be true if the product were built completely differently.

---

# 2. The Hiring Metaphor

**Reveals:** why someone chose their current solution, and what would make them fire it.

People "hire" a product to do a job. They fire it when something does the job better, or
when the cost of keeping it exceeds the cost of change.

Ask: what did they hire before this? What made them fire it? What would make them fire
what they use now?

**Hides:** it assumes a deliberate choice. Many current workflows were never chosen — they
accumulated. "Nobody decided this" is a legitimate and useful finding.

---

# 3. Workflow Archaeology

**Reveals:** where the opportunity actually is.

Document what happens today, step by step. Then look at the **gaps between steps** rather
than the steps themselves.

The friction is rarely inside a task. It is in the handoff: re-entering data, waiting for
someone, switching tools, remembering something the system did not carry forward.

**Hides:** it describes the present, not the possible. A workflow perfectly documented can
still lead to optimizing something that should be eliminated. Pair it with Jobs To Be Done.

---

# 4. The Switching Equation

**Reveals:** whether adoption is realistic.

```
switch if:   (value of new − value of current)  >  (migration + retraining
                                                    + disruption + risk)
```

Most product thinking optimizes the left side. Adoption is usually decided by the right.

**Hides:** it treats a personal decision as arithmetic. Real switching involves who gets
blamed if it fails — which is why the "risk" term is often larger than any real cost.

---

# 5. Buyer, User, Blocker

**Reveals:** that the decision usually involves more than one person.

| Role | Cares about |
| --- | --- |
| User | Whether it makes their day better |
| Buyer | Whether it justifies the cost |
| Blocker | Whether it creates risk they own |

A product loved by users and rejected by a blocker does not get adopted. In regulated or
organizational contexts, the blocker is often the deciding party and is almost never
interviewed.

**Hides:** in solo or consumer contexts all three may be one person — in which case say so
explicitly rather than inventing three personas.

---

# 6. The Day, Not the Session

**Reveals:** the real conditions the product must survive.

Product thinking imagines a focused user at a clean desk. Reality is interruptions, time
pressure, poor connectivity, shared devices, and someone waiting.

Ask: what is happening around this person while they use the product? What interrupts
them? What happens to their work when it does?

**Hides:** nothing — but it is routinely skipped, and it is the model most likely to change
a design decision.

---

# 7. Stated vs Revealed Preference

**Reveals:** the gap between what people say and what they do.

Stated preference is what someone reports when asked. Revealed preference is what their
behavior shows.

They diverge constantly. People say they want more features and use three. They say price
is the objection and switch for convenience.

Weight revealed preference higher — and when working from proxy sources, prefer evidence
of **behavior** (what workarounds exist, what gets abandoned) over evidence of **opinion**
(what reviewers say they want).

**Hides:** revealed preference only shows what was possible within existing options. It
cannot reveal demand for something that has never existed.

---

# 8. The Immovable

**Reveals:** the boundary of what can be built.

Every user has things that will not change: a professional obligation, a physical
constraint, an institutional system, an ingrained habit.

A product that requires an immovable to move will not be adopted, regardless of quality.

Ask directly: what would this person refuse to give up?

**Hides:** immovables occasionally do move — when regulation changes, or a generation
turns over. Distinguish "will not change" from "has not changed yet".

---

# 9. The Empathy Check

**Reveals:** whether the persona is a person or a template.

Read the persona and ask: could this describe anyone in this market?

If yes, it will not constrain a single decision, and every downstream module will
substitute its own imagined user.

**Hides:** specificity can become false precision. A vividly written persona built on no
evidence is more dangerous than a vague one, because it is more convincing.

---

# 10. The Source Inversion

**Reveals:** what the evidence is not telling you.

Every proxy source is self-selected. Review writers are the annoyed and the delighted.
Forum posters are the technically engaged. Study participants are whoever agreed.

Ask: **who is missing from my sources, and would they say something different?**

The silent majority in most markets is people for whom the current workflow is tolerable —
and they are the hardest to convert and the easiest to forget.

**Hides:** nothing. It is the correction for every other model in this list.

---

# Combining Models

| Situation | Model |
| --- | --- |
| Naming what to build against | Jobs To Be Done |
| Understanding the incumbent | The Hiring Metaphor |
| Finding the opportunity | Workflow Archaeology |
| Judging adoption realism | The Switching Equation |
| Mapping the decision | Buyer, User, Blocker |
| Designing for reality | The Day, Not the Session |
| Weighing evidence | Stated vs Revealed Preference |
| Bounding the possible | The Immovable |
| Testing the persona | The Empathy Check |
| Correcting for bias | The Source Inversion |

Apply Workflow Archaeology before Jobs To Be Done — observe before interpreting. Apply The
Source Inversion last, to everything.

---

# Self Assessment

- Did I document behavior before naming jobs?
- Do I know what they hired before, and why they fired it?
- Did I look at the gaps between steps, not just the steps?
- Did I weigh switching cost against product value honestly?
- Do I know who could block this decision?
- Would my persona survive the empathy check?
- Who is missing from my sources?

---

> **Mental Model Principle**
>
> Every model here makes a person simpler than they are.
>
> Use several, and give the most weight to the one that makes adoption look hardest.
