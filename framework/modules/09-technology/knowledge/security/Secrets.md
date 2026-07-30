---
Title: Secrets
Module: 09-technology
Section: knowledge/security
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Keep credentials out of the codebase and make rotation a procedure that exists.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/security/Encryption.md
Outputs:
  - Secret handling within security_model
Related Modules:
  - 13-operations
Tags:
  - Technology
  - Security
  - Concept
---

# Secrets

---

# What It Is

The credentials the system holds, and where they live.

| Secret | Consequence if exposed |
| --- | --- |
| Database credentials | Full data access, bypassing every application check |
| Encryption keys | Encryption at rest becomes decorative |
| Third-party API keys — including model providers | Someone else's bill, and possibly their data |
| Signing keys for tokens | Any identity can be forged |
| Deployment credentials | Arbitrary code in production |
| Customer-supplied credentials for integrations | Their systems, not just yours |

The last row is the one that changes the calculation: holding a customer's credentials to another system makes a breach here a
breach there, and it is a liability question as much as a technical one.

---

# When It Applies

In Move 4 (Protect), and enforced continuously by `09-technology/knowledge/CI-CD.md`'s scanning.

---

# How to Apply It Here

**Name where each secret is stored.** A managed secret store, environment variables from a controlled source, or a
platform-provided mechanism. "Not in the repository" is a floor, not a design.

**Write the rotation procedure.** For each secret: how it is replaced, whether the system tolerates two valid values during the
change, and how long it takes. `13-operations`' 3am test applies — a rotation nobody has performed is a hypothesis.

**Scan continuously, not once.** Secrets enter repositories by accident, repeatedly. The pipeline is where that becomes
impossible rather than unlikely.

**Keep secrets out of logs and error responses.** `api/Errors.md` covers the response side; connection strings and tokens in log
output are the other common path.

**Treat customer-supplied credentials as their data.** Scope them as narrowly as the integration allows, store them encrypted
with a key they do not share, and state how they are revoked.

---

# Where It Misleads

**"Not committed to git" is treated as the whole requirement.** Secrets also live in CI configuration, in developer machines, in
logs, in error trackers and in support tickets.

**Rotation is assumed to be possible and never tested.** Many systems cannot accept two valid keys at once, which means
rotation is an outage. Knowing that in advance changes the design.

**Exposure is treated as a low-likelihood event.** It is routine, which is why scanning and rotation are the mechanisms rather
than care.

**Model provider keys are treated as low value.** They are a direct financial exposure — usage is billed — and for
`14-ai-systems` that cost is already in the margin arithmetic.

**Secrets are shared between environments.** One credential valid in staging and production means a staging compromise is a
production compromise.

---

# Related

| | |
| --- | --- |
| `Encryption.md` | What the keys protect |
| `09-technology` `CI-CD.md` | Continuous scanning |
| `09-technology` `Deployment.md` | Deployment credentials |
| `13-operations` | Rotation as a scheduled procedure |

---

> **Concept Note**
>
> Name the store and write the rotation steps.
>
> A rotation procedure nobody has executed is not a procedure — and
> you will find that out on the day it is urgent.
