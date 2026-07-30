---
Title: Template
Module: 11-growth
Section: core
Category: Output
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The working template for the Growth Plan — this module's primary output.
Audience:
  - AI Agents
Prerequisites:
  - 11-growth/core/06-Framework.md
Outputs:
  - projects/<slug>/research/11-growth.md
Related Modules:
  - 12-metrics
Tags:
  - Growth
  - Template
  - Output
---

# Template — Growth Plan

---

# Usage

Copy everything below the line into `projects/<slug>/research/11-growth.md` and fill it.

This is a **working document**. It feeds:

| Deliverable | Fed by | Required |
| --- | --- | --- |
| `13-Growth-Plan.md` | all sections | optional — emitted when the run's scope calls for it |
| `09-Roadmap.md` | §10 sequencing | required |
| `11-Success-Metrics.md` | §4 activation, §6 retention, §7 loops | via `12-metrics` |

| Marker | Meaning |
| --- | --- |
| `«placeholder»` | Replace with real content |
| `<!-- guidance -->` | Instructions for you. Remove before completing |
| `[tag]` | Evidence tag per `engine/evidence-policy.md` |

**Two rules govern this module.** A channel claim must cite where the segment was actually
observed — not where products like this are usually marketed. And CAC arrived from
`06-business` as unknowable before launch; it does not become knowable here.

---
---

# Growth Plan — «Project Name»

| | |
| --- | --- |
| Module | 11-growth |
| Date | «ISO date» |
| Primary segment | «from 03-user» |
| Price | «from 06-business» |
| Problem evidence standing | **verified / assumed** |
| Activation moment | «from 10-execution §5» |
| Status | draft / reviewed / gated |

---

## 1. The Growth Plan, in One Paragraph

<!-- Write last. How this product reaches its first users, what brings them back, and
     what makes each new user cheaper to acquire than the last — if anything does. -->

«One paragraph.»

---

## 2. Growth Model

<!-- Move 1. One primary model. These are not marketing styles — they demand different
     products, different prices and different teams. -->

**Primary model:** «sales-led / product-led / community-led / marketplace / referral»

**Why this and not «alternative»:** «reasoning from the segment research» `[tag]`

**What this model requires the product to do:** «the product implications — capabilities
this model needs that the MVP may not have»

**Does the MVP support it?** «yes / no — if no, name what is missing and whether it is
deferred scope or a regress»

### The Payback Check

<!-- The arithmetic that decides whether the model is possible at this price. -->

| | |
| --- | --- |
| Price | «figure, from 06-business» |
| Gross margin per user per month | «figure, from 06-business» |
| Acceptable payback period | «months — an operator input or a stated assumption» |
| **Implied CAC ceiling** | «margin × months» |
| Cost of one unit of the chosen motion | «e.g. a sales conversation, a conference stand, a paid click» `[tag]` |
| Conversions needed per unit | «n» |
| **Implied CAC of the motion** | «figure» `[tag]` |
| **Fits under the ceiling** | «yes / no» |

**If no:** «the model, the price or the segment has to change. That is a regress to
06-business or 07-strategy, recorded here — not absorbed as optimism about conversion.»

---

## 3. Where the Segment Actually Is

<!-- Move 2. Every row cites where the segment was OBSERVED — from 03-user's research,
     02-market's trade sources, or 05-competition's channel analysis.
     A channel with no citation is a channel chosen by fashion. -->

| Channel | Segment reached | Evidence they are there | Effort | Learning cost | Priority |
| --- | --- | --- | --- | --- | --- |
| «channel» | «segment» | `[verified: source]` | S/M/L | «what one test costs» | 1 |

**First channel:** «one» — «why start here»

<!-- Choose the first channel by LEARNING cost, not by projected CAC. Projected CAC is an
     assumption; the cost of finding out is a fact. -->

**Channels deliberately not used:** «which, and why they would waste money on this segment»

**Channels that cannot be evidenced:** «named, with what would establish them — these are
open questions, not plans»

---

## 4. Activation

<!-- Move 3. Carried from 10-execution §5. Acquisition without activation is churn with
     extra steps. -->

| | |
| --- | --- |
| Activation event | «the specific action meaning "they got value"» |
| Why this event | «reasoning — what it proves about the user» |
| Time to activate | «minutes, from 10-execution» |
| Steps to activate | «n, from 10-execution» |
| Biggest friction | «what stands in the way» |
| Target activation rate | «percentage of new users» `[assumption: needs validation]` |

**The one change that would most improve activation:** «from the flow analysis, not from
general practice»

**Switching cost the user must pay first:** «from 05-competition — migration, retraining,
parallel running. If it exists, it belongs in the activation flow, not after it.»

---

## 5. The First Ten Customers

<!-- Named where possible, specifically profiled otherwise. "Marketing" is not a plan for
     the first ten, and the first ten are where a product either becomes real or does not. -->

| # | Who | How reached | Why they would say yes | Status |
| --- | --- | --- | --- | --- |
| 1 | «named person or specific profile» | «specific route» | «their reason» | prospect / contacted / committed |

**The pitch, in one sentence:** «what you actually say to them»

**What would make them say no:** «the honest objection — from 05-competition's status quo
analysis»

**If the problem is assumed rather than verified:** «these ten are the validation sample.
Say so — this is Milestone Zero's population, not a sales pipeline.»

---

## 6. Retention

<!-- Move 4. Mechanically. "A great product" is not a retention mechanism.
     Each mechanism must be locatable in the product — name the requirement that delivers it. -->

