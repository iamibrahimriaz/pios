---
Title: REST
Module: 09-technology
Section: knowledge/api
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Use resource conventions where they fit, and name operations where they do not.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/api/Endpoints.md
Outputs:
  - Contract style within api_contract
Related Modules:
  - 08-product
Tags:
  - Technology
  - API
  - Concept
---

# REST

---

# What It Is

A convention: resources identified by path, operations expressed with standard methods, state carried in representations.

Its value is entirely in predictability — a caller can guess the shape and be right.

| Method | Semantics that matter here |
| --- | --- |
| GET | Safe, repeatable, cacheable, and must never change state |
| POST | Creates or invokes; not idempotent unless made so deliberately |
| PUT | Replaces; idempotent |
| PATCH | Modifies partially; the semantics of a partial update need stating |
| DELETE | Idempotent — deleting twice is not an error |

The honest limitation: **not every operation is a resource transition.** "Submit for approval", "recalculate", "send the
reminder" are actions. Forcing them into resource shapes produces contortions, and naming them plainly is clearer than a
convention observed awkwardly.

---

# When It Applies

In Move 3 (Expose), as the default style for most products.

---

# How to Apply It Here

**Keep GET free of side effects, without exception.** Anything that changes state on a GET breaks caching, breaks retries and
surprises every client.

**Name action endpoints where the operation is an action.** A clearly named operation is better than a resource invented to
justify a method.

**State PATCH semantics explicitly.** Whether a missing field means "leave unchanged" or "set to null" is a decision, and
both readings are common.

**Return the resulting representation on writes.** It saves the caller a round trip and makes the resulting state — which Move
3 requires anyway — visible.

**Apply the disclosure policy from `Endpoints.md` uniformly.** Path-based resources make it easy to leak existence through
inconsistent status codes.

---

# Where It Misleads

**Convention is followed past the point of clarity.** Nested paths four levels deep, or an action modeled as a sub-resource
nobody would name, are conventions costing comprehension.

**Method semantics are assumed rather than implemented.** DELETE that errors on a second call is not idempotent, and every
retry-capable client will hit it.

**Endpoints mirror tables.** REST describes resources, and a resource is a concept in the domain — not necessarily a row.
`Endpoints.md` makes the same point: the interface serves capabilities.

**Status codes are used loosely.** A 200 containing an error body defeats every client library's error handling.
`Errors.md` covers the discipline.

**Over-fetching is accepted as the cost of the style.** It is often fine, and where it is not, that is the argument
`GraphQL.md` addresses — as a trade, not a default.

---

# Related

| | |
| --- | --- |
| `Endpoints.md` | Concrete specification and disclosure policy |
| `GraphQL.md` | The alternative, with its own costs |
| `Errors.md`, `Pagination.md` | Conventions that need deciding once |
| `Versioning.md` | Changing paths and payloads later |

---

> **Concept Note**
>
> REST's whole value is that a caller can guess correctly.
>
> When an operation is genuinely an action, name it — a resource
> invented to satisfy a method helps nobody.
