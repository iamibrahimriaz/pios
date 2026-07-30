---
Title: Research Methodology
Module: 11-growth
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define how growth claims are sourced, labeled and bounded.
Audience:
  - AI Agents
Prerequisites:
  - engine/evidence-policy.md
  - 11-growth/core/06-Framework.md
Outputs:
  - Honestly bounded growth plan
Related Modules:
  - 12-metrics
Tags:
  - Growth
  - Methodology
  - Evidence
---

# Research Methodology

---

# The Structural Problem

Every number in this module describes behavior that has not happened yet.

Conversion rates, activation rates, churn, cycle times, cost per acquisition — none of them can
be observed for a product with no users. A growth plan written before launch is
**structurally low-confidence**, and the honest response is to say so rather than to produce
figures that look like findings.

| Can be evidenced | Cannot be evidenced before launch |
| --- | --- |
| Where the segment gathers | What proportion of them will convert |
| What the segment reads | How long a loop's cycle will be |
| Whether the segment refers, as a professional norm | Churn |
| What one channel test costs | Cost per acquired customer |
| The switching cost from the status quo | Activation rate |
| What competitors do | Whether it works for them |

---

# Channel Claims Are Research Claims

A channel is a factual claim about where people are. It is therefore evidenceable, and it must
be evidenced:

| Tier | Source | Use |
| --- | --- | --- |
| 1 | The segment observed there in `03-user`'s primary research | Definitive |
| 2 | Membership or circulation figures from the body itself | Strong |
| 3 | Trade publications and professional associations from `02-market` | Strong |
| 4 | Where competitors visibly spend — from `05-competition` | Establishes their behavior, not its effectiveness |
| 5 | Platform audience data for the specific segment | Indicative, and usually about a broader group |
| 6 | Practitioner commentary about the profession | Indicative — tag `[inferred]` |
| 7 | "Products like this use this channel" | **Not a source** |

Tier 7 is the module's characteristic failure and deserves the name:

> **Borrowed growth.** Importing the playbook of a product with a different model, segment and
> price. It is not wrong because it is conventional — it is wrong because the segment is not
> there and the buying process does not work that way.

Tier 4 needs the same caution `05-competition` applies to vendor marketing: that a competitor
spends on a channel establishes that they spend on it. Whether it works for them is not
visible from outside, and unprofitable channels persist for years.

---

# Rates Are Assumptions, and Must Look Like It

Every conversion rate, activation rate, churn figure and cycle time is
`[assumption: needs validation]` unless it cites observed data.

**The basis must be stated.** An assumption with a basis can be argued with; one without is a
number that acquires authority by repetition:

| Weak | Acceptable |
| --- | --- |
| "10% conversion" | "10% conversion `[assumption: needs validation]` — basis: the trade association's own reported response rate for member mailings, applied to a warmer route" |
| "5% monthly churn" | "5% `[assumption]` — basis: 06-business's sensitivity table midpoint, unvalidated" |

**Do not import industry benchmarks as findings.** A published median conversion rate describes
a population this product is not yet in, measured with definitions nobody states. It can inform
a range. It cannot support a plan.

---

# CAC and Churn Do Not Become Knowable Here

`06-business` established that both were unobtainable before launch, and handled them with a
sensitivity table plus a declared position rather than a figure.

This module inherits that position unchanged. It is the same discipline `07-strategy` was
required to observe — inherited uncertainty is carried forward in the strength the source
module used, and a new module is not new information.

> **Growth laundering.** A business model honestly says "CAC is unknown, here is the range
> under which it works". The growth plan states a CAC per channel, drops the range, and the
> financial model built on top of it treats the figure as established.

What this module can add is **learning cost**: what one test of a channel costs and how long it
takes to answer. That is knowable now, and it is what the first channel should be chosen on.

---

# The Closure Test Is Not a Judgment

