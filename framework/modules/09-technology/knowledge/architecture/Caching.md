---
Title: Caching
Module: 09-technology
Section: knowledge/architecture
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Treat staleness as a product decision and authorization as a cache-key concern.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/architecture/Modules.md
Outputs:
  - Caching design within architecture
Related Modules:
  - 08-product
Tags:
  - Technology
  - Architecture
  - Concept
---

# Caching

---

# What It Is

Keeping a copy of a computed result — as an **architectural decision**, because it introduces a second version of the truth.

`scalability/Caching.md` covers caching as a response to load. This file covers what it changes about correctness:

| Decision | Nature of the decision |
| --- | --- |
| **How stale may this be?** | A product question. Seconds, minutes or hours is visible to the user |
| **How is it invalidated?** | The hard part. Time-based is simple and imprecise; event-based is precise and easy to miss a path |
| **What is the key?** | Where authorization leaks — a key omitting the viewer serves one user's data to another |
| **What happens on a miss under load?** | Many simultaneous misses can be worse than no cache at all |
| **Is the cached data regulated?** | Then it is another store under Move 4 — retention, residency and erasure apply |

The third row is the security-relevant one and it is a real, recurring failure: a cached response keyed only by URL, served to a
different user with different permissions.

---

# When It Applies

In Move 5 (Choose), and only after Move 6 has identified an actual bottleneck. A cache added before then is complexity with no
measured benefit.

---

# How to Apply It Here

**State the acceptable staleness per cached thing, and treat it as a requirement.** A user seeing a figure that is five minutes
old is a product behavior `08-product` should have specified.

**Include the viewer in every key for anything permission-dependent.** Or do not cache it. There is no third option that is safe.

**Prefer invalidating on write to expiring on time where correctness matters.** Then enumerate every path that writes the
underlying data — the missed path is the stale-forever bug.

**Classify cached regulated data.** Move 4's obligations follow the data, and `database/Soft-Delete.md`'s consistency point
applies: an erasure that misses the cache has not erased.

**Cache the expensive thing, not everything.** Move 6 names the first bottleneck. That is the thing worth caching, and the rest is
unmeasured complexity.

---

# Where It Misleads

**Caching is added preventively.** It introduces a second truth, an invalidation obligation and a debugging surface, in exchange
for solving a problem nobody has measured.

**Authorization is forgotten in the key.** This is the leak. It passes every test written by one user and fails the moment two
users with different permissions request the same resource.

**Invalidation is assumed to be handled.** It is the hardest part, and it fails by omission — one write path that does not
invalidate produces data that is wrong indefinitely, with no error anywhere.

**Stale data is treated as harmless.** In clinical or financial work a stale figure can be acted upon. Whether it is harmless is a
domain question, not a technical one.

**A cache becomes a store.** Once something exists only in the cache, losing it loses data — and caches are designed to be
losable. `09-technology/knowledge/Storage.md` draws that line.

---

# Related

| | |
| --- | --- |
| `scalability/Caching.md` | Caching as a load response |
| `09-technology` `Storage.md` | Cache versus store |
| `api/Authorization.md` | What the key must account for |
| `08-product` | Where staleness becomes specified behavior |

---

> **Concept Note**
>
> A cache key that omits the viewer will eventually serve one user's
> data to another.
>
> And an erasure that misses the cache has not erased anything.
