---
Title: Deployment
Module: 09-technology
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Make releasing and reverting routine, including the schema changes that cannot be reverted.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/Hosting.md
Outputs:
  - Deployment approach within architecture
Related Modules:
  - 10-execution
  - 13-operations
Tags:
  - Technology
  - Deployment
  - Concept
---

# Deployment

---

# What It Is

How a change reaches users, and how it is taken back.

The second half is the part that gets designed last and needed first:

| | Question |
| --- | --- |
| **Release** | What happens, in what order, and who can trigger it |
| **Revert** | How the previous version is restored, and how long that takes |
| **Schema changes** | Which migrations are reversible — most are not |
| **Environments** | What exists between a developer's machine and production |
| **Data in non-production** | Whether regulated data is ever copied there — usually it must not be |

**Reverting code is easy; reverting a migration is often impossible.** A release containing a destructive schema change
has no rollback, and that fact should be known before the release rather than during the incident.

---

# When It Applies

In Move 5 (Choose), and consumed by `13-operations`, whose runbooks assume a revert path exists.

---

# How to Apply It Here

**Write the revert procedure as steps.** `13-operations`' 3am test applies: do this, expect this, if different. A revert
nobody has performed is a hypothesis.

**Separate schema changes from code changes.** Deploy the additive migration, then the code, then the destructive change
later — if at all. That sequencing is what keeps a revert possible.

**State whether production data is ever copied into other environments.** For regulated data the answer is almost always
no, which means realistic test data is a task rather than an assumption.

**Decide who may deploy, and how they are authenticated.** Deployment credentials are among the most sensitive secrets in
the system, and `security/Secrets.md` covers where they live.

**Keep it simple enough to be used.** A deployment process too elaborate for a small team gets bypassed under pressure,
which is precisely when it matters.

---

# Where It Misleads

**Revert is assumed to be automatic.** It is not, once the database has changed. The honest position is stated per
release: revertible, or forward-fix only.

**Zero-downtime deployment is designed for before it is needed.** For a professional tool with a known working day, a short
maintenance window may be entirely acceptable — and it removes a large amount of complexity.

**Environments multiply without purpose.** Each one costs money, drifts from production, and needs data. Two well-maintained
environments beat four neglected ones.

**Production data leaks into staging for convenience.** It is a breach with extra steps, and it is the most common way
regulated data ends up somewhere Move 4 never accounted for.

**Deployment is treated as `10-execution`'s concern.** Module 10 sequences the work; the mechanism and its revert path are
a design decision, and `13-operations` inherits them.

---

# Related

| | |
| --- | --- |
| `CI-CD.md` | The automation around it |
| `database/Migration.md` | Which schema changes can be reversed |
| `security/Secrets.md` | Deployment credentials |
| `13-operations` | Runbooks that assume a revert path |

---

> **Concept Note**
>
> Reverting code is easy. Reverting a migration usually is not.
>
> Know which of the two a release contains before you ship it, not
> during the incident.
