---
Title: User Journey
Module: 03-user
Section: knowledge
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Document what happens today, step by step, and find the friction between steps.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 03-user/knowledge/Personas.md
Outputs:
  - current_workflow
Related Modules:
  - 08-product
  - 10-execution
Tags:
  - User
  - Journey
  - Method
---

# User Journey

---

# What It Is

A step-by-step record of what the person does **today**, with the tools named — before this product
exists.

It is the current-state journey, not a designed future one. `10-execution` designs the future flows;
this module's job is to establish the baseline any new product has to beat.

| Per step | |
| --- | --- |
| **What they do** | The action, in their words where possible |
| **Which tool** | Named. "A spreadsheet" and "the practice system" are different findings |
| **How long** | Even roughly, tagged |
| **What is annoying** | The friction, stated as they would state it |

---

# When It Applies

In Move 4 (Observe) — **before** Move 5 (Job). The order is deliberate: what people do is evidence,
what they are trying to achieve is interpretation, and interpreting first produces a job statement
describing the product you already wanted to build.

---

# How to Apply It Here

**Look between the steps, not at them.** This move produces more product insight than any other in
the module, and almost all of it sits in the transitions: the re-typing, the copy-paste, the waiting
for someone else, the checking that the last step worked. Steps get automated; transitions get
eliminated, which is worth more.

**Name every tool, including the human ones.** A colleague, a paper form and a memory are all tools
in the current workflow. Products that ignore them replace software and leave the actual work in
place.

**Record the workarounds.** A workaround is the strongest evidence in the framework — someone paying
a cost repeatedly to get an outcome. `04-problem` builds its verified-problem case largely from
these.

**Include the unhappy path.** What happens when the step fails, the data is wrong, or the person is
interrupted? Those branches become `08-product`'s edge categories, and they are where installed tools
usually earn their loyalty.

**Stop at the boundary of the job.** A journey extended into everything the person does all day
becomes unusable. Bound it by the job under examination.

**Then price leaving it.** Move 4's second output is `switching_cost`, and the journey is what makes it
calculable — across data migration, retraining, workflow disruption, contractual lock-in and perceived
risk. It is the most underestimated number in product work: a better tool costing two weeks of
disruption loses to a worse tool already installed. State the bar this product must clear to be worth
the switch, and hand that bar to `07-strategy`.

---

# Where It Misleads

**Journeys get drawn as the idealized process rather than the observed one.** Published procedures
describe what should happen. The gap between the documented process and the actual one is frequently
the opportunity, and it is invisible if the documented version is copied down.

**An inferred journey looks identical to an observed one.** If no user was spoken to, the artifact is
`[inferred: basis]` throughout and should say so — otherwise `08-product` will build requirements
against a process nobody performs.

**Smooth journeys are a signal of shallow observation.** Real workflows contain dead ends,
duplication and steps whose only purpose is to satisfy someone else. A five-step journey with no
friction has usually been summarized rather than recorded.

**The journey can quietly become a design.** Once the current state is written, it is tempting to
annotate it with fixes. Keep those out — they pre-empt `07-strategy`'s scope decision and
`08-product`'s requirements.

---

# Related

| | |
| --- | --- |
| `Behaviors.md` | Observation before interpretation |
| `Pain-Points.md` | The friction, extracted and rated |
| `Jobs-To-Be-Done.md` | What this journey is in service of |
| `10-execution` | Where the future-state flow is designed |

---

> **Concept Note**
>
> Document the process that happens, not the one that is published.
>
> The opportunity is in the friction between the steps — which is
> exactly what a tidy diagram removes.
