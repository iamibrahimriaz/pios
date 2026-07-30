---
Title: Storage
Module: 09-technology
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Choose datastores from the data model and its obligations, including where files live.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/Tech-Stack.md
Outputs:
  - Storage choices within tech_stack
Related Modules:
  - 02-market
  - 13-operations
Tags:
  - Technology
  - Storage
  - Concept
---

# Storage

---

# What It Is

Where the data actually lives — decided by the model from Move 2 and the obligations from Move 4, not by category
preference.

| Data kind | What decides the store |
| --- | --- |
| Entities with relationships and constraints | Whether the constraints can be enforced by the store itself |
| Documents and uploaded files | Size, access pattern, retention, and whether they contain regulated content |
| Derived or cached data | Whether losing it is recoverable — if yes, it is not storage, it is a cache |
| Audit and history | Append-only behavior, and immutability requirements from Move 4 |
| Secrets | Never in the application store — `security/Secrets.md` |

Two obligations from Move 4 govern all of it: **data residency** — where it may physically be — and **retention**,
which is a column and a scheduled job rather than an intention.

---

# When It Applies

In Move 5 (Choose), constrained by Move 2's classification of every entity: PII, regulated data, retention period, audit
requirement.

---

# How to Apply It Here

**Let the constraints choose the store.** Move 2 encoded business rules as `UNIQUE` and `CHECK` constraints. A store that
cannot enforce them moves those rules into application code, where they are enforced by whoever remembers.

**Locate every regulated field, per store.** Move 4's obligations apply per location. Data split across three stores means
three erasure paths, three retention jobs and three residency questions.

**Decide where files live, explicitly.** Uploaded documents frequently carry the most sensitive content and get the least
design attention. Access control on a file store is a separate mechanism from the one on the database.

**Check residency against `02-market`'s jurisdiction.** A managed service's default region may place regulated data
outside the permitted jurisdiction, which is a blocker rather than a configuration detail.

**Name the erasure path through every store.** Deletion on request means deletion everywhere, including backups, caches
and file storage. `security/Backups.md` covers the awkward part.

---

# Where It Misleads

**Store choice is made by category rather than by constraint.** The useful question is not relational versus document but
whether the rules in Move 2 can be enforced where the data sits.

**Multiple stores are adopted before there is a reason.** Each additional store multiplies the erasure paths, the backup
policies, the residency questions and the failure modes. `13-operations` runs all of them.

**Files are treated as an implementation detail.** They are usually the largest, most sensitive and least indexed data in
the product.

**Retention is recorded as a policy.** Move 4 is explicit: retention is a column plus a scheduled job at a named
enforcement point. A policy with no job is an unmet obligation.

**Backups are assumed to be outside the erasure obligation.** They are not, and the reconciliation between "delete on
request" and "keep backups for 90 days" has to be designed rather than discovered.

---

# Related

| | |
| --- | --- |
| `database/Entities.md` | The model the store must hold |
| `security/Encryption.md` | Protection at rest, per store |
| `security/Backups.md`, `security/Recovery.md` | Retention against erasure |
| `02-market` | Jurisdiction and residency |

---

> **Concept Note**
>
> Every additional store is another erasure path, another backup
> policy and another residency question.
>
> Retention is a column and a job. Written as a policy, it is an
> obligation nobody meets.
