---
Title: Audit
Module: 09-technology
Section: knowledge/database
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Design the audit trail as an obligation with a mechanism, not as logging.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/database/Entities.md
Outputs:
  - Audit design within data_model and security_model
Related Modules:
  - 02-market
  - 13-operations
Tags:
  - Technology
  - Audit
  - Concept
---

# Audit

---

# What It Is

The record of **who did what to which record, and when** — an obligation in most regulated markets, and distinct from
application logging.

| | Audit trail | Application log |
| --- | --- | --- |
| Purpose | Accountability, and evidence | Diagnosis |
| Audience | Regulators, investigators, the customer | Engineers |
| Retention | Set by the regime, often years | Days or weeks |
| Mutability | Append-only; must not be editable | Freely rotated and dropped |
| Completeness | Every access or change to a classified entity | Whatever was useful |

Move 4's rule applies: the obligation traces to a **named mechanism at a named enforcement point.** For audit, the
enforcement point is the layer through which all access passes — which is why `security/Authorization.md` insists that
layer be locatable.

Note the frequently missed half: in health and financial contexts, **read access is auditable too**, not only changes.

---

# When It Applies

In Move 2 (Model) as a classification per entity, and in Move 4 (Protect) as the mechanism.

---

# How to Apply It Here

**Record which entities require audit, from Move 2's classification.** Not everything does. Auditing everything produces
volume nobody can search and cost nobody budgeted.

**Capture actor, action, target, timestamp and outcome.** Including failed attempts — a denied access is frequently the
most interesting entry in an investigation.

**Make the write unavoidable.** If producing an audit entry is a separate call an engineer can forget, entries will be
missing exactly where they matter. `Backend.md` treats this as a criterion for the backend choice.

**Set retention from the regime and enforce it with a job.** Audit retention frequently exceeds the retention of the data
it describes, which is a real tension `security/GDPR.md` has to resolve deliberately.

**Say who can read it, and prove they cannot alter it.** An audit trail an administrator can edit provides no assurance to
anyone.

---

# Where It Misleads

**Logging is offered where audit is required.** Different retention, different mutability, different completeness
guarantee. A log rotated after seven days does not satisfy a seven-year obligation.

**Read access is omitted.** In clinical and financial systems, who *looked* is the question investigations ask. Designing
for change-only audit fails the obligation while appearing complete.

**Audit is added after the design is fixed.** Retrofitting it means finding every path that touches a classified entity —
which is the work Move 4 exists to do once, in the right order.

**The audit trail contains the sensitive data itself.** Copying regulated values into a long-retention append-only store
creates a second erasure problem with a longer retention period.

**Nobody ever reads it, so its usability is never tested.** `13-operations` needs it during an incident. An audit trail that
cannot be queried by actor and date range is evidence in principle only.

---

# Related

| | |
| --- | --- |
| `History.md` | Change history for product purposes, by contrast |
| `security/Authorization.md` | The enforcement point audit hangs from |
| `security/GDPR.md` | Retention against erasure |
| `13-operations` | Where audit is actually used |

---

> **Concept Note**
>
> Audit is an obligation with a mechanism. Logging is a diagnostic
> convenience.
>
> In regulated work, who looked is as auditable as who changed — and
> it is the half usually missing.
