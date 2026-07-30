---
Title: Error States
Module: 10-execution
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Turn failure responses into recoveries the user can actually perform.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 10-execution/knowledge/Loading-States.md
Outputs:
  - Error states within ux_flows
Related Modules:
  - 08-product
  - 09-technology
Tags:
  - Execution
  - UX
  - Concept
---

# Error States

---

# What It Is

What the user sees and does when something fails — the point where `09-technology`'s status codes become an experience.

Every error state answers three questions:

| Question | Bad answer | Good answer |
| --- | --- | --- |
| What happened? | "An error occurred" | "The note could not be saved" |
| Is my work safe? | Silence | "Your text is still here" |
| What do I do now? | "Try again later" | "Retry" — or a named alternative |

The second question is the one products fail. `08-product`'s invalid-input category required the input preserved, and an error screen
that discards what the user wrote turns a recoverable problem into lost work.

And the framework's traceability point: module 08 worked five edge categories, `09-technology` mapped them to failure responses. If they
do not appear here, they exist in three documents and no running system.

---

# When It Applies

In Move 1 (Flow), as the failure and recovery table per path, and as a required state per screen.

---

# How to Apply It Here

**Write errors in the user's terms, from `03-user`'s vocabulary.** They describe what did not happen to *their* work, not what the
system encountered.

**Distinguish the four kinds the user can act on differently:** their input was wrong, they lack permission, the system failed, or the
connection failed. Each has a different recovery, and one generic message serves none.

**State whether retrying is safe, and make it one action.** `09-technology/knowledge/api/Errors.md` carries that flag in the contract;
this is where it becomes a button.

**Keep internal detail out.** Stack traces and identifiers belong in `13-operations`' logs. An error containing them is both unhelpful
and an information leak.

**Respect the disclosure policy.** "You do not have permission to view record 4821" confirms 4821 exists.
`09-technology/knowledge/api/Authorization.md` decided; the interface must not undo it.

---

# Where It Misleads

**Errors are written for the developer.** They surface the technical cause and omit the only two things the user needs: whether their
work survived and what to do next.

**One generic error covers everything.** A validation failure and a service outage need opposite responses — correct the field, or wait
and retry.

**Recovery is not offered.** "Please try again later" leaves the user to guess whether the work was saved, whether retrying duplicates
it, and how long later is.

**Errors are only designed for the paths that failed during development.** The five categories are the checklist precisely because
recall covers two or three.

**The offline case is treated as an error.** For `03-user`'s unreliable-connectivity findings it is an expected condition, and the
principle derived from that finding usually requires the path to complete anyway.

---

# Related

| | |
| --- | --- |
| `Loading-States.md` | The wait that becomes a failure |
| `Microcopy.md` | The wording |
| `08-product` | The five edge categories |
| `09-technology` | Status codes, retry flags and disclosure |

---

> **Concept Note**
>
> Say what happened, whether their work survived, and what to do
> next.
>
> The second one is the one products omit — and it is the difference
> between an inconvenience and lost work.
