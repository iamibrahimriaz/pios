---
Title: Monitoring
Module: 13-operations
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Give every alert a threshold, a named person and a runbook — or delete it.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 13-operations/knowledge/Runbooks.md
Outputs:
  - Alert hygiene within compliance_operations
Related Modules:
  - 09-technology
  - 12-metrics
Tags:
  - Operations
  - Monitoring
  - Concept
---

# Monitoring

---

# What It Is

Alerting as an operational discipline — where `09-technology/knowledge/scalability/Monitoring.md` decided **what to observe**, this decides
**what wakes someone up.**

> Every alert needs a threshold, a named person, and a runbook. An alert missing any of the three is worse than no alert.

| Missing | Consequence |
| --- | --- |
| Threshold | It fires on noise, or never |
| Named person | Everyone assumes someone else is looking |
| Runbook | The person woken does not know what to do |

And the rule that keeps the set usable:

> **A tolerated alert teaches the team to tolerate all of them.**
>
> An alert nobody acts on is **deleted**, not ignored.

Plus the honest counterpart: name what is deliberately **not** alerted on, usually because there is no action to take.

---

# When It Applies

In Move 5 (Comply), alongside the compliance schedule — alert hygiene is part of running the system rather than designing it.

---

# How to Apply It Here

**Write the three attributes per alert as a table.** Threshold, person, runbook. A row with a blank is a row to fix or remove.

**Alert on absence as well as on failure.** `09-technology/knowledge/scalability/Background-Jobs.md` covers it: a scheduled job that stops
running raises no error, and the retention obligation quietly stops being met.

**Keep alerts and dashboards distinct.** A dashboard requires someone to look. An alert finds them. At 3am only the second works.

**Delete the alerts that have fired without action.** This is a maintenance task with a cadence, and the alternative is a set everyone has
learned to dismiss.

**Distinguish system alerts from product metrics.** `12-metrics` measures whether anyone is better off; this measures whether the system is
up. A healthy system can disguise a failing product, and conflating the two hides it.

---

# Where It Misleads

**Alert coverage is treated as a virtue.** Volume degrades response. A small set that always means something beats a large set that
sometimes does.

**Thresholds are set at the point of technical interest rather than user impact.** `SLAs.md`'s grading rule applies: the question is what
the user cannot do.

**Alerts are configured and never reviewed.** Systems change, and a threshold appropriate at launch fires constantly at ten times the
volume — which is exactly when attention matters most.

**The person is a rota that does not exist.** `SLAs.md`'s rota question applies: an alert routed to on-call, where on-call is one person
who is asleep, is a delayed alert.

**Cost is not monitored.** For AI features it moves with usage rather than with deployments, and `09-technology` requires it observed
rather than projected.

---

# Related

| | |
| --- | --- |
| `Runbooks.md` | What every alert must point to |
| `SLAs.md` | Severity, and who is woken |
| `09-technology` `scalability/Monitoring.md` | What to observe |
| `12-metrics` | Product measurement, by contrast |

---

> **Concept Note**
>
> Threshold, person, runbook — or delete it.
>
> One tolerated alert teaches everyone to tolerate all of them, and then
> the real one arrives among fifty warnings.
