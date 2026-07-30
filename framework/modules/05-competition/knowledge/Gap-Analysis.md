---
Title: Gap Analysis
Module: 05-competition
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Find the opening and test whether it can be held.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 05-competition/knowledge/Feature-Comparison.md
Outputs:
  - gap_analysis
Related Modules:
  - 07-strategy
Tags:
  - Competition
  - Gap
  - Method
---

# Gap Analysis

---

# What It Is

Two questions, and the second is the one usually skipped.

**Finding the gap** comes straight out of Move 3: which ranked problem does nobody solve well, for the segment
chosen in `03-user`?

**Holding it** is the harder question:

> If this works, what stops the incumbent shipping it in six months?

| Answer | Defensibility |
| --- | --- |
| Nothing | Not defensible — a feature, not a company |
| It conflicts with their business model | Strong — they would cannibalize themselves |
| It requires data they do not have | Strong while it lasts |
| It requires a different sales motion | Moderate — they can build it, but not sell it |
| Their existing customers would object | Moderate |
| We would simply be faster | Weak, but sometimes sufficient |

> **"Not defensible" is a legitimate finding and must be stated.**
>
> Many good businesses start without a moat. But it must be a known condition carried into `07-strategy`, not
> something discovered after launch.

---

# When It Applies

In Move 5 (Locate), after coverage and pricing. It is the input `07-strategy` weighs most heavily when drawing the
MVP line.

---

# How to Apply It Here

**Name the specific incumbent, and reason about them.** Defensibility is not a general property; it is a claim about
what a named company can and cannot do given its customers, revenue and architecture.

**Look for the conflict rather than the capability.** Almost anything can be built. The durable gaps are the ones a
competitor is structurally unwilling to close — because it would undercut their pricing, annoy their largest
accounts, or require a sales motion they do not have.

**Cross-check against `02-market`'s gap reasoning.** Module 02 asked why the gap persists at market level;
this asks what stops it closing at company level. If the two disagree, one of them is wrong.

**Say how long a data or timing advantage lasts.** "Strong while it lasts" needs a duration attached, even a rough
one. A twelve-month lead and a five-year one support different strategies.

**State the finding plainly when there is no moat.** Speed, focus and being willing to serve a segment nobody wants
are real advantages. They are also temporary, and `07-strategy` and `11-growth` must plan accordingly.

---

# Where It Misleads

**Finding the gap is satisfying and testing it is not**, so the second question gets omitted. A gap without a
defensibility answer is the module's most expensive failure: it produces a product an incumbent copies in a quarter.

**Technology is claimed as a moat when it rarely is.** A model, a stack, or an architecture is available to
everyone. What is not available is proprietary data, a distribution relationship, or a commercial conflict —
`Technology-Comparison.md` makes the same point from the other side.

**A gap is assumed to be an oversight.** Incumbents have usually considered it. The reason they declined is the
finding, and it may be that the segment is unprofitable to serve — which is `06-business`'s problem next.

**Defensibility is confused with difficulty.** Something hard to build is not defended; it is merely delayed, and a
funded competitor buys the delay away.

**The gap gets widened to justify the product.** If the opening only exists once the coverage table is scored
charitably, it does not exist. The table is the evidence, and it was written before this move for that reason.

---

# Related

| | |
| --- | --- |
| `Feature-Comparison.md` | Where the gap is found |
| `Weaknesses.md` | Which competitor gaps are structural |
| `Threats.md` | How they respond if it works |
| `07-strategy` | Where a moatless gap becomes a stated risk |

---

> **Concept Note**
>
> Ask what stops them shipping it in six months, and write the answer
> down even when the answer is "nothing".
>
> A gap nobody defended is a feature, and features get copied.
