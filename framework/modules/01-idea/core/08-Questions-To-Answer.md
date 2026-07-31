---
Title: Questions To Answer
Module: 01-idea
Section: core
Category: Interrogation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: The question bank used to convert a vague idea into a precise premise.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 01-idea/core/06-Framework.md
Outputs:
  - clarifying_questions
  - state.open_questions
Related Modules:
  - 02-market
  - 03-user
Tags:
  - Idea
  - Questions
  - Discovery
---

# Questions To Answer

---

# Overview

This is the interrogation bank for module 01.

Two kinds of question live here:

| Kind | Answered by | Purpose |
| --- | --- | --- |
| **Internal** | the agent, from the idea itself | Structures the brief |
| **Operator** | the human | Resolves what cannot be researched |

Work through every section. A section skipped is an assumption made silently.

---

# How to Use This

1. Read each question.
2. If it can be answered from the idea, answer it in the brief.
3. If it cannot, and the answer **changes the work**, it becomes an operator question.
4. If it cannot, and the answer changes nothing, record an assumption and move on.
5. Rank operator questions as **blocking** or **deferrable**.

The test for asking: *would a different answer produce a different product?*
If no, do not ask it. Politeness questions waste the checkpoint.

---

# 1. The Idea Itself

| # | Question | If unanswered |
| --- | --- | --- |
| 1.1 | What is being proposed, in one sentence? | The brief has no anchor |
| 1.2 | Is this a product, a feature, or a business? | Scope is undefined |
| 1.3 | What triggered this idea — an observation, a complaint, a gap, a trend? | The evidence basis is unknown |
| 1.4 | Has the operator seen this problem personally, or heard about it? | Confidence in the premise is unknown |

Questions 1.3 and 1.4 matter more than they appear. An idea born from watching someone
struggle carries different evidence weight from one born from reading a market report.
Record which it is.

---

# 2. The Problem Underneath

| # | Question | If unanswered |
| --- | --- | --- |
| 2.1 | What is hard, slow, expensive or unpleasant today? | No problem to research |
| 2.2 | Who experiences it? | No user to research |
| 2.3 | How often does it occur? | Severity cannot be assessed |
| 2.4 | What does it cost them — time, money, risk, frustration? | Value cannot be estimated |
| 2.5 | What do they do about it today? | The real competitor is unknown |
| 2.6 | Why has nobody solved this already? | The gap may not exist |

> **2.6 is the highest-value question in this module.**
>
> If a problem is obvious, valuable and unsolved, there is usually a reason: regulation,
> distribution, data access, incentives, or the problem being less painful than it
> appears. Find the reason.
>
> If there is genuinely no reason, be suspicious of the premise rather than excited by it.

---

# 3. Context — Always Ask, Never Guess

Every question in this section is **blocking** unless the idea already answers it. These
are the answers that change what gets built, and none of them can be researched.

| # | Question | Why it changes the product |
| --- | --- | --- |
| 3.1 | Which country or region? | Determines the regulatory regime, the data model and hosting |
| 3.2 | Which segment — individual, small team, large organization? | Different buyer, price, integration surface, sales motion |
| 3.3 | Who pays? Is it the same person who uses it? | Two audiences means two sets of criteria |
| 3.4 | What do they use today? | Replacement, adjacent tool and greenfield are different builds |
| 3.5 | Is there an incumbent system this must integrate with? | Interop may dominate the architecture |
| 3.6 | In what physical or operational setting is it used? | Drives the interface and the failure modes |
| 3.7 | Is this a regulated domain? | Compliance is structural, not a feature |
| **3.8** | **What should this actually be — a website, a phone app, both, a desktop program, or something with no interface at all? And if more than one, which first?** | **Gate criterion 3.** It changes market sizing, where competitors are found, the billing rail, whether offline is a requirement, and the acquisition channel. Eight later modules assume an answer; none of them re-examines it |

**None of these may be assumed.** If the idea does not answer them, they go to the
operator as blocking questions.

---

# 4. Value

| # | Question | If unanswered |
| --- | --- | --- |
| 4.1 | What changes for the user if this exists? | No value proposition |
| 4.2 | Is the value saved time, saved money, reduced risk, or new capability? | Pricing has no basis |
| 4.3 | Is that value large enough to make someone change their behavior? | Adoption is unlikely |
| 4.4 | Who benefits *besides* the direct user? | Missed buyer or channel |

---

# 5. Scope

| # | Question | If unanswered |
| --- | --- | --- |
| 5.1 | What is explicitly **not** part of this? | Scope creeps through every later module |
| 5.2 | Is this one product, or several bundled by ambition? | The MVP cannot be cut |
| 5.3 | What is the smallest version that would still be useful? | No MVP anchor exists |
| 5.4 | What would the operator refuse to build? | Constraints surface too late |

Question 5.2 catches the most common failure in this module. An idea phrased as
"...and everything else they need" is several products. Say so early, while it is cheap.

---

# 6. Constraints

| # | Question | If unanswered |
| --- | --- | --- |
| 6.1 | Is there a timeline? | The roadmap has no shape |
| 6.2 | Is there a budget? | Architecture and stack cannot be bounded |
| 6.3 | Who is building this — team size and skills? | Estimates are meaningless |
| 6.4 | Is any technology already committed to? | Later choices may be moot |
| 6.5 | Is any distribution channel already available? | Growth planning is guesswork |

---

# 7. Ambition

| # | Question | If unanswered |
| --- | --- | --- |
| 7.1 | Is this a business, a side project, or an internal tool? | Success criteria are undefined |
| 7.2 | What does success look like in twelve months? | Metrics have no target |
| 7.3 | What would make the operator stop? | Failure is never defined in advance, and it costs them |

---

# 8. Questions the Agent Asks Itself

Not for the operator. These check the agent's own work before the checkpoint.

- Did I accept the proposed solution instead of finding the problem?
- Which context dimension did I fill in with a plausible guess?
- Which assumption is so obvious to me that I failed to write it down?
- If a domain expert read my brief, what would they immediately correct?
- Am I asking the operator anything I could have researched myself?
- Would a different answer to each of my questions actually change the work?

---

# Ranking Questions for the Checkpoint

| Rank | Criterion | Behavior |
| --- | --- | --- |
| **Blocking** | The answer determines what gets researched | Halt. Do not proceed |
| **Deferrable** | The answer refines but does not redirect | Record an assumption, proceed, revisit |

All of section 3 is blocking by default.

Present blocking questions first, few in number, and phrased so a busy person can answer
each in one line. A checkpoint with twenty questions gets ignored; one with four sharp
ones gets answered.

---

# Minimum Bar

The gate requires **at least five** clarifying questions asked and either answered or
explicitly deferred.

Five is a floor, not a target. An idea described in one sentence should generate ten.

---

# Anti-Patterns

| Anti-pattern | Example | Why it fails |
| --- | --- | --- |
| Unanswerable | "What is your vision?" | Produces prose, not a decision |
| Already researchable | "How big is the market?" | That is module 02's job, not the operator's |
| Leading | "You want this to be AI-powered, right?" | Confirms an assumption instead of testing it |
| Compound | "Who uses it, who pays, and where?" | Gets one answer for three questions |
| Cosmetic | "What should it be called?" | Changes nothing about the work |

---

> **Interrogation Principle**
>
> The operator knows things that cannot be researched: their market, their access,
> their constraints, their intent.
>
> Ask for those. Research the rest yourself.
