---
Title: Microservices
Module: 09-technology
Section: knowledge/architecture
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: State what splitting buys and what it costs, and require a reason from the requirements.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/architecture/Monolith.md
Outputs:
  - Architecture shape within architecture
Related Modules:
  - 06-business
  - 13-operations
Tags:
  - Technology
  - Architecture
  - Concept
---

# Microservices

---

# What It Is

Separately deployable services communicating over a network.

| Buys | Costs |
| --- | --- |
| Independent scaling of one component | Every call can now fail partially |
| Independent deployment | Distributed transactions, or accepting eventual consistency |
| Technology choice per service | Multiple deployments, environments and monitoring surfaces |
| Team autonomy per service | A cost floor per service, paid whether used or not |
| Fault isolation, when boundaries are right | Debugging across services, without one stack trace |

The organizational point is usually decisive: the shape solves a **coordination problem between teams**. With one or two people,
there is no coordination problem to solve, and the costs arrive anyway.

The framework's position: a split needs a reason drawn from the requirements — a component with a genuinely different scaling
profile, a regulatory boundary requiring isolation, or a team per service. Absent one, `Architecture-Styles.md`'s inflation
applies.

---

# When It Applies

In Move 5 (Choose), only where such a reason exists and survives the load and cost checks.

---

# How to Apply It Here

**Name the requirement forcing the split.** Not a preference: a scaling profile, an isolation obligation, or a team boundary.
One named reason, per service.

**Run the cost check on the sum.** Each service has a floor. `09-technology/knowledge/Infrastructure.md` totals them, and three
services can exceed the ceiling `06-business` set before any customer exists.

**Get the boundary right first — in one deployable.** `Modules.md` is the cheap place to discover a boundary is wrong. Once it is
a network boundary, moving it is a migration.

**Design for partial failure explicitly.** What happens when service B is unavailable is an `08-product` edge case in the failure
category, and it needs a specified behavior per call.

**Confirm operability.** Multiple deployables mean multiple things to monitor, patch and recover. `13-operations` staffs it, and a
rota of one cannot cover four services meaningfully.

---

# Where It Misleads

**It is chosen for scalability the product will never need.** Move 6's figures come from `06-business`, and they usually show one
instance is sufficient for years.

**Extraction is expected to fix coupling.** Coupled code across a network is coupled code with latency and partial failure added.
The boundary is the problem, and the boundary can be fixed in place.

**Consistency is assumed to survive the split.** Transactions do not cross services. Every invariant spanning two services
becomes a design problem — usually solved with a queue and an accepted window of inconsistency.

**The operational cost is treated as one-time.** It is recurring, per service, forever, and it lands in `13-operations`' true
cost to serve.

**One AI component justifies a full split.** Extracting the inference path is frequently correct and is one extraction — not an
architecture. `Monolith.md` names it as the usual first candidate.

---

# Related

| | |
| --- | --- |
| `Monolith.md` | The default, and the first extraction candidate |
| `Modules.md` | Where boundaries should be tested first |
| `Queues.md`, `Events.md` | How split services actually communicate |
| `06-business`, `13-operations` | The cost ceiling and the rota |

---

> **Concept Note**
>
> The shape solves a coordination problem between teams. With two
> people there is none to solve.
>
> Get the boundary right inside one deployable — that is the only place
> it is still cheap to be wrong.
