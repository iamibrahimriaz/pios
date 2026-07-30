---
Title: GDPR
Module: 09-technology
Section: knowledge/security
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Convert data-protection obligations into mechanisms, and never claim compliance.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/security/Authorization.md
Outputs:
  - Data-protection mechanisms within security_model
Related Modules:
  - 02-market
  - 13-operations
Tags:
  - Technology
  - Security
  - Concept
---

# GDPR

---

# What It Is

A data-protection regime whose obligations, where it applies, become **mechanisms at enforcement points** in this module.

The framework's rule governs everything here:

> "We will be compliant with «regime»" is not a control. It is a hope with a citation.

Obligations most likely to shape the design — each stated as a mechanism, not a regime name:

| Obligation | Mechanism | Enforcement point |
| --- | --- | --- |
| Erasure on request | Hard delete + cascade through every store and version + audit entry | Deletion service |
| Data minimization | Only fields a requirement needs — Move 1's orphan rule applied to columns | Data model |
| Purpose limitation | The stated purpose per field, including whether it may train a model | Data model, and `14-ai-systems` |
| Access on request | Export of a subject's data in a portable form | Export operation |
| Retention limits | Retention column + scheduled job | Datastore + job runner |
| Breach notification within a deadline | Detection, assessment and a communication runbook | `13-operations` |
| Records of processing | Documented, maintained on a cadence | `13-operations` |

**This is not legal advice, and this framework does not determine applicability.** `02-market` Frame 2 establishes which regimes
apply; this module builds the mechanisms for the obligations that module found.

---

# When It Applies

In Move 4 (Protect), where Frame 2 identified the regime.

---

# How to Apply It Here

**Trace the erasure path through every store and every version.** `database/Soft-Delete.md`, `database/History.md` and
`Backups.md` each hold part of it. An erasure that reaches only the current row has not occurred.

**Apply minimization at the column level.** A field with no requirement behind it is an orphan under Move 1 and a liability
under the regime. The two arguments agree.

**State the purpose per field, including model training.** Whether customer data may be used to improve a model is a purpose
question with a legal answer, and `14-ai-systems` requires data rights stated as legal claims rather than as access.

**Make retention a job, not a policy.** Move 4 is explicit about the format, and a policy with no scheduled enforcement is an
unmet obligation.

**Treat an obligation with no mechanism as a blocker.** Not a risk: *a risk is something that might cost you; an unmet legal
obligation means the product cannot lawfully operate.*

---

# Where It Misleads

**Compliance is written as a state.** `13-operations` is explicit: it is a cadence with an owner and evidence produced. A control
that existed once is not a control.

**Erasure is implemented as a flag.** That is the failure `database/Soft-Delete.md` names, and it is the most common serious
gap in this area.

**Backups are treated as out of scope.** They are not, and the reconciliation must be written down before a buyer asks.

**Consent is treated as the basis for everything.** There are several lawful bases and consent is frequently the weakest choice
for a professional product. Which basis applies is a legal determination, not a technical default.

**A privacy policy is mistaken for a mechanism.** It is a disclosure. The mechanism is the deletion service, the retention job
and the audit trail.

---

# Related

| | |
| --- | --- |
| `HIPAA.md` | A different regime, the same mechanism discipline |
| `database/Soft-Delete.md`, `database/History.md` | The erasure surface |
| `Backups.md` | The copies erasure must reach |
| `02-market`, `13-operations` | Applicability, and the compliance schedule |

---

> **Concept Note**
>
> Obligation, mechanism, enforcement point, citation — for every
> requirement the regime imposes.
>
> An obligation with no mechanism is a blocker, not a risk. The
> product cannot lawfully operate.
