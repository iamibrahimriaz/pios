---
Title: SLAs
Module: 13-operations
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Grade severity by user impact, and commit only to what a rota can actually staff.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 13-operations/knowledge/Support-Model.md
Outputs:
  - Severity levels within support_model
Related Modules:
  - 06-business
  - 09-technology
Tags:
  - Operations
  - Severity
  - Concept
---

# SLAs

---

# What It Is

Severity levels and the response commitments attached to them — graded **by user impact, not by which component failed.**

| Wrong | Right |
| --- | --- |
| "The database is down" | "Users cannot save work" |
| "The queue is backed up" | "Notes take an hour to appear" |
| "An integration is failing" | "Referral letters cannot be sent" |

Component-based severity produces an argument during the incident, which is the worst possible time to be having it. Impact-based severity
can be assigned by whoever noticed, in seconds.

Two fixed points:

> **Data loss is always S1**, using the data-loss position `09-technology` was required to state.

And per level: the first response time, the resolution target, and **who is woken** — which is where a coverage claim becomes a person's
night.

---

# When It Applies

In Move 2 (Grade), before the incident process and the runbooks — runbooks written without severity have no sense of urgency attached.

---

# How to Apply It Here

**Write each level as a user-facing sentence.** "Users cannot complete a consultation note" is assignable in seconds by anyone.

**Apply the ten-second test.** If someone noticing the problem cannot classify it in ten seconds, the definitions are too complicated to
use under pressure.

**Name who is woken per level, by role and by person.** A severity level with a response time and no named person is a commitment nobody
made.

**Answer the rota question honestly.** A rota of one is not a rota. For a solo operator, "weekday hours only, best effort, and here is what
happens when I am unavailable" is worth more than a coverage table nobody can staff.

**Distinguish an internal target from a contractual SLA.** `06-business/knowledge/pricing/Enterprise.md` treats the contractual version as
premium content with a real recurring cost, and breaching one has financial consequences.

---

# Where It Misleads

**Severity is defined by system component because that is how engineers think about it.** The classification then requires knowing the
cause, which is exactly what is unknown at the start of an incident.

**Response times are committed without a rota behind them.** A 24/7 one-hour response from a single person is not a commitment, it is a
sentence.

**Everything is graded high.** The same failure `07-strategy/knowledge/risks/Mitigation.md` names about uniform risk ratings: if
every incident is S1, prioritization is impossible and the response degrades for the ones that matter.

**Data loss is graded by volume.** One record lost in a clinical system is an S1. The position `09-technology` stated makes this
non-negotiable rather than proportionate.

**Availability is promised in nines without measuring it.** Three nines is roughly nine hours of downtime a year; four is under an hour.
Committing to either requires knowing what the system actually does.

---

# Related

| | |
| --- | --- |
| `Incident-Process.md` | What happens once graded |
| `Runbooks.md` | The steps per failure |
| `09-technology` | The data-loss position, stated there |
| `06-business` | Contractual SLAs as priced obligations |

---

> **Concept Note**
>
> Grade by what the user cannot do, in a sentence anyone can assign in
> ten seconds.
>
> A response time with no named person behind it is a promise nobody
> made — and a rota of one is not a rota.
