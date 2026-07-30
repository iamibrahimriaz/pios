---
Title: Scaling
Module: 09-technology
Section: knowledge/architecture
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Design the shape so scaling remains possible, without building for absent scale.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/architecture/Architecture-Styles.md
Outputs:
  - Scaling properties within architecture
Related Modules:
  - 06-business
Tags:
  - Technology
  - Architecture
  - Concept
---

# Scaling

---

# What It Is

Scalability as a **property of the shape** rather than as work to be done — the design decisions that keep options open without
paying for capacity nobody needs.

`scalability/Horizontal-Scaling.md` and its siblings cover the responses. This file covers what makes them available:

| Design property | Why it preserves the option |
| --- | --- |
| **The application holds no local state** | Sessions, uploads and caches outside the process mean a second instance is possible |
| **Where state lives is deliberate** | Every stateful component is a scaling constraint, and knowing which one is first is Move 6's job |
| **Slow work is already asynchronous** | `Queues.md` — the request path stays short regardless of volume |
| **Reads and writes are distinguishable** | A read replica becomes available without restructuring |
| **One hot path is identifiable** | The candidate for extraction, known but not extracted |

These cost almost nothing at launch. That is the distinction the framework draws: **keeping an option open is cheap; exercising it
early is inflation.**

---

# When It Applies

In Move 5 (Choose) as design properties, and in Move 6 (Size) where the first bottleneck and the deliberate non-goals are named.

---

# How to Apply It Here

**Keep the application stateless from the first version.** It is nearly free then and a refactor later. Local session state and
local file writes are the two things that quietly prevent a second instance.

**Name every stateful component.** The database, the file store, the cache, the queue. One of them will be the first bottleneck,
and Move 6 requires it named with a figure.

**State the scaling response per bottleneck.** "The reporting query, at roughly 50 concurrent users; response: a read replica" is
the form Move 6 requires — a named limit and a named response.

**Say what you are deliberately not building for.** Move 6's third requirement, and the one usually missing. "Not built for
multi-region — every user is in one country" is a complete justification.

**Check the load figures against `06-business`.** They come from its projections with the arithmetic shown. A design sized well
beyond them fails the load check.

---

# Where It Misleads

**Scaling capability is built instead of preserved.** The stateless property costs nothing; a distributed architecture costs
money and months. The first is prudent, the second is `Architecture-Styles.md`'s inflation.

**The database is assumed to be the bottleneck.** Frequently it is one query, which is an index — `database/Indexes.md`. Naming
the bottleneck specifically usually reveals something cheap.

**Vertical headroom is underestimated.** A single well-sized instance handles far more than assumed, and
`scalability/Vertical-Scaling.md` covers how far.

**Scaling is planned without a load figure.** "It should scale" is what Move 6 explicitly rejects. Without a number there is no
design, only a hope.

**The absent non-goal invites the assumption of oversight.** Stating what the system is not built for is what makes the design
defensible rather than merely modest.

---

# Related

| | |
| --- | --- |
| `Architecture-Styles.md` | The load and cost checks |
| `Queues.md` | Keeping the request path short |
| `scalability/Horizontal-Scaling.md`, `scalability/Vertical-Scaling.md` | The responses |
| `06-business` | Where the load figures come from |

---

> **Concept Note**
>
> Keep the option open, do not exercise it.
>
> Statelessness is free at the start. A distributed architecture for
> absent load is paid for immediately.
