---
Title: Performance
Module: 09-technology
Section: knowledge/scalability
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Name the first bottleneck with a figure, and state how the system degrades.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/Performance.md
Outputs:
  - scalability_plan
Related Modules:
  - 06-business
  - 13-operations
Tags:
  - Technology
  - Scalability
  - Method
---

# Performance

---

# What It Is

Behavior under load — where `09-technology/knowledge/Performance.md` covers the target, this covers what happens as volume rises.

Move 6's required form is specific:

| Required | Not acceptable |
| --- | --- |
| "First bottleneck: the reporting query, at roughly 50 concurrent users" | "It should scale" |
| "Response: add a read replica" | "Scale horizontally" |
| "Not built for: multi-region. Correct because every user is in one country" | Silence |

The third row is the one usually missing, and it is what makes the design defensible rather than merely modest.

Where the bottleneck usually is, in order of likelihood:

| Candidate | Typical fix |
| --- | --- |
| One unindexed or aggregate query | `database/Indexes.md` — the cheapest fix in the framework |
| N+1 query patterns | Batching, or a different interface shape |
| A single external service or provider quota | `Queues.md`, and a stated ceiling |
| Database write capacity | Vertical first, then partitioning — a large step |
| Application CPU or memory | `Vertical-Scaling.md`, then `Horizontal-Scaling.md` |

---

# When It Applies

In Move 6 (Size), producing `scalability_plan`.

---

# How to Apply It Here

**Name one bottleneck with a number.** Derived from `06-business`'s projections with the arithmetic shown — the same
show-the-arithmetic rule module 02 applies to market sizing.

**State the response, specifically.** "A read replica for reporting" is a response. "Scale horizontally" is a category.

**Describe degradation, not just the limit.** What the user experiences as the system approaches capacity: slower responses, queued
work, a rejected request with a clear message. Graceful degradation is a design, and `08-product`'s limit category should carry it.

**Say what the system is deliberately not built for**, with the reason. Multi-region, offline, real-time collaboration, unbounded
history — each stated non-goal prevents someone treating a limit as an oversight.

**Instrument what you predicted.** `Monitoring.md` watches the named bottleneck, which is how the prediction becomes useful rather
than decorative.

---

# Where It Misleads

**"It should scale" is offered as a plan.** Move 6 rejects it explicitly. Without a figure and a named limit there is nothing to
verify and nothing to monitor.

**Optimization begins before measurement.** The first bottleneck is usually one query, and effort spent anywhere else is effort
spent where the constraint is not.

**Load testing is skipped because the launch volume is small.** The point is not the volume; it is knowing *where* it breaks, so the
response is known in advance rather than improvised during an incident.

**Degradation is unspecified, so failure is abrupt.** A system that gets slower and then times out with no message is worse than one
that queues the request and says so.

**Success is assumed to be gradual.** A single institutional customer can multiply load overnight, which is why the named limit
matters more than the current volume.

---

# Related

| | |
| --- | --- |
| `09-technology` `Performance.md` | Where the target figure comes from |
| `Vertical-Scaling.md`, `Horizontal-Scaling.md` | The responses |
| `Monitoring.md` | Watching the named bottleneck |
| `06-business` | The load figures, with arithmetic |

---

> **Concept Note**
>
> One bottleneck, one number, one response — and a list of what you are
> deliberately not building for.
>
> "It should scale" is not a plan. It is the absence of one, phrased
> reassuringly.
