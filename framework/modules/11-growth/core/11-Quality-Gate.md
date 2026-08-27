---
Title: Quality Gate
Module: 11-growth
Section: core
Category: Verification
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define how each gate criterion for this module is evaluated.
Audience:
  - AI Agents
Prerequisites:
  - 11-growth/module.yaml
  - engine/gates.yaml
Outputs:
  - Gate verdict
Related Modules:
  - 12-metrics
Tags:
  - Growth
  - Quality Gate
  - Verification
---

# Quality Gate

---

# Overview

`module.yaml` states the criteria. This document explains how to evaluate each.

This module's output becomes a spending plan. What passes here determines where money goes
before there is any evidence that it should.

---

# Governing Rule

> A gate is failed by default when its status cannot be determined.
>
> Uncertainty is a fail, not a pass.

---

# Criterion 1 — Channels matched to where the named segments actually are

**Passes when** every channel row cites where the segment was observed — `03-user`'s research,
`02-market`'s trade sources, or `05-competition`'s channel analysis — and channels that cannot
be evidenced are listed separately as open questions.

**Fails when** any channel appears with no citation, or when unevidenced channels sit in the
plan as though they were established.

| Fails | Passes |
| --- | --- |
| "Content marketing, SEO, LinkedIn" | "The «trade association» annual conference — `[verified: 03-user, 4 of 6 interviewees named it as their one professional event]`" |
| "Paid search — high intent" | "«Publication» — `[verified: circulation 14,000, association-reported, covers 60% of practicing «role»]`" |

**The borrowed-growth check.** Read each channel and ask: was this chosen because the segment is
there, or because products like this use it? The second is the module's characteristic failure,
and the citation requirement is the only reliable defense.

**Competitor spend is not proof.** That a competitor advertises somewhere establishes that they
advertise there. Unprofitable channels persist for years, and their profitability is not visible
from outside.

**Also required:** the **first channel**, chosen by learning cost rather than projected CAC, with
the reasoning. Projected CAC before launch is an assumption; the cost of finding out is a fact.

---

# Criterion 2 — >= 1 growth loop described with its inputs and outputs

**Passes when** at least one mechanism is described as a cycle with input, action and output,
and each carries an explicit **closure verdict**.

**Fails when** a mechanism is presented as a loop without the closure test being applied, or when
nothing closes and the document does not say so.

> **The closure test.** Does the output become the next input?

| Loop | Funnel |
| --- | --- |
| Each clinic invites colleagues in the same clinic | Each conference produces leads |
| Data improves the product, which attracts users | Content attracts users while it is published |

**A funnel is legitimate and passes this criterion** — provided it is called a funnel. Many good
businesses grow through one. What fails is a funnel drawn with an arrow back to the top: that
diagram claims compounding the business does not have, and it changes decisions about spend,
hiring and valuation made by someone reading it in good faith.

**Also required per loop:** cycle time, what makes each turn bigger, where it leaks, and the
evidence it works — which before launch is usually "none, this is a hypothesis". Writing that is
worth more than a diagram implying otherwise.

---

# Criterion 3 — Retention mechanism identified, not assumed

**Passes when** every retention mechanism is named mechanically **and** maps to a requirement in
`08-product` that delivers it.

**Fails when** retention rests on product quality, or when a mechanism has no requirement behind
it.

| Fails | Passes |
| --- | --- |
| "Users will stay because the product saves them time" | "Accumulated consultation history — R4 stores it, and leaving means losing three months of records" |
| "Strong engagement" | "Workflow dependency — R7 produces the referral letter the practice's admin process now expects" |

**The location check.** Cover the mechanism column and read only the requirement column. Does
each requirement actually create a cost to leaving? A requirement that stores nothing, involves
nobody else, and sits outside any routine does not retain anyone.

**Also required:**

| Check | Fails when |
| --- | --- |
| MVP versus deferred | The mechanism arrives in later scope and the plan does not say retention is unproven at launch |
| Churn position | Stated more confidently than `06-business` did |
| Early warning | No observable behavior that precedes leaving |

The early warning is the actionable output of this section. A churn percentage tells you what
happened; the behavior that precedes it is the only thing anybody can act on.

---

# Criterion 4 — Time to first value measured in minutes, and stated

**Passes when** the activation event is a specific action, and time to first value is stated in
minutes and steps, consistent with `10-execution` §5.

**Fails when** activation is a signup, when the figure is absent, or when it contradicts
`10-execution`.

| Fails | Passes |
| --- | --- |
| "Users activate when they sign up" | "A doctor has saved their first consultation note against a real patient — 4 steps, target 6 minutes" |
| "Quick onboarding" | The step count, the target in minutes, and the longest unavoidable step |

