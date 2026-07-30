---
Title: Vertical Scaling
Module: 09-technology
Section: knowledge/scalability
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Exhaust the simplest scaling response before considering any other.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/architecture/Scaling.md
Outputs:
  - Scaling response within scalability_plan
Related Modules:
  - 06-business
Tags:
  - Technology
  - Scalability
  - Concept
---

# Vertical Scaling

---

# What It Is

Making the machine bigger — the first scaling response, and for most products the only one needed.

Its advantages are unusual in this field: **it requires no design change at all.**

| Advantage | |
| --- | --- |
| No code change | The application does not know |
| No new failure modes | Nothing distributed is introduced |
| Immediate | Minutes, typically |
| Reversible | Scale back down when the load was temporary |
| Cheap in engineering time | Which is the expensive resource at launch |

The honest limits:

| Limit | |
| --- | --- |
| A ceiling exists | Large, and further away than usually assumed |
| Cost rises faster than capacity at the top end | The point where horizontal becomes cheaper |
| A single instance is a single point of failure | An availability question, not a capacity one |
| Resizing may need a restart | A maintenance window, which many products can accept |

---

# When It Applies

In Move 6 (Size), as the stated response to the first bottleneck wherever it suffices.

---

# How to Apply It Here

**Name it as the response where it works.** Move 6 requires a named response per bottleneck, and "increase the instance size"
is a complete and creditable answer.

**Compute where the ceiling actually is.** Against `06-business`'s target figures. For a professional tool with thousands of
users, a single large instance is frequently sufficient indefinitely — and knowing that ends the architecture argument with
arithmetic.

**Separate capacity from availability.** If a single instance is unacceptable for uptime reasons, that is a redundancy
requirement, and it should be stated as one rather than disguised as scaling.

**Check the query first.** Before more hardware, `database/Indexes.md`: the first bottleneck is usually one query, and an index
is cheaper than any instance size.

**Say when it stops being the answer.** The load figure at which horizontal scaling becomes necessary or cheaper. That is a
trigger, not a plan to execute now.

---

# Where It Misleads

**It is dismissed as unsophisticated.** It is the highest-leverage scaling response available to a small team, because it
consumes no engineering time — the scarcest resource in the plan.

**Its ceiling is assumed to be low.** Modern single instances are very large. Assuming otherwise is the premise behind most
architecture inflation.

**Capacity problems are solved with hardware when they are query problems.** More memory hides a missing index until the data
grows again.

**Availability requirements are met by scaling.** A bigger single instance is still one instance. Redundancy is a separate design
decision with its own cost.

**Cost is not checked at the larger size.** The instance that solves the problem may break `06-business`'s cost ceiling, which
is the same check `09-technology/knowledge/Infrastructure.md` runs.

---

# Related

| | |
| --- | --- |
| `Horizontal-Scaling.md` | The next response, and its cost |
| `Performance.md` | Finding what is actually slow |
| `database/Indexes.md` | The cheaper fix, usually |
| `06-business` | Target figures and the cost ceiling |

---

> **Concept Note**
>
> Bigger machine, no code change, done in minutes.
>
> Its ceiling is much higher than the architecture conversation
> assumes — and the first bottleneck is usually one query anyway.
