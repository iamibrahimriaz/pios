---
Title: Entities
Module: 09-technology
Section: knowledge/database
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Derive entities from requirements and specify them well enough to generate a schema.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/core/06-Framework.md
Outputs:
  - data_model
Related Modules:
  - 08-product
Tags:
  - Technology
  - Data Model
  - Method
---

# Entities

---

# What It Is

The things the system contains — **derived** from `08-product`'s requirements, never invented.

Three passes produce them: nouns give candidate entities, verbs give operations, adjectives and states give state
machines and enumerations. Then the check runs in both directions:

| Failure | What it means |
| --- | --- |
| **Orphan entity** — no requirement mentions it | Speculative modeling. Remove it |
| **Unmodeled requirement** — its data is nowhere | The model is incomplete, or the requirement is vague |

> An unmodeled requirement usually means the requirement left its data implicit. That is `08-product`'s defect, and the
> correct response is to name it and regress — not to invent the missing entity here, where nobody will know it was
> invented.

The specification bar is the module's defining standard:

> **The schema test.** Could an engineer or a coding agent generate the schema from this document without asking a single
> follow-up question?

---

# When It Applies

In Move 1 (Derive) and Move 2 (Model), before interfaces and before technology.

---

# How to Apply It Here

**Give every column a type, a nullability and a default.** "A date" is three different columns. Anything left out is a
decision handed to whoever builds it, made without any of this context.

**Classify every entity.** PII, regulated data, retention period, audit requirement. Move 4's obligations attach to these
classifications, and `12-metrics` runs its privacy check against them.

**Encode rules as constraints.** A business rule in prose is enforced by whoever remembers it; the same rule as a `CHECK`
or `UNIQUE` is enforced by the database. Where a requirement can be a constraint, make it one.

**Model state machines including the forbidden transitions.** Which transitions are impossible is where the bugs live, and
it is the half usually omitted.

**Name the requirement each entity serves.** That reference is what makes the orphan check mechanical rather than a
judgment.

---

# Where It Misleads

**The model gets built from a mental picture and reconciled afterwards — and it always reconciles.** Deriving in the stated
direction means the requirements chose the entities rather than confirming them.

**Speculative fields arrive for future use.** An unused column is architecture inflation at the schema level, and it will be
populated inconsistently by the time anyone needs it.

**Nullability is left to the implementer.** It is a business rule: whether a value may be absent is something the
requirements answered, or should have.

**Classification is skipped for entities that seem innocuous.** A free-text note field in a clinical product contains
regulated data by default, and Move 4's erasure and retention obligations apply to it.

**Constraints are omitted as an optimization.** They are requirements in their strongest form. Omitting them moves
enforcement into code where it is optional.

---

# Related

| | |
| --- | --- |
| `Relationships.md` | Cardinality and on-delete behavior |
| `ERD.md` | The model as a diagram, and its limits |
| `Audit.md`, `History.md` | Obligations attached to classification |
| `08-product` | The requirements entities are derived from |

---

> **Concept Note**
>
> Could someone generate the schema without asking one question?
>
> A rule written in prose is enforced by memory. The same rule as a
> constraint is enforced by the database.
