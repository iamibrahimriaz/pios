---
Title: Reflection
Module: 09-technology
Section: learn
Category: Foundation
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Prompt a learner to examine what their technical choices were actually optimizing for.
Audience:
  - Product Managers
  - Founders
  - Engineers
Prerequisites:
  - 09-technology/learn/16-Evaluation.md
Outputs:
  - Examined assumptions about your own design habits
Related Modules:
  - 06-business
  - 13-operations
Tags:
  - Technology
  - Reflection
  - Learn
---

# Reflection

---

# Overview

Technical decisions are made by people with preferences, career interests and habits.
These questions are about which of those were operating.

---

# On the Architecture

**What are you actually optimizing for?** Scale, cost, familiarity, speed of build, or
what would look right to another engineer. All five are legitimate except the last, and
the last is more common than anyone admits.

**Which component would you remove if someone made you?** There is usually one you would
give up without much resistance. That is the inflation.

**What does this cost to operate, in a person's hours per month?** Module 13 will ask.
Answering now sometimes removes a component immediately.

---

# On the Data Model

**Which constraint did you leave to the application?** And what happens the first time
something other than the application writes?

**What did you make nullable because you were not sure?** Nullable-because-undecided is a
decision to handle the null case in every consumer, forever.

**What happens when a user asks you to delete everything about them?** Follow it through
every store, including backups and derived data. Most models fail this and most documents
do not say so.

---

# On the Obligations

**Which one has no mechanism?** Check the list from module 02 against the mechanisms
here. A gap is normal at first pass; leaving the gap unmarked is not.

**Did you record anything as a risk that is actually a blocker?** The distinction is
whether a mechanism exists that satisfies it. Risks get managed; blockers get resolved,
and softening one into the other buys time at a bad exchange rate.

**Who will run each mechanism?** If the honest answer is "the same person, for all
eleven," that is a finding about the whole design.

---

# On the Cost

**Did you compute at launch scale or at the scale that made it look reasonable?**

**What is the dominant line?** For most products it is not what people expect. For
service-delivered products it is human time, which does not appear in an infrastructure
estimate at all.

**What would you do if it exceeded the ceiling?** Decide now. Afterwards, the answer
becomes "it will come down with scale," which is the absorption the check exists to
prevent.

---

# On the Stack

**Would you choose this if you had to operate it alone at 3am?** Different question from
whether it is the best technology, and more predictive of how the next year goes.

**What are you choosing because you want to learn it?** Sometimes a legitimate reason —
say so explicitly rather than dressing it in performance claims.

---

# On Your Own Pattern

| Look for | What it suggests |
| --- | --- |
| Your architectures always have more components than the problem needs | You design for the scale you hope for |
| Your security sections describe posture | Mechanisms are being deferred to implementation |
| Your costs are always computed at scale | The arithmetic is being chosen |
| You have never recorded a blocker | Conflicts are being softened into risks |
| Your stack is always what you used last | Familiarity is fine; state it as the reason |

---

# The Question Worth Returning To

> If this product has exactly the number of customers it has today for the next two
> years, what would you build differently?

The gap between that answer and your current design is the inflation, measured. For most
products it is large, and closing it is the single cheapest thing available in this
module — it reduces build time, operational surface, and cost per user at once.

---

> **Reflection Principle**
>
> The architecture you would be proud to show another engineer and the architecture one
> person can run are rarely the same design.
>
> Knowing which one you produced is the reflection that matters here.
