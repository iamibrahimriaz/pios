---
Title: Events
Module: 09-technology
Section: knowledge/architecture
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Use events where decoupling is needed, and account for what becomes harder.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/architecture/Modules.md
Outputs:
  - Event design within architecture
Related Modules:
  - 12-metrics
  - 13-operations
Tags:
  - Technology
  - Architecture
  - Concept
---

# Events

---

# What It Is

Notifications that something happened, published without knowledge of who consumes them.

The trade is decoupling for traceability:

| Gains | Loses |
| --- | --- |
| A publisher need not know its consumers | The flow is no longer readable in one place |
| New consumers added without changing the publisher | Debugging requires reconstructing what fired |
| Slow work moves out of the request path | Ordering and delivery guarantees must be chosen deliberately |
| A natural fit for audit and metrics | Failure handling becomes per-consumer |

Two distinctions worth keeping straight:

| | Meaning |
| --- | --- |
| **Event** | A fact: this happened. Past tense, no expectation |
| **Command** | An instruction: do this. Has an expected outcome, and a failure that matters |
| **Event sourcing** | Storing events *as* the state — a much larger commitment, and rarely warranted early |

---

# When It Applies

In Move 5 (Choose), where decoupling is genuinely needed. Frequently the same need is met more simply by
`Queues.md`'s background work.

---

# How to Apply It Here

**Name each event as a past-tense fact.** "Note completed" rather than "complete note". The naming enforces the distinction, and
the distinction decides whether failure matters.

**State the delivery guarantee.** At-most-once, at-least-once, exactly-once-in-effect. At-least-once is the realistic default,
which means every consumer must be **idempotent** — the same requirement `api/Endpoints.md` makes of writes.

**Say what happens when a consumer fails.** Retry, dead-letter, alert. This is `08-product`'s failure category applied to
consumers, and silence here becomes silently lost work.

**Use events for audit and metrics deliberately.** `database/Audit.md` and `12-metrics`' event definitions align naturally with
them — but the audit obligation requires guaranteed capture, which constrains the delivery guarantee.

**Keep the payload minimal and versioned.** Consumers depend on the shape, which makes it a contract with the same problems
`api/Versioning.md` describes.

---

# Where It Misleads

**Events are adopted for internal calls that could be direct.** Inside one deployable, a function call is traceable, transactional
and debuggable. Replacing it with an event loses all three and gains nothing unless a consumer is genuinely unknown.

**Ordering is assumed.** Most transports do not guarantee it across partitions, and business logic depending on order will fail
intermittently — the hardest class of bug to reproduce.

**Event sourcing is adopted for its audit benefits.** It is a fundamentally different way of storing state with substantial
consequences for querying and migration. `database/Audit.md` satisfies the obligation far more cheaply.

**Failure becomes invisible.** A consumer that stops working produces no error at the publisher, and nobody notices until the
downstream effect is missed. `scalability/Monitoring.md` has to cover consumer lag explicitly.

**Payload changes break consumers silently.** No compiler catches it. Versioning the payload is the mechanism.

---

# Related

| | |
| --- | --- |
| `Queues.md` | The simpler mechanism for most background work |
| `Modules.md` | The boundaries events cross |
| `12-metrics` | Where events become measurement |
| `scalability/Monitoring.md` | Consumer failure and lag |

---

> **Concept Note**
>
> Past-tense facts, at-least-once delivery, idempotent consumers.
>
> Inside one deployable a function call is traceable and
> transactional — replacing it with an event pays for decoupling you
> may not need.
