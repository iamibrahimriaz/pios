---
Title: Authentication
Module: 09-technology
Section: knowledge/security
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Design identity, credential handling and recovery against the real environment.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/security/Authorization.md
Outputs:
  - Authentication within security_model
Related Modules:
  - 03-user
  - 13-operations
Tags:
  - Technology
  - Security
  - Concept
---

# Authentication

---

# What It Is

The security model of identity — as distinct from `api/Authentication.md`, which covers how a credential travels.

| Decision | What decides it |
| --- | --- |
| Factors required | The data classification from Move 2, and the regime from Move 4 |
| Credential storage | Never recoverable — hashed with a current algorithm, or delegated entirely |
| Session lifetime | `03-user`'s environment: shared workstation, personal device, public space |
| Lockout and rate limiting | Balanced against locking a clinician out mid-consultation |
| **Account recovery** | The weakest link in most designs, and the least designed |
| Identity provider | Whether the buyer's organization requires single sign-on |

**Recovery is the part that undoes the rest.** A system with strong authentication and a reset flow that relies on a single
email account has the security of that email account.

---

# When It Applies

In Move 4 (Protect), constrained by `03-user`'s conditions of use.

---

# How to Apply It Here

**Delegate identity where the buyer expects it.** Institutional customers frequently require single sign-on, and it is both
more secure and a procurement requirement. That makes it a `06-business` consideration as much as a technical one.

**Set session lifetime from the environment, not from convention.** A shared clinical workstation needs a short session and a
fast re-entry path. A personal device does not. `03-user` recorded which.

**Design recovery as carefully as sign-in.** Who can trigger it, what proves identity, what is notified, what is audited. In a
regulated product an unaudited reset is an access-control gap.

**Balance lockout against the cost of being locked out.** Aggressive lockout in a clinical setting has a patient-safety
dimension. Rate limiting with escalating delays is usually the better instrument.

**Audit authentication events, including failures.** `database/Audit.md` requires denied attempts, and repeated failures are
the earliest signal `13-operations` gets of an attack.

---

# Where It Misleads

**Recovery is treated as a usability feature.** It is an authentication path with a lower bar than the front door, and it is
where accounts are actually taken.

**Credential handling is implemented rather than delegated.** Storing passwords is a permanent obligation to keep current with
hashing practice. Delegation removes the class of risk entirely.

**Session lifetime is chosen for convenience.** Long sessions on shared devices mean the next person inherits the last person's
access — which in a clinical setting is an audited access-control failure.

**Second factors are added without considering the environment.** A factor requiring a personal phone fails where phones are
prohibited, and `03-user`'s immovables should have said so.

**Machine and human identity share one mechanism.** Different lifetimes, different revocation and different audit needs, as
`api/Authentication.md` sets out.

---

# Related

| | |
| --- | --- |
| `api/Authentication.md` | How the credential travels |
| `Authorization.md` | What the identity may do |
| `Secrets.md` | Where signing material lives |
| `03-user` | Devices, environment and immovables |

---

> **Concept Note**
>
> The account-recovery flow is your real authentication mechanism,
> because it is the weakest one you have.
>
> Design it with the same care as sign-in, and audit it the same
> way.
