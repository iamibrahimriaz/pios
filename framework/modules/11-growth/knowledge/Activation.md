---
Title: Activation
Module: 11-growth
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Name the event that proves a user received value, and put switching cost inside it.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 11-growth/knowledge/Acquisition-Channels.md
Outputs:
  - Activation definition within onboarding_strategy
Related Modules:
  - 10-execution
  - 12-metrics
Tags:
  - Growth
  - Activation
  - Method
---

# Activation

---

# What It Is

The moment a user has actually **received value** — named as a specific event.

`10-execution` established time to first value in steps and minutes. This names the event that marks it, and that event becomes the
metric `12-metrics` builds around.

| Required | Why |
| --- | --- |
| **The specific action** | "Signed up" is not activation. "Completed and saved their first consultation note" is |
| **Why that action proves value** | Otherwise it is a convenient event, chosen because it is easy to log |
| **The biggest friction before it** | The thing worth fixing first |
| **The switching cost paid first** | From `05-competition` — migration and retraining belong *inside* activation, not after it |

And the sentence that governs the whole module's sequencing:

> **Acquisition without activation is churn with extra steps.** A plan that spends on reaching users before the activation path works
> is buying disappointment at retail price.

---

# When It Applies

In Move 3 (Activate), after channels and before retention.

---

# How to Apply It Here

**Choose the event by what it proves, then check it is loggable.** Reversing the order produces a convenient event — a login, a click —
that measures nothing.

**Put migration and training inside the activation path.** `03-user` priced switching across five dimensions. A user who has not moved
their data has not activated, whatever they have clicked.

**Name the single largest friction before the event.** That is the highest-leverage fix in the product, and `10-execution`'s step count
usually identifies it.

**Distinguish activation from onboarding completion.** Finishing a tour is not receiving value. `Onboarding.md` covers the path;
this covers the destination.

**Hand the event to `12-metrics` for proper definition.** It needs a numerator, denominator, window and population — none of which is
settled here.

---

# Where It Misleads

**Sign-up is treated as activation.** It is the beginning of the risk period, not the end. Products with strong sign-up and weak
activation look healthy in acquisition numbers and churn silently.

**Activation is defined as an easily logged event.** A login is not a return, as `12-metrics` puts it, and by the same logic a click
is not value.

**Switching cost is deferred to "later in onboarding".** It is the largest obstacle `05-competition` identified. Placing it after
activation means the activation number counts users who have not really adopted anything.

**Time to first value is estimated rather than counted.** It is routinely three times longer than assumed once sign-up, setup and empty
states are included — which `10-execution` requires counting.

**Acquisition is scaled while activation is broken.** The sequence rule exists for this: no channel test until activation works for the
first ten.

---

# Related

| | |
| --- | --- |
| `Onboarding.md` | The path to the activation event |
| `Retention.md` | What happens after value arrives |
| `10-execution` | Time to first value, in steps and minutes |
| `12-metrics` | Where the event is defined computably |

---

> **Concept Note**
>
> Name the event that proves value, and count migration as part of
> reaching it.
>
> Acquisition without activation is churn with extra steps — bought at
> retail price.
