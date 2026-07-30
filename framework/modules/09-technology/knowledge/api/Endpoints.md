---
Title: Endpoints
Module: 09-technology
Section: knowledge/api
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Give every capability a concrete operation, checked in both directions.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/core/06-Framework.md
Outputs:
  - api_contract
Related Modules:
  - 08-product
Tags:
  - Technology
  - API
  - Method
---

# Endpoints

---

# What It Is

The operations through which each capability is reached — specified concretely.

> A description of an endpoint is not an endpoint.

Concrete means actual request and response bodies, actual field names, actual validation rules. And the coverage check runs
both ways:

| Direction | Failure |
| --- | --- |
| Requirement → operation | A MUST requirement is unreachable. It will surface mid-build |
| Operation → requirement | Speculative surface area. Every endpoint is code, tests, docs **and attack surface** |

Two decisions that are easy to leave implicit and expensive to leave implicit:

| Decision | Why |
| --- | --- |
| **Idempotency, per write operation** | Retry is universal. Non-idempotent writes plus retries produce duplicates |
| **Existence disclosure — 404 or 403** | Returning 403 for a record the caller may not see confirms it exists |

---

# When It Applies

In Move 3 (Expose), after the data model exists and before technology is chosen.

---

# How to Apply It Here

**Write real payloads.** Field names, types, which fields are optional, what validation rejects. That is what makes the
contract implementable without follow-up questions.

**Map `08-product`'s five edge categories to failure responses.** Each becomes a status and an error code. An edge case with
no corresponding failure response was specified and then dropped — worse than never specifying it.

**State idempotency per write.** Which operations are safe to repeat, and how the client signals a retry. This is the
decision that prevents duplicate records in every real network.

**Choose the disclosure policy deliberately and apply it consistently.** Whether an unauthorized caller sees 404 or 403 is a
security decision, and inconsistency between endpoints is itself an information leak.

**Delete endpoints with no requirement.** Speculative surface is not free: it is code, tests, documentation and a way in.

---

# Where It Misleads

**Endpoints are described rather than specified.** "An endpoint to create a note" leaves every field, every validation rule
and every error to whoever builds it — which is the schema test failing at the interface layer.

**Coverage is checked one way.** Missing operations surface during the build; speculative ones never surface at all, and they
accumulate permanently.

**Error responses are added later.** They are most of the interface. `Errors.md` covers the form; the point here is that the
edge cases already specified them and they must not be lost in translation.

**Idempotency is assumed from the method.** The convention helps and does not decide it. A create operation retried after a
timeout needs an explicit answer.

**The interface mirrors the database.** Endpoints serve capabilities, not tables. A one-to-one mapping from entities to
endpoints usually means the requirements were skipped.

---

# Related

| | |
| --- | --- |
| `REST.md`, `GraphQL.md` | The shape the contract takes |
| `Errors.md` | Failure responses from edge cases |
| `Versioning.md` | Changing a contract once it is used |
| `08-product` | Requirements and edge categories |

---

> **Concept Note**
>
> Real fields, real validation, real error codes — or it is a
> description, not a contract.
>
> Every endpoint with no requirement behind it is permanent attack
> surface nobody asked for.
