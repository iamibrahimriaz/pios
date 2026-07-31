---
Title: Mental Models
Module: 10-execution
Section: core
Category: Thinking Framework
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Define the lenses through which an execution plan should be examined.
Audience:
  - AI Agents
  - Delivery Leads
  - Founders
Prerequisites:
  - 10-execution/core/03-Core-Principles.md
Outputs:
  - Multi-perspective examination of the plan
Related Modules:
  - 12-metrics
Tags:
  - Execution
  - ../constitution/core/04-Mental-Models.md
---

# Mental Models

---

# Model Statement

> A plan is judged by what happens on the first morning.
>
> These lenses are ways of standing in that morning while there is
> still time to change it.

---

# 1. The Demo Test

**Reveals:** layers disguised as milestones.

For each milestone, answer in writing: what can you show a real user doing when this is done?

If the answer names a component, it is a stage. If it names a person completing an action, it is
a milestone.

**Hides:** a demonstrable milestone can still be the wrong one to build first. The test is about
shape, not priority.

---

# 2. The Stopping Test

**Reveals:** milestones that are actually dependencies.

Ask, per milestone: if delivery stopped here, would anything usable exist?

Not complete — usable. A milestone that fails this belongs inside another one, not beside it.

**Hides:** some genuinely necessary work leaves nothing usable. That work is fine; it just is
not its own milestone.

---

# 3. The First Morning

**Reveals:** everything the plan assumes about its reader.

Stand in the first hour of work with no context, no meeting, and only the handoff. What is the
first thing you type? What do you have to decide before you can?

Every decision that surfaces is a defect in the plan.

**Hides:** it optimizes for starting. A plan can be startable and still head somewhere wrong.

---

# 4. The Route, Not the Requirements

**Reveals:** holes in the user's experience.

Requirements are a set. A user walks a sequence. Read the flow as a walk: arrive, act, wait,
succeed, fail, recover, return.

The gaps show up in the transitions, which is exactly where requirement lists have nothing to
say.

**Hides:** it covers the primary path. Secondary personas and alternate routes need their own
walks.

---

# 5. The Interruption

**Reveals:** designs that assume uninterrupted attention.

Take the persona's real context from `03-user` and interrupt them at each step. What survives?
What is lost? Where do they resume?

Most real users are interrupted, and most flows are designed by someone who was not.

**Hides:** it is one context constraint among several — connectivity, shared devices, time
pressure and physical environment each deserve the same treatment.

---

# 6. The First Five Minutes

**Reveals:** whether the product will be adopted.

Time to first value, counted in steps and minutes, from arrival to the moment the user has
something they actually wanted.

It predicts adoption better than any feature comparison, and it cannot be improved while it is
unmeasured.

**Hides:** it says nothing about retention. A fast first value can precede an empty second
week.

---

# 7. The Empty Product

**Reveals:** the state every user starts in and no design covers.

Read every screen with no data in it. What does the user see? What are they told to do? Is there
a path out?

The populated state is the one designers work in and the one users see least at the beginning.

**Hides:** it focuses on first use. Emptiness recurs — a filter with no matches, a deleted
history, a new team member.

---

# 8. Backwards From Launch

**Reveals:** sequencing errors, particularly around irreversible decisions.

Start at launch and walk backwards. What had to be true before that? And before that?

One-way doors surface immediately when read in this direction, because their consequences are
visible before their commitment point.

**Hides:** it can produce a plan optimized for launch rather than for learning, which is the
wrong optimization when the problem is still assumed.

---

# 9. The Two Readers

**Reveals:** definitions of done that are not definitions.

For each milestone, imagine two people who both want it finished — one who wants to move on, one
who wants it solid. Could they disagree about whether it is done?

If they could, the definition is a description.

**Hides:** agreement does not mean the bar is high enough. Both readers might be satisfied by
too little.

---

# 10. The Estimate With No Team

**Reveals:** fabricated confidence.

Read every duration in the plan and ask who is doing the work. If the answer is not written down
somewhere, the number came from nowhere.

**Hides:** nothing. It is mechanical, and it catches the module's most tempting failure.

---

# 11. The Silent Guess

**Reveals:** assumptions that will be resolved by whoever is building.

Read the build instructions looking for anything undecided. Each one will be settled quietly, by
someone who does not know it was open, and never mentioned again.

Everything found belongs in Blocked Work, with a name against it.

**Hides:** it does not detect decisions the plan made wrongly but confidently. That is the
review loop's job.

---

# 12. The Test That Never Runs

**Reveals:** verification that exists on paper.

For each MUST requirement, name the check that would fail if it broke. Then ask when that check
actually runs.

An edge case specified in three documents and verified nowhere is an edge case the product does
not handle.

**Hides:** a running test can still assert the wrong thing.

---

# Combining Models

| Situation | Model |
| --- | --- |
| Checking milestone shape | The Demo Test |
| Checking milestone independence | The Stopping Test |
| Checking the handoff | The First Morning |
| Checking the user's experience | The Route, Not the Requirements |
| Checking against real conditions | The Interruption |
| Checking adoption | The First Five Minutes |
| Checking initial states | The Empty Product |
| Checking sequence | Backwards From Launch |
| Checking definitions of done | The Two Readers |
| Checking estimates | The Estimate With No Team |
| Checking honesty | The Silent Guess |
| Checking verification | The Test That Never Runs |

Apply The Route and The Interruption while writing the flows. Apply The First Morning, The Silent
Guess and The Estimate With No Team last, on the finished plan.

---

# Self Assessment

- Does every milestone name a person doing something?
- Could delivery stop anywhere and leave something usable?
- What would I have to decide before typing the first line?
- Where does the user's route have a gap?
- What survives an interruption at each step?
- How many minutes to first value?
- What does the product look like with nothing in it?
- Read backwards, are the one-way doors early enough?
- Could two readers disagree about any "done"?
- Who is doing the work behind each duration?
- What will be guessed at silently?
- Which verification never actually runs?

---

> **Mental Model Principle**
>
> The First Morning is the only lens that matters if you have time
> for one.
>
> Everything the plan gets wrong shows up in the first hour of
> somebody trying to use it.
