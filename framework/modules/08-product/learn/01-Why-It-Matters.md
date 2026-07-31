---
Title: Why It Matters
Module: 08-product
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Explain why specification is a distinct skill and why the two-builder test is the standard.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 08-product/core/00-Purpose.md
Outputs:
  - Understanding of why the product stage exists
Related Modules:
  - 07-strategy
  - 09-technology
  - 10-execution
Tags:
  - Product
  - Specification
  - Learn
---

# Why It Matters

---

# Overview

Everyone believes they can write a specification, because a specification looks like a
description and everyone can describe things. The difference shows up only when someone
else builds from it.

---

# The Two-Builder Test

> Give the specification to two competent builders who have never spoken. If they
> produce materially different things, it is underspecified.

This is a demanding standard and it is the right one, because it tests the only property
that matters: whether the document carries the decision, or whether the decision is
still in the author's head.

Most specifications fail it in the same places:

| Where they diverge | Because the spec said |
| --- | --- |
| What happens on failure | Nothing about failure |
| What the empty state shows | Nothing about empty states |
| Whether an action is reversible | Nothing about reversal |
| What "fast" means | "The system should be responsive" |
| Which fields are required | "Users can enter their details" |

None of these are exotic. They are the ordinary content of a working product, and they
are missing from most documents because the author knows the answers and did not notice
that the document does not contain them.

---

# Why the Trace Terminates Here

The framework's requirement trace runs:

```
03-user   job to be done
   ↓
04-problem   problem, ranked with evidence
   ↓
07-strategy  approach chosen against the ranking
   ↓
08-product   every requirement traces to a ranked problem
```

This module is where the trace is checked. The check catches a specific and very common
thing: a requirement that entered because it seemed obviously necessary, and which
addresses no ranked problem at all.

Those requirements are not usually bad ideas. They are unfunded ones — they consume
build effort that the ranking did not justify, and in aggregate they are how an MVP
becomes a product.

**The orphan always has the best rationale in the document.** It has to: it cannot point
at a problem, so it argues instead. A persuasive paragraph explaining why something is
essential is a signal worth checking, not a reason to stop checking.

---

# Why Acceptance Criteria Must Be Observable

An acceptance criterion is a statement about which someone can be wrong.

```
Aspirational:  "The interface is intuitive and easy to use"
Observable:    "A user who has never seen this screen completes the
                task without opening help, in under n minutes,
                in n of 5 attempts"
```

The first cannot be tested, so it will be declared met. The second can fail, which is
what makes it worth writing.

The framework requires criteria to be testable rather than aspirational, and the test is
simple: can you imagine the result that would mean "not met"? If not, the criterion is
a sentiment.

---

# Why Edge Cases Are the Specification

Products are mostly not the happy path. The happy path is the part everyone agrees on
and can visualize; it takes a paragraph. The rest of the product is:

- What happens when the input is empty, enormous, or malformed
- What happens when the network fails halfway
- What happens when two people act at once
- What happens the very first time, before there is any data
- What happens when the user does the thing you told them not to

A specification that covers only the happy path is roughly a fifth of a specification,
and the missing four fifths get decided by whoever is building at the time — differently
each time, under time pressure, without the context that would inform the decision.

---

# Why "Dropped Silently" Is Named in the Gate

The gate requires anything out of MVP scope to move to the roadmap rather than being
dropped silently. The word *silently* is doing the work.

Cutting is fine. Cutting without recording produces a document where the absence is
indistinguishable from an oversight, and three months later nobody can tell whether a
missing capability was rejected, deferred, or forgotten. Module 14 has the same
discipline for a different reason: an omission that is not recorded as a decision gets
re-proposed forever.

---

# What Skipping This Stage Costs

| Skipped | Surfaces as |
| --- | --- |
| The trace | An MVP containing features nobody's evidence justified |
| Observable criteria | "Done" negotiated during build rather than decided before |
| Edge cases | The four fifths of the product decided ad hoc |
| Recorded cuts | Scope that grows back, and nobody remembers why |

---

# What This Module Does Not Do

It does not design the interface — module 10 does the flows. It does not choose the
technology or the data model — module 09 does. It does not decide what to build; module
07 already chose, and this module writes it down.

That last distinction is worth holding. A specification stage that starts making
strategic choices is a strategy stage happening at the wrong time, with none of module
07's requirements applied to it.

---

> **Why It Matters Principle**
>
> The measure of a specification is not how complete it looks.
>
> It is whether two people who have never spoken build the same thing from it — and
> almost every document that feels finished still fails that.
