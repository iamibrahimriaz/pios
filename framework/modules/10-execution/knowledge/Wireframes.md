---
Title: Wireframes
Module: 10-execution
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Use low-fidelity layout to settle structure, and specify every state rather than one.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 10-execution/knowledge/Information-Architecture.md
Outputs:
  - Screen definitions within ux_flows
Related Modules:
  - 08-product
Tags:
  - Execution
  - UX
  - Concept
---

# Wireframes

---

# What It Is

Low-fidelity screen layouts — enough to settle what is on a screen and how it is arranged, without settling how it looks.

The framework's requirement about them is specific:

> **Every screen needs its unpopulated states.** Empty, loading, error, permission. A screen specified only in its populated state
> ships broken, because the populated state is the one that occurs least often at the beginning.

| Per screen | |
| --- | --- |
| What is on it, and its priority | The one thing the user came for, first |
| What the primary action is | Exactly one per screen, ideally |
| Its four unpopulated states | Each specified, not implied |
| Which flow steps it serves | The trace back to `User-Flows.md` |
| What it does at the real size and conditions | `03-user`'s device and environment |

Deliberate low fidelity is the point: rough artifacts get honest reactions, and `04-problem`'s prototype guidance says why —
polished ones get compliments or critiques of the polish.

---

# When It Applies

In Move 1 (Flow), after the paths and the structure. They are inputs to design, not design itself.

---

# How to Apply It Here

**Draw the empty state first.** It is every user's first experience and the most commonly unspecified screen in software.
`Empty-States.md` covers what it must do.

**Name one primary action per screen.** More than one means the screen has not decided what it is for, and the user has to.

**Show real content lengths.** Placeholder text of uniform length hides the layout problem. Names, notes and lists in a professional
tool are long, inconsistent and occasionally empty.

**Check against the real conditions.** `03-user` recorded the device, the light, the free hand. A layout that works at a desk and
fails standing has been checked against the wrong thing.

**Trace each screen to flow steps.** A screen serving no step in a critical path is either supporting a non-critical path or is an
orphan, and the same discipline `08-product` applies to requirements applies here.

---

# Where It Misleads

**Only the populated state is drawn.** The result ships with a blank screen on first use, no loading indication, and an error state
nobody designed — which is most of what an early user actually sees.

**Fidelity rises and the conversation changes.** Once it looks finished, feedback becomes about colors and the structural question
goes unasked.

**Wireframes become the specification.** `08-product`'s behavior is the specification; these are one way of expressing part of it. A
wireframe cannot carry validation rules or edge behavior.

**Perfect placeholder data is used.** Short names, tidy lists, no missing fields. Real data breaks layouts, and it does so on the
first customer.

**Screens are drawn for the full product.** Only the MVP's screens matter now, and drawing the rest is effort below the line.

---

# Related

| | |
| --- | --- |
| `Empty-States.md`, `Loading-States.md`, `Error-States.md` | The states each screen needs |
| `Information-Architecture.md` | What belongs where |
| `Interaction.md` | How the primary action behaves |
| `08-product` | The behavior wireframes express |

---

> **Concept Note**
>
> Draw the empty state first — it is what every user sees before any
> other.
>
> A screen specified only when full ships broken, because full is the
> rarest state at the beginning.
