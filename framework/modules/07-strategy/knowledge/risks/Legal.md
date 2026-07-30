---
Title: Legal Risks
Module: 07-strategy
Section: knowledge/risks
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Register regulatory and liability risks as obligations with owners, not as regime names.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 07-strategy/knowledge/risks/Mitigation.md
Outputs:
  - Legal risks within risk_register
Related Modules:
  - 02-market
  - 09-technology
  - 13-operations
Tags:
  - Strategy
  - Risk
  - Concept
---

# Legal Risks

---

# What It Is

The risks arising from law, regulation and liability — carried forward from `02-market` Frame 2 and stated as
**obligations**, never as regime names.

> "GDPR applies" is not a finding. "Personal data must be erasable on request, which requires an erasure path through
> every store" is one.

| Risk | Early warning sign |
| --- | --- |
| **A regime excludes the chosen segment** | Frame 2 should have caught it; if not, procurement will |
| **Certification is required before selling** | Buyer questionnaires asking for it |
| **The AI mechanism is restricted for this use** | Regulatory guidance and direction of travel |
| **Data rights are assumed rather than held** | No written basis for using the data |
| **Liability for an automated decision is unallocated** | Contract negotiation raising it |
| **Regulation is tightening on the mechanism** | Consultations, draft guidance, enforcement actions |
| **Professional-body rules constrain the workflow** | Practitioner reluctance nobody can explain in product terms |

The framework's rule from `09-technology` applies throughout: **never claim compliance.** Record the obligation, the
mechanism that addresses it, where it is enforced, and the citation.

---

# When It Applies

In Move 6 (Register). `09-technology` turns these into mechanisms and enforcement points; `13-operations` turns them
into a schedule with evidence.

---

# How to Apply It Here

**State data rights as legal claims, with a basis.** `14-ai-systems` requires this: having access to data is not the
same as having the right to use it for this purpose. An unstated basis is the risk.

**Register liability allocation for anything automated.** Where the product produces an output a professional acts on,
someone carries responsibility for a wrong one. Institutional contracts will raise it, and it is cheaper to have an
answer than to negotiate one.

**Attach the certification lead time and cost.** From Frame 2. A twelve-month certification is a sequencing constraint
and a `Financial.md` entry, not just a legal note.

**Watch the direction of travel, not only the current rules.** Frame 2 recorded whether the regime is tightening,
stable or loosening. A mechanism legal today and being consulted on is a dated risk.

**Register professional-body constraints separately from law.** They are frequently stricter, less visible, and more
predictive of practitioner behavior than the statute.

---

# Where It Misleads

**Regime names get registered instead of obligations.** A register listing three acronyms tells nobody what to build or
what to schedule. The obligation is the actionable unit.

**Compliance is treated as a state rather than a schedule.** `13-operations` is explicit: compliance is a cadence with
an owner and **evidence produced**. A risk marked mitigated because a control exists is a risk nobody is maintaining.

**Legal review is deferred until launch.** By then the architecture and the requirements are set, and the obligations
`09-technology` should have derived have been built around instead.

**The AI-specific exposure is omitted.** Automated decisions, explainability requirements, training-data provenance and
sector-specific guidance are current, moving, and jurisdiction-specific. `14-ai-systems` needs them named.

**"We will get advice later" is recorded as a mitigation.** It is a plan to find out, without an owner or a date.
`Mitigation.md` requires both.

---

# Related

| | |
| --- | --- |
| `Security.md` | Breach and exposure risk |
| `Technical.md` | Where data rights meet feasibility |
| `02-market` | Frame 2, and the direction of travel |
| `09-technology`, `13-operations` | Mechanisms, and the compliance schedule |

---

> **Concept Note**
>
> Register obligations, not regime names — and never record
> compliance as achieved.
>
> A control with no owner and no cadence is a control that existed
> once.
