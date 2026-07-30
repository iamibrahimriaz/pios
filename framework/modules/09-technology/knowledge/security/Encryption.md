---
Title: Encryption
Module: 09-technology
Section: knowledge/security
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Apply encryption where it addresses a stated threat, and know what it does not protect against.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/security/Authorization.md
Outputs:
  - Encryption within security_model
Related Modules:
  - 02-market
Tags:
  - Technology
  - Security
  - Concept
---

# Encryption

---

# What It Is

Protection of data by making it unreadable without a key — and the honest question is always **which threat it addresses**.

| Where | Protects against | Does not protect against |
| --- | --- | --- |
| **In transit** | Interception on the network | Anything at either end |
| **At rest, whole-disk or provider-managed** | Stolen media, decommissioned hardware | A compromised application, or a valid query |
| **At rest, field-level** | Direct database access, and some insider access | The application, which must be able to read it |
| **End-to-end** | Everyone including the operator | Nothing the endpoints do |

The pattern worth stating plainly: **encryption at rest does very little against the most likely breach**, which is
compromised application access or a missing authorization check. `Authorization.md` addresses that threat; encryption
addresses a different, narrower one.

It is nonetheless frequently a **stated obligation** in Move 4, and a procurement requirement. Both are legitimate reasons to
have it.

---

# When It Applies

In Move 4 (Protect), per data classification from Move 2.

---

# How to Apply It Here

**State the threat each measure addresses.** "At rest, provider-managed, addressing physical media and the buyer's security
questionnaire" is honest. "Encrypted for security" is not a design.

**Use transport encryption everywhere, without exception.** Internal service traffic included; it is nearly free and its
absence is a finding in any review.

**Apply field-level encryption selectively.** It breaks indexing, searching and constraints on the encrypted column, which is
a real cost. Reserve it for fields where the narrower threat matters.

**Say where the keys live and who can reach them.** `Secrets.md` covers it. Encryption with keys stored beside the data
addresses almost nothing.

**Record it as an obligation where the regime names it.** Move 4's format applies: obligation, mechanism, enforcement point,
citation.

---

# Where It Misleads

**Encryption at rest is treated as the answer to "is the data safe".** It answers a narrow question. The likely breach path is
a valid-looking query with a missing authorization check, and no encryption prevents that.

**Field-level encryption is applied broadly and breaks the model.** An encrypted column cannot be uniquely constrained,
indexed usefully or searched — which conflicts directly with Move 2's constraint discipline.

**Key management is left implicit.** The keys are the system's most sensitive secret, and where they live is the whole
strength of the measure.

**"Encrypted" is claimed without specifying which kind.** In a security questionnaire that ambiguity becomes a
misrepresentation, and Move 4's rule — never claim compliance — applies.

**Backups are excluded.** They contain the same data with a longer life. `Backups.md` covers them, and they are the copy most
likely to be somewhere unexpected.

---

# Related

| | |
| --- | --- |
| `Secrets.md` | Where the keys live |
| `Authorization.md` | The threat encryption does not address |
| `Backups.md` | The copies that outlive the data |
| `02-market` | Where encryption is a named obligation |

---

> **Concept Note**
>
> Say which threat each measure addresses.
>
> Encryption at rest protects against stolen hardware. It does nothing
> about the missing authorization check, which is how the data
> actually leaves.
