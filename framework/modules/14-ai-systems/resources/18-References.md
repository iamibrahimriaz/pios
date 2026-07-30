---
Title: References
Module: 14-ai-systems
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Require version-and-date citation for model claims, and treat data rights as legal.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 00-AI-Constitution/resources/18-References.md
Outputs:
  - Source routes for AI capability decisions
Related Modules:
  - 02-market
  - 09-technology
Tags:
  - AI
  - References
  - Reference
---

# References

---

# Overview

Every factual claim in this module decays faster than anywhere else in the framework. Model capabilities, prices, context limits and provider terms
are all version-scoped, and a claim without a version and a date is already unreliable.

---

# The Version-and-Date Rule

> Model capabilities and prices are version-scoped and change — cite them with a version and a date, exactly as `09-technology` requires of every
> technology claim.

```
Capability: «provider» «model-version», «claim»
  [verified: «provider documentation», accessed «date»]
Price: £«x» per «unit», same version
  [verified: provider pricing page, accessed «date»]
Context limit: «n» tokens, same version
  [verified: «documentation», «date»]
Deprecation: the previous version was deprecated «n» months after release
  [verified: «deprecation notice», «date»]
```

The last line is the one nobody records and everyone needs. Deprecation exposure is a registered risk in
`07-strategy/knowledge/risks/Technical.md`, and its evidence lives here.

---

# Input → Source

| Input | Source | Standing |
| --- | --- | --- |
| Model capability claims | Provider documentation, per version | `[verified: provider, version, date]` |
| Cost per operation | Provider pricing, per version | `[verified]` with the date |
| Operations per user per month | `03-user`'s observed job frequency | Inherits module 03's tag |
| Revenue per user | `06-business` | Inherits |
| **Data availability** | **Checked, not projected** | `[verified]` or it is a **blocker** |
| Data quality | Assessed against real samples | `[verified]` for the sample |
| **Data rights** | **A legal determination** | Not a technical answer |
| Provider terms on training and retention | The contract, not the marketing page | `[verified: contract]` or unconfirmed |
| Residency of the inference endpoint | Provider documentation | `[verified]`, and Frame 2 decides if it is permitted |
| Accuracy in production | A golden set judged by a domain expert | `[verified]` for that set only |
| The non-AI alternative's performance | Measured, or `03-user`'s current-state observation | Whichever exists |

---

# Data Rights Are a Legal Question

The framework is explicit that this is not a technical matter:

| Question | Why it is legal |
| --- | --- |
| Do we have the right, under which regime? | **Consent for treatment is not consent for model input** |
| Does the data leave our systems? | To whose infrastructure, in which jurisdiction |
| Are regulated or PII fields in the input? | Check `09-technology` §3 mechanically |
| Is provider training on our data disabled? | **And is that contracted, or assumed?** |

> Sending a regulated field to a model provider is the same class of exposure as putting one in an analytics event property.

This is the fourth appearance of one discipline: `09-technology` traces obligations to mechanisms, `12-metrics` checks event properties,
`13-operations` schedules the review, and this module checks model inputs. **The regulated column list is the same list every time.**

---

# Benchmarks Are Not Evidence About Your Task

Published model benchmarks are the most cited and least applicable source here.

| Problem | Detail |
| --- | --- |
| **Different task** | A benchmark measures a standardized task, not yours |
| **Different distribution** | Clean, curated inputs. Real inputs are noisy, accented, atypical |
| **Different judge** | Automated scoring, not a domain expert on clinical correctness |
| **Version drift** | The figure was measured on a version that may be deprecated |

The framework's answer is a **golden set built from real cases and judged by a domain expert**, never used for tuning. That is the only accuracy
evidence about your task, and it is why `Evaluation.md` requires the set stratified to include the hard cases rather than the demonstrable ones.

---

# Source Tiers, Applied

| Tier | At the AI stage |
| --- | --- |
| **Primary** | Provider documentation, pricing and contracts, per version and dated. A domain expert's judgment on output quality. Your own golden set |
| **Industry** | Regulator guidance on automated decisions and clinical software — via `02-market` Frame 2 |
| **Academic** | Occasionally relevant for an approach's limits; rarely for a product decision |
| **Product and technical** | Provider status pages and deprecation notices. Dated by construction |
| **Community** | Practitioner reports of failure modes in the wild — useful for populating Move 6 specifically |
| **AI-assisted** | Generating candidate capabilities, drafting the golden set's stratification, and arguing the non-AI alternative's case. **Never a capability claim, never a price, never an accuracy figure** |

The final row carries a particular irony worth stating: a model asked about its own capabilities, price or context limit will answer from
training data of unknown vintage. Those figures feed the cost ratio, which feeds the framework's three cost checks, which decide whether the
business works.

The genuinely valuable use is the one in the passing example: ask it to argue for the **non-AI alternative** as its advocate would. That is the
advocate check performed adversarially, and it is the check most likely to be skipped.

---

# Documenting the Decisions

**Record what was dropped, with the simpler thing adopted instead.** Those records are what stop a capability being re-proposed every quarter as an
obvious omission.

**Write the specific failure, not the class.** "May hallucinate" generates nothing. "May invent a drug interaction that does not exist, which a
rushed clinician could accept" generates a guardrail.

**State the detection column honestly, including "no".** A failure nobody can detect is the most serious entry available, and it constrains
autonomy regardless of accuracy.

**Set the bar before building, and state what happens if it is missed.** Afterwards, the bar becomes whatever was achieved.

**Compute the cost ratio and forward it.** Cost per operation × operations per user ÷ revenue per user, to `09-technology` and `13-operations`.

---

# Common Mistakes With Sources Here

| Mistake | Consequence |
| --- | --- |
| A model-supplied price or context limit | The cost ratio, and three downstream cost checks, run on a stale figure |
| A benchmark score as accuracy evidence | A different task, distribution and judge, presented as yours |
| Data availability projected | A blocker recorded as a risk; a capability that cannot be scheduled |
| Data rights assumed from terms of service | Consent for treatment is not consent for training |
| Provider training assumed disabled | An unconfirmed contractual question at the center of a compliance exposure |
| A golden set of clean cases | Measures a population you do not serve |
| A golden set used for tuning | Measures how well the capability was fitted to it |
| Generic failure modes | A disclaimer where a guardrail belongs |

---

> **Resource Note**
>
> Cite the version and the date, or the claim is decaying as you write it.
>
> And the one thing a model is genuinely useful for here is arguing against
> itself — ask it to make the case for the form field.