**Why the event must prove value.** An activation event chosen for being easy to log measures
nothing. The test: if a user did this and never returned, would you still claim they got value?
If yes, it is the wrong event.

**Also required:** the switching cost from `05-competition` positioned **inside** the activation
flow. Migration and retraining are not post-activation concerns — they are the largest thing
standing between a user and first value, and placing them afterwards is how activation rates get
planned optimistically.

---

# Criterion 5 — Every conversion figure carries the market it was measured in, or is tagged [assumption]

**Passes when:** each rate states where it came from — your own data, or a named external
market.

**Fails when:** an industry benchmark appears untagged. It was measured in a market with a
different switching cost, buyer and alternative, and it feeds the payback check.

**Why this one matters most here.** Every other gap in this module produces a weaker plan.
This one produces a plan that **passes an arithmetic check it should have failed**.

---

# Module-Specific Checks

## The Payback Check

**Fails when** the implied CAC of the chosen motion exceeds the CAC ceiling implied by price and
payback period, and no regress is recorded.

```
margin per user per month × acceptable payback months = ceiling
cost of one unit of the motion ÷ conversions per unit = implied CAC
```

This module's arithmetic check, and the sibling of `09-technology`'s cost check. Both convert an
argument into a comparison of two numbers.

**The bent-assumption watch.** The most common way an unaffordable motion survives is that the
conversion assumption rises until the arithmetic passes. If a conversion rate changed while the
payback check was being run, the gate fails.

A failed payback check is a **regress** — to `06-business` for the price, or `07-strategy` for
the segment. It is not a signal to plan harder.

## The Growth Laundering Check

**Fails when** CAC or churn is stated more confidently here than in `06-business`.

Module 06 could not know either and said so with a sensitivity table. This module has no new
information, and a new document is not new evidence. This is the same check `07-strategy` runs
against confidence laundering, applied to the two numbers most likely to end up in a financial
model.

## The Sequence Check

**Fails when** acquisition spend is planned before Milestone Zero, where the sharpest problem is
assumed.

This is the fourth and final place Milestone Zero has consequences: declared in `04-problem`,
made binding in `07-strategy`, sequenced first in `10-execution`, and here it gates money.
Spending to acquire users for a product whose problem is unverified amplifies the uncertainty
rather than resolving it.

## The Referral Coherence Check

**Fails when** a referral mechanism assumes a norm `03-user` contradicts.

Whether a segment refers is a research finding about professional norms — peers share, competitors
do not. A referral program for a segment that will not refer is a research failure that arrived
here undetected.

---

# Universal Gates

| | |
| --- | --- |
| U1 | Every factual claim carries exactly one evidence tag |
| U2 | `acquisition_channels`, `growth_loops`, `retention_model`, `onboarding_strategy`, `expansion_paths` all in `state.outputs` |
| U3 | No claim contradicts the evidence log without superseding it |
| U4 | The growth model records the alternative it rejected |
| U5 | Every rate, cost and conversion figure without a source is in `state.assumptions` with a validation method |
| U6 | Written for a reader with no access to this conversation |
| U7 | Every control declared load-bearing names where it executes, and that place exists |

U5 does most of the work here. Nearly every quantity in this module is an assumption, and the
register is what stops a plan of hypotheses from reading as a forecast.

---

# Verdict

```yaml
gate:
  module: 11-growth
  criteria:
    channels_evidenced: pass | fail
    loop_described_with_closure_verdict: pass | fail
    retention_mechanism_located: pass | fail
    time_to_first_value_stated: pass | fail
    conversion_figures_carry_market: pass | fail
  module_checks:
    payback: pass | fail
    no_growth_laundering: pass | fail
    spend_gated_on_validation: pass | fail
    referral_coherent: pass | fail
  universal: [U1, U2, U3, U4, U5, U6, U7]
  compounding: loop | funnel | none
  verdict: pass | fail
  regressed_to: «06-business / 07-strategy / none»
  notes: «what failed and what was done»
```

| Verdict | Action |
| --- | --- |
| Pass | Hand to `12-metrics` |
| Fail | Revise, or `return to 06-business`. Three attempts, then halt |

`compounding: funnel` is a passing value. It is recorded explicitly because it is the single most
consequential thing this module can tell an operator about their business, and it is the thing
most often obscured.

---

> **Gate Principle**
>
> Almost nothing here can be verified, and this gate cannot change that.
>
> What it can do is make sure the plan says so — because the next
> document that quotes these numbers will not.
