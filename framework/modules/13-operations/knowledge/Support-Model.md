---
Title: Support Model
Module: 13-operations
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Separate support commitments from forecasts, and treat each burden as a product signal.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 13-operations/core/06-Framework.md
Outputs:
  - support_model
Related Modules:
  - 08-product
  - 10-execution
Tags:
  - Operations
  - Support
  - Method
---

# Support Model

---

# What It Is

Who answers users, how fast, about what — and two kinds of statement that carry different standing:

| | Nature | Standing |
| --- | --- | --- |
| Channels, hours, response targets | **Commitments** | Operator decisions — `[verified: operator]` |
| Ticket volume, staffing need | **Forecasts** | Assumptions before launch |

> A response target the operator has not agreed to is a promise made on their behalf. A volume estimate presented as a plan is a
> staffing decision made on a guess.

And the reframing that makes this move productive:

> **The most common support request is usually a design defect with a queue attached.**

So each expected burden names why it will happen — from `10-execution`'s flow analysis — and **the product change that would remove
it.**

| Expected burden | Product change |
| --- | --- |
| "How do I get my existing records in?" | Import tooling, or a guided migration step |
| "Why can't I edit this?" | The state machine's rule made visible in the interface |
| "It didn't save" | The failure state from `08-product` §8, actually implemented |

---

# When It Applies

In Move 1 (Support), first — before severity, response and cost.

---

# How to Apply It Here

**Attribute every commitment to the operator.** Hours, channels and response targets are theirs to make. The framework proposes; it does
not commit on their behalf.

**Derive the expected burdens from `10-execution`'s flows.** The steps with the most friction, the states most likely to confuse, and the
edge cases `08-product` specified are where tickets come from.

**Route the removable burdens to the roadmap.** A support burden accepted without asking this question becomes a permanent staffing line
paid for a fixable defect.

**Say which burdens are genuinely permanent, and why.** Some are — regulated-market onboarding, integration setup, questions inherent to
the domain. Naming them separates the unavoidable cost from the avoidable one.

**Count free and trial users.** `06-business/knowledge/pricing/Freemium.md` and `Trials.md` both note they generate questions at close to
the rate paying customers do.

---

# Where It Misleads

**Response targets are written as though they were free.** Each one implies availability, which implies a rota — and
`The Rota Question` is the thing most often left unasked.

**Support volume is forecast confidently.** It is an assumption before launch and should carry the tag. `Cost-Model.md` runs sensitivity
on it because the staffing conclusion depends entirely on it.

**Tickets are treated as an operational cost rather than a product signal.** Then the queue is staffed instead of the defect being fixed,
permanently.

**The support channel is chosen for the operator's convenience.** `03-user` recorded how these users actually communicate — email, phone,
or through their organization's own process.

**Institutional support commitments are made casually.** `06-business/knowledge/pricing/Enterprise.md` prices them as recurring
obligations, because a named response time is a rota with a contract attached.

---

# Related

| | |
| --- | --- |
| `SLAs.md` | Where commitments become contractual |
| `Incident-Process.md` | What happens when it is not a question but an outage |
| `Cost-Model.md` | Where support staffing enters the arithmetic |
| `08-product`, `10-execution` | Edge cases and flows that generate tickets |

---

> **Concept Note**
>
> The most common support request is a design defect with a queue
> attached.
>
> Name the product change that removes it — or say plainly that this one
> is permanent, and why.
