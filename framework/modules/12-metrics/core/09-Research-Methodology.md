---
Title: Research Methodology
Module: 12-metrics
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define how metric definitions and targets are sourced, labeled and bounded.
Audience:
  - AI Agents
Prerequisites:
  - engine/evidence-policy.md
  - 12-metrics/core/06-Framework.md
Outputs:
  - Honestly bounded metrics plan
Related Modules:
  - 13-operations
Tags:
  - Metrics
  - Methodology
  - Evidence
---

# Research Methodology

---

# Definitions Are Decisions. Targets Are Not.

This module contains two kinds of statement with completely different evidential standing, and
conflating them is its characteristic error.

| | Nature | Standing |
| --- | --- | --- |
| **Definition** | A decision about what to count | Can be high-confidence — it is chosen |
| **Target** | A prediction about behavior | Cannot be, for a product with no users |

A metrics plan can therefore be simultaneously **precise and unproven**, and saying so is the
honest position:

> Confidence in these definitions: high. Confidence in these targets: low — there is no baseline,
> and every figure is an assumption with a stated basis.

Most metrics documents state one confidence for both, and it is always the definition's.

---

# The Computation Test

A definition is finished when it can be executed by someone who did not write it.

> Given only this definition, would two analysts produce the same number?

Five parts, and each has a specific failure when omitted:

| Part | Omitted |
| --- | --- |
| Numerator | Nobody knows what is being counted |
| Denominator | A count is reported as a rate |
| Time window | Rolling seven days and calendar month differ by more than the metric moves |
| Population | Trials, internal users and churned accounts each change the answer |
| Exclusions | Test data inflates every early figure, then disappears and looks like decline |

"Active users" fails all five and is the most widely reported metric in software.

---

# Targets Without Baselines

For a new product there is no baseline. This is a fact about the situation, not a gap to fill.

| Source of a target | Handling |
| --- | --- |
| A real baseline | State it and its source |
| A comparable product | Cite it, and state that the population differs |
| The operator | Attribute it to them — `[verified: operator]` |
| Nothing | `[assumption: needs validation]`, with the basis stated |

**Do not import industry benchmarks as targets.** A published median activation or retention rate
describes a population this product is not in, measured with definitions nobody discloses. It can
inform a range. It cannot support a bar.

**Name the milestone that produces the first real baseline.** That converts an admitted weakness
into a plan, and it is the same move `04-problem`'s declared shortfall makes: state the position,
then say what closes it.

---

# The Two Mechanical Checks

Both take under a minute and both catch failures that survive careful review.

## The Vanity Check

> Could this number fall if the product got worse?

| Cannot fall | Can fall |
| --- | --- |
| Total registered users | Weekly active users completing the core job |
| Cumulative notes created | Notes per active user per week |
| Total revenue to date | Monthly recurring revenue |

A number that only rises measures elapsed time. It is not that cumulative counts are never
useful — it is that they cannot be steered by, because no decision changes their direction.

## The Gaming Question

> What would someone do to make this rise without the product becoming more valuable?

Every metric has an answer, and the answer is not hypothetical: organizations reliably find it.

| Metric | Degenerate behavior |
| --- | --- |
| Notes saved per week | Many short fragmentary notes |
| Consultations completed | Rushing consultations |
| Sessions per user | Notifications that fragment one session into four |
| Time in product | Making things slower to find |

This is Goodhart's problem stated concretely, and the answers become the counter-metrics. Skipping
it is how a team optimizes a product into a worse one with every individual decision looking
defensible.

---

# Leading Indicator Links Are Inferences

A leading indicator's claim is causal: *this moves, therefore that will follow*.

Before launch, that claim has no data behind it. It is `[inferred]`, and the basis must be stated:

| Weak | Acceptable |
| --- | --- |
| "Notes per week predicts retention" | "Notes per week predicts retention `[inferred: 04-problem found the workaround is abandoned once a habit forms; frequency is the closest proxy for habit]`" |

An indicator whose link cannot be articulated is a number that moves and means nothing — and it
will be acted on anyway, because it moves early and that is what people want.

