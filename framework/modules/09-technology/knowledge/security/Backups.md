---
Title: Backups
Module: 09-technology
Section: knowledge/security
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Design backups against a stated recovery objective, and reconcile them with erasure.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/security/Encryption.md
Outputs:
  - Backup design within security_model
Related Modules:
  - 02-market
  - 13-operations
Tags:
  - Technology
  - Security
  - Concept
---

# Backups

---

# What It Is

Copies of the data, designed against two numbers that must be stated rather than assumed:

| | Question | Consequence |
| --- | --- | --- |
| **Recovery point** | How much data may be lost? | Sets the backup frequency |
| **Recovery time** | How long may restoration take? | Sets the method and the rehearsal |

Both come from the product, not from convention. For a clinical documentation tool, losing a day of notes is a patient-safety
event; for an internal reporting tool it may be an inconvenience.

And the tension this file exists to name:

> Deletion on request means deletion everywhere. Backups are the copies that outlive the data.

A retention policy of 90 days for backups and an obligation to erase on request are in direct conflict, and the resolution has
to be designed — commonly by documenting that erasure completes within the backup cycle, and ensuring restores re-apply
outstanding erasures.

---

# When It Applies

In Move 4 (Protect). `Recovery.md` covers verification; `13-operations` records `restore_tested: yes | no | never`.

---

# How to Apply It Here

**State both objectives as numbers, sourced from the product.** They are the design inputs, and without them backup frequency
is arbitrary.

**Reconcile with erasure explicitly, in writing.** How an erasure request interacts with existing backups, and what happens if a
restore reintroduces erased data. This is the answer a security review asks for and almost nobody has.

**Keep at least one copy outside the primary environment.** A backup in the same account as the data is protection against
corruption, not against account compromise or accidental deletion of the environment.

**Encrypt them, with keys not stored alongside.** They contain everything, they live longer, and they are frequently the copy in
the least controlled location.

**Cover every store.** `Storage.md`'s point applies: files, search indexes and caches are data too, and a backup covering only
the database restores a partially functional system.

---

# Where It Misleads

**Backups are assumed to exist because the provider mentions them.** Provider defaults may be shorter than needed, may not cover
every store, and may not be restorable in the form required.

**A backup is treated as a recovery capability.** It is not until a restore has been performed. `Recovery.md` and
`13-operations`' `restore_tested: never` exist because this is the most common gap in small products.

**The erasure conflict is discovered during a security review.** It is entirely predictable and cheap to resolve on paper, and
expensive to resolve under questioning.

**Backups are excluded from the classification.** They hold regulated data, so residency, retention and encryption obligations
apply to them exactly as to the primary store.

**Frequency is chosen by cost alone.** The recovery point objective is a product decision, and if cost forces it lower, that is
a trade the operator should make knowingly.

---

# Related

| | |
| --- | --- |
| `Recovery.md` | Whether the backup actually works |
| `Encryption.md` | Protecting the copies |
| `database/Soft-Delete.md` | Hard delete versus what backups hold |
| `13-operations` | Restore verification, on a cadence |

---

> **Concept Note**
>
> State how much data may be lost and how long recovery may take —
> both from the product, not from convention.
>
> Then answer how erasure and backups coexist. That question always
> arrives, and usually from a buyer.
