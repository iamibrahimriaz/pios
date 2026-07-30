---
Title: Requirements
Module: 08-product
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Write requirements with priority language that means something, and resist scope laundering.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 08-product/core/06-Framework.md
Outputs:
  - prd_body
Related Modules:
  - 04-problem
  - 07-strategy
Tags:
  - Product
  - Requirements
  - Method
---

# Requirements

---

# What It Is

Statements of what the product must do, each with a parent problem and a priority that carries a fixed meaning.

| Level | Meaning — exactly |
| --- | --- |
| **MUST** | The release does not ship without it |
| **SHOULD** | The release ships without it, and is weaker for it |
| **COULD** | Genuinely optional. If it never happens, nothing is lost |

Two rules govern MUST, and both are gate criteria:

1. **MUST is reserved for capabilities above `07-strategy`'s MVP line.** Nothing below the line may be a MUST, however
   sensible it looks while writing.
2. **If nearly everything is a MUST, the labels are decoration.** A specification whose MUST list equals its
   requirement list has not prioritized; it has relabeled.

---

# When It Applies

In Move 2 (Specify), after the traceability spine exists. Nothing new is chosen in this module — something already
chosen is made precise.

---

# How to Apply It Here

**Name the parent problem on every requirement.** The spine assigned it before the requirement was written; carrying
it on the line is what keeps the trace checkable in both directions.

**Send discovered capabilities to the deferral ledger, not the MUST list.** Specifying invites completeness, and each
adjacent thing the product "obviously" also needs is individually reasonable. The ledger is where they go.

**Regress rather than expand when something is genuinely load-bearing.** If the core job cannot complete without a
capability that is below the line, that is `07-strategy`'s end-to-end test failing. The correct action is a recorded
regress to module 07 — not a quiet promotion here.

**Keep technology out of the requirement.** A requirement naming a framework, a database or a component has removed a
decision from `09-technology`, which chooses technology fifth of six for a reason.

**State what is optional in the input.** Which fields must be provided and which may be absent is the difference
between two engineers building the same thing and two engineers building different things.

---

# Where It Misleads

> **Scope laundering.** Module 07 drew a line. This module quietly moves it, one reasonable addition at a time, and
> the cut the operator approved is no longer the cut being built.

That is the module's named failure, and it is guarded mechanically: the requirement list is compared against
`07-strategy`'s cut as a list-versus-list boundary check, not as a judgment.

**Priority inflation is invisible from the inside.** Every MUST felt necessary when it was written. The check is
arithmetic — count them against the line — rather than introspective.

**Requirements get written as descriptions of screens.** A screen is a design output. A requirement describing a layout
has skipped the behavior and pre-empted design, and the behavior is what `10-execution` and `09-technology` both need.

**Aspirational language enters here and survives to the criteria.** `features/Acceptance-Criteria.md` bans a specific
vocabulary; requirements written in that vocabulary cannot produce criteria that pass it.

**A requirement absorbs several behaviors.** One requirement doing four things cannot be prioritized, sequenced, or
accepted independently. Splitting is nearly always correct.

---

# Related

| | |
| --- | --- |
| `features/Feature-Discovery.md` | The spine, and the orphan rule |
| `features/Feature-Prioritization.md` | Scoring and sequence |
| `Roadmap.md` | The deferral ledger |
| `07-strategy` | The binding cut, and where a regress goes |

---

> **Concept Note**
>
> MUST means the release does not ship. If everything is a MUST,
> nothing was prioritized.
>
> A capability discovered while specifying goes to the ledger — or
> back to module 07 as a failed cut. Never to the MUST list.
