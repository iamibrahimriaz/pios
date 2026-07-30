---
Title: Best Practices
Module: 12-metrics
Section: core
Category: Practice
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: What experienced product people do when defining metrics that inexperienced ones do not.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 12-metrics/core/06-Framework.md
Outputs:
  - Higher-quality metrics plans
Related Modules:
  - 13-operations
Tags:
  - Metrics
  - Best Practices
---

# Best Practices

---

# 1. Start From the Unit of Value the Price Is Attached To

`06-business` established what the customer is paying for. The north star measures that unit.

A product priced on one unit and measured on another gets optimized away from its own business
model, gradually, with no single decision to point at.

---

# 2. Write the Rejected Alternatives First

Name the two obvious candidates and why each would mislead, then name the choice.

Written afterwards, the rejections are shaped to flatter a decision already made — and the reasons
are the part that makes the choice reviewable in a year.

---

# 3. Ask the Falling Question Out Loud

"Could this number go down if the product got worse?"

Five seconds, and it eliminates the entire class of cumulative metrics that dominate reporting.

---

# 4. Write the Gaming Answer Next to the Metric, Not in a Later Section

For each metric, one line: what would raise this without the product improving.

Written beside the metric, it becomes the counter-metric immediately. Deferred to a "risks" section,
it becomes prose.

---

# 5. Write the Five Parts as a Block, Every Time

Numerator, denominator, window, population, exclusions. As a block, not a sentence.

A sentence lets parts go missing without looking incomplete. A block with an empty row does not.

---

# 6. Name the Exclusions Before Launch, Not After the First Odd Number

Internal accounts, test practices, the founder's own usage.

Named later, the metric appears to decline when they are removed — and the correction is
indistinguishable from a real decline in the same week.

---

# 7. State the Time Window as Rolling or Calendar, Explicitly

Rolling seven days and calendar week differ by more than most metrics move in a quarter.

Two teams choosing differently produce a permanent disagreement that gets explained as seasonality.

---

# 8. Define "Returning" as a Qualifying Action

Not a login, not a session. The action they came to perform.

This one decision determines whether the retention number can be trusted, and it is usually made by
whoever writes the query.

---

# 9. Write the Basis for Every Leading Indicator's Link

"«Metric» predicts «metric» `[inferred: reasoning]`".

An indicator with no basis still gets acted on, because it moves early and that is what people want
from a number.

---

# 10. Say Whether You Know the Lead Time

If an indicator moves one day before the metric it predicts, it is not an early warning, and the
only time anyone finds out is when they needed it to be.

---

# 11. Give Every Counter-Metric a Threshold and a Purpose

The threshold makes it actionable. The purpose is what stops it being relaxed the first time it is
inconvenient.

---

# 12. Say "There Is No Baseline" in Those Words

Then tag every target as an assumption with its basis.

The sentence costs nothing and it stops a room full of people treating a guess as a projection three
months later.

---

# 13. Ask the Operator What Success Looks Like, and What Would Make Them Stop

Two questions. The first gives the targets an owner; the second gives the stop conditions a number.

Without them, the framework's targets replace the operator's — which is a decision nobody made.

---

# 14. Describe the Result That Would Fail Each Target

One clause per target. If no plausible result would fail it, the target is a statement of intent.

---

# 15. Write the Events Immediately After Each Metric

Metric, then the events it needs, in the same pass.

Written as a separate exercise later, the event list covers the metrics that are easy to instrument
rather than the ones that matter.

---

# 16. Assign Every Event to a Milestone

That is what places it in a definition of done in `10-execution`, and it is the only mechanism that
gets instrumentation shipped with the feature.

An event with no milestone is a good intention in a document.

---

# 17. Specify Identity Before Specifying Cohorts

Across sessions, across devices, before signup.

Every cohort and retention metric depends on it, and it is the section most often left out — usually
discovered when the first retention chart looks impossibly bad.

---

# 18. List the Regulated Columns, Then Check Every Property Against Them

Mechanically. Copy the list from `09-technology` §3 and check each event property for membership.

Do not read for it — check. A property name that looks harmless can carry regulated content, and the
exposure is invisible once the events are live.

---

# 19. Cost the Measurement

Event volume, retention period, tooling tier.

It is a real line, occasionally a large one, and it is routinely absent from a cost model that was
otherwise carefully checked.

---

# 20. State Two Confidences

One for the definitions, one for the targets.

Definitions are decisions and can be certain. Targets for a product with no users cannot be, and a
single figure always reports the definition's.

---

# Anti-Practices

| Habit | Why it fails |
| --- | --- |
| North star chosen before consulting the price | The product drifts from its business model |
| Rejections written after the choice | Shaped to flatter it |
| Skipping the falling question | Cumulative metrics survive |
| Gaming answers in a separate section | They become prose, not counter-metrics |
| Definitions written as sentences | Parts go missing without looking incomplete |
| Exclusions added after the first odd number | The correction looks like a decline |
| Window left implicit | Permanent disagreement, explained as seasonality |
| "Returning" as a login | Abandonment looks like health |
| Leading indicator links asserted | Acted on early and confidently |
| Counter-metrics without thresholds | Nothing to breach |
| Baseline absence left unstated | A guess becomes a projection |
| Targets set without the operator | The framework decides what success means |
| Events specified as a later exercise | Only the easy metrics get instrumented |
| Events with no milestone | Nobody builds them |
| Cohorts before identity | The retention chart is wrong and nobody knows why |
| Reading for regulated properties | A harmless-looking name carries protected content |
| Measurement cost omitted | A checked cost model, breached |
| One confidence figure | The targets inherit the definitions' certainty |

---

# Self Assessment

- Does the north star measure the priced unit of value?
- Did I write the rejections first?
- Did I ask the falling question of every metric?
- Is every gaming answer next to its metric?
- Are all five definition parts present as a block?
- Are exclusions named now, not later?
- Is every window explicitly rolling or calendar?
- Is "returning" a qualifying action?
- Does every leading indicator state its basis and lead time?
- Does every counter-metric have a threshold and a purpose?
- Did I write "there is no baseline"?
- Did I ask the operator both questions?
- Can every target be failed by a describable result?
- Are events written beside their metrics?
- Does every event have a milestone?
- Is identity specified before cohorts?
- Did I check every property against the regulated list?
- Is measurement costed?
- Did I state two confidences?

---

> **Practice Principle**
>
> Three practices here take under a minute each: the falling question,
> the gaming line, and checking properties against the regulated list.
>
> They catch a vanity metric, a degrading product, and a compliance
> exposure — none of which are visible on a careful read.
