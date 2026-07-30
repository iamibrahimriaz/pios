---
Title: Versioning
Module: 09-technology
Section: knowledge/api
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Decide the versioning approach before there are callers, and know which changes break them.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/api/Endpoints.md
Outputs:
  - Versioning approach within api_contract
Related Modules:
  - 08-product
  - 13-operations
Tags:
  - Technology
  - API
  - Concept
---

# Versioning

---

# What It Is

How the contract changes once something depends on it.

The first question is who the callers are, because it decides how much this matters:

| Callers | Consequence |
| --- | --- |
| Only your own client, deployed together | Versioning is nearly free — change both at once |
| A mobile app users may not update | Old versions live for as long as the installs do |
| Customers' integrations | The contract is a commitment, contractual in institutional markets |
| Public and undocumented use | Anything observable is depended upon |

And what actually breaks a caller:

| Safe | Breaking |
| --- | --- |
| Adding an optional field | Removing or renaming a field |
| Adding an endpoint | Changing a type, or a field's meaning |
| Adding an enum value the client ignores | Adding a required request field |
| Loosening validation | Tightening validation; changing a status code |
| — | Changing default sort or pagination behavior |

---

# When It Applies

In Move 3 (Expose), decided before the first caller exists — because retrofitting a version scheme is itself a breaking
change.

---

# How to Apply It Here

**Choose the mechanism and record it.** Path prefix, header, or per-endpoint. Any is defensible; deciding after callers exist
is not.

**Prefer additive change and keep it that way.** Most evolution can be additive. The discipline is treating removal as a
version event rather than a tidy-up.

**State a deprecation period.** How long an old version is supported, and how callers are told. `13-operations` owns the
communication and the schedule; the commitment is made here.

**Watch the quiet breaking changes.** Default sort order, default page size, pagination strategy and validation strictness are
all depended upon without appearing in any type definition.

**Version the error codes too.** Clients branch on them, so a renamed code is as breaking as a renamed field — which is why
`Errors.md` requires them stable.

---

# Where It Misleads

**Versioning is deferred because there is only one client.** Then a customer integration arrives, and the contract becomes a
commitment with no mechanism for changing it.

**Only the schema is treated as the contract.** Behavior is too: order, defaults, error codes, disclosure policy. Clients
depend on what they observe.

**Supporting two versions is assumed to be cheap.** It is two code paths, two test suites and two sets of edge cases —
`08-product`'s `features/Feature-Lifecycle.md` applies: every version shipped becomes a permanent obligation.

**Deprecation is announced without a date.** An old version with no end date is a permanent version, and the migration never
happens.

**Undocumented behavior is assumed to be free to change.** If it is observable, something depends on it. The contract is what
callers can see, not what was written down.

---

# Related

| | |
| --- | --- |
| `Endpoints.md` | The contract being versioned |
| `Errors.md` | Codes are part of it |
| `Pagination.md`, `Sorting.md` | Defaults callers depend on |
| `13-operations` | Deprecation communication and cadence |

---

> **Concept Note**
>
> Decide the scheme before the first caller, because adding one later
> is itself a breaking change.
>
> The contract is everything observable — including the default sort
> order nobody documented.
