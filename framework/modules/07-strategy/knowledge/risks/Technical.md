---
Title: Technical Risks
Module: 07-strategy
Section: knowledge/risks
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Register technical risks that could change the strategy, not the implementation details.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 07-strategy/knowledge/risks/Mitigation.md
Outputs:
  - Technical risks within risk_register
Related Modules:
  - 09-technology
  - 14-ai-systems
Tags:
  - Strategy
  - Risk
  - Concept
---

# Technical Risks

---

# What It Is

The technical risks that could change **the strategy** — as distinct from the engineering risks `09-technology` will
handle inside its own design.

The test for inclusion here: **if this turns out badly, does the approach change?**

| Risk | Early warning sign |
| --- | --- |
| **The required data does not exist or cannot be obtained** | `14-ai-systems`' availability check — unconfirmed data is a blocker there |
| **The integration the approach depends on is not available** | API documentation; a refusal; a partner's terms |
| **A single supplier controls a necessary input** | Provider pricing, terms and deprecation notices |
| **The AI mechanism cannot reach the accuracy the job needs** | A Wizard of Oz or prototype result from `04-problem` |
| **Per-unit operating cost exceeds margin at real usage** | Cost per user computed against `06-business`'s margin |
| **A compliance obligation forbids the mechanism** | `02-market` Frame 2's findings |
| **The data cannot be migrated from the incumbent** | Export format and completeness, checked early |

Anything that does not change the approach — framework choices, refactoring, scaling work — belongs to
`09-technology`, not to a strategic register.

---

# When It Applies

In Move 6 (Register). Several of these are checkable before building, which makes them candidates for Milestone Zero
rather than for monitoring.

---

# How to Apply It Here

**Check data availability before registering it as a risk.** `14-ai-systems` requires availability **confirmed, not
projected**. If it can be confirmed now, confirm it; if it cannot, it is a blocker and the approach may be wrong.

**Register supplier dependency where a single provider is load-bearing.** `05-competition` identified supplier power as
structural. Terms change, prices change, and versions are deprecated — and for a model provider all three happen.

**Test the accuracy risk cheaply.** `04-problem`'s Wizard of Oz method establishes whether human-quality output is even
useful, before anything is built. That sequencing turns a technical risk into a validation question.

**Verify the export path from the incumbent early.** Migration is one of the five switching-cost dimensions, and an
incumbent whose data cannot be extracted makes adoption impossible regardless of product quality.

**Send everything else to module 09.** A strategic register cluttered with implementation risks loses the few entries
that would actually change the plan.

---

# Where It Misleads

**Implementation risk is registered as strategic risk.** "Scaling may be difficult" belongs in `09-technology`'s
design. It fails the test: the approach does not change.

**Technical risk is inflated to justify architecture.** A speculative scaling risk becomes a reason to build for scale
now — `09-technology`'s architecture inflation, entering through the register.

**Model capability is assumed to improve on schedule.** Betting the approach on a capability that does not yet work
well enough is a real strategy and must be labeled as one, with a fallback.

**The data-rights question is treated as technical.** Whether data may lawfully be used is a legal claim.
`Legal.md` and `09-technology` hold it, and `14-ai-systems` requires it stated as a right rather than an access.

**Cost risk is deferred to implementation.** Per-user operating cost is arithmetic available now, and it has ended
products whose cost exceeded their margin. It is a strategy risk, not an engineering one.

---

# Related

| | |
| --- | --- |
| `Legal.md` | Data rights and regulatory prohibition |
| `Security.md` | Exposure and breach risk |
| `09-technology` | Where engineering risk belongs |
| `14-ai-systems` | Data availability, accuracy and cost |

---

> **Concept Note**
>
> Include it only if a bad outcome changes the approach.
>
> Everything else is module 09's problem, and putting it here hides
> the two entries that mattered.
