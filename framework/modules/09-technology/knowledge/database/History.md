---
Title: History
Module: 09-technology
Section: knowledge/database
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Decide whether previous versions are a product requirement before storing them.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/database/Audit.md
Outputs:
  - Versioning design within data_model
Related Modules:
  - 08-product
Tags:
  - Technology
  - Data Model
  - Concept
---

# History

---

# What It Is

Keeping previous versions of a record — as a **product capability**, distinct from `Audit.md`'s accountability obligation.

| Approach | Suits |
| --- | --- |
| **No history** | Records whose previous values have no use — the correct default |
| **Versioned rows** — each change a new row | Records users compare, revert or cite: documents, notes, quotes |
| **Change log** — field, old value, new value | Where the *diff* is the product feature |
| **Point-in-time reconstruction** | Regulated records that must be shown as they were on a date |

The last one is a real requirement in clinical and financial contexts: what the record said when a decision was taken,
not what it says now.

The question that decides all of it: **does a requirement in `08-product` use the previous version?** If not, storing it is
speculative modeling with a retention consequence.

---

# When It Applies

In Move 2 (Model), as an entity-level decision derived from requirements.

---

# How to Apply It Here

**Point at the requirement.** History is expensive in storage, in query complexity and in erasure obligations. It needs a
named requirement, like any other entity.

**Distinguish it from audit explicitly.** Audit answers who and when for accountability; history answers what it said, for
the user. A product may need both, and they have different retention periods.

**Include history in the erasure path.** Deletion on request means every version, not the current one. This is the most
commonly missed part of an erasure design.

**Decide what a version contains.** Whole-record snapshots are simple and large; field-level diffs are compact and harder
to reconstruct. The choice follows from whether the user views versions or the differences between them.

**Cap it, and say so.** "The last ten versions" or "12 months" is a design. Unbounded history is a storage line that grows
forever and a retention obligation nobody set.

---

# Where It Misleads

**History is added because it feels prudent.** It is a permanent cost with no requirement behind it — an orphan entity by
Move 1's rule.

**It is conflated with audit and satisfies neither.** A versioned table users can edit is not an audit trail; an
append-only audit log is not a usable version history.

**Erasure is applied to the current row only.** Every prior version holds the same regulated data, and an erasure that
misses them has not occurred.

**Reconstruction is assumed to be possible from a change log.** It is, until one migration changes the shape of the fields
being logged. Point-in-time requirements need the design to state how a migration is handled.

**Unbounded growth is discovered in Move 6.** History tables are frequently the largest in a system and the first
bottleneck for the queries that touch them.

---

# Related

| | |
| --- | --- |
| `Audit.md` | Accountability, with different rules |
| `Soft-Delete.md` | Records that are hidden rather than removed |
| `security/GDPR.md` | Erasure across every version |
| `08-product` | The requirement that justifies history |

---

> **Concept Note**
>
> Store previous versions only where a requirement reads them.
>
> And when erasure comes, it applies to every version — that is the
> part designs forget.
