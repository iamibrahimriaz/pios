---
Title: Research Methodology
Module: 09-technology
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define how technical claims are sourced, labeled and bounded.
Audience:
  - AI Agents
Prerequisites:
  - engine/evidence-policy.md
  - 09-technology/core/06-Framework.md
Outputs:
  - Sourced, correctly labeled technical design
Related Modules:
  - 13-operations
Tags:
  - Technology
  - Methodology
  - Evidence
---

# Research Methodology

---

# Three Kinds of Statement

Every statement in a technical design is one of three things, and the distinction is not
cosmetic — each has a different failure mode:

| Kind | Example | Label |
| --- | --- | --- |
| **Derived** | "The record needs a clinician reference, because R4 requires filtering by clinician" | `derived: R4` |
| **Documented** | "«Datastore» supports row-level security from version «n»" | `[verified: source]` |
| **Judgment** | "Identifiers are UUIDs rather than integers" | `judgment` — registered |

The dangerous statements are documented-looking judgments. "«Technology» handles this well"
reads as a documented capability, is actually a recollection, and is acted on immediately.

---

# The Derivation Chain

Every entity, column, operation and control must be traceable:

```
problem (04)  →  requirement (08)  →  entity / operation / control (here)
```

If a chain cannot be written, one of two things is true:

| | Meaning | Action |
| --- | --- | --- |
| The element serves no requirement | Speculative | Remove it |
| The requirement's data was implicit | Module 08 was vague | Name it and regress |

The second case is the one that matters. Inventing the missing entity here is the easier
path, produces a document that looks complete, and permanently hides the fact that a
requirement was never fully specified.

---

# Version-Specific Claims Must Be Looked Up

Technology moves. A capability that did not exist two versions ago, a limit that was raised,
a default that changed, a feature that was deprecated — these are the facts most likely to be
recalled and most likely to be wrong.

| Claim class | Must be | Because |
| --- | --- | --- |
| A technology supports X | Cited to current documentation, with a version | Support is version-scoped |
| A limit or quota is N | Cited to the provider's published limits | Quotas change and vary by tier |
| A price is N | Cited to the current price page, with the date | Pricing changes and is region-specific |
| A feature is deprecated | Cited | Deprecation timelines are specific |
| A regulation requires X | Cited to the regulation or the issuing body | Everything else is commentary |

**Source hierarchy**

| Tier | Source | Use |
| --- | --- | --- |
| 1 | Official documentation for the specific version | Definitive |
| 2 | The project's own release notes or changelog | Definitive for what changed |
| 3 | The provider's published limits and pricing pages | Definitive, with the date recorded |
| 4 | The regulation, standard or specification itself | Definitive for obligations |
| 5 | Maintainer statements in issues or discussions | Strong |
| 6 | Recent, dated technical writing by practitioners | Indicative — tag `[inferred]` |
| 7 | Benchmarks with a published methodology | Indicative, and rarely transferable |
| 8 | Undated blog posts and forum answers | Weak — and usually about an older version |
| 9 | Recollection | Not a source |

Tier 7 needs a caution. A benchmark measures one workload on one configuration. It tells you
nothing about this product's workload unless the workload matches, and it usually does not.

---

# Compliance Claims Are the Highest-Stakes Claims in the Framework

| Never write | Because |
| --- | --- |
| "The system is HIPAA compliant" | Compliance is assessed, not asserted, and not by this document |
| "«Provider» is compliant, so we are" | A compliant provider is a precondition, never a conclusion |
| An invented required field or retention period | It reads as authoritative, is immediately actionable, and creates legal exposure |
| "Encrypted" with no scope, algorithm or key custody | It sounds like a control and specifies nothing |

**The correct form** is always obligation → mechanism → enforcement point → citation:

| Obligation | Mechanism | Enforced at | Source |
| --- | --- | --- | --- |
| Retain records «n» years | `retained_until` column + scheduled purge | Datastore + job runner | `[verified: «regulation, section»]` |
| Restrict access to treating clinician | Record-level authorization predicate | Query layer | `[verified: «regulation, section»]` |