Whether a mechanism is a loop or a funnel has a mechanical answer: does the output become the
next input?

| Loop | Funnel |
| --- | --- |
| Users produce something that attracts users | Spend produces users |
| Data improves the product, which attracts users | Content attracts users while it is published |
| Each clinic invites colleagues in the same clinic | Each conference produces leads |

A funnel is legitimate — many good businesses grow through one. Presenting a funnel as a loop is
not, because it implies compounding the business does not have and changes decisions about
spend, hiring and valuation.

**Never draw the arrow back unless the mechanism closes.** A diagram is a claim.

---

# Retention Mechanisms Must Be Locatable

A retention mechanism is a claim about the product, not about the market — so it is checkable
against `08-product` directly.

| Mechanism | Requires |
| --- | --- |
| Accumulated data | A requirement that stores something the user would lose |
| Habit | A requirement inside a routine the user already has |
| Workflow dependency | A requirement other people or processes rely on |
| Network | A requirement involving other users |
| Switching cost | Something that is genuinely costly to move |

A mechanism with no requirement behind it is a hope. A mechanism delivered by **deferred**
scope means retention is unproven at launch — which is a legitimate position, and a very
different one from what the plan otherwise implies.

---

# Referral Is a Finding, Not a Design Choice

Whether a segment refers depends on professional norms: whether users are colleagues or
competitors, whether recommending carries reputational risk, whether adoption is visible.

| Segment characteristic | Referral outcome |
| --- | --- |
| Users are peers who share practice | Refers readily |
| Users compete for the same customers | Does not refer |
| Adoption is invisible to peers | No natural moment |
| Recommending carries professional risk | Refers privately, if at all |

This comes from `03-user`. Designing a referral program for a segment that will not refer is
not an execution failure; it is a research failure that arrived here undetected.

---

# The Prohibitions

| Never | Why |
| --- | --- |
| List a channel with no evidence the segment is there | Borrowed growth |
| Use a competitor's channel spend as proof it works | Unprofitable channels persist for years |
| State a conversion, activation or churn rate as a finding | It has not happened yet |
| Import an industry benchmark as this product's number | Different population, undisclosed definitions |
| Restate module 06's unknown CAC as a per-channel figure | Growth laundering |
| Raise a conversion assumption until the payback check passes | The unaffordable motion survives |
| Draw an arrow back on a funnel | The diagram claims compounding |
| Claim a retention mechanism with no requirement behind it | A hope |
| Design a referral program for a segment that will not refer | A research finding was ignored |
| Plan acquisition spend before validation, where the problem is assumed | Amplifying an unvalidated product |

---

# Cross-Checks Before the Gate

| Check | Against | Fails when |
| --- | --- | --- |
| Payback | `06-business` | Implied CAC exceeds the ceiling and no regress is recorded |
| Model coherence | `06-business` route to market | The motion contradicts the assumed route |
| Channel evidence | `03-user`, `02-market` | A channel cites nothing |
| Activation | `10-execution` §5 | The event and time to first value disagree |
| Switching cost | `05-competition` | Migration sits outside activation |
| Retention | `08-product` §7 | A mechanism has no requirement |
| Churn and CAC | `06-business` | Stated more confidently than the source |
| Referral | `03-user` | A program assumes a norm the research contradicts |
| Sequencing | `07-strategy` | Spend is planned before Milestone Zero |

---

# Self Assessment

- Does every channel cite where the segment was observed?
- Is every rate in this document tagged, with a basis?
- Did I import any benchmark as a finding?
- Is my CAC position the same strength as module 06's?
- Did I bend a conversion assumption to make the arithmetic work?
- Does every arrow that closes actually close?
- Does every retention mechanism name a requirement?
- Is referral a finding here, or a decision?

---

> **Methodology Principle**
>
> This is the module most able to produce a document full of
> confident numbers about nothing that has happened.
>
> Its integrity is measured by how many of them are tagged.
