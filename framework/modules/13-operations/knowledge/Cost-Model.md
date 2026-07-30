---
Title: Cost Model
Module: 13-operations
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Complete the true cost to serve, and regress rather than absorb a ceiling breach.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 13-operations/knowledge/Compliance-Operations.md
Outputs:
  - cost_model
Related Modules:
  - 06-business
  - 09-technology
Tags:
  - Operations
  - Cost
  - Method
---

# Cost Model

---

# What It Is

The completion of the cost to serve. `09-technology` costed the infrastructure and checked it against `06-business`'s ceiling. That check was
necessary and incomplete — it omitted the two lines only this module can supply:

| Line | Why it was missing |
| --- | --- |
| **Support staffing** | Volume was unknown until the flow analysis and burden existed |
| **Compliance operations** | The recurring obligations were not yet a schedule |

With both, the **true cost per user** exists for the first time in the run.

```
infrastructure + inference + support staffing + compliance operations
  ÷ active users
  = true cost per user   vs   06-business's ceiling
```

> **If it exceeds the ceiling, that is a regress** — to `06-business` for the price or `07-strategy` for the scope. The thing that must not
> happen is absorbing it by assuming support takes less time than the plan just stated.

This is the last of the framework's three arithmetic checks:

| Module | Check |
| --- | --- |
| `09-technology` | Infrastructure cost per user against the ceiling |
| `11-growth` | Implied CAC against the payback ceiling |
| **`13-operations`** | **True cost to serve against the ceiling** |

---

# When It Applies

In Move 6 (Cost), last in the module and last of the three checks.

---

# How to Apply It Here

**Convert support volume into hours and hours into money, at a real rate.** Including the operator's own time —
`06-business/knowledge/CAC.md` makes the same point about founder-led sales, and it applies identically here.

**Price the compliance schedule.** Each recurring obligation from `Compliance-Operations.md` has a cadence and an owner, which means it has
hours attached.

**Show the arithmetic and tag every input.** Support volume is an assumption; the rates and the schedule are decisions. The same
show-your-working rule `02-market` applies to sizing.

**Run sensitivity on support volume.** It is the load-bearing assumption in this model exactly as CAC and churn are in `06-business`'s. If
double the tickets breaks the margin, that is the finding.

**Report a breach rather than resolving it here.** The regress is the mechanism. Quietly reducing the assumed support time to make the
arithmetic pass is the failure this check exists to catch.

---

# Where It Misleads

**Support time is treated as free because the operator does it.** It is the largest cost in many small products and it caps growth at what
one person can sustain — which is also `06-business/knowledge/GTM.md`'s founder-led ceiling.

**Compliance hours are omitted as overhead.** A quarterly access review, a restore rehearsal and an annual training are real recurring hours
with a legal function.

**The model is built at target scale only.** At launch there are few users and most of the fixed costs, so cost per user is at its worst
precisely when runway is tightest.

**Onboarding effort is excluded.** `11-growth/knowledge/Onboarding.md` notes that manual migration and setup persist longer than planned, and
they belong here as a cost per new customer.

**A ceiling breach is absorbed with an optimistic revision.** Each revision is individually defensible, and the outcome is a margin that
exists only in the document.

---

# Related

| | |
| --- | --- |
| `Support-Model.md` | The volume forecast and its standing |
| `Compliance-Operations.md` | The schedule being priced |
| `09-technology` `Infrastructure.md` | The first of the three checks |
| `06-business` | The ceiling, and where a breach regresses to |

---

> **Concept Note**
>
> Infrastructure, inference, support and compliance — divided by users,
> against the ceiling.
>
> A breach is a regress to price or scope. Assuming support takes less
> time than you just wrote down is not a resolution.
