---
Title: Success Metrics
Module: 08-product
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Tie each requirement to the outcome it is meant to change, and keep targets out.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 08-product/knowledge/KPIs.md
Outputs:
  - Outcome mapping within prd_body
Related Modules:
  - 04-problem
  - 12-metrics
Tags:
  - Product
  - Metrics
  - Concept
---

# Success Metrics

---

# What It Is

The mapping from requirement to **outcome** — what would be different for the user if this shipped and worked.

The outcome is not new information. `04-problem` established the cost per occurrence, and `06-business` established
what share the product claims to remove. This module's contribution is connecting individual requirements to that
chain:

```
ranked problem  →  its cost per occurrence  →  requirement  →  the outcome that should change
```

That chain is what makes success checkable. Without it, a shipped release can be assessed only on whether the
requirements were built — which is a statement about the team rather than about the product.

---

# When It Applies

Alongside Move 1 (Trace) and Move 3 (Behave). The spine already names the parent problem; the outcome is the other end
of the same link.

---

# How to Apply It Here

**Write the outcome in the user's terms.** "Leaves the clinic on time" rather than "documentation efficiency
improved". `03-user`'s language is the source, and it is what `12-metrics` will need to measure something people
recognize.

**Attach the baseline from `04-problem`, with its tag.** The cost per occurrence is the figure any improvement is
measured against. If it was `[assumption]`, the outcome claim inherits that standing.

**Say which requirements share an outcome.** Several requirements frequently serve one outcome, and that grouping tells
`12-metrics` not to build four metrics where one belongs.

**Flag where the outcome depends on something outside the product.** If leaving on time also requires a rota change,
the product cannot deliver the outcome alone. That is honest and it prevents `12-metrics` measuring the product against
something it does not control.

**Leave the target to module 12.** `01-idea` set this rule and it holds here: name what would be looked at, not the
number it should reach.

---

# Where It Misleads

**Output gets recorded as outcome.** "Notes are generated automatically" is what the product does. "Notes are complete
before the patient leaves" is what changes for the user, and only the second can fail in an informative way.

**Every requirement is given its own outcome.** Most requirements are supporting work — validation, permissions, error
handling. Forcing an outcome onto each produces a list of invented benefits.

**The outcome is stated where the mechanism is uncertain.** For AI capabilities, whether the outcome arrives depends on
output quality. `14-ai-systems` sets acceptance criteria for that, and the outcome claim should reference the
dependency.

**A target written here becomes the commitment.** It has no baseline, no population and no window, and it will
nonetheless be quoted. That is why the boundary is strict.

**Success is defined as shipping.** A release that built everything and changed nothing is a completed project and a
failed product. The outcome mapping is what makes the difference visible.

---

# Related

| | |
| --- | --- |
| `KPIs.md` | The observable behavior side of the same boundary |
| `features/Acceptance-Criteria.md` | Whether the requirement works, as distinct from whether it helps |
| `04-problem` | The cost per occurrence, and its tag |
| `12-metrics` | Definitions, targets and counter-metrics |

---

> **Concept Note**
>
> Output is what the product does. Outcome is what changes for the
> person.
>
> A release that shipped everything and changed nothing passed every
> acceptance criterion it had.
