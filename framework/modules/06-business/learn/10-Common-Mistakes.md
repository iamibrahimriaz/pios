---
Title: Common Mistakes
Module: 06-business
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Name the recurring failures in business modeling and what each costs.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 06-business/learn/01-Why-It-Matters.md
Outputs:
  - Recognition of business-stage failure patterns
Related Modules:
  - 11-growth
  - 13-operations
Tags:
  - Business
  - Mistakes
  - Learn
---

# Common Mistakes

---

# Overview

Business models fail in a distinctive way: the arithmetic is correct throughout and the
conclusion is still wrong. Every mistake below is a sound calculation on an input that
was chosen rather than found.

---

# 1. The Payer Never Named

**What it looks like.** The document says "customers" and "users" interchangeably.

**Why it is tempting.** In the researcher's mind there is one person, because module 03
described one person.

**What it costs.** The pricing is designed for whoever the document happened to
describe. If that is the practitioner and the budget belongs to an administrator, the
product is evaluated on criteria it was never built for.

**Instead.** Write three names, even if two are the same: who uses it, who signs, who
can veto. The veto is the one nobody lists, and it decides more deals than either of
the others.

---

# 2. Price Set by Comparison Only

**What it looks like.** "Competitors charge $40, so we will charge $30."

**Why it is tempting.** It is defensible, quick, and feels market-aware.

**What it costs.** It concedes that you are the cheaper version of an existing thing,
and it forfeits the value calculation entirely. If your product saves four hours a
month for someone whose time costs $60 an hour, the comparison price is irrelevant
information about a different product.

**Instead.** Compute value first, then apply the constraint, and record both. When they
conflict, the conflict is the finding — and it is exactly what module 13 will need if
the cost check fails.

---

# 3. Benchmarks Borrowed From Elsewhere

**What it looks like.** "Industry-standard churn is 5% monthly; conversion is 2%."

**Why it is tempting.** These figures exist, are citable, and fill four empty cells.

**What it costs.** Benchmarks aggregate across products with different buyers, channels
and switching costs. Applied to your case they produce a model that is precise and
unconnected. Module 11 then inherits conversion figures from a market that was not
yours — the failure that module names **borrowed growth**.

**Instead.** Use them as a sanity range, tagged `[assumption]`, and never as the input
your conclusion rests on.

---

# 4. Willingness to Pay From a Survey

**What it looks like.** "70% said they would pay $20/month."

**Why it is tempting.** It is the only pre-launch evidence available and it has a number
in it.

**What it costs.** Stated willingness to pay overstates real willingness reliably and
substantially. Worse, it looks like evidence rather than inference, so it enters the
model untagged and is inherited as verified.

**Instead.** Tag it as what it is. The stronger signal is what they pay today for the
workaround — in money or in hours — which module 03 already documented.

---

# 5. The Sensitivity That Varies Everything by 20%

**What it looks like.** A tidy table moving each input up and down by the same
percentage.

**Why it is tempting.** It looks rigorous and produces a reassuring range.

**What it costs.** It hides the real exposure. One input is usually far less certain
than the others — often CAC, which can be wrong by a factor of five — and moving it 20%
understates that while appearing to have addressed it.

**Instead.** One input, its genuine plausible range, and the point at which the answer
changes.

---

# 6. The Founder's Time Priced at Zero

**What it looks like.** A cost model containing infrastructure and nothing else.

**Why it is tempting.** It is not an invoice, and early on it feels like enthusiasm
rather than cost.

**What it costs.** This is the single most common reason module 13's cost check passes
when it should fail. In service-delivered and high-touch products, the operator's hours
are the dominant cost — and a model omitting them shows a comfortable margin on a
product nobody can afford to run.

**Instead.** Put a real hourly rate on it. If the answer is that the business does not
work at that rate, that is the finding, and it arrives now rather than in month
fourteen.

---

# 7. LTV Computed From Assumed Churn

**What it looks like.** "LTV is $1,200, so we can spend $400 to acquire."

**Why it is tempting.** The ratio is a familiar decision rule.

**What it costs.** LTV is churn in disguise, and churn is unknowable pre-launch. A
small error in an assumed churn rate produces a large error in LTV, which then licenses
a spending decision. The ratio's authority is entirely borrowed from a number nobody
has.

**Instead.** Use a payback ceiling. "We can spend what a customer returns in n months"
is a decision rule built on price and gross margin, both of which you at least control.

---

# 8. The Path to Ten Customers Described as a Channel

**What it looks like.** "We will acquire early customers through content marketing and
partnerships."

**Why it is tempting.** It is what the growth plan will say later, so it feels
consistent.

**What it costs.** The first ten customers never come from a channel. They come from
named people. A plan that cannot name them has not yet been tested against reality, and
module 11 will build a funnel on a foundation that was never laid.

**Instead.** Name the first three. If you cannot, that is a finding about reachability
that belongs in the document.

---

# The Pattern

| Mistake | Underlying move |
| --- | --- |
| Payer unnamed | Assuming one person |
| Price by comparison | Skipping the value calculation |
| Borrowed benchmarks | Filling a cell with a citable number |
| Survey willingness | Preferring an available number to a real signal |
| Uniform sensitivity | Rigor as performance |
| Time priced at zero | Omitting the cost with no invoice |
| LTV from assumed churn | Building a decision rule on an unknowable input |
| Channel instead of names | Deferring the hard part to module 11 |

Six of the eight produce a model that closes comfortably. That is the characteristic
failure here — not bad arithmetic, but arithmetic performed on numbers selected to make
it work.

---

> **Mistakes Principle**
>
> A business model that works on the first attempt has usually been assembled
> backwards.
>
> The useful version tells you which single number has to be true, and how far from it
> you can afford to be.
