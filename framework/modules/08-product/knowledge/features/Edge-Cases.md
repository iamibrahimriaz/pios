---
Title: Edge Cases
Module: 08-product
Section: knowledge/features
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Work all five categories for every MUST requirement, and state what data can be lost.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 08-product/knowledge/Requirements.md
Outputs:
  - edge_cases
Related Modules:
  - 09-technology
  - 13-operations
Tags:
  - Product
  - Edge Cases
  - Method
---

# Edge Cases

---

# What It Is

The unhappy paths — and there are more of them than happy paths.

> A requirement with only happy-path behavior is roughly half specified, and the missing half is where products fail in
> front of real users.

Five categories, worked for **every MUST requirement**:

| Category | The question |
| --- | --- |
| **Empty** | First use. No data yet. What does the user see, and what do they do next? |
| **Invalid** | Wrong, incomplete or impossible input. What are they told, and what is preserved? |
| **Failure** | The operation cannot complete. Is work lost? Can they retry? |
| **Permission** | The user is not allowed. What do they see — and does it reveal something it should not? |
| **Limit or conflict** | Too many, too large, two at once, offline, interrupted |

"Not applicable — «reason»" is an acceptable answer. **A blank is not:** a blank is indistinguishable from not having
considered it.

> **The data-loss position.** State plainly what can be lost and when. This is the single most consequential edge-state
> answer in most products, and it is almost never written down until it happens.

---

# When It Applies

In Move 4 (Break), after behavior and before ordering — because the edge states are most of the effort being estimated.

---

# How to Apply It Here

**Work the categories as a checklist, not from memory.** Recall produces the two or three that come to mind; the
checklist produces the ones that do not, which are the ones that ship broken.

**Answer the empty state first.** Every user's first experience is the empty state, and it is the most commonly
unspecified screen in software.

**State what is preserved on invalid input.** Losing a user's work to a validation error is a trust failure, and it is
entirely a specification decision.

**Write the permission answer with the disclosure question attached.** "Not found" and "not permitted" reveal different
things. Which one is shown is a security decision `09-technology` will enforce and this module must state.

**Include the environment conditions from `03-user`.** Interrupted, offline, one hand, someone waiting. Those are real
limits, and they belong in the fifth category rather than being treated as unlikely.

---

# Where It Misleads

**Edge cases are treated as polish and scheduled after launch.** They are the specification's other half, and the
`13-operations` runbook is written from them. Deferred, they become incidents.

**Only the imaginable categories get worked.** Failure and limit are the two most often skipped, and they are where data
loss lives.

**"The system shows an error" is recorded as an answer.** What error, containing what, and what happens to the user's
work? Two engineers will build different things from that sentence, which is the two-builder test failing.

**Data loss is left implicit.** Nobody writes it down because writing it down makes it real. It becomes real anyway,
usually in front of a customer, and then it is `13-operations`' S1 incident.

**Edge cases get written for requirements below the line.** The instruction is every MUST requirement. Below-line
effort here is effort spent on things that will not ship.

---

# Related

| | |
| --- | --- |
| `Acceptance-Criteria.md` | Where edge behavior becomes provable |
| `08-product` `Requirements.md` | The MUST list this is worked against |
| `03-user` | The real conditions of use |
| `09-technology`, `13-operations` | Enforcement, and the runbook |

---

> **Concept Note**
>
> Five categories, every MUST, and "not applicable — reason" instead
> of a blank.
>
> Then state what can be lost and when. It is the answer nobody writes
> until the day it is needed.
