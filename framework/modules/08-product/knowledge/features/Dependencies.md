---
Title: Dependencies
Module: 08-product
Section: knowledge/features
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Distinguish real dependencies from assumed ones, and name external blockers with owners.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 08-product/knowledge/features/Feature-Prioritization.md
Outputs:
  - Dependency order within prioritization
Related Modules:
  - 09-technology
  - 10-execution
Tags:
  - Product
  - Dependencies
  - Concept
---

# Dependencies

---

# What It Is

What must exist before what — separated by kind, because only one kind is a fact about the requirements.

| Kind | Test | Treatment |
| --- | --- | --- |
| **Real** | The second requirement cannot function without the first | Sequence it |
| **Assumed** | It would be more convenient in this order | Not a dependency; note the preference and move on |
| **External** | Something outside this product must arrive — an API, an agreement, data, a decision | Blocked work, with a named owner |
| **Data** | One requirement produces what another consumes | Real, and it usually reveals the entity `09-technology` will model |

The distinction matters because a claimed dependency serializes work. Assumed dependencies presented as real ones make
a plan longer than it needs to be, and nobody re-examines them once they are in a diagram.

---

# When It Applies

In Move 5 (Order), alongside scoring. `10-execution` inherits the order and turns it into sequence, parallelization and
blocked work.

---

# How to Apply It Here

**Apply the functional test to each claimed dependency.** Could the second thing work at all without the first? If yes,
it is a preference. That question removes most of them.

**Name an owner for every external dependency.** `13-operations`' rule holds throughout the framework: "the team" is not
an owner. An external blocker with no name attached is not being pursued by anyone.

**Record what is parallelizable.** It changes the shape of the plan more than any estimate, and it falls out of the
dependency list for free.

**Note data dependencies specifically.** Where one requirement produces what another needs, that is a shared entity, and
`09-technology` derives the data model from exactly these relationships.

**State the consequence if an external dependency does not arrive.** A fallback, a reduced scope, or a stop. An external
blocker with no contingency is a single point of failure in the plan.

---

# Where It Misleads

**Preferences get recorded as dependencies and never revisited.** Once drawn, a dependency graph is treated as
structural. The functional test is the only thing that keeps it honest, and it has to be applied deliberately.

**External dependencies are assumed to resolve.** An integration partner's timeline, a data agreement, a platform's
roadmap — none is under this product's control. `07-strategy`'s `risks/Technical.md` registers them; this names them
concretely.

**Technical dependencies are invented here.** What depends on what technically is `09-technology`'s derivation. This
module knows functional and data dependencies; asserting technical ones pre-empts a module with better information.

**Long dependency chains go unquestioned.** Each link should survive the functional test independently. A five-step chain
frequently contains two real links and three preferences.

**Dependencies are used to justify sequencing that suits the builder.** Ordering by what is pleasant to build next is a
preference wearing a graph.

---

# Related

| | |
| --- | --- |
| `Feature-Prioritization.md` | The scoring dependencies constrain |
| `08-product` `Milestones.md` | The first shippable slice |
| `09-technology` | Where the data model is derived |
| `10-execution` | Sequence, parallelization and blocked work |

---

> **Concept Note**
>
> Ask whether the second thing could work at all without the first.
>
> Most claimed dependencies fail that question, and every one that
> survives it makes the plan longer for a reason.
