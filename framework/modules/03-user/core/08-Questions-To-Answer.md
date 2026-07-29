---
Title: Questions To Answer
Module: 03-user
Section: core
Category: Interrogation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The question bank used to move from a market to a specific person and their working reality.
Audience:
  - AI Agents
  - Researchers
Prerequisites:
  - 03-user/core/06-Framework.md
Outputs:
  - Filled sections of the User Analysis
  - state.open_questions
Related Modules:
  - 04-problem
  - 10-execution
Tags:
  - User
  - Questions
  - Research
---

# Questions To Answer

---

# Overview

Most questions here are researchable by proxy — reviews, forums, studies, job postings.

A few are genuinely for the operator, marked **OPERATOR**. And a third category is
unique to this module: questions that can only be answered by **asking a real user**.
Those are marked **NEEDS USER** and become the validation list handed to module 04.

Recording a question as NEEDS USER is a valid outcome. Inventing an answer is not.

---

# 1. Segmentation

| # | Question | If unanswered |
| --- | --- | --- |
| 1.1 | Who inside the market boundary would buy this? | No segments |
| 1.2 | Which groups behave differently from each other, and how? | Segmentation is demographic, not behavioral |
| 1.3 | How large is each group? | Cannot prioritize |
| 1.4 | How intensely does each feel the problem? | Cannot prioritize |
| 1.5 | Which can pay, and from whose budget? | Module 06 has no payer |
| 1.6 | How would each be reached? | Module 11 has no channel |
| 1.7 | Is the buyer the same person as the user? | Two audiences may be missed |

> **1.2 is the test that makes a segment real.** If two groups would buy, use, and reject
> the product for identical reasons, they are one segment described twice.

---

# 2. Prioritization

| # | Question | If unanswered |
| --- | --- | --- |
| 2.1 | Which segment do we serve first? | The product has no focus |
| 2.2 | What in the criteria table justifies that? | The choice is preference, not reasoning |
| 2.3 | If a larger segment was passed over, why? | The obvious objection goes unanswered |
| 2.4 | What do we give up by choosing this one? | The cost of the choice is hidden |
| 2.5 | What would make us change this choice later? | No trigger for revisiting |

---

# 3. The Person

| # | Question | If unanswered |
| --- | --- | --- |
| 3.1 | What is their role, and what are they accountable for? | No context |
| 3.2 | What does their working day look like? | Flows will be designed for an imaginary day |
| 3.3 | What does success look like to them personally? | Value proposition has no target |
| 3.4 | What are their constraints — time, budget, skill, physical setting? | The product may be unusable in context |
| 3.5 | How comfortable are they with new software? | Onboarding is mis-pitched |
| 3.6 | **NEEDS USER** — What would they say frustrates them most? | Persona rests on inference |
| 3.7 | Who else influences or blocks their decision? | The real blocker is invisible |
| 3.8 | What is genuinely not known about this person? | Gaps are hidden rather than handed forward |

<!-- 3.8 is not a failure to answer the others. It is a deliverable. -->

---

# 4. Current Workflow

| # | Question | If unanswered |
| --- | --- | --- |
| 4.1 | What are the actual steps they take today? | Module 04 has nothing to rank against |
| 4.2 | Which tools do they use at each step? | The real competitor is unknown |
| 4.3 | How long does the whole workflow take? | Value cannot be quantified |
| 4.4 | Where does it break, stall, or annoy? | The opportunity is unlocated |
| 4.5 | Which step would they most want removed? | Priority is guesswork |
| 4.6 | What do they do when something goes wrong? | Failure states will be unspecified |
| 4.7 | Which tools must the product coexist with? | Integration requirements missed |
| 4.8 | How often does this workflow happen? | Severity cannot be assessed |

> **4.4 is where the product usually is.** The opportunity is more often in the friction
> between steps than in the steps themselves.

---

# 5. Switching Cost