State the **lead time** or say it is unknown. An indicator that moves one day before the lagging
metric is not an early warning.

---

# Instrumentation Is Not Research — It Is a Build Instruction

§8 of the output is different in kind from everything else in this module. It is not a description
of what will be measured; it is a specification of what must be written.

| Requirement | Because |
| --- | --- |
| Precise trigger | An event that fires inconsistently produces a metric that drifts |
| Every property, with type | An untyped property cannot be segmented or validated |
| The metric it feeds | An orphan event is cost, noise and a privacy liability |
| The milestone it ships in | An event with no milestone is one nobody is building |

**Coverage runs both directions** — the same discipline as modules 08 and 09:

| Direction | Failure |
| --- | --- |
| Metric → event | Uncomputable. It will be silently replaced by whatever is available |
| Event → metric | Logged forever, used never |

**Identity resolution is part of the specification.** Across sessions, across devices, before
signup. Omitted, every cohort and retention metric is uncomputable — and it is the most commonly
omitted section of an instrumentation plan.

---

# Privacy Exclusions Are a Compliance Matter

An event property is data leaving the system.

> A regulated column appearing as an event property means regulated data is now in a third-party
> system with different retention, different access control, and possibly a different
> jurisdiction.

This is not a data-quality question. The check is mechanical:

```
List regulated and PII columns from 09-technology §3
For each event property, check membership in that list
  ├─ any overlap → remove it, or the gate fails
  └─ none        → record "none — verified"
```

**What must be stated**

| | |
| --- | --- |
| What must never be captured | From `02-market` and `09-technology` |
| The regime or reason | Cited |
| The enforcement mechanism | A property allowlist, a redaction layer — something specific |
| Event data retention | The period, and the obligation it satisfies |

"We will be careful with PII" is the same class of statement as "the system will be compliant",
which `09-technology` prohibits for the same reason.

---

# The Prohibitions

| Never | Why |
| --- | --- |
| State one confidence for definitions and targets | They differ by kind, not degree |
| Import an industry benchmark as a target | Different population, undisclosed definitions |
| Present a target as derived | It is a prediction about behavior nobody has observed |
| Report a cumulative count as a primary metric | It measures elapsed time |
| Define a metric without all five computation parts | It is a description |
| Assert a leading indicator link without a basis | An inference acted on as a finding |
| Define "returning" as a login | Abandonment looks like health |
| Specify an event with no metric | Cost, noise and liability |
| Specify a metric with no event | Uncomputable, and quietly substituted |
| Put a regulated column in an event property | A compliance exposure |
| Say "we will be careful with PII" | Not a mechanism |
| Set a target that cannot be missed | Not a target |

---

# Cross-Checks Before the Gate

| Check | Against | Fails when |
| --- | --- | --- |
| Goal coverage | `08-product` §6 | A PRD goal has no metric |
| Activation | `11-growth` | The event differs from the one defined there |
| Time to activate | `10-execution` §5 | The target contradicts time to first value |
| Retention | `11-growth` §6 | The metric does not measure the identified mechanism |
| Value alignment | `06-business` | The north star measures a different unit than the price is attached to |
| Decision points | `10-execution` §9 | A decision point has no metric that can answer it |
| Privacy | `09-technology` §3, `02-market` | A regulated column appears as a property |
| Cost | `09-technology` §12 | Measurement cost breaches the ceiling |
| Milestones | `10-execution` §7 | An event is assigned to no milestone |

---

# Self Assessment

- Did I state confidence separately for definitions and targets?
- Could two analysts compute every metric identically?
- Is any target an imported benchmark?
- Could every one of my metrics fall if the product got worse?
- Did I write down how each would be gamed?
- Does every leading indicator state the basis for its link?
- Is "returning" an action?
- Does every event feed a metric, and every metric have events?
- Did I check every property against the regulated column list?
- Is every event assigned to a milestone?

---

> **Methodology Principle**
>
> This module can be exact about what it will count and honest
> about not knowing how much there will be.
>
> Documents that blur the two produce precise-looking forecasts,
> which is the least useful thing a metrics plan can be.
