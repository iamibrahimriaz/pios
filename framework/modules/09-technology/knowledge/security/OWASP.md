---
Title: OWASP
Module: 09-technology
Section: knowledge/security
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Use a vulnerability catalog as a coverage check, not as a threat model.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/security/Authorization.md
Outputs:
  - Coverage check within security_model
Related Modules:
  - 14-ai-systems
Tags:
  - Technology
  - Security
  - Concept
---

# OWASP

---

# What It Is

A published catalog of common web application vulnerability classes, maintained by the Open Web Application Security Project.

Its role here is a **coverage sweep**, and the framework is explicit about the distinction:

> A recital of generic vulnerability classes is not a threat model.

The threat model is Move 4's specific question — what would it take for one user of this product to see another user's data,
answered against this design. The catalog is the checklist run afterward to find what the specific analysis missed.

| Class | Where this framework already addresses it |
| --- | --- |
| Broken access control | `Authorization.md` — the located enforcement point |
| Cryptographic failures | `Encryption.md`, `Secrets.md` |
| Injection | `api/Filtering.md` — enumerated parameters over expression languages |
| Insecure design | Move 4 itself, run in order |
| Security misconfiguration | `09-technology` `Hosting.md`, `Deployment.md` |
| Vulnerable components | `CI-CD.md`'s dependency scanning |
| Identification and authentication failures | `Authentication.md`, including recovery |
| Logging and monitoring failures | `database/Audit.md`, `scalability/Monitoring.md` |

Broken access control sits at the top of the list in practice, which is why it gets a located enforcement point rather than a
checklist entry.

---

# When It Applies

At the end of Move 4, as the sweep after the specific threat analysis.

---

# How to Apply It Here

**Run the specific question first.** The cross-tenant threat answer is worth more than the entire catalog, because it is about
this design.

**Use the catalog to find omissions, then discard it.** Each class either maps to a mechanism already designed or reveals a gap.
Recording the mapping is useful; reproducing the list is not.

**Treat dependency vulnerabilities as continuous.** A one-time check is a snapshot; `CI-CD.md`'s scanning is the mechanism.

**Extend the sweep for AI features.** Prompt injection, training-data exposure and output-handling failures are not in the
classic web catalog. `14-ai-systems` covers them, and they are real for any product passing user content to a model.

**Keep the output as mechanisms, not as reassurance.** A completed checklist with no named mechanisms is the same failure Move 4
prohibits — a claim rather than a control.

---

# Where It Misleads

**A completed checklist is presented as a threat model.** It has no severity, no specificity and no relation to this product's
actual data flows. `02-market`'s objection to SWOT applies: a format that weights everything equally will be filled as if
everything mattered equally.

**Generic classes obscure the one that matters.** For professional multi-tenant software, broken access control is the
overwhelming risk, and it is one line in a list of ten.

**Categories are mapped to intentions.** "We validate input" is not a mechanism at an enforcement point.

**AI-specific risks are omitted because they are not in the list.** Any product sending user text to a model has an injection
surface the web catalog does not describe.

**The sweep is run once, at design time.** Dependencies change weekly, and that is what makes scanning a schedule rather than a
review item.

---

# Related

| | |
| --- | --- |
| `Authorization.md` | The specific threat question |
| `Secrets.md`, `Encryption.md` | Cryptographic mechanisms |
| `09-technology` `CI-CD.md` | Continuous dependency checking |
| `14-ai-systems` | Model-specific failure modes |

---

> **Concept Note**
>
> Answer the specific question first, then run the catalog to find what
> you missed.
>
> A completed checklist with no mechanisms behind it is a claim — and
> Move 4 does not accept claims.
