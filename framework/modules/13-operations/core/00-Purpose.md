---
Title: Purpose
Module: 13-operations
Section: core
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define why the Operations module exists and what it establishes for the rest of the run.
Audience:
  - AI Agents
  - Operators
  - Founders
Prerequisites:
  - core/00-Purpose.md
  - 10-execution gate passed
Outputs:
  - Shared understanding of what this module establishes
Related Modules:
  - 14-ai-systems
Tags:
  - Operations
  - Purpose
  - Foundation
---

# Purpose

---

# Overview

Every module before this one described a product that has not launched. This one describes the
day after.

Who answers when a user is stuck. What happens when something breaks at three in the morning.
Which obligations recur, who owns each, and what evidence they produce. And what keeping the whole
thing alive actually costs — including the two lines every earlier cost model omitted.

> Most blueprints stop at launch. That is why so many products become unmaintainable in month
> three.

---

# Purpose Statement

> Make the product runnable by a real person with limited time — and say plainly
> what that costs and where its limits are.

---

# Why This Module Exists

Three failures dominate operations planning.

**The runbook that requires its author.** Steps that say "investigate the issue" or "check the
logs". Perfectly clear to the person who wrote them and useless to anyone else, which is precisely
who will be reading at 3am.

**Compliance as a state rather than a schedule.** A mechanism exists — a log is written, a
retention column is present — and nobody reviews it, tests it, or produces evidence that it works.
It satisfies an auditor for exactly as long as nobody looks.

**The coverage table nobody can staff.** Four-hour response targets, weekend coverage, an on-call
rota of one person who also builds the product. It holds for a month.

The module's structure — the 3am test, obligations with owners and evidence artifacts, and an
explicit rota question — exists to make each of these visible before launch rather than during an
incident.

---

# The Judgment This Module Makes

| Output | What it commits |
| --- | --- |
| `support_model` | Who answers users, how fast, and about what |
| `incident_process` | What happens when something breaks, and in what order |
| `runbooks` | How a stranger fixes it without waking the author |
| `compliance_operations` | Which obligations recur, owned by whom, producing what evidence |
| `cost_model` | What running this actually costs — the complete figure |

---

# Core Objectives

- Define support commitments with the operator's agreement, and forecasts as forecasts.
- Turn each support burden into a product question rather than a staffing line.
- Grade severity by user impact so it can be assigned in seconds.
- Give every incident stage a named owner, and users something to read during an outage.
- Write runbooks a stranger can follow while tired.
- Turn every obligation into a schedule with an owner and an artifact.
- Complete the cost to serve, and check it against the ceiling.
- Answer the rota question honestly.

---

# What AI Should Learn Here

- A response target is a promise to users; only the operator can make it.
- The most common support request is usually a design defect with a queue attached.
- Severity defined by component produces an argument during the incident.
- "Investigate the issue" is not a step.
- Compliance is a schedule, not a state.
- Being compliant and being able to *show* it are different achievements.
- An untested restore is not a backup.
- A rota of one is not a rota.

---

# Commitments and Forecasts

Like `12-metrics`, this module holds two kinds of statement — and here the distinction is about
someone's time rather than someone's data:

| | Nature | Standing |
| --- | --- | --- |
| **Commitment** | Response targets, hours, cadences, owners | Requires the operator's agreement |
| **Forecast** | Ticket volume, support hours, staffing need | An assumption before launch |

A commitment written without agreement is a promise made on the operator's behalf, usually to
users, and they discover it when it is broken. A forecast presented as a plan is a staffing decision
resting on a guess.

**The owner rule follows from this.** An owner who has not been told is not an owner, and "the team"
is not a name — the same rule `10-execution` applies to blocked work, for the same reason.

---

# The Three-Stage Obligation Chain

This module completes something the framework starts in its second module:

| Module | With a regulatory obligation |
| --- | --- |
| `02-market` | Finds it and cites it |
| `09-technology` | Builds the mechanism that meets it, at a named enforcement point |
| **`13-operations`** | **Runs it — cadence, named owner, evidence produced** |

