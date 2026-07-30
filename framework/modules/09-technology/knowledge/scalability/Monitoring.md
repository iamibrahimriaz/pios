---
Title: Monitoring
Module: 09-technology
Section: knowledge/scalability
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Instrument the system so a named bottleneck and a silent failure both become visible.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/scalability/Performance.md
Outputs:
  - Monitoring within scalability_plan
Related Modules:
  - 12-metrics
  - 13-operations
Tags:
  - Technology
  - Monitoring
  - Method
---

# Monitoring

---

# What It Is

System observation — distinct from `12-metrics`, which measures whether the **product** is working. This measures whether the
**system** is.

| | System monitoring | Product metrics |
| --- | --- | --- |
| Question | Is it up, fast and keeping up? | Is anyone better off? |
| Owner | This module, run by `13-operations` | `12-metrics` |
| Audience | Whoever is on call | The operator |

What must be observed, derived from what this module designed:

| Signal | Because |
| --- | --- |
| Error rate, by endpoint | The first indication of a failing release |
| Latency percentiles | `Performance.md` — averages hide the worst experience |
| The named first bottleneck from Move 6 | It is the thing expected to break |
| Queue depth and oldest item age | `Queues.md` — a backlog looks healthy |
| **Scheduled job success** | `Background-Jobs.md` — absence of success is the only symptom |
| Inference cost and volume | `14-ai-systems`' per-user cost, observed rather than projected |
| Provider quota consumption | A ceiling reached without warning otherwise |

---

# When It Applies

In Move 6 (Size), alongside the bottleneck analysis. `13-operations` owns the response.

---

# How to Apply It Here

**Instrument the bottleneck you named.** Move 6 requires it identified with a figure. Monitoring it is what makes the prediction
checkable and the response timely.

**Alert on absence, not only on errors.** A job that stopped, a queue no longer draining, a metric that went quiet. These are the
failures nothing reports.

**Set thresholds someone will act on.** `13-operations`' rule about differentiated severity applies: an alert nobody responds to
trains everyone to ignore alerts.

**Keep sensitive data out of logs and traces.** Move 2's classification applies to observability data, and error trackers are a
frequent unplanned location for regulated content.

**Include cost as a monitored signal.** For AI features, cost per user is a business constraint from `06-business`, and it is the
one that moves with usage rather than with a deployment.

---

# Where It Misleads

**Dashboards are built and alerts are not.** A dashboard requires someone to look; an alert finds someone. Only the second works at
3am, which is the case `13-operations` designs for.

**Averages are monitored.** They conceal the users having the worst experience, and those are the users who leave.
`Performance.md` requires percentiles.

**Silent failures are not covered.** Error-rate monitoring catches things that break loudly. Scheduled jobs and event consumers fail
quietly, and they need absence-based alerting.

**Everything is alerted at the same severity.** The register becomes noise, and the real incident arrives among fifty warnings.

**System monitoring is presented as product measurement.** Uptime and latency say nothing about whether the problem is being solved.
`12-metrics` answers that, and conflating them lets a healthy system disguise a failing product.

---

# Related

| | |
| --- | --- |
| `Performance.md` | Percentiles and the bottleneck |
| `Queues.md`, `Background-Jobs.md` | The silent failure cases |
| `12-metrics` | Product measurement, by contrast |
| `13-operations` | Severity, response and the rota |

---

> **Concept Note**
>
> Alert on the absence of things, not only on errors.
>
> A dashboard needs someone to look at it. An alert goes and finds
> them — and at 3am only one of those works.
