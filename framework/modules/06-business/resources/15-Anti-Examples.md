---
Title: Anti-Examples
Module: 06-business
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show business models with false rigor, and the reason each fails.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 06-business/core/06-Framework.md
Outputs:
  - Recognition of arithmetic built on hidden assumptions
Related Modules:
  - 07-strategy
  - 11-growth
Tags:
  - Business
  - Anti Examples
  - Reference
---

# Anti-Examples

---

# Overview

> A model built on six assumptions is not wrong because it is assumed. It is wrong when it hides that it is.

Every example below hides it, and each does so in a different way.

---

# Anti-Example 1 — Price Before Value

## ❌ Looks rigorous

```
Pricing: £49/month per practice.

Rationale: competitive with the market (competitors £240–£350/month),
accessible for solo practitioners, and a psychologically comfortable
price point. At 200 practices this yields £117,600 ARR.
```

**Why it fails**

- **The price was chosen, then justified.** No value calculation appears anywhere, which inverts Entries 2 and 3. `06-business` is explicit:
  a price chosen first and justified afterward is a preference wearing a business model.
- **"Psychologically comfortable" is not an anchor.** The three anchors are value, competitors and free.
- **The free incumbent is unanswered.** Competitors charge £240–£350; the paper pad charges nothing, and that is the real comparison.
- **£117,600 assumes 200 practices** with no route, no channel and no conversion assumption behind them.

## ✅ Passes

```
ENTRY 2 — VALUE FIRST
  From 04-problem: 60–120 min/day after-session note time
    [assumption: recollection, unmeasured]
  Occurrences: 8–9 sessions/week × 44 weeks
  Annual time at stake: ~290–580 hours [assumption]

  Capture share: the product addresses in-session capture. It will not
    remove all after-session work. Estimate 50% [assumption — stated,
    because full capture is the standard silent inflation]

  Value visibility: ABSORBED. This is unpaid personal time, not an
    invoiced cost. Real, and much harder to sell against than a bill of
    the same size. Carried forward as a sales-difficulty finding.

  Payer: the GP personally (segment A). They bear the cost and they sign.
    Unusually favorable — but it is their own money, not a budget line.

ENTRY 3 — PRICE
  Anchor 1, value: at 50% capture, ~145–290 hours/year recovered. Even
    valued conservatively as personal time, £600/year is a small fraction.
  Anchor 2, competitors: all paid options are £2,900+/year and priced for
    3+ clinicians. We are not competing with them for this buyer.
  Anchor 3, FREE: the paper pad costs £0.
    Why pay £600 when today costs nothing?
    Because the pad does not close the day — it defers the work.
    Net of switching cost (03-user: must work first time, in a live
    consultation) the margin is thinner than the raw value suggests.

  Price: £50/month, £600/year. Unit: per practice (not per seat — a
    single-handed practice has one clinician, and per-seat pricing would
    penalize the one thing we want, which is a second clinician joining).
```

---

# Anti-Example 2 — Untagged Arithmetic

## ❌ Looks rigorous

```
Unit economics
  Price          £49/month
  Gross margin   85%
  CAC            £180
  Churn          3%/month
  Lifetime       33 months
  LTV            £1,374
  LTV:CAC        7.6
  Payback        4.3 months
Conclusion: strong unit economics. Proceed.
```

**Why it fails**

- **Six inputs, no tags, one precise conclusion.** Margin, CAC and churn are all invented. The arithmetic is correct and the result means
  nothing.
- **85% margin with no cost to serve derived.** For a product with inference cost per consultation, that figure is a guess about the largest
  variable expense.
- **3% monthly churn produces a 33-month lifetime.** At 5% it is 20 months and LTV:CAC falls to 4.6. Neither figure has any evidence, and the
  verdict depends entirely on which one was picked.
- **No load-bearing assumption named, no sensitivity.** A point estimate on assumed inputs is false precision.

## ✅ Passes

```
ENTRY 4 — ECONOMICS   (every input tagged)

  Price            £50/month [decision]
  Cost to serve    DERIVED, not assumed:
                     infrastructure    £2/user/month [inferred: 09-tech]
                     inference         £6–14/user/month [assumption:
                       140 consultations/week × cost/operation — the
                       range is the load-bearing uncertainty]
                     support           £4/user/month [assumption:
                       13-operations forecast]
                   → margin 52%–76%. NOT 85%.
  CAC              £250–£900 [assumption: no channel tested. Includes the
                     operator's own time at a real rate — excluding it
                     produces a CAC that collapses on the first hire]
  Churn            2%–6%/month [assumption: no comparable benchmark for
                     this segment exists]
  Lifetime         capped at 36 months by convention, stated
  LTV              £50 × 0.52..0.76 × 36 = £936–£1,368

  LOAD-BEARING ASSUMPTION: inference cost per user.
    At £6 the margin is 76% and the model works.
    At £14 the margin is 52% and payback exceeds 12 months at high CAC.
    This single input decides the verdict.

  SENSITIVITY
                   CAC £250        CAC £900
    Churn 2%       LTV:CAC 5.5     LTV:CAC 1.5   ← fails
    Churn 6%       LTV:CAC 1.9     LTV:CAC 0.5   ← fails badly

  VERDICT: viable only in the low-CAC, low-churn, low-inference-cost
    corner. Three assumptions must all land favorably.
    What would have to be true: inference under £8/user, CAC under £400,
    churn under 3%.
```

---

# Anti-Example 3 — Payer Assumed Identical to User

