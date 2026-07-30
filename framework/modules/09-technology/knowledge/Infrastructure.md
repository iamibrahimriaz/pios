---
Title: Infrastructure
Module: 09-technology
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Enumerate every running component and price it against the business model's ceiling.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/Hosting.md
Outputs:
  - Infrastructure inventory within architecture
Related Modules:
  - 06-business
  - 14-ai-systems
Tags:
  - Technology
  - Infrastructure
  - Method
---

# Infrastructure

---

# What It Is

The list of everything that runs, with what each costs — the input to the **cost check**, which is the framework's first
of three arithmetic checks against `06-business`.

| Component class | Cost behavior |
| --- | --- |
| Compute — application, workers | Mostly fixed at low scale, then linear |
| Datastores | Fixed floor, then storage and connection limits |
| File and object storage | Linear with volume, plus egress |
| Queues, caches, search | Each a separate floor, paid whether used or not |
| **Model inference** | Linear with usage — `14-ai-systems` computes it per user |
| Monitoring, logging, error tracking | Often overlooked; frequently a real line |
| Third-party services | Per-seat or per-call, and they scale with success |

```
sum of component costs ÷ active users = cost per user
cost per user  vs  06-business's cost-to-serve ceiling
```

> A design that breaks the ceiling breaks the business model, and the resolution is a regress — to `06-business` for the
> price, or to `07-strategy` for the scope — not a quiet acceptance here.

---

# When It Applies

In Move 5 (Choose) as the cost check, and again in Move 6 (Size) at target scale.

---

# How to Apply It Here

**Enumerate exhaustively, including the small floors.** Six services at a modest monthly minimum each is a real number,
and it is the number that exists before any customer does.

**Compute at two points: launch and target.** Launch tests the runway; target tests the margin. Both come from
`06-business`'s own projections, with the arithmetic shown.

**Put inference cost in the same table.** For AI products it is frequently the dominant variable cost, and it rises with
engagement — meaning the best customers cost the most. `14-ai-systems` requires it as a share of revenue per user.

**Attribute each component to a requirement.** A running service that no requirement needs is architecture inflation with
a monthly invoice.

**Report the ceiling breach rather than absorbing it.** The check exists to force a decision, and quietly accepting a
broken margin is the failure it was written to prevent.

---

# Where It Misleads

**Infrastructure is priced at scale and the idle floor is ignored.** Pre-revenue, the floor is what matters, and
architectures with many always-on components have a high one.

**Managed-service minimums are treated as negligible.** Individually they are. Summed across a design with a queue, a
cache, a search index and a warehouse, they are a salary.

**Variable costs are modeled as linear when they are super-linear.** Egress, cross-region traffic and per-call third-party
fees can rise faster than users. Move 6's bottleneck analysis should say which.

**Cost is treated as an operational concern rather than a design one.** It is Move 5's sharpest anti-inflation check
precisely because it converts an argument about engineering taste into arithmetic.

**Monitoring and logging are omitted.** They are required by `13-operations` and they are frequently the third-largest
line in a small product's bill.

---

# Related

| | |
| --- | --- |
| `Hosting.md` | Where it runs |
| `scalability/Monitoring.md` | What must be observed, and its cost |
| `06-business` | The ceiling, and where a breach regresses to |
| `14-ai-systems` | Inference cost per user |

---

> **Concept Note**
>
> List everything that runs, divide by users, compare to the ceiling.
>
> The check exists to force a regress — absorbing a broken margin
> quietly is the failure it was written against.
