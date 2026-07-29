---
Title: Research Methodology
Module: 06-business
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define how business-model evidence is sourced, and how to model honestly when it cannot be.
Audience:
  - AI Agents
  - Researchers
  - Founders
Prerequisites:
  - engine/evidence-policy.md
  - 06-business/core/06-Framework.md
Outputs:
  - Evidence-tagged business inputs
  - unit_economics with sensitivity
Related Modules:
  - 05-competition
  - 11-growth
Tags:
  - Business
  - Research
  - Methodology
---

# Research Methodology

---

# Overview

This module produces the most convincing-looking output in the framework, and the least
verifiable.

A unit economics table is arithmetic. Arithmetic looks like rigor. But `LTV:CAC = 4.2`
derived from an assumed price, an assumed margin, an assumed CAC and an assumed churn rate
is a guess carried to one decimal place.

The methodology here is therefore mostly about **honesty discipline**: which inputs can be
established, which cannot, and how to present a model whose inputs are mostly assumed.

---

# Methodology Statement

> Arithmetic does not create evidence.
>
> A calculation is exactly as reliable as its least reliable input, however many
> decimal places it produces.

---

# What Can Be Established

| Input | Source | Achievable tag |
| --- | --- | --- |
| Competitor pricing | Module 05 `pricing_comparison` | `[verified]` |
| Market price range | Module 05 | `[verified]` |
| Value at stake | Module 04 cost figures | Inherits module 04's standing |
| Segment budget norms | Industry surveys, professional body data | `[verified]` if sourced |
| Infrastructure cost | Published cloud pricing × modeled usage | `[inferred]` |
| Third-party / AI cost | Published API pricing × modeled volume | `[inferred]` |
| Compliance cost | Module 02 regulatory research | Inherits module 02's standing |
| Sales cycle length | Competitor case studies, practitioner reports | `[inferred]` |
| Churn benchmarks | Public company filings, industry reports | `[inferred]` — for *their* product, not ours |

---

# What Cannot Be Established Before Launch

| Input | Why not |
| --- | --- |
| **Our CAC** | Depends on a channel that has never been run |
| **Our churn** | Depends on a product that does not exist |
| **Our conversion rate** | Same |
| **Actual willingness to pay** | Requires a real sales conversation |

These four are the load-bearing inputs of almost every model. All four are unknowable.

That is not a reason to omit them — a model needs them. It is a reason to tag them
honestly and to present the result as a sensitivity range rather than a forecast.

```
CAC: $400 [assumption: needs validation — no channel has been tested;
 figure chosen as the value at which LTV:CAC = 3 given modeled price and churn]
```

That tag is more useful than a number, because it reveals the model was solved backwards
from a threshold — which is legitimate, and which the reader must be able to see.

---

# Sourcing Segment Budget

The most useful researchable input, and the one most often skipped.

Before modeling a price, establish what this segment plausibly spends on software at all.

| Source | Yields |
| --- | --- |
| Professional body surveys | Typical practice or firm spend |
| Industry benchmark reports | Software spend as a share of revenue |
| Competitor pricing at the low end | The floor the segment tolerates |
| Job postings mentioning tool budgets | Occasional direct evidence |
| Forum discussions about cost | Practitioner attitudes to price |

A price that exceeds the segment's entire annual software budget is not a positioning
choice. It is a contradiction, and it should be caught here rather than in a sales
meeting.

---

# Deriving Cost to Serve

Do not assume a margin. Build it.

```
cost to serve per customer per year
  = infrastructure   (published cloud pricing × modeled usage)
  + support          (expected tickets × handling time × loaded rate)
  + third-party      (per-operation pricing × modeled volume)
  + compliance       (fixed cost ÷ customer count)
```

Each component is `[inferred]` at best, but each is inferred from a **published price** —
which is far stronger than "80% gross margin, standard for SaaS".

The AI component deserves separate attention. A per-user monthly AI cost that consumes a
meaningful share of a per-user monthly price is a structural problem. Module 14 produces
this figure; if it has not run yet, model it here from published API pricing and flag it
for revisiting.

---

# Solving Backwards Is Legitimate — When Declared

A common and useful technique: instead of estimating CAC, ask what CAC the model can
tolerate.

```
Given price $1,200/yr, margin 75%, churn 20%:
  LTV = 1200 × 0.75 × 5 = $4,500
  For LTV:CAC ≥ 3, CAC must stay below $1,500.
```

This produces a **budget** rather than a forecast, and a budget is actionable: module 11
now knows what it has to work with.

State clearly that the figure was derived this way. Presented without that context, it
reads as a research finding.

---

# Sensitivity Over Point Estimates

Where most inputs are assumed, a single number is false precision.

| Scenario | CAC | Churn | LTV:CAC | Verdict |
| --- | --- | --- | --- | --- |
| Optimistic | «figure» | «%» | «ratio» | viable |
| Modeled | «figure» | «%» | «ratio» | viable |
| Pessimistic | «figure» | «%» | «ratio» | not viable |

Then state where the model breaks — the first threshold to fail as assumptions worsen.

A reader who sees the model flip between viable and not viable across a plausible range
understands the real situation. A reader shown `4.2` does not.

---

# Benchmarks Are Evidence About Other Companies

"SaaS churn averages 5% annually" is a `[verified]` claim about an industry. It is an
`[assumption]` about this product.

Tag the distinction:

```
Churn 20%/yr [assumption: needs validation — SMB SaaS benchmarks range 15–30%
 [verified: «source»]; no product-specific basis exists]
```

The benchmark supports the *range*. It does not establish the *value*.

---

# What Does Not Belong Here

| Activity | Belongs to |
| --- | --- |
| Market sizing | `02-market` |
| Competitor pricing capture | `05-competition` |
| Channel execution detail | `11-growth` |
| Metric definitions and instrumentation | `12-metrics` |
| Infrastructure architecture | `09-technology` |

This module sets the **constraint** — cost to serve per customer — that module 09 must
design inside. It does not design the infrastructure.

---

# When Retrieval Is Unavailable

Then competitor pricing is unavailable too, and Entry 3 has no market anchor.

1. Price from value alone, showing the derivation.
2. Tag every input `[assumption: needs validation]`.
3. Present sensitivity as the primary output; omit the point estimate.
4. Set confidence to `low`.
5. Set the verdict to `INSUFFICIENT EVIDENCE` if the outcome flips across the plausible
   range — which it usually will.
6. Record the two or three inputs most worth establishing as high-priority open questions.

Do **not** produce benchmark figures from memory. "Typical SaaS CAC is $500" cited as
though sourced is the characteristic fabrication of this module.

---

# Recording

| Destination | What |
| --- | --- |
| `state.evidence_log` | Every sourced input with its tag |
| `state.assumptions` | Every assumed input, with what would validate it |
| `state.open_questions` | The inputs most worth establishing, ranked |
| Model §5 | Sensitivity table |
| Model §13 | Sourced vs assumed counts, and honest confidence |

---

# Self Assessment

- Which inputs did I source, and which did I choose?
- Did I derive cost to serve, or assume a margin?
- Did I establish what this segment spends on software at all?
- Did I declare where I solved backwards from a threshold?
- Did I present sensitivity, or a single number?
- Did I cite any benchmark I did not actually retrieve?
- Does the confidence level match the sourced-to-assumed ratio?

---

> **Research Principle**
>
> The two numbers this model most depends on cannot be known yet.
>
> Everything else in this module is arranging honestly around that fact.
