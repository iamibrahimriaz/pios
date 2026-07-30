---
Title: Accessibility
Module: 10-execution
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Build the accessible path into the flow, since it is cheap here and expensive later.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 03-user/knowledge/Accessibility.md
Outputs:
  - Accessible flows within ux_flows
Related Modules:
  - 03-user
  - 08-product
Tags:
  - Execution
  - UX
  - Concept
---

# Accessibility

---

# What It Is

Accessibility as **flow and interaction design** — where `03-user/knowledge/Accessibility.md` established it as a user fact and a
frequent legal obligation, this is where it becomes a route someone can actually take.

What must be designed rather than inherited:

| Element | The decision |
| --- | --- |
| **Keyboard path** | Every critical path completable without a pointer, in a sensible order |
| **Focus order and visibility** | Where focus starts on each screen, where it goes, and that it can be seen |
| **Announcements** | What a screen reader is told when something changes without navigation |
| **Labels and relationships** | Every control named, every field associated with its label |
| **Contrast and target size** | Against `03-user`'s conditions — sunlight, gloves, imprecise touch |
| **Error association** | Which field an error belongs to, conveyed non-visually |

The one most often missed is announcements. A product that updates part of a screen silently is a product where a screen-reader user
does not know anything happened — and `Loading-States.md` and `Error-States.md` both create those moments.

---

# When It Applies

In Move 1 (Flow), designed into the paths rather than reviewed afterwards.

---

# How to Apply It Here

**Walk each critical path with the keyboard only, and record it.** That single exercise finds most problems, and it is the same
discipline `04-problem`'s usability method applies: give a task, offer no help, watch where it stops.

**Specify focus behavior per screen.** Where focus lands on arrival, after a dialog closes, after an error. Unspecified, it resets to
the top and the user retraces the whole page.

**Specify what is announced when content changes.** Every loading, error and empty transition is a change someone cannot see.

**Carry the binding standard's requirements as requirements.** If `02-market` Frame 2 found one, `08-product` should hold the specific
obligations — not the standard's name.

**Use the situational constraints as the practical test.** Gloves, sunlight, one hand, a shared screen. They come from `03-user` and
they improve the product for everyone.

---

# Where It Misleads

**It is scheduled as a late audit.** Retrofitting into a built interface is expensive and partial; designing the keyboard path in
costs almost nothing. The cost difference is the whole argument.

**Conformance is mistaken for usability.** A product can satisfy every checkpoint and remain unusable one-handed in a noisy room. The
standard is a floor and the situational constraints are the real test.

**Automated checks are treated as coverage.** They find missing labels and contrast failures. They cannot tell whether the keyboard path
completes the job, which is the thing that matters.

**Only the happy path is made accessible.** Errors, empty states and loading transitions are where non-visual users lose the thread,
and they are the states most often skipped generally.

**It is scoped out of the MVP quietly.** `03-user` noted this is a `07-strategy` decision with a legal dimension, and it belongs in
the deferral ledger with the obligation named — not omitted.

---

# Related

| | |
| --- | --- |
| `03-user` `Accessibility.md` | The user fact and the obligation |
| `Interaction.md` | Keyboard paths and input methods |
| `Error-States.md`, `Loading-States.md` | The changes that need announcing |
| `Motion.md` | Reduced motion as a requirement |

---

> **Concept Note**
>
> Walk every critical path with the keyboard alone. That one exercise
> finds most of it.
>
> And a screen that changes silently is a screen where nothing happened,
> for anyone who cannot see it.
