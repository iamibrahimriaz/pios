---
Title: Framework
Module: 11-growth
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the method by which a product's growth is planned from research rather than convention.
Audience:
  - AI Agents
  - Founders
Prerequisites:
  - 11-growth/core/03-Core-Principles.md
  - 06-business and 08-product gates passed
Outputs:
  - acquisition_channels
  - growth_loops
  - retention_model
  - onboarding_strategy
  - expansion_paths
Related Modules:
  - 12-metrics
Tags:
  - Growth
  - Framework
  - Method
---

# Framework — The Loop

---

# The Method

> Growth is a property of the product, not an activity performed on it.
>
> This module's job is to say which property this product actually has — and to be
> honest when the answer is "none yet".

Six moves. The first two decide whether the plan is possible at all; the last four decide
whether it compounds.

```
   Model  →  Locate  →  Activate  →  Retain  →  Loop  →  Name
     │        │          │           │          │        │
   motion   channels   value      staying    compounding first ten
```

| Move | Question | Produces |
| --- | --- | --- |
| 1. Model | How does this product fundamentally grow? | The growth model, and the payback check |
| 2. Locate | Where is this segment, actually? | `acquisition_channels` |
| 3. Activate | When has a user received value? | `onboarding_strategy` |
| 4. Retain | What mechanically brings them back? | `retention_model` |
| 5. Loop | Does anything compound? | `growth_loops` |
| 6. Name | Who are the first ten? | The first-ten list, and `expansion_paths` |

---

# Move 1 — Model

**Choose one growth model, and check it against the price.**

These are not marketing styles. They demand different products, different prices and
different teams:

| Model | Requires | Breaks when |
| --- | --- | --- |
| Sales-led | A price that funds conversations | The price is too low to pay for a human |
| Product-led | A product usable without help | The product needs configuration or training |
| Community-led | A segment that already gathers | The users are isolated or competitive |
| Marketplace | Two sides, and a plan for the cold start | One side is assumed |
| Referral | Users who benefit from other users joining | Users are competitors |

## The Payback Check

The arithmetic that decides whether the chosen model is possible:

```
Gross margin per user per month  [from 06-business]
× acceptable payback period in months  [operator input, or a stated assumption]
= the CAC ceiling

Cost of one unit of the motion  [cited]
÷ conversions per unit  [assumption]
= the motion's implied CAC
```

If the second exceeds the first, the model is not affordable at this price — and the
resolution is a **regress** to `06-business` for the price or `07-strategy` for the segment,
not optimism about conversion rates.

This is the module's arithmetic check, and it parallels `09-technology`'s cost check. Both
convert a debate into a comparison of two numbers, and both are the only reliable defense
against a plan that reads well.

> A £20-a-month product cannot carry a field sales motion. A £50,000 product cannot be
> discovered through a self-serve signup. Neither statement is a matter of execution
> quality.

---

# Move 2 — Locate

**Find where the segment already is. Do not choose where to market.**

Every channel row must cite where the segment was **observed** — `03-user`'s research,
`02-market`'s trade sources, `05-competition`'s channel analysis. A channel with no citation
was chosen by convention.

> **Borrowed growth** is this module's characteristic failure: importing the playbook of a
> product with a different model, segment and price. A content-marketing-and-free-trial motion
> applied to something sold to hospital procurement. It is not wrong because it is
> unfashionable — it is wrong because the segment is not there and the buying process does not
> work that way.

**Choose the first channel by learning cost, not by projected CAC.**

Projected CAC before launch is an assumption — `06-business` already established that and
handled it with a sensitivity table rather than a figure. What *is* knowable is the cost of
finding out: what one test of this channel costs, and how quickly it produces an answer.

| Compare channels on | Not on |
| --- | --- |
| Cost of one test | Projected CAC |
| Time to a usable answer | Modeled volume |
| Whether the segment is evidenced there | Whether the channel is well regarded |

**Name the channels deliberately not used**, and the ones that cannot be evidenced. The
second group are open questions, not plans.

---

# Move 3 — Activate

**Define the moment a user has received value.**

`10-execution` established time to first value in steps and minutes. This move names the
**event** that marks it, and that event becomes the metric `12-metrics` builds around.

| Required | Why |
| --- | --- |
| The specific action | "Signed up" is not activation. "Completed and saved their first consultation note" is |
| Why that action proves value | Otherwise it is a convenient event, chosen because it is easy to log |
| The biggest friction before it | The thing worth fixing first |
| The switching cost paid first | From `05-competition` — migration and retraining belong *inside* activation, not after it |

