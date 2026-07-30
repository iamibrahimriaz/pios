---
Title: References
Module: 09-technology
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Route technical claims to verifiable sources, and require version-and-date citation.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 00-AI-Constitution/resources/18-References.md
Outputs:
  - Source routes for technical decisions
Related Modules:
  - 02-market
  - 06-business
Tags:
  - Technology
  - References
  - Reference
---

# References

---

# Overview

Technical claims decay faster than any others in the framework. A pricing page changes weekly, a model version is deprecated in months, and a
regulatory guidance note is superseded. This file sets what must be cited and how.

---

# Input → Source

| Claim | Source | Standing |
| --- | --- | --- |
| **Obligations under a regime** | Regulator publications and official guidance — via `02-market` Frame 2 | `[verified]`, cited with the document and date |
| **Certification requirements, cost, duration** | The regulator or notified body's published schedule | `[verified]` if published |
| Infrastructure rates | Provider pricing pages and calculators | `[verified]` with the access date |
| Model inference rates | Provider pricing, **per model version** | `[verified: provider, version, date]` |
| Service limits and quotas | Provider documentation | `[verified]` — and they change |
| What an integration permits | The target system's API documentation | `[verified]` |
| Whether data can be exported from an incumbent | The incumbent's documentation, or a sample export | `[verified]` only with a sample |
| Load figures | `06-business`'s projections, with the arithmetic shown | Inherits module 06's tags |
| Query performance | A query plan against representative data | `[verified]` for the plan, `[inferred]` for the projection |
| A team's capability | The operator | `[verified: operator]` |

---

# The Version-and-Date Rule

The framework requires it for every technology claim, and `14-ai-systems` restates it for models:

> Model capabilities and prices are version-scoped and change — cite them with a version and a date.

```
Inference: «provider» «model-version», £«x» per «unit»
  [verified: provider pricing page, accessed «date»]
Note: the provider deprecated the previous version «n» months after
  release. Deprecation exposure is registered — 07-strategy/risks/Technical.md.
```

The same discipline applies to service limits, which are frequently the real ceiling: a provider quota is a hard constraint that no amount of
horizontal scaling raises, and it is documented and dated.

---

# What Cannot Be Sourced From Outside

| Claim | Why |
| --- | --- |
| A competitor's architecture or data model | `05-competition/knowledge/Architecture-Comparison.md`: you can see what their product cannot do, not why |
| Real-world performance of a stack at your load | Only measurable, and benchmarks describe other workloads |
| Whether a design will scale | Move 6's answer is a named bottleneck with a figure, not a claim |
| Actual transaction pricing from a provider | List rates are published; negotiated terms are not |

---

# Where Legal Questions Stop Being Technical

Three questions in this module have legal answers and no technical ones:

| Question | Who answers |
| --- | --- |
| Which regime applies, and to whom | `02-market` Frame 2, and ultimately legal advice |
| Whether we may use this data for this purpose | A legal determination — `14-ai-systems` treats data rights as legal claims |
| Whether an erasure-versus-retention conflict is acceptable | Legal, then the operator |

The framework's position throughout: **record the obligation and the mechanism, and never claim compliance.** An assessor draws the conclusion;
this module supplies the evidence.

---

# Source Tiers, Applied

| Tier | At the technology stage |
| --- | --- |
| **Primary** | Regulator publications. Provider documentation and pricing. The target system's API docs. The operator, on capability and operability |
| **Industry** | Standards bodies where a standard binds — via `02-market` |
| **Academic** | Occasionally relevant for an algorithmic approach; rarely for a design decision |
| **Product and technical** | Provider status pages, changelogs, deprecation notices. Strong and dated by construction |
| **Community** | Useful for operational gotchas; never for a capability claim |
| **AI-assisted** | Generating candidate schemas, reviewing a design against the moves, and stress-testing the threat question. **Never a provider price, never a service limit, never a compliance conclusion** |

The AI-assisted row deserves the same caution here as elsewhere, with one addition specific to this module: a model's knowledge of provider
pricing and service limits is **version-stale by construction**. Those figures feed the cost check, which decides whether the business model
works, so they must come from the provider's page with a date.

---

# Documenting the Decisions

**Every stack row carries three columns.** Rejected alternative, trade-off accepted, reversibility cost. An asserted choice fails the gate.

**Every index names its query.** An index with no query is a guess with a permanent write cost.

**Every obligation carries its citation.** Not the regime's name — the document and the date, so a future reader can check whether it still says
that.

**The blocker list is part of the deliverable.** An obligation with no mechanism is surfaced, not softened into a risk.

---

# Common Mistakes With Sources Here

| Mistake | Consequence |
| --- | --- |
| A model-supplied provider price | The cost check runs on a stale number and the margin verdict is wrong |
| Undated pricing | The idle floor is computed against rates that have changed |
| "Compliant with «regime»" | A claim the framework forbids, and one an assessor will test |
| A regime named without its obligations | Nothing to build and nothing to schedule |
| Competitor architecture asserted | Fabrication that reads as research |
| A benchmark used as a performance claim | It describes another workload on other hardware |
| Service quotas assumed | The real ceiling, discovered in production |

---

> **Resource Note**
>
> Cite the version and the date, or the claim is already decaying.
>
> And a provider price supplied from memory rather than from the page is the
> input most likely to make the cost check — and the business model — wrong.
