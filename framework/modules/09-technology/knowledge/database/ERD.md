---
Title: ERD
Module: 09-technology
Section: knowledge/database
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Use the diagram for orientation, and keep the specification in the table.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/database/Relationships.md
Outputs:
  - Diagram within data_model
Related Modules:
  - 08-product
Tags:
  - Technology
  - Data Model
  - Concept
---

# ERD

---

# What It Is

The entity-relationship diagram — a **navigation aid**, not the model.

What a diagram conveys well and badly:

| Conveys | Does not convey |
| --- | --- |
| Which entities exist | Types, nullability, defaults |
| Which are connected | Constraints and check rules |
| Roughly how many there are | On-delete behavior, reliably |
| Where the clusters are | State machines and forbidden transitions |
| Cardinality, if annotated | Classification — PII, retention, audit |

Everything in the right-hand column is required by the schema test, and none of it survives in a picture. The diagram
orients a reader; the tables specify the system.

---

# When It Applies

In Move 2 (Model), produced after the entity and relationship tables — not instead of them.

---

# How to Apply It Here

**Draw it last.** A diagram drawn first becomes the model, and it is a model missing every property the schema test
requires.

**Annotate cardinality on every line.** An unlabeled line is ambiguous in exactly the way `Relationships.md` warns about,
and readers will each resolve it differently.

**Mark the entities carrying regulated data.** A visual indication of where PII sits is genuinely useful — it makes the
erasure and retention surface visible at a glance.

**Keep it to one page.** A diagram requiring scrolling in two directions is not orienting anyone. If the model is that
large, group it — `architecture/Modules.md` covers grouping.

**Regenerate rather than maintain it.** A hand-drawn diagram diverges from the schema within weeks. Generated from the
model, it cannot.

---

# Where It Misleads

**The diagram gets treated as the deliverable.** It passes review easily — it looks complete — and it fails the schema test
entirely. Reviewers should be reading the tables.

**Diagram tidiness influences the model.** Entities get merged or split to make the picture readable, which is a data
decision taken for a visual reason.

**Stale diagrams mislead more than absent ones.** A picture showing a relationship that no longer exists is worse than no
picture, because it is trusted.

**Cardinality notation is assumed to be understood.** Crow's feet, numbers and arrows are read differently by different
readers. Where it matters, write it in words in the table.

**The diagram substitutes for the classification table.** Where regulated data lives determines most of Move 4's work, and
a diagram cannot carry retention periods or audit requirements.

---

# Related

| | |
| --- | --- |
| `Entities.md` | The specification the diagram orients |
| `Relationships.md` | Cardinality and deletion rules |
| `architecture/Modules.md` | Grouping a large model |
| `08-product` | The requirements behind every box |

---

> **Concept Note**
>
> The diagram orients. The tables specify.
>
> A picture cannot carry a nullability, a retention period or a
> forbidden transition — and those are the parts that get built
> wrong.
