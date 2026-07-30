---
Title: Questions To Answer
Module: 14-ai-systems
Section: core
Category: Inquiry
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The complete question set this module must answer before its gate can pass.
Audience:
  - AI Agents
  - Engineers
  - Product Managers
Prerequisites:
  - 14-ai-systems/core/06-Framework.md
Outputs:
  - Answered question set
Related Modules:
  - 12-metrics
  - 13-operations
Tags:
  - AI Systems
  - Questions
---

# Questions To Answer

---

# Overview

The first question decides whether the rest apply. The second decides whether each capability
survives.

Questions marked **OPERATOR** cannot be inferred. Questions marked **NEEDS EXPERT** cannot be
answered by the build team, and pretending otherwise is how a domain product ships confidently wrong
output.

---

# 0. Whether This Module Applies

| # | Question | If unanswered |
| --- | --- | --- |
| 0.1 | Does any requirement need judgment, generation, extraction or prediction that cannot be a rule? | A model is added because it is expected |
| 0.2 | If none does, has that been recorded plainly? | The absence looks like an omission |

> "No AI capability is justified for this product" is a complete and legitimate output.

---

# 1. Inherited Inputs

| # | Question | If unanswered |
| --- | --- | --- |
| 1.1 | Which requirements might a model serve? | Capabilities with no parent |
| 1.2 | What are the jobs, from `03-user`? | The capability serves the product, not the user |
| 1.3 | Which data fields are PII or regulated, from `09-technology` §3? | Regulated data reaches a provider |
| 1.4 | What is the architecture the capability sits inside? | Architecture invented here |
| 1.5 | Are there regulatory disclosure obligations? | An undisclosed AI involvement that had to be disclosed |
| 1.6 | What is revenue per user per month? | The cost ratio cannot be computed |
| 1.7 | What is the persona's real tolerance for error? | Autonomy chosen against nothing |
| 1.8 | What latency does the flow allow? | A capability too slow for the step it sits in |

---

# 2. The Comparison

Asked of every candidate. This section decides the module.

| # | Question | If unanswered |
| --- | --- | --- |
| 2.1 | What requirement does this capability serve? | An orphan, arriving from what is possible |
| 2.2 | **What is the honest non-AI alternative?** | Capability theater |
| 2.3 | **Could a competent person argue for that alternative in one sentence?** | It was a straw man; the comparison proved nothing |
| 2.4 | Which wins, and why? | The choice was made before the analysis |
| 2.5 | If the alternative wins, was the capability dropped? | The analysis was decorative |
| 2.6 | For each dropped capability, what was adopted instead? | It returns next quarter as an omission |
| 2.7 | Does the alternative win on quality but lose on effort? | A legitimate reason, unstated |
| 2.8 | How many capabilities were proposed, and how many kept? | The ratio is the module's honesty signal |

> A module that proposes five and keeps one has done its job. One that keeps all five has not run
> 2.2 honestly.

---

# 3. Data

| # | Question | If unanswered |
| --- | --- | --- |
| 3.1 | What data does this capability need? | Unbuildable |
| 3.2 | Where does it come from? | Assumed to exist somewhere |
| 3.3 | **Is it available now — confirmed, not projected?** | The most common pre-start failure |
| 3.4 | Is there enough of it for this approach? | A capability that cannot reach its bar |
| 3.5 | What is its quality? | Garbage input, confident output |
| 3.6 | **How does the capability behave before any data accumulates?** | Worst exactly when the product is newest |
| 3.7 | Do we have the right to use this data this way, under which regime? | A legal exposure, not a technical one |
| 3.8 | Is consent required, and do we have it? | Consent for treatment is not consent for model input |
| 3.9 | Does the data leave our systems, to whom, in which jurisdiction? | Regulated data moved without anyone deciding to |
| 3.10 | **Does any model input carry a regulated or PII field?** | Fails the gate |
| 3.11 | Is provider training on our data disabled, and contracted? | Assumed, not agreed |

---

# 4. Autonomy

| # | Question | If unanswered |
| --- | --- | --- |
| 4.1 | What does the user experience? | The capability is described in system terms |
| 4.2 | **What does one wrong output cost, in the user's terms?** | Autonomy chosen by convenience |
| 4.3 | **Who bears that cost?** | The user pays for a decision the operator made |
| 4.4 | **Can the user detect that it is wrong?** | The decisive question, skipped |
| 4.5 | Is the error recoverable, and how? | An unrecoverable error treated as a minor one |
| 4.6 | What autonomy level, and why that one? | The level rises to whatever is impressive |
| 4.7 | Is review always, sampled, or never? | Oversight assumed |
| 4.8 | Can the user override, and is the override recorded? | No trail, and no learning |
| 4.9 | Is AI involvement disclosed? | A disclosure obligation missed |
| 4.10 | Is generated content labeled? | Indistinguishable from human-authored content |
| 4.11 | Can the user see why a suggestion was made? | Trust with no basis |

