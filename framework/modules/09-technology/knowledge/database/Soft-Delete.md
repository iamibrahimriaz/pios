---
Title: Soft Delete
Module: 09-technology
Section: knowledge/database
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Distinguish hiding a record from deleting it, and keep the erasure obligation intact.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/database/Relationships.md
Outputs:
  - Deletion semantics within data_model
Related Modules:
  - 02-market
  - 08-product
Tags:
  - Technology
  - Data Model
  - Concept
---

# Soft Delete

---

# What It Is

Marking a record as removed rather than removing it — and the framework's position is that these are **two different
operations serving two different requirements**, and both usually exist.

| Operation | Serves | Data |
| --- | --- | --- |
| **Soft delete** | The user's "remove this" — recoverable, undoable, hides from lists | Retained |
| **Hard delete** | The legal erasure obligation from Move 4 | Gone, including from history, backups and caches |

Conflating them produces the most common compliance failure in this module: a product whose delete is a flag, and whose
"deletion on request" therefore never deletes anything.

Move 4's example is explicit — *deletion on request → hard delete + cascade + audit entry → deletion service.*

---

# When It Applies

In Move 2 (Model) as semantics per entity, and in Move 4 (Protect) where erasure is an obligation.

---

# How to Apply It Here

**Specify both operations where both are required.** The user-facing removal and the legal erasure are different endpoints,
different permissions and different consequences.

**Make hidden records genuinely invisible.** Every query, export, report, search index and count must exclude them. A
soft-delete flag honored in four places out of five is a data leak with a plausible explanation.

**Trace the hard-delete path through the whole model.** `Relationships.md`'s graph is the map: every related row, every
version from `History.md`, every file in object storage, every cache.

**Reconcile erasure with retention.** Some records must be kept for years and some must be erasable on request. Where those
collide, the resolution is a legal question with a designed answer — not something to leave to whoever implements it.

**Record the audit entry for a hard delete.** The deletion itself is an auditable event, and it is the one entry that
outlives the data.

---

# Where It Misleads

**Soft delete is treated as satisfying erasure.** It is the opposite: the data is still there, still in backups, still
searchable by anyone who queries directly. This is the failure that gets discovered during a security review.

**The flag is not applied consistently.** A report, an admin screen or a search index that ignores it will show a record the
user believes is gone.

**Cascade behavior for soft delete is left undefined.** When a parent is hidden, are the children hidden? That is a rule
`08-product` should have specified, and it produces visible bugs when it is not.

**Unique constraints break.** A soft-deleted row still occupies a unique value, so the user cannot re-create it. The
constraint has to account for the flag, which is easy to design and hard to retrofit.

**"Nothing is ever really deleted" is adopted as a principle.** In regulated markets it is unlawful, and it is also the
sentence that appears in incident reports.

---

# Related

| | |
| --- | --- |
| `Relationships.md` | On-delete behavior and the cascade path |
| `History.md` | Versions the erasure must also reach |
| `security/GDPR.md` | Where erasure is the obligation |
| `security/Backups.md` | The hardest part of erasing anything |

---

> **Concept Note**
>
> Hiding and erasing are two operations, and most products need
> both.
>
> A delete that sets a flag does not satisfy a legal erasure — it just
> looks like it does until someone checks.
