---
Title: Why It Matters
Module: 11-growth
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Explain why growth planning is constrained by user behavior and arithmetic rather than by tactics.
Audience:
  - Product Managers
  - Founders
  - Marketers
Prerequisites:
  - 11-growth/README.md
Outputs:
  - Understanding of why the growth stage exists
Related Modules:
  - 03-user
  - 06-business
  - 12-metrics
Tags:
  - Growth
  - Channels
  - Learn
---

# Why It Matters

---

# Overview

Growth is the part of a product plan most likely to be written from a list of tactics.
The tactics are real and they work somewhere. Whether they work here depends on three
things established in earlier modules, and this is where those three collide.

---

# Why the Channel Question Is a User Question

The gate requires channels matched to where the named segments actually are. That phrasing
is doing work: **actually**, and **named**.

A channel plan is not a list of channels that exist. It is a claim about where a specific
group of people already pay attention:

| Question | What it settles |
| --- | --- |
| Where does this segment already go for this kind of thing? | Whether the channel reaches them at all |
| Who do they trust on it? | Whether reaching them accomplishes anything |
| What are they doing when they are there? | Whether they can act |
| Is the payer there, or only the user? | Whether the message can even be aimed correctly |

The last row is the one that gets missed. Module 06 distinguished the payer from the
user for exactly this reason — a channel that reaches enthusiastic practitioners and
never reaches the person with the budget produces demand that cannot convert.

---

# Why Most Loops Are Funnels

A growth loop is a mechanism whose output becomes its own input. Users produce something
that brings more users, and the cycle compounds without proportional spending.

> **The closure test.** Trace the arrow. Does the output actually re-enter as an input?

Most diagrams labeled "loop" fail this:

```
Not a loop:  users sign up → use the product → tell colleagues → more users
             (the third step is a hope, not a mechanism)
Closed:      each note produced creates a shareable artifact that names the
             producer, and recipients are people with the same job
```

The difference is whether something in the product's normal operation produces the
input, or whether it depends on users choosing to do promotional work.

Calling a funnel a funnel is not a failure. Funnels are how most successful businesses
grow. The worked example concludes `compounding: FUNNEL` and is a better plan for
saying so — because a funnel's economics are entirely about the payback ceiling, and
knowing that focuses the whole plan on one number.

---

# Why Borrowed Growth Fails

Published conversion rates and channel benchmarks are real measurements. They come from
a market with:

- A different switching cost
- A different buyer
- A different alternative, including a different status quo
- A different level of category awareness

Module 03 measured the switching cost for *your* users. If it is high — data migration,
retraining, contractual timing, perceived risk — then a conversion rate measured where
it was low is not conservative or aggressive, it is unrelated.

This is the failure this module names, and it is particularly damaging because the
borrowed numbers feed the payback check. A plan can pass the arithmetic on figures that
were never about this product.

---

# Why Time to First Value Is Measured in Minutes

The gate requires it stated as a number. That precision exists because the alternative —
"quickly," "immediately," "in a single session" — cannot be designed against.

Time to first value is the interval between a user arriving and a user getting something
they would miss. Every minute in it is a place they can leave, and the components are all
things module 10 designed:

| Component | Where it was decided |
| --- | --- |
| Account creation | `10-execution` flow |
| The cold-start screen | `10-execution`, and it is the most common stall |
| Data entry before anything works | `08-product` requirements |
| Waiting for a process to complete | `09-technology` architecture |

Which means a bad number here is usually not a growth problem. It is a product problem
this module is the first to measure.

---

# Why the Payback Check Runs Here

Module 06 set a payback ceiling. This module produces the implied CAC — what the channel
plan actually costs per acquired customer.

```
06-business  what a customer returns in n months
    ↓
11-growth    what the plan implies acquisition costs
    ↓
  breach → REGRESS to 06-business (price) or 07-strategy (scope)
```

This is the second of three arithmetic checks. Like the others, the rule is that a breach
regresses rather than being absorbed — and the absorption here has a characteristic
form: assuming the conversion rate improves with optimization. It always might. It has
not yet.

---

# Why Retention Comes Before Acquisition

The gate requires a retention mechanism identified, not assumed. The ordering is
deliberate: acquisition into a product people leave is a way of spending money to
discover the retention problem more expensively.

A retention *mechanism* is something structural — accumulated data that would be lost,
a workflow other people depend on, a record that has to stay in one place. "Users will
keep using it because it is useful" is an assumption, and it is the one most often wrong.

---

# What Skipping This Stage Costs

| Skipped | Surfaces as |
| --- | --- |
| Real channel matching | Spend against people who were never there |
| The closure test | A plan that assumes compounding it will not get |
| Own conversion figures | Arithmetic that passes on somebody else's market |
| Time to first value as a number | A stall nobody located |
| The payback check | Acquisition that costs more than it returns, discovered by running out of money |
| A retention mechanism | Growth that leaks faster than it fills |

---

# What This Module Does Not Do

It does not set the price — module 06 did. It does not define metrics — module 12 does,
using this module's loops and retention model. It does not build the onboarding flow;
module 10 designed it, and this module measures how long it takes.

---

> **Why It Matters Principle**
>
> Growth plans are the easiest place in the framework to be confidently wrong, because
> nothing in them can be tested without spending money.
>
> The three defenses are all arithmetic: does the loop close, what does the plan imply
> per customer, and how many minutes until someone gets something.
