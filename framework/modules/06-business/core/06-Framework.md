---
Title: Framework
Module: 06-business
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the repeatable method for establishing whether a viable business exists.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 05-competition gate passed
  - engine/evidence-policy.md
  - 06-business/core/03-Core-Principles.md
Outputs:
  - business_model
  - pricing_strategy
  - unit_economics
  - go_to_market
  - revenue_model
Related Modules:
  - 07-strategy
  - 11-growth
Tags:
  - Business
  - Framework
  - Method
---

# The Ledger

---

# Overview

This module asks whether a business exists around the solution — not whether the product
is good, and not whether the problem is real. Those were settled earlier.

It is also the module where fabrication is easiest and hardest to detect, because its
output is **arithmetic**. A calculation performed on six guesses produces a precise number
with a decimal point, and precision reads as rigor.

> Arithmetic does not create evidence.

Every entry in the ledger carries a tag. Where most inputs are assumed — which is normal
without primary research — the model is a sensitivity analysis, not a forecast, and must
present itself as one.

---

# Framework Statement

> A business model is six numbers and one question:
> does anyone with the authority to sign believe this is worth more than it costs?

---

# The Six Entries

```
Market Sizing (02) + Competitor Pricing (05) + Segments (03)
   ↓
1. Payer      — who signs, as distinct from who uses
   ↓
2. Value      — what the problem costs them today
   ↓
3. Price      — anchored to value and to competitors, never to instinct
   ↓
4. Economics  — CAC, margin, churn, LTV, payback
   ↓
5. Route      — how the first ten customers are reached
   ↓
6. Test       — does the arithmetic survive its own assumptions?
   ↓
Business Model → 07-strategy, 11-growth, 12-metrics
```

The order matters most between entries 2 and 3. **Value before price.** A price chosen
first and justified afterward is a preference wearing a business model.

---

# Entry 1 — Payer

Identify who signs.

Module 03 established the user. This module establishes the payer, and states explicitly
whether they are the same person. Saying "the same person" is a required answer, not a
reason to skip the question.

Where they differ, three separate things must hold:

| | Question | Fails when |
| --- | --- | --- |
| **Willingness** | Do they want to pay? | The value is invisible to them |
| **Ability** | Can they afford it? | It exceeds the segment's software budget |
| **Authority** | Can they sign? | Approval sits with someone never consulted |

All three are commonly conflated, and a product can fail on any one of them while the
other two are fine. A user who wants it, in an organization that can afford it, still
needs someone with authority — and that person is usually the blocker identified in
module 03.

Then find the **purchase trigger**: the event that makes them buy now rather than later.
Products without a trigger get agreed with and deferred indefinitely.

**Produces:** the payer section of `business_model`

---

# Entry 2 — Value

Establish what the problem costs them today, before considering what to charge.

Module 04 produced cost per occurrence and frequency. Multiply:

```
annual value at stake = cost per occurrence × occurrences per year
```

Then estimate what share of that the product actually captures. A product that removes
half a problem delivers half the value, not all of it.

Two qualifications matter:

**Is the value visible?** An absorbed cost — unpaid overtime, a normalized workaround, a
role that exists to bridge a gap — is real but not felt. It is far harder to sell against
than an invoiced cost of the same size. If module 04 flagged the cost as absorbed, carry
that forward; it changes the sales difficulty, not the value.

**Does the payer bear it?** If the sufferer and the payer differ, value felt by the user
may not translate into willingness by the buyer. Module 03's buyer/blocker mapping is the
input here.

**Produces:** the value basis for pricing

---

# Entry 3 — Price

Price is anchored to two things and never to instinct.

**Anchor one — value.** Price as a fraction of annual value delivered. A product priced
above about a third of the value it delivers has to argue hard; below a tenth it is
leaving money on the table and may signal low value.

**Anchor two — competitors.** From module 05's `pricing_comparison`. Position above, below
or at market, and say why.

**The free anchor.** The status quo is almost always free. A price must be justifiable
against nothing at all:

> Why does someone pay «figure» when what they do today costs zero?

The answer must reference the value in Entry 2 and the switching cost from module 03. If
the price exceeds the value net of switching cost, the model fails here rather than in the
economics.

