---
Title: Loading States
Module: 10-execution
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Make waiting honest, and match the indication to how long it will actually take.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 10-execution/knowledge/Wireframes.md
Outputs:
  - Loading states within ux_flows
Related Modules:
  - 09-technology
  - 14-ai-systems
Tags:
  - Execution
  - UX
  - Concept
---

# Loading States

---

# What It Is

What the user sees while something is happening — matched to the duration, which `09-technology/knowledge/Performance.md` already
budgeted.

| Duration | Appropriate indication |
| --- | --- |
| Under ~300ms | Nothing. An indicator that flashes is worse than none |
| Under a second | An inline indicator on the element being acted upon |
| A few seconds | A clear indicator, and the interface stays usable if possible |
| Longer than the interaction budget | Acknowledge and continue elsewhere — `09-technology/knowledge/architecture/Queues.md` |
| Unknown or variable | Say what is happening, not how long is left |

Two AI-specific cases matter, because inference is slow and variable:

- **Streaming output** turns a long wait into an immediate one, and is frequently the correct answer.
- **Background drafting** — acknowledging, then presenting the result later — is the alternative when latency exceeds the budget
  entirely.

---

# When It Applies

In Move 1 (Flow), per screen and per action, informed by the performance budget.

---

# How to Apply It Here

**Take the duration from the performance target.** `09-technology` derived it from how much time the user actually has. The indication
follows from the number.

**Never block the whole screen for a partial operation.** If one section is loading, that section indicates it. A full-screen block for
a component's refresh is a much larger interruption than the work warrants.

**Preserve what the user typed.** Losing input to a loading transition is a trust failure, and `08-product`'s invalid-input category
already required preservation.

**Prefer optimistic acknowledgment where the operation is reliable and reversible.** Show it as done, reconcile behind. Where it is
neither, do not — an optimistic state that rolls back is worse than a brief wait.

**Say what is happening for anything genuinely slow.** "Drafting the note" is informative; a spinner is not. For AI features this
also sets the expectation that the output will need review.

---

# Where It Misleads

**A spinner is used for every duration.** For 200ms it is a flicker; for 30 seconds it is indistinguishable from a hang, and the user
reloads — frequently duplicating the operation.

**Loading is designed on a fast connection.** `03-user` recorded the real connectivity. The state that matters is the one on the
network the user actually has.

**Progress is faked.** A bar that advances on a timer and stalls at 90% is worse than an honest indeterminate indicator, because it
makes the next wait untrustworthy.

**The timeout case is not designed.** What the user sees when it never completes is `Error-States.md`'s, and it needs to exist —
`08-product`'s failure category specified it.

**Perceived speed is ignored as a lever.** Acknowledging instantly and completing in the background frequently beats optimizing the
operation, and it is a design decision rather than an engineering one.

---

# Related

| | |
| --- | --- |
| `Error-States.md` | Where a wait that fails ends up |
| `Empty-States.md` | Distinguishing loading from empty |
| `09-technology` `Performance.md` | The budget the indication follows |
| `14-ai-systems` | Streaming and background drafting |

---

> **Concept Note**
>
> Match the indication to the duration, and never fake progress.
>
> A spinner at 30 seconds looks exactly like a hang — and the user's
> response is to reload and do it twice.
