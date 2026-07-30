---
Title: Microcopy
Module: 10-execution
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Write the words in the user's vocabulary, and make buttons name their consequence.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 10-execution/knowledge/Information-Architecture.md
Outputs:
  - Copy within ux_flows
Related Modules:
  - 03-user
  - 13-operations
Tags:
  - Execution
  - UX
  - Concept
---

# Microcopy

---

# What It Is

The words in the interface — labels, buttons, hints, confirmations, errors, empty states.

Two rules carry most of the value:

| Rule | Why |
| --- | --- |
| **Use the practitioners' vocabulary** | From `03-user`. A product that renames the domain makes every user translate |
| **A button names its consequence** | "Save note" tells you what happens; "Submit" and "OK" do not |

The second rule matters most in confirmations. A dialog with "Are you sure?" and buttons labeled OK and Cancel requires the user to
remember which action they triggered. Buttons labeled "Delete the appointment" and "Keep it" do not.

Microcopy is also where `13-operations`' support load is created or avoided. A label that is guessed wrong once is a ticket; guessed
wrong by everyone, it is a recurring cost in the true cost to serve.

---

# When It Applies

In Move 1 (Flow), alongside the states — every empty, error and loading state is mostly copy.

---

# How to Apply It Here

**Take terms from `03-user` verbatim.** Where the internal term differs, the interface uses theirs and the difference stays internal.
`09-technology/knowledge/architecture/DDD.md` makes the same point about the model.

**Label buttons with verbs and objects.** The consequence, in the user's words. This single change removes a large share of
misclicks and confirmation confusion.

**Write the error copy from `Error-States.md`'s three questions.** What happened, whether their work survived, what to do next — in
plain language, without the technical cause.

**Say the specific thing rather than the reassuring thing.** `08-product` bans aspirational vocabulary from criteria for the same
reason: "successfully processed" says less than "sent to Dr Patel".

**Keep it short enough to be read.** Professional users scan. A three-line explanation in a busy interface is not read, and its
absence would not be noticed.

---

# Where It Misleads

**Copy is treated as a finishing task.** It is the interface for most practical purposes — the user reads labels, not layouts — and
placeholder wording ships more often than placeholder design.

**Internal or technical vocabulary reaches the surface.** Entity names, status enumerations and team shorthand each force the user to
learn something that serves them not at all.

**Tone is prioritized over clarity.** Playful copy in a clinical or financial context reads as unserious, and in an error state it reads
as evasive.

**Generic dialog buttons are used for destructive actions.** OK and Cancel put the burden of recall on someone who is already
distracted, which is exactly when destructive mistakes happen.

**Copy is written by whoever builds the screen, inconsistently.** Three words for the same concept across three screens is the most
common source of avoidable confusion, and `Information-Architecture.md`'s vocabulary decision is what prevents it.

---

# Related

| | |
| --- | --- |
| `Error-States.md`, `Empty-States.md` | Mostly copy |
| `Information-Architecture.md` | The vocabulary decision |
| `Interaction.md` | Confirmations and their labels |
| `03-user`, `13-operations` | The words, and the support cost |

---

> **Concept Note**
>
> Buttons name their consequence. "Delete the appointment" and
> "Keep it" beat OK and Cancel every time.
>
> The user reads labels, not layouts — copy is the interface.
