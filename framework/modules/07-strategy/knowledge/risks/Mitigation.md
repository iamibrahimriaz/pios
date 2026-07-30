---
Title: Mitigation
Module: 07-strategy
Section: knowledge/risks
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Make the risk register operational through early warning signs and differentiated ratings.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 07-strategy/core/06-Framework.md
Outputs:
  - risk_register
Related Modules:
  - 04-problem
  - 13-operations
Tags:
  - Strategy
  - Risk
  - Method
---

# Mitigation

---

# What It Is

The structure that turns a list of worries into something anyone would consult.

Each risk carries four things:

| | |
| --- | --- |
| **Likelihood** | Rated honestly, and differentiated |
| **Impact** | What it costs if it happens |
| **Mitigation** | What reduces the likelihood or the impact — with an owner |
| **Early warning sign** | What you would observe *before* it fully materializes |

> The early warning is what makes a register operational rather than decorative.

And the rating discipline: **a register where everything is "medium" is a register nobody will act on.** If every row
carries the same rating, no row has been assessed.

Three risks are inherited and must appear explicitly:

| From | Risk |
| --- | --- |
| `04-problem` | If the sharpest problem is assumed, the entire product rests on it |
| `05-competition` | If the gap is not defensible, there is a clock on the opportunity |
| `06-business` | The load-bearing economic assumption |

---

# When It Applies

In Move 6 (Register). The register is a deliverable in its own right and is consumed by `10-execution` and
`13-operations`.

---

# How to Apply It Here

**Write the early warning as an observation, not a feeling.** "Three of the first ten pilots stall at information
governance" is observable. "Adoption seems slow" is not, and it arrives too late to act on.

**Force the ratings apart.** If several risks look equal, rank them against each other and assign accordingly. The
register's value is the ordering.

**Give every mitigation an owner.** `13-operations`' rule applies here too: "the team" is not an owner. An unowned
mitigation is a sentence.

**Distinguish mitigation from acceptance.** Some risks cannot be reduced — a platform's pricing, a regulatory
direction, an indefensible gap. Accepting them explicitly, with the early warning recorded, is a legitimate and
honest entry.

**Connect the register to the stop conditions.** A risk materializing at full impact should map to a stop condition or
a re-scope. Where it maps to neither, the register has recorded something nobody will ever act on.

---

# Where It Misleads

**Uniform ratings make the register unusable and are the default outcome.** Rating honestly means some risks are low,
which feels like understating them. The alternative is a document with no signal.

**Mitigations get written as intentions.** "Monitor closely", "engage early", "stay flexible" reduce nothing. A
mitigation names an action, an owner and a trigger.

**The inherited risks are omitted because they came from other modules.** They are the largest risks in the register.
An assumed sharpest problem is the framework's central danger, and it belongs at the top with Milestone Zero as its
mitigation.

**Risks are listed without consequence.** The consequence is what makes it a decision. `06-business`'s example
applies: "CAC may be higher" changes nothing; "above £900, payback passes 18 months and the model needs funding" is
actionable.

**The register is written once and never revisited.** The early warning signs are the mechanism for revisiting it, and
they only work if someone is looking. That is a `13-operations` responsibility with a cadence, not a one-off.

---

# Related

| | |
| --- | --- |
| `Product.md`, `Market.md`, `Technical.md` and siblings | The risk categories |
| `07-strategy` `Milestones.md` | Where Milestone Zero mitigates the largest risk |
| `04-problem` | Where stop conditions originate |
| `13-operations` | Where monitoring becomes a schedule |

---

> **Concept Note**
>
> Name what you would see before it happens, and who is looking.
>
> A register where every row is "medium" has assessed nothing and will
> be read once.
