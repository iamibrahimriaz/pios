---
Title: Related Modules
Module: 06-business
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Show how the Business module connects to the framework, and trace the three arithmetic checks it sets up.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 06-business/README.md
Outputs:
  - Understanding of the business stage's position in the chain
Related Modules:
  - 09-technology
  - 11-growth
  - 13-operations
Tags:
  - Business
  - Relationships
  - Learn
---

# Related Modules

---

# Overview

This module is the framework's economic anchor. Three later modules are required to
check their own plans against numbers set here, and each of those checks is a place
where a run can discover the business does not close.

---

# What It Takes In

| Input | From | Used for |
| --- | --- | --- |
| `tam_sam_som` | `02-market` | The ceiling on the revenue model |
| `pricing_comparison` | `05-competition` | The competitive constraint on price |
| `segments` | `03-user` | Who is being priced, and whether they can pay |

The gate fails back to `05-competition`, usually because a price cannot be justified
without competitor figures that were estimated rather than captured.

---

# The Three Arithmetic Checks

This is the module's defining relationship with the rest of the framework:

```
06-business  price · gross margin · cost ceiling · payback ceiling
     │
     ├──→ 09-technology   infrastructure cost per user vs the ceiling
     ├──→ 11-growth       implied CAC vs the payback ceiling
     └──→ 13-operations   true cost to serve — including human time — vs the ceiling
```

Three properties make these checks work:

**They run in different modules.** Each catches a different kind of cost, and no single
author is checking their own arithmetic.

**They are cumulative.** Module 13's check includes what modules 09 and 14 found, which
is why it is the last one and the one that most often fails.

**Failure means regress, not adjust.** A breach returns to this module for the price or
to `07-strategy` for the scope. It is never absorbed by revising the forecast that just
produced it.

That last rule is the whole point. Absorbing a breach is always the smallest available
change and it is always individually defensible, which is why the framework states the
alternative explicitly rather than leaving it to judgment.

---

# What It Sends Forward

| Output | Who consumes it | What they do with it |
| --- | --- | --- |
| `business_model` | `07-strategy` | Constrains which approaches are viable |
| `pricing_strategy` | `11-growth`, `13-operations` | The revenue side of both checks |
| `unit_economics` | `09`, `11`, `13` | The ceilings |
| `go_to_market` | `11-growth` | The starting point the growth plan elaborates |
| `revenue_model` | `12-metrics` | What the north star has to be consistent with |

---

# The Milestone Zero Connection

If module 04 declared a shortfall, module 11 is required to gate acquisition spend on
Milestone Zero — the validation that would resolve it. That gate is enforced using this
module's payback ceiling: spending before the problem is confirmed puts money against
an unvalidated premise.

So a run with weak evidence produces a business model whose spending permission is
conditional, and the condition was set two modules earlier. That interaction is easy to
miss and it is one of the framework's better features.

---

# What It Deliberately Does Not Do

| It does not | Because |
| --- | --- |
| Choose the solution | That is `07-strategy`, which consumes the model |
| Plan channels | That is `11-growth`, against the ceiling set here |
| Estimate infrastructure cost | That is `09-technology`, which reports back |
| Decide viability | It states the conditions; three later modules test them |

The last row is the one most often misread. A completed business model is frequently
treated as the go/no-go decision, and it is the specification of what that decision
depends on.

---

> **Relationships Principle**
>
> This module does not prove the business works.
>
> It writes down the numbers precisely enough that three later modules can prove it
> does not — and the framework is more valuable for the runs where they do.
