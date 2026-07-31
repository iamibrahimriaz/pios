---
Title: Why It Matters
Module: 12-metrics
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Explain why a metric is an instruction and why definition matters more than selection.
Audience:
  - Product Managers
  - Founders
  - Analysts
Prerequisites:
  - 12-metrics/core/00-Purpose.md
Outputs:
  - Understanding of why the metrics stage exists
Related Modules:
  - 08-product
  - 09-technology
  - 11-growth
Tags:
  - Metrics
  - Instrumentation
  - Learn
---

# Why It Matters

---

# Overview

Metrics get treated as a reporting concern — the thing you set up so you can see how it
is going. They are better understood as the most durable instruction a product team ever
writes, because people optimize what is measured long after they have forgotten why it
was chosen.

---

# Why Exactly One North Star

The gate permits one. Not a balanced scorecard, not three primary metrics.

The reason is behavioral rather than analytical. Two metrics of equal standing produce a
tie-breaking conversation every time they conflict, and they conflict constantly —
activation against quality, volume against retention, speed against accuracy. Whoever is
most persuasive in the room wins those conversations, which means the real priority is a
function of who is present.

One north star settles it in advance. The other metrics still exist, as success metrics
and leading indicators; they simply do not have equal standing.

The requirement to state the reasoning matters as much as the count. A north star with no
recorded justification becomes a habit within two quarters, and habits survive the
conditions that produced them.

---

# Why Definition Is the Real Work

Choosing "weekly active users" takes a minute. Defining it takes an afternoon and decides
everything:

| Question | Consequence |
| --- | --- |
| What counts as active? | Opening the app, or completing the core action |
| Which week? | Rolling seven days, or calendar week |
| Who counts? | All accounts, or excluding internal and trial |
| What about a user with two accounts? | Deduplicated, or not |
| When is it computed? | And what happens to late-arriving events |

Two teams using the same metric name with different answers produce different numbers
and do not know it. That is not a measurement problem — it is a decision problem, because
each of those answers encodes a view about what the product is for.

---

# The Computation Test

> Can this metric be computed from data that will actually exist?

This is the cheapest test in the module and the one most often skipped, because it
requires knowing what module 09's data model records and what module 10's build handoff
will instrument.

Metrics that fail it look identical to metrics that pass. "Percentage of notes the
clinician did not need to correct" is a fine metric and requires that edits are captured
per note, which is a product requirement — not an analytics configuration.

Failing this test is how a metric set arrives at launch unmeasurable, and the fix at that
point is a release rather than a query.

---

# The Vanity Check

> Does this number go up when nothing good has happened?

Registered accounts rise when people sign up and never return. Page views rise when the
navigation is confusing. Total events rise with anything. Cumulative anything only ever
goes up, which is precisely why cumulative charts are so popular in board decks.

The test is a thought experiment: describe a week where this metric improved and the
business did not. If the description is easy, the metric is vanity.

---

# The Gaming Question

> If someone optimized this without caring about the outcome, what would they do?

Every metric can be gamed. The useful question is what the gamed behavior looks like:

| Metric | Gamed by | Harmful? |
| --- | --- | --- |
| Notes created | Encouraging more, shorter notes | Yes — it degrades the record |
| Time in app | Making things slower to find | Yes |
| Notes reaching the record without correction | Making the model more conservative | Partially — the failure mode is benign |
| Support tickets closed | Closing without resolving | Yes |

A metric whose gamed behavior is roughly what you wanted anyway is a well-chosen metric.
That is the actual selection criterion, and it is rarely applied.

---

# Why Instrumentation Belongs Here

The gate requires instrumentation specified at event level for the build handoff. It is
in this module rather than in module 10 because the events follow from the metrics, and
specifying them late means specifying them from the built product rather than from the
decisions.

It also puts this module in the path of the **regulated column list**. Every event
property is checked against module 09's list, because an analytics pipeline is a data
export — usually to a third party, often in another jurisdiction, frequently with a
retention policy nobody chose.

That check is the third of four places the list is used, and it is the one people are
most surprised to be asked about.

---

# Why Leading and Lagging Must Be Distinguished

A lagging indicator tells you what happened. A leading one tells you early enough to act.
Retention is lagging by definition — you cannot know it until time has passed. Something
observable in the first session that correlates with retention is leading, and it is the
only kind you can steer by.

Confusing the two produces a dashboard where every number is a report on the past, and a
team that responds to results a quarter after the cause.

---

# What Skipping This Stage Costs

| Skipped | Surfaces as |
| --- | --- |
| One north star | Priority determined by whoever argues best that week |
| Precise definitions | Two teams disagreeing about a number they both computed correctly |
| The computation test | A metric set that cannot be measured until a release ships |
| The vanity check | Charts that go up during a quarter nothing improved |
| The gaming question | Behavior that optimizes the number and damages the product |
| The regulated-field check | Personal data in a third-party analytics pipeline |

---

# What This Module Does Not Do

It does not set targets in isolation — they derive from module 06's model and module 11's
plan. It does not decide what the product does. It does not measure anything; it specifies
what will be measured and how.

---

> **Why It Matters Principle**
>
> Whatever you measure becomes what people do, long after anyone remembers deciding it.
>
> That is why this module cares more about definition, computability and gaming than
> about which metric you choose.
