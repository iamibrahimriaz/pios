---
Title: Information Architecture
Module: 10-execution
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Organize the product around the user's mental model, in the user's vocabulary.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 10-execution/knowledge/User-Flows.md
Outputs:
  - Structure within ux_flows
Related Modules:
  - 03-user
  - 09-technology
Tags:
  - Execution
  - UX
  - Concept
---

# Information Architecture

---

# What It Is

How the product is organized — what lives where, and what it is called.

Two sources compete, and only one is correct:

| Organize by | Result |
| --- | --- |
| **The user's mental model** | Navigation matches how they already think about the work |
| The data model | Navigation matches how the system stores things |

`09-technology` derived entities from requirements, which makes the data model a faithful description of the system and a poor
description of the user's world. A patient, a note and an appointment may be three entities and one place the clinician goes.

The vocabulary rule is the same one `09-technology/knowledge/architecture/DDD.md` applies to the model: **use the practitioners'
words**, recorded in `03-user`. A product that renames the domain forces every user to translate.

---

# When It Applies

In Move 1 (Flow), as the structure the paths run through.

---

# How to Apply It Here

**Name things as the user names them.** `03-user` recorded the vocabulary. Where the internal term differs from theirs, the
interface uses theirs and the difference stays internal.

**Organize around the job, not the entity.** The clinician's unit of work is a consultation, and it may touch four entities. The
navigation should reflect the consultation.

**Keep depth shallow for frequent tasks.** `03-user`'s frequency findings decide it: a task performed forty times a day should be one
step from the entry point.

**Decide what the entry point shows.** For a professional tool it is usually today's work rather than a dashboard, and that decision
is a `08-product` behavior with an empty state.

**State what is deliberately not in the navigation.** Administrative and rarely used functions belong somewhere findable and out of
the way. Saying so prevents them accumulating in the main path.

---

# Where It Misleads

**The navigation mirrors the entities.** It is the path of least resistance because the model already exists, and it produces a
product organized for the database.

**Internal terminology reaches the interface.** Terms from the data model, the architecture, or the team's shorthand each force the
user to learn vocabulary that serves them not at all.

**Everything is made reachable from everywhere.** Comprehensive navigation is undifferentiated navigation; the frequent task loses its
advantage.

**Structure is designed for the complete product.** The MVP has a fraction of the surface. A navigation built for the eventual scope
is mostly empty, and empty navigation reads as an unfinished product.

**Search is offered instead of structure.** Search finds what you can name. Structure is how someone discovers what exists, and
`09-technology/knowledge/database/Search.md` notes most search needs are lookups anyway.

---

# Related

| | |
| --- | --- |
| `User-Flows.md` | The routes through the structure |
| `Microcopy.md` | The words, in detail |
| `Wireframes.md` | Where structure becomes layout |
| `03-user`, `09-technology` | Vocabulary, and the model not to mirror |

---

> **Concept Note**
>
> Organize around the job, name things as the user names them.
>
> A navigation that mirrors the data model is a product organized for
> the convenience of the storage layer.