Where the obligation cannot be established, it is an **open question and a blocker** — not a
softened claim. An unmet legal obligation is different in kind from a risk: it means the
product cannot lawfully operate, and pretending otherwise is the most consequential dishonesty
available in this module.

---

# Sizing Is Arithmetic, and the Arithmetic Is Shown

The same rule module 02 applies to market sizing applies here:

> **Arithmetic does not create evidence.** A derived figure is only as good as its inputs, and
> the inputs must be visible.

```
1,000 users at launch  [from 06-business]
× 12 sessions/user/month  [inferred: from 03-user workflow frequency]
× 8 requests/session  [derived: from the job walk in 08-product]
= 96,000 requests/month ≈ 0.04 requests/second average
```

Written that way, the answer is checkable and the conclusion is obvious: this product does not
need a distributed architecture at launch. Written as "expected moderate load", it justifies
anything.

**Peak matters more than average.** State the assumed peak-to-average ratio and where it came
from. Most systems fail at peak, and most sizing is done on averages.

---

# Cost Figures

| Requirement | |
| --- | --- |
| Every figure cites a published price, with the date | Prices change |
| Every figure states the tier and region | Both change the number materially |
| The total states what is excluded | Data transfer and support are the usual omissions |
| Cost per user is derived and compared to the ceiling | This is a gate criterion |

A cost model that omits the components nobody thinks about — egress, backups, logging
retention, staging environments — is not conservative. It is wrong in the direction that
matters.

---

# The Prohibitions

| Never | Why |
| --- | --- |
| State a version-specific capability from memory | The most reliably wrong class of statement in technical writing |
| Invent a limit, quota or threshold | It gets built against and tested against |
| Invent a regulated field, code or retention period | Authoritative, actionable, and a legal exposure |
| Claim compliance | It is not this document's to claim |
| Present a judgment as documented | The reader cannot tell what is verified |
| Cite a benchmark as evidence for this product's performance | Different workload, different configuration |
| Choose a technology and write the justification afterwards | The justification will be excellent and unrelated to the reason |
| Copy a threat model | A generic threat list examines nothing about this system |

---

# Judgments Are Assumptions

Design requires judgments no research produced: identifier types, soft versus hard delete,
naming conventions, whether something is a separate entity or a column, cache lifetimes.

These are legitimate. Presenting them as derived is not.

1. Label the judgment.
2. Record the alternative rejected — U4.
3. If it is a **one-way door**, register it in `state.assumptions` with a validation method
   and give it the strongest justification in the document.

| Test | |
| --- | --- |
| Cheap to change after launch | Judgment; record it and move on |
| Requires a data migration to change | One-way door; justify it properly |
| Requires a rewrite, or cannot be changed | One-way door; this is where the evidence belongs |

Most technical decisions are cheap to reverse and get argued about at length. A few — data
model shape, tenancy model, primary datastore, regulatory posture — are not, and are often
made in an afternoon. Concentrating the evidence on the second group is most of what
experience looks like in this module.

---

# Cross-Checks Before the Gate

| Check | Against | Fails when |
| --- | --- | --- |
| Entity traceability | `08-product` | An entity serves no requirement |
| Requirement coverage | `08-product` | A requirement's data is unmodeled |
| Operation coverage | `08-product` | A MUST requirement is unreachable |
| Edge-case coverage | `08-product` §8 | An edge case has no failure response |
| Obligation trace | `02-market` | An obligation has no mechanism |
| Cost | `06-business` | Cost per user exceeds the ceiling |
| Load | `06-business` | Capacity far exceeds the projections |
| Environment | `03-user` | The design assumes connectivity the user lacks |
| First slice | `08-product` §11 | The first buildable piece is not the first shippable slice |

---

# Self Assessment

- Can I write the derivation chain for every entity and operation?
- Did I look up every version-specific claim, or recall one?
- Does every compliance statement name a mechanism and cite a source?
- Is any number here a guess?
- Did I show the sizing arithmetic, including peak?
- Do my cost figures cite prices with dates, and include the components people forget?
- Are my judgments labeled, and are the one-way doors properly justified?
- Did I choose the technology before or after writing the reason?

---

> **Methodology Principle**
>
> Every other module's errors cost a rewrite.
>
> An error here is built, deployed, and filled with real data
> before anybody reads this document again.
