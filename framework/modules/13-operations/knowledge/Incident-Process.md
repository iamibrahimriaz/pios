---
Title: Incident Process
Module: 13-operations
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Give every stage an owner and a timebox, and separate mitigating from resolving.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 13-operations/knowledge/SLAs.md
Outputs:
  - incident_process
Related Modules:
  - 02-market
  - 09-technology
Tags:
  - Operations
  - Incidents
  - Method
---

# Incident Process

---

# What It Is

What happens when something breaks, in order, with an owner and a timebox per stage.

```
Detect → Triage → Communicate → Mitigate → Resolve → Review
```

Two stages are routinely missing, and both are the ones users notice:

> **Communicate.** Users experiencing an outage with no word about it are having a worse incident than the outage itself. Name the channel,
> the person who writes it, and the point at which they do.

> **Mitigate, separately from Resolve.** Stopping the harm is not the same as fixing the cause, and conflating them produces incidents that
> stay open — and users who stay broken — while somebody diagnoses.

And the obligation that turns a technical event into a legal one:

> **Regulatory notification obligations** belong here. Where a regime imposes a breach notification deadline, name the deadline and who
> starts the clock. A deadline nobody knows is a deadline that gets missed, and the failure is legal rather than technical.

---

# When It Applies

In Move 3 (Respond), after severity is graded.

---

# How to Apply It Here

**Name the person per stage, not the team.** "The team communicates" means nobody does. This is the framework's recurring rule about
owners and it applies hardest under pressure.

**Write the mitigation options separately from the fix.** Disabling a feature, switching to manual, putting up a notice — each stops the
harm without diagnosing anything, and each is faster than a fix.

**Pre-write the communication template.** At the point it is needed, nobody has time to compose it. A template with blanks is the
difference between a message going out in five minutes and in two hours.

**Carry the notification deadline from `02-market` Frame 2.** For a breach involving regulated data, the clock starts at discovery, and who
starts it needs a name.

**Require a review with an output.** A review producing no runbook update, no alert change and no roadmap item was a conversation. That is
also where `Support-Model.md`'s product-signal question gets asked again.

---

# Where It Misleads

**Communication is treated as optional during a technical incident.** It is what users experience. Silence converts a thirty-minute outage
into a loss of confidence.

**Mitigate and resolve are collapsed.** The incident stays open while someone finds the root cause, and the users remain broken for the
duration of the investigation rather than the duration of the harm.

**The process is written for a large team.** For a solo operator it is a short checklist, and that is correct. What must survive is the
order, the communication step and the notification deadline.

**Reviews become blame allocation and then stop happening.** The output is a change to a runbook, an alert, or the product — nothing else.

**The regulated dimension is discovered during the incident.** A notification deadline learned at that moment has usually already been
partly consumed.

---

# Related

| | |
| --- | --- |
| `SLAs.md` | Severity, and who is woken |
| `Runbooks.md` | The steps for known failures |
| `Compliance-Operations.md` | Where notification obligations are scheduled |
| `09-technology`, `02-market` | Failure modes, and the regime's deadline |

---

> **Concept Note**
>
> Stop the harm before you find the cause, and tell people while you are
> doing it.
>
> Silence turns a short outage into a lost customer, and an unknown
> notification deadline turns a technical failure into a legal one.
