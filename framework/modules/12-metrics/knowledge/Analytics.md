---
Title: Analytics
Module: 12-metrics
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Choose where metrics are computed, weighing the compliance cost of a third-party system.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 12-metrics/knowledge/Instrumentation.md
Outputs:
  - Analytics approach within instrumentation_plan
Related Modules:
  - 02-market
  - 09-technology
Tags:
  - Metrics
  - Analytics
  - Concept
---

# Analytics

---

# What It Is

Where the events land and how the metrics get computed — a decision with a compliance dimension, not only a tooling one.

| Approach | Trade |
| --- | --- |
| **Query the product database directly** | No new store, no new jurisdiction, no third party. Limited to what the operational schema holds, and reporting queries compete with the product — `09-technology`'s likely first bottleneck |
| **A third-party analytics service** | Fast to adopt, good tooling. **A second store of user data**, with its own retention, access control and jurisdiction |
| A self-hosted analytics store | Full control, an operational component `13-operations` must run |
| A warehouse | Right once there is volume and several sources; premature before that |

For a small product with regulated data, the first row is frequently the correct answer and rarely the default choice. Most early
metrics — activation, frequency, cohorts — are computable from the operational data the product already holds lawfully.

---

# When It Applies

In Move 6 (Instrument), alongside the event specification. It is distinct from `04-problem/knowledge/validation/Analytics.md`, which uses
*existing* data to validate a problem.

---

# How to Apply It Here

**Check whether the operational database can answer the questions.** Activation, frequency and cohort retention usually can be computed
from records the product already stores.

**Treat a third-party service as a data processor.** `02-market` Frame 2 and `09-technology`'s obligations apply to it: residency,
retention, access, and an agreement in place. For health or financial data that assessment comes before adoption.

**Keep reporting queries off the operational path where they are heavy.** `09-technology/knowledge/scalability/Performance.md` names the
reporting query as the most common first bottleneck; a read replica is the usual response.

**Decide who can see the analytics.** It contains user behavior, and in professional contexts that is sensitive to the customer even
when it is not regulated.

**Keep the definitions in one place.** A metric computed one way in a dashboard and another way in a query is two metrics with one name —
which is what `Success-Metrics.md`'s five-part definition exists to prevent.

---

# Where It Misleads

**A third-party tool is added by default and never assessed.** It becomes a second store of user data in another jurisdiction, and the
assessment happens during a customer's security review instead.

**Dashboards are treated as the metric definition.** A tool's built-in "active users" is not the definition this module wrote, and it
will silently replace it — the exact substitution `Instrumentation.md` warns about.

**Everything is sent so that questions can be answered later.** That is the orphan-event failure with a compliance surface attached, and
data minimization applies to analytics.

**Reporting is run against production without a plan.** It is the classic cause of a slow product at the exact moment usage grows.

**Analytics is confused with system monitoring.** `09-technology/knowledge/scalability/Monitoring.md` asks whether the system is up;
this asks whether anyone is better off. A healthy system can disguise a failing product.

---

# Related

| | |
| --- | --- |
| `Instrumentation.md` | The events and the privacy check |
| `Cohorts.md` | What most early analysis actually needs |
| `09-technology` | Residency, obligations, and the reporting bottleneck |
| `04-problem` `validation/Analytics.md` | Using existing data to validate |

---

> **Concept Note**
>
> Most early metrics are computable from data you already hold
> lawfully.
>
> A third-party analytics service is a second copy of user behavior in
> someone else's jurisdiction — assess it before adopting it, not during
> a security review.
