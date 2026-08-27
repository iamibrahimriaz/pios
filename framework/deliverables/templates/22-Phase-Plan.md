# Phase Plan — «Project Name»

<!-- fill: This template produces a DIRECTORY, not a file: `projects/<slug>/phases/`.

     Part A below is `phases/README.md` — the board.
     Part B is one `phase-NN-<slug>.md` per milestone.

     Method: framework/engine/phases.md. Read it before writing either part; it carries the
     boundary this artifact is most likely to cross.

     EVERYTHING HERE IS DERIVED. Every milestone, every definition of done, every gate is
     already in deliverables/04-delivery/09-Roadmap.md. This artifact selects and arranges;
     it never establishes. If you need a fact the roadmap does not carry, that is a finding —
     write that it is not established, and do not compute it here. -->

---

# PART A — `phases/README.md`

<!-- fill: The board. Someone opens the run folder, reads this one screen, and knows what is
     being built, in what order, and what they may start. Nothing else in the folder has that
     job. -->

# Build Phases — «Project Name»

**Verdict:** «the run's recommendation, in the Executive Summary's words, unchanged»
**Confidence:** «high | medium | low»
**Current phase:** «phase-NN — or NONE, and why»

<!-- fill: WHERE THE VERDICT DOES NOT SUPPORT BUILDING, that is the first line on this page
     and no build phase is marked current. A board that lists eight ready phases under a
     "do not build yet" verdict will be acted on as an eight-phase plan, and the verdict will
     be read as commentary. -->

---

## Before anything on this board

<!-- fill: Delete this section only if there is genuinely nothing gating phase 01. Where a
     Milestone Zero exists it is phase-00 and it is named here, with what it decides. -->

«What must be true before the first build phase may start, and where it is specified»

---

## The board

| Phase | Name | Status | Gated behind | Definition of done | Specified in |
| --- | --- | --- | --- | --- | --- |
| 00 | «Milestone Zero, if present» | «done / current / blocked / not started» | «—» | «short form; the full text is in the phase document» | `milestone-zero/` |
| 01 | «name» | «status» | «phase-00» | «short form» | `deliverables/02-product/04-Feature-Spec.md` |

**Exactly one phase is `current`, and it is the first one not done.** If none can be, say
which condition is unmet rather than promoting the next phase.

---

## What is NOT on this board

<!-- fill: Post-MVP scope the roadmap carried forward, and anything the feature spec cut.
     This is the section that stops the board being read as the whole product. -->

| Deferred | Why | Where it is recorded |
| --- | --- | --- |
| «capability» | «reason from 09-Roadmap.md or 04-Feature-Spec.md» | «path» |

---

## How to use this folder

1. Read the phase document for the current phase. Only that one.
2. Its "Specified in" paths are the documents to work from — they are the specification;
   this folder is an index over it.
3. When a phase's acceptance test passes, mark it done here and move `current` forward.
4. **Do not edit the deliverables.** If one is wrong, say so; the run's record of what it
   believed is what makes the output auditable.

---

# PART B — `phases/phase-NN-«slug».md`

<!-- fill: One per milestone in state.outputs.roadmap.milestones. No more and no fewer —
     a phase with no milestone behind it is scope the roadmap never authorized, and a
     milestone with no phase is work that quietly left the plan. -->

# Phase «NN» — «Milestone name»

**Status:** «done | current | blocked | not started»
**Gated behind:** «phase-NN, or nothing»
**Milestone id:** «id, as recorded in state.outputs.roadmap.milestones»

---

## What this phase delivers

«One paragraph. What exists at the end of this phase that did not exist at the start,
described as a capability rather than as a list of tasks.»

---

## What is deliberately NOT in this phase

<!-- fill: Equal weight to the section above. A phase that states only what is in it grows
     during implementation, because nothing on the page says where its edge is. Each
     exclusion carries its reason and where it went instead. -->

| Not in this phase | Why | Where it went |
| --- | --- | --- |
| «capability» | «reason» | «phase-NN, or deferred — with the document that records it» |

---

## Definition of done

<!-- fill: The SAME conditions, in the same shape, as this milestone's "Definition of done" in
     09-Roadmap.md — one checkbox per condition, copied word for word. Do not merge three
     conditions into a sentence and do not split one into two; the validator compares them
     condition by condition, and a merge reads as a softening because the weakest one
     disappears into the prose. -->

- [ ] «condition, copied verbatim from 09-Roadmap.md»
- [ ] «condition, copied verbatim from 09-Roadmap.md»

**Source:** `deliverables/04-delivery/09-Roadmap.md`, milestone «id»

<!-- fill: If the roadmap's definition of done looks wrong or incomplete while you are
     copying it, copy it anyway and record the objection under "Open questions" below. The
     definition was written when the milestone was designed; this document is written after,
     which is the moment it is easiest to adjust toward whatever is convenient now. -->

---

## End-to-end acceptance test

<!-- fill: One test, executable, that demonstrates the whole phase rather than a unit of it.
     Written so that someone who did not build it can run it and get an unambiguous answer. -->

| | |
| --- | --- |
| **Preconditions** | «what must exist first» |
| **Steps** | «what to do» |
| **Pass** | «the observable result that means this phase is done» |
| **Fail** | «what a failure looks like, so a partial pass is not read as a pass» |

---

## Specified in

<!-- fill: Paths only. Do not restate what these documents say — a second copy of a
     requirement is a second source of truth, and the two disagree within a week. -->

| What | Where |
| --- | --- |
| Requirements | `deliverables/02-product/03-PRD.md` |
| Feature behavior | `deliverables/02-product/04-Feature-Spec.md` |
| Data | `deliverables/03-technical/05-Data-Model.md` |
| Interfaces | `deliverables/03-technical/06-API-Contract.md` |
| Setup and CI | `deliverables/04-delivery/16-Engineering-Setup.md` |

---

## Non-negotiables in this phase

<!-- fill: Each with the cost of breaking it, taken from 12-Build-Handoff.md. A rule whose
     reason is absent gets refactored away by someone who assumes it was arbitrary. -->

| Rule | What breaks if it is ignored |
| --- | --- |
| «rule» | «consequence» |

---

## Blocked and open

| Item | Owner | When it bites |
| --- | --- | --- |
| «what is needed» | «named person» | «the moment work stops without it» |

---

<!-- ACCEPTANCE
  - README.md lists every phase in order with status and what gates it
  - One phase document per milestone in state.outputs.roadmap.milestones — no more, no fewer
  - Every definition of done is 09-Roadmap.md's, word for word
  - Each phase states what is NOT in it, with reasons
  - Each phase names its specifying deliverables by path and restates none of them
  - No task breakdown, no estimates, no sprint plan anywhere in the folder
  - Exactly one phase marked current, and it is the first not done
  - Milestone Zero, where committed, is phase-00 and every build phase names it as its gate
  - Where the verdict does not support building, README.md says so first
-->

> **Phase Principle**
>
> A plan that says what is in the current phase and not what is outside it has not scoped
> anything. The edge is the artifact.
