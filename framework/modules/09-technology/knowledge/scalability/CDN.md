---
Title: CDN
Module: 09-technology
Section: knowledge/scalability
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Serve static assets from the edge, and keep regulated content off it.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/scalability/Caching.md
Outputs:
  - Asset delivery within scalability_plan
Related Modules:
  - 02-market
Tags:
  - Technology
  - Scalability
  - Concept
---

# CDN

---

# What It Is

A content delivery network — copies of content served from locations near the requester.

What it is genuinely good for, and where it stops:

| Suited to | Not suited to |
| --- | --- |
| Application assets — scripts, styles, fonts, images | Anything permission-dependent |
| Public documents and marketing content | Regulated records |
| Large downloads, where egress cost matters | Frequently changing data |
| Absorbing traffic spikes on static content | Reducing database load — that is `Caching.md` |

The constraint that matters most in this framework: **a CDN is a distributed cache in locations you do not control.** For
regulated data that collides directly with Move 4's residency and erasure obligations, and with `02-market` Frame 2's
jurisdiction.

---

# When It Applies

In Move 5 (Choose) for asset delivery. For most professional tools it is a modest optimization rather than a scaling necessity.

---

# How to Apply It Here

**Use it for assets, and say so explicitly.** Scripts, styles and images are the whole legitimate scope for most products, and it
is a real improvement to load time.

**Keep signed, permission-dependent content off the shared cache.** If a file must be authorized per request, it is served by the
application or by a signed short-lived URL — not cached publicly.

**Check residency before enabling edge distribution of anything sensitive.** Copies in arbitrary regions is exactly what a
residency obligation prohibits.

**Version asset filenames rather than relying on invalidation.** A content hash in the name makes stale assets impossible, which is
the one caching problem with a clean solution.

**Note the egress saving where files are large.** For a document-heavy product this can be a real line in
`09-technology/knowledge/Infrastructure.md`'s cost table.

---

# Where It Misleads

**A CDN is expected to solve application slowness.** It serves static content. If the slow part is a query, nothing at the edge
helps — `Performance.md` locates the actual bottleneck.

**Regulated files are placed behind it for convenience.** Now copies exist in unknown regions with their own retention, and both
residency and erasure obligations are breached.

**Cache headers are left at defaults.** An overly long cache on a changing asset serves stale code; an overly short one removes the
benefit. Both are decisions.

**Private content is cached because the URL looked unguessable.** Obscurity is not authorization, and a shared cache may serve it to
anyone with the URL.

**It is adopted as standard practice for an internal tool.** A product used by two hundred people in one country gains very little
and adds a component to configure, pay for and reason about.

---

# Related

| | |
| --- | --- |
| `Caching.md` | Caching that relieves the database |
| `architecture/Caching.md` | Keys, and authorization leakage |
| `security/Encryption.md` | Protecting content in transit and at rest |
| `02-market` | Jurisdiction and residency |

---

> **Concept Note**
>
> Assets at the edge, regulated records nowhere near it.
>
> A CDN is a cache in places you do not control — which is the whole
> benefit, and the whole problem.
