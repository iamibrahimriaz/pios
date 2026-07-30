---
Title: Assumptions
Module: 01-idea
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define what counts as an assumption, and how each is recorded so it can be closed.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - engine/evidence-policy.md
Outputs:
  - initial_assumptions, each with a validation method
Related Modules:
  - 04-problem
  - 07-strategy
Tags:
  - Idea
  - Assumptions
  - Evidence
---

# Assumptions

---

# What It Is

Anything the idea depends on that has not been established.

Not a doubt or a caveat — a **load-bearing belief**. The test is mechanical: if this turned out
to be false, would the idea change? If yes, it is an assumption and it gets recorded. If no, it
is background.

Every assumption in this framework carries two things:

| Field | Why |
| --- | --- |
| The statement | What is being assumed, in one sentence |
| The validation method | What would settle it, and roughly what that costs |

An assumption with no validation method is a worry. With one, it is a task.

---

# When It Applies

In Pass 5 (Interrogate) and Pass 6 (Bound), and then continuously. Every module appends to
`state.assumptions`, and universal gate U5 requires it.

This module's set is special only in being first: `initial_assumptions` are the beliefs present
in the raw idea before any research at all.

---

# How to Apply It Here

**Surface the assumptions the idea does not know it has.** A raw idea usually assumes:

| Hidden assumption | Often false |
| --- | --- |
| The person with the problem is the person who pays | Frequently a different party entirely |
| The problem is worth solving to them | It may be tolerated deliberately |
| They are permitted to adopt a solution | Regulated professions often are not |
| The current way is bad | It may be bad *and* good enough |
| The work happens the way it is described | Descriptions of one's own workflow are unreliable |

**Sort by consequence, not by confidence.** The assumption most worth testing is the one that
would invalidate the most work if wrong — usually the problem assumption, which is also usually
the cheapest to test.

**Name the cheapest test.** Not the best test. Ten conversations beat a survey of two hundred
for this purpose, and both beat a build.

**Never resolve an assumption by restating it more confidently.** This is the framework's
central prohibition, and it starts here, where the idea is still soft enough to be rephrased
into a fact without anyone noticing.

---

# Where It Misleads

**A long assumption list can substitute for judgment.** Thirty recorded assumptions with no
ranking is a document nobody acts on. Three ranked by consequence is an agenda.

**An assumption can be recorded and then treated as settled** because it is written down and
therefore feels handled. `04-problem`'s declared shortfall and `07-strategy`'s Milestone Zero
exist precisely because that happens.

**Some assumptions cannot be closed before building.** That is legitimate. What is not
legitimate is failing to say so — the framework's answer is a lowered confidence, a stated
position, and validation sequenced before the build.

---

# Related

| | |
| --- | --- |
| `engine/evidence-policy.md` | The three tags and the prohibition |
| `Hypothesis.md` | The form an assumption takes when made falsifiable |
| `Idea-Validation.md` | How each is closed, and what that costs |

---

> **Concept Note**
>
> The dangerous assumption is not the one you doubt.
>
> It is the one so obvious to you that it never appeared in the sentence.
