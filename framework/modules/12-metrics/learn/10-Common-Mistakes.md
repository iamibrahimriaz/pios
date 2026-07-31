---
Title: Common Mistakes
Module: 12-metrics
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Name the recurring failures in measurement design and what each costs.
Audience:
  - Product Managers
  - Founders
  - Analysts
Prerequisites:
  - 12-metrics/learn/01-Why-It-Matters.md
Outputs:
  - Recognition of measurement failure patterns
Related Modules:
  - 09-technology
  - 11-growth
Tags:
  - Metrics
  - Mistakes
  - Learn
---

# Common Mistakes

---

# Overview

Measurement mistakes are unusually durable. A badly chosen metric outlives the person who
chose it, the strategy that justified it, and the product it was measuring.

---

# 1. The Metric That Cannot Be Computed

**What it looks like.** "Percentage of outputs the user accepted without editing."

**Why it is tempting.** It is exactly the right thing to measure.

**What it costs.** It requires per-item edit capture, which is a product requirement
rather than an analytics setting. Discovered at launch, the fix is a release. Discovered
here, it is a line in module 08's specification.

**Instead.** Trace every metric to the fields module 09's data model actually contains.
Where a field is missing, decide now whether to add it or to change the metric.

---

# 2. Vanity Metrics on the Main Chart

**What it looks like.** Cumulative registrations, total events processed, page views.

**Why it is tempting.** They rise. They are easy to compute. They look like progress and
nobody has to explain a decline.

**What it costs.** They rise during quarters in which nothing improved, which means they
cannot inform a decision — and they occupy the position where a metric that could inform
one should be.

**Instead.** Apply the vanity check: describe a week where this improved and the business
did not. If that week is easy to describe, move the metric off the main chart.

---

# 3. The Metric Nobody Gamed On Purpose

**What it looks like.** A team improving a number through behavior that damages the
product, entirely in good faith.

**Why it is tempting.** The metric was chosen for its meaning, not for its incentive, and
gaming is imagined as something dishonest people do.

**What it costs.** Most metric gaming is honest. People are told a number matters and they
move it — by shortening notes, by closing tickets faster, by prompting more often. The
damage arrives as a side effect of exactly the behavior that was asked for.

**Instead.** Ask the gaming question before adopting the metric, and prefer metrics whose
gamed behavior is roughly what you wanted anyway.

---

# 4. Two Metrics of Equal Standing

**What it looks like.** A north star and a "quality counterweight," both described as
primary.

**Why it is tempting.** It looks balanced and it avoids a difficult decision.

**What it costs.** Every conflict becomes a debate, and the winner is whoever is most
persuasive that week. The organization's real priority becomes unstable and unrecorded.

**Instead.** One north star, with the others as guardrails that have thresholds rather
than as equals. A guardrail is a floor, not a competing objective.

---

# 5. Definitions Left to the Implementer

**What it looks like.** "Weekly active users," with no further specification.

**Why it is tempting.** Everyone knows what it means.

**What it costs.** Nobody knows what it means. Rolling or calendar week, opened or
completed, all accounts or excluding internal — five reasonable people produce five
different numbers, all correct.

**Instead.** Population, event, window, exclusions, and when it is computed. Five lines,
written once.

---

# 6. Everything Lagging

**What it looks like.** A dashboard of retention, revenue and churn.

**Why it is tempting.** These are the numbers that matter, and they are the ones asked
about.

**What it costs.** They all report the past. A team steering by them responds to causes a
quarter after they occurred, and cannot tell whether a change made this week helped.

**Instead.** At least one leading indicator: something observable in the first session
that correlates with the lagging outcome. Finding it requires a hypothesis and is worth
the effort.

---

# 7. Regulated Fields in Event Properties

**What it looks like.** An analytics event carrying a name, an email, a record
identifier, or free text.

**Why it is tempting.** It makes debugging easy, and analytics feels like an internal
tool rather than a data export.

**What it costs.** An analytics pipeline is a transfer to a third party, often in another
jurisdiction, with a retention policy nobody chose. This is the same class of exposure as
sending a regulated field to a model provider, and it is the check this module owes the
obligation chain.

**Instead.** Check every property against module 09's regulated column list. Identifiers
should be opaque and the free text should not be there at all.

---

# 8. Targets From Ambition

**What it looks like.** "20% month-on-month growth."

**Why it is tempting.** It is motivating and round.

**What it costs.** A target unconnected to the business model tells you nothing when you
miss it. Was the plan wrong, or the execution? A target derived from module 06 — what has
to be true for the model to work — answers that immediately.

**Instead.** Derive targets. If the derived number is uninspiring, that is information
about the business rather than a reason for a better-sounding target.

---

# The Pattern

| Mistake | Underlying move |
| --- | --- |
| Uncomputable metric | Choosing meaning without checking feasibility |
| Vanity on the main chart | Preferring a number that only rises |
| Unasked gaming question | Choosing for meaning, not for incentive |
| Two primaries | Avoiding a decision |
| Definitions deferred | Assuming shared understanding |
| All lagging | Measuring what is asked about |
| Regulated fields in events | Treating analytics as internal |
| Targets from ambition | Choosing a number that motivates |

Half of these are the same move: **selecting a metric for what it means rather than for
what it does.** A metric is an instruction, and its meaning is the least predictive thing
about its effect.

---

> **Mistakes Principle**
>
> Metrics outlive their reasons.
>
> Whatever is on the main chart will still be there when the strategy that chose it has
> been replaced twice — which is why the gaming question is worth an hour now.
