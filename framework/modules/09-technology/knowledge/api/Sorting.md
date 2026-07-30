---
Title: Sorting
Module: 09-technology
Section: knowledge/api
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Make ordering deterministic, because pagination depends on it.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/api/Pagination.md
Outputs:
  - Sort parameters within api_contract
Related Modules:
  - 08-product
Tags:
  - Technology
  - API
  - Concept
---

# Sorting

---

# What It Is

The order in which a collection is returned — and the property that matters is **determinism**.

| Requirement | Why |
| --- | --- |
| **A default order, always** | Unordered results are returned in whatever order the store finds convenient, and it changes |
| **A unique tiebreaker** | Sorting on a non-unique column leaves ties resolved arbitrarily, which breaks pagination at page boundaries |
| **An index per sortable field** | Same rule as filtering — sorting an unindexed column sorts the whole table |
| **Explicit direction** | Ascending or descending, stated rather than assumed |

The pagination link is the practical reason to care: with a non-deterministic sort, a record can appear on two consecutive
pages or on neither, and the symptom looks like data loss.

---

# When It Applies

In Move 3 (Expose), alongside pagination and filtering.

---

# How to Apply It Here

**Set a default sort per collection, from the requirement.** What order the user expects is a product question `08-product`
answered — most recent first, alphabetical, by due date.

**Add a unique tiebreaker to every sort.** Usually the primary key. It costs nothing and it removes the entire class of
boundary bugs.

**Expose only the sortable fields the requirements need.** Each is a contract commitment and an index, exactly as with
filtering.

**State how nulls sort.** First or last is a visible product behavior, and the store's default may not be what the user
expects.

**Define what happens for an unsupported sort field.** A 400 naming the supported values, per `Errors.md`. Silently ignoring
it produces results in the wrong order with no indication.

---

# Where It Misleads

**No default sort is specified and the results look stable in testing.** They are stable until the data grows, the plan
changes, or a replica answers — and then the order shifts with no code change.

**Sorting on a timestamp is assumed to be unique.** Two records created in the same second tie, and the tie resolves
differently on each query. This is the most common cause of pagination anomalies.

**Sortable fields are added generously.** Each requires an index, and a sort on an unindexed column is a full sort of the
table for every request.

**Sorting is applied in the client.** It then only orders the current page, which is not sorting — it is rearranging a
subset, and the user sees a list that appears wrongly ordered.

**Multi-field sort semantics are left implicit.** Which field takes precedence, and whether directions can differ per
field, must be documented or two implementations will differ.

---

# Related

| | |
| --- | --- |
| `Pagination.md` | What depends on determinism |
| `Filtering.md` | The same index and contract rules |
| `database/Indexes.md` | Composite order follows the query |
| `Errors.md` | Rejecting unsupported values |

---

> **Concept Note**
>
> Every sort needs a unique tiebreaker.
>
> Without one, records appear on two pages or on none — and it reads as
> data loss, not as a sorting bug.
