---
Title: Caching
Module: 09-technology
Section: knowledge/scalability
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Use caching as a measured response to a named bottleneck.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/architecture/Caching.md
Outputs:
  - Caching response within scalability_plan
Related Modules:
  - 14-ai-systems
Tags:
  - Technology
  - Scalability
  - Concept
---

# Caching

---

# What It Is

Caching as a **load response** — the correctness consequences are `architecture/Caching.md`'s subject; this file is about when it
actually helps.

It helps when the access pattern has a particular shape:

| Cache when | Do not bother when |
| --- | --- |
| Reads far outnumber writes | Every read is of freshly written data |
| The same values are requested repeatedly | Access is uniformly distributed across a large set |
| The computation is expensive | The query is already fast — an index would have been the fix |
| Staleness is acceptable for a stated period | Correctness requires the current value |

The measure that decides it is the **hit ratio**. A cache with a low hit ratio adds a lookup, a network hop and an invalidation
obligation while relieving nothing.

For AI features there is a second, sharper case: caching identical inference requests removes both latency *and* cost per call,
and cost per user is already in `14-ai-systems`' arithmetic.

---

# When It Applies

In Move 6 (Size), after the first bottleneck is named — never before.

---

# How to Apply It Here

**Measure before adding.** Move 6 names the bottleneck with a figure. A cache introduced without that figure has no way to be
shown to have worked.

**Estimate the hit ratio from the access pattern.** A reporting query every user runs each morning caches well. A per-record
lookup across a large corpus does not.

**Fix the query first.** `database/Indexes.md`: a missing index masquerading as a caching need is extremely common, and the index
has no staleness cost.

**Cache inference results where inputs repeat.** For an AI feature this is a direct cost reduction, and it should appear in the
per-user cost figure rather than being treated as an optimization.

**Handle the simultaneous-miss case.** Many requests missing at once can hit the origin harder than no cache at all. A single-flight
mechanism is part of the design.

---

# Where It Misleads

**Caching is the reflexive answer to slowness.** The reflex skips the measurement, and the underlying cause — usually a query — stays
in place and reappears at the next data volume.

**Hit ratio is never checked after deployment.** An ineffective cache is pure overhead plus an invalidation obligation, and nothing
reports it. `Monitoring.md` should.

**Caching is used to hide a design problem.** A page requiring forty queries cached to appear fast is still a page requiring forty
queries, and the first cache miss shows it.

**Cost savings from inference caching are assumed rather than computed.** The saving depends entirely on how often inputs repeat,
which is a product question.

**Stale data is treated as a scalability trade rather than a product decision.** `architecture/Caching.md` is explicit: staleness is
visible to the user and belongs in `08-product`.

---

# Related

| | |
| --- | --- |
| `architecture/Caching.md` | Invalidation, keys and correctness |
| `Performance.md` | Finding the bottleneck first |
| `database/Indexes.md` | The cheaper fix, usually |
| `14-ai-systems` | Where a cache reduces cost per user |

---

> **Concept Note**
>
> Measure, then cache — and check the hit ratio afterwards.
>
> A cache nobody measures is overhead with an invalidation obligation
> attached.
