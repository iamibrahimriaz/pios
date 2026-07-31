---
Title: Evaluation
Module: 14-ai-systems
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Give a learner a way to test whether their AI proposals would survive an honest comparison.
Audience:
  - Product Managers
  - Founders
  - Engineers
Prerequisites:
  - 14-ai-systems/learn/10-Common-Mistakes.md
Outputs:
  - A self-assessment for AI capability decisions
Related Modules:
  - 08-product
  - 09-technology
Tags:
  - AI
  - Evaluation
  - Learn
---

# Evaluation

---

# Overview

The test underneath all of these: **can you lose?** A comparison you cannot lose is not a
comparison.

---

# Exercise 1 — Argue the Alternative

Take an AI feature you like. Write the case for the simplest non-AI alternative in one
sentence, as its advocate would.

**Passing looks like.** The sentence is genuinely persuasive and mentions cost, risk and
determinism.

**Failing looks like.** It reads as a description of the problem. That is a straw man,
and it is what most comparison sections contain.

---

# Exercise 2 — Ask the Detectability Question

For any AI feature you use, work out whether you would know if it were wrong — and what it
would take to find out.

**Passing looks like.** You identify at least one feature whose errors you could only
catch by redoing the task.

**Failing looks like.** You assume you would notice. Most people assume this about
summarization and are wrong.

---

# Exercise 3 — Classify the Data

For a capability you would like to build, answer three separate questions: does the data
exist today, is it good enough, and do you have the right to use it this way?

**Passing looks like.** Three separate answers, and at least one is uncomfortable.

**Failing looks like.** One answer covering all three. Availability, quality and rights
fail independently and the third is legal.

---

# Exercise 4 — Stratify a Golden Set

Design a hundred-case evaluation set for a capability. List the categories and their
proportions.

**Passing looks like.** The hard cases are deliberately over-represented — noisy inputs,
edge presentations, atypical users.

**Failing looks like.** A representative sample of typical cases. That measures the
average and hides the failures that matter.

---

# Exercise 5 — Write a Bar That Can Fail

State a threshold, a subset threshold, and what happens if either is missed.

**Passing looks like.** The consequence is specific and unwelcome — the capability does
not ship, and the existing approach continues.

**Failing looks like.** "We would iterate." Then the bar cannot fail and it will be met.

---

# Exercise 6 — Make One Failure Mode Specific

Take "the model may produce inaccurate output" and rewrite it as a specific failure with a
detection column and a guardrail.

**Passing looks like.** The detection column contains an honest "no" at least once, and
the guardrail follows from it.

**Failing looks like.** Every failure is detectable. That is unusual, and it usually means
the detection was assumed rather than examined.

---

# Exercise 7 — Record a Rejection Properly

Take a capability you have decided against. Write it as a rejection: what was dropped,
what simpler thing was adopted instead, and why.

**Passing looks like.** A record that would stop the same idea being re-proposed next
quarter as an obvious omission.

**Failing looks like.** A deferral. If it is not coming back, say so.

---

# Rubric

| Level | Description |
| --- | --- |
| **Not yet** | Proposes capabilities; alternatives named but not argued; accuracy sets autonomy |
| **Working** | Real alternatives; data availability checked; a bar set |
| **Competent** | Advocate check applied; detectability drives the ceiling; data rights treated as legal |
| **Fluent** | Proposes generously and ships little, records rejections so they stay rejected, and can name the capability whose alternative won |

---

# A Note on What Cannot Be Assessed Here

Whether the capability will actually work. That requires the golden set, the model, and a
domain expert judging outputs — none of which exist at planning time.

What is assessable is whether the decision to build it was made against something real.
A capability that beat an argued alternative, whose data is confirmed, whose bar is set
and whose failure modes are specific may still underperform. It will just fail in a way
you planned for, at a point where you said you would stop.

---

> **Evaluation Principle**
>
> A capability that has not survived a real alternative has not been evaluated, however
> carefully it was designed.
>
> The measure of this module is how many proposals it eliminated.
