---
Title: Long Term Vision
Module: 07-strategy
Section: knowledge/solutions
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: State where the chosen approach leads, so the choice can be judged on its destination.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 07-strategy/knowledge/solutions/Tradeoffs.md
Outputs:
  - Destination of the chosen approach
Related Modules:
  - 06-business
  - 09-technology
Tags:
  - Strategy
  - Options
  - Concept
---

# Long Term Vision

---

# What It Is

Where each option **leads** — a property of the approach, assessed during the comparison.

This is distinct from `07-strategy/knowledge/Vision.md`, which is the destination the product is aimed at, and from
`Future.md`, which is the horizon in the roadmap. Here the question is narrower and more decision-relevant:

> If this option succeeds, what kind of company does it make?

| Option shape | Where it tends to lead |
| --- | --- |
| **Narrow tool** | A focused business with a ceiling set by segment and price |
| **Workflow replacement** | A system of record — high switching cost, long sales cycles, heavy operations |
| **Layer on top** | Dependence on the incumbent's platform and its terms |
| **Service first** | A services business, unless the automation transition is planned and triggered |
| **Second segment first** | A different product than the one originally conceived |

Each destination is legitimate. They are not equally compatible with the operator's goal, and that is the point of
assessing them.

---

# When It Applies

In Move 2 (Compare), as a criterion, and in Move 3 (Choose) as part of what the choice commits to.

---

# How to Apply It Here

**Score the destination against `01-idea`'s operator goal.** Replace a salary, venture scale, or sell to one known
buyer — the same option leads somewhere well suited to one and badly suited to another. That question is the
framework's most consequential input and this is where it pays off.

**Name the dependency each destination creates.** A layer depends on a platform's API and pricing. A service business
depends on people. A system of record depends on operational maturity `13-operations` must fund.

**Say what the destination requires that does not exist yet.** Sales capability, certification, an operations rota, a
data agreement. Those are real future costs and they belong in `06-business`'s model rather than arriving as
surprises.

**Note the architectural implication as context, not as scope.** If an option leads to multi-tenancy or a second
jurisdiction, `09-technology` should know. Knowing is free; building for it now is inflation.

**Check that the destination matches the vision.** If the chosen option's natural end point is not the vision from
`01-idea`, that is a finding for the human checkpoint — not something to reconcile by editing the vision.

---

# Where It Misleads

**The destination is assumed to be a choice made later.** It is largely determined by the first build. A layer is hard
to convert into a system of record, and a services business rarely becomes a product company without a deliberate,
triggered transition.

**Every option is described as leading to a large business.** Options differ, and describing them all as expandable
removes the criterion. The narrow tool's ceiling is real and should be stated as such.

**Long-term reasoning becomes justification for present scope.** Building today for a destination years away is
`Future.md`'s failure and `09-technology`'s architecture inflation. The destination informs the choice, not the cut.

**The platform-dependency risk of a layer is understated.** Terms change, pricing changes, and the platform can ship
the capability. `05-competition`'s threat analysis covers the last case and it is the most likely one.

**The transition from service to product is left implicit.** Without a stated trigger and a named mechanism, it does
not happen — the services revenue is immediate and the automation always defers.

---

# Related

| | |
| --- | --- |
| `Tradeoffs.md` | Where the destination is scored |
| `MVP-Solution.md` | The narrow tool's ceiling |
| `07-strategy` `Future.md` | The roadmap horizon, held loosely |
| `01-idea` `Goals.md` | The operator goal that judges the destination |

---

> **Concept Note**
>
> Ask what kind of company each option makes, and check it against
> what the operator actually wants.
>
> The destination is mostly decided by the first build — not by a
> later choice.
