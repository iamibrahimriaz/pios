---
Title: Product Risks
Module: 07-strategy
Section: knowledge/risks
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Register the risk that the product is right and still not adopted.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 07-strategy/knowledge/risks/Mitigation.md
Outputs:
  - Product risks within risk_register
Related Modules:
  - 03-user
  - 04-problem
Tags:
  - Strategy
  - Risk
  - Concept
---

# Product Risks

---

# What It Is

The risks that the thing built does not get used — even when the problem is real and the solution works.

| Risk | Early warning sign |
| --- | --- |
| **The sharpest problem was assumed, not verified** | Milestone Zero's result, if it was run at all |
| **Switching cost exceeds the benefit** | Trials that complete tasks and do not convert |
| **The MVP cannot complete a job end to end** | The end-to-end test fails at requirements stage in `08-product` |
| **An immovable has to move** | Users describe a workaround to use the product |
| **The output needs checking, so nothing is saved** | Users re-read every result; time-saved metric flat |
| **Adoption stalls at a hand-off** | Usage drops at the step involving a second person |
| **The buyer's need diverges from the user's** | Enthusiasm from users, no progress with the signer |

The first row is the framework's central risk. Where `04-problem` marked the sharpest problem assumed, everything
downstream rests on it, and Milestone Zero is its mitigation.

---

# When It Applies

In Move 6 (Register), and re-examined at the human checkpoint — these are the risks the operator is actually deciding
about.

---

# How to Apply It Here

**Register the assumed-problem risk first and at full weight.** It is inherited from `04-problem` explicitly, and its
mitigation is a required Milestone Zero rather than any amount of build quality.

**Use `03-user`'s switching cost as the impact figure.** It is already quantified across five dimensions, and it makes
the risk concrete rather than general.

**Watch the review-time risk in AI products.** Output requiring careful checking has moved the work rather than removed
it. `12-metrics`' counter-metrics are the detection mechanism, and the early warning is users reading every result.

**Name the hand-off risk where a second person is involved.** `03-user`'s environment findings identify them, and
hand-offs are where products are abandoned quietly rather than rejected loudly.

**Set the early warning at trial level, not at revenue level.** By the time revenue reflects an adoption problem, the
information is months old.

---

# Where It Misleads

**Product risk is written as build risk.** Whether it can be built is `Technical.md`. Whether anyone uses it is this
file, and it is the larger risk in nearly every case.

**A working product is assumed to be an adopted one.** Adoption is governed by switching cost, habit, and whoever else
touches the work — none of which improves with product quality.

**The false negative is not registered.** An MVP that half-solves the problem produces rejection that gets read as
evidence against the problem. That is a risk about the *cut*, and `MVP.md`'s viability requirement is its mitigation.

**Feature gaps are registered as risks.** A missing capability is a scope decision recorded in the deferral ledger.
A risk is something that could invalidate the plan.

**The metric that would reveal the risk is not defined.** `12-metrics` defines it computably; a risk with no
corresponding measure has no early warning that anyone will actually observe.

---

# Related

| | |
| --- | --- |
| `Mitigation.md` | Structure and rating discipline |
| `Market.md` | Risks outside the product |
| `07-strategy` `MVP.md` | Viability, and the false-negative risk |
| `03-user`, `04-problem` | Where switching cost and evidence standing come from |

---

> **Concept Note**
>
> The largest product risk is that it works and nobody switches.
>
> Build quality does not reduce it — switching cost, habit and the
> hand-off do.
