---
Title: Background Jobs
Module: 09-technology
Section: knowledge/scalability
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Treat scheduled work as the enforcement point for obligations, and make silent failure impossible.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/scalability/Queues.md
Outputs:
  - Scheduled work within scalability_plan
Related Modules:
  - 13-operations
Tags:
  - Technology
  - Scalability
  - Concept
---

# Background Jobs

---

# What It Is

Work that runs on a schedule rather than in response to a request — and in this framework it is where several **obligations** are
enforced.

| Job | What it enforces |
| --- | --- |
| **Retention** | Move 4's retention obligation — a column plus this job |
| **Erasure completion** | Where deletion cascades or backup reconciliation runs asynchronously |
| **Compliance evidence** | `13-operations` requires evidence produced on a cadence |
| Reporting and aggregation | Product features, and frequently the first bottleneck |
| Reconciliation with external systems | Detecting drift nobody would otherwise see |
| Cleanup of expired sessions, tokens, temporary files | Hygiene with a security dimension |

The distinction from `Queues.md`: a queued job is triggered by something; a scheduled job runs whether or not anyone is watching.
That difference is why **silent failure is the characteristic risk** here.

---

# When It Applies

In Move 5 (Choose) — `Backend.md` treats the job runner as part of the backend decision — and in Move 4 as the enforcement point
for scheduled obligations.

---

# How to Apply It Here

**Make every scheduled job report success, not only failure.** A job that stops running produces no error. Absence of a success
signal is the only detectable symptom, and `Monitoring.md` must alert on it.

**Make jobs idempotent and re-runnable.** A missed run should be recoverable by running it again, which requires the job to
tolerate having already partly completed.

**Name the owner and the runbook.** `13-operations`' rule applies: a failed retention job is a compliance failure, and it needs a
named person and steps.

**Bound the work per run.** A job processing everything since the last successful run will attempt a week's backlog after a week's
outage, and time out permanently. Batching with progress is the fix.

**Keep obligation jobs separate from feature jobs.** A retention job failing has legal consequences; a report failing does not. They
deserve different alerting and different severities.

---

# Where It Misleads

**Scheduled jobs are assumed to be running.** Nothing complains when a cron entry is lost in a migration, and the retention
obligation quietly stops being met — discovered, if ever, during an audit.

**They are treated as maintenance rather than as mechanisms.** Move 4 makes them enforcement points for legal obligations, which
puts them in the same category as an access-control check.

**Overlapping runs are not prevented.** A job taking longer than its interval starts again while running, and two concurrent
instances of a retention job can produce results nobody intended.

**Timezone and daylight-saving behavior is left implicit.** For anything tied to a business day this produces a missed or doubled
run twice a year.

**Long-running jobs are deployed without regard to release.** `09-technology/knowledge/Deployment.md` covers in-flight work: a
deploy mid-run can leave a job half-complete with no record of where it stopped.

---

# Related

| | |
| --- | --- |
| `Queues.md` | Triggered work, by contrast |
| `Monitoring.md` | Alerting on absence of success |
| `security/GDPR.md` | Retention and erasure as obligations |
| `13-operations` | Owners, runbooks and compliance cadence |

---

> **Concept Note**
>
> A scheduled job that stops running raises no error. Alert on the
> absence of success, not on failure.
>
> Retention and erasure live in these jobs — which makes them
> compliance mechanisms, not maintenance.
