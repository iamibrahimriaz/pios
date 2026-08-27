---
Title: Quality Gate
Module: 06-business
Section: core
Category: Gate
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define how the Business module's gate is evaluated, criterion by criterion.
Audience:
  - AI Agents
Prerequisites:
  - 06-business/module.yaml
  - engine/gates.yaml
Outputs:
  - Gate verdict recorded in state.run
Related Modules:
  - 05-competition
  - 07-strategy
Tags:
  - Business
  - Quality
  - Gate
---

# Quality Gate

---

# Overview

`module.yaml` states the criteria. This document explains how to evaluate each.

The characteristic failure of this module is not a wrong number. It is a **precise
number** that nobody can tell was invented. Most of this gate is aimed at that.

---

# Governing Rule

> A gate is failed by default when its status cannot be determined.
>
> Uncertainty is a fail, not a pass.

---

# Criterion 1 — Payer identified and distinguished from the user

**Passes when:** the payer is named, the relationship to the user is stated explicitly
(including "the same person"), and willingness, ability and authority are assessed
separately.

**Fails when:** the payer is assumed to be the user without the question being asked, or
when the three capacities are collapsed into one judgment.

**Test:** does the document say who would have to approve this purchase? In any
organizational context, an unnamed approver is an unmapped blocker.

| Fails | Passes |
| --- | --- |
| "Doctors will pay $99/month" | "The practice principal signs; the practice manager holds the software budget and must agree. Willingness: high (from review evidence). Ability: within typical practice software spend. Authority: principal alone, for amounts under «figure»." |

---

# Criterion 2 — Price point justified against competitor pricing and value delivered

**Passes when:** all three justifications are present — against value, against competitor
pricing, and **against free**.

**Fails when:** any is missing, or when the price appears before the value calculation in
the reasoning.

**The order test.** Read sections 3 and 4 of the output. Was value established first, or
was a price chosen and value assembled to support it? A price with a value justification
that arrives at exactly the chosen number is usually the second.

**The free justification is mandatory** whenever module 05 identified a free status quo,
which it almost always will. "Why does someone pay «figure» when what they do today costs
nothing?" must have an answer that references value net of switching cost.

**The budget check.** Does the price fit inside what this segment plausibly spends on
software at all? A price exceeding the segment's entire annual software budget fails, no
matter how well-justified against value.

---

# Criterion 3 — Unit economics stated with assumptions surfaced

**Passes when:** every input carries a tag, the load-bearing assumption is named, and a
sensitivity table is present.

**Fails when:** any input is untagged, or when a point estimate is presented without
sensitivity while most inputs are assumed.

**The arithmetic trap check.** Count the inputs. Count how many are `[verified]` or
`[inferred]` from a published price. If most are `[assumption]`, the output must be
presented as a sensitivity range, not a forecast. A single confident `LTV:CAC` figure
built on four assumptions fails this criterion regardless of the arithmetic being correct.

**The margin check.** Was gross margin derived from a cost-to-serve breakdown, or asserted?
"80%, standard for SaaS" is an assertion and fails.

**The backwards-solve check.** If any figure was derived by solving for a threshold, that
must be declared. Solving backwards is legitimate; presenting the result as a research
finding is not.

---

# Criterion 4 — Path to first 10 customers described

**Passes when:** ten customers are named, or profiled specifically enough that someone
could go and find them, each with a route and a reason they would say yes.

**Fails when:** the section lists channels rather than customers.

| Fails | Passes |
| --- | --- |
| "SEO, content marketing, and partnerships" | "1. «Named practice» — introduced via «relationship». 2–4. Practices posting in «forum» about after-hours documentation — direct outreach. 5–10. Attendees of «annual conference», approached at «event»." |

**The honest-blank clause.** If no route can be identified, that is a finding and must be
stated plainly — "no existing access to this segment; acquisition route unestablished".
That fails the criterion but declares it, which is the correct behavior. Substituting
channel categories to fill the section is not.

---

# Criterion 5 — Willingness to pay carries its own evidence, or is recorded as unestablished with the test that would settle it

**Passes when:** the module states, as a separate claim with its own tag, whether anyone has
been observed paying for this — **or** records willingness to pay as unestablished and names
the test that would settle it.

**Fails when:** willingness to pay is treated as following from problem evidence, competitor
pricing, or the strength of the pain described in module 04.

## Six claims, and this module owns the last one

`engine/evidence-policy.md` separates them: **existence · frequency · severity · business
impact · solution demand · willingness to pay.** Evidence for any of the first five is not
evidence for the sixth.

> **A problem can be real, recurring, cross-vendor and expensively documented, and people
> will still not pay to prevent it.** That is the ordinary fate of insurance products, and it
> is not a rare case.

