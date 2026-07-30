---
Title: Retention
Module: 11-growth
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Name the mechanism that holds users, and trace it to the requirement that delivers it.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 11-growth/knowledge/Activation.md
Outputs:
  - retention_model
Related Modules:
  - 06-business
  - 08-product
Tags:
  - Growth
  - Retention
  - Method
---

# Retention

---

# What It Is

The **mechanism** that brings users back — where `06-business/knowledge/Retention.md` needed a churn number for arithmetic, this
supplies the reason the number might be defensible.

> "A great product" is not a retention mechanism. These are:

| Mechanism | How it holds |
| --- | --- |
| **Accumulated data** | Leaving means losing history |
| **Habit** | The product is inside a routine |
| **Workflow dependency** | Colleagues or processes now assume it |
| **Network** | Other people are here |
| **Switching cost** | Migration back is expensive |

And the check that makes it real:

> **Every mechanism must name the requirement that delivers it.** A retention mechanism with no requirement behind it is a hope, and
> this check is mechanical — the same traceability discipline modules 08 and 09 apply.

Then the timing question: does the mechanism arrive in the MVP, or in deferred scope? If it is deferred, **retention is unproven at
launch**, and the roadmap must say so rather than discovering it from a churn number.

---

# When It Applies

In Move 4 (Retain), after activation is defined.

---

# How to Apply It Here

**Point at a requirement identifier per mechanism.** `08-product/knowledge/KPIs.md` asks this module's question from the other side —
which requirement delivers each retention mechanism.

**Check habit against `03-user`'s frequency.** Habit is only available where the job recurs often. For a monthly or per-episode job it
is not a mechanism, and something else — a trigger, an integration, stored history — has to carry it.

**Say which mechanisms exist at launch and which do not.** Accumulated data begins accumulating on day one and is weak in month one.
That is honest and it belongs in the model.

**Record the observable behavior that precedes leaving.** `Churn.md` covers this: it is actionable in a way a churn percentage is not.

**Leave the churn number to `06-business`.** This module does not make it knowable. It supplies the mechanism; module 06 keeps the
sensitivity table.

---

# Where It Misleads

**Product quality is offered as retention.** Quality is necessary and holds nobody. Users leave good products constantly, because
nothing in them made leaving costly or forgetting them difficult.

**A mechanism is claimed without a requirement.** "Users will build up history" is a mechanism if something stores and surfaces it, and
a hope if nothing does.

**Retention is assumed to exist because switching cost does.** Switching cost holds a customer who wants to leave, which shows up at
renewal with a bad reference attached. `06-business` makes the same distinction between willing and resentful retention.

**The mechanism is in a later release.** Then launch retention rests on nothing, and the churn observed is not evidence about the
eventual product — a distinction the roadmap must make.

**Engagement features are added as retention.** An unrequested reason to return is `14-ai-systems`' capability theater in another form.
Retention comes from the job recurring, not from notifications about it.

---

# Related

| | |
| --- | --- |
| `Churn.md` | The behavior that precedes leaving |
| `Growth-Loops.md` | Whether retention compounds |
| `06-business` `Retention.md` | Churn as an arithmetic input |
| `08-product` | The requirement each mechanism traces to |

---

> **Concept Note**
>
> Name the mechanism, then name the requirement that builds it.
>
> If the mechanism ships in a later release, retention is unproven at
> launch — and the churn you observe is about a different product.
