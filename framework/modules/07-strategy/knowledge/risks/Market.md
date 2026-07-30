---
Title: Market Risks
Module: 07-strategy
Section: knowledge/risks
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Register the risks arising outside the product, including the clock on an indefensible gap.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 07-strategy/knowledge/risks/Mitigation.md
Outputs:
  - Market risks within risk_register
Related Modules:
  - 02-market
  - 05-competition
Tags:
  - Strategy
  - Risk
  - Concept
---

# Market Risks

---

# What It Is

The risks that come from the market rather than from the build.

| Risk | Early warning sign |
| --- | --- |
| **The gap is not defensible — a clock is running** | An incumbent's changelog, a job posting, a conference announcement |
| **An incumbent ships an adequate version to its own customers** | Sales conversations start mentioning them |
| **A platform absorbs the capability** | Platform roadmap notes, developer previews |
| **The enabling technology becomes free** | Provider pricing changes; the feature appears as a default elsewhere |
| **The segment turns out to be unreachable** | No route produces a first customer after a named period |
| **Timing was wrong — the market is not ready** | Buyers agree with the problem and defer indefinitely |
| **The problem disappears** | A process reform or payment change removes it |

The first row is inherited from `05-competition` explicitly: **if the gap is not defensible, there is a clock on the
opportunity.** The register's job is to say roughly how long and what to watch.

---

# When It Applies

In Move 6 (Register), drawing on `02-market`'s trends — including the required trend that argues against the idea —
and `05-competition`'s threat assessment.

---

# How to Apply It Here

**Convert the adversarial trend into a registered risk.** `02-market` required at least one trend working against the
idea. If it is not in the register, one of the two modules did not do its job.

**Attach a rough duration to the defensibility clock.** "Twelve to twenty-four months before an incumbent could ship
this" changes the sequence. "Not defensible" alone does not.

**Register unreachability with a date attached.** If no route produces a customer within a stated period, that is a
stop condition rather than a general concern. `06-business`'s first-ten route is the test.

**Watch the specific incumbent, named.** Defensibility was assessed against a named company in `05-competition`. The
early warning is that company's behavior, not the market's.

**Keep the benign risk in.** A process reform or a change in how the work is funded can remove the problem entirely.
In institutional markets that is the honest tail risk and it is nobody's fault when it happens.

---

# Where It Misleads

**Market risk is treated as beyond influence and therefore not registered.** Unmitigable risks still need early
warnings, because the response — accelerate, re-scope, or stop — depends on seeing them early.

**Competitive response is imagined as a better product.** `05-competition` is explicit: the likely response is an
adequate version shipped to customers they already have. Adequate plus installed beats better plus unknown.

**Commoditization is treated as distant.** For AI-based products it is the central market risk and it has repeatedly
arrived faster than planned for. `05-competition`'s question — what survives if the model is free — is the test.

**"We are early" is recorded as a position rather than a risk.** Early and wrong are indistinguishable from the
inside. The distinguishing evidence is behavioral, and `04-problem` either has it or does not.

**Market risk becomes a reason to widen scope.** Anticipating a response can justify any amount of building. The
correct output is a risk with a timeline handed to the sequence, not a larger MVP.

---

# Related

| | |
| --- | --- |
| `Mitigation.md` | Structure, ratings and ownership |
| `Business.md` | Risks to the model rather than the market |
| `02-market` | Trends, timing and the adversarial finding |
| `05-competition` | Defensibility and threat assessment |

---

> **Concept Note**
>
> An indefensible gap is a clock. Register the duration and name the
> company you are watching.
>
> The response you should expect is adequate and already distributed —
> not better.
