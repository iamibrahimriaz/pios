---
Title: Future Improvements
Module: 08-product
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: State what the Product module does not yet do well.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 08-product/learn/19-Related-Modules.md
Outputs:
  - A candid list of the module's limitations
Related Modules:
  - 09-technology
  - 10-execution
Tags:
  - Product
  - Improvements
  - Learn
---

# Future Improvements

---

# Known Limitations

**The trace is checked but not typed.** A requirement must trace to a ranked problem.
Nothing distinguishes a requirement that fully addresses a problem from one that touches
it tangentially, so a weak trace and a strong one look identical.

**The two-builder test is a standard, not a mechanism.** It is the best test in the
module and nothing in the gate performs it. In practice it is run only when a builder
comes back with a question, which is after the cost has been incurred.

**Edge case categories are guidance, not structure.** Five categories are named. The
schema has one list, so a specification covering only empty-state cases satisfies
"edge cases specified."

**Reversibility has no field.** It changes the design of every state-changing action and
is carried in prose when it is carried at all.

**Acceptance criteria testability is judged by the author.** "Testable, not aspirational"
is exactly the kind of criterion that the person who wrote an aspirational one will
believe they have met.

**Nothing detects scope laundering arriving from module 07.** If the MVP was never really
cut, this module specifies it faithfully and the gate passes. The framework relies on the
specifier noticing and reporting back.

**Non-functional requirements had no home. Partly addressed, and the remainder is
narrower.** Performance, availability, accessibility and data-retention expectations all
shape requirements, and they used to land in module 09 as architecture concerns — too late
for the ones that change what gets specified. Criterion 7 and the `interface-requirements`
artifact now give the interface-facing subset a home at this module: interaction states,
layout across the supported range, an accessibility conformance target, perceived-performance
budgets, supported clients, and crawlable surfaces.

**What is still missing.** Availability, durability and data-retention expectations have no
home here and still arrive at module 09. They are less damaging there than the interface ones
were — an availability target does not change which components exist — but they do change what
a requirement can promise, and a requirement written without knowing them can promise something
the architecture will not support.

**Criterion 7 cannot detect a lazy pass.** A run may write "not applicable" against a surface
that plainly has an interface, and the criterion has no way to contradict it. What it prevents
is the silent omission — the surface named at module 01 and never consulted again — which was
the actual failure. **A false "not applicable" is at least a sentence somebody wrote and can be
challenged.**

---

# Candidate Improvements

| Candidate | What it would fix | Cost |
| --- | --- | --- |
| A trace strength — full, partial, exception | Weak traces stop looking like strong ones | Small |
| A `reversible` boolean on state-changing requirements | The most consequential omitted property gets a slot | Small, and high value |
| Structured edge cases across five categories | Partial coverage stops passing | Small |
| A non-functional requirements section | Performance and accessibility stop arriving late | Moderate |
| An automated criterion check for adjectives | Catches the most common aspirational form cheaply | Small, crude, and probably worth it |
| A scope-reality check against module 07's cut | Laundering becomes visible at the point it becomes concrete | Moderate |

The reversibility row is the one to do first. It is a single field, it changes the
interface design of every action it applies to, and its absence is what produced the
worked example's most instructive edge-case failure.

---

# What Should Not Change

**The trace requirement stays absolute.** Every proposal to relax it is a proposal to
admit orphans, and orphans are how an MVP becomes a product without anyone deciding to
let it.

**"Not dropped silently" stays in the gate.** It is the least glamorous criterion here
and it prevents the specific failure where nobody can tell a decision from an oversight.

**Specification stays separate from design.** A module that specifies layouts constrains
module 10 for no stated reason and ages badly.

**The module stays downstream of the decision.** A specification stage that starts
choosing is a strategy stage with none of module 07's requirements applied to it.

---

> **Improvements Principle**
>
> The module's best test — hand it to two builders — is the one thing it cannot
> automate.
>
> Everything else here is a field. That one is a practice, and it has to be adopted
> rather than enforced.