| # | Question | If unanswered |
| --- | --- | --- |
| 5.1 | What data would have to move, and how much? | Migration underestimated |
| 5.2 | Who would need retraining, and for how long? | Adoption cost invisible |
| 5.3 | What stops working during the changeover? | Disruption risk unassessed |
| 5.4 | Are they contractually locked in, and until when? | Timing of any sale is unknown |
| 5.5 | What do they fear going wrong if they switch? | The real objection is unaddressed |
| 5.6 | What would have to be true for switching to be worth it? | The product has no bar to clear |
| 5.7 | Who inside the organization would resist? | The blocker surfaces during the sale |

---

# 6. Jobs To Be Done

| # | Question | If unanswered |
| --- | --- | --- |
| 6.1 | In what situation does the need arise? | The job has no trigger |
| 6.2 | What are they trying to achieve, independent of any tool? | The job names a solution |
| 6.3 | What becomes possible for them when it is done? | The outcome is missing |
| 6.4 | How often does this job arise? | Priority is unknown |
| 6.5 | What satisfies it today, and how well? | The baseline is undefined |
| 6.6 | Which job carries the product? | Focus is missing |
| 6.7 | Which jobs will we deliberately not serve? | Scope will expand in module 08 |

**The test for 6.2:** if the sentence names a product, tool, or feature, it is not a job.

---

# 7. The Immovables

| # | Question | If unanswered |
| --- | --- | --- |
| 7.1 | What would this person not change, whatever the product does? | The product may require an impossible change |
| 7.2 | Which habits are load-bearing for them? | Adoption friction is underestimated |
| 7.3 | Which tools are effectively permanent in their environment? | Integration reality is missed |

---

# 8. Questions for the Operator

| # | Question | Rank |
| --- | --- | --- |
| O1 | **OPERATOR** — Do you have access to any user of this type today? | Blocking if primary research is expected |
| O2 | **OPERATOR** — Have you personally observed this workflow? | Deferrable — changes evidence standing |
| O3 | **OPERATOR** — Is any segment out of bounds commercially? | Deferrable |

---

# 9. Questions Needing a Real User

These cannot be answered by proxy. Record them; do not answer them.

They become the first entries in the validation plan and are handed to `04-problem`.

| # | Question | Why proxy cannot answer it |
| --- | --- | --- |
| U1 | What frustrates you most about how you do this today? | Reviews report frustration with a product, not with the workflow |
| U2 | What did you try before, and why did you stop? | Abandoned attempts are rarely written up |
| U3 | What would have to be true for you to change tools? | Stated preference requires a person |
| U4 | Who else has to approve this? | Organizational reality is undocumented |
| U5 | What would you refuse to give up? | Nobody writes this down |

---

# 10. Questions the Agent Asks Itself

- Did I choose this segment because it is best, or because it was easiest to research?
- Could my persona describe anyone in this market?
- Did I invent any quote, name, statistic, or detail?
- Which persona rows are inference wearing the clothes of observation?
- Did I document the workflow before naming the jobs?
- Does any job statement contain a solution?
- Did I read three-star reviews, or only the extremes?
- Is my stated confidence consistent with my research mode?

---

# Anti-Patterns

| Anti-pattern | Example | Why it fails |
| --- | --- | --- |
| Demographic segment | "Users aged 30–45" | Does not change behavior |
| Persona as character sketch | "Sarah loves coffee and hates paperwork" | Untraceable, constrains nothing |
| Invented quote | An unattributed user voice | Undetectable fabrication downstream |
| Job naming a solution | "They want an AI assistant" | Locks the solution before the problem |
| Skipping switching cost | No migration assessment | The product loses to an installed inferior tool |
| Answering a NEEDS USER question | Inventing a stated preference | Fabrication presented as research |

---

> **Interrogation Principle**
>
> Some questions in this module have no answer available to you.
>
> Writing "we do not know, and here is how to find out" is research.
> Filling the gap with something plausible is not.
