---
Title: Vision
Module: 08-product
Section: knowledge
Category: Concept
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: Keep the vision out of requirements, where it functions as justification for scope.
Audience:
  - AI Agents
  - Product Managers
  - Founders
Prerequisites:
  - 07-strategy/knowledge/Vision.md
Outputs:
  - One-line reference in prd_body
Related Modules:
  - 01-idea
  - 07-strategy
Tags:
  - Product
  - Vision
  - Concept
---

# Vision

---

# What It Is

The destination, inherited from `01-idea` and used as a tiebreaker by `07-strategy`. In this module it has **one
legitimate appearance: a single line of context in the PRD.**

It has no role in a requirement, and the reason is mechanical:

| In a requirement, a vision | Consequence |
| --- | --- |
| Serves as a parent | The trace breaks — parents are ranked problems, not destinations |
| Justifies inclusion | Any capability can be justified this way, individually reasonably |
| Explains a priority | Priority comes from problem rank, reach, confidence and effort |

> A requirement traced to a vision rather than to a ranked problem is an orphan with a justification attached.

And the framework's rule for orphans is that they are **deleted, not justified** — precisely because the justification
is written after the fact and sounds entirely reasonable.

---

# When It Applies

Once, in the PRD's inherited section. Never in Move 1's spine, Move 2's priorities, or Move 5's scoring.

---

# How to Apply It Here

**Quote it and stop.** One line, attributed to `01-idea`. It orients the reader; it decides nothing here.

**Check every requirement's parent is a ranked problem.** That is the spine's job and it is what makes vision-derived
scope detectable. A parent column containing anything other than a problem identifier is a finding.

**Recognize the pattern when it appears.** "This is essential to our vision of…" attached to a capability with no
problem parent is the specific sentence the orphan rule exists to catch.

**Send vision-shaped capabilities to the ledger.** Something consistent with the destination but unattached to a ranked
problem is a future candidate. `Roadmap.md` records it with the reason.

**Leave tiebreaking to module 07.** If two requirements genuinely tie on the scoring factors, the resolution is a
priority question for module 07's cut, not a vision judgment made here.

---

# Where It Misleads

**The vision is the framework's primary scope-creep vector, and this is where it lands.** `01-idea` names it
explicitly; `07-strategy` restricts it to tiebreaking after scoring. By the time it reaches requirements it has no
constraint left except this rule.

**Vision language makes a weak requirement read as strategic.** A capability with no evidence behind it acquires
apparent weight from the sentence around it, and reviewers hesitate to challenge a destination.

**It becomes the answer to "why is this a MUST?"** The answer must be the problem rank and the MVP line. Anything else
means the priority was assigned rather than derived.

**A restated vision drifts.** Each rewriting makes it broader, and a broader destination justifies more. If it needs
restating, it is being used for something.

**It substitutes for the non-goals.** A vision says where this is going; non-goals say what is excluded now. Only the
second is a working boundary during specification.

---

# Related

| | |
| --- | --- |
| `Mission.md` | The present-tense counterpart, also inherited |
| `Product-Strategy.md` | What else is inherited and fixed |
| `features/Feature-Discovery.md` | The spine and the orphan rule |
| `01-idea`, `07-strategy` | Where the vision is written and legitimately used |

---

> **Concept Note**
>
> One line of context, and no requirement traced to it.
>
> A capability justified by the destination is an orphan — and orphans
> are deleted, because their justification always sounds reasonable.
