---
Title: Hosting
Module: 09-technology
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Choose where it runs against residency, cost per user and who operates it.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/Tech-Stack.md
Outputs:
  - Hosting choice within tech_stack
Related Modules:
  - 02-market
  - 06-business
  - 13-operations
Tags:
  - Technology
  - Hosting
  - Concept
---

# Hosting

---

# What It Is

Where the system runs, decided against three constraints that are all external to engineering taste:

| Constraint | Source |
| --- | --- |
| **Data residency** | `02-market` Frame 2's jurisdiction — often a hard legal boundary |
| **Cost per user** | `06-business`'s cost-to-serve ceiling |
| **Who operates it** | `13-operations`' rota — a design nobody can run is not a design |

And one commercial constraint that appears in institutional sales: some buyers require **self-hosting or a named
region**, which is a decision about the business model as much as the infrastructure.

---

# When It Applies

In Move 5 (Choose), and re-checked in Move 6 (Size) where the cost arithmetic runs.

---

# How to Apply It Here

**Pin the region explicitly and record it.** Defaults place data wherever the provider prefers. Where a regime constrains
residency, the region is a compliance mechanism at a named enforcement point.

**Run the cost check as arithmetic, not as an impression.** Cost per user at launch scale against `06-business`'s ceiling.
This is the sharper of Move 5's two anti-inflation checks because it converts taste into a number.

**Weigh managed services as a cost-versus-capacity trade.** They cost more per unit and consume far less operational
attention. For a one-person operation that trade is usually correct and should be stated as the reason.

**Check idle cost, not just cost at scale.** A pre-revenue product pays for whatever runs continuously. Architectures with
many always-on components have a floor that arrives before the first customer.

**State whether self-hosting is supported.** If it is, it is a distribution model with its own release, support and
upgrade obligations — `13-operations` and `06-business/knowledge/pricing/Enterprise.md` both need to know.

---

# Where It Misleads

**Cost is estimated at target scale and ignored at launch.** The relevant figure at launch is the floor: what is paid with
no users. That is the number that consumes runway.

**Residency is treated as configuration.** It is frequently a legal boundary, and a provider region chosen by default can
place regulated data outside the permitted jurisdiction — a blocker under Move 4's rule.

**Multi-region is designed for without a requirement.** Move 6 requires stating what the system is deliberately not built
for, and "every user is in one country" is a complete justification.

**Operational load is assumed to be zero.** Patching, certificate renewal, capacity, and incident response are recurring
work. `13-operations` prices them into the true cost to serve.

**Provider lock-in is unstated.** Managed services trade portability for convenience. That is a legitimate trade and it
belongs in `Tech-Stack.md`'s reversibility column.

---

# Related

| | |
| --- | --- |
| `Infrastructure.md` | What runs, and what it costs |
| `Deployment.md` | How it gets there |
| `02-market`, `06-business` | Residency and the cost ceiling |
| `13-operations` | Who operates it, and at what cadence |

---

> **Concept Note**
>
> Pin the region, compute the cost per user, and name who is on call.
>
> The figure that matters before revenue is the idle floor — what you
> pay with no customers at all.
