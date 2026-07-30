---
Title: Core Principles
Module: 13-operations
Section: core
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the principles that govern judgment when planning operations.
Audience:
  - AI Agents
  - Operators
  - Founders
Prerequisites:
  - constitution/core/03-Core-Principles.md
Outputs:
  - Consistent operational judgment
Related Modules:
  - 14-ai-systems
Tags:
  - Operations
  - Principles
---

# Core Principles

---

# Principle Statement

> Everything in this module is somebody's time.
>
> The framework cannot promise it, so its job is to write down
> exactly whose promise each line is.

---

# Principle 1 — A Response Target Is a Promise to Users

Only the operator can make it. Written without their agreement, it is a promise made on their
behalf — and they find out when it is broken, in public.

Attribute every commitment, or mark it unapproved.

---

# Principle 2 — Forecasts Are Not Commitments

Ticket volume, support hours, staffing need. None of them observable before launch.

A forecast presented as a plan is a staffing decision resting on a guess, and it becomes a budget
line that nobody remembers was invented.

---

# Principle 3 — The Most Common Support Request Is a Design Defect

It arrives with a queue attached, and the queue is paid for indefinitely.

Every expected burden names the product change that would remove it. Some burdens are genuinely
permanent — say which, and why that is correct.

---

# Principle 4 — Severity Is Defined by User Impact

"The database is down" is not a severity. "Users cannot save work" is.

Component-based severity produces an argument during the incident, which is the worst available
time to have one. The test: could the person who noticed assign a level in ten seconds without
knowing the architecture?

---

# Principle 5 — Data Loss Is Always S1

`09-technology` was required to state what can be lost and when. This module makes that operational.

---

# Principle 6 — Users Experiencing Silence Are Having a Worse Incident

Name the channel, the person who writes the update, and the moment they do it.

An outage with no word about it costs more trust than the outage itself, and it is the cheapest thing
in this document to get right.

---

# Principle 7 — Mitigate Is Not Resolve

Stopping the harm and fixing the cause are different actions with different urgencies.

Conflated, incidents stay open — and users stay broken — while somebody diagnoses a root cause.

---

# Principle 8 — Every Stage and Every Alert Has a Named Owner

"The team" is not an owner. An obligation nobody owns is an obligation nobody meets, and an owner
who has not been told is not an owner.

---

# Principle 9 — "Investigate the Issue" Is Not a Step

A step says what to do, precisely enough to do it, and what you should see afterwards.

The reader is tired, has no context, and cannot ask anyone. That is not a pessimistic assumption; it
is the normal condition in which runbooks are read.

---

# Principle 10 — Every Step Needs an Expected Result

Without one the reader cannot tell whether the step worked, so they proceed anyway — and the failure
surfaces three steps later, unattributable.

---

# Principle 11 — Every Runbook Needs a Verification and an Escalation

The verification is how the reader knows they are finished. The escalation is what happens when the
runbook does not work, which it sometimes will not.

A runbook that ends after its last step leaves the reader with neither.

---

# Principle 12 — An Alert Needs a Threshold, a Person and a Runbook

Missing any of the three, it is worse than no alert.

> A tolerated alert teaches the team to tolerate all of them.

So an alert nobody acts on is deleted, not ignored.

---

# Principle 13 — Compliance Is a Schedule, Not a State

`02-market` found the obligation. `09-technology` built the mechanism. This module runs it.

A mechanism that exists but is never exercised satisfies an auditor for exactly as long as nobody
looks.

---

# Principle 14 — Every Obligation Produces Evidence

Being compliant and being able to demonstrate compliance are different achievements, and only the
second survives an audit.

An obligation with no artifact cannot be shown to have been met, however diligently it was performed.

---

# Principle 15 — An Untested Restore Is Not a Backup

Nor is an untested rollback a rollback, nor an unwalked runbook a runbook.

None of the three is expensive to verify. All of them are discovered unverified during the incident
that needed them. "Never tested" is an acceptable answer; silence is not.

---

# Principle 16 — An Unautomated Policy Is a Policy Nobody Executes

Retention, deletion, archival. Where a step depends on somebody remembering, mark it manual and give
it an owner and a cadence — or accept that it will not happen.

---

# Principle 17 — The Cost Model Must Include Support and Compliance

They are the two lines no earlier module could supply and the two every cost model forgets.

Without them there is no cost to serve — only an infrastructure bill.

---

# Principle 18 — Do Not Lower an Estimate to Pass the Cost Check

The support estimate was derived from response targets the operator approved. Reducing it silently
withdraws the commitment, and the withdrawal surfaces as broken promises rather than a revised plan.

If the cost exceeds the ceiling, the price or the scope changes. That is a regress.

---

# Principle 19 — A Rota of One Is Not a Rota

Coverage claimed with nobody behind it fails during the first incident.

An honest limit — "weekday hours, best effort, and here is what happens when I am away" — is a real
operations plan. A four-hour target staffed by one person is a wish.

---

# Principle Hierarchy

```
Support commitments attributed, forecasts tagged
   ↓
Severity graded by user impact
   ↓
Incident process owned, with users informed
   ↓
Runbooks that survive a stranger at 3am
   ↓
Obligations scheduled, owned, producing evidence
   ↓
The complete cost to serve, checked
   ↓
The rota question answered honestly
```

Each level depends on the one above. Runbooks written before severity exists carry no urgency;
compliance scheduled last leaves mechanisms nobody exercises.

---

# Common Violations

- Response targets nobody agreed to.
- Volume forecasts presented as plans.
- Support burdens accepted without asking what would remove them.
- Severity defined by component.
- Data loss triaged below S1.
- Users told nothing during an outage.
- Mitigate and Resolve treated as one stage.
- "The team" as an owner.
- "Investigate the issue" as a step.
- Steps with no expected result.
- Runbooks with no verification or escalation.
- Alerts with no person or no runbook.
- Compliance asserted as a state.
- Obligations producing no evidence.
- Restore, rollback and runbooks presented as working, untested.
- Unautomated policies assumed to happen.
- Cost models missing support and compliance.
- Estimates lowered to pass the cost check.
- Coverage that one person cannot staff.

---

# Self Assessment

- Whose promise is each target?
- Is every forecast tagged?
- Which burden should be a roadmap item?
- Could severity be assigned in ten seconds?
- Do users get told anything?
- Are Mitigate and Resolve separate?
- Does every stage, alert and obligation have a name against it?
- Would a stranger get stuck in any runbook?
- Does every step say what you should see?
- Does every obligation produce an artifact?
- Have restore and rollback been tested — and does the document say so?
- Does the cost include support and compliance?
- Did any estimate fall to make the arithmetic work?
- Can one person actually sustain this?

---

> **Core Principle**
>
> Every other module can be wrong and cost a rewrite.
>
> This one is wrong at 3am, while something is broken, and the
> person reading it has no one to ask.
