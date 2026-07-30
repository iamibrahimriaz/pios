---
Title: Runbooks
Module: 13-operations
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Write procedures a stranger could follow alone at 3am, including what not to do.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 13-operations/knowledge/Incident-Process.md
Outputs:
  - runbooks
Related Modules:
  - 08-product
  - 09-technology
Tags:
  - Operations
  - Runbooks
  - Method
---

# Runbooks

---

# What It Is

The procedures, written to one standard:

> **The 3am test.** Could someone who did not build this system follow this, alone, half awake, with nobody to ask?

That is the defining standard of this module, and the operational sibling of `10-execution`'s cold-start test.

| Not a step | A step |
| --- | --- |
| "Investigate the issue" | "Run «command». If the output shows «pattern», go to step 4" |
| "Check the logs" | "Open «location». Search for «string» in the last 15 minutes" |
| "Restart the service" | "Run «command». Wait for «observable». If it does not appear within 60 seconds, escalate" |

**Four things beyond the steps:**

| Element | Why |
| --- | --- |
| The precise trigger | So the reader knows this is the right runbook |
| **What access is needed, and where to get it** | The most common 3am blocker is a credential |
| A recovery verification | Otherwise "done" means "I ran the steps" |
| An escalation | Because the runbook will sometimes not work |

And one more that experience adds: **"do not do"** — the tempting action that makes it worse. Every system has one, and it is usually
attempted by somebody helpful.

---

# When It Applies

In Move 4 (Write), sourced from `09-technology`'s failure modes and `08-product`'s edge cases — both already enumerated what can go wrong.

---

# How to Apply It Here

**Write steps in three columns: do this, expect this, if different.** The third column is what makes it followable by someone who cannot
diagnose.

**Put the access requirements at the top.** Which credentials, which accounts, which approvals — and where to obtain them. A procedure
blocked on access nobody has is the most avoidable failure available.

**Never write "investigate".** It is the instruction that means "work it out", which is precisely what the reader cannot do at 3am.

**Verify recovery explicitly.** What observable state proves it worked. `09-technology/knowledge/security/Recovery.md` makes the same point
about restores: completing the steps is not the same as having recovered.

**Write the "do not do" line.** Restarting the thing mid-migration, clearing the queue, running the reconciliation twice. Whatever the
tempting wrong move is, name it.

---

# Where It Misleads

**Runbooks are written by the person who built the system.** They compress the parts that are obvious to them, and those are exactly the
parts the reader needs. The 3am test asks about a stranger for this reason.

**They are written and never followed.** An unexercised runbook is a hypothesis. `Backups.md` applies the same point to restores — the
rehearsal is what makes it real.

**They go stale silently.** A command that changed, a location that moved, a service that was renamed. `Incident-Process.md`'s review step
is the mechanism that keeps them current.

**Only the exotic failures get runbooks.** The frequent, mundane ones — a stuck job, a full disk, an expired certificate — are where the
time actually goes.

**Escalation points to a person who may be the reader.** For a solo operator, escalation means an external party: a provider's support, a
contractor, or a documented decision to accept the outage until morning. That is an honest answer and it should be written.

---

# Related

| | |
| --- | --- |
| `Incident-Process.md` | The process runbooks sit inside |
| `Backups.md` | The runbook that must be rehearsed |
| `Monitoring.md` | Every alert needs one |
| `08-product`, `09-technology` | The failures already enumerated |

---

> **Concept Note**
>
> Do this, expect this, if different. Access at the top, verification at
> the end, and never the word "investigate".
>
> Then name the tempting action that makes it worse — every system has
> one.
