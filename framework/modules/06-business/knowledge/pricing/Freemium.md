---
Title: Freemium
Module: 06-business
Section: knowledge/pricing
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Require a conversion trigger and a funded free tier before adopting freemium.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 06-business/knowledge/pricing/Free.md
Outputs:
  - Freemium decision within pricing_strategy
Related Modules:
  - 11-growth
  - 14-ai-systems
Tags:
  - Business
  - Pricing
  - Concept
---

# Freemium

---

# What It Is

A permanently free tier funded by conversion to a paid one.

It works only when three conditions hold together:

| Condition | Fails when |
| --- | --- |
| **The free tier delivers real value** | It is crippled, so nobody stays long enough to convert |
| **A natural trigger forces the upgrade** | The limit never binds, so nobody ever needs to pay |
| **The marginal cost of a free user is near zero** | Every free user costs money — the AI case |

The third condition is why freemium suits storage and collaboration products and suits AI products badly. A free
user running inference has a real per-use cost, and at low conversion rates the free tier is a funded loss.

```
cost of serving all free users < margin from converted users
```

If that inequality does not hold at a realistic conversion rate — low single-digit percentages — freemium is not
available.

---

# When It Applies

In Entry 3 (Price), and only where `Free.md`'s funding question has a real answer. The conversion assumption feeds
`11-growth`'s loop.

---

# How to Apply It Here

**Name the trigger before the tier.** What event makes a free user need to pay? A volume limit they will reach, a
collaborator they must add, a report they need to export, a retention period they exceed. Without a trigger, the
free tier is permanent.

**Check the trigger against real behavior.** `03-user`'s frequency findings say whether the median user reaches
the limit. A cap above typical usage converts nobody; a cap below it converts by frustration, and frustration
converts badly.

**Compute the free tier's cost at scale.** Ten thousand free users at a small per-use cost is a monthly bill.
`14-ai-systems` requires cost per user, and this is where a plausible-sounding free tier becomes visible as an
expense.

**Assume a low conversion rate.** Single-digit percentages are normal. Any model requiring 20% conversion should
state that as the load-bearing assumption it is, and `Financial-Risks.md` should test it.

**Consider a trial instead.** For most professional products a time-boxed trial produces a decision, while
freemium produces a population. `Trials.md` covers the difference.

---

# Where It Misleads

**Freemium is chosen for acquisition and delivers a cost center with no decision point.** Free users are not a
funnel unless something forces a choice. Without a trigger they are an operating expense that grows with success.

**The free tier is weakened to drive conversion, which suppresses both.** A tier too limited to be useful loses
the users before they reach the trigger. The tier must genuinely work — that is the condition, and it is in
tension with the commercial motive.

**Conversion rates from famous consumer products get applied to professional tools.** Different buyer, different
decision, different budget process. A borrowed rate is `[assumption]`, and it is the input the whole model rests
on.

**Support load from free users is not staffed.** They generate questions at close to the rate paying customers
do, and `13-operations` has to answer them. That cost belongs in the inequality above.

**Freemium and a free-forever competitor are confused.** If a competitor's product is free and funded by something
this operator does not have, freemium does not neutralize them — it matches their price and their cost structure
without their funding.

---

# Related

| | |
| --- | --- |
| `Free.md` | Free as competition and as strategy |
| `Trials.md` | The alternative that forces a decision |
| `Upgrade-Path.md` | Whether the paid tier is worth reaching |
| `14-ai-systems` | Marginal cost per user, which decides feasibility |

---

> **Concept Note**
>
> Name the event that forces the upgrade, then check whether the
> median user ever reaches it.
>
> For an AI product, every free user has a bill attached — freemium
> is a decision to pay it.