Each stage without the next is incomplete in a specific way. An obligation found but unmechanized
is a compliance gap. A mechanism built but never exercised is a compliance theatre. Only the third
stage produces something an auditor can be shown.

---

# The Cost to Serve, Completed

`09-technology` costed infrastructure and checked it against `06-business`'s ceiling. That check was
necessary and incomplete, because two lines could not exist yet:

| Line | Why it was missing |
| --- | --- |
| Support staffing | The volume forecast and response targets did not exist |
| Compliance operations | The recurring obligations were not yet a schedule |

With both, the **true cost per user** exists for the first time in the run — and this is the third
and final arithmetic check the framework runs against the business model:

| Module | Check |
| --- | --- |
| `09-technology` | Infrastructure cost per user against the ceiling |
| `11-growth` | Implied CAC against the payback ceiling |
| **`13-operations`** | **Complete cost to serve against the ceiling** |

If it exceeds the ceiling, that is a regress to `06-business` or `07-strategy`. What must not happen
is reducing the support estimate to make the arithmetic pass — that estimate came from response
targets the operator approved, and lowering it silently withdraws the commitment.

---

# Scope

**This module covers**

- Support channels, hours, targets, and the burden analysis
- Severity levels and the incident process
- Runbooks and alerting
- Non-negotiables and how a breach becomes visible
- Recurring compliance obligations, owners and evidence
- Data lifecycle, backup and restore
- Release, rollback and migration policy
- The complete running cost
- Operational risks and the rota

**This module does not cover**

| Not here | Belongs to |
| --- | --- |
| The security controls themselves | `09-technology` — carried, then operated |
| What the product does | `08-product` — settled |
| Build sequence and milestones | `10-execution` |
| Metric definitions | `12-metrics` — thresholds carried, then alerted on |
| Model monitoring and fallback behavior | `14-ai-systems` |

---

# Position in the Run

```
10-execution → [ 13-operations ] → deliver stage
```

This module closes the `operationalise` stage.

---

# What This Module Hands Forward

| Output | Consumed by | Used for |
| --- | --- | --- |
| Non-negotiables, alert instrumentation | `12-Build-Handoff.md` | Rules that must hold, and what must be emitted |
| Support-burden product changes | `09-Roadmap.md` | Fixes that remove permanent staffing cost |
| Operational risks | `10-Risks-and-Assumptions.md` | Single-person dependencies, coverage gaps |
| All outputs | `14-Operations-Plan.md` | The shipped operations artifact — optional in the manifest |

---

# The Reader

Each module in the second half of the framework has a harder reader than the last. Module 08's
reader cannot ask questions. Module 10's is starting work with a keyboard open.

> This module's reader is doing all of that, at 3am, alone, having been asleep ten minutes ago.

That is the standard the runbooks are calibrated to, and it is why U6 — written for a reader with no
access to this conversation — has its strictest interpretation here. The reader has no context *and*
no patience, and they are right not to have any.

---

# Success Criteria

- Support commitments attributed to the operator; forecasts tagged.
- Every support burden paired with the product change that would remove it.
- Severity assignable in ten seconds by whoever noticed.
- Every incident stage owned, and users told something during an outage.
- Every runbook passing the 3am test, with a verification and an escalation.
- Every alert with a threshold, a person and a runbook.
- Every obligation with a cadence, an owner and an evidence artifact.
- Restore and rollback status stated honestly, including "never".
- True cost per user inside the ceiling, or a regress recorded.
- The rota question answered.

---

# Self Assessment

- Whose promise is each response target?
- Which support burden should be a roadmap item instead of a staffing line?
- Could the person who noticed assign a severity?
- Would a stranger get stuck anywhere in my runbooks?
- Does every obligation produce something an auditor could be shown?
- Has restore ever actually been tested?
- Does the complete cost to serve fit the price?
- Can one person really do this?

---

> **Purpose Principle**
>
> Twelve modules planned a product. This one plans the years
> afterwards, which is where products are actually lost.
>
> Its most valuable output is often a limit, honestly stated.
