---
Title: Relationships
Module: 09-technology
Section: knowledge/database
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Specify cardinality and on-delete behavior, both of which are business rules.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/database/Entities.md
Outputs:
  - Relationships within data_model
Related Modules:
  - 08-product
Tags:
  - Technology
  - Data Model
  - Method
---

# Relationships

---

# What It Is

How entities connect — and two properties that are business decisions rather than technical ones:

| Property | Why it is a business rule |
| --- | --- |
| **Cardinality** | 1:N and N:M are different products. Whether a note belongs to one patient or several is a clinical rule |
| **On-delete behavior** | Cascade versus restrict decides whether deleting a patient deletes their history — which is a policy question |

Both are gate content: the model must be complete enough to generate a schema, and a relationship without a cardinality
and an on-delete rule is not.

| On-delete | Meaning |
| --- | --- |
| **Restrict** | The parent cannot be deleted while children exist — safest default |
| **Cascade** | Children go too. Correct sometimes, catastrophic when chosen carelessly |
| **Set null** | The child survives, orphaned — requires the column to be nullable, which is itself a rule |

---

# When It Applies

In Move 2 (Model), alongside entity specification.

---

# How to Apply It Here

**Take cardinality from the requirement, and quote it.** If `08-product` did not settle whether one or many, that is an
unmodeled requirement and a regress candidate — not a guess made here.

**Default to restrict and justify anything else.** Cascade deletion is how data disappears unexpectedly. Where it is
correct — a record and its own attachments — say so explicitly.

**Reconcile on-delete with the erasure obligation.** Move 4 requires deletion on request. Restrict-everywhere and
"delete the patient" are in direct tension, and the resolution is a designed deletion path rather than a discovered one.

**Model N:M relationships as their own entity where the link carries data.** A join with a role, a date or a status is an
entity, and treating it as a plain join loses the data the requirement implied.

**State the required-versus-optional side.** Whether the child may exist without a parent is nullability, and it is a rule
about the domain.

---

# Where It Misleads

**Cardinality is chosen for convenience and constrains the product permanently.** Assuming one-to-one because the first
customer works that way makes the second customer a migration.

**Cascade is set to make deletion work in development.** It then works the same way in production, on real data, with no
recovery beyond the backup.

**On-delete is treated as a database detail.** It answers "what happens to their records when a patient leaves", which is a
question with a regulatory answer in most jurisdictions.

**The erasure path is not traced through the relationships.** Deletion on request means every related row across every
store, and the graph of relationships is the map of that work.

**Diagrams show relationships without the rules.** `ERD.md` covers this: a line between two boxes conveys neither
cardinality nor deletion behavior reliably.

---

# Related

| | |
| --- | --- |
| `Entities.md` | The things being related |
| `ERD.md` | The diagram, and what it cannot carry |
| `Soft-Delete.md` | Deletion that is not deletion |
| `security/GDPR.md` | Where erasure becomes an obligation |

---

> **Concept Note**
>
> Cardinality and on-delete are business rules wearing technical
> clothes.
>
> Default to restrict. Cascade is how data vanishes in production
> with nobody having chosen it.
