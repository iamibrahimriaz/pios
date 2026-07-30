---
Title: Errors
Module: 09-technology
Section: knowledge/api
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Turn every specified edge case into a failure response a client can act on.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/api/Endpoints.md
Outputs:
  - Failure responses within api_contract
Related Modules:
  - 08-product
  - 13-operations
Tags:
  - Technology
  - API
  - Method
---

# Errors

---

# What It Is

The failure half of the contract — and the framework's rule is that it is **not new work**:

> Module 08 specified five categories per requirement. Each maps to a status and an error code here. An edge case with no
> corresponding failure response was specified and then dropped, which is worse than never having specified it.

| `08-product` category | Typical response |
| --- | --- |
| Empty | Not an error — an empty result with a defined shape |
| Invalid | 400 or 422, with the field and the reason, and the input preserved |
| Failure | 500 or 503, with whether retrying is safe |
| Permission | 403 or 404, per the disclosure policy |
| Limit or conflict | 409 for conflict, 429 for rate, 413 for size |

A response body needs three things the client can use: a **stable machine-readable code**, the **field** where relevant, and
whether the operation is **safe to retry**.

---

# When It Applies

In Move 3 (Expose), worked from `08-product`'s edge cases rather than invented.

---

# How to Apply It Here

**Give every error a stable code.** Clients branch on codes, not on messages. A message is for humans and may be reworded; a
code is part of the contract.

**Say whether a retry is safe.** Combined with the idempotency decision from `Endpoints.md`, this is what lets a client recover
without creating duplicates.

**Name the field on validation errors.** A 400 that does not say which field failed forces the user to guess, and
`08-product`'s invalid-input category required the input to be preserved.

**Keep internal detail out of the response and in the log.** Stack traces and query text in an error body are an information
leak; `13-operations` needs them, the caller does not.

**Distinguish client faults from server faults honestly.** Returning 400 for a server problem hides real failures from
monitoring, and `scalability/Monitoring.md` will not see them.

---

# Where It Misleads

**Errors are treated as the part to fill in later.** They are most of the interface's surface and all of its behavior under
stress. Deferring them means the edge cases module 08 worked are silently lost.

**A 200 carries an error in the body.** Every client library treats 200 as success, so the failure goes unhandled and
unmonitored.

**Messages are used as the contract.** Rewording a message then breaks clients, which is the worst possible coupling: a
cosmetic change with functional consequences.

**Errors reveal what authorization concealed.** "User 4821 not permitted" confirms user 4821 exists. The disclosure policy
applies to error content too.

**Retry guidance is omitted.** Without it, clients either never retry — losing recoverable operations — or always retry,
producing duplicates on non-idempotent writes.

---

# Related

| | |
| --- | --- |
| `Endpoints.md` | Idempotency and disclosure |
| `Authorization.md` | What a refusal may reveal |
| `08-product` | The five edge categories |
| `13-operations` | Where internal detail belongs |

---

> **Concept Note**
>
> Stable code, the field, and whether retrying is safe.
>
> An edge case specified in module 08 with no failure response here was
> not deferred — it was dropped.
