---
Title: Onboarding
Module: 11-growth
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Design the shortest path to the activation event, and remove steps rather than explain them.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 11-growth/knowledge/Activation.md
Outputs:
  - onboarding_strategy
Related Modules:
  - 10-execution
  - 13-operations
Tags:
  - Growth
  - Onboarding
  - Concept
---

# Onboarding

---

# What It Is

The path from arrival to the activation event — and the framework's position is that the work is **removing steps, not explaining
them.**

| Approach | Effect |
| --- | --- |
| **Remove the step** | Best. Nothing to explain, nothing to abandon |
| **Defer the step** | Ask for it when it is needed, not before |
| **Pre-fill the step** | From data already available |
| Explain the step | A tour, a tooltip, a video — the weakest option, and the most commonly chosen |

The measure is `10-execution`'s step count to first value. Every step between arrival and activation is a place users leave, and the
steps that most often exist without needing to are configuration, invitations and profile completion.

For institutional products, onboarding is also **someone's work**: data migration, account setup and training. That is
`06-business`'s onboarding cost and `13-operations`' load, and it must be priced rather than absorbed.

---

# When It Applies

In Move 3 (Activate), producing `onboarding_strategy`.

---

# How to Apply It Here

**List every step and justify each one.** The question per step is whether activation is possible without it. Most survive scrutiny
badly.

**Design the empty state as onboarding.** `10-execution/knowledge/Empty-States.md` makes the point: a well-designed first-use state
frequently removes the need for a tour entirely.

**Defer everything not required for the first successful use.** Team invitations, preferences and integrations can wait until the user
has a reason to want them.

**Say who does the work when it is manual.** Migration and setup performed by the operator is a named cost with a named person.
`13-operations`' rule applies: "the team" is not an owner.

**Measure abandonment per step.** `12-metrics` defines the events; the drop-off between them is the most actionable data an early
product has.

---

# Where It Misleads

**A tour is built instead of a shorter path.** Explanation is easier to add than steps are to remove, so it is what gets added — and it
adds a step of its own.

**Onboarding is designed for the complete product.** The MVP has one path. Introducing capabilities that do not exist yet, or are below
the line, wastes the user's attention on absent features.

**Configuration is required up front.** Asking a professional to configure something before they have seen value is asking them to
invest in an unproven tool.

**Manual onboarding is treated as temporary.** It frequently persists, and it caps growth at whatever the operator can perform. That is
a real constraint on the growth model, and `06-business/knowledge/GTM.md` names the same ceiling.

**Completion of onboarding is reported as activation.** Finishing a tour proves nothing about value received, and
`Activation.md` requires the event to prove value.

---

# Related

| | |
| --- | --- |
| `Activation.md` | The destination |
| `Retention.md` | What must exist by the time onboarding ends |
| `10-execution` | Empty states, and the step count |
| `06-business`, `13-operations` | Onboarding as a priced cost |

---

> **Concept Note**
>
> Remove the step, defer it, or pre-fill it. Explaining it is the last
> resort and the usual choice.
>
> A tour is a step added to explain the steps you did not remove.