Then choose the **model** — subscription, usage, license, freemium — and the **unit**.
The unit is a strategic choice: per user rewards small teams, per transaction scales with
customer success, per organization simplifies the sale.

**Produces:** `pricing_strategy`

---

# Entry 4 — Economics

The arithmetic. Every input tagged.

| Input | Typical source |
| --- | --- |
| Price | Entry 3 |
| Gross margin | Cost to serve — infrastructure, support, third-party costs |
| CAC | Channel assumption from Entry 5 |
| Churn | Competitor benchmarks, or assumption |
| Lifetime | `1 / churn` |
| LTV | `price × margin × lifetime` |
| Payback | `CAC / (monthly price × margin)` |

**Cost to serve** must include what module 09 will later have to live inside — the
per-customer infrastructure budget. Where the product includes AI operations, that cost
belongs here, and it has ended products whose per-user cost exceeded their margin.

**Then name the load-bearing assumption:** which single input, wrong by half, changes the
verdict? It is usually CAC or churn, both of which are pure assumption before launch.

**Then run sensitivity.** With mostly-assumed inputs, a point estimate is false precision.
A table showing what happens when CAC doubles and churn doubles is more honest and more
useful.

**Produces:** `unit_economics`

---

# Entry 5 — Route

How the first ten customers are reached.

This is the reality test of the module. A business model with excellent arithmetic and no
answer here is not a business model.

**Name them.** Specific organizations, or profiles specific enough to go and find. "Solo
practices in «region» who posted in «forum» about «problem»" is a route. "Digital
marketing" is not.

Then establish:

| | Why it matters |
| --- | --- |
| Existing access | Any relationship or audience already available changes CAC entirely |
| Channels | Matched to where module 03 said the segment actually is |
| Sales motion | Self-serve, founder-led, inside sales, partner |
| Sales cycle length | Interacts with runway — a nine-month cycle and twelve months of money is a finding |

**Produces:** `go_to_market`

---

# Entry 6 — Test

Does the arithmetic survive?

| Test | Conventional threshold |
| --- | --- |
| LTV : CAC | Above 3 |
| Payback period | Under 12 months |
| Gross margin | Above 60% for software |
| Price as share of value delivered | Under 30% |
| Break-even customer count | Reachable within SOM in year one |

Thresholds are conventions, not laws — a capital-efficient business can work at LTV:CAC
of 2, and a well-funded one can wait five years for payback. State the threshold used and
why.

**Where the model breaks** is the useful output. Which threshold fails first as
assumptions worsen? That is what the operator should watch after launch.

Then answer plainly: **what would have to be true for this to work?**

**Produces:** the viability verdict and `revenue_model`

---

# When This Module Returns to 05-competition

`on_fail: return to 05-competition`. Common triggers:

| Trigger | What it means |
| --- | --- |
| Competitor pricing was never captured | Entry 3 has no anchor |
| Competitors are priced far below any viable price | The market may not support entry |
| No payer can be identified | The segment may not buy software at all |
| The gap serves a segment with no budget | Module 03 or 05 chose wrong |

---

# Common Failures

| Failure | What it looks like | Cost |
| --- | --- | --- |
| Price before value | A number chosen, then justified | The model rationalizes rather than tests |
| Untagged arithmetic | Six guesses producing a precise LTV | False rigor; nobody can tell it is guesswork |
| Payer assumed identical to user | No approval path considered | The sale stalls at a blocker nobody mapped |
| Free incumbent ignored | Price justified only against paid competitors | The hardest objection is unanswered |
| Cost to serve omitted | Margin assumed, not derived | AI or infrastructure costs eat the margin |
| Vague go-to-market | "Content marketing and SEO" | No route to the first customer |
| Point estimate presented as forecast | One LTV number, no sensitivity | Reads as knowledge; is arithmetic on guesses |

---

# Self Assessment

- Did I establish value before choosing a price?
- Did I distinguish willingness, ability and authority to pay?
- Can I justify the price against something that costs nothing?
- Does every input in the economics carry a tag?
- Do I know which assumption the verdict depends on?
- Could I go and find the first ten customers tomorrow?
- Did I state which threshold fails first?

---

> **Framework Principle**
>
> A model built on six assumptions is not wrong because it is assumed.
>
> It is wrong when it presents itself as anything other than assumed.
