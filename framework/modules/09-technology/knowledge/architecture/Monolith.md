---
Title: Monolith
Module: 09-technology
Section: knowledge/architecture
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Treat one deployable as the default and state what it genuinely costs.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/architecture/Architecture-Styles.md
Outputs:
  - Architecture shape within architecture
Related Modules:
  - 13-operations
Tags:
  - Technology
  - Architecture
  - Concept
---

# Monolith

---

# What It Is

One deployable unit containing the whole application — the framework's default shape, and the correct answer for most products at
launch.

What it gives, plainly:

| Advantage | Why it matters at launch |
| --- | --- |
| One thing to deploy | `09-technology/knowledge/Deployment.md` stays simple, and revert stays possible |
| Transactions across the model | Consistency is free rather than designed |
| One place to debug | A stack trace crosses the whole request |
| One thing to operate | `13-operations`' rota is one rota |
| Lowest idle cost | The floor `06-business` pays before revenue |

And the real costs, which should be stated rather than dismissed:

| Cost | Mitigation |
| --- | --- |
| Everything scales together | Vertical scaling first; extract the one hot path later |
| Boundaries erode without discipline | `Modules.md` — enforced internal boundaries |
| One deployment for all changes | Acceptable when the team is small |
| A fault can affect everything | Bounded by the same discipline that keeps boundaries clean |

---

# When It Applies

In Move 5 (Choose), as the starting position from which any other shape must be justified.

---

# How to Apply It Here

**Choose it explicitly rather than by omission.** A recorded decision — with the alternative and the trade-off, per
`09-technology/knowledge/Tech-Stack.md` — is what distinguishes a default from an absence of thought.

**Enforce internal boundaries from the start.** That is the whole difference between a monolith that stays workable and one that
becomes the thing people complain about. `Modules.md` covers the mechanism.

**Identify the path that would be extracted first.** Usually the one with a different scaling profile — inference, report
generation, document processing. Knowing it is free; extracting it early is not.

**Keep long-running work out of the request path.** `Queues.md` covers this: a background worker in the same deployable is still
one deployable, and it prevents the most common reason people abandon the shape.

**State the vertical-scaling headroom.** `scalability/Vertical-Scaling.md` covers how far it goes, which is much further than
usually assumed.

---

# Where It Misleads

**It is treated as a phase rather than a shape.** Many products should stay this way permanently. "We will split it later" is
sometimes true and is not a requirement.

**"Monolith" is used to mean "unstructured".** They are unrelated. A well-bounded single deployable is a design; a tangle is a
failure of discipline that splitting into services would only distribute.

**Its faults are attributed to the shape.** Slow deployments, coupled code and difficult testing are usually boundary problems.
Distributing them across a network makes them harder, not better.

**Scaling limits are assumed to arrive early.** For a professional tool with thousands of users, a single well-sized instance is
frequently sufficient for years — and Move 6's job is to say where the actual first bottleneck is, which is usually a query.

**It is rejected because it sounds unambitious.** `Architecture-Styles.md` names the inflation this produces, and the cost check
is where it becomes visible.

---

# Related

| | |
| --- | --- |
| `Modules.md` | The boundaries that keep it workable |
| `Microservices.md` | What splitting actually costs |
| `Queues.md` | Keeping slow work out of the request |
| `scalability/Vertical-Scaling.md` | How far one instance goes |

---

> **Concept Note**
>
> One deployable, with real internal boundaries, is the default — and
> frequently the destination.
>
> "Monolith" and "unstructured" are unrelated words, and splitting a
> tangle just distributes it.
