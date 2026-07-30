---
Title: Questions
Module: 01-idea
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define what makes a clarifying question worth asking the operator.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 01-idea/core/08-Questions-To-Answer.md
Outputs:
  - clarifying_questions
Related Modules:
  - 03-user
Tags:
  - Idea
  - Questions
  - Concept
---

# Questions

---

# What It Is

A question whose answer changes what happens next.

This module's gate requires at least five, answered or explicitly deferred, because module 01 is
the framework's first human checkpoint and the only place where asking is cheap.

Three classes:

| Class | Answered by | Example |
| --- | --- | --- |
| **Operator** | The person whose idea this is | "Which country's health system?" |
| **Needs user** | Real people, later | "How do clinicians currently handle this?" |
| **Resolvable** | Research in a later module | "What does the regulation require?" |

Only the first class belongs at the checkpoint. The other two are recorded and routed.

---

# When It Applies

In Pass 4 (Surface) and at the checkpoint that closes the module.

---

# How to Apply It Here

**Ask only what changes the run.** The test: name the module whose output would differ depending
on the answer. If none would, the question is curiosity.

| Weak | Strong |
| --- | --- |
| "What features are you imagining?" | "Are you selling to individual practices or to a health system?" — changes modules 03, 06 and 11 |
| "Who are the competitors?" | "Is there a system they are contractually required to use?" — may end the idea |
| "What is the vision?" | "Is there a jurisdiction you will not operate in?" — changes 02 |

**Ask the blocking questions first.** Some answers determine whether later research is even
possible. Jurisdiction, buyer, and whether the operator has domain access are the usual three.

**Offer a default with each question.** An operator answers "which segment first?" more easily
when given a recommendation and a reason. A checkpoint of open-ended questions is work handed
back rather than a decision requested.

**Route the rest.** A `NEEDS USER` question goes to `state.open_questions` and reappears in
`03-user`. A resolvable question goes to whichever module resolves it. Neither gets guessed at
here.

**Do not ask what the operator cannot know.** "What will your churn be?" is not a clarifying
question; it is a forecast, and asking for it invites a number that will be treated as a fact.

---

# Where It Misleads

**A long question list reads as diligence and delays the run.** Five sharp questions produce
better answers than twenty, because the operator answers all five properly.

**Deferring is not free.** A deferred question with no owner and no module attached is a gap that
resurfaces as an assumption in module 06. Deferral is a routing decision, and it must name a
destination.

**The operator's answer is evidence about the operator, not about the market.** It is tagged
`[verified: operator]`, which means the source is known — not that the claim is true. A founder's
description of their users' workflow is a strong hypothesis and a weak finding.

---

# Related

| | |
| --- | --- |
| `Assumptions.md` | What an unanswered question becomes |
| `Stakeholders.md` | The subject of the most valuable questions |
| `engine/evidence-policy.md` | How operator answers are tagged |

---

> **Concept Note**
>
> This is the cheapest moment in the entire run to ask anything.
>
> Five questions here can save two modules of research aimed at
> the wrong country, the wrong buyer, or the wrong person.
