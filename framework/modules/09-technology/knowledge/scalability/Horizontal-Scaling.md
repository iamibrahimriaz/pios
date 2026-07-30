---
Title: Horizontal Scaling
Module: 09-technology
Section: knowledge/scalability
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Add instances where the application allows it, and name what does not scale that way.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/scalability/Vertical-Scaling.md
Outputs:
  - Scaling response within scalability_plan
Related Modules:
  - 06-business
  - 13-operations
Tags:
  - Technology
  - Scalability
  - Concept
---

# Horizontal Scaling

---

# What It Is

Adding more instances behind a load balancer — available only if the application is stateless, which
`architecture/Scaling.md` established as a free design property.

What it scales and what it does not:

| Scales this way | Does not |
| --- | --- |
| Stateless application instances | The database's write capacity |
| Background workers | Anything holding local state |
| Read traffic, with replicas | A single external service's rate limit |
| Inference calls, up to the provider's limit | Provider quotas — a `14-ai-systems` constraint |

The pattern that matters: **adding application instances moves the bottleneck to the database.** That is not a failure; it is the
next bottleneck, and Move 6 requires it named in advance.

---

# When It Applies

In Move 6 (Size), as the response where vertical scaling has been exhausted or where redundancy is separately required.

---

# How to Apply It Here

**Verify statelessness before claiming the capability.** Local sessions, local file writes and in-process caches each prevent it,
and each is easy to introduce accidentally.

**Name the next bottleneck.** Adding instances relocates the constraint. If the answer is the database, `Caching.md` and read
replicas are the next responses, in that order.

**Distinguish redundancy from capacity.** Two instances for availability and ten for throughput are different requirements with
different costs. `13-operations` cares about the first.

**Watch the connection count.** More instances mean more database connections, and connection limits are a real ceiling reached
sooner than expected. Pooling is part of the design.

**Cost it per instance against the ceiling.** `09-technology/knowledge/Infrastructure.md`'s arithmetic applies, and horizontal
scaling multiplies the per-instance cost directly.

---

# Where It Misleads

**It is treated as scalability itself.** It scales one layer. The stateful components — database, file store, queue — are where
capacity actually runs out, and they need their own responses.

**Sticky sessions are used to work around state.** They defeat the point: an instance failure now loses those users' sessions, and
load distributes unevenly.

**Auto-scaling is configured as a substitute for knowing the bottleneck.** It adds instances until the constraint is elsewhere,
then adds more, and the bill scales while the problem persists.

**Provider rate limits are ignored.** For AI features the inference provider's quota is a hard ceiling no amount of application
scaling raises. `14-ai-systems` should have it.

**It is designed before it is needed.** `Vertical-Scaling.md` first, and `architecture/Scaling.md`'s rule stands: keep the option
open, do not exercise it early.

---

# Related

| | |
| --- | --- |
| `Vertical-Scaling.md` | The response to try first |
| `Caching.md`, `Queues.md` | Relieving the database and the request path |
| `architecture/Scaling.md` | The statelessness that makes this possible |
| `14-ai-systems` | Provider quotas as a ceiling |

---

> **Concept Note**
>
> Adding instances moves the bottleneck to the database. Name it before
> you move it.
>
> And sticky sessions are not statelessness — they are the problem with
> a workaround attached.