---

# 5. Evaluation

| # | Question | If unanswered |
| --- | --- | --- |
| 5.1 | What does quality mean for this capability? | "It seems good" |
| 5.2 | How is it measured? | Never measured |
| 5.3 | **What is the passing bar?** | Whatever was achieved becomes the bar |
| 5.4 | Over what sample size? | A judgment from three examples |
| 5.5 | How is the golden set built, and kept out of tuning? | It measures fit to itself |
| 5.6 | **NEEDS EXPERT** — who judges, and what qualifies them? | The build team assesses clinical or legal correctness |
| 5.7 | **What is the ship gate?** | It ships regardless |
| 5.8 | What happens if the bar is missed? | It ships anyway |
| 5.9 | How is a model or prompt change re-evaluated? | Silent regression |
| 5.10 | What statistical criteria apply? | No measurable expectation |
| 5.11 | **What must be true of every single output?** | Where most real safety lives, unspecified |

---

# 6. Failure

| # | Question | If unanswered |
| --- | --- | --- |
| 6.1 | How does this fail, specifically in this product? | "The model may hallucinate" |
| 6.2 | What does each failure cost the user? | Severity unassessed |
| 6.3 | **How is each failure detected?** | It is not |
| 6.4 | What guardrail constrains it? | A better prompt, offered as a control |
| 6.5 | **What is the worst realistic outcome?** | Nobody has said it out loud |
| 6.6 | Would we know it happened? | Frequently no — which is the finding |
| 6.7 | Which failures are silent and plausible? | The dangerous class, unexamined |
| 6.8 | **What does the user do when it is wrong, and how do they notice?** | Stuck, holding a confident error |
| 6.9 | Is the non-AI fallback a requirement? | A contingency nobody builds |
| 6.10 | What happens when the provider has an outage? | The feature simply stops |
| 6.11 | What happens when this model version is deprecated? | Forced migration, unplanned |
| 6.12 | What would switching provider require? | Lock-in discovered when it matters |

---

# 7. Cost

| # | Question | If unanswered |
| --- | --- | --- |
| 7.1 | What does one operation cost? | Unbudgeted |
| 7.2 | How many operations per user per month, and on what basis? | The multiplier is invented |
| 7.3 | What is AI cost per user per month? | The line is missing from the cost to serve |
| 7.4 | **What share of revenue per user does it consume?** | A margin problem discovered by an accountant |
| 7.5 | Is that acceptable, and to whom? | Nobody decided |
| 7.6 | If not, which lever changes — approach, volume, price, or drop it? | It is absorbed |
| 7.7 | **OPERATOR** — is this share of revenue acceptable to you? | The framework decides their margin |

---

# 8. Open

| # | Question | Category |
| --- | --- | --- |
| 8.1 | Which quality expectation has never been measured on this product's real inputs? | **Assumption** |
| 8.2 | Which data need is unconfirmed? | **Blocker** |
| 8.3 | Is any data-rights question unresolved? | **Blocker** |
| 8.4 | Who in the operator's world can judge domain quality? | **OPERATOR** |
| 8.5 | Is the operator willing to disclose AI involvement to their users? | **OPERATOR** |

---

# Question Coverage

| Section | Feeds |
| --- | --- |
| 0 | §1 — or an early exit |
| 1 | §2, §3 inherited scope and placement |
| 2 | §2 Candidate comparison |
| 3 | §6 Data |
| 4 | §4, §7 Capability detail and oversight |
| 5 | §8 Evaluation |
| 6 | §9 Failure modes, §5 model strategy |
| 7 | §10 Cost |
| 8 | §11 Assumptions |

---

# Self Assessment

- Did I answer 0.1 honestly before proposing anything?
- Does every candidate have a real answer to 2.2 and 2.3?
- What is my proposed-to-kept ratio?
- Is any data need answered "projected" rather than confirmed?
- Did I check 3.10 mechanically?
- Did I answer 4.4 before choosing an autonomy level?
- Was the bar in 5.3 set before or after seeing outputs?
- Is 5.6 answered with someone qualified?
- Could 6.1 apply to any product, or only this one?
- Did I compute 7.4?

---

> **Question Principle**
>
> Question 2.2 is the module.
>
> Every other question here is care taken over something that
> already survived it.
