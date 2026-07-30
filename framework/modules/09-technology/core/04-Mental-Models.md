---
Title: Mental Models
Module: 09-technology
Section: core
Category: Thinking Framework
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the lenses through which a technical design should be examined.
Audience:
  - AI Agents
  - Engineers
  - Founders
Prerequisites:
  - 09-technology/core/03-Core-Principles.md
Outputs:
  - Multi-perspective examination of the design
Related Modules:
  - 10-execution
Tags:
  - Technology
  - Mental Models
---

# Mental Models

---

# Model Statement

> A design always looks sufficient to the person who holds the whole
> system in their head.
>
> Nobody who builds from it will.

---

# 1. The Schema Test

**Reveals:** everything the design left implicit.

Read the data model as though you had to write the DDL and nobody was available to ask. Write
down every question. The list is the defect list.

**Hides:** it says nothing about whether the model is *right* — only whether it is complete. A
fully specified wrong model passes.

---

# 2. The Derivation Chain

**Reveals:** invented structure.

For each entity, column and operation, write the chain: problem → requirement → this. Anything
whose chain breaks either serves nothing or is covering a vague requirement.

**Hides:** a valid chain can still produce a poor model. Traceability is about legitimacy, not
quality.

---

# 3. The Coverage Grid

**Reveals:** gaps and speculation at once.

Requirements down one axis, operations across the other. Empty rows are unreachable
capabilities. Empty columns are surface area serving nothing.

**Hides:** a filled cell does not mean the operation actually satisfies the requirement. It
means one exists.

---

# 4. Obligation to Mechanism

**Reveals:** compliance written as intention.

For each regulatory obligation, insist on three things: the mechanism, the place it is
enforced, and the citation. Anything that resolves to "we will handle this" is unmet.

**Hides:** a mechanism can be named and still be insufficient. This lens catches absence, not
adequacy — adequacy needs someone qualified to assess it.

---

# 5. The Adversary's Path

**Reveals:** the threats that matter for this specific system.

One question, asked against this design: *what would it take for one user of this product to
see another user's data?* Then follow the path — identifier in a URL, a query without a scope,
a cache without a key, a log with a payload, a backup with wide access.

**Hides:** it centers one threat class. Availability, integrity and insider misuse need their
own passes.

---

# 6. The Forbidden Path

**Reveals:** state machine defects.

Draw the transitions nobody should be able to make, then ask what currently prevents each one.
"Nothing, but nobody would" is the answer that precedes the incident.

**Hides:** it only covers modeled states. Implicit state — held in a boolean pair, or in a
timestamp being null — escapes it entirely.

---

# 7. The Arithmetic

**Reveals:** architecture inflation.

Multiply out the actual load from the business model's own figures. Users, sessions per user,
requests per session, peak-to-average ratio.

The number is usually far smaller than the design assumes, and it converts an argument about
engineering taste into a calculation.

**Hides:** averages hide peaks, and some workloads are spiky by nature. State the peak
assumption and where it came from.

---

# 8. The Cost Per User

**Reveals:** whether the business model survives this design.

Total monthly cost divided by users at launch, set against the ceiling from `06-business`.

This is the most decisive lens in the module, because the answer is a number and the ceiling is
someone else's number. There is no way to be persuasive about it.

**Hides:** launch cost is not steady-state cost. Check both, and note which components scale
with users and which do not.

---

# 9. Reversibility Sorting

**Reveals:** where the evidence belongs.

Sort every decision into three buckets:

| Bucket | Standard of evidence |
| --- | --- |
| Cheap to change | Decide and move on |
| Requires a data migration | Justify properly |
| Requires a rewrite, or cannot be changed | The strongest argument in the document |

Attention is usually distributed by how interesting a decision is, which correlates poorly with
how expensive it is to undo.

**Hides:** reversibility is assessed optimistically. Ask what it would cost with real data and
real users, not in principle.

---

# 10. The Operator's Reality

**Reveals:** designs nobody can run.

Ask who operates this after launch, with what experience, at what hours. Then read the design
as that person during an incident at 2am.

**Hides:** it can bias toward the familiar. Sometimes the right answer is a technology the team
must learn — but that is then a cost to state, not an assumption to make.

---

# 11. The Boring Alternative

**Reveals:** novelty chosen without a reason.

For each choice, name the most common, least interesting technology that would have served.
Write why it was not chosen.

If no reason survives being written down, take the boring one.

**Hides:** the common choice is sometimes genuinely wrong for the constraints. The lens asks for
a reason, not for conformity.

---

# 12. The Absent Line

**Reveals:** limits that will be read as oversights.

Read the design as an engineer who joins in a year and hits a limit. Is it recorded as a
decision, or does it look like nobody thought about it?

**Hides:** nothing. It costs three sentences and prevents a category of unnecessary rework.

---

# Combining Models

| Situation | Model |
| --- | --- |
| Checking the model is buildable | The Schema Test |
| Checking nothing was invented | The Derivation Chain |
| Checking interface completeness | The Coverage Grid |
| Checking compliance is real | Obligation to Mechanism |
| Checking security | The Adversary's Path |
| Checking lifecycles | The Forbidden Path |
| Checking the design is not inflated | The Arithmetic |
| Checking the business survives it | The Cost Per User |
| Deciding where to spend rigor | Reversibility Sorting |
| Checking it can be run | The Operator's Reality |
| Checking choices honestly | The Boring Alternative |
| Preventing future rework | The Absent Line |

Apply the Derivation Chain and the Arithmetic early — they shape the design. Apply the Cost Per
User, the Boring Alternative and the Absent Line last, on the finished document.

---

# Self Assessment

- Is my list of schema questions empty?
- Does every element have an unbroken derivation chain?
- Are there empty rows or columns in the coverage grid?
- Does every obligation resolve to a mechanism and a place?
- Can I trace an adversary's path to another user's data?
- What prevents each forbidden transition?
- What does the arithmetic actually say about load?
- What is the cost per user, and what is the ceiling?
- Have I put the strongest arguments on the one-way doors?
- Could the person on call at 2am operate this?
- What boring alternative did I pass over, and why?
- What limit have I left looking like an accident?

---

> **Mental Model Principle**
>
> Two of these lenses produce numbers rather than opinions.
>
> Those are the two that settle arguments this module
> would otherwise lose to whoever is most fluent.
