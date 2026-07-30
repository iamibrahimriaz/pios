---
Title: DDD
Module: 09-technology
Section: knowledge/architecture
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Take the parts of domain-driven design that help here, and leave the machinery.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/architecture/Modules.md
Outputs:
  - Boundary derivation within architecture
Related Modules:
  - 03-user
  - 08-product
Tags:
  - Technology
  - Architecture
  - Method
---

# DDD

---

# What It Is

A design approach organized around the language and boundaries of the problem domain.

Three of its ideas earn their place in this module. The rest is machinery a small product does not need:

| Idea | Why it helps here |
| --- | --- |
| **Ubiquitous language** | Use the practitioners' words in the model — `03-user` already recorded them |
| **Bounded context** | A boundary within which one term means one thing — the strongest guide to `Modules.md` |
| **Aggregate** | The unit that must change together, which is what a transaction boundary actually is |

The bounded-context idea is the useful one, and its diagnostic is a **word that means two things**. If "appointment" means one
thing in scheduling and another in billing, that is a boundary — and modeling both with one entity produces a table with columns
that are conditionally meaningless.

---

# When It Applies

As reference during Move 1 (Derive) and Move 5 (Choose). Nothing in the module requires its vocabulary.

---

# How to Apply It Here

**Take the vocabulary from `03-user` and use it unchanged.** Practitioners' words in the model mean the model can be discussed with
them, and translation layers between "our term" and "their term" are where misunderstandings live.

**Find the words that mean two things.** Each one is a candidate boundary. This single question does more for a data model than
any amount of pattern application.

**Use aggregates to decide transaction scope.** What must be consistent at all times, versus what may lag briefly. That decision
is what `Queues.md` and `Events.md` depend on.

**Stop there.** Repositories, factories, specifications and domain events are tools for large systems with many contributors. In a
small product they add ceremony `Architecture-Styles.md`'s inflation check should catch.

**Keep the model derived from requirements.** Move 1's rule stands: entities come from `08-product`'s nouns. DDD supplies the
boundaries, not permission to invent the entities.

---

# Where It Misleads

**Its patterns are applied wholesale to a small product.** The machinery is substantial and its benefits appear at a scale most
products never reach. Applying it early is inflation with respectable vocabulary.

**"Bounded context" becomes a justification for splitting into services.** A context is a boundary; it need not be a deployable.
`Modules.md` is where it should live first.

**The domain model is designed before the requirements are read.** That is Move 1 inverted — a mental picture reconciled
afterward, which always reconciles.

**Ubiquitous language is invented rather than adopted.** If the term is not what practitioners say, it is not their language.
`03-user` has the real vocabulary.

**Aggregates are drawn to be tidy rather than transactional.** Their only real purpose here is deciding what must change together,
which is a consistency question with an operational answer.

---

# Related

| | |
| --- | --- |
| `Modules.md` | Where bounded contexts should first appear |
| `Events.md`, `Queues.md` | What crossing an aggregate boundary implies |
| `database/Entities.md` | Deriving the model from requirements |
| `03-user` | The vocabulary to adopt |

---

> **Concept Note**
>
> Take three ideas: their words, the boundaries where a word changes
> meaning, and what must change together.
>
> Leave the rest. A word that means two things has told you more than
> any pattern will.
