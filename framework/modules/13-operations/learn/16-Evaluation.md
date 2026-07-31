---
Title: Evaluation
Module: 13-operations
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Give a learner a way to test whether their operations plan would survive an incident.
Audience:
  - Product Managers
  - Founders
  - Operators
Prerequisites:
  - 13-operations/learn/10-Common-Mistakes.md
Outputs:
  - A self-assessment for operations planning
Related Modules:
  - 06-business
  - 09-technology
Tags:
  - Operations
  - Evaluation
  - Learn
---

# Evaluation

---

# Overview

Operations is the most testable module in the framework, because everything in it is
performable. You can hand someone a runbook and watch.

---

# Exercise 1 — Run the 3am Test

Give a runbook to someone unfamiliar with the system. Ask them to follow it aloud without
asking you anything.

**Passing looks like.** They complete it, or they stop at a genuine escalation point.

**Failing looks like.** They stop at "investigate," or at a credential the document does
not locate. Both are the standard failures and both are one line to fix.

---

# Exercise 2 — Separate Commitments From Forecasts

Take a support plan and mark every statement as a commitment or a forecast.

**Passing looks like.** Every commitment traces to a person who agreed to it.

**Failing looks like.** Response times written by whoever wrote the plan. Those are
promises made on someone's behalf.

---

# Exercise 3 — Price Yourself In

Take a cost model and add your own hours at a real rate: support, onboarding, compliance,
delivery.

**Passing looks like.** The dominant cost line changes, and it is now human time.

**Failing looks like.** Infrastructure still dominates. For most small products that is
the arithmetic of a model with a zero in it.

---

# Exercise 4 — Name the Tempting Action

For any system you know, name the action that would silence an alarm and make the
situation worse.

**Passing looks like.** You find one immediately, and can state the consequence.

**Failing looks like.** You cannot think of one. Every system has one; not knowing yours
means it is available to whoever is on call.

---

# Exercise 5 — Assign Every Obligation

Take a compliance list and write a person's name, a cadence, an evidence artifact and a
location against each row.

**Passing looks like.** Some names repeat until the load is visibly unreasonable. That is
a finding about the plan, not a formatting problem.

**Failing looks like.** Roles instead of names, or an empty evidence column.

---

# Exercise 6 — Alert on Absence

Take a scheduled job and write the alert. Then check whether it would fire if the job
stopped running entirely.

**Passing looks like.** It alerts on the absence of a success signal within a window.

**Failing looks like.** It alerts on errors. A stopped job produces none.

---

# Exercise 7 — Force the Regress

Take a cost model that clears its ceiling and increase support volume until it does not.
Write the regress: which module, what recommendation.

**Passing looks like.** A specific recommendation with reasoning — raise the price, cut
the scope — and an identification of whose decision it is.

**Failing looks like.** You revise the volume estimate. That is the absorption, and it
feels like refinement.

---

# Rubric

| Level | Description |
| --- | --- |
| **Not yet** | Support plan of intentions; compliance stated as a status; no runbooks |
| **Working** | Runbooks exist; costs cover infrastructure; obligations listed |
| **Competent** | 3am test passed; own hours priced; obligations carry all four fields |
| **Fluent** | Reports a ceiling breach as a regress with a recommendation, and states the rota of one honestly |

---

# A Note on What Cannot Be Assessed Here

Whether the plan is sustainable for the person running it. Nothing here measures that,
and it is the question that decides whether a small product survives its second year.

The framework can surface the inputs — the same name against eleven obligations, an
unsustainable rota, a dominant human cost line — and the judgment about whether that is
livable belongs to the operator. What the module can insist on is that the information is
visible rather than distributed across four sections where nobody adds it up.

---

> **Evaluation Principle**
>
> Hand the runbook to a stranger. Watch where they stop.
>
> It is the same test as module 10's build handoff, applied to a person who is tired,
> alone, and being paged.