## ❌ Looks rigorous

```
Target customer: general practitioners. They experience the problem
directly and will purchase the solution themselves.
```

**Why it fails**

- **Willingness, ability and authority are collapsed into one sentence.** A product can fail on any one while the other two are fine.
- **Ability is unexamined.** A single-handed practice may have no software budget line at all, whatever the value at stake.
- **No purchase trigger.** Products without one get agreed with and deferred indefinitely — the quietest way a good product dies.
- **It is right for segment A and wrong for segment B**, and the sentence does not distinguish them.

## ✅ Passes

```
ENTRY 1 — PAYER   (segment A)
  User      the GP
  Payer     the GP
  Approver  the GP
  Same person: STATED, not skipped.

  Willingness  They bear the cost personally. High. [inferred]
  Ability      UNKNOWN [GAP]. Does a single-handed practice have a
               software budget line, or does this come from personal
               income? Different answers, very different price ceilings.
               → 04-problem T3 tests it.
  Authority    Yes, by definition of segment A.

  PURCHASE TRIGGER — the missing piece
    The problem has existed for years without provoking a purchase.
    Candidate triggers: a locum arriving; an appraisal; a complaint about
    record quality; a partner joining.
    None confirmed. [GAP]
    Without a trigger this is a product people agree with and postpone.

  WHO LOSES IF THIS IS BOUGHT
    Nobody obvious in segment A. In segment B, a practice manager whose
    role includes chasing outstanding documentation.
```

---

# Anti-Example 4 — The Vague Go-To-Market

## ❌ Looks rigorous

```
Go-to-market
  Phase 1: content marketing and SEO to build awareness
  Phase 2: paid acquisition on professional networks
  Phase 3: partnerships with professional bodies
Target: 200 practices in year one.
```

**Why it fails**

- **No route to a single customer.** These are channel categories, not access. The gate requires a path to the first ten, and
  `Customer-Acquisition.md`'s test applies: if it cannot become a list of names in a week, it is not a route.
- **200 practices is asserted.** No contact volume, no conversion, no capacity.
- **The sales motion is absent**, and so is the cycle length — which for institutional buyers interacts with runway.

## ✅ Passes

```
ENTRY 5 — ROUTE

  THE FIRST TEN — named or specifically profiled
    1–4  Four practices in the operator's partner's professional network
         [verified: relationships exist]
         Reached: directly, in person
    5–10 «Named professional association», 60 single-handed members in
         «county» [verified: published membership list]
         Reached: association meeting «date», then direct email

  EXISTING ACCESS: yes — the partner's network. This is why the first four
    are cheap, and it is why their CAC must not be extrapolated.

  SALES MOTION: founder-led. £600/year cannot fund a salesperson, and
    segment A has no procurement, so self-serve is plausible LATER but not
    for the first ten — they need the conversation to establish trust.

  CYCLE LENGTH: unknown, estimated days-to-weeks for segment A (no
    procurement). Segment B would be 6–12 weeks — one reason A was chosen.

  Runway check: 07-strategy/risks/Financial.md. Founder-led at ~4 hours
    per close caps throughput at roughly «n»/month.

  CUSTOMER ELEVEN: no repeatable channel identified. 11-growth must find
    one, and the first ten prove the problem rather than the channel.
```

---

# Anti-Example 5 — Absorbing the Ceiling Breach

## ❌ Looks rigorous

```
Cost to serve is estimated at £12/user/month against a £15 ceiling.
Tight but acceptable; support costs should reduce as documentation
improves and users become self-sufficient.
```

**Why it fails**

- **The breach is absorbed with an optimistic revision.** "Support costs should reduce" is the assumption being adjusted to make the
  arithmetic pass, and it is individually defensible — which is what makes it dangerous.
- **No mechanism for the reduction.** `13-operations` treats support burden as a product signal with a named change; "users become
  self-sufficient" names nothing.
- **The framework's instruction is the opposite.** A breach is a **regress** to price or scope, not a projection.

## ✅ Passes

```
ENTRY 6 — TEST
  True cost to serve (completed by 13-operations, not here):
    infrastructure £2 + inference £6–14 + support £4 + compliance £1
    = £13–£21/user/month
  Ceiling at £50 price and 60% target margin: £20/user/month.

  AT THE HIGH END, THE MODEL BREAKS.

  Not absorbed. Options, for 07-strategy:
    a) Raise the price to £70 — tests against the free incumbent again
    b) Reduce operations per user — 14-ai-systems: fewer inference calls,
       caching identical requests, or a cheaper approach
    c) Narrow scope so support burden falls — 07-strategy
    d) Accept a lower margin and a longer payback, funded — operator input

  Recommendation: (b) first. It is the only option that does not change
    the price, the scope or the funding, and 14-ai-systems has not yet
    run its comparison.

  Threshold to watch: inference cost per user. Above £10, revisit.
```

---

# The Pattern Across All Five

| Failure | How it presents |
| --- | --- |
| Price before value | A number, then a rationale, no value calculation |
| Untagged arithmetic | Six guesses producing one precise LTV |
| Payer assumed identical | Willingness, ability and authority collapsed |
| Vague go-to-market | Channel categories where a route belongs |
| Absorbed breach | An optimistic revision that makes the arithmetic pass |

---

> **Resource Note**
>
> The honest model concludes "viable in one corner, if three assumptions
> land."
>
> The dishonest one concludes "LTV:CAC 7.6 — proceed." Both took the same
> spreadsheet.
