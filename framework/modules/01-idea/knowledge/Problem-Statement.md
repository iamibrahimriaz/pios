---
Title: Problem Statement
Module: 01-idea
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define what a problem statement is, and how to write one a later module can test.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 01-idea/core/06-Framework.md
Outputs:
  - A testable problem statement for the idea brief
Related Modules:
  - 04-problem
Tags:
  - Idea
  - Problem
  - Concept
---

# Problem Statement

---

# What It Is

A single sentence naming **who** has a difficulty, **what** the difficulty is, and **what it
costs them**.

It is not a description of a solution, a market, or an opportunity. Those are three different
sentences, and a problem statement containing any of them has smuggled in an answer.

| Element | Example |
| --- | --- |
| Who | A single-handed GP in a rural practice |
| What | Writing up consultation notes after the patient has left |
| Cost | Forty minutes of unpaid time at the end of every clinic |

---

# When It Applies

In Pass 2 (Separate), where the raw idea is split into problem, solution and assumption. The
problem statement is the output of that split.

It is written **before** any research, which makes it a claim rather than a finding. Module 04
tests it; this module only has to state it precisely enough to be testable.

---

# How to Apply It Here

**Write the cost, not the inconvenience.** "It is annoying" cannot be tested. "It takes forty
minutes at the end of every clinic" can be — someone can be asked, and the answer can differ
from the claim.

**Name one who.** A statement covering "clinicians, practice managers and patients" is three
statements, and this module's job is to identify which one the idea is actually about. The
others go to `scope_boundaries`.

**Tag it.** A problem statement written before research is `[assumption: needs validation]`,
unless the operator supplied it from direct experience — then it is `[verified: operator]` with
the basis recorded.

**The solution test.** Read the statement and ask whether it implies a particular product:

| Solution embedded | Problem stated |
| --- | --- |
| "GPs need a dictation tool for notes" | "Notes are written after the patient leaves, costing forty minutes a clinic" |
| "There is no good software for X" | "«Person» cannot do «task» without «cost»" |

The second form leaves the solution space open, which is what modules 05 and 07 need in order
to compare options at all.

---

# Where It Misleads

**A well-written problem statement feels validated.** Precision and evidence are different
properties, and this module produces only the first. A sharp, specific, entirely imaginary
problem reads better than a vague real one — which is why the tag matters more than the wording.

**The stated cost is usually the *visible* cost.** Forty minutes of note-writing may matter less
to the person than the fear of having recorded something wrong. Module 03 finds that out; this
module should not guess at it.

**One statement rarely survives contact with users.** Expect module 04 to reorder, merge or
discard it. That is the process working, not a defect in the statement.

---

# Related

| | |
| --- | --- |
| `Hypothesis.md` | What the statement becomes once a solution is attached |
| `Assumptions.md` | Where its untested parts are recorded |
| `04-problem` | The module that tests, scores and ranks it |

---

> **Concept Note**
>
> A problem statement is the shortest thing in the run, and the thing
> most likely to be quietly rewritten later to match what got built.
>
> Record the date on it.
