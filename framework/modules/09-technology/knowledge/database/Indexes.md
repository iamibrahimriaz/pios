---
Title: Indexes
Module: 09-technology
Section: knowledge/database
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Require every index to name the query it serves.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/database/Entities.md
Outputs:
  - Indexes within data_model
Related Modules:
  - 08-product
Tags:
  - Technology
  - Data Model
  - Concept
---

# Indexes

---

# What It Is

The access paths — and the framework's rule about them is a single sentence:

> Each names the query it serves. **An index with no query is a guess.**

Where the queries come from is not mysterious. They are already implied:

| Source | Query it implies |
| --- | --- |
| `08-product`'s behavior descriptions | The lookups each operation performs |
| The API operations from Move 3 | Every filter, sort and pagination key |
| Uniqueness constraints from Move 2 | The unique index that enforces them |
| Foreign keys from `Relationships.md` | Lookups in the child direction |
| `12-metrics`' event queries | Reporting access patterns, which differ from operational ones |

---

# When It Applies

In Move 2 (Model), and revisited in Move 6 (Size) where the first bottleneck is named — usually a query.

---

# How to Apply It Here

**Write the query beside each index.** One line: which operation, which filter, which sort. That pairing makes the index
reviewable and makes an unnecessary one visible.

**Index what the API exposes.** `api/Filtering.md` and `api/Sorting.md` define which fields a caller may filter and sort
by. Every one of those needs an access path, or the endpoint is a table scan with a nice interface.

**Enforce uniqueness with a unique index.** It is Move 2's constraint discipline: a rule the database holds cannot be
forgotten by application code.

**Separate reporting access from operational access.** Aggregate queries have different shapes, and in Move 6 they are
frequently the first bottleneck. Serving both from the same indexes is where that bottleneck comes from.

**Say what is deliberately not indexed.** A large table scanned rarely by an administrator is a legitimate choice, and
stating it stops someone treating it as an oversight.

---

# Where It Misleads

**Indexes get added speculatively because they seem harmless.** Each one costs write performance and storage, and an
unused index is permanent overhead nobody removes because nobody knows what it was for.

**Foreign keys are assumed to be indexed.** Depending on the store, they may not be, and the child-direction lookup is one
of the most common queries in any model.

**Indexing is deferred as an optimization.** The access paths are derivable from the requirements now, and Move 6 requires
the first bottleneck named — which cannot be done without knowing them.

**Composite index order is treated as arbitrary.** It determines which queries the index can serve. The order follows from
the query, which is why the query must be written down.

**Full-text needs are met with an index.** They usually are not; `Search.md` covers why search is a separate design
decision rather than a column property.

---

# Related

| | |
| --- | --- |
| `Entities.md` | Where constraints and indexes are specified |
| `Search.md` | When an index is the wrong tool |
| `api/Filtering.md`, `api/Sorting.md` | The exposed access paths |
| `scalability/Performance.md` | Where the missing index surfaces |

---

> **Concept Note**
>
> Write the query next to the index.
>
> An index with no named query is a guess with a permanent write
> cost — and nobody will ever dare remove it.
