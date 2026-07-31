---
Title: Common Mistakes
Module: 04-problem
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Name the ways evidence gets manufactured at the problem stage and what each costs.
Audience:
  - Product Managers
  - Founders
  - Researchers
Prerequisites:
  - 04-problem/learn/01-Why-It-Matters.md
Outputs:
  - Recognition of problem-stage failure patterns
Related Modules:
  - 07-strategy
  - 08-product
Tags:
  - Problem
  - Mistakes
  - Learn
---

# Common Mistakes

---

# Overview

Every mistake in this module has the same effect: something that was not known becomes
something that is treated as known. They differ only in how the promotion happens.

---

# 1. Inference Promoted to Evidence

**What it looks like.** "Users find this frustrating." No source, no count, stated in
the same voice as the sourced findings around it.

**Why it is tempting.** It is probably true. Hedging a probably-true statement feels
pedantic, and the document reads better without the qualifier.

**What it costs.** This is the failure the framework is built against. The claim is
inherited by modules 05, 06 and 07 as verified, and by module 08 as the root of a
requirement trace. Nothing downstream can detect it, because it looks exactly like the
claims that were checked.

**Instead.** Tag it. `[inferred: from the observed workaround]` is a useful line — it
says what the inference rests on, so a later module can judge its weight.

---

# 2. The Ranking Built to Reach a Predetermined Winner

**What it looks like.** A scored table in which the problem the team already wanted to
solve comes first, by a comfortable margin.

**Why it is tempting.** The team came in with a solution — most do — and the scoring
gets tuned, usually unconsciously, until the arithmetic agrees.

**What it costs.** Module 07's gate requires the chosen approach to be justified against
the ranked problems. If the ranking was reverse-engineered, that check passes
automatically and validates nothing.

**Instead.** Score each axis before looking at the totals, and write the evidence for
each score before assigning it. If the winner surprises you, the process worked.

---

# 3. Solving the Symptom

**What it looks like.** "Users forget to update the status field." Ranked, scored, and
addressed with reminders.

**Why it is tempting.** Symptoms are visible and specific; root causes are diffuse and
often organizational.

**What it costs.** A product that removes the symptom and leaves the cause produces a
new symptom within a quarter. In this example, the field is probably not the user's job
to maintain, or updating it produces nothing they care about.

**Instead.** Ask why twice more. The stopping point is where the answer becomes
something you can act on but the next answer would be someone else's decision.

---

# 4. The Interview About a Hypothetical, Recorded as Evidence

**What it looks like.** "Eight of ten said they would use this weekly."

**Why it is tempting.** It has a number in it, and numbers read as evidence.

**What it costs.** Stated future behavior is close to worthless as a predictor and
excellent at producing false confidence. Its presence in the evidence log crowds out
the real signal, which is what those ten people currently do.

**Instead.** Ask about the past. "How many times did this happen last week" produces a
frequency you can score. "Would you use it" produces agreement.

---

# 5. The Problem That Is Real and Already Solved

**What it looks like.** A well-evidenced, frequent, severe problem — with a mature tool
that handles it, which the user is broadly content with.

**Why it is tempting.** All the evidence checks pass. The problem *is* real.

**What it costs.** Module 05 will find the incumbent and module 03's switching cost
will explain why nobody moves. But by then the ranking has already directed the
strategy. The check belongs here: "what do they do about it today" is one of the three
axes precisely so that an adequately-solved problem scores low.

**Instead.** Score the workaround honestly. A good existing solution is a low score on
that axis, not a footnote.

---

# 6. A Validation Plan That Cannot Fail

**What it looks like.** "Interview ten more users to validate the problem."

**Why it is tempting.** It sounds like rigor and it commits to nothing.

**What it costs.** Ten more sympathetic conversations will validate almost any problem.
The plan produces confirmation, is recorded as validation, and the uncertainty it was
supposed to resolve is now invisible.

**Instead.** State what result would disconfirm. "If fewer than half have built a
workaround, the frequency claim is wrong." A plan with no failing outcome is not a
plan.

---

# 7. Passing the Gate Instead of Declaring the Shortfall

**What it looks like.** Three problems marked `[verified]` where the evidence is a
plausible reading of two conversations.

**Why it is tempting.** `declared_shortfall` feels like admitting the research failed,
and the criterion is right there asking for three.

**What it costs.** Everything. This is the single most damaging thing that can happen
in the framework — it converts a survivable known gap into an undetectable false
foundation. Module 07 then does not weight for uncertainty, because as far as it can
tell there is none.

**Instead.** Declare it. The run continues either way; the difference is whether module
07 knows what it is standing on.

---

# The Pattern

| Mistake | Underlying move |
| --- | --- |
| Inference promoted | Removing a qualifier that felt weak |
| Reverse-engineered ranking | Justifying a decision already made |
| Symptom solved | Stopping at the visible layer |
| Hypothetical as evidence | Preferring a number to an observation |
| Already-solved problem | Scoring the pain and not the alternative |
| Unfalsifiable validation plan | Rigor as performance |
| Gate passed instead of shortfall declared | Avoiding the appearance of failure |

Six of the seven make the run look more confident. That is this module's characteristic
failure and it is precisely inverted from what the module is for.

---

> **Mistakes Principle**
>
> The worst outcome here is not a weak evidence base. It is a weak evidence base that
> nobody downstream can see.
>
> Every mistake on this page converts the first into the second.