**The collapse is a sentence, not a decision.** *"44 people reported losing money to this, so
there is clearly demand"* moves from claim 4 to claim 6 in one clause, and nothing in the
paragraph looks wrong. **The first half is `[verified]`; the second is `[assumption]`.** Only
splitting the sentence makes that visible.

## What competitor pricing does and does not establish

**Criterion 2 requires the price to be justified against competitor pricing.** That
establishes what a market will bear **for products that already exist and have customers**.
It does not establish that anyone will pay *you*, at that price, for something that does not
exist yet.

**Both are needed and they are different claims.** A price anchored to a real comparable and
tagged `[assumption: needs validation]` for the willingness itself is a pass. A price anchored
to a comparable and presented as demonstrated demand is the failure this criterion exists to
catch.

## Unestablished is a pass — silently assumed is not

**From a public corpus, willingness to pay can never be established.** No volume of
complaints, reviews or forum threads converts into it. **The honest output is
`unestablished`, with the test named** — and that test becomes a Milestone Zero, ahead of any
build.

`engine/instrument-substitution.md` carries the ladder: stated interest → stated price →
registration with friction → refundable reservation → uncaptured card authorization → real
purchase. **Name the rung.** A number from rung 2 and a number from rung 5 are not the same
evidence and must not carry the same weight.

> **Where stated and revealed willingness to pay disagree, revealed governs** — recorded
> before the result, never chosen after it.

| Fails | Passes |
| --- | --- |
| "The problem costs users «n» hours a week, so a «price» tool is easily justified" | "Value justifies «price» [inferred: from the hours in 04]. **Whether anyone pays it is unestablished** — nobody has been observed buying, because nothing exists to buy [assumption: needs validation]. Test: MZ-2, uncaptured card authorization, threshold pre-registered" |
| A price table, competitor anchors, and no statement about demand | "Competitors sustain «band» [verified: pricing pages]. That establishes what the market bears for existing products; it does not establish demand for this one" |
| "Strong willingness to pay" citing module 04's severity scores | "Severity is claim 3. Willingness to pay is claim 6. We have the first and not the second" |

---

# Universal Gates

U1–U7 apply. Most often missed here:

| | |
| --- | --- |
| **U1** | Numbers are claims. An untagged figure is an untagged claim, however arithmetic its origin |
| **U3** | Price must not contradict segment budget evidence from `03-user` and `02-market` |
| **U5** | Every assumed input needs a validation method, not just a tag |

---

# Evaluation Procedure

1. Run the four passes of `engine/review-loop.md`.
2. Count sourced vs assumed inputs; check confidence matches.
3. Verify the price fits the segment's plausible budget.
4. Evaluate universal gates U1–U7.
5. Evaluate criteria 1–5. **All of them.**
6. Record the verdict.

```yaml
gate:
  module: 06-business
  attempt: 1
  verdict_reported: VIABLE WITH CONDITIONS
  inputs: {sourced: 3, inferred: 4, assumed: 6}
  criteria:
    payer_identified_and_distinguished: pass
    price_justified_three_ways: pass
    unit_economics_assumptions_surfaced: fail
    first_ten_customers: pass
    wtp_evidenced_or_unestablished: pass
  verdict: fail
  reason: "Gross margin asserted at 80% with no cost-to-serve derivation."
  action: "Derive from infrastructure, support and third-party components."
```

---

# On Failure

`module.yaml` sets `on_fail: return to 05-competition`.

| Kind | Example | Action |
| --- | --- | --- |
| **Local** | Margin asserted, sensitivity missing | Revise here |
| **Upstream (competition)** | No competitor pricing captured — no anchor exists | Return to `05-competition` |
| **Upstream (user)** | The segment has no budget for software at all | Return via `05` to `03-user` |

| Attempt | Action |
| --- | --- |
| 1–2 | Revise or regress |
| 3 | Halt. Escalate |

**A `NOT VIABLE AS MODELED` verdict passes the gate** if the analysis is honest. The gate
tests the quality of the reasoning, not the attractiveness of the conclusion. A run that
reports "not viable at any price this segment would pay" has saved the operator a year.

---

# What a Passing Module 06 Looks Like

- The payer is a specific role, and the approval path is mapped.
- Value was computed before price, from module 04's cost figures.
- The price is defended against free, not only against paid competitors.
- Every number carries a tag, and the assumed ones outnumber the sourced ones openly.
- The load-bearing assumption is named, and sensitivity shows what happens when it moves.
- Ten plausible first customers exist on the page.
- The verdict is no more confident than the inputs allow.

---

> **Gate Principle**
>
> This module can produce a beautiful model of a business that cannot exist.
>
> The gate's job is to make sure a reader can tell the difference.
