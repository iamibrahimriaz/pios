---
Title: Prediction
Module: 14-ai-systems
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Require historical data and confront the base rate before predicting anything.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 14-ai-systems/knowledge/AI-Use-Cases.md
Outputs:
  - Predictive capabilities within model_strategy
Related Modules:
  - 09-technology
  - 12-metrics
Tags:
  - AI
  - Prediction
  - Concept
---

# Prediction

---

# What It Is

Estimating something not yet known — a likelihood, a value, a classification of what will happen.

Two properties make it the hardest capability class for a new product:

**It needs history the product does not have.** Prediction learns from outcomes, and a new product has no outcomes.
`Ground`'s cold-start question applies with full force: the capability is worst exactly when the product is newest.

**The base rate governs usefulness.** For a rare event, a model with respectable accuracy produces mostly false positives:

| If the event occurs in 2% of cases | And the model is 90% accurate |
| --- | --- |
| True positives | 18 per 1,000 |
| False positives | 98 per 1,000 |
| So a positive prediction is right | Roughly 15% of the time |

That is frequently worse than useless, because the user learns to ignore it — the same dynamic `13-operations` describes about tolerated
alerts.

---

# When It Applies

In Move 2 (Compare) and Move 3 (Ground), where the data requirement usually decides it.

---

# How to Apply It Here

**Confirm the historical data exists, with outcomes attached.** Unconfirmed data is a **blocker, not a risk**. Predictions require labeled
outcomes, and most products have neither at launch.

**Compute the base rate before anything else.** If the event is rare, work out what a plausible accuracy actually yields. That arithmetic
frequently ends the proposal, cheaply.

**Compare against the ordering heuristic.** "Sorted by most recently used" or "flagged if over 30 days" are the honest alternatives, and for
many prediction proposals they win. `AI-Use-Cases.md`'s advocate check applies.

**Plan the cold-start path.** A non-AI rule for the first period is a design decision rather than a disappointment, and it is usually what
ships.

**Measure the prediction against the outcome.** `12-metrics` can define it: a prediction whose accuracy is never observed in production is
unfalsifiable, and it will drift silently.

---

# Where It Misleads

**Accuracy is quoted without the base rate.** A 90% accurate rare-event predictor is mostly wrong when it fires, and the headline figure
conceals it entirely.

**Historical data is assumed to be obtainable.** "We will have this once we have users" is a projection, and the framework requires
confirmation. It also means the capability cannot be estimated or scheduled.

**Correlation in training data becomes a decision rule.** In regulated domains a predictor can encode a proxy for something it must not use,
which is a legal exposure as much as a quality one.

**Drift is not monitored.** The world changes, and a model trained on last year's behavior degrades without any error appearing.

**A confidence score is presented to the user as certainty.** `Automation.md`'s detectability rule applies: an unhelpful prediction the user
cannot evaluate is worse than none.

---

# Related

| | |
| --- | --- |
| `Recommendation.md` | The adjacent capability, with the same cold-start problem |
| `Evaluation.md` | The bar, and the cadence that catches drift |
| `AI-Use-Cases.md` | The heuristic alternative |
| `12-metrics` | Observing accuracy in production |

---

> **Concept Note**
>
> Compute the base rate first. For a rare event, respectable accuracy
> produces mostly false positives.
>
> And a predictor needs outcomes it does not have yet — which is a
> blocker, not a risk.
