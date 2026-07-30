---
Title: Search
Module: 09-technology
Section: knowledge/database
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Establish what the user is actually searching for before adding a search system.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/database/Indexes.md
Outputs:
  - Search design within data_model
Related Modules:
  - 08-product
  - 14-ai-systems
Tags:
  - Technology
  - Search
  - Concept
---

# Search

---

# What It Is

Finding records — where the design depends entirely on what "finding" means in the requirement.

| What the user is doing | What it needs |
| --- | --- |
| Going to a record they know exists | A lookup by identifier or name — an index, nothing more |
| Filtering a list by known attributes | Query parameters and indexes — `api/Filtering.md` |
| Looking for a word inside text | Full-text search in the primary store, usually sufficient |
| Finding records that are *about* something | Semantic search — and that is a `14-ai-systems` decision |
| Exploring a large corpus | A dedicated search system, with its own sync and consistency problems |

Most search requirements are the first two rows and get built as the last one. Each row down that table adds
infrastructure, cost, an erasure surface and a consistency problem.

---

# When It Applies

In Move 2 (Model) once the requirement is understood, and in Move 5 (Choose) if a separate system is genuinely needed.

---

# How to Apply It Here

**Read the requirement before choosing the mechanism.** `08-product`'s behavior says what the user types and what they
expect back. Frequently it is a name they already know.

**Try the primary store's full-text capability first.** For a professional tool with thousands of records rather than
millions, it is usually adequate — and it has no sync, no second copy and no separate erasure path.

**Count the erasure consequence of a second index.** A search index holding regulated text is another store Move 4's
deletion obligation must reach, and `Soft-Delete.md`'s consistency requirement applies to it too.

**Enforce authorization in search results.** This is the classic leak: a search that returns titles the user is not
permitted to open. The enforcement point from `security/Authorization.md` must apply to the search path.

**Hand semantic search to module 14.** If the requirement is genuinely about meaning rather than words, it is an AI
capability with an accuracy question, a cost per query and an acceptance criterion.

---

# Where It Misleads

**A search system is adopted for a lookup requirement.** It brings an index to keep in sync, a cost floor, a failure mode and
a second place regulated data lives — to solve something an index would have solved.

**Search results bypass permission checks.** Filtering after retrieval leaks existence; filtering before retrieval requires
the authorization rule to be expressible in the search query. Which one applies is a design decision, not an implementation
detail.

**Relevance is treated as a solved property.** What "best match" means is a product decision. Unspecified, it becomes
whatever the default scoring does, and users will find it wrong in ways nobody predicted.

**Index freshness is assumed to be immediate.** A separate system is eventually consistent, and a user searching for the
record they just created and not finding it is a bug report.

**Semantic search is added because it is available.** `14-ai-systems`' method applies: compare it against the non-AI
alternative, and dropping it is a valid outcome.

---

# Related

| | |
| --- | --- |
| `Indexes.md` | The access paths most search requirements need |
| `api/Filtering.md` | Structured filtering at the interface |
| `security/Authorization.md` | The check search results must respect |
| `14-ai-systems` | Where semantic search is justified or dropped |

---

> **Concept Note**
>
> Most search requirements are a lookup for a record the user already
> knows about.
>
> The one that leaks is the search that returns titles the user is not
> allowed to open.
