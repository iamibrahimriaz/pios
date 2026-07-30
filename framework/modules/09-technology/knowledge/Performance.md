---
Title: Performance
Module: 09-technology
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Derive performance targets from what the user has time for, not from convention.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 09-technology/knowledge/Tech-Stack.md
Outputs:
  - Performance requirements within architecture
Related Modules:
  - 03-user
  - 08-product
Tags:
  - Technology
  - Performance
  - Concept
---

# Performance

---

# What It Is

Performance as a **requirement with a number**, derived from the situation rather than from an industry figure.

`08-product` banned the word "fast" from acceptance criteria and required a figure instead. This file is about where that
figure comes from:

| Source of the number | Example |
| --- | --- |
| The user's available time | A consultation has ten minutes; the capture step may take three seconds, not thirty |
| The step's position in the flow | An interactive step needs a different budget from an overnight one |
| What the user does while waiting | If they can continue, latency matters less; if they must wait, it dominates |
| The status quo's speed | `04-problem`'s baseline — being slower than the spreadsheet is fatal |

For AI features the budget is frequently the binding constraint: model latency may exceed what the interaction allows,
which is a `14-ai-systems` finding rather than an optimization problem.

---

# When It Applies

Alongside Move 5 (Choose) and Move 6 (Size). `scalability/Performance.md` covers behavior under load; this covers the
target itself.

---

# How to Apply It Here

**Take the number from `03-user`'s observed conditions.** How long the user actually has is a fact from the research. Any
other figure is a convention borrowed from a different product.

**State it per operation, not globally.** One target for the whole system means the interactive paths and the batch paths
are held to the same wrong number.

**Say what happens when the budget is exceeded.** A timeout, a partial result, a queued job with a notification. That is a
`08-product` edge case — the failure category — and it needs a specified behavior.

**Check the AI path separately.** If inference latency exceeds the interaction budget, the options are a different
interaction — draft in the background, present later — or a different mechanism. Both are decisions, not tuning.

**Measure percentiles, not averages.** The average hides the experience of the users who are having the worst one, and they
are the ones who abandon.

---

# Where It Misleads

**Targets are borrowed from consumer web conventions.** A professional tool used forty times a day has a different budget
from a page visited once, in both directions.

**Performance work begins before there is a measurement.** Move 6 requires naming the first bottleneck. Optimizing anything
else is effort spent where the constraint is not.

**Latency is optimized while the total task time is ignored.** A fast step in a flow that still takes the user twenty
minutes has not helped. `03-user`'s journey holds the number that matters.

**Slow-by-design is not distinguished from slow-by-defect.** An overnight batch is a design; a report that times out is a
defect. Conflating them produces optimization of the wrong one.

**The perceived-speed option is skipped.** Acknowledging an action immediately and completing it in the background is
frequently the correct answer, and it is a behavior decision `08-product` should have specified.

---

# Related

| | |
| --- | --- |
| `scalability/Performance.md` | Behavior under load, and degradation |
| `08-product` | Where the figure becomes an acceptance criterion |
| `03-user` | The time actually available |
| `14-ai-systems` | Where inference latency becomes a constraint |

---

> **Concept Note**
>
> The number comes from how much time the user has, and nowhere
> else.
>
> If inference takes longer than the interaction allows, that is a
> mechanism decision — not something to tune.
