---
Title: References
Module: 05-competition
Section: resources
Category: Reference
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Route competitive claims to verifiable sources, and set the limit on inference.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - ../constitution/resources/18-References.md
Outputs:
  - Source routes for competitive research
Related Modules:
  - 02-market
  - 06-business
Tags:
  - Competition
  - References
  - Reference
---

# References

---

# Overview

Competitive research has an unusual property: much of what matters is publicly documented, and much of what gets written is invented anyway.
This file separates the two.

---

# What Is Verifiable From Outside

| Claim | Source | Standing |
| --- | --- | --- |
| List price, and what it includes | The pricing page — **with the access date** | `[verified]` |
| What the product does | Changelogs, release notes, documentation | `[verified]` |
| What breaks, and what users complain about | Support forums, review sites, community threads | `[verified]` for the complaint pattern |
| Which integrations exist | Integration directories, partner pages | `[verified]` |
| Certifications held | Trust pages, certification registers | `[verified]` |
| Incident history | Public status pages | `[verified]` |
| Which segment they sell to | Copy, case studies, minimum contract size | `[inferred]` — strong |
| Sales motion | Job postings, "contact us", implementation docs | `[inferred]` — strong |
| Channels that work in this market | Where they sustain investment | `[inferred]` — and paid for by them |
| Business model constraints | Pricing structure and packaging | `[inferred]` — the most valuable inference available |

The last row is where the module's best findings come from. **Ask what their revenue model forbids them from shipping** —
per-seat pricing on a product that reduces seats, services revenue that automation would remove, a minimum contract that excludes a segment.
That inference is defensible from published pricing alone.

---

# What Is Not Verifiable From Outside

| Claim | Why not |
| --- | --- |
| Their data model or architecture | Nothing published; a confident paragraph here is fabrication |
| Their roadmap | Unless they published it, and then it is intent |
| Their customer count or revenue | Unless disclosed |
| Their internal quality or technical debt | Unknowable, and irrelevant to the buyer |
| Why they withdrew a product | Findable sometimes — ask someone. Otherwise an open question |

`Architecture-Comparison.md` sets the rule: **you can see what their product cannot do; you cannot see why.** Reason from documented limits,
and leave the codebase narrative unwritten — it is the one finding nobody can check.

---

# Sourcing the Status Quo

The strongest competitor in most markets has no website, so the routes are different:

| Need | Route |
| --- | --- |
| What they use today | `03-user`'s observed workflow — already documented |
| What it costs them | `04-problem`'s cost per occurrence |
| Why they keep it | `04-problem`'s workaround analysis: habit, control, distrust, sufficiency |
| How many use nothing at all | `02-market` Frame 5's gap reasoning, plus the absence of any supplier |

None of this comes from a category search, which is why the enumeration has to start from modules 03 and 04 rather than from a product list.

---

# Dating Discipline

Everything in this module decays:

**Prices change and pages are rewritten.** Record the access date with every figure. `06-business` will still be using it in six weeks.

**Reviews describe a product that has changed.** A complaint from three years ago may name friction since fixed, and building against it
targets a competitor that no longer exists.

**Changelogs are the antidote.** They are dated by construction, and they show what actually shipped rather than what is claimed.

---

# Source Tiers, Applied

| Tier | At the competition stage |
| --- | --- |
| **Primary** | The competitor's own pricing, documentation, changelogs, status pages, certifications |
| **Industry** | Sector press on entrants, funding and consolidation — useful for the threat picture |
| **Academic** | Rarely relevant |
| **Product and technical** | Integration directories, developer docs, public APIs — strong for capability |
| **Community** | Review sites, forums, "alternatives to" pages — the best route to substitutes and workarounds |
| **AI-assisted** | Generating the search list and candidate categories. **Never a capability claim, never a price** |

The last row again: a model asked what a competitor's product does will produce a plausible feature list. It is `[inferred]` from training
data of unknown vintage, and it is exactly how a withdrawn feature or an imagined one enters the analysis as fact.

---

# Common Mistakes With Sources Here

| Mistake | Consequence |
| --- | --- |
| An estimated price with no source | A guess becomes `06-business`'s revenue model |
| Undated pricing or reviews | Evidence about a product that has changed |
| Marketing copy scored as capability | Intent recorded as function |
| Architectural speculation | Fabrication that reads as research and cannot be checked |
| Only searching product categories | The status quo — the actual incumbent — never appears |
| Not searching for who stopped | The reason a gap persists goes unfound |

---

> **Resource Note**
>
> The most valuable inference in this module is legitimate and free: read
> their pricing and ask what their revenue model forbids them from
> shipping.
>
> The least valuable is a confident account of their architecture, which
> nobody can check and everyone will believe.
