---
Title: PRD
Module: 08-product
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define what belongs in a PRD and what it must inherit rather than restate.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 08-product/knowledge/Requirements.md
Outputs:
  - prd_body
Related Modules:
  - 07-strategy
  - 09-technology
Tags:
  - Product
  - PRD
  - Concept
---

# PRD

---

# What It Is

The product requirements document — the artifact this module exists to produce, and the one most other modules read.

Its content divides into three kinds, and confusing them is what makes PRDs unusable:

| Kind | Source | Treatment here |
| --- | --- | --- |
| **Inherited** | Modules 01–07 | Referenced with its evidence tag, never re-argued |
| **Produced** | This module | Requirements, behavior, edge states, criteria, order |
| **Deferred** | Modules 09–13 | Named as a dependency, not decided |

The inherited section is short by design: the problem, the persona, the chosen approach, the MVP line and the
non-goals. Restating the reasoning behind them duplicates the research dossier and invites the decisions to be
reopened in a document that has no authority to change them.

---

# When It Applies

Assembled across all six moves and delivered as `prd_body`. It feeds the `prd` deliverable and is consumed by
`09-technology`, `10-execution` and design.

---

# How to Apply It Here

**Open with the one-sentence proposal and the non-goals.** A reader who stops after the first page should know what is
being built and what is deliberately excluded. `07-strategy` produced both.

**Carry evidence tags through unchanged.** If the problem is `[assumption: needs validation]`, the PRD says so. A PRD
that presents an assumed problem in confident prose is the framework's central failure occurring in its most-read
artifact.

**Keep the traceability spine visible.** Each requirement showing its parent problem is what lets a reviewer check both
directions — no orphans, no unserved problems above the line.

**Mark what is deferred and to whom.** Data model, architecture, screens, dates and metric targets each belong to a
named later module. A PRD that decides them removes those decisions from the modules equipped to make them.

**Write it so a builder can act without asking.** That is the standard `10-execution`'s cold-start test applies to the
handoff, and the PRD is most of what that test reads.

---

# Where It Misleads

**PRDs grow to demonstrate thoroughness.** Length correlates with the number of decisions nobody will find. The
requirements, the edge states and the criteria are the load-bearing content; everything else should be a reference.

**The inherited section becomes an argument.** Re-justifying the chosen approach invites the reader to re-litigate a
decision the operator already made at the human checkpoint.

**Assumptions get smoothed into facts by paragraph structure.** `04-problem` kept validated and assumed problems
visually separate for this reason, and a PRD that merges them undoes that work — without anyone lying.

**Implementation detail arrives because it feels concrete.** Naming a technology in a PRD looks decisive and pre-empts
`09-technology`, which derives it from requirements rather than inheriting it.

**It gets treated as a contract rather than a current statement.** Requirements change as evidence arrives. What must
not change silently is the cut — and the deferral ledger is how a change becomes visible.

---

# Related

| | |
| --- | --- |
| `FRD.md` | The narrower functional document, and when it is separate |
| `Requirements.md` | The core produced content |
| `Product-Strategy.md` | What is inherited and not re-decided |
| `09-technology`, `10-execution` | What the PRD must leave to them |

---

> **Concept Note**
>
> Inherit, produce, defer — and label which is which.
>
> A PRD that re-argues module 07's decision has reopened it, and a
> PRD that decides module 09's has closed it too early.
