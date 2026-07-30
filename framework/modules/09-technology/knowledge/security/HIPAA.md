---
Title: HIPAA
Module: 09-technology
Section: knowledge/security
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show how a sector regime becomes mechanisms, including the access-audit obligation.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/security/GDPR.md
Outputs:
  - Health-data mechanisms within security_model
Related Modules:
  - 02-market
  - 13-operations
Tags:
  - Technology
  - Security
  - Concept
---

# HIPAA

---

# What It Is

A United States regime governing protected health information — included here as the worked example of a **sector** regime, as
opposed to `GDPR.md`'s general data-protection one.

Two features make it structurally different, and both change the design:

| Feature | Consequence |
| --- | --- |
| **Access is auditable, not only change** | Who *looked* at a record must be recorded — `database/Audit.md`'s most-missed half |
| **Minimum necessary access** | Authorization must be relational, not role-based: the treating clinician, not "clinicians" |

Plus obligations that flow into other files:

| Obligation | Mechanism | Enforcement point |
| --- | --- | --- |
| Access restricted to the treating relationship | Record-level authorization check | Query layer |
| Access logged, including reads | Audit entry on every access to a classified entity | The located enforcement point |
| Agreements with any processor handling the data | Contractual, before the service is used | Procurement — including model providers |
| Breach assessment and notification | Detection, assessment, communication runbook | `13-operations` |
| Workforce access controls and training | Access review on a cadence, with evidence | `13-operations` |

**This is not legal advice, and applicability is `02-market` Frame 2's determination** — including whether the operator is a
covered entity or a processor, which changes the obligations substantially.

---

# When It Applies

In Move 4 (Protect), where Frame 2 identified US health data in scope.

---

# How to Apply It Here

**Design read-auditing from the start.** Retrofitting it means finding every path that touches a record, which is the work Move
4's ordering exists to do once.

**Make authorization relational.** `security/Authorization.md`'s point becomes an obligation here: minimum-necessary cannot be
expressed with roles alone.

**Check every third party that touches the data, including model providers.** Sending health information to an external
inference service requires the appropriate agreement in place. `14-ai-systems` treats data rights as legal claims for exactly
this reason.

**Include the operator's own staff in the access model.** Who at the vendor can view customer records, when, and with what audit
entry — institutional buyers will ask, and the answer should exist before they do.

**Expect certification and questionnaire cost.** `02-market` Frame 2 costed it; `06-business/knowledge/pricing/Enterprise.md`
prices the review it triggers on every deal.

---

# Where It Misleads

**A provider's compliance is read as the product's.** Infrastructure that supports the regime does not make an application
compliant. The mechanisms above are the application's responsibility.

**Read-auditing is omitted because change-auditing feels complete.** It is the specific obligation most often missed, and it is
the one investigations rely on.

**Role-based access is offered for minimum-necessary.** A role grants access to a category; the obligation is about a
relationship to a specific patient.

**Model providers are treated as infrastructure.** They are processors receiving the data, and the agreement is a precondition
rather than a formality.

**Compliance is claimed.** Move 4 forbids it, and in this regime the claim carries specific consequences. Record the obligation
and the mechanism; let an assessor draw the conclusion.

---

# Related

| | |
| --- | --- |
| `GDPR.md` | The general-regime counterpart |
| `database/Audit.md` | Read access as an auditable event |
| `Authorization.md` | Relational rules over roles |
| `02-market`, `14-ai-systems` | Applicability, and data rights for models |

---

> **Concept Note**
>
> In health data, who looked is as auditable as who changed — and
> "clinicians" is not minimum-necessary access.
>
> The relationship is the rule, and it has to live in the query.
