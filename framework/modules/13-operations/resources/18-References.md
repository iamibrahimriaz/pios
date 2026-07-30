---
Title: References
Module: 13-operations
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Separate operator commitments from forecasts, and route obligations to their citations.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 00-AI-Constitution/resources/18-References.md
Outputs:
  - Source routes for operations planning
Related Modules:
  - 02-market
  - 09-technology
Tags:
  - Operations
  - References
  - Reference
---

# References

---

# Overview

This module produces two kinds of statement with different standing, and mixing them is how a product acquires obligations nobody agreed to:

| | Nature | Standing |
| --- | --- | --- |
| Channels, hours, response targets, who is on call | **Commitments** | `[verified: operator]` |
| Ticket volume, staffing need, cost per user | **Forecasts** | `[assumption]` |

> A response target the operator has not agreed to is a promise made on their behalf. A volume estimate presented as a plan is a staffing
> decision made on a guess.

---

# Input → Source

| Input | Source |
| --- | --- |
| Support hours, channels, response targets | **The operator.** Nobody else can commit them |
| Who is on call, and their sustainable limit | **The operator** |
| Expected ticket volume | `10-execution`'s flows and `08-product`'s edge cases → `[assumption]` |
| Which burdens are fixable | `10-execution`'s friction analysis |
| Severity definitions | `08-product`'s user impact; `09-technology`'s data-loss position |
| Failure modes needing runbooks | `09-technology`'s failure modes; `08-product`'s five edge categories |
| Regulatory notification deadlines | `02-market` Frame 2 — **with the citation and date** |
| Recurring obligations | `09-technology`'s mechanisms, each needing a cadence here |
| Restore objectives | `09-technology`'s recovery point and recovery time |
| Infrastructure cost | `09-technology`, dated |
| Inference cost | `14-ai-systems` |
| The cost ceiling | `06-business` |
| A real hourly rate for the operator's time | **The operator** |

Two rows deserve emphasis. **The notification deadline** must carry its citation, because a deadline nobody knows is a deadline that gets missed
and the failure is legal rather than technical. And **the operator's hourly rate** is what converts a support forecast into a cost — omitting it
is the standard reason the third arithmetic check passes when it should not.

---

# Runbooks Are Sourced, Not Invented

Every runbook corresponds to something already enumerated:

| Runbook | Where the failure came from |
| --- | --- |
| Transcription backlog | `09-technology`'s queue depth signal |
| Retention job failure | `09-technology`'s scheduled-obligation mechanism |
| Upload failure rate | `08-product`'s R-02 failure edge case |
| Restore | `09-technology`'s recovery procedure |
| Suspected cross-practice access | `09-technology`'s threat answer |
| Erasure request | `09-technology`'s deletion service |

If a runbook has no corresponding failure mode, either module 09 missed it — worth raising — or it is not a real failure.

---

# What Cannot Be Sourced Before Launch

| Figure | Status |
| --- | --- |
| Ticket volume | `[assumption]`. It is the load-bearing input to the cost check |
| Minutes per support interaction | `[assumption]` |
| Minutes per transcription — for a service-delivered product | `[assumption]`, and frequently the dominant cost |
| Actual restore duration | Unknown until rehearsed. That is why the rehearsal has a cadence |
| Whether a rota of one is sustainable | The operator's judgment, and it changes with experience |

The framework's response is the same as elsewhere: a **range, a named load-bearing assumption, and a sensitivity** rather than a point estimate.

---

# Source Tiers, Applied

| Tier | At the operations stage |
| --- | --- |
| **Primary** | The operator, for every commitment. Regulator publications, for notification deadlines. Modules 08 and 09's outputs |
| **Industry** | Sector norms for support expectations in this segment — weak, but occasionally sets a buyer's expectation |
| **Academic** | Not relevant |
| **Product and technical** | Provider status pages and support terms — what you can actually promise depends on what they promise you |
| **Community** | Practitioner discussion of what support they expect from suppliers |
| **AI-assisted** | Drafting runbooks and testing them against the 3am standard. **Never a commitment, never a volume figure** |

The AI-assisted row has one strong use here: hand a runbook to a fresh context and ask what it cannot do without asking a question. That is the
3am test performed rather than asserted, and it finds every "investigate" reliably.

---

# Documenting the Plan

**Attribute every commitment.** Hours, channels, response times, on-call. `[verified: operator]` or it is not a commitment.

**Every obligation carries four things.** Cadence, named owner, evidence produced, and where the evidence is kept. "The team" is not an owner.

**Every alert carries three.** Threshold, named person, runbook. Missing any one and it is worse than no alert.

**Every runbook carries access at the top and a verification at the end.** And a "do not do" line, because every system has one.

**Report a ceiling breach as a regress.** To `06-business` for price or `07-strategy` for scope. Never absorbed by revising the forecast the plan
just stated.

---

# Common Mistakes With Sources Here

| Mistake | Consequence |
| --- | --- |
| A response commitment nobody agreed to | A promise that breaks during the first incident |
| Volume presented as a plan | Staffing decided on a guess, and the cost check passes falsely |
| The operator's time unpriced | The largest cost in the model omitted |
| A notification deadline without its citation | A legal failure, in a situation already going badly |
| Compliance recorded as achieved | A control that existed once, discovered during an audit |
| An obligation with a role instead of a name | It belongs to nobody |
| The ceiling breach absorbed | A margin that exists only in the document |

---

> **Resource Note**
>
> Commitments come from the operator. Forecasts are assumptions. Label
> them differently, because one of them is a promise.
>
> And price the operator's own hours — without them, the third arithmetic
> check passes on a product nobody can afford to run.
