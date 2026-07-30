---
Title: Migration
Module: 09-technology
Section: knowledge/database
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Separate reversible schema changes from destructive ones, and cover data migration from the incumbent.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/database/Entities.md
Outputs:
  - Migration approach within data_model
Related Modules:
  - 03-user
  - 10-execution
Tags:
  - Technology
  - Migration
  - Concept
---

# Migration

---

# What It Is

Two different things share the word, and both matter here:

**Schema migration** — changing the model over time:

| Change | Reversible? |
| --- | --- |
| Add a nullable column, add a table, add an index | Yes |
| Add a non-null column with a default | Usually |
| Rename or retype a column | Only with both versions tolerated |
| Drop a column or table | **No** — the data is gone |

**Data migration** — bringing a customer's existing records in from the incumbent. This is one of the five switching-cost
dimensions `03-user` priced, and it is frequently the largest barrier to adoption.

---

# When It Applies

In Move 2 (Model) for the change strategy, and as a requirement wherever `03-user` found data that must move.

---

# How to Apply It Here

**Apply changes in expand-then-contract order.** Add the new shape, move to it, then remove the old one in a later release.
That sequence keeps `Deployment.md`'s revert path available.

**Mark destructive migrations explicitly.** A release containing one has no rollback. Knowing that before shipping is the
difference between a decision and an incident.

**Treat import from the incumbent as a first-class requirement.** If it is in scope, it needs its own entity handling, its
own validation and its own edge cases — and `08-product` should have specified them.

**Check the export side early.** `07-strategy`'s `risks/Technical.md` registers it: an incumbent whose data cannot be
extracted makes adoption impossible regardless of product quality.

**Plan for partial and dirty data.** Real imported data is incomplete, inconsistent and contains values the model forbids.
What happens to a row that fails validation is an `08-product` edge case, and silence is not an answer.

---

# Where It Misleads

**Migration is treated as an operational script rather than a product surface.** Import is something a customer does, sees
the results of, and judges the product by. It has behavior, errors and edge cases.

**Reversibility is assumed for all migrations.** Dropping a column is final. Test-environment habits — recreate and reload —
do not transfer to production data.

**Import is scoped as "we will help them".** That is `06-business`'s onboarding cost and `13-operations`' load. If it is
manual, someone is doing it, and the price has to cover them.

**Dirty data is discovered during the first real import.** It is discoverable earlier, from a sample export, and it usually
changes the validation rules.

**Migration timing ignores the size of the table.** A change that locks a large table is a maintenance window, which is a
decision involving the customer rather than a deployment detail.

---

# Related

| | |
| --- | --- |
| `Entities.md` | The model being changed |
| `09-technology` `Deployment.md` | Where revertibility is decided |
| `03-user` | Switching cost, including migration |
| `10-execution` | Where import becomes sequenced work |

---

> **Concept Note**
>
> Expand, migrate, contract — in separate releases, so a revert stays
> possible.
>
> And importing a customer's existing data is a product surface they
> will judge you by, not a script.
