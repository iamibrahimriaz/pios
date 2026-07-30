---
Title: Modules
Module: 08-product
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Group requirements by the job they serve, without pre-empting technical structure.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 08-product/knowledge/Requirements.md
Outputs:
  - Grouping within feature_spec
Related Modules:
  - 09-technology
  - 10-execution
Tags:
  - Product
  - Structure
  - Concept
---

# Modules

---

# What It Is

The grouping of requirements into named areas — done for **navigation and ownership**, not as a design.

The right grouping principle here is the user's job:

| Group by | Result |
| --- | --- |
| **The job or journey it serves** | Groups that map to `03-user`'s workflow and can be sliced vertically by `10-execution` |
| The screen it appears on | Pre-empts design, and screens change |
| The technical component | Pre-empts `09-technology`, which derives structure from requirements |
| The team that will build it | Groups that dissolve when the team changes |

Grouping by job keeps the trace intact — each group belongs to a problem, and `10-execution` can cut a complete journey
out of it.

---

# When It Applies

Emerging during Move 1 (Trace) as the spine takes shape, and used in Move 5 (Order) to sequence coherent slices.

---

# How to Apply It Here

**Name groups after what the user is doing**, in their language. "Capturing the consultation" rather than "Input
subsystem". `03-user`'s job statements are the source.

**Keep groups small enough to be sliced.** A group containing the whole product cannot be sequenced. Three to six
requirements per group is a workable size for a small product.

**Show each group's parent problem.** A group with no parent problem is a collection of orphans that acquired a heading —
which is harder to spot than a single orphan requirement.

**Let cross-cutting obligations sit in their own group.** Access control, audit logging and export derive from
`09-technology`'s obligations rather than from a job, and grouping them separately prevents them being scattered and
half-implemented.

**Expect `09-technology` to structure differently.** A product area and a service boundary are different things, and
module 09 derives its structure from the data and the operations, not from these headings.

---

# Where It Misleads

**Grouping becomes architecture by implication.** Named product areas start to look like components, and
`09-technology` inherits a structure it should have derived. That is architecture inflation arriving through a
document's table of contents.

**Groups get drawn to look balanced.** Real products are lopsided: one area carries the value and three are supporting.
Even grouping hides where the work and the risk actually are.

**A group hides an unserved problem.** A heading implies coverage. The check is the spine — each ranked problem above the
line mapped to at least one requirement — not the presence of a plausible group name.

**Cross-cutting concerns are duplicated per group.** Writing access control into five groups produces five partial
implementations and no single enforcement point, which is precisely what `09-technology` requires to be *located*.

**Grouping substitutes for prioritization.** Areas are not ordered by importance. `features/Feature-Prioritization.md`
orders individual requirements, and a whole group is rarely uniformly high or low priority.

---

# Related

| | |
| --- | --- |
| `Requirements.md` | The units being grouped |
| `features/Feature-Prioritization.md` | Ordering, which grouping does not do |
| `03-user` | Where the jobs come from |
| `09-technology`, `10-execution` | Structure and slices, derived separately |

---

> **Concept Note**
>
> Group by the job, in the user's words.
>
> Group by screen or component and you have made design and
> architecture decisions in a table of contents.
