---
Title: Motion
Module: 10-execution
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Use motion only where it communicates, and respect the preference to reduce it.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 10-execution/knowledge/Interaction.md
Outputs:
  - Motion decisions within ux_flows
Related Modules:
  - 03-user
Tags:
  - Execution
  - UX
  - Concept
---

# Motion

---

# What It Is

Animation and transition — legitimate only where it **communicates something the static state cannot**.

| Communicates | Duration |
| --- | --- |
| Where something came from or went | ~150–250ms |
| That an action was registered | Immediate, brief |
| The relationship between two states | Short enough not to be waited for |
| That something is in progress | `Loading-States.md`'s territory |
| Nothing — it is decorative | Remove it |

The constraint that decides most cases: for a professional tool used dozens of times a day, **motion is a tax paid on every
repetition.** A 400ms transition is pleasant once and an obstruction the fortieth time.

And an accessibility requirement rather than a preference: where the operating system requests reduced motion, honor it. For some
users motion causes genuine discomfort, and `Accessibility.md` treats this as a requirement.

---

# When It Applies

In Move 1 (Flow), and only where a transition carries meaning. Most flows in a professional tool need very little.

---

# How to Apply It Here

**Justify each motion by what it tells the user.** If the static before-and-after states are unambiguous, the motion is decoration.

**Keep durations short, and shorter for frequent actions.** `03-user`'s frequency finding decides it: a task performed constantly
should have transitions the user never waits for.

**Honor reduced-motion preferences.** A requirement, not an enhancement, and it needs a specified fallback — usually an instant state
change.

**Use it for spatial continuity where the flow moves between contexts.** Showing that a panel came from a row is one of the few cases
where motion genuinely reduces confusion.

**Never make it the only feedback.** An animation is the confirmation nobody sees if they looked away, were interrupted, or have
reduced motion enabled. `Interaction.md` needs a persistent signal too.

---

# Where It Misleads

**Motion is added for polish and taxes every interaction.** It is the clearest case of a consumer convention applied badly to a
professional tool, and `05-competition`'s point about density applies — the trained daily user wants speed.

**Duration is copied from marketing sites.** A landing page rewards a 500ms reveal. A clinical tool does not.

**It is used to conceal slowness.** A transition that fills a wait is `Loading-States.md`'s job done dishonestly, and it makes the
interface feel slower once the user recognizes it.

**Reduced-motion is treated as a niche setting.** It is a documented accessibility need with a real user population, and ignoring it
can be a compliance issue where a standard applies.

**Motion carries information alone.** Anything conveyed only by movement is invisible to a user who was interrupted — which
`03-user` said is constantly.

---

# Related

| | |
| --- | --- |
| `Interaction.md` | Feedback that persists |
| `Loading-States.md` | Indicating progress honestly |
| `Accessibility.md` | Reduced motion as a requirement |
| `03-user` | Frequency, and the conditions of use |

---

> **Concept Note**
>
> Motion is a tax paid on every repetition.
>
> Pleasant once, an obstruction the fortieth time — and invisible to
> anyone who looked away.
