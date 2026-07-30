---
Title: Instrumentation
Module: 12-metrics
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Specify the events, resolve identity, and keep regulated data out of analytics.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 12-metrics/knowledge/Success-Metrics.md
Outputs:
  - instrumentation_plan
Related Modules:
  - 09-technology
  - 10-execution
Tags:
  - Metrics
  - Instrumentation
  - Method
---

# Instrumentation

---

# What It Is

The events themselves — the **only move in this module whose output becomes code**, and it is consumed directly by the `critical` build
handoff.

> An event not specified here will not be built. Instrumentation is not retrofitted — the feature ships, the events do not, and the
> product runs blind while someone schedules the work that was supposed to be free.

| Per event | |
| --- | --- |
| The precise trigger | When exactly it fires |
| Every property, with its type | What travels with it |
| The metric it feeds | The trace back to a definition |
| The milestone it ships in | Otherwise it ships in none |

**Coverage, both directions:**

| Direction | Failure | Consequence |
| --- | --- | --- |
| Metric → event | Uncomputable metric | It will be silently replaced with whatever is available |
| Event → metric | Orphan event | Noise, cost, and a privacy liability with no benefit |

**Identity resolution** — how a user is identified across sessions, across devices, and before signup. It is the most commonly omitted
part of an instrumentation plan, and without it every cohort and retention metric is uncomputable.

**Privacy exclusions**, and the framework is unusually direct here:

> Analytics on regulated data is a compliance exposure, not a data-quality question. A regulated column appearing as an event property
> means the regulated data is now in a third-party system with different retention, different access control and a different
> jurisdiction.

The check is mechanical: list the regulated columns from `09-technology` §3, then check them against every event property. **Any overlap
fails the gate.**

---

# When It Applies

In Move 6 (Instrument), last — instrumenting first produces events for the metrics that were easy to log.

---

# How to Apply It Here

**Write the events into the build handoff, per milestone.** `10-execution`'s cold-start test means the builder must see them without
opening another document.

**Run the regulated-column check as a list comparison.** Not a judgment. Module 09 classified every field; the overlap is arithmetic.

**Specify identity resolution explicitly**, including the pre-signup case if any metric depends on it.

**Delete orphan events.** Every property captured is cost, noise and a liability. `09-technology`'s data-minimization point applies to
analytics exactly as to storage.

**Say what is deliberately not instrumented.** An honest exclusion beats an implied claim of full coverage, the same way
`10-execution` treats untested areas.

---

# Where It Misleads

**Instrumentation is assumed to be trivial and gets deferred.** It is small work that never gets scheduled, and the product then runs
without any of the metrics this module defined.

**Regulated fields arrive as event properties for debugging convenience.** A note excerpt, a patient identifier, a diagnosis in a
property name. Each one moves regulated data into a third-party system nobody assessed.

**Identity is left to the analytics library's default.** Then cross-device users are counted twice, cohorts are wrong, and retention is
uncomputable — silently, with plausible-looking numbers.

**Events are named inconsistently.** Three names for one action makes every query a guess. A naming convention decided once costs
nothing.

**Everything is logged in case it is useful.** That is the orphan-event failure at scale: cost, noise, and a privacy surface with no
metric behind it.

---

# Related

| | |
| --- | --- |
| `Success-Metrics.md` | The definitions events must satisfy |
| `Cohorts.md` | What identity resolution makes possible |
| `09-technology` | The regulated columns, and the classification |
| `10-execution` | The build handoff these ship in |

---

> **Concept Note**
>
> An event not specified here will not be built, and the product will
> run blind.
>
> Then check every property against module 09's regulated columns — any
> overlap is a compliance exposure, not a data question.