| Mechanism | How it works | Delivered by | Strength |
| --- | --- | --- | --- |
| «accumulated data / habit / workflow dependency / network / switching cost» | «why leaving becomes costly» | R«n» from 08-product | high / med / low |

**Mechanisms with no requirement behind them:** «none, or list them — a retention mechanism
nothing in the product delivers is a hope»

| | |
| --- | --- |
| Expected churn | «figure» `[assumption: needs validation]` |
| Basis | «from 06-business's sensitivity table, or stated as unknown» |
| Behavior that precedes leaving | «the observable early warning» |
| First retention risk | «when in the lifecycle, and why» |

**Does retention depend on the MVP or on deferred scope?** «if deferred, retention is
unproven at launch and the roadmap must say so»

---

## 7. Growth Loops

<!-- Move 5. At least one, described honestly.

     THE TEST: does the output become the next input? If not, it is a funnel.
     A funnel is legitimate. A funnel with an arrow drawn back to the top is not. -->

### Loop «n» — «name»

```
«input» → «action» → «output» → «how the output becomes the next input»
```

| | |
| --- | --- |
| Type | viral / content / paid / sales / data |
| Cycle time | «duration» |
| What makes each turn bigger | «the amplification, or "nothing — it is linear"» |
| Where it leaks | «the step that loses the most» |
| Evidence it works | `[tag]` — «or "none, this is a hypothesis"» |
| **Closes?** | «yes — the output feeds the input / no — this is a funnel» |

**Honest statement:** «if none of the described mechanisms close, say so plainly here. A
product can grow through a funnel; it just grows linearly with spend, and the plan should
say that rather than imply compounding.»

---

## 8. Onboarding

| Stage | Goal | Method | Success signal | Skippable |
| --- | --- | --- | --- | --- |
| 1 | «what the user achieves» | «how» | «observable» | yes / no |

| | |
| --- | --- |
| Migration required | «yes — where it sits / no» |
| Drop-off risk, highest | «which stage, and why» |
| Time to value target | «minutes, matching 10-execution» |

---

## 9. Expansion

<!-- Only where the business model supports it. If revenue per customer is fixed, say so
     rather than inventing an expansion path. -->

| Path | Trigger | Revenue impact | Requires |
| --- | --- | --- | --- |
| «seat expansion / tier upgrade / usage growth» | «when» | «figure» `[tag]` | «capability» |

**Or:** «no expansion path — revenue per customer is «figure» and growth is by customer
count alone»

---

## 10. Sequencing

<!-- Growth spend before activation works amplifies a product nobody stays with.
     State what must be true before each stage. -->

| Stage | Do not start until | Signal to watch |
| --- | --- | --- |
| First ten customers | «the MVP completes the core job end to end» | «activation rate» |
| First channel test | «activation works for the first ten» | «cost per activated user» |
| Channel scale | «retention holds past «period»» | «cohort retention» |

**If the sharpest problem is assumed:** «no acquisition spend before Milestone Zero
completes. State it here — this is where the framework's evidence position becomes a
spending decision.»

---

## 11. Referral

| | |
| --- | --- |
| Would they refer? | «yes / no» `[tag]` |
| Why, or why not | «reasoning from 03-user — professional norms, competition between users, visibility» |
| Natural referral moment | «where in the flow» |
| Incentive needed | «yes / no — and what that says about the product» |

<!-- In some professions users refer readily; in others they are competitors and will not.
     This is a research finding, not a design choice. -->

---

## 12. Growth Assumptions

| # | Assumption | Impact if wrong | Cheapest validation |
| --- | --- | --- | --- |
| A«n» | «statement» | «consequence» | «test» |

<!-- Every rate, cost and conversion figure in this document is an assumption unless it
     cites a source. List them all here — U5. -->

---

## 13. Contradicting Evidence

<!-- Required and non-empty. What in the research argues against this growth plan? -->

- «finding that argues against a channel, a loop or the retention position»

---

## 14. Confidence

| | |
| --- | --- |
| Confidence in this plan | high / medium / low |
| Basis | «share of channel and retention claims that cite evidence» |
| Weakest element | «what, and why» |
| What would raise it | «specific test» |

<!-- Growth plans for pre-launch products are structurally low-confidence. Saying so is
     more useful than a confident plan built on invented conversion rates. -->

---

## 15. Handoff

| Consumer | What it takes from here |
| --- | --- |
| `12-metrics` | Activation event, retention mechanism, loops — these become the metrics |
| `09-Roadmap.md` | §10 sequencing — when growth work starts |
| `13-Growth-Plan.md` | All sections |

---

<!-- ACCEPTANCE — remove before completing
- [ ] One primary growth model, with the alternative rejected and the reasoning cited
- [ ] The payback check completed, with arithmetic — and a regress recorded if it fails
- [ ] Every channel cites where the segment was observed
- [ ] First channel chosen by learning cost, not projected CAC
- [ ] Channels deliberately not used, listed
- [ ] Activation event defined, with time and steps from 10-execution
- [ ] First ten customers named or specifically profiled
- [ ] Every retention mechanism names the requirement that delivers it
- [ ] At least one loop described, with an honest closes-or-not verdict
- [ ] Funnels called funnels
- [ ] Sequencing states what must be true before spending
- [ ] No acquisition spend before Milestone Zero, where the problem is assumed
- [ ] Every rate and cost figure either cites a source or appears in §12
- [ ] §13 non-empty
- [ ] Every «placeholder» replaced and every guidance comment removed
-->

---

> **Template Principle**
>
> Most growth plans are written for a product that already works.
>
> This one is written before launch, which means its honest job is
> to say what must be true before any money is spent.
