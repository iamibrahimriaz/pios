---
Title: Learning Objectives
Module: 08-product
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define what a learner should know and be able to do after the Product module.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 08-product/learn/01-Why-It-Matters.md
Outputs:
  - Specification competencies
Related Modules:
  - 07-strategy
  - 09-technology
Tags:
  - Product
  - Objectives
  - Learn
---

# Learning Objectives

---

# Overview

> After this module you should be able to write a requirement that two independent
> builders implement the same way, and to notice the one in your own document that
> traces to nothing.

---

# Knowledge Objectives

You should understand:

- What the **two-builder test** is and why it is the standard
- What makes an acceptance criterion observable rather than aspirational
- The five categories of edge case — empty, boundary, failure, concurrent, hostile
- What an **orphan requirement** is and why it always has a strong rationale
- The difference between deferring to the roadmap and dropping silently
- What **scope laundering** is, and how it arrives from module 07

---

# Thinking Objectives

The shift is from *what should it do* to *what would someone building this need to
decide, that I have not decided for them*.

Instead of asking:

> "Have I described the feature?"

ask:

- What happens when this fails?
- What is on screen before any data exists?
- Can this be undone, and does the user know before they act?
- Which problem does this requirement trace to?
- What would "not met" look like for this criterion?

The last question is the fastest available test of a criterion's usefulness.

---

# Skill Objectives

You should be able to:

- Write requirements with a stated trace to a ranked problem
- Convert an aspirational criterion into an observable one
- Enumerate edge cases across all five categories rather than the easy one
- Specify failure states as first-class requirements, not as error handling
- Record a cut with its reason and its destination
- Recognize your own orphan requirements by the strength of their rationale

---

# Analytical Objectives

You should develop the ability to:

- Read a specification and find the decision the author left in their own head
- Notice when a phase-two list contains everything
- Distinguish a requirement from a design preference
- Tell an edge case from an unlikely scenario — the difference is whether it is
  reachable, not whether it is common

---

# Judgment Objectives

**How much detail.** Enough that two builders converge, and no more. Detail beyond that
constrains implementation choices that belong to module 09 and to the builders, and it
ages badly.

**Where the MVP line falls in practice.** Module 07 drew it. This module discovers what
it actually means, and that discovery frequently reveals the cut was not real. Reporting
that back is correct; absorbing it by writing a larger MVP is scope laundering
completing itself.

---

# You Have Learned This When

| Signal | What it indicates |
| --- | --- |
| You write the failure state before the happy path | Edge cases are the specification to you |
| You can name the requirement that traces to nothing | The trace is live |
| Your criteria have imaginable failures | They are observable |
| A cut is recorded with a destination | Silence is no longer an option you take |
| You are suspicious of your most persuasive paragraph | You know what an orphan looks like |

---

# What This Module Does Not Teach You

It does not teach interface design — module 10 owns flows. It does not teach data
modeling or API design — module 09 does. It does not teach prioritization frameworks in
the abstract; the priority here is inherited from module 04's ranking.

---

> **Objectives Principle**
>
> The skill is noticing what you know that the document does not say.
>
> Every specification failure is an author who forgot they were the only one holding a
> particular decision.
