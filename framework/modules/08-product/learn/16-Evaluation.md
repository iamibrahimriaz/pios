---
Title: Evaluation
Module: 08-product
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Give a learner a way to test whether their specification carries the decision.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 08-product/learn/10-Common-Mistakes.md
Outputs:
  - A self-assessment for specification
Related Modules:
  - 09-technology
  - 10-execution
Tags:
  - Product
  - Evaluation
  - Learn
---

# Evaluation

---

# Overview

Specification is the most objectively assessable skill in the framework, because you can
hand the document to someone and see what they build.

---

# Exercise 1 — Run the Two-Builder Test

Write a one-feature specification. Give it to two people separately and ask each to
sketch what they would build, without discussing it.

**Passing looks like.** The sketches agree on behavior, including what happens on
failure.

**Failing looks like.** They diverge on something you considered obvious. That divergence
is the most valuable feedback available in this module, and it is always about something
you knew and did not write.

---

# Exercise 2 — Audit for Orphans

Take any requirement list. For each item, name the ranked problem it serves.

**Passing looks like.** You find at least one orphan. In a first pass it is usually two
or three.

**Failing looks like.** Everything traces neatly. Either the list is unusually
disciplined, or the traces were assigned after the fact — which is the same
reverse-engineering that module 04 warns about, applied one stage later.

---

# Exercise 3 — Make a Criterion Fail

Take five acceptance criteria and, for each, write the observation that would mean "not
met."

**Passing looks like.** All five produce a concrete failing observation.

**Failing looks like.** One or two produce "it doesn't feel right." Those are sentiments,
and they will be marked met.

---

# Exercise 4 — Five Edges

Pick one requirement. Write the empty case, the boundary case, the failure case, the
concurrent case and the hostile case.

**Passing looks like.** All five are reachable states with defined behavior.

**Failing looks like.** You skip concurrent or hostile. Those two are the most commonly
omitted and the most commonly expensive — one produces data corruption, the other
produces a security incident.

---

# Exercise 5 — Mark Reversibility

Take a specification and annotate every state-changing action as reversible or not.

**Passing looks like.** At least one irreversible action was not previously flagged
anywhere, and flagging it changes the design.

**Failing looks like.** Everything is reversible. Very few products are.

---

# Exercise 6 — Find the Persuasive Paragraph

Read your own specification and find the passage where you argued hardest.

**Passing looks like.** You check its trace, and understand why it needed the argument.

**Failing looks like.** You conclude it argued hard because it matters most. Sometimes
true; more often it argued because it had nothing to point at.

---

# Rubric

| Level | Description |
| --- | --- |
| **Not yet** | Describes features; criteria are aspirational; happy path only |
| **Working** | Observable criteria; edge cases for the obvious inputs |
| **Competent** | Traces checked; five edge categories; reversibility stated; cuts recorded with destinations |
| **Fluent** | Passes the two-builder test on the first attempt, and reports back when a cut turns out not to have been real |

---

# A Note on What Cannot Be Assessed Here

Whether the product is worth building. A specification can be flawless and describe
something nobody needs — the trace check only verifies that requirements match the
ranking, not that the ranking was right.

This module's quality and the product's merit are independent, and a very good
specification is exactly the artifact most likely to be mistaken for evidence that the
underlying decision was sound.

---

> **Evaluation Principle**
>
> Hand it to someone and watch what they build.
>
> Every other assessment in this module is an approximation of that one, and none of
> them are as informative.
