# Producing the Phase Plan

**The roadmap, arranged so the current phase can be read without the other fifteen.** Template:
`deliverables/templates/22-Phase-Plan.md`. Output: `projects/<slug>/phases/`.

---

## When this runs

**Every completed run.** It is a required completion artifact in `deliverables/manifest.yaml`.
It is not offered and it is not conditional.

**A run that reached "do not build" produces it too**, and that is when the first line of the
board matters most. A folder with a roadmap in it and no board does not stay unbuilt — it gets
opened by an agent that reads a complete specification, finds a sequenced milestone list, and
starts on milestone one.

---

## Why this exists

`09-Roadmap.md` already carries the milestones, their dependencies and a definition of done for
each. Everything in this artifact is in that file.

**What that file cannot do is be read one milestone at a time.** An agent starting work opens a
document covering the whole program, and the sections describing work that is six months away are
indistinguishable in weight from the section describing what to do now. The observable result is
scope drift toward whatever was most interesting on the page, not toward what was sequenced first.

> The roadmap answers *what is the plan*. The phase plan answers *what am I allowed to start*.
> They are different questions and only one of them has a single answer at any moment.

---

## Reproduced, never re-derived

**Every definition of done in this package already exists in `09-Roadmap.md`.** Copy it. Do not
tighten it, do not restate it in your own words, do not fold two milestones' criteria together
because they read similarly.

**If a definition of done looks wrong while you are copying it, record that it looks wrong.** Do
not change it. It was written when the milestone was designed and the scope was being argued —
which is the only moment it could be set honestly. This document is written afterwards, at the
moment it is easiest to adjust toward whatever the run already concluded.

This is the same rule `engine/milestone-zero.md` applies to stop-condition thresholds, for the
same reason, and it fails the same way when it is relaxed.

---

## The boundary — and it is the one this artifact exists closest to

**Phases stop at milestone granularity. They do not decompose into tasks.**

No task list. No estimates. No sprint plan. No implementation order inside a phase beyond what
`09-Roadmap.md` already recorded as a dependency. No ticket titles.

`constitution/core/00-Purpose.md` ends this framework at the pre-development package. **A phase
document is an index over a specification that already exists.** A task breakdown is the first
step of the build, and it belongs to whoever is doing the build — they know their team, their
tooling and their week, and this run knows none of those things.

**Expect the pull toward it every time you write one of these.** Each phase document has a
"what this phase delivers" section that would read more usefully with six bullets under it, and
each of those bullets is a task. The request will not arrive as *"add sprint planning"*. It
arrives as *"break this down a bit so the agent knows where to start"*, one phase at a time,
and the folder is a project plan before anyone decided it should be one.

**The test:** does this sentence tell the builder what must be true at the end, or does it tell
them what to do on Tuesday? The second one is not this framework's to write.

---

## One phase per milestone, and the count is checked

**One document per entry in `state.outputs.roadmap.milestones`. No more and no fewer.**

- **A phase with no milestone behind it** is scope the roadmap never authorized. It got added
  while writing this, it will be built, and nothing in the research supports it.
- **A milestone with no phase document** is work that left the plan silently. The roadmap still
  lists it, so every review passes; the board is what anyone actually works from, and it is not
  there.

**Record the milestones in state before writing this.** `state.outputs.roadmap.milestones`, each
with an `id` and a `name`. The validator compares that list against the documents on disk, and
it can only do that if the list exists.

---

## Exactly one phase is current

**And it is the first one not done.** Not the one most ready, not the one nobody is blocked on,
not two of them because a team could run them in parallel.

**Where none can be current, say which condition is unmet.** Do not promote the next phase to
keep the board looking active. A board with a current phase is acted on; that is the whole
mechanism, and it works in the wrong direction just as reliably.

**Where the strategy committed to a Milestone Zero, it is phase-00, and every build phase says
in its own document that it is gated behind it.** Naming the gate only on the board does not
survive: the phase document is what gets opened, and a gate that appears one file away is a gate
nobody read.

---

## Where the verdict does not support building

**The board says so on its first line, and no build phase is marked current.**

The phases still get written. An agent that is told "do not build" and given nothing else will
build; an agent told "do not build, phase-00 is the validation that would change this answer,
here is what it decides" has somewhere to go.

This mirrors `engine/handoff.md`'s rule for the entry file, and the two must agree. **If the
entry file says the build is blocked and the board shows phase-01 current, the folder contains
two answers and the builder will use the one that lets them start.**

**Say what makes the next phase current, and include the operator deciding to proceed anyway.**
`development_authorized: false` records that they have not decided — it is not a refusal, and the
board has no standing to issue one. A board whose only route forward is a validation result
**stalls permanently the moment the operator chooses a different route**, and the agent reading it
either halts against its owner's instruction or ignores the board entirely. Neither outcome
preserves the finding the board exists to carry.

**Reserve the word *blocked* for what a decision cannot waive** — a legal requirement, a
dependency, an unbuilt predecessor. A phase waiting on a judgment is *not started*, and the
distinction is the difference between a board that reports and a board that forbids.
`engine/handoff.md`, *An undecided question is not withheld permission*.

---

## What each phase document must carry that the roadmap does not

**The edge.** `09-Roadmap.md` states what a milestone delivers. It rarely states what the
milestone deliberately excludes, because at planning time the exclusions are obvious from
context. They are not obvious four weeks later to whoever is implementing it.

**Give "what is NOT in this phase" equal weight to what is**, each exclusion carrying its reason
and where it went instead. A phase that states only its contents grows during implementation,
and it grows in the direction of whatever the implementer found interesting — which nothing in
the run evaluated.

**And name the specifying documents by path, restating none of them.** A requirement copied into
a phase document is a second source of truth. The two disagree within a week, and the phase
document wins, because it is the one open on the screen.

---

## Checklist

- [ ] `state.outputs.roadmap.milestones` recorded, each with an `id` and a `name`
- [ ] `phases/README.md` written — verdict, confidence, current phase, the board, what is not on it
- [ ] One `phase-NN-<slug>.md` per milestone, and no others
- [ ] Every definition of done copied from `09-Roadmap.md` word for word
- [ ] Every phase states what is deliberately NOT in it, with reasons
- [ ] Every phase carries an end-to-end acceptance test with a stated failure shape
- [ ] Every phase names its specifying deliverables by path and restates none of them
- [ ] No task breakdown, no estimates, no sprint plan anywhere in the folder
- [ ] Exactly one phase marked current, and it is the first not done
- [ ] Milestone Zero, where committed, is phase-00 and every build phase names it as its gate
- [ ] Where the verdict blocks the build, that is the first line of the board
- [ ] The board and the entry file give the same answer about whether work may start

---

> **Phase Principle**
>
> A roadmap tells you the plan. A phase plan tells you what you may start, and refuses to tell
> you how — because the run knows the first and has never met the team that answers the second.
