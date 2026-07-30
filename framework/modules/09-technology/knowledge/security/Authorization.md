---
Title: Authorization
Module: 09-technology
Section: knowledge/security
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Locate the enforcement point, and answer the cross-tenant threat question against it.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/core/06-Framework.md
Outputs:
  - Authorization within security_model
Related Modules:
  - 02-market
  - 13-operations
Tags:
  - Technology
  - Security
  - Method
---

# Authorization

---

# What It Is

The design of who may touch what — and Move 4's requirement is that it be **located**, not merely described.

> Every obligation traces to a named mechanism at a named enforcement point.

For authorization that means one place through which every access passes, where the rule cannot be bypassed by a path
someone forgot. `api/Authorization.md` covers expressing it at the interface; this file is about where it lives and how it is
proven.

The proof is Move 4's threat question, and it is deliberately specific:

> **What would it take for one user of this product to see another user's data?** — answered against this design, with the
> test that verifies it.

A recital of generic vulnerability classes is not a threat model. That question, answered concretely, is.

---

# When It Applies

In Move 4 (Protect), and it constrains Move 5 — `Backend.md` treats a locatable enforcement point as a criterion for the
backend choice.

---

# How to Apply It Here

**Name the layer, and show that nothing bypasses it.** A query layer, a repository, a policy middleware. Then list the paths
that reach data: API, background jobs, exports, reports, search, admin tools. Each must pass through it.

**Express relational rules, not just roles.** Most real rules in professional software are relationships — "the clinician
treating this patient" — and a role-only model cannot represent them.

**Write the test that verifies the threat answer.** An automated test attempting cross-tenant access, run in the pipeline, is
what turns the answer into an ongoing guarantee rather than a claim made once.

**Include the non-API paths.** Background jobs, scheduled reports and admin screens are where authorization is most often
absent, because they were not thought of as callers.

**Design for least privilege in the operator's own access too.** Who at the operator can read customer data, under what
circumstances, with what audit entry. `database/Audit.md` records it and institutional buyers will ask.

---

# Where It Misleads

**Authorization is implemented per handler and described as a model.** Scattered checks fail on the path nobody reviewed, and
they fail silently — nothing errors when a check is simply absent.

**Roles are mistaken for a complete model.** They handle operation-level access and cannot express record-level rules, which
is where the serious vulnerabilities are.

**The threat model is written generically.** A list of vulnerability classes is not an answer about this design. The
cross-tenant question is answerable in a paragraph and worth more than the list.

**Admin access is treated as outside the model.** It is the most powerful access in the system and frequently the least
constrained and least audited.

**Multi-tenancy is assumed to be handled by a column.** A tenant identifier only works if every query includes it, which is
the located-enforcement requirement restated — and the one place it is easiest to omit is a report.

---

# Related

| | |
| --- | --- |
| `api/Authorization.md` | Expression at the interface |
| `Authentication.md` | Establishing identity first |
| `database/Audit.md` | Recording access, including refusals |
| `OWASP.md` | The class of failure this prevents |

---

> **Concept Note**
>
> Answer one question concretely: what would it take for one user to
> see another's data?
>
> Then write the test. An answer with no test is a claim that was true
> the day it was written.
