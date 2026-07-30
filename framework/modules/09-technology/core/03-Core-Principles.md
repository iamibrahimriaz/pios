---
Title: Core Principles
Module: 09-technology
Section: core
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the principles that govern judgment when designing the technical shape.
Audience:
  - AI Agents
  - Engineers
  - Founders
Prerequisites:
  - constitution/core/03-Core-Principles.md
Outputs:
  - Consistent technical judgment
Related Modules:
  - 10-execution
Tags:
  - Technology
  - Principles
---

# Core Principles

---

# Principle Statement

> Choose the technology last.
>
> Almost every failure in this module is a decision made before
> anyone knew what had to be built.

---

# Principle 1 — Derive, Do Not Invent

Entities and operations come from the requirement text, not from a mental image of the product.

A model built from the picture and reconciled with the requirements afterwards always
reconciles, which is why the reconciliation proves nothing.

---

# Principle 2 — Both Directions, Again

No entity without a requirement. No requirement without data.

An orphan entity is speculative modeling. An unmodeled requirement is either a hole here or a
vagueness in module 08 — and it must be named as one of the two, never filled in silently.

---

# Principle 3 — The Schema Test Is the Standard

The data model is finished when someone could generate a schema from it without asking a
single question.

Not "clear", not "thorough". Every column typed, every nullability stated, every cardinality
and on-delete behavior named. Anything absent is a decision handed to whoever builds it.

---

# Principle 4 — A Constraint Is a Requirement That Cannot Be Forgotten

A business rule in prose is enforced by whoever remembers it. The same rule as a `UNIQUE`,
`CHECK` or `FOREIGN KEY` is enforced by the database.

Where a requirement can be expressed as a constraint, express it as one. That is the most
durable place a product rule can live.

---

# Principle 5 — Forbidden Transitions Matter More Than Legal Ones

Every state machine's legal path gets written. The forbidden transitions — and what happens
when one is attempted — are where defects accumulate.

Unstated, every state can reach every other state, and eventually one does.

---

# Principle 6 — Every Capability Reachable, Every Operation Purposeful

A MUST requirement with no operation surfaces mid-build, when the design is fixed and the
cheap moment has passed.

An operation with no requirement is code, tests, documentation and attack surface serving
nothing.

---

# Principle 7 — Edge Cases Become Failure Responses

Module 08 specified five categories per requirement. Each maps here to a status and a code.

An edge case specified and then not exposed is worse than one never specified: the thinking was
done, the design ignored it, and the product's failure behavior is whatever the framework does
by default.

---

# Principle 8 — Compliance Is a Mechanism, Not a Commitment

"The system will be compliant" is a hope with a citation.

Every obligation names a mechanism, an enforcement point, and a source. An obligation with no
mechanism is a **blocker** — not a risk — because it means the product cannot lawfully operate.

---

# Principle 9 — Authorization Must Be Located

"Role-based access control" with no enforcement point is the most common serious defect in
designs of this kind, precisely because it reads as an answer.

State whether it is role-level or record-level, and where in the system it is enforced.

---

# Principle 10 — Technology Last, and With Its Trade-off

Shape follows load and team. Technology follows shape.

Every choice states what was rejected, what the choice is **worse** at, and what changing it
would cost. A trade-off that is a benefit with a hedge is not a trade-off.

---

# Principle 11 — Size to the Business, Not to Ambition

Capacity figures derive from the business model's own projections, with the arithmetic shown.

Designing for a scale nobody projects is not prudence. It is a cost the business did not agree
to and a delay the roadmap did not allow.

---

# Principle 12 — Cost Is a Design Constraint

The business model set a cost-to-serve ceiling. A design that exceeds it has invalidated the
business model.

This module is the first that can see it, and the resolution is a regress — the price, the
scope, or the design — not an absorbed inconsistency.

---

# Principle 13 — Say What You Are Not Building For

State the scale, the capability and the environment the design deliberately excludes.

Without it, every limit reads as an oversight to the first person who hits one, and gets
"fixed" by someone who does not know it was a decision.

---

# Principle 14 — Version Claims Are Looked Up, Never Recalled

Capabilities, limits, quotas, prices and deprecations are version-scoped and change.

They are also the statements most likely to be written confidently from memory, and the most
reliably wrong class of statement in technical writing.

---

# Principle 15 — Spend the Evidence on the One-Way Doors

Most technical decisions are cheap to reverse and are argued about at length. A few — data
model shape, tenancy model, primary datastore, regulatory posture — are not, and are often made
in an afternoon.

Identify which is which, then put the justification where reversal is expensive.

---

# Principle Hierarchy

```
Entities and operations derived from requirements
   ↓
Data modeled to the schema test
   ↓
Capabilities exposed, edge cases mapped to failures
   ↓
Obligations traced to mechanisms
   ↓
Shape chosen, then technology, with trade-offs
   ↓
Sized to the projections, costed against the ceiling
   ↓
One-way doors named and justified
```

Each level depends on the one above. A stack chosen first constrains the model; a model built
before deriving constrains the requirements.

---

# Common Violations

- Modeling from a picture of the product.
- Entities that serve no requirement.
- Requirements whose data lives nowhere.
- Columns without types; relationships without cardinality.
- On-delete behavior left to a default.
- State machines with no forbidden transitions.
- MUST requirements with no operation.
- Endpoints that exist because they seemed likely.
- Edge cases with no failure response.
- Compliance asserted rather than mechanized.
- Authorization described but not located.
- Retention periods invented.
- Technology asserted without alternatives.
- Distributed designs at pre-launch scale.
- Cost above the ceiling, absorbed silently.
- Version claims written from memory.
- Backups specified, restore never addressed.

---

# Self Assessment

- Did I derive, or did I picture and reconcile?
- Are both traceability directions clean?
- Would a builder have any questions about the schema?
- Which business rules did I leave in prose that could have been constraints?
- Did I write the forbidden transitions?
- Does every obligation name a mechanism and a place?
- Did I choose the stack before writing the reason?
- Do my capacity figures come from `06-business`?
- Is the cost inside the ceiling?
- Did I look up every version claim?
- Do the one-way doors carry the strongest arguments in the document?

---

> **Core Principle**
>
> A data model is the most expensive thing in a product to change
> and the cheapest thing to get right.
>
> This module exists mostly to make sure that happens in the right order.
