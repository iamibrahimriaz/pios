---
Title: Purpose
Module: 11-growth
Section: core
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define why the Growth module exists and what it establishes for the rest of the run.
Audience:
  - AI Agents
  - Founders
Prerequisites:
  - constitution/core
  - 06-business and 08-product gates passed
Outputs:
  - Shared understanding of what this module establishes
Related Modules:
  - 12-metrics
Tags:
  - Growth
  - Purpose
  - Foundation
---

# Purpose

---

# Overview

The product is specified and planned. Nobody knows it exists.

This module decides how the first users are found, what marks the moment they receive value,
what brings them back, and whether anything about the product makes each new user cheaper to
reach than the last.

It runs before launch, which means almost everything in it is a hypothesis. Its value is not in
the forecast — it is in which hypotheses get tested first, and in refusing to present any of
them as results.

---

# Purpose Statement

> Plan how the product reaches, activates and retains users — using what the research
> established about where these people are, and admitting what it did not.

---

# Why This Module Exists

Three failures dominate growth planning.

**Borrowed growth.** Importing the playbook of a product with a different model, segment and
price. A content-marketing-and-free-trial motion applied to something sold to a procurement
committee. It fails not because it is conventional but because the segment is not there and the
buying process does not work that way.

**The funnel drawn as a loop.** A diagram with an arrow curving back to the top, describing a
mechanism whose output never becomes its input. It implies compounding the business does not
have, and it changes decisions about spend, hiring and valuation made by someone reading it in
good faith.

**Confident numbers about nothing that has happened.** Conversion rates, activation rates,
churn. None of them observable for a product with no users, all of them easy to state.

The module's structure — a payback check before anything else, a citation requirement on every
channel, a mechanical closure test, and retention mechanisms traced to requirements — exists to
make each of these visible.

---

# The Judgment This Module Makes

| Output | What it commits |
| --- | --- |
| The growth model | Which motion this product grows by — a product decision, not a marketing one |
| `acquisition_channels` | Where the first money and attention go |
| `onboarding_strategy` | What activation means, and how a user reaches it |
| `retention_model` | What mechanically brings people back, and which requirement delivers it |
| `growth_loops` | Whether anything compounds — stated honestly |
| `expansion_paths` | Whether revenue per customer can grow, or cannot |

---

# Core Objectives

- Choose one growth model, and check it against the price before anything else.
- Cite where the segment was observed for every channel.
- Choose the first channel by learning cost, not by a projected number.
- Define activation as an action that proves value.
- Locate every retention mechanism in a requirement.
- Apply the closure test, and call a funnel a funnel.
- Name the first ten customers.
- Gate spending on what must be true first.

---

# What AI Should Learn Here

- Growth is a property of the product, not an activity performed on it.
- A growth model is a product decision: it demands capabilities, a price and a team.
- A channel is a factual claim about where people are, so it can be evidenced — and must be.
- Acquisition without activation is churn with extra steps.
- "A great product" is not a retention mechanism.
- A funnel is legitimate. A funnel with an arrow drawn back is not.
- CAC and churn arrived unknown from `06-business` and do not become known here.
- Spending to acquire users for an unvalidated problem amplifies the uncertainty.

---

# The Register Problem

Every module in this stage has a way of overreaching. This one's inherits directly from
`07-strategy`'s:

> **Growth laundering.** A business model honestly says "CAC is unknown; here is the range under
> which it works". The growth plan states a CAC per channel, drops the range, and the financial
> model built on top treats the figure as established.

The same happens to churn, to conversion rates, and to activation. Each restatement is a small
increase in confidence, and by the third document the uncertainty has disappeared entirely.

What this module *can* add is **learning cost** — what one test of a channel costs and how long
it takes to answer. That is knowable now, it is what the first channel should be chosen on, and
it is more useful than a projection.

---

# The Payback Check

The first thing this module does, because it decides whether the rest of the plan is possible:

```
margin per user per month × acceptable payback months  =  the CAC ceiling
cost of one unit of the motion ÷ conversions per unit  =  the motion's implied CAC
```

> A £20-a-month product cannot carry a field sales motion. A £50,000 product cannot be
> discovered through a self-serve signup. Neither statement is about execution quality.

Where the implied CAC exceeds the ceiling, the resolution is a regress — to `06-business` for
the price, or `07-strategy` for the segment. The one thing that must not happen is the
conversion assumption rising until the arithmetic passes, which is how an unaffordable motion
reaches a funding decision.

This is the sibling of `09-technology`'s cost check. Both convert an argument into a comparison
of two numbers, and both are the only reliable defense against a plan that reads well.

---

# Scope

**This module covers**

- The growth model and its affordability
- Acquisition channels, their evidence and their learning costs
- Activation: the event, the time, the friction, the switching cost
- Retention mechanisms and their location in the product
- Growth loops, and the honest verdict on compounding
- Onboarding, referral and expansion
- The sequence in which growth work may begin

**This module does not cover**

| Not here | Belongs to |
| --- | --- |
| Price and unit economics | `06-business` — settled |
| What the product does | `08-product` — settled |
| Metric definitions, targets, instrumentation | `12-metrics` |
| Support and customer success operations | `13-operations` |
| Build sequence and milestones | `10-execution` |

---

# Position in the Run

```
06-business ┐
08-product  ┴→ [ 11-growth ] → 12-metrics
```

This module runs before `12-metrics`, which consumes `growth_loops` and `retention_model`. The
activation event defined here becomes the instrumented metric defined there.

---

# What This Module Hands Forward

| Output | Consumed by | Used for |
| --- | --- | --- |
| Activation event | 12 | The activation metric, and its instrumentation |
| `retention_model` | 12 | Retention metrics and their leading indicators |
| `growth_loops` | 12 | Which loop metrics are worth tracking |
| Sequencing table | `09-Roadmap.md` | When growth work starts, and what gates it |
| All outputs | `13-Growth-Plan.md` | The shipped growth artifact — optional in the manifest |

`12-metrics` is the strict consumer. A vague activation event becomes an uncomputable metric,
and the product ships unable to tell whether anyone activated at all.

---

# Milestone Zero, for the Last Time

This is the fourth and final place the mechanism has consequences:

| Module | What it did |
| --- | --- |
| `04-problem` | Declared the shortfall — the sharpest problem is assumed |
| `07-strategy` | Made validation-before-building binding |
| `10-execution` | Sequenced it as the first milestone |
| **`11-growth`** | **Gates acquisition spend on it** |

Where the problem is assumed, no acquisition spend happens before Milestone Zero completes. This
is where an evidence position becomes a money decision — and it is the point of the framework's
insistence on tagging in the first place.

---

# Success Criteria

- A growth model that survives the payback check.
- Every channel citing where the segment was observed.
- A first channel chosen by learning cost.
- An activation event that proves value, with time and steps from `10-execution`.
- Every retention mechanism traced to a requirement.
- An honest compounding verdict: loop, funnel, or none.
- Ten named or specifically profiled first customers.
- Spending gated on validation, where the problem is assumed.

---

# Self Assessment

- Does the model survive the arithmetic?
- Did I cite where the segment is, or where products like this advertise?
- Would my activation event count someone who never came back?
- Does every retention mechanism exist in the MVP?
- Does anything actually compound?
- Am I planning to spend money before knowing the problem is real?

---

> **Purpose Principle**
>
> This module cannot know how the market will respond.
>
> What it can do is put the cheapest question first, and stop the
> plan from claiming an answer it does not have.
