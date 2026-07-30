---
Title: Recommendation
Module: 14-ai-systems
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Beat the recency heuristic before building a recommender, and avoid the feedback loop.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 14-ai-systems/knowledge/Prediction.md
Outputs:
  - Recommendation capabilities within model_strategy
Related Modules:
  - 08-product
  - 12-metrics
Tags:
  - AI
  - Recommendation
  - Concept
---

# Recommendation

---

# What It Is

Surfacing what the user probably wants next — and the capability whose non-AI alternative is unusually strong.

| Approach | Data needed | Typically beats |
| --- | --- | --- |
| **Most recently used, by this user** | None | A surprisingly large share of recommenders |
| **Most frequently used, by this user** | The user's own history | Most personalization proposals |
| Rule-based relevance — same patient, same day, same category | Domain rules | Cold-start situations |
| Collaborative filtering | Many users' behavior | Nothing available at launch |
| Model-based semantic similarity | Content, and a way to embed it | Genuinely novel discovery needs |

The framework's advocate check bites hard here: for a professional tool, "sorted by what this clinician used last week" is an honest
alternative that a competent person would defend — and it needs no data, no model, no evaluation and no cost per operation.

---

# When It Applies

In Move 2 (Compare), where the heuristic usually wins, and in Move 3 where collaborative approaches fail the data test at launch.

---

# How to Apply It Here

**Implement the recency heuristic first and measure it.** It is close to free, and it establishes the bar any model must beat. Without it,
the model's performance has nothing to be compared against.

**Confirm the data for collaborative approaches.** They need many users behaving, which a launching product does not have.
`Prediction.md`'s cold-start point applies identically.

**Watch the feedback loop.** A recommender trained on what users clicked teaches itself that what it surfaced is what they want. Over time it
narrows, and the narrowing looks like improving engagement — `12-metrics`' counter-metric territory.

**Keep it dismissible and non-blocking.** A per-instance guarantee from `Evaluation.md`: the user can always ignore it, and it never occupies
the position the deliberate action needs.

**Define what a good recommendation means.** Clicked is not the same as useful. `12-metrics`' vanity logic applies — a recommendation clicked
and then abandoned was a mistake with an engagement signal attached.

---

# Where It Misleads

**Personalization is proposed before the baseline exists.** Most professional tools need "the things you were working on", which is not
personalization — it is a sort order.

**Click-through is used as the quality measure.** It rewards prominence and novelty rather than usefulness, and it is exactly the metric a
narrowing feedback loop improves.

**Diversity is lost silently.** A recommender optimizing for clicks converges, and the user stops seeing things they would have wanted. Nothing
in the metrics reports this unless a counter-metric was defined.

**Cold-start behavior is unspecified.** A new user with no history is the majority case at launch, and an empty or arbitrary recommendation
list is the first thing they see — `10-execution/knowledge/Empty-States.md` applies.

**Recommendations occupy the primary position.** In a professional tool, the deliberate action must always be reachable directly. A suggestion
that displaces it is a cost paid on every use.

---

# Related

| | |
| --- | --- |
| `Prediction.md` | Cold start and the data requirement |
| `AI-Use-Cases.md` | The heuristic alternative, defended honestly |
| `Evaluation.md` | Dismissibility as a per-instance guarantee |
| `12-metrics` | Why clicks are the wrong measure |

---

> **Concept Note**
>
> Build "what you used last week" first. It is free, and it is the bar.
>
> A recommender trained on its own clicks narrows over time, and the
> narrowing looks like rising engagement.
