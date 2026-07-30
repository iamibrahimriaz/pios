---
Title: User Flows
Module: 10-execution
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Map two or three critical paths end to end, including what can fail.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 10-execution/core/06-Framework.md
Outputs:
  - ux_flows
Related Modules:
  - 03-user
  - 08-product
Tags:
  - Execution
  - UX
  - Method
---

# User Flows

---

# What It Is

The route the user actually walks — because requirements are not a route.

> A user does not experience a requirement list; they experience a sequence of screens and states, and products are lost in the
> parts of that sequence nobody specified.

**Two or three critical paths only.** The flows that carry the product. Mapping every path produces a document nobody reads and
hides the two that matter.

| Per path | |
| --- | --- |
| Trigger | What starts it |
| Each step | What the user sees, what they do, what the system does |
| What can fail | And what recovery looks like from the user's side |

And a number the framework treats as predictive:

> **Time to first value.** From arrival to the moment the user gets something they actually wanted, in steps and in minutes. It
> predicts adoption better than any feature comparison, and it cannot be improved without being measured.

---

# When It Applies

In Move 1 (Flow), first — before slicing, because milestones cut across flows and a milestone drawn without them misses whole parts
of the route.

---

# How to Apply It Here

**Take the paths from `03-user`'s job, not from the requirement list.** The core job is the first path. `08-product`'s spine already
mapped requirements to job steps.

**Build the failure and recovery table.** Module 08 found the edge cases; this is where they become something a person experiences
rather than a status code. That translation is the main work of this move.

**Count the steps to first value and write the number down.** Then look at what could be removed. Onboarding, configuration and
sign-up steps all sit between arrival and value.

**Compare the step count to the status quo.** `05-competition`'s point applies: if the incumbent process takes four steps and this
takes six, interface quality is irrelevant.

**Map the hand-off if a second person is involved.** `03-user` identified them, and hand-offs are where flows break silently — the
first person finishes and nothing tells the second.

---

# Where It Misleads

**Every path gets mapped, and the important ones disappear into the volume.** Two or three is the instruction; completeness here is
a cost with no benefit.

**Flows are drawn as the happy path only.** The failure branches are where the product is judged, and they are already specified in
`08-product` — omitting them here loses work already done.

**The flow becomes a design.** Screens and layout are design's output, derived from these. A flow that specifies layout has closed a
decision it does not need to make.

**Time to first value is not measured because it seems obvious.** It is routinely three times longer than assumed once sign-up,
setup and empty states are counted.

**The idealized route is documented.** `03-user`'s conditions apply: interrupted, one-handed, someone waiting. A flow that only works
uninterrupted describes a demo.

---

# Related

| | |
| --- | --- |
| `UX-Principles.md` | Principles that must derive from findings |
| `Empty-States.md`, `Error-States.md`, `Loading-States.md` | The states every screen needs |
| `Information-Architecture.md` | Where things live along the route |
| `03-user`, `08-product` | The job, and the edge cases |

---

> **Concept Note**
>
> Two or three paths, each with its failures, and one number: steps to
> first value.
>
> Requirements describe what exists. A flow describes what someone
> walks through — and that is where products are lost.
