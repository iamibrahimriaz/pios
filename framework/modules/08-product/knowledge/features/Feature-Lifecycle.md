---
Title: Feature Lifecycle
Module: 08-product
Section: knowledge/features
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Recognize that every shipped requirement becomes a permanent obligation.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 08-product/knowledge/Requirements.md
Outputs:
  - Lifecycle awareness within prd_body
Related Modules:
  - 13-operations
  - 12-metrics
Tags:
  - Product
  - Lifecycle
  - Concept
---

# Feature Lifecycle

---

# What It Is

The full cost of a requirement, which does not end at shipping.

| Stage | What it costs |
| --- | --- |
| **Specified** | The effort estimated in Move 5 |
| **Shipped** | Nothing further, briefly |
| **Supported** | Questions, confusion, bug reports — permanently, in `13-operations` |
| **Maintained** | Every dependency upgrade, every schema change, every regression test |
| **Constraining** | It limits what can change elsewhere, forever |
| **Removed** | Migration, communication, and users who relied on it |

The asymmetry is the point: **specifying is cheap, shipping is measurable, and everything after is permanent and
unmeasured.** A requirement's estimate covers only the second column's first row.

Removal is the hardest stage. Once a capability is in front of users, someone depends on it, and taking it away is a
harder conversation than never having built it.

---

# When It Applies

As a consideration during Move 2 (Specify) and Move 5 (Order), and as the honest counterweight to scope inflation.

---

# How to Apply It Here

**Weigh the permanent cost against the problem rank.** A requirement serving a low-ranked problem carries the same
ongoing support and maintenance cost as one serving the sharpest. That asymmetry is what makes the ledger valuable.

**Prefer deferral to speculative inclusion.** Anything shipped can only be removed with cost. Anything deferred can be
added later at the cost of building it — which is the smaller of the two.

**Note requirements that will generate support load.** `13-operations` staffs for them and prices the true cost to
serve. A capability with a confusing edge case is a recurring ticket, not a one-time build.

**Flag anything that constrains future change.** A public identifier, an export format, an API surface, a stored data
shape. These become commitments `09-technology` cannot easily revise.

**Say what would justify removing it.** Almost nobody writes this, and its absence is why products accumulate. A
usage threshold from `12-metrics` is the usual form.

---

# Where It Misleads

**Only build cost is estimated, so only build cost is considered.** Support and maintenance are real, recurring, and
invisible in any effort score. That invisibility is why specs grow.

**"It's only a small feature" ignores five of the six stages.** Small to build says nothing about small to support, and
the smallest features frequently generate the most confusion.

**Removal is assumed to be available.** It is available at a cost that rises with every user who adopts it. Planning as
though features can be withdrawn freely is how products become unchangeable.

**Deprecation is treated as an operational task.** It is a product decision with a communication plan, a migration path
and a timeline — and in institutional markets, possibly a contractual one.

**Usage is never measured, so nothing is ever removed.** `12-metrics` can tell you what nobody uses, but only if the
events were defined. That is why `08-product/knowledge/KPIs.md` records observability per requirement.

---

# Related

| | |
| --- | --- |
| `Future-Scope.md` | What is deliberately left for later |
| `08-product` `Roadmap.md` | The deferral ledger |
| `13-operations` | Support load and true cost to serve |
| `12-metrics` | Where usage becomes visible |

---

> **Concept Note**
>
> Specifying is cheap, building is estimated, and everything after is
> permanent and unmeasured.
>
> Anything deferred can be added later. Anything shipped can only be
> removed.
