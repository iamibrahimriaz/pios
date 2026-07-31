---
Title: Anti-Examples
Module: framework/constitution
Section: resources
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Demonstrate common poor research patterns, weak reasoning, and low-quality documentation so they can be recognized and avoided.
Audience:
  - AI Agents
  - Product Managers
  - Researchers
  - Business Analysts
  - Product Owners
Prerequisites:
  - learn/10-Common-Mistakes.md
  - core/11-Quality-Gate.md
  - core/12-Checklist.md
  - core/13-Template.md
  - 14-Examples.md
Outputs:
  - Recognition of poor research
  - Improved research quality
Related Modules:
  - 16-Evaluation.md
  - 17-Reflection.md
Tags:
  - Anti Examples
  - Bad Practices
  - Research Quality
---

# Anti-Examples

---

# Overview

One of the fastest ways to improve research quality is to understand what **bad research looks like**.

This document contains examples of poor thinking, weak reasoning, and common documentation mistakes.

These examples are intentionally incorrect.

Their purpose is to help AI agents recognize and avoid patterns that reduce research quality.

---

# Anti-Example 1 — Starting with the Solution

## ❌ Poor Thinking

```
Let's build an AI-powered pharmacy management system.
```

Problems

- No problem identified.
- No user research.
- No business validation.
- AI selected before understanding the need.

Better Thinking

```
Identify the operational challenges pharmacies face before deciding whether AI adds measurable value.
```

---

# Anti-Example 2 — Making Assumptions

## ❌ Poor Thinking

```
Doctors want a mobile application.
```

Problems

- No supporting evidence.
- No interviews.
- No market validation.
- User preference assumed.

Better Thinking

```
Research how doctors currently work and identify which devices they prefer during consultations.
```

---

# Anti-Example 3 — Copying Competitors

## ❌ Poor Thinking

```
Competitor X has 80 features.

We should build the same 80 features.
```

Problems

- No strategic thinking.
- No differentiation.
- Increased complexity.
- Ignores user priorities.

Better Thinking

```
Understand why those features exist, determine which create value, and identify opportunities competitors have missed.
```

---

# Anti-Example 4 — Technology First

## ❌ Poor Thinking

```
We'll use Kubernetes, Microservices, GraphQL, Redis, Kafka, and AI.
```

Problems

- Technology chosen without requirements.
- Unnecessary complexity.
- High maintenance cost.
- No business justification.

Better Thinking

```
Select technology after understanding scalability, team expertise, budget, and product requirements.
```

---

# Anti-Example 5 — Feature Overload

## ❌ Poor Thinking

```
Version 1 should include every feature users might ever need.
```

Problems

- Impossible scope.
- Delayed launch.
- High development cost.
- Difficult validation.

Better Thinking

```
Identify the smallest feature set that solves the core problem and validate it before expanding.
```

---

# Anti-Example 6 — Unsupported Recommendations

## ❌ Poor Thinking

```
This pricing model is the best.
```

Problems

- No comparison.
- No evidence.
- No customer validation.
- No financial reasoning.

Better Thinking

```
Compare multiple pricing models, analyze competitors, estimate customer willingness to pay, and justify the recommendation.
```

---

# Anti-Example 7 — Ignoring Risks

## ❌ Poor Thinking

```
Everything looks good.
```

Problems

- Unrealiztic.
- No risk assessment.
- No contingency planning.

Better Thinking

```
Document technical, business, legal, operational, and market risks before finalizing recommendations.
```

---

# Anti-Example 8 — Weak Conclusions

## ❌ Poor Thinking

```
The product should succeed.
```

Problems

- Subjective.
- No evidence.
- No measurable reasoning.

Better Thinking

```
Current research indicates strong market demand, moderate competition, and a viable business opportunity, while identifying customer acquisition as the primary uncertainty.
```

---

# Anti-Example 9 — Research Without Structure

## ❌ Poor Thinking

```
Collected information from multiple websites.
```

Problems

- No methodology.
- No organization.
- No analysis.
- Difficult to reproduce.

Better Thinking

```
Follow a structured methodology with defined objectives, validated sources, documented findings, analysis, and recommendations.
```

---

# Anti-Example 10 — No Traceability

## ❌ Poor Thinking

```
I recommend Feature A.
```

Problems

Readers cannot determine:

- Why?
- Based on what evidence?
- Compared with what alternatives?
- What risks exist?

Better Thinking

Every recommendation should clearly trace back to:

- Research
- Evidence
- Analysis
- Decision process

---

# Anti-Example 11 — Ignoring the Business

## ❌ Poor Thinking

```
Users will love it.
```

Problems

- Business ignored.
- Revenue ignored.
- Costs ignored.
- Sustainability ignored.

Better Thinking

Every recommendation should balance:

- User value
- Business value
- Technical feasibility
- Operational sustainability

---

# Anti-Example 12 — Ignoring Users

## ❌ Poor Thinking

```
This interface looks modern.
```

Problems

- Personal opinion.
- No usability validation.
- No user feedback.

Better Thinking

Design decisions should be based on user goals, workflows, and usability evidence.

---

# Anti-Example 13 — False Confidence

## ❌ Poor Thinking

```
This will definitely become a successful product.
```

Problems

- Impossible certainty.
- Ignores uncertainty.
- Ignores market dynamics.

Better Thinking

State confidence based on available evidence and clearly document remaining uncertainties.

---

# Anti-Example 14 — Confusing Data with Insight

## ❌ Poor Thinking

```
The healthcare software market is growing.
```

Problems

- Fact only.
- No interpretation.
- No strategic value.

Better Thinking

```
The healthcare software market is expanding, yet independent doctors remain underserved, indicating a potential opportunity for lightweight, cloud-based practice management solutions.
```

---

# Anti-Example 15 — Ending Research Too Early

## ❌ Poor Thinking

```
Research completed.
```

Problems

Questions remain unanswered.

Risks remain undocumented.

Validation has not occurred.

Better Thinking

Research ends only after:

- Validation
- Quality review
- Documentation
- Lessons learned
- Knowledge improvement

---

# Common Warning Signs

Review your work if you notice:

- Too many assumptions.
- Very little evidence.
- Generic recommendations.
- Missing user research.
- Missing competitor analysis.
- No trade-offs.
- No risks.
- No reasoning.
- No implementation guidance.

These indicate incomplete research.

---

# How to Use Anti-Examples

Use these examples during:

- Self-review
- Peer review
- AI evaluation
- Contributor training
- Research audits

Ask:

> "Does any part of my work resemble these anti-examples?"

If the answer is **Yes**, revise the research.

---

# Self Assessment

Before completing any project:

- Have I avoided assumptions?
- Have I justified recommendations?
- Have I explained my reasoning?
- Have I documented risks?
- Have I validated important conclusions?
- Can someone reproduce my work?

If any answer is **No**, continue improving the research.

---

# References

This document complements:

- Common Mistakes
- Research Methodology
- Quality Gate
- Research Checklist
- Examples

Together, these modules define both good and bad research patterns.

---

# Future Improvements

Future versions may include:

- Domain-specific anti-examples
- AI-generated anti-pattern detection
- Real-world case studies
- Before-and-after document comparisons
- Research quality scoring

---

> **Anti-Example Principle**

> Understanding failure is as important as understanding success.

> Product Intelligence OS uses anti-examples to teach what **not** to do, helping AI agents recognize weak reasoning, avoid common pitfalls, and consistently produce higher-quality product intelligence.