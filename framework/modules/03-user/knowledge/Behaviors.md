---
Title: Behaviors
Module: 03-user
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Separate what people do from what they say and what we conclude.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 03-user/core/06-Framework.md
Outputs:
  - Behavioral evidence within current_workflow
Related Modules:
  - 04-problem
Tags:
  - User
  - Behavior
  - Concept
---

# Behaviors

---

# What It Is

What people actually do — as distinct from what they say they do, what they say they want, and what
we conclude from either.

The framework ranks these deliberately, because they are routinely recorded as if equivalent:

| Strength | Kind of evidence | Example |
| --- | --- | --- |
| **Strongest** | Observed behavior with a cost attached | Keeps a private spreadsheet, updated nightly, in parallel with the official system |
| Strong | A workaround they built | Emails themselves a reminder because the tool has none |
| Moderate | Reported behavior | "I usually check it twice" |
| Weak | Stated preference | "I would like it to be faster" |
| Weakest | Predicted behavior | "I would definitely use that" |

The bottom two rows are the ones most easily gathered and most likely to be wrong. Stated intent is
not behavior, and the gap between them has ended more products than competition has.

---

# When It Applies

Throughout Move 4 (Observe), and as the evidence base Move 5 (Job) interprets. Behavior is also what
`04-problem` requires to call a problem verified.

---

# How to Apply It Here

**Prefer behavior with a cost.** Anything a person spends time, money or reputation on repeatedly is
strong evidence — the cost is what makes it credible. Free opinions are cheap in both senses.

**Record the behavior before the interpretation, and keep them in separate sentences.** "She keeps a
duplicate spreadsheet" is an observation. "She does not trust the system" is a conclusion, and it may
be wrong — she may simply need it sorted differently.

**Treat workarounds as the headline finding.** A built workaround proves three things at once: the
problem is real, it is worth effort, and the current tool does not solve it. Little else in the
framework establishes all three from one observation.

**Note what the behavior costs them now.** That figure is the bar `08-product` has to beat and the
baseline `12-metrics` will measure against.

**Tag reported behavior as reported.** Recollection compresses and flatters. "Twice a day" often means
"whenever I remember", and the difference matters to a retention model.

---

# Where It Misleads

**Stated preference is the most abundant evidence available and the least predictive.** It is easy to
collect, sounds like validation, and describes an imagined future self. `04-problem` explicitly will
not accept it as verification.

**Behavior is over-explained.** People do things for reasons including habit, a rule, someone else's
instruction, and no reason at all. Assigning a motive and then designing for the motive builds for a
person who does not exist.

**Absence of a behavior is read as absence of a need.** Nobody works around a problem they have
accepted as unavoidable. Silence can mean resignation, and that is a harder market but not an empty
one.

**Observing one person becomes a claim about a segment.** One vivid behavior is a lead, not a
distribution. Say how many were observed; a sample of one is a legitimate finding when labeled as
one.

---

# Related

| | |
| --- | --- |
| `User-Journey.md` | Where behavior is recorded in sequence |
| `Pain-Points.md` | The friction behavior reveals |
| `Jobs-To-Be-Done.md` | The interpretation behavior supports |
| `04-problem` | Where behavior becomes verification |

---

> **Concept Note**
>
> What someone built a workaround for is worth more than anything
> they told you they wanted.
>
> Record the action, then the conclusion — never merged into one
> sentence.
