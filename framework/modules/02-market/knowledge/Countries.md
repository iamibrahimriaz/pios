---
Title: Countries
Module: 02-market
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Explain why jurisdiction is a hard input and what changes when it changes.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 02-market/knowledge/Market-Definition.md
Outputs:
  - Jurisdiction within market_definition
Related Modules:
  - 09-technology
  - 13-operations
Tags:
  - Market
  - Jurisdiction
  - Concept
---

# Countries

---

# What It Is

The **where** of the market boundary — the named jurisdiction or jurisdictions in which the
product would be sold and operated.

It is not a detail of the definition. It determines which regimes apply in Frame 2, which
population is counted in Frame 3, where data may be stored in `09-technology`, and what
`13-operations` has to comply with on a schedule.

| Same idea | Different jurisdiction | What changes |
| --- | --- | --- |
| Clinical documentation tool | England | NHS structures, national procurement patterns |
| Clinical documentation tool | Germany | Different regime, different certification, different language |
| Clinical documentation tool | United States | State-level variation, HIPAA, insurer-driven incentives |

The product concept survives the move. Almost nothing else does.

---

# When It Applies

In Frame 1 (Bound), taken from `idea_brief`. Frame 2 reads it directly.

**It is never inferred.** If the jurisdiction is unset, the run should not have reached this
module — the correct action is to return to `01-idea` and ask.

---

# How to Apply It Here

**Name the jurisdiction at the level the law operates at.** "Europe" is not a jurisdiction for
health data. "The US" is not one for insurance or licensing. Go to the level where the rules are
actually written.

**Pick one to launch in, even when several are plausible.** Sizing, regulation and operations all
need a single answer. Record the others as candidates in `scope_boundaries` — that is a
`07-strategy` decision, not a market one.

**Note the language and the data-residency implication now.** Both become requirements in
`08-product` and constraints in `09-technology`, and both are invisible if the jurisdiction is
left vague.

**Where a second jurisdiction is genuinely planned, size it separately.** Two countries added
together produce a figure that describes a market nobody operates in.

---

# Where It Misleads

**Multi-country ambition inflates every figure in Frame 3 while removing the ability to check
any of them.** A TAM summed across ten countries cannot be verified against any single regime,
population or price level.

**Regulatory similarity is assumed far more often than it is verified.** Neighboring countries
with comparable regimes still differ in certification, evidence requirements and enforcement.
Assumed equivalence is an `[assumption: needs validation]`, not a shortcut.

**The operator's own location gets mistaken for the market.** Where the builder lives constrains
what they can research and operate easily; it does not establish where the demand is. If those
are the same place, say so deliberately rather than by default.

---

# Related

| | |
| --- | --- |
| `Market-Definition.md` | Where jurisdiction is one of three required parts |
| `PESTEL.md` | The environment specific to that jurisdiction |
| `09-technology` | Data residency and regime obligations |
| `13-operations` | Compliance as a recurring schedule |

---

> **Concept Note**
>
> Jurisdiction is an input, not a finding.
>
> A market sized before it is located is arithmetic without a
> subject.
