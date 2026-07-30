---
Title: Security Risks
Module: 07-strategy
Section: knowledge/risks
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Register security exposure at the level that changes the strategy, driven by what data is held.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 07-strategy/knowledge/risks/Legal.md
Outputs:
  - Security risks within risk_register
Related Modules:
  - 09-technology
  - 13-operations
Tags:
  - Strategy
  - Risk
  - Concept
---

# Security Risks

---

# What It Is

Exposure arising from what the product holds and what it can do — registered at strategic level, with the controls
themselves belonging to `09-technology`.

Severity is driven by the data, not by the architecture:

| What is held | Consequence of exposure |
| --- | --- |
| Special-category or health data | Regulatory penalty, notification duty, and the end of trust in the segment |
| Financial or payment data | Direct loss, scheme obligations |
| Credentials to another system | Compromise propagates beyond this product |
| Commercially sensitive customer data | Contractual liability |
| Nothing sensitive | Low — and stating this is a legitimate, useful finding |

| Risk | Early warning sign |
| --- | --- |
| **A breach ends the product in this segment** | The security questionnaire's depth in early deals |
| **The security review blocks every sale** | First institutional deal stalling at review |
| **Data sent to a third-party model provider** | The provider's terms and retention policy |
| **Over-broad access because authorization was never located** | `09-technology` cannot name the enforcement point |
| **No recovery capability** | `13-operations` records `restore_tested: never` |

---

# When It Applies

In Move 6 (Register). It also constrains the MVP: for a product holding sensitive data, the security floor is above the
line regardless of ranking.

---

# How to Apply It Here

**Drive the rating from the data classification.** A product holding health data cannot rate breach risk as medium
because the product is small. The consequence is a property of the data.

**Register third-party model providers explicitly.** Sending regulated data to an external provider is a strategic
decision with legal and contractual consequences. `14-ai-systems` and `09-technology` both need it stated.

**Treat the security review as a sales dependency.** In institutional markets it arrives on every deal. Preparing the
documentation once converts a recurring blocker into an asset — and unprepared, it is a `Business.md` risk about
stalled deals.

**Put the security floor above the MVP line.** Access control, audit logging and recovery are obligations. `06-business`
established they are never a paid tier, and `Prioritization.md` puts obligations above ranking.

**Register the absence of recovery as its own risk.** `13-operations` records `restore_tested: yes | no | never`, and
never is the entry that belongs here.

---

# Where It Misleads

**Security is treated as an implementation concern and left to module 09.** The strategic question is what data the
approach requires the product to hold — and that is decided here, in the choice of approach.

**Holding less data is not considered as an option.** The strongest control is not holding it. `09-technology` derives
the data model from requirements, and an approach requiring less sensitive data is a legitimately different option.

**Small scale is assumed to reduce exposure.** It reduces the chance of being targeted and not the consequence.
Notification duties and penalties do not scale down with customer count.

**The provider's terms are assumed acceptable.** Retention, training use and sub-processing all matter to a regulated
buyer, and they are the questions the security review will ask.

**Controls are registered as mitigations without owners or verification.** `Mitigation.md` requires an owner;
`13-operations` requires the evidence and the cadence. A control nobody tests is a control nobody has.

---

# Related

| | |
| --- | --- |
| `Legal.md` | Obligations and liability |
| `Technical.md` | Supplier dependency and data availability |
| `09-technology` | Where authorization is located and controls designed |
| `13-operations` | Incident handling and restore verification |

---

> **Concept Note**
>
> The rating comes from the data, not from the size of the product.
>
> And the strongest control available is choosing an approach that
> never holds it.
