---
Title: Queues
Module: 09-technology
Section: knowledge/architecture
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Move slow work out of the request path, and specify how the user learns the outcome.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/architecture/Events.md
Outputs:
  - Asynchronous design within architecture
Related Modules:
  - 08-product
  - 14-ai-systems
Tags:
  - Technology
  - Architecture
  - Concept
---

# Queues

---

# What It Is

Work accepted now and performed shortly afterward — as an **architectural decision**, because it changes what the user sees.

`scalability/Queues.md` covers queues as a load-smoothing response. This file is about the design consequence:

> The moment work becomes asynchronous, the user no longer receives the result. They receive an acknowledgment — and how they
> learn the outcome becomes a product requirement.

| What must be specified | Because |
| --- | --- |
| What the user sees immediately | An acknowledgment with an accurate expectation |
| How they learn it finished | Polling, notification, the next screen — an `08-product` behavior |
| How they learn it **failed** | The most commonly omitted case |
| Whether they can retry, and whether that duplicates | Idempotency, per `api/Endpoints.md` |
| What happens to work still queued during a deployment | `09-technology/knowledge/Deployment.md` |

Typical candidates: sending mail, generating documents, importing data, and **model inference** — which for `14-ai-systems` is
frequently the case that forces this decision, since latency exceeds the interaction budget.

---

# When It Applies

In Move 5 (Choose), and it produces requirements that belong back in `08-product`.

---

# How to Apply It Here

**Hand the notification behavior back to `08-product`.** Asynchronous processing creates user-visible states — pending, failed,
complete — and they need specified behavior and acceptance criteria.

**Make every job idempotent.** At-least-once delivery is the practical guarantee, so a job must tolerate running twice without
duplicating its effect.

**Specify the failure path with an owner.** Retries with backoff, a limit, then a dead-letter destination that someone actually
looks at. `13-operations` needs the runbook, and an unwatched dead-letter queue is silent data loss.

**Keep the queue inside one deployable where possible.** A worker process in the same codebase is still one deployable, and it
avoids the cost floor `Microservices.md` describes.

**Use it for AI latency deliberately, not reluctantly.** Drafting in the background and presenting the result later is often a
better interaction than a spinner — a `10-execution` flow decision informed by `09-technology/knowledge/Performance.md`'s budget.

---

# Where It Misleads

**The user-facing consequence is treated as an implementation detail.** A job queue changes the interaction. Without a specified
pending and failed state, the interface shows nothing and the user assumes it worked.

**Failure notification is omitted.** The job fails, the queue retries, the retries exhaust, and the user is never told. This is
the most common way asynchronous work loses data invisibly.

**Ordering is assumed.** Parallel workers process out of order. Anything order-dependent needs partitioning or serialization,
stated explicitly.

**Queue depth is not monitored.** A queue growing faster than it drains is a failure that looks like normal operation until it is
hours behind. `scalability/Monitoring.md` covers it.

**In-flight work is lost on deploy.** Graceful shutdown and job durability are design decisions, and the default in many setups
is to lose whatever was running.

---

# Related

| | |
| --- | --- |
| `Events.md` | Notifications, by contrast with work items |
| `scalability/Queues.md` | Queues as a load response |
| `08-product` | Where pending and failed states are specified |
| `14-ai-systems` | Where inference latency forces this |

---

> **Concept Note**
>
> Going asynchronous replaces a result with a promise — and the promise
> needs a way to be kept, and a way to be broken visibly.
>
> The failure notification is the part that gets left out, and it is how
> work disappears silently.
