---
Title: Interviews
Module: 04-problem
Section: knowledge/validation
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Establish what interviews can prove, and how the questions destroy the evidence.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 04-problem/knowledge/Validation.md
Outputs:
  - Interview method within validation_plan
Related Modules:
  - 03-user
Tags:
  - Problem
  - Interviews
  - Method
---

# Interviews

---

# What It Is

Structured conversations with people in the segment, used to establish what happens today.

Their reach is narrow and real:

| Interviews can establish | Interviews cannot establish |
| --- | --- |
| That a problem exists for this person | How common it is |
| What they do today, step by step | What they would do with a new product |
| What it costs them, in their terms | What they would pay |
| That a workaround exists, and what it is | That they will switch |

The distinction is between **history and prediction.** Interviews are excellent at the past and worthless at
the future, and almost every misuse comes from asking them to forecast.

---

# When It Applies

The default method in Stage 6 for existence, workflow and cost claims. `03-user`'s Move 4 depends on them
entirely.

---

# How to Apply It Here

**Ask about the last time it happened.** "Walk me through the last consultation where you ran over" produces
recallable specifics. "How do you usually handle notes?" produces a summary of a summary.

**Ask what they did, then what it cost, then what they tried.** Three questions, in that order, and each about
a specific past occurrence. That sequence produces everything Stage 3 needs to score.

**Never describe the product before the questions are done.** Once a solution is visible, severity inflates,
enthusiasm appears, and the interview becomes a demo with polite feedback. This single rule accounts for most
of the difference between useful and useless interviews.

**Record the number and who they were.** Five solo GPs is a finding with a scope. "Users we spoke to" is not,
and `Evidence.md` cannot tag it.

**Quote them verbatim, or not at all.** The prohibition in `03-user/knowledge/Personas.md` applies with full
force: a paraphrase that becomes a quotation is fabricated primary evidence.

---

# Where It Misleads

**The interviewer's questions determine the answers, and the interviewer is usually invested.** Leading
questions do not feel leading from the inside — "Would it be useful if you didn't have to re-type that?" reads
as neutral and has one available answer.

**Agreement across interviews is treated as convergent evidence.** If every participant was asked the same
leading question, five agreements are one artifact of the question. Convergence only counts when the question
was open.

**People are unreliable about frequency, duration and their own consistency.** Recollection compresses and
flatters. Reported figures should be tagged as reported, and where a figure is load-bearing it needs data
rather than memory.

**Enthusiasm is the least predictive signal available and the most pleasant to collect.** "I would absolutely
use that" costs nothing to say. `Prototype.md` and `MVP.md` exist because only a cost makes a signal credible.

**Recruitment self-selects.** People who agree to talk about a problem are people for whom it is salient. That
biases incidence upward, which is one more reason interviews cannot answer "how common".

---

# Related

| | |
| --- | --- |
| `Surveys.md` | For incidence, where interviews fail |
| `Prototype.md` | For behavior under a real choice |
| `Success-Criteria.md` | Defining the invalidating result first |
| `03-user` | Where interview output becomes the workflow |

---

> **Concept Note**
>
> Ask about the last time. Never about the next time.
>
> And say nothing about the product until every question is
> answered — after that, you are collecting politeness.
