---
Title: GraphQL
Module: 09-technology
Section: knowledge/api
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Weigh flexible querying against the authorization and cost problems it introduces.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/api/REST.md
Outputs:
  - Contract style within api_contract
Related Modules:
  - 08-product
Tags:
  - Technology
  - API
  - Concept
---

# GraphQL

---

# What It Is

A contract where the caller specifies which fields it wants, against a typed schema.

The trade is genuine in both directions:

| Gains | Costs |
| --- | --- |
| The client fetches exactly what it needs | Authorization must be enforced **per field**, not per endpoint |
| One request instead of several | Query cost is caller-controlled — an expensive query is a client's choice |
| The schema is introspectable and self-documenting | Caching is harder; the HTTP layer no longer helps |
| Adding fields rarely breaks clients | Every resolver is a potential N+1 query |

The decisive question for this framework is the first cost. Move 4 requires authorization at a **named enforcement point**.
With per-field resolution, that point must cover every field on every path, which is a harder guarantee than one check per
endpoint.

---

# When It Applies

In Move 3 (Expose), where the requirements show genuinely varied client needs. Otherwise `REST.md`'s predictability is worth
more.

---

# How to Apply It Here

**Justify it from the requirements.** Several clients with materially different data needs is a reason. One web client is
not, and the cost of the flexibility is paid regardless.

**Locate authorization at the resolver layer and prove the coverage.** Move 4's threat question applies directly: what would
it take for one user to see another's data? With per-field access, the answer must be checked field by field.

**Bound query cost.** Depth limits, complexity limits, and a documented maximum. Without them, cost per request is set by
whoever is calling.

**Design against N+1 explicitly.** Batching is not automatic. A nested query that looks trivial can produce hundreds of
round trips, and Move 6's bottleneck analysis should say so.

**Say what happens on partial failure.** Returning data and errors together is a shape clients must handle deliberately, and
it is the most misunderstood property of the style.

---

# Where It Misleads

**It is chosen for elegance and pays for it in authorization complexity.** This is the specific risk in a regulated product:
a field-level access rule missed on one path is a data leak with no obvious symptom.

**Query cost is assumed to be the server's problem to optimize.** It is the caller's to *set*. Without limits, a legitimate
client can produce an accidental denial of service.

**Caching benefits are assumed to transfer.** HTTP caching largely does not apply, so caching becomes an application concern
— which `architecture/Caching.md` treats as a design decision with staleness consequences.

**The schema becomes the data model exposed.** Move 3 exposes capabilities. A schema mirroring the entities gives callers
access shaped by storage rather than by requirements.

**Versioning is assumed to be unnecessary.** Additive change is easier; removing or retyping a field still breaks clients, and
`Versioning.md` still applies.

---

# Related

| | |
| --- | --- |
| `REST.md` | The predictable default |
| `Authorization.md` | Per-field enforcement |
| `architecture/Caching.md` | What the HTTP layer no longer does |
| `scalability/Performance.md` | Where N+1 surfaces |

---

> **Concept Note**
>
> The flexibility is real and so is the bill: authorization moves from
> one check per endpoint to one per field.
>
> In a regulated product, that is the whole decision.
