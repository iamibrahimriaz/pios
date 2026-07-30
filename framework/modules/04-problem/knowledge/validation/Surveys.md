---
Title: Surveys
Module: 04-problem
Section: knowledge/validation
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Use surveys for incidence, and only for incidence.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 04-problem/knowledge/validation/Interviews.md
Outputs:
  - Survey method within validation_plan
Related Modules:
  - 02-market
Tags:
  - Problem
  - Surveys
  - Method
---

# Surveys

---

# What It Is

A fixed set of questions asked of many people, used to establish **how common** something is.

That is the one thing surveys do that interviews cannot, and it is the only reason to run one here.

| Surveys can establish | Surveys cannot establish |
| --- | --- |
| Incidence — what share report the problem | Why, or what it costs them in reality |
| Distribution of a known behavior | A behavior nobody has described yet |
| Which of several known problems ranks highest | Whether anyone will buy |
| Which tools are in use | How those tools are actually used |

**Run interviews first.** A survey can only ask about things already discovered; its options come from
qualitative work, and a survey written without it measures the author's assumptions with a decimal place
attached.

---

# When It Applies

In Stage 6, for incidence claims — typically after interviews have established what the problem is and before
`02-market`'s sizing depends on how widespread it is.

---

# How to Apply It Here

**Ask about behavior and the past, not intent.** "In the last week, how many times did you complete notes after
your last patient left?" is answerable. "Would you use a tool that…" is not evidence of anything.

**State the population and the response rate.** A survey of 200 self-selected forum members is a finding about
forum members. Without both figures, the percentage cannot be tagged `[verified]` for the segment.

**Keep it short enough to be finished.** Every question loses respondents, and the ones who abandon are
systematically different from the ones who persist.

**Pre-register the invalidating threshold.** "If fewer than 40% report this weekly, the problem is not common
enough to build around." Set before the data arrives, as `Success-Criteria.md` requires.

**Use free text sparingly and read it first.** One open question at the end often produces the most useful
finding in the whole instrument, and it is the part that cannot be gamed by the option list.

---

# Where It Misleads

**Surveys produce numbers, and numbers get quoted without their sampling.** "68% of practices face this" travels
into a business case and loses the fact that it came from a self-selected sample of thirty. Precision has
nothing to do with representativeness.

**Self-selection biases every consumer survey upward on salience.** People who answer a survey about a problem
are disproportionately people who have it. This is not correctable by size — a larger biased sample is a more
confident wrong answer.

**Willingness-to-pay questions are the most misleading in the framework.** Stated price acceptance
systematically exceeds real behavior, and it exceeds it by an amount nobody can predict. `06-business` should
never rest on a survey figure alone.

**Option lists constrain the finding to what was already believed.** If the real problem was not in the list,
the survey cannot discover it — and the result will look clean.

**Agreement scales measure agreeableness.** "Strongly agree" to a sympathetically worded statement costs the
respondent nothing and predicts nothing.

---

# Related

| | |
| --- | --- |
| `Interviews.md` | What must come first |
| `Analytics.md` | Behavior, where it can be measured instead of asked |
| `Success-Criteria.md` | Setting the threshold in advance |
| `02-market` | Where incidence corrects the sizing |

---

> **Concept Note**
>
> Use a survey to count something you already understand.
>
> Run one before the interviews and you will measure your own
> assumptions — to two decimal places.
