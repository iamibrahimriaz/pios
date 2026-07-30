---
Title: Questions To Answer
Module: 12-metrics
Section: core
Category: Inquiry
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The complete question set this module must answer before its gate can pass.
Audience:
  - AI Agents
  - Product Managers
Prerequisites:
  - 12-metrics/core/06-Framework.md
Outputs:
  - Answered question set
Related Modules:
  - 13-operations
Tags:
  - Metrics
  - Questions
---

# Questions To Answer

---

# Overview

Most questions here are **decisions**, not research. A metric definition is chosen, not
discovered — which means these questions can all be answered, and answered precisely.

The targets are the exception. For a product with no users they are assumptions, and the questions
about them exist mainly to keep that visible.

Questions marked **OPERATOR** cannot be inferred.

---

# 1. Inherited Inputs

| # | Question | If unanswered |
| --- | --- | --- |
| 1.1 | What are the goals in `08-product` §6? | Goals go unmeasured — a gate failure |
| 1.2 | What is the activation event from `11-growth`? | Two documents define value differently |
| 1.3 | What retention mechanism was identified? | "Returning" has no meaning |
| 1.4 | Which columns are PII or regulated, from `09-technology` §3? | Regulated data reaches an analytics vendor |
| 1.5 | What are the decision points in `10-execution` §9? | A decision point with no metric cannot decide |
| 1.6 | What unit of value is the price attached to, from `06-business`? | The product is measured away from its business model |
| 1.7 | Does a baseline exist for anything? | Targets get invented and treated as derived |

---

# 2. The North Star

| # | Question | If unanswered |
| --- | --- | --- |
| 2.1 | What one number represents value delivered to the user? | Every team optimizes something different |
| 2.2 | Why this one? | Cannot be re-examined later |
| 2.3 | What are two alternatives, and why would each mislead? | The obvious wrong choice is never ruled out |
| 2.4 | **Could this number fall if the product got worse?** | It is a cumulative count and will always rise |
| 2.5 | **What would make it rise without the product improving?** | The counter-metrics have no basis |
| 2.6 | Is it a user outcome or a company convenience? | Revenue chosen, which moves last and steers nothing |
| 2.7 | How often is it reviewed, and by whom? | A metric nobody looks at |

> 2.4 and 2.5 are mechanical and they catch the two most common north star failures. Neither takes
> longer than a minute to answer.

---

# 3. Definitions

Asked of every metric.

| # | Question | If unanswered |
| --- | --- | --- |
| 3.1 | What exactly is the numerator? | Nobody knows what is counted |
| 3.2 | What exactly is the denominator? | A count passes as a rate |
| 3.3 | What is the time window, rolling or calendar? | Two teams report different numbers |
| 3.4 | Which users are in the population? | Trials and churned accounts shift the figure |
| 3.5 | What is excluded? | Test data inflates every early number |
| 3.6 | Which events is it computed from? | Uncomputable |
| 3.7 | **Would two analysts produce the same number from this?** | The definition is a description |
| 3.8 | Does every goal in `08-product` §6 have a metric? | A goal that was never a goal |
| 3.9 | Are there goals that cannot be measured? | Quietly dropped instead of recorded |

---

# 4. Leading and Lagging

| # | Question | If unanswered |
| --- | --- | --- |
| 4.1 | Which metrics move first? | Nothing to steer by |
| 4.2 | For each leading indicator: which lagging metric does it predict? | A number that moves and means nothing |
| 4.3 | What is the basis for believing the link exists? | An assumed correlation acted on as fact |
| 4.4 | How far ahead does it move? | The warning arrives with the confirmation |
| 4.5 | What is the warning threshold? | Nobody knows when to act |
| 4.6 | Which metrics only confirm? | Late metrics treated as steering instruments |
| 4.7 | Who sees each lagging metric, and when? | Reported to nobody |

---

# 5. Activation and Retention

| # | Question | If unanswered |
| --- | --- | --- |
| 5.1 | How is activation computed — numerator, denominator, window? | The rate is not comparable between weeks |
| 5.2 | What target activation rate, and on what basis? | No bar |
| 5.3 | How are cohorts defined? | Retention is uncomputable |
| 5.4 | At what point is retention measured? | Every report uses a different day |
| 5.5 | **What action counts as "returning"?** | A login counts, and abandonment looks like health |
| 5.6 | What is the early warning behavior? | Churn observed only after it happens |
| 5.7 | Which retention mechanism is being measured? | The metric does not test the mechanism |

