---
Title: Common Mistakes
Module: 13-operations
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Name the recurring failures in operations planning and what each costs.
Audience:
  - Product Managers
  - Founders
  - Operators
Prerequisites:
  - 13-operations/learn/01-Why-It-Matters.md
Outputs:
  - Recognition of operations failure patterns
Related Modules:
  - 06-business
  - 09-technology
Tags:
  - Operations
  - Mistakes
  - Learn
---

# Common Mistakes

---

# Overview

Operations failures are discovered at the worst possible moment — during an incident, an
audit, or a cash-flow review. That is what makes planning them in advance worth the
discomfort.

---

# 1. The Commitment Nobody Agreed To

**What it looks like.** A response-time table written by the product team.

**Why it is tempting.** The plan needs numbers, and the person who will answer the phone
is not in the room.

**What it costs.** It is a promise made on someone's behalf. It breaks during the first
incident, in front of the first customer, and the customer's complaint is legitimate.

**Instead.** Commitments come from the operator and are tagged `[verified: operator]`.
Everything else is a forecast and is tagged as an assumption. The two must not appear in
the same voice.

---

# 2. The Operator's Time Priced at Zero

**What it looks like.** A cost model of infrastructure and inference.

**Why it is tempting.** It generates no invoice, and early on it feels like commitment
rather than cost.

**What it costs.** It is the single most common reason this module's check passes when it
should fail. For service-delivered products the human hours are the dominant line, and a
model omitting them shows a comfortable margin on something nobody can afford to run.

**Instead.** A real hourly rate. If the business does not work at that rate, that is the
finding — and it arrives now rather than in month fourteen.

---

# 3. The Breach Absorbed

**What it looks like.** "Costs are expected to decrease as the product matures."

**Why it is tempting.** It is probably true, it requires no difficult conversation, and
the forecast is the only lever entirely under your control.

**What it costs.** The whole purpose of the check. A margin produced by revising the
forecast that just failed exists only in the document, and no later module will test it
again.

**Instead.** Regress. To module 06 for the price, or module 07 for the scope, with a
recommendation. In the worked example the recommendation is to raise the price, and
module 06's value calculation supports it.

---

# 4. The Runbook That Says "Investigate"

**What it looks like.** "1. Investigate the cause. 2. Check the logs."

**Why it is tempting.** It is what you would do, and you know what it means.

**What it costs.** At 3am, the person following it does not. "Investigate" requires the
knowledge the runbook exists to substitute for, so the runbook accomplishes nothing at
the moment it is needed.

**Instead.** Step, expected, if different. Plus access at the top and a verification at
the end. Hand it to someone unfamiliar and see where they stop.

---

# 5. No "Do Not Do" Line

**What it looks like.** A correct, complete runbook with no warnings.

**Why it is tempting.** It seems obvious that you would not clear the queue.

**What it costs.** At 3am, under pressure, the action that silences the alarm is
enormously attractive — and in the worked example, clearing the queue destroys recorded
consultations with no recovery. Every system has one such action.

**Instead.** Name it, with the consequence. It is one line and it is the most valuable
one in the document.

---

# 6. Compliance Recorded as Achieved

**What it looks like.** "We are compliant. An annual review is planned."

**Why it is tempting.** It is a state you can declare, and reviews are easy to plan.

**What it costs.** A control that existed once. An auditor asks for evidence and there is
none — not because the work was not done, but because nothing recorded that it was.

**Instead.** Cadence, owner, evidence, location. A quarterly access review producing a
dated signed list is demonstrable; the same review producing a memory is not.

---

# 7. An Obligation Owned by a Role

**What it looks like.** "Owner: the engineering team."

**Why it is tempting.** Naming a person makes it real, and roles change.

**What it costs.** It belongs to nobody. Everyone assumes someone else, and the discovery
happens when it has not been done for four quarters.

**Instead.** A name. If the same name appears against eleven obligations, that is a
finding about the whole plan and it should be reported rather than tidied.

---

# 8. Alerts Without a Runbook

**What it looks like.** Comprehensive monitoring, thresholds tuned, notifications wired.

**Why it is tempting.** Monitoring feels like preparation, and runbooks are tedious.

**What it costs.** An alert with no runbook wakes someone who then improvises. Repeated
enough, it produces the alert fatigue that causes the real one to be missed.

**Instead.** Three things per alert — threshold, person, runbook — and delete any alert
that has no available action. The worked example deletes three that fired in testing for
exactly that reason.

---

# 9. Alerting on Failure Rather Than on Absence

**What it looks like.** An alert when the retention job errors.

**Why it is tempting.** Errors are what you watch for.

**What it costs.** A stopped job raises no error. The most dangerous scheduled task is one
that silently stops running, and failure-based alerting is blind to it.

**Instead.** Alert on the absence of success within a window. This applies to every
scheduled obligation.

---

# 10. The Rota of One, Described as a Rota

**What it looks like.** A coverage table with shifts, in an organization of one person.

**Why it is tempting.** It looks professional and the honest version looks weak.

**What it costs.** It is a commitment that cannot be met. It breaks publicly, and the
customer was told something untrue at the point of sale.

**Instead.** State it plainly: one person, weekday hours, best effort, customers notified
when unavailable. Told to the customer at the sale. A rota of one is not a rota, and
saying so is the honest version of a coverage table.

---

# The Pattern

| Mistake | Underlying move |
| --- | --- |
| Uncommitted commitment | Filling a table with numbers |
| Time priced at zero | Omitting the cost with no invoice |
| Breach absorbed | Pulling the only lever you control |
| "Investigate" | Writing for yourself |
| No "do not do" | Assuming the obvious is obvious |
| Compliance as a state | Declaring rather than evidencing |
| Role as owner | Avoiding naming someone |
| Alert without runbook | Monitoring as preparation |
| Alerting on failure | Watching for the wrong signal |
| Rota of one | Presenting capability you do not have |

Half of these are the same underlying move: **producing a document that describes a
capability the organization does not have.** In operations that gap does not stay
theoretical — it is tested, on a schedule, by reality.

---

> **Mistakes Principle**
>
> Every one of these is comfortable to write and expensive to discover.
>
> The discovery happens during an incident, an audit, or a cash-flow review — which are
> the three worst moments available.
