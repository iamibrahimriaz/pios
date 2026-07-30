---
Title: Recovery
Module: 09-technology
Section: knowledge/security
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Verify that restoration works, because an unverified backup is not a capability.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/security/Backups.md
Outputs:
  - Recovery verification within security_model
Related Modules:
  - 13-operations
Tags:
  - Technology
  - Security
  - Method
---

# Recovery

---

# What It Is

The demonstrated ability to bring the system back — and the framework's position is unambiguous:

> An unverified backup is not a recovery capability. `13-operations` records `restore_tested: yes | no | never`, and **never**
> is a finding.

What a verification actually establishes:

| Verified | What it proves |
| --- | --- |
| A restore completes | The backup is readable and the procedure exists |
| The restored system starts | Configuration and secrets are also recoverable |
| The data is complete | Every store was covered, not only the database |
| It took *n* hours | Whether the recovery time objective is real |
| Outstanding erasures were re-applied | The `Backups.md` reconciliation works in practice |

The fourth row is the one that changes plans. Recovery time is nearly always longer than assumed, and the gap between the
assumed and the measured figure is what a rehearsal buys.

---

# When It Applies

In Move 4 (Protect) as a designed procedure, and in `13-operations` as a scheduled rehearsal with an owner.

---

# How to Apply It Here

**Write the procedure as steps, in three columns.** Do this, expect this, if different. That is `13-operations`' 3am test, and a
recovery runbook is the clearest case for it — it will be read by someone under pressure.

**Include the access needed at the top.** Which credentials, which accounts, which approvals. A recovery blocked on access
nobody has is the most avoidable failure in this file.

**Rehearse to a real environment and record the time.** The measured duration replaces the assumed recovery time objective, and
if it exceeds it, that is a design finding.

**Verify data completeness, not just process completion.** A restore that starts cleanly and is missing the file store has
recovered a broken product.

**Re-apply outstanding erasures as part of the procedure.** Otherwise a restore silently reverses a legal obligation, which is
the worst kind of quiet failure.

---

# Where It Misleads

**Backup existence is reported as recovery readiness.** They are different claims, and only one of them has ever been tested in
most products.

**Recovery time is estimated and never measured.** Estimates are optimistic by a wide margin, and the estimate is what the
customer commitment was based on.

**Configuration and secrets are forgotten.** Data restores and the system still will not start, because the credentials to
external services live somewhere the backup did not reach.

**Partial recovery is not planned for.** Restoring one customer's records, or one table, is a much more common need than a full
restore — and it is a different procedure.

**Rehearsal is treated as optional because nothing has failed.** `13-operations` schedules it precisely because the absence of
an incident is not evidence of capability.

---

# Related

| | |
| --- | --- |
| `Backups.md` | The copies being restored |
| `Secrets.md` | What a restore also needs |
| `09-technology` `Deployment.md` | Environments and revert paths |
| `13-operations` | The rehearsal cadence, and `restore_tested` |

---

> **Concept Note**
>
> Restore it, time it, check the data, re-apply the erasures.
>
> Until that has happened, you have backups — which is a different
> thing from being able to recover.
