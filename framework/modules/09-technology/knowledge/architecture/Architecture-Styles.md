---
Title: Architecture Styles
Module: 09-technology
Section: knowledge/architecture
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Choose the shape against load and team, and run the two checks against inflation.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/core/06-Framework.md
Outputs:
  - architecture
Related Modules:
  - 06-business
  - 13-operations
Tags:
  - Technology
  - Architecture
  - Method
---

# Architecture Styles

---

# What It Is

The shape of the system — chosen **against the load and the team**, not against what the industry is discussing.

| Shape | Suits |
| --- | --- |
| One deployable | Almost every product at launch. Simplest to build, deploy, debug and operate |
| Modular monolith | The same, with enforced internal boundaries — most of the benefit, none of the network |
| Separate services | Genuinely independent scaling or deployment needs, and a team per service |
| Serverless functions | Spiky, low-volume workloads where idle cost matters most |

And the module's characteristic failure:

> **Architecture inflation.** Designing for a scale that does not exist. Every component is individually justifiable; together
> they cost more than the business model can carry and take longer to build than the roadmap allows.

Two mechanical checks:

| Check | Fails when |
| --- | --- |
| **The load check** | The design's stated capacity far exceeds the launch and target figures from `06-business` |
| **The cost check** | Cost per user at launch exceeds `06-business`'s cost-to-serve ceiling |

> The cost check is the sharper of the two, because it converts an aesthetic argument about engineering taste into arithmetic.

---

# When It Applies

In Move 5 (Choose), before technology. Shape first, then the stack.

---

# How to Apply It Here

**Start from one deployable and justify any departure.** The burden of proof runs that way, and for most products at launch it is
not discharged.

**Run both checks and record the numbers.** Launch and target load from `06-business`; cost per user against its ceiling. A
design breaking the ceiling breaks the business model, and the resolution is a **regress** — to `06-business` for the price or
`07-strategy` for the scope — not a quiet acceptance.

**Apply the operability check.** Can the team that will run this actually run it? `13-operations` inherits the answer as a rota,
and a design nobody can operate is not a design.

**Get the boundaries right before splitting anything.** `Modules.md` covers this: internal boundaries in one deployable are
cheap to move, and boundaries between services are not.

**Say what you are deliberately not building for.** Move 6 requires it, and it stops the first person to hit a limit treating it
as an oversight.

---

# Where It Misleads

**Shapes are chosen by reputation.** The architectures discussed publicly are those of companies with thousands of engineers and
problems this product does not have.

**Inflation is invisible because each piece is defensible.** A queue, a cache, a search cluster and three services each have a
reason. The sum is unaffordable and unbuildable, which is why the checks are arithmetic rather than judgment.

**Future scale is treated as a present requirement.** `07-strategy`'s far horizon is a direction. Building for it is the same
error `08-product` commits when a vision justifies a feature.

**Splitting is expected to improve things.** It converts function calls into network calls, adds partial failure, and multiplies
the operational surface. It buys independent scaling and deployment, which most launch-stage products do not need.

**Operability is assumed.** The operator's actual skills and availability are a design constraint, and they belong in the
decision rather than in a later surprise.

---

# Related

| | |
| --- | --- |
| `Monolith.md`, `Microservices.md`, `Modules.md` | The shapes in detail |
| `Scaling.md` | Scaling as a shape property |
| `09-technology` `Infrastructure.md` | The cost check |
| `06-business`, `13-operations` | The ceiling, and who runs it |

---

> **Concept Note**
>
> Start with one deployable and make anything else earn its place with
> arithmetic.
>
> The cost check turns a taste argument into a number — and a design
> that breaks the ceiling breaks the business.
