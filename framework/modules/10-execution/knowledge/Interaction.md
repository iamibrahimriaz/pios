---
Title: Interaction
Module: 10-execution
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Design actions around consequence and reversibility, under the real conditions of use.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 10-execution/knowledge/UX-Principles.md
Outputs:
  - Interaction design within ux_flows
Related Modules:
  - 03-user
  - 14-ai-systems
Tags:
  - Execution
  - UX
  - Concept
---

# Interaction

---

# What It Is

How actions are performed — governed by two properties of the action rather than by convention:

| Reversible? | Consequence | Treatment |
| --- | --- | --- |
| Yes | Low | Do it immediately, offer undo |
| Yes | High | Do it immediately, offer undo prominently |
| **No** | Low | Do it immediately; nothing to protect |
| **No** | High | Confirm — and make the confirmation specific, not a generic dialog |

**Undo beats confirmation** wherever it is available. A confirmation interrupts every use to prevent a rare mistake; undo interrupts
nothing and fixes the mistake when it happens.

The conditions constrain everything: `03-user` recorded whether the user has one hand, is interrupted, is standing, is observed. A
principle derived from those findings — every action survives being abandoned halfway — is an interaction requirement.

---

# When It Applies

In Move 1 (Flow), per action along the critical paths.

---

# How to Apply It Here

**Classify each action by reversibility and consequence.** That table decides confirmation without argument, and it stops confirmations
being added by anxiety.

**Make interrupted actions recoverable.** Where `03-user` found constant interruption, work in progress must persist — which is a
`08-product` requirement and frequently a data-model one.

**Support the keyboard for frequent tasks.** A professional performing a task forty times a day is measurably faster with a keyboard
path, and `Accessibility.md` requires it independently.

**Design AI interactions around detectability.** `14-ai-systems`' rule governs: where the user cannot tell the output is wrong,
autonomy above suggestion needs a visibility mechanism. That mechanism is an interaction design — showing the source, highlighting
uncertainty, requiring a specific confirmation.

**Make destructive actions specific.** Naming what will be deleted, and requiring the name where the consequence is severe, is worth
more than a second generic dialog.

---

# Where It Misleads

**Confirmations are added instead of undo.** They train users to dismiss them, which removes the protection while keeping the friction.

**Interaction is designed for the demo conditions.** Two hands, a mouse, an uninterrupted minute. `03-user` recorded otherwise, and
that is the environment the product actually lives in.

**Novel interactions are introduced without accounting for retraining.** `07-strategy`'s point applies: every convention broken is
retraining, and it is the layer where novelty is most expensive.

**AI suggestions are made too easy to accept.** One-click acceptance of an unverified output is exactly the case where detectability
governs. The friction should be proportional to the cost of a wrong answer being accepted silently.

**Autosave is assumed to be enough.** It protects against loss and not against a wrong action. Undo is a separate mechanism and users
need both.

---

# Related

| | |
| --- | --- |
| `UX-Principles.md` | The findings that constrain interaction |
| `Motion.md` | Feedback for an action's result |
| `Accessibility.md` | Keyboard and input requirements |
| `03-user`, `14-ai-systems` | Conditions, and detectability |

---

> **Concept Note**
>
> Undo beats confirmation wherever it is possible.
>
> A confirmation taxes every use to prevent a rare mistake, and users
> learn to dismiss it — so it stops preventing anything.
