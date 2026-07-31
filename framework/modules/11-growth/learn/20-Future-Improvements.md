---
Title: Future Improvements
Module: 11-growth
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: State what the Growth module does not yet do well.
Audience:
  - Product Managers
  - Founders
  - Marketers
Prerequisites:
  - 11-growth/learn/19-Related-Modules.md
Outputs:
  - A candid list of the module's limitations
Related Modules:
  - 03-user
  - 06-business
Tags:
  - Growth
  - Improvements
  - Learn
---

# Future Improvements

---

# Known Limitations

**Nothing checks conversion figures against their source market.** Borrowed growth is
named as a failure and there is no field recording where a rate was measured, so a
benchmark and an observation are indistinguishable in the plan.

**The closure test is guidance.** A diagram labeled "loop" satisfies "at least one growth
loop described with its inputs and outputs" without closing.

**Switching cost arrives as a single number.** Module 03 produces one figure from five
components, and this module needs to know which dominates — an adoption barrier caused by
retraining is addressed differently from one caused by contract timing.

**The spend gate has no enforcement.** Withholding acquisition spend until Milestone Zero
is a rule with no check, at the end of a four-link chain that also has no checks at its
other links.

**Time to first value has no decomposition.** A number is required; the breakdown that
would make it actionable — account creation, empty state, data entry, processing wait —
is not, so the module reports a problem it cannot locate.

**No treatment of channel saturation.** A channel that works for the first hundred
customers frequently does not work for the next thousand, and the plan has no structure
for where the ceiling is.

**Expansion paths are underspecified.** They are a required output with no criteria, so
in practice they hold a list of future products.

---

# Candidate Improvements

| Candidate | What it would fix | Cost |
| --- | --- | --- |
| A `source_market` field on every conversion figure | Borrowed growth becomes visible | Small, and the highest-value change here |
| A structured closure test — name the mechanism per step | Funnels stop being labeled loops | Small |
| Carry switching cost as its five components | The dominant barrier becomes actionable | Small, and it is a module 03 change |
| A Milestone Zero spend-gate check | The chain's final link gets teeth | Small |
| Time-to-first-value decomposition | The module can locate what it measures | Small |
| Channel saturation estimates | The plan stops assuming linear scaling | Moderate, and inherently speculative |

The first row deserves emphasis. Every other limitation here produces a weaker plan; that
one produces a plan that passes an arithmetic check it should have failed.

---

# What Should Not Change

**Time to first value stays measured in minutes.** It is the most specific criterion in
the module and the reason product causes of poor conversion get found at all.

**The payback check stays here rather than in module 06.** The author of the ceiling
should not also be the auditor of the plan that has to clear it.

**Retention stays required to be a mechanism.** "Because it is useful" is the single most
common retention model and the one most often wrong.

**Funnels stay acceptable.** Every version of growth guidance that treats loops as
superior produces plans with drawn-in loops. A funnel with honest arithmetic is a better
artifact than a loop with a hopeful arrow.

**The spend gate stays.** It is the only place in the framework where an evidence gap
directly restricts money, and that is what makes the whole Milestone Zero chain more than
documentation.

---

> **Improvements Principle**
>
> This module's arithmetic is only as good as the origin of its conversion rates, and the
> framework currently does not ask where they came from.
>
> One field would fix the module's most consequential failure.