**Acquisition without activation is churn with extra steps.** A plan that spends on reaching
users before the activation path works is buying disappointment at retail price.

---

# Move 4 — Retain

**State the mechanism, and locate it in the product.**

"A great product" is not a retention mechanism. These are:

| Mechanism | How it holds |
| --- | --- |
| Accumulated data | Leaving means losing history |
| Habit | The product is inside a routine |
| Workflow dependency | Colleagues or processes now assume it |
| Network | Other people are here |
| Switching cost | Migration back is expensive |

**Every mechanism must name the requirement that delivers it.** A retention mechanism with no
requirement behind it is a hope, and this check is mechanical — the same traceability
discipline modules 08 and 09 apply.

**Ask whether retention depends on the MVP or on deferred scope.** If the mechanism arrives in
a later release, retention is unproven at launch, and the roadmap needs to say so rather than
discovering it from a churn number.

**Churn stays an assumption.** `06-business` could not know it and used sensitivity; this
module does not make it knowable. What can be established is the **observable behavior that
precedes leaving** — that is actionable, and a churn percentage is not.

---

# Move 5 — Loop

**Describe what compounds, and be honest when nothing does.**

> **The closure test.** Does the output become the next input?

If yes, it is a loop: each turn makes the next turn cheaper or bigger. If no, it is a funnel:
output scales with input, linearly, forever.

| Loop | Funnel |
| --- | --- |
| Users produce something that attracts users | Spend produces users |
| Data improves the product, which attracts users | Content attracts users while it is published |
| Each clinic invites colleagues in the same clinic | Each conference produces leads |

A funnel is entirely legitimate. Many good businesses grow through one. **A funnel with an
arrow drawn back to the top is not** — that diagram implies compounding the business does not
have, and it changes how the operator thinks about spend, hiring and valuation.

Per loop: cycle time, what makes each turn bigger, where it leaks, and the evidence it works
— which before launch is usually "none, this is a hypothesis". Saying that is more useful than
a diagram implying otherwise.

---

# Move 6 — Name

**The first ten customers, named or specifically profiled.**

"Marketing" is not a plan for the first ten, and the first ten are where a product either
becomes real or does not.

| Required per row | |
| --- | --- |
| Who | A name where possible, a specific profile otherwise |
| How reached | A specific route, not a channel category |
| Why they would say yes | Their reason, not the product's features |
| What would make them say no | From `05-competition`'s status quo analysis |

**Where the sharpest problem is assumed, these ten are the validation sample** — Milestone
Zero's population, not a sales pipeline. Naming them as such is what keeps the first
conversations honest: they are being asked whether the problem is real, not being sold to.

---

# The Sequence Rule

Growth spend before activation works amplifies a product nobody stays with.

| Stage | Do not start until |
| --- | --- |
| First ten customers | The MVP completes the core job end to end |
| First channel test | Activation works for the first ten |
| Channel scale | Retention holds past a stated period |

**Where the problem is assumed: no acquisition spend before Milestone Zero completes.** This
is where the framework's evidence position turns into a spending decision — the fourth and
last place Milestone Zero has consequences, after `04-problem` declared it, `07-strategy` made
it binding, and `10-execution` sequenced it first.

---

# Why the Order Is What It Is

| If you… | You get |
| --- | --- |
| Locate before choosing the model | Channels that suit no particular motion |
| Skip the payback check | A motion the price cannot fund, discovered after hiring |
| Plan acquisition before activation | Spend on a path that loses people |
| Describe loops before retention | Compounding assumed on top of churn |
| Name the first ten last | The plan never becomes concrete |

---

# What This Module Does Not Decide

| Not here | Belongs to |
| --- | --- |
| Price and unit economics | `06-business` — settled |
| What the product does | `08-product` — settled |
| Metric definitions, targets, instrumentation | `12-metrics` |
| Support and success operations | `13-operations` |
| Build sequence | `10-execution` |

---

# Self Assessment

- Does the chosen model survive the payback check?
- Does every channel cite where the segment was observed?
- Did I choose the first channel by learning cost or by a projected number?
- Is the activation event a specific action, and does it prove value?
- Does every retention mechanism name a requirement?
- Does anything actually close, or have I drawn an arrow back on a funnel?
- Are the first ten named?
- Does the plan forbid spending before validation, where the problem is assumed?

---

> **Framework Principle**
>
> This module runs before there are any users, which means almost
> everything in it is a hypothesis.
>
> Its value is in which hypotheses it commits to testing first,
> and in refusing to present any of them as results.
