---
Title: Core Principles
Module: 14-ai-systems
Section: core
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the principles that govern judgment when deciding where a model belongs.
Audience:
  - AI Agents
  - Engineers
  - Founders
Prerequisites:
  - constitution/core/03-Core-Principles.md
Outputs:
  - Consistent judgment about AI capability
Related Modules:
  - 12-metrics
  - 13-operations
Tags:
  - AI Systems
  - Principles
---

# Core Principles

---

# Principle Statement

> A model is a component with an unusual property: it fails fluently.
>
> Every principle here follows from that one fact.

---

# Principle 1 — Every Capability Earns Its Place Against Something Simpler

A rule, a lookup, a sorted list, a better form, a default, or asking a different party for structured
input.

The comparison is the module's only gate criterion, because it is the only thing standing between the
product and a model added because it was expected.

---

# Principle 2 — A Straw Man Invalidates the Analysis

It does not weaken it. The whole point of the comparison is that it could have gone the other way.

The test: could a competent person argue for the alternative in one honest sentence? If not, rewrite
the alternative and compare again.

---

# Principle 3 — Dropping Is a Successful Outcome

A module that proposes five capabilities and keeps one has done its job.

Record what was dropped and the simpler thing adopted instead — that record is what stops the same
capability being re-proposed next quarter as an obvious omission.

---

# Principle 4 — A Capability With No Requirement Is an Orphan

The same rule modules 08 and 09 apply. Here the orphan usually arrives from a different direction: not
from the research, but from what is currently possible.

---

# Principle 5 — Unconfirmed Data Is a Blocker, Not a Risk

The most common way an AI capability fails is that it fails before it starts, because the data did not
exist in the form it needed.

"We will have this" is not availability. A capability resting on unchecked data cannot be estimated,
scheduled or built.

---

# Principle 6 — Cold Start Is Part of the Design

Most model-served features are at their worst exactly when the product is newest and users are least
tolerant.

The answer is usually a non-AI path for the first period. That is a design decision, not a
disappointment.

---

# Principle 7 — Data Rights Are a Legal Question

Consent for treatment is not consent for model input. A compliant provider is a precondition, never a
conclusion.

Cite the regime, state the basis, and check every model input against the regulated field list from
`09-technology` §3 — mechanically, as three other modules do.

---

# Principle 8 — Detectability Governs Autonomy, Not Accuracy

A capability right 99% of the time whose 1% is undetectable and consequential is more dangerous than
one right 90% of the time and visibly wrong the rest.

Where the user bears the cost and cannot detect the error, autonomy above "suggests" requires a
mechanism that makes the error visible.

---

# Principle 9 — Ask What One Wrong Output Costs, and Who Pays

In the user's terms, not the system's. Then ask whether it is recoverable.

Autonomy chosen without those answers rises to whatever is impressive.

---

# Principle 10 — The Bar Is Set Before the Build

A bar set after seeing outputs is a description of what happened.

"We will evaluate it" is not a plan. A metric, a method, a figure, a sample size, and the result
required before users see it — that is a plan.

---

# Principle 11 — The Judge Must Be Qualified

In a domain product, quality review requires a domain expert.

A developer who finds a generated clinical summary convincing has established that it is convincing —
precisely the property that makes a wrong one dangerous. This is the same reason `03-user` forbids
inventing user quotes.

---

# Principle 12 — The Golden Set Is Quarantined

Built from real cases, and never used for tuning.

A set that has been optimized against measures how well the capability was fitted to it.

---

# Principle 13 — Two Kinds of Acceptance Criterion Are Required

`08-product`'s `Given / when / then` form assumes the same input produces the same output. A model
breaks that assumption.

So: a **statistical** bar over a sample, and **per-instance guarantees** that hold every single time.
The second is where most real safety lives — always labeled, always dismissible, always bounded,
always cited.

---

# Principle 14 — A Failure Mode Must Be Specific to This Product

"The model may hallucinate" is a property of models. "The model may invent a drug interaction that
does not exist, which a rushed clinician could accept" is something you can design against.

---

# Principle 15 — A Better Prompt Is Not a Guardrail

A guardrail is a constraint on output, a required citation, a confidence threshold below which nothing
is shown, a validation against a real source, or a human confirmation step.

Prompts are how the capability works. Guardrails are what holds when it does not.

---

# Principle 16 — Say the Worst Realistic Outcome Out Loud

And then answer whether you would know it happened. "No" is a common answer and an important finding.

---

# Principle 17 — The Non-AI Fallback Is a Requirement

The provider will have an outage. The model will be deprecated. The output will sometimes be wrong.

What the user does then is part of the product, so it belongs in `08-product` with every other
requirement — not in an AI annex nobody opens while building.

---

# Principle 18 — Pin the Version, Cite the Date

Model capabilities, limits and prices are version-scoped with a fast clock.

An unpinned model changes behavior with no deployment, and evaluation results expire silently.

---

# Principle 19 — Quality Expectations Are Assumptions Until Measured on Real Inputs

Not benchmarks — those are other people's data. Not demos — those are curated examples.

Nothing establishes how a model performs on this product's inputs except running it on this product's
inputs.

---

# Principle 20 — Compute the Share of Revenue

Cost per operation, times operations per user, divided by revenue per user.

A capability consuming a significant fraction of revenue per user is a margin problem, and it has
killed products. Note it and choose a lever: a cheaper approach, fewer operations, a higher price, or
drop it.

---

# Principle Hierarchy

```
Candidates proposed, each serving a requirement
   ↓
Compared honestly against a simpler alternative
   ↓
Data confirmed, rights established
   ↓
Autonomy set by the wrongness cost and detectability
   ↓
The bar and the ship gate defined before commitment
   ↓
Failure modes specific, detected, guarded, with a fallback
   ↓
Cost checked against revenue
```

Each level depends on the one above. Data work done before the comparison is work spent on capabilities
that should have been dropped; autonomy decided before the comparison is a decision about a feature
that will not exist.

---

# Common Violations

- A capability kept because it was expected.
- A straw-man alternative.
- Nothing dropped.
- A capability serving no requirement.
- Data assumed rather than confirmed.
- Cold start unaddressed.
- A regulated field as a model input.
- Autonomy above the detectability of the error.
- The build team judging domain quality.
- The bar set after seeing outputs.
- The golden set used for tuning.
- Only statistical criteria, with no per-instance guarantees.
- Generic failure modes.
- A prompt offered as a guardrail.
- The worst outcome unstated.
- The fallback treated as a contingency.
- An unpinned model version.
- Benchmarks cited as evidence of quality.
- The cost ratio never computed.

---

# Self Assessment

- Would something simpler have worked?
- Could someone argue for each alternative I rejected?
- What did I drop?
- Does every capability serve a requirement?
- Is any data need unconfirmed?
- Does any model input carry a protected field?
- Can the user detect a wrong output?
- Is the autonomy level justified?
- Was the bar set before the build?
- Is the judge qualified?
- Are my failure modes about this product?
- Is the fallback a requirement?
- Is the version pinned?
- What share of revenue does this consume?

---

> **Core Principle**
>
> The framework's central rule is that an assumption must never be
> smoothed into a fact.
>
> A model does that by default, in every sentence it produces —
> which is why this module is the most cautious one in it.
