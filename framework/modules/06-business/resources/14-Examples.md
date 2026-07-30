---
Title: Examples
Module: 06-business
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show a business model whose verdict is conditional and whose conditions are named.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 06-business/core/06-Framework.md
Outputs:
  - A reference business model
Related Modules:
  - 07-strategy
  - 13-operations
Tags:
  - Business
  - Examples
  - Reference
---

# Examples

---

# Overview

The run continues. The passing model reaches a **conditional verdict with named thresholds** rather than a favorable one — which is what
lets `07-strategy` sequence around it and `13-operations` complete the arithmetic later.

---

# The Worked Business Model

```
BUSINESS MODEL — «Consultation notes for single-handed practices»

ENTRY 1 — PAYER   (segment A)
  User / payer / approver: the GP. Same person — stated, not skipped.
  Willingness  high [inferred: they bear the cost personally]
  Ability      UNKNOWN [GAP] — practice budget line, or personal income?
               → 04-problem T3 tests it
  Authority    yes, by definition of segment A
  Purchase trigger  NONE CONFIRMED [GAP]
               Candidates: a locum arriving, an appraisal, a complaint
               about record quality, a partner joining.
               Without one, this is agreed with and postponed.

ENTRY 2 — VALUE   (before price)
  From 04-problem: 60–120 min/day after-session notes [assumption]
  × 8–9 sessions/week × 44 weeks = ~290–580 hours/year [assumption]
  Capture share: 50% [assumption — the product addresses in-session
    capture; it will not remove all after-session work]
  → ~145–290 hours/year recovered

  Value visibility: ABSORBED. Unpaid personal time, not an invoiced cost.
    Real, and harder to sell against than a bill of the same size.
  Payer bears it: yes. Favorable — but it is personal money.

ENTRY 3 — PRICE
  Anchor 1 — value: £600/year against 145–290 hours. Small fraction.
  Anchor 2 — competitors: all paid options £2,900+/year, priced for 3+
    clinicians [05-competition, dated]. Not competing for this buyer.
  Anchor 3 — FREE: the paper pad costs £0.
    Answer: the pad defers the work rather than closing the day.
    Net of switching cost (must work first time, live, unrehearsed) the
    margin over free is thinner than the raw value implies.

  Price £50/month · £600/year
  Unit  per practice, not per seat.
    Reason: a single-handed practice has one clinician, and per-seat
    pricing would penalize the one growth we want — a second clinician
    joining. 06-business/knowledge/pricing/Pricing-Models.md.
  Model subscription. Value recurs — the job is daily.

ENTRY 4 — ECONOMICS   (every input tagged)
  Cost to serve, DERIVED:
    infrastructure  £2/user/month [inferred: 09-technology]
    inference       £6–14/user/month [assumption: 140 consultations/week
                    × cost per operation — see 14-ai-systems]
    support         £4/user/month [assumption: 13-operations forecast]
    compliance      £1/user/month [assumption: 13-operations schedule]
  → margin 52%–76%

  CAC    £250–£900 [assumption: no channel tested; includes the operator's
         own time at a real rate]
  Churn  2%–6%/month [assumption: no comparable benchmark exists]
  Lifetime capped at 36 months by convention, stated
  LTV    £936–£1,368

  LOAD-BEARING ASSUMPTION: inference cost per user.
    £6  → margin 76%, model works across most CAC/churn combinations
    £14 → margin 52%, payback exceeds 12 months at high CAC

  SENSITIVITY
                 CAC £250      CAC £900
    Churn 2%     5.5           1.5   ← fails
    Churn 6%     1.9           0.5   ← fails badly

ENTRY 5 — ROUTE
  FIRST TEN
    1–4   four practices in the operator's partner's network
          [verified: relationships exist] — reached directly
    5–10  «named association», 60 single-handed members in «county»
          [verified: membership list] — association meeting, then email
  Existing access: yes. Which is why 1–4 are cheap and non-extrapolable.
  Motion: founder-led. £600/year cannot fund a salesperson; segment A has
    no procurement, so self-serve is plausible later, not for the first ten.
  Cycle: days-to-weeks for A (no procurement). B would be 6–12 weeks —
    one reason A was chosen.
  Customer eleven: no repeatable channel yet. 11-growth owns it.

ENTRY 6 — TEST
  LTV:CAC        1.5–5.5 depending on three assumptions
  Payback        4–18 months
  Gross margin   52%–76% (below the 60% convention at the high cost end)
  Price/value    small fraction — comfortable
  Break-even     ~«n» practices. Inside SOM? SOM was 24 in year one, so
                 break-even is NOT reachable in year one. Stated.

  VERDICT: CONDITIONALLY VIABLE.
  What would have to be true:
    1. Inference cost under £8/user/month  → 14-ai-systems
    2. CAC under £400 for customer eleven onward → 11-growth
    3. Churn under 3%/month → requires a retention mechanism, 11-growth

  Which threshold fails first as assumptions worsen: gross margin, via
    inference cost. Watch that number.

  Note for 13-operations: this ceiling is £20/user/month. Your Move 6
    completes the arithmetic with support and compliance actuals.
```

---

# Example 1 — Value Before Price

## ❌ Poor

```
£49/month is accessible and competitive with the market.
```

## ✅ Good

```
Value at stake: 145–290 hours/year recovered at 50% capture [assumption].
Price £600/year is a small fraction of that.
Justified against £0 (the paper pad), net of a switching cost that
requires it to work first time in a live consultation.
```

**Why.** The ratio is the justification, and it travels better than the number — it also stays correctable when the value estimate changes.

---

# Example 2 — Deriving the Margin

## ❌ Poor

```
Gross margin: 85% (typical for SaaS).
```

## ✅ Good

```
infrastructure £2 + inference £6–14 + support £4 + compliance £1
= margin 52%–76%. The inference range is the load-bearing uncertainty.
```

**Why.** For an AI product, inference is frequently the dominant variable cost and the one that rises with engagement. An assumed margin
hides the largest expense in the model.

---

# Example 3 — Naming the Assumption Before Testing It

## ❌ Poor

```
Sensitivity: if churn increases to 4%, LTV falls to £1,030. Still healthy.
```

## ✅ Good

```
LOAD-BEARING: inference cost per user. Named before the table was built.
The table then shows the model failing in three of four corners.
Threshold to watch: £10/user/month.
```

**Why.** Naming it first is the defense against adjusting it until the verdict passes. Every such adjustment is individually defensible, which
is why the order matters.

---

# Example 4 — A Route Someone Could Walk Tomorrow

## ❌ Poor

```
Target: solo GPs via professional networks and content marketing.
```

## ✅ Good

```
1–4   four practices in «person»'s network — reached in person
5–10  60 single-handed members of «named association» in «county»
      [verified: published membership list] — meeting «date», then email
```

**Why.** This is a list of names by the end of the week. It also states honestly that the first four came through existing access and cannot
be used to project CAC.

---

# Example 5 — A Conditional Verdict

## ❌ Poor

```
Unit economics are strong. Proceed.
```

## ✅ Good

```
CONDITIONALLY VIABLE. Three thresholds must hold:
inference < £8, CAC < £400, churn < 3%.
First to fail: gross margin, via inference cost.
Break-even is not reachable within year one SOM. Stated.
```

**Why.** This is a watch list rather than a conclusion, and it is what `07-strategy` needs at the human checkpoint — including the
uncomfortable fact about break-even.

---

> **Resource Note**
>
> The passing model says "viable if three things land, and here is which
> one to watch."
>
> That is more useful than a favorable verdict, and it is the only version
> that survives module 13 completing the arithmetic.
