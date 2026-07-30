---
Title: Modules
Module: 09-technology
Section: knowledge/architecture
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Draw internal boundaries that are cheap to move and enforced by something other than intent.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/architecture/Monolith.md
Outputs:
  - Internal structure within architecture
Related Modules:
  - 08-product
Tags:
  - Technology
  - Architecture
  - Concept
---

# Modules

---

# What It Is

Boundaries inside one deployable — the cheapest place in the framework to be wrong about a boundary.

A module boundary is worth having when three things hold:

| Property | Meaning |
| --- | --- |
| **Owns its data** | Other modules do not read its tables directly |
| **Has a stated interface** | Callers use named operations, not internals |
| **Can be reasoned about alone** | Its rules make sense without opening another module |

Boundaries derive from the domain, and the domain is already described. `08-product`'s grouping by job is one input;
`DDD.md` covers deriving them from the model. What they must not follow is a technical layering — a "services" module and a
"models" module are layers, and they put every domain concept in both.

---

# When It Applies

In Move 5 (Choose), after the shape is chosen and regardless of which shape it is.

---

# How to Apply It Here

**Enforce the boundary mechanically.** A convention nobody checks erodes within weeks. Language features, package rules, a lint
rule or a directory-level import restriction — anything that fails a build rather than a review.

**Give each module its own tables and forbid cross-reads.** Shared table access is the coupling that makes later extraction
impossible, and it is invisible in an architecture diagram.

**Keep cross-cutting obligations in one module.** Authorization, audit and retention are the located enforcement points from Move
4. Scattering them across modules is what breaks the "located" requirement.

**Test the boundary by asking what extraction would cost.** If pulling a module into its own service would require touching
twenty files elsewhere, the boundary is nominal.

**Expect it to differ from `08-product`'s grouping.** Product areas group by job for navigation; modules group by data ownership.
Related but not identical, and both are legitimate.

---

# Where It Misleads

**Modules are drawn as technical layers.** Controllers, services, repositories. Every domain concept then spans all three, and no
boundary exists in the sense that matters.

**Boundaries are documented and not enforced.** Documented boundaries are aspirations. The mechanism is what makes them real, and
without it the design decays into the thing people blame the monolith for.

**Shared tables are treated as an optimization.** They are the single most consequential coupling in a codebase, and they are the
reason extractions turn into rewrites.

**Boundaries are drawn once and never revisited.** Inside one deployable they are cheap to move, which is the shape's main
advantage — and it goes unused if nobody revisits them.

**Too many modules are created early.** Three or four meaningful boundaries beat twelve nominal ones, and the domain rarely
supports twelve at launch.

---

# Related

| | |
| --- | --- |
| `Monolith.md` | The shape modules live inside |
| `Microservices.md` | Where a boundary becomes expensive |
| `DDD.md` | Deriving boundaries from the domain |
| `08-product` | Grouping by job, for a different purpose |

---

> **Concept Note**
>
> A boundary nothing enforces is a comment.
>
> Inside one deployable, boundaries are cheap to move — which is
> exactly why that is where you should get them wrong.
