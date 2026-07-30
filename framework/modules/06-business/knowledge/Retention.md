---
Title: Retention
Module: 06-business
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Treat churn as the assumption it is, and require a mechanism before assuming a lifetime.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 06-business/knowledge/LTV.md
Outputs:
  - Churn assumption within unit_economics
Related Modules:
  - 11-growth
  - 12-metrics
Tags:
  - Business
  - Retention
  - Concept
---

# Retention

---

# What It Is

The rate at which customers keep paying — the input that determines lifetime, and therefore LTV.

This module needs a **number** for the arithmetic. `11-growth` owns the **mechanism** that would justify it, and
`12-metrics` owns its **definition**. Keeping those three separate prevents the most common error here: assuming a
retention rate no mechanism supports.

| Distinction | Why it matters |
| --- | --- |
| **Logo churn** — customers lost | Drives lifetime for a flat-priced product |
| **Revenue churn** — money lost | Diverges from logo churn wherever seats or usage vary |
| **Renewal** — an annual decision | Behaves nothing like monthly churn: one review date, one large risk |

For an annually contracted institutional product, monthly churn is the wrong model entirely — the customer cannot
leave until the renewal, and then may leave all at once.

---

# When It Applies

In Entry 4 (Economics), as the input to lifetime. It is revisited at Entry 6 (Test) as a sensitivity.

---

# How to Apply It Here

**Name the mechanism that would keep them, or assume nothing.** Habit, switching cost, integration, stored data,
contractual term, or a workflow dependency. `03-user`'s frequency finding governs whether habit is even available
as a mechanism.

**Match the model to the billing shape.** Monthly self-serve churns continuously; annual contracts churn at one
date. `Subscription.md` covers the difference and it changes the arithmetic, not just the presentation.

**Use competitor benchmarks with their source and segment.** A churn figure from a consumer product tells you
nothing about a regulated professional tool. If no comparable figure exists, say so and use a range.

**Test the low-frequency case honestly.** A monthly or per-episode product has weak habit and needs a different
mechanism — a trigger, an integration, or stored history that would be lost. Without one, high churn is the
default expectation.

**Distinguish churn from failure to activate.** A customer who never got value and left in month one is an
onboarding problem, not a retention one, and the fixes are different. `11-growth` separates them properly.

---

# Where It Misleads

**Churn is assumed by analogy to companies with nothing in common with this one.** "SaaS churn is around 3%
monthly" averages across markets, price points, contract shapes and buyer types. It is not a benchmark for
anything specific.

**A favorable churn assumption is chosen because LTV needs it.** This is the module's arithmetic run backward, and
it is invisible in the output — the LTV looks derived. `Financial-Risks.md` requires the sensitivity that exposes
it.

**Retention gets confused with usage.** A customer still paying and no longer using the product is retained
today and gone at renewal. `12-metrics` insists a login is not a return, and the same distinction applies to a
renewal.

**Contractual retention is read as satisfaction.** A twelve-month term retains a customer who has already
decided to leave. That is a deferred loss, and it usually arrives with a bad reference attached.

**Negative churn is projected before an upgrade path exists.** Expansion offsetting losses requires something
worth upgrading to, and `pricing/Upgrade-Path.md` says when that is real.

---

# Related

| | |
| --- | --- |
| `LTV.md` | Where churn becomes lifetime |
| `Subscription.md` | How the billing shape changes the model |
| `11-growth` | Where the retention mechanism is required |
| `12-metrics` | Where retention is defined computably |

---

> **Concept Note**
>
> Name what would keep them before assuming how long they stay.
>
> Churn is the least evidenced number in the model and the one LTV
> divides by — a bad guess here is a bad business, silently.
