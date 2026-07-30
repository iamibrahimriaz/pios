---
Title: Product Strategy
Module: 08-product
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: State what this module inherits from module 07 and must not re-decide.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 07-strategy/knowledge/MVP.md
Outputs:
  - Inherited strategy section of prd_body
Related Modules:
  - 07-strategy
Tags:
  - Product
  - Strategy
  - Concept
---

# Product Strategy

---

# What It Is

The strategy this module operates inside — decided by `07-strategy`, approved by the operator at the human checkpoint,
and **binding here**.

> Module 07 decided what to build. This module makes that decision unambiguous.
>
> Nothing new is chosen here. Something already chosen is made precise.

What is inherited and fixed:

| Inherited | Consequence for this module |
| --- | --- |
| The chosen approach | Requirements express it; they do not reconsider it |
| The MVP line | MUST is reserved for what sits above it |
| The non-goals | An excluded capability stays excluded, ledger or not |
| The ranked problems | Every requirement traces to one |
| The bet, and its evidence standing | Carried into the PRD with its tag |
| Stop conditions and reversal triggers | Referenced, not renegotiated |

---

# When It Applies

Before Move 1, and as the reference for every boundary judgment in Moves 2 and 5.

---

# How to Apply It Here

**Restate the strategy in one short section and move on.** The proposal, the cut, the non-goals. Enough that a reader
knows the frame; not enough to reopen it.

**Treat the cut as an external constraint.** The correct response to a cut that appears wrong is a recorded regress to
`07-strategy`, not an adjustment here. That regress is a legitimate and expected event when the end-to-end test fails.

**Carry the bet forward with its tag.** If the sharpest problem is assumed, the PRD says so and `10-execution` will
require Milestone Zero. A confident restatement of an assumed premise is how the tag gets lost.

**Use the non-goals as a working boundary check.** When a capability suggests itself during specification, check the
non-goal list first. It exists to settle that argument once.

**Reference the reversal trigger rather than re-deriving it.** If evidence arrives that should change the strategy, the
trigger is already written and the path is back to module 07.

---

# Where It Misleads

**Strategy gets re-derived in the PRD because it reads as context-setting.** Re-arguing an approved decision invites it
to be reopened in a document with no authority to change it, and by readers who were not at the checkpoint.

**The cut is treated as a starting point rather than a boundary.** This is scope laundering's origin: the line becomes
negotiable during specification, and the approved cut is no longer the cut being built.

**Non-goals are forgotten because they are absences.** Nothing in the requirement list reminds you of them. Checking
them explicitly is the only mechanism, which is why module 07 wrote them down.

**Inherited confidence is upgraded silently.** An `[assumption]` becomes an assertion through nothing more than being
restated in a new document, in different words, by someone who now takes it for granted.

**Strategic reasoning substitutes for specification.** A PRD strong on why and weak on exactly-what fails the
two-builder test, which is the only standard this module is actually judged against.

---

# Related

| | |
| --- | --- |
| `Vision.md`, `Mission.md` | Other inherited framing, similarly not re-decided |
| `Requirements.md` | Where the cut is enforced as MUST discipline |
| `Roadmap.md` | Where below-line items are recorded |
| `07-strategy` | The source, and the destination of a regress |

---

> **Concept Note**
>
> The cut is a constraint, not a starting point.
>
> If it is wrong, regress to module 07 and record it — do not fix it
> quietly while specifying.
