---
Title: Compliance Operations
Module: 13-operations
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Turn obligations into a schedule with an owner and evidence produced.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 13-operations/core/06-Framework.md
Outputs:
  - compliance_operations
Related Modules:
  - 02-market
  - 09-technology
Tags:
  - Operations
  - Compliance
  - Method
---

# Compliance Operations

---

# What It Is

The third stage of a chain running through the whole framework:

| Module | What it does with an obligation |
| --- | --- |
| `02-market` | Finds it |
| `09-technology` | Builds the mechanism that meets it |
| **`13-operations`** | **Runs it — owner, cadence, evidence produced** |

> **Compliance is a schedule, not a state.**
>
> A mechanism that exists but is never exercised — a log nobody reviews, a training nobody repeats, a restore nobody tests — satisfies an
> auditor for exactly as long as nobody looks.

Every recurring obligation states four things:

| | Why |
| --- | --- |
| The cadence | Monthly, quarterly, annually |
| A **named owner** | "The team" is not an owner |
| The evidence it produces | A record, a report, a signed review |
| Where that evidence is kept | Findable a year later, by someone else |

> Being compliant and being able to **show** you were compliant are different achievements, and only the second one survives an audit.

---

# When It Applies

In Move 5 (Comply), producing `compliance_operations`.

---

# How to Apply It Here

**Take the obligations from `09-technology`'s mechanisms, one row each.** Module 09 named the mechanism and the enforcement point; this adds
who runs it and how often.

**Include the recurring items that look like engineering tasks.** Access review, restore rehearsal, dependency scanning, log review,
training. Each is an obligation with a cadence in most regimes.

**Make the evidence column concrete.** "Quarterly access review, signed off by «owner», stored in «location»" is auditable. "Access is
reviewed regularly" is not.

**Schedule the restore rehearsal explicitly.** `09-technology/knowledge/security/Recovery.md` records `restore_tested: yes | no | never`,
and this is the cadence that keeps it at yes.

**Cost it.** `Cost-Model.md` needs the hours. Compliance operations is one of the two lines the framework could not compute until this
module existed.

---

# Where It Misleads

**Compliance is recorded as achieved.** `09-technology` forbids claiming it, and this module explains why: a control exercised once was a
control that day. The cadence is the control.

**Owners are roles rather than people.** A rota entry with no name is unassigned, and the obligation quietly belongs to nobody.

**Evidence is assumed to be reconstructible later.** It is not. An access review performed and unrecorded did not happen, as far as an
auditor is concerned.

**The schedule is written and not diarized.** An obligation with a cadence and no reminder is an obligation that lapses in month four, and
nothing reports it — `Monitoring.md`'s absence-alerting point applies.

**The operator's own access is omitted.** Who at the vendor can view customer data, reviewed on a cadence, is a question institutional
buyers ask and `09-technology/knowledge/security/HIPAA.md` treats as an obligation.

---

# Related

| | |
| --- | --- |
| `Monitoring.md` | Alert hygiene as part of the same move |
| `Backups.md` | The rehearsal that must be scheduled |
| `Cost-Model.md` | Where these hours are priced |
| `02-market`, `09-technology` | Where obligations are found and built |

---

> **Concept Note**
>
> Cadence, named owner, evidence produced, and where it is kept.
>
> Being compliant and being able to show it are different achievements —
> and only one of them survives an audit.
