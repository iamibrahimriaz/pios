---
Title: API Authorization
Module: 09-technology
Section: knowledge/api
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Express permission at the interface, including what a refusal reveals.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/api/Authentication.md
Outputs:
  - Authorization at the interface within api_contract
Related Modules:
  - 08-product
Tags:
  - Technology
  - API
  - Concept
---

# API Authorization

---

# What It Is

What an authenticated caller is permitted to do — expressed at the interface, and enforced at the point
`security/Authorization.md` locates.

Three levels, and the third is where products fail:

| Level | Question |
| --- | --- |
| **Operation** | May this caller invoke this endpoint at all? |
| **Record** | May they act on *this particular* record? |
| **Field** | May they see or change *this particular field* on it? |

Operation-level checks are easy and nearly always present. Record-level checks are the ones that get missed, and their
absence is the single most common serious vulnerability in professional software: a caller changing an identifier in a
path and receiving someone else's data.

And the disclosure decision from `Endpoints.md`:

> Returning 403 for a record the caller may not see confirms it exists.

---

# When It Applies

In Move 3 (Expose) per operation, tied to the enforcement point designed in Move 4.

---

# How to Apply It Here

**State the record-level rule for every operation that takes an identifier.** "The caller must be the treating clinician for
this patient" is a rule. "Authenticated users may read notes" is not, and it is how the vulnerability above ships.

**Apply the disclosure policy consistently.** Choose 404-for-unauthorized as the default where existence itself is sensitive,
and record the choice. Inconsistency between endpoints leaks by comparison.

**Enforce in the query, not after retrieval.** Filtering fetched rows works until one path forgets. Pushing the rule into the
query layer is what makes it structural — and it is what `database/Search.md` requires for search results too.

**Specify field-level rules where they exist.** A record one role may read fully and another partially is a real requirement
in clinical and HR contexts, and it needs stating per field.

**List operations need the same rule as fetch operations.** A collection endpoint returning everything is the record-level
failure applied a thousand times at once.

---

# Where It Misleads

**Authentication is mistaken for authorization.** Knowing who someone is says nothing about what they may touch. A product
with solid sign-in and no record-level checks is wide open to its own users.

**Client-side hiding is treated as enforcement.** The interface is the boundary; anything the client conceals is still
reachable by anyone sending the request directly.

**Roles are used where the rule is relational.** "Clinician" is a role; "the clinician treating this patient" is a
relationship, and most real rules in professional software are relational.

**Refusals leak through timing and status codes.** A fast 403 and a slow 404 distinguish themselves. Where existence is
sensitive, the responses should be indistinguishable.

**The rule is documented per endpoint and implemented per handler.** That is the scattered enforcement Move 4 forbids, and it
fails silently on the path nobody reviewed.

---

# Related

| | |
| --- | --- |
| `Authentication.md` | Establishing identity first |
| `security/Authorization.md` | Locating the enforcement point |
| `Endpoints.md` | The disclosure decision |
| `database/Search.md` | Where results must respect the same rule |

---

> **Concept Note**
>
> Record-level authorization is the check that gets missed, and
> changing an identifier in a path is how it gets found.
>
> Enforce it in the query. Anything checked after retrieval is checked
> optionally.