---

# 6. Counter-Metrics

| # | Question | If unanswered |
| --- | --- | --- |
| 6.1 | What must not get worse while the primary metrics improve? | The product degrades in good faith |
| 6.2 | What threshold, for each? | A guard with no line |
| 6.3 | What does each protect against? | The threshold gets relaxed when inconvenient |
| 6.4 | Which non-negotiables from `09-technology` are observable here? | A security rule with no visibility |
| 6.5 | Who is alerted when one is breached? | Observed and ignored |

---

# 7. Targets

| # | Question | If unanswered |
| --- | --- | --- |
| 7.1 | Is there a baseline for anything? | Invented figures pass as derived |
| 7.2 | For each target: what is the basis? | Numbers acquire authority by repetition |
| 7.3 | **Could each target be missed by a real result?** | It is a statement, not a target |
| 7.4 | Which targets are guesses? | They are not in the assumption register |
| 7.5 | Which milestone produces the first real baseline? | The weakness has no closing plan |
| 7.6 | **OPERATOR** — what would count as success to you? | The framework's targets replace the operator's |
| 7.7 | **OPERATOR** — what result would make you stop? | The stop condition has no number |

---

# 8. Instrumentation

| # | Question | If unanswered |
| --- | --- | --- |
| 8.1 | Which events must exist? | Nothing is measurable |
| 8.2 | For each: what is the precise trigger? | Fires inconsistently, and the metric drifts |
| 8.3 | For each: what properties, with what types? | The metric cannot be segmented |
| 8.4 | For each: which metric does it feed? | Orphan event — cost and liability |
| 8.5 | For each: which milestone ships it? | Nobody is building it |
| 8.6 | **Does any metric lack an event?** | It will be replaced by whatever is available |
| 8.7 | How is a user identified across sessions? | Cohorts uncomputable |
| 8.8 | Across devices? | Retention undercounted, silently |
| 8.9 | Before signup? | The funnel starts after the interesting part |
| 8.10 | **What must never be captured, and how is that enforced?** | Regulated data in a third-party system |
| 8.11 | **Does any regulated column appear as an event property?** | A compliance exposure, not a data-quality issue |
| 8.12 | How long is event data retained? | Retention obligation breached by the analytics tool |

> 8.11 is the question in this module with legal consequences. It is answered by listing the
> regulated columns and checking each against every property — mechanically, not by judgment.

---

# 9. Infrastructure and Review

| # | Question | If unanswered |
| --- | --- | --- |
| 9.1 | What tool, and how do events reach it? | A plan with no pipeline |
| 9.2 | Where does the team see this? | Metrics exist and are never looked at |
| 9.3 | What does measurement cost? | An unbudgeted line, sometimes a large one |
| 9.4 | Does that cost fit `09-technology`'s cost model? | The cost ceiling breached by analytics |
| 9.5 | Who reviews, how often? | Nobody owns the numbers |
| 9.6 | When should the metrics themselves be reconsidered? | Launch metrics used at a scale they do not fit |

---

# Question Coverage

| Section | Feeds |
| --- | --- |
| 1 | §2 header inputs |
| 2 | §2 North Star |
| 3 | §2, §3 definitions and goal metrics |
| 4 | §4, §5 leading and lagging |
| 5 | §6 Activation and Retention |
| 6 | §7 Counter-Metrics |
| 7 | §11 Baselines and Targets |
| 8 | §8 Instrumentation |
| 9 | §9, §10, §12 Infrastructure, reporting, review triggers |

---

# Self Assessment

- Did I answer 2.4 and 2.5 in writing?
- Could two analysts answer 3.7 identically for every metric?
- Does every goal in 3.8 have a metric?
- Is 4.3 answered with a basis, or an assumption presented as one?
- Is 5.5 an action rather than a login?
- Did 6.1 come from 2.5?
- Could every target in 7.3 be missed?
- Did I ask the operator 7.6 and 7.7?
- Did I check 8.11 mechanically?

---

> **Question Principle**
>
> Almost every question here has a decidable answer, which makes
> vagueness a choice rather than a limitation.
>
> The exception is the targets — and the honest answer there is
> to say they are guesses and name what will replace them.
