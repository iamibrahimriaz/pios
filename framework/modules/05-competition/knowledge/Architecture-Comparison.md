---
Title: Architecture Comparison
Module: 05-competition
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: State what can honestly be inferred about a competitor's architecture, and where inference must stop.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 05-competition/knowledge/Technology-Comparison.md
Outputs:
  - Architectural constraints within competitor_matrix
Related Modules:
  - 09-technology
Tags:
  - Competition
  - Architecture
  - Concept
---

# Architecture Comparison

---

# What It Is

An assessment of what a competitor's architecture **prevents them from doing** — and an explicit boundary on how much
of that can be known from outside.

The reason to look at all is that architecture produces durable constraints, and durable constraints are what
`Gap-Analysis.md` needs.

| Observable from outside | Not observable |
| --- | --- |
| Whether the product is multi-tenant or deployed per customer | How their data is modeled |
| Whether data can be exported, and in what form | Their service boundaries |
| Whether it works offline | Their scaling approach |
| Whether the API supports the operation the workflow needs | Their internal quality |
| What their status page and incident history show | Where their technical debt sits |
| What their documentation says the system cannot do | Anything about their codebase |

The right-hand column is where competitive analysis turns into fiction. Nothing there can be tagged, so nothing there
belongs in the artifact.

---

# When It Applies

In Move 5 (Locate), only where an architectural constraint is the answer to the defensibility question. Otherwise this
dimension is skipped.

---

# How to Apply It Here

**Reason from documented behavior, not from imagined internals.** "Their API has no endpoint for this, and their
documentation says exports run nightly" is evidence about a limit. "Their data model was not designed for this" is a
guess unless they have said so.

**Use their own statements where they exist.** Public engineering posts, documented limits, deprecation notices,
status-page history and release notes are citable. Competitors describe their own constraints more often than
expected.

**Attach a duration to any architectural weakness.** Rebuilding something central takes time and money, not
permanence. `Weaknesses.md` requires the same discipline — a three-year lead is a strategy, forever is not.

**Note per-customer deployment models specifically.** A competitor deploying separately for each customer usually has
slow release cycles and high support costs, which constrains how fast they can respond and which segments they can
serve. That is both visible and consequential.

**Tag everything `[inferred]` with the basis named.** This is the dimension where the framework's evidence rules do
the most work, because plausible architectural narratives are easy to construct and impossible to check.

---

# Where It Misleads

**Architectural speculation is the most fabrication-prone content in this module.** A confident paragraph about a
competitor's data model reads as research, cannot be verified, and will be quoted. If the basis cannot be named, the
line should not exist.

**"Legacy architecture" is used as an explanation for anything.** It is frequently true and rarely specific. Unless it
names the constraint and the consequence, it explains nothing and predicts nothing.

**Slow release cadence is attributed to architecture.** It may be process, certification requirements, contractual
change control, or deliberate stability that customers demand. Any of those is a stronger finding than a guess about
code.

**Their architecture is compared to a plan rather than a product.** This product does not exist yet, and comparing a
running system to an intended design will flatter the design every time.

**It becomes a design session for `09-technology`.** Module 09 derives architecture from requirements and picks
technology fifth of six. Importing a competitor's shape here inverts that order.

---

# Related

| | |
| --- | --- |
| `Technology-Comparison.md` | What is worth recording at all |
| `Weaknesses.md` | Structural versus temporary gaps |
| `Gap-Analysis.md` | Where a real constraint becomes defensibility |
| `09-technology` | Where this product's architecture is derived |

---

> **Concept Note**
>
> You can see what their product cannot do. You cannot see why.
>
> Reason from documented limits, and leave the codebase narrative
> unwritten — it is the one finding here nobody can check.
