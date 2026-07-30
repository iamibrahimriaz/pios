---
Title: References
Module: 11-growth
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Require a citation per channel, and mark the growth figures that have no source.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 00-AI-Constitution/resources/18-References.md
Outputs:
  - Source routes for growth planning
Related Modules:
  - 03-user
  - 05-competition
Tags:
  - Growth
  - References
  - Reference
---

# References

---

# Overview

This module has one hard sourcing rule — **every channel cites where the segment was observed** — and one honest admission: most growth figures
have no source before launch.

---

# The Channel Citation Rule

> A channel with no citation was chosen by convention.

| Acceptable citation | Not acceptable |
| --- | --- |
| "«Association», 60 single-handed members in «county» [verified: published membership list, «date»]" | "Professional associations" |
| "«Forum», «n» posters identifiably single-handed discussing documentation [verified: accessed «date»]" | "Online communities" |
| "«Event», attendance list published, «n» single-handed attendees" | "Industry conferences" |
| "«Competitor» has sustained spend on «channel» for «n» years [verified: «evidence»]" | "SEO works in this market" |

The last row is the underused route. `05-competition/knowledge/Marketing-Comparison.md` makes the point: competitors have already paid to learn
which channels work here, and sustained investment is the strongest channel evidence available before running anything.

---

# What Has No Source Before Launch

| Figure | Status |
| --- | --- |
| CAC, per channel | `[assumption]` — no channel has been tested |
| Conversion rate | `[assumption]` — and it frequently decides the payback check |
| Churn | `[assumption]` — `06-business` holds the number, with sensitivity |
| Viral coefficient | `[assumption]`, and usually for a mechanism that does not exist |
| Trial-to-paid rate | `[assumption]` — and consumer benchmarks do not transfer |
| Time to first value in practice | Estimable from `10-execution`'s step count; actual is unknown |

The module's response is not to find better guesses. It is to **compare channels on the cost of finding out** — a figure that is knowable now.

---

# Where the Non-Numeric Inputs Come From

| Input | Source |
| --- | --- |
| The segment's social structure — do they refer? | `03-user`. For competing practitioners the answer is structurally no |
| The job's natural frequency | `03-user`. Decides whether habit is available as a retention mechanism |
| Switching cost, and its binding dimension | `03-user`. Belongs inside activation |
| Margin per user, and the payback ceiling | `06-business` |
| Which requirement delivers each retention mechanism | `08-product`, by identifier |
| The status quo's objection | `05-competition`. It will be the same for every one of the first ten |
| Acceptable payback period | **The operator** |
| Whether the problem is verified | `04-problem`. It gates all acquisition spend |

---

# Benchmarks and Why They Mislead Here

Growth benchmarks are the most circulated numbers in product work and the least transferable.

**What breaks the transfer**

- **Price point.** A £20/month product and a £2,400/year one cannot share a motion, let alone a CAC.
- **Buyer.** Self-serve figures describe markets where the user signs. Where they cannot, none of it applies.
- **Segment structure.** Referral rates assume users who benefit from other users joining. In a competitive professional segment that is false.
- **Definition.** "Activation" in a published figure may mean sign-up, first use, or a habit threshold.

If a benchmark is used at all, it belongs as the **upper bound of a sensitivity range**, with the population difference named — the same
handling `06-business` and `12-metrics` require.

---

# Source Tiers, Applied

| Tier | At the growth stage |
| --- | --- |
| **Primary** | Membership lists, attendance lists, forum threads — evidence of where the segment is. The operator, for payback appetite |
| **Industry** | Sector event and association listings; practitioner press |
| **Academic** | Not relevant |
| **Product and technical** | Competitors' sustained channel investment — `05-competition` |
| **Community** | The forums themselves, which are simultaneously a source and a channel |
| **AI-assisted** | Generating candidate channels to then verify. **Never a CAC, conversion rate or viral coefficient** |

The AI-assisted caution matters here because the borrowed-growth failure is precisely what a model produces by default: asked for a growth
strategy, it supplies the modal playbook — content, free trial, product-led — regardless of price, buyer or segment.

---

# Documenting the Plan

**Cite every channel, or list it as an open question.** Channels that cannot be evidenced are not plans; they are things to test later.

**Show the payback check as arithmetic, both halves.** Ceiling from margin and payback period; implied CAC from the motion's cost and its
conversion assumption. Then name which assumption decides it.

**Record `compounding: loop | funnel | none`.** With the closure test's reasoning, and with the evidence — which before launch is usually
"none, this is a hypothesis".

**Point each retention mechanism at a requirement identifier.** A mechanism with no requirement behind it is a hope, and the check is
mechanical.

---

# Common Mistakes With Sources Here

| Mistake | Consequence |
| --- | --- |
| A channel with no citation | The plan is a convention, and the segment may not be there |
| A borrowed playbook | A motion the price cannot fund, discovered after hiring |
| Benchmark conversion in the payback check | The affordability verdict rests on another market's number |
| Referral assumed without checking the segment | A loop that cannot operate, projected as compounding |
| Retention claimed with no requirement | A hope in the position where a mechanism belongs |
| First-ten CAC extrapolated | The warm network's cost applied to cold acquisition |

---

> **Resource Note**
>
> Cite where you saw them. Compare channels on the cost of finding out.
>
> And when asked for a growth strategy, notice that the modal answer —
> content, free trial, product-led — is the borrowed-growth failure with a
> respectable name.
