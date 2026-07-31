---
Title: Future Improvements
Module: 06-business
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: State what the Business module does not yet do well.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 06-business/learn/19-Related-Modules.md
Outputs:
  - A candid list of the module's limitations
Related Modules:
  - 11-growth
  - 13-operations
Tags:
  - Business
  - Improvements
  - Learn
---

# Future Improvements

---

# Known Limitations

**The load-bearing assumption is a convention, not a field.** The framework asks for it
repeatedly and nothing in the schema holds it. Modules 09, 11 and 13 each have to infer
which input matters, and they infer differently.

**Nothing checks that a regress actually happened.** When module 13 reports a ceiling
breach, the rule is to return here. No mechanism verifies that the price or the scope
changed, so a run can report the breach, note it, and continue with the original
numbers.

**The cost model has no required line for human time.** It is the most commonly omitted
cost and the most commonly dominant one in small products. Its absence is not a gate
failure.

**Sensitivity has no required form.** "Run a sensitivity" permits the decorative ±20%
table on every input, which is worse than no sensitivity because it looks like the
question was addressed.

**Multi-sided and marketplace economics are unsupported.** One payer, one price. A
product where one side subsidizes another needs two models and a transfer between them,
and the framework handles it by convention.

**No treatment of price changes over time.** Introductory pricing, grandfathering,
annual increases — all normal, none structured. The model is a snapshot and the business
is not.

**Currency and tax are unhandled.** The regulated-jurisdiction discipline from module 02
does not extend to the money. A price is a number with no currency requirement and no
treatment of sales tax, which changes the payer's real cost by a fifth in many markets.

---

# Candidate Improvements

| Candidate | What it would fix | Cost |
| --- | --- | --- |
| A `load_bearing_assumption` field | Three downstream modules stop inferring | Small, and probably the highest-value change here |
| A regress-confirmed check when a breach is reported | The three checks stop being absorbable | Moderate; requires state the engine does not track well |
| A required `human_time` line in the cost model | The dominant cost stops being invisible | Small |
| A sensitivity form: one input, real range, breakpoint | Decorative sensitivity stops passing | Small |
| Currency and tax on every price | The payer's real cost becomes correct | Small, and overdue |
| Two-sided model support | Marketplaces stop being a convention | Large |
| Price-over-time structure | Introductory and annual changes become modelable | Moderate |

---

# What Should Not Change

**The payer criterion stays first.** It catches more failures than the other three gate
criteria combined, and it is the one that looks most like a formality.

**Value and constraint stay separate numbers.** Collapsing them into a single "price"
loses the information that makes a later regress decidable. In the worked example, the
fact that the constraint was a free incumbent rather than the value was what made
raising the price the recommended response.

**Payback ceiling stays preferred over LTV/CAC.** Every review proposes reinstating the
ratio because it is familiar. It is built on assumed churn, and pre-launch churn is
unknowable — so the ratio's authority is entirely borrowed.

**The three checks stay in three different modules.** Consolidating them into one
review here would mean the author of the numbers is also the auditor of them.

---

> **Improvements Principle**
>
> The framework's economic discipline depends on a regress that nothing enforces.
>
> Everything else here is a schema gap. That one is the difference between three checks
> that bind and three checks that can be noted and ignored.
