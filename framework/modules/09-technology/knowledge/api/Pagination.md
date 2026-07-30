---
Title: Pagination
Module: 09-technology
Section: knowledge/api
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Decide the pagination strategy once, and page every collection from the start.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/api/Endpoints.md
Outputs:
  - Pagination within api_contract
Related Modules:
  - 08-product
Tags:
  - Technology
  - API
  - Concept
---

# Pagination

---

# What It Is

How a collection is returned in parts. Two strategies, with a real difference:

| | Offset-based | Cursor-based |
| --- | --- | --- |
| Mechanism | Skip *n*, take *m* | "Everything after this position" |
| Jump to page 7 | Yes | No |
| Behavior when data changes mid-traversal | Items shift — **duplicates and omissions** | Stable |
| Cost at high offsets | Degrades — the store still counts the skipped rows | Constant |
| Requires | Nothing | A stable sort key, and an index for it |

Offset is simpler and correct for small, slow-changing collections where users want page numbers. Cursor is correct for
anything long, anything actively changing, and anything a machine iterates.

**Every collection endpoint is paginated from the beginning.** An unpaginated list works at ten records and fails at ten
thousand, and by then clients depend on receiving everything.

---

# When It Applies

In Move 3 (Expose), decided once and applied uniformly.

---

# How to Apply It Here

**Set a default and a maximum page size.** Without a maximum, page size is a cost lever the caller controls — the same
problem `GraphQL.md` has with query complexity.

**Pair the strategy with an index.** Cursor pagination needs the sort key indexed, which `database/Indexes.md` requires to be
named against the query anyway.

**Decide whether a total count is provided.** Counting is expensive on large tables, and "showing 1–20 of 4,312" is a
product decision with a cost. Frequently "more available" is enough.

**Keep the sort deterministic.** Paginating on a non-unique key produces unstable results at the boundaries. A tiebreaker on
a unique column fixes it, and `Sorting.md` covers it.

**Apply authorization before pagination.** A page of twenty filtered down to twelve after retrieval leaks the existence of
eight, and it also makes page sizes meaningless.

---

# Where It Misleads

**Offset pagination is chosen by default and then breaks quietly.** A user paging through a list while records are being added
sees some records twice and misses others. Nobody reports it as a bug; it looks like confusion.

**Pagination is added when a list gets slow.** By then it is a breaking change to every client, and `Versioning.md` applies.

**Deep offsets are assumed cheap.** Skipping 100,000 rows is work the store still performs, and Move 6 will find it as the
first bottleneck.

**Counts are provided because they look complete.** On a large table the count can cost more than the page.

**Machine consumers are given the human strategy.** An integration iterating everything needs stability, not page numbers.

---

# Related

| | |
| --- | --- |
| `Sorting.md` | The stable order pagination depends on |
| `Filtering.md` | Applied before the page is cut |
| `database/Indexes.md` | The access path the cursor needs |
| `Versioning.md` | Why adding pagination later breaks clients |

---

> **Concept Note**
>
> Paginate every collection from the first version, with a maximum
> page size.
>
> Offset pagination on changing data silently shows some records twice
> and hides others — and nobody ever reports it.
