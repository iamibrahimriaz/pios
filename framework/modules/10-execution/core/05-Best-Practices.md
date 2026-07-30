---
Title: Best Practices
Module: 10-execution
Section: core
Category: Practice
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: What experienced delivery leads do when planning that inexperienced ones do not.
Audience:
  - AI Agents
  - Delivery Leads
  - Founders
Prerequisites:
  - 10-execution/core/06-Framework.md
Outputs:
  - Higher-quality execution plans
Related Modules:
  - 12-metrics
Tags:
  - Execution
  - Best Practices
---

# Best Practices

---

# 1. Write the Demo Sentence Before the Milestone Name

For each milestone, write "at the end of this, «person» can «do something»" — then name it.

Naming first produces layer names, because layers are what come to mind. The sentence forces the
milestone to be a slice before it is a label.

---

# 2. Build the First Milestone Around Module 08's First Shippable Slice

That slice was identified specifically so this module would not have to guess.

Re-deriving it here produces a different answer, usually a larger one, and quietly discards work
already done.

---

# 3. Ask for the Team Before Writing Any Number

One question to the operator: who is building this, and how many of them.

Asked afterwards, the durations are already written and the answer becomes a correction nobody
makes.

---

# 4. Write "Relative Size" Rather Than Reaching for Weeks

S, M, L against each other is defensible with no team facts at all. It is also what sequencing
actually needs.

Weeks feel more useful and are unsupportable. The plan is more valuable without them.

---

# 5. Write the Failure Rows While Writing the Steps

For each step, in the same pass: what can fail, what the user sees, how they recover, and whether
their work survives.

Done as a later pass, the failure table covers the two cases that come to mind rather than the
ones module 08 worked to find.

---

# 6. Count the Steps to First Value, Then Try to Remove One

Count them literally. Then attempt to delete a step and see what breaks.

The exercise usually finds one removable step, and the first removable step is worth more than
most features on the roadmap.

---

# 7. Write the Empty State Before the Populated One

For every screen, describe what it shows with nothing in it, and what action is offered.

Designed in this order, first-run experience is a feature. Designed afterwards, it is a blank
page with a spinner.

---

# 8. Draw Every Design Principle From a Named Finding

Two columns: the principle, and the research finding it came from.

A principle with an empty second column is a platitude, and the two-column format makes that
visible immediately rather than after a review nobody wanted to have.

---

# 9. Read the Plan Backwards From Launch

Start at launch, ask what had to be true before it, and keep going.

One-way doors surface immediately in this direction, because their consequences appear before
their commitment point.

---

# 10. Place the One-Way Doors Explicitly, With Reasoning

Name the milestone in which each irreversible decision is committed, and why there.

Left implicit, they land wherever the dependency graph puts them — which is often too late to be
cheap and too early to be informed.

---

# 11. List the Acceptance Criteria, Do Not Reference Them

Copy the criteria from `08-product` into the definition of done.

"Meets the acceptance criteria" requires the reader to hold two documents open and reconcile
them, which is what a handoff exists to prevent.

---

# 12. Write "Not Done" in the Same Breath as "Done"

Immediately after the criteria: what a reader might assume is finished and is not.

One line, written once, prevents the entire class of dispute where a milestone is complete and
three weeks of work remain.

---

# 13. Make "Stop" an Available Outcome at Every Decision Point

If the outcomes are "continue" and "continue after fixes", it is a status meeting.

A decision point that cannot conclude "stop" does not re-examine the plan; it confirms it.

---

# 14. Build the Coverage Table Before Choosing Test Levels

Requirements down the page, then assign verification. Not the reverse.

Choosing levels first produces a sensible-looking pyramid with requirements missing from it.

---

# 15. Write What Is Not Tested, Deliberately

An explicit exclusion is worth more than an implied claim of full coverage — and it is the only
version of this section that survives a real schedule.

---

# 16. Put Every Undecided Thing in Blocked Work, With a Person's Name

Not "the team". A person, or the operator.

Unowned blocked work is unstarted work nobody is waiting for, which is indistinguishable from
work that was never needed.

---

# 17. Search the Handoff for "As Discussed"

Literally search for it, along with "per the research", "as we agreed", and "the team will
decide".

Every hit is a sentence written for someone who was in the room, in a document for someone who
was not.

---

# 18. Read the Handoff as Someone With No Context, Last

Not a proofread. Stand in the first hour: what is the first thing you type, and what do you have
to decide before you can?

Every decision that surfaces is a defect, and this is the last opportunity to remove it.

---

# 19. Write §1 Last

The one-paragraph summary is only accurate once the milestones exist.

Written first, it becomes the thing the plan is shaped to match.

---

# Anti-Practices

| Habit | Why it fails |
| --- | --- |
| Naming milestones before writing the demo sentence | Layer names come to mind first |
| Re-deriving the first slice | Discards work already done, usually enlarging it |
| Writing durations before asking about the team | The numbers are written and never corrected |
| Reaching for weeks with no team facts | Unsupportable, and treated as commitments |
| Failure tables as a later pass | Covers the obvious cases, not the found ones |
| Populated states first | First-run experience becomes an afterthought |
| Generic design principles | Constrain nothing, survive every review |
| Referencing acceptance criteria | Forces the reader to reconcile two documents |
| Done with no absences | The complete milestone with three weeks left |
| Decision points with no "stop" | Confirmation dressed as re-examination |
| Test levels before coverage | A neat pyramid with requirements missing |
| Implied full coverage | Unobservable and reassuring |
| Blockers owned by "the team" | Unowned means unstarted |
| Assumptions in build instructions | Silent decisions by whoever builds |
| Never reading the handoff cold | Every defect stays in |

---

# Self Assessment

- Did I write the demo sentence before the milestone name?
- Is my first milestone module 08's first shippable slice?
- Did I ask about the team before writing a number?
- Are my sizes relative where team facts are missing?
- Did I write the failure rows alongside the steps?
- Did I try to remove a step from first value?
- Did I write empty states first?
- Does every design principle name its finding?
- Did I read the plan backwards from launch?
- Are the one-way doors placed with reasoning?
- Did I list the acceptance criteria rather than reference them?
- Does every "done" have a "not done"?
- Can every decision point conclude "stop"?
- Did I build the coverage table first?
- Did I state what is not tested?
- Does every blocker have a person's name?
- Did I search for "as discussed"?
- Did I read the handoff cold?

---

> **Practice Principle**
>
> Three practices here are single questions: who is the team,
> what can you demonstrate, and what would you have to decide first.
>
> A plan that answers those three honestly is already better than
> most plans that answer everything else.
