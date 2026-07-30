---
Title: Core Principles
Module: 08-product
Section: core
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the principles that govern judgment when specifying a product.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - constitution/core/03-Core-Principles.md
Outputs:
  - Consistent specification judgment
Related Modules:
  - 09-technology
Tags:
  - Product
  - Principles
---

# Core Principles

---

# Principle Statement

> A specification is a promise to someone who cannot ask you anything.
>
> Every gap in it becomes their guess.

---

# Principle 1 — Nothing Enters Without a Parent

Every requirement names the ranked problem it serves. No parent, no requirement.

This is enforced by deletion rather than by argument, because an orphan can almost always be
justified — the justification is written after the fact, it sounds reasonable, and it is
precisely how unattached features enter products.

---

# Principle 2 — Traceability Runs Both Ways

Requirements must have parents, and problems above the line must have children.

The second direction is the one usually skipped, and it catches the more serious defect: a
problem the strategy committed to solving that the specification quietly does not address.

---

# Principle 3 — MUST Means the Release Does Not Ship

Not "important". Not "we really want this".

MUST is reserved for capabilities module 07 placed above the line. If the MUST list is
effectively the requirement list, nothing was prioritized — the labels were applied, not
used.

---

# Principle 4 — The Cut Is a Boundary, Not a Starting Point

An operator approved a specific scope. This module works inside it.

Specifying reveals adjacent capabilities that appear necessary, and each is individually
defensible. They go to the ledger. If one is genuinely load-bearing for the core job, that
is module 07's end-to-end test failing — a recorded regress, not a quiet addition.

---

# Principle 5 — Precision Is Not Evidence

A requirement can be exact and still rest on an assumption.

Writing "the system must alert the clinician within 30 seconds" does not establish that
clinicians need alerting. It establishes what the product will do if they do. The evidence
standing belongs to the problem, and it does not improve by being specified.

---

# Principle 6 — Write for Two Builders, Not for One Reader

The test of a behavior description is not whether it reads clearly. It is whether two
independent engineers would build the same thing from it.

"Is this clear?" cannot be answered by the author — they already know what they meant. "Where
would two readings diverge?" can be, and it produces the rewrite.

---

# Principle 7 — Behavior, Not Implementation

Describe what the user does and what the system does. Not the database, the framework, the
component or the screen.

A requirement that names a technology has taken a decision belonging to `09-technology` —
usually without the analysis that module would have done.

---

# Principle 8 — The Unhappy Paths Are the Product

Empty states, invalid input, failures, refusals, limits, conflicts. These outnumber the happy
path and consume most of the build.

A requirement specified only for success is roughly half specified, and the missing half is
where users lose work and trust.

---

# Principle 9 — Say What Can Be Lost

Of all the edge answers, the data-loss position is the one that matters most and is written
down least.

State it explicitly per requirement. If nothing can be lost, that sentence is the answer and
it is worth making.

---

# Principle 10 — A Criterion That Cannot Fail Is Not a Criterion

"Fast", "intuitive", "seamless", "robust" cannot be observed, so they cannot be failed.

Every criterion must name an observation that would fail it. If none exists, it is a hope in
checkbox form, and it will be marked complete without anything being verified.

---

# Principle 11 — Numbers Must Have Origins

Every limit, threshold, retention period, field and code is a cited standard, a derivation
from a finding, or a registered design decision.

A number chosen because a number was needed is worse than an open question: the builder
implements it, the tester tests it, and nobody learns it was invented until a user does.

---

# Principle 12 — Judgments Made Here Are Assumptions

Specification requires choices no research produced — defaults, step counts, reversibility,
ordering.

These are legitimate. Presenting them as derived is not. Label them, record the alternative,
and register the load-bearing ones as assumptions with a validation method.

---

# Principle 13 — Nothing Is Dropped Silently

Everything considered lands somewhere: a requirement, or a ledger row with a reason and a
revisit trigger.

Silence is how the same idea gets re-proposed every month with no memory of why it was
excluded — and how a genuinely good deferred capability is simply forgotten.

---

# Principle 14 — Inherit Confidence, Do Not Improve It

The problems arrive tagged. Requirements serving an assumed problem are marked, and the
document's confidence statement cannot exceed the confidence of the problems underneath it.

This module translates. It has no mechanism for making anything more certain, and it must not
appear to.

---

# Principle Hierarchy

```
Spine traced from problems and the job
   ↓
Requirements written, priority anchored to the cut
   ↓
Behavior specified to the two-builder standard
   ↓
Failure states worked
   ↓
Ordered, with a first shippable slice
   ↓
Criteria that can fail
   ↓
Everything else accounted for in the ledger
```

Each level depends on the one above. Requirements written before the spine get parents
assigned retrospectively; criteria written before behavior test the description rather than
the product.

---

# Common Violations

- Assigning a requirement's parent after writing it.
- Leaving a committed problem unserved with no deferral recorded.
- Labeling everything MUST.
- Growing the MUST list past the approved cut.
- Treating a precise requirement as an established need.
- Behavior that reads well and builds two ways.
- Naming a framework or database in a requirement.
- Specifying only the happy path.
- Leaving the data-loss position unstated.
- Aspirational acceptance criteria.
- Invented limits and retention periods.
- Design decisions presented as derived.
- Capabilities that appear nowhere in the final document.
- Writing with more certainty than module 04 established.

---

# Self Assessment

- Does every requirement name its parent, chosen before it was written?
- Is every problem above the line served or explicitly deferred?
- Is my MUST list the approved cut and nothing more?
- Would two builders build the same thing?
- Have I specified the failures?
- Can every criterion fail?
- Does every number have an origin?
- Is every judgment of mine labeled as one?
- Is anything I considered absent from the document?

---

> **Core Principle**
>
> The strategy could be re-decided. The research could be redone.
>
> This document gets built — including the parts nobody meant.
