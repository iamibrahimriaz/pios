---
Title: Filtering
Module: 09-technology
Section: knowledge/api
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Expose only the filters requirements need, each with an index behind it.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/api/Endpoints.md
Outputs:
  - Filter parameters within api_contract
Related Modules:
  - 08-product
Tags:
  - Technology
  - API
  - Concept
---

# Filtering

---

# What It Is

The parameters by which a caller narrows a collection — and each one is a commitment.

Every exposed filter is three things at once:

| A filter is | Consequence |
| --- | --- |
| A query the store must serve | It needs an access path — `database/Indexes.md` |
| Part of the contract | Removing it later is a breaking change |
| A cost lever the caller controls | An unindexed filter is a table scan on request |

Which filters exist is not a design choice made here. `08-product`'s behavior descriptions say what the user narrows by —
status, date range, the person it belongs to — and those are the filters.

---

# When It Applies

In Move 3 (Expose), paired with `database/Indexes.md` in Move 2.

---

# How to Apply It Here

**Expose the filters the requirements name, and no others.** A speculative filter is speculative surface: contract,
code, tests and an index nobody needed.

**Give every filter an index and name the query.** Move 2's rule runs the other way too — a filter with no index is a
performance failure waiting for the first customer with real data volume.

**Define the semantics precisely.** Whether a date range is inclusive, whether multiple values mean AND or OR, whether an
absent parameter means "all" — two engineers will differ, which is the two-builder test failing.

**Apply authorization first, always.** Filters narrow within what the caller may see. Filtering the whole table and then
checking permissions is the record-level failure `Authorization.md` describes.

**Cap combinatorial freedom.** Arbitrary filter expressions are a query language, and a query language is a cost surface with
an injection risk. Enumerated parameters are almost always sufficient.

---

# Where It Misleads

**Generic filtering is built to avoid deciding.** A parameter accepting arbitrary field-operator-value expressions looks
flexible and hands query cost, index requirements and injection risk to the caller.

**Filters are added because they are easy.** Each is permanent. Once a client uses it, removal requires a version.

**Semantics are left to convention.** Repeated parameters, comma-separated lists and JSON-encoded filters all appear in the
wild, and none is obvious. Document the one chosen.

**Filtering happens after retrieval.** For small collections it works and for large ones it fails — and in both cases it
breaks pagination, because the page size no longer means anything.

**Unindexed filters pass review.** They work perfectly against test data. Move 6's bottleneck analysis is where they surface,
if it is run.

---

# Related

| | |
| --- | --- |
| `Sorting.md` | The companion parameter, with the same rules |
| `Pagination.md` | Applied after filtering |
| `database/Indexes.md` | The access path each filter requires |
| `Authorization.md` | Applied before filtering, without exception |

---

> **Concept Note**
>
> Every filter is a query, a contract and a cost — expose the ones the
> requirements name and index all of them.
>
> A generic filter expression is a query language you now have to
> secure.
