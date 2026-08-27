# Handoff — making the run directory legible to whoever builds

**This is the framework's last act, not the first step of a build.** `constitution/core/00-Purpose.md`
states the boundary: this framework produces research, specification, proposal and handoff, and
stops. **The handoff is the final research artifact.**

Its job is to make the specification legible to whoever builds next — so that someone can open the
run directory, say *"analyze this project and start developing"*, and have that be enough **without
this framework being involved in what happens after.**

> **Writing the entry file is the whole step. Acting on it is not part of this framework**, and an
> agent that writes the entry file and then starts building has carried the run past the point where
> anything gates it.

**One folder. No copy, no subset, no second repository.** The run directory already holds
the specification; what it lacks is an entry file telling an agent what to read, in what
order, and what not to touch. Writing that file is the whole step.

---

## Why not assemble a separate build package

Because every version of that idea reintroduces the same defect. A subset copied into a
staging folder, or into a new repository, produces **two copies of the same specification
with nothing keeping them aligned** — and the build proceeds from whichever went stale. The
copy is then maintained by hand, forever, by someone who has to remember it exists.

Selecting which documents a builder sees is a real need. **Solve it with reading order, not
with file selection.** The entry file says what to read first, what is reference, and what is
research behind the specification rather than instruction in it. A builder who ignores that
ordering and reads the risk register has lost nothing; a builder handed nine files out of
sixteen and told the rest do not concern them has lost the ability to check a decision.

> A specification that exists in two places has no source of truth. A specification that
> exists in one place, with a stated reading order, has both.

---

## When it runs

**Every completed run, automatically.** It is a required completion artifact in
`deliverables/manifest.yaml`, alongside the proposal and the engineering presentation. It is not
offered and it is not conditional.

**A run that reached "do not build" still produces it, and that is when it matters most.** The
entry file is where an agent is told the gate is closed and what it may do instead. A folder with
no entry file does not stay unbuilt; it gets opened by an agent that reads the specification,
finds it complete, and starts.

---

## What this step produces

**One file, at the root of the run directory**, named by whatever convention the operator's
tool expects — `CLAUDE.md`, `AGENTS.md`, or another. **Ask; do not guess.** If they have no
preference, write `CLAUDE.md` and say so.

**Fill `deliverables/templates/19-AI-Entry-File.md`.** It carries the required structure and the
guidance for each section.

Its job is that a bare instruction is sufficient. If the operator has to remember a
paragraph of context to start a session, the file has failed and no amount of detail inside
it compensates.

It carries, in this order:

1. **A standing instruction**, written to trigger on any phrasing of "start", "continue" or
   "build the next thing" — not on one exact sentence.
2. **What is in the folder**: which directory is the specification, which is the working
   record, and where code goes. A run directory contains research the builder does not need
   on day one, and an unexplained folder gets either ignored or read at the wrong moment.
3. **Read this first, in this order** — the build handoff in full, then the engineering
   setup, then the reference documents by name.
4. **How to check what already exists**, so a second session continues rather than restarts.
5. **The current phase, and only that one** — named, with `phases/phase-NN-*.md` pointed at.
   **Do not restate its scope, its definition of done or its acceptance test.** Those were
   copied from the roadmap into the phase document; a copy here is a third version, and the
   one open on the agent's screen is the one that wins.
6. **What closing it means**: mark it done on the board, move `current` forward, stop there.
7. **The non-negotiables, each with the cost of breaking it.** A rule whose reason is absent
   gets refactored away by someone who assumes it was arbitrary.
8. **The blocked list** — what to ask about rather than decide.
9. **A progress file to maintain**, and an instruction not to edit the specification or the
   audit trail in place. If a document is wrong, the builder says so; they do not correct it,
   because the run's record of what it believed is what makes the output auditable.

**Point 7 is the one that decays.** Copy the constraint and its consequence together, or the
constraint travels alone and does not survive contact with a library that suggests otherwise.

---

## The entry file and the phase board must give the same answer

**Both of them tell an agent whether work may start**, and they are written by different steps
from different sources — this file from the readiness states, the board from the roadmap and the
verdict. `engine/phases.md` produces the second.

**Where they disagree, the builder acts on the more permissive one.** An entry file that says
the commercial gate is open, beside a board showing phase-01 current, is read as permission —
the board is the operational document and the entry file reads like preamble.

So: **where the run recommends against starting, the board's first line says so and no phase is
marked current.** Check it by opening both, not by remembering what you wrote.

**Both documents state the recommendation; neither issues a prohibition.** The board says what
makes a phase current — including the operator deciding to proceed without the outstanding
answer — so that a run whose recommendation is overruled produces a board that still works. See
*An undecided question is not withheld permission* below.

---

## The folder must be self-contained

**Nothing in the entry file may point outside the run directory** — not at the framework, not
at `PIOS_HOME`, not at an absolute path on the operator's machine.

This is what lets the folder move. It works in place; it works copied to another machine;
it works with `git init` run inside it and pushed as the product repository. The operator
chooses when and whether to do that, and nothing has to be rewritten when they do.

**Check it rather than assuming it.** Every path the entry file names must resolve from the
run directory root.

---

## Readiness is five states, and only three of them are the run's

**A complete specification is not permission to build.** These are confused every time, because
they arrive together: the package is finished, it looks finished, and finished reads as authorized.

| State | Means | Whose |
| --- | --- | --- |
| **research_ready** | The evidence base is complete and its limits are stated | The run's |
| **product_definition_ready** | Scope, requirements and acceptance criteria are settled | The run's |
| **engineering_ready** | An implementer can start with no further decisions from research | The run's |
| **commercially_validated** | Someone has been observed paying, or the equivalent test passed | **Not the run's** — a validation result |
| **development_authorized** | The owner has authorized the build, on a recorded basis | **Never set by a run** |

**They are not a ladder that carries.** A run can and often should deliver `engineering_ready: true`
alongside `commercially_validated: false`, and that is a complete, honest result rather than an
unfinished one.

> **A count of ticked engineering boxes says the product is fully specified. It says nothing about
> whether anyone will pay for it.** Those are different questions and only one of them has an
> answer at handoff.

**Recorded in `state.run.readiness`, and stated in the entry file's first section** — with
`blocked_on` naming what is missing and whose it is to supply. An operator may authorize without the
commercial gate; that is theirs to do, and it is recorded as an `override` with who decided and on
what basis. **It is never inferred from the specification being complete.**

**Where the commercial gate is open, the entry file says what an agent may do instead** — help run
the validation, review the package, ask the blocked questions. A folder that only says "do not
build" gets built anyway, by the next agent that reads a complete specification and finds no
alternative offered.

### An undecided question is not withheld permission

**`development_authorized: false` means the operator has not decided. It does not mean permission
was refused, and the run has no standing to refuse it.** The distinction is invisible in the state
file and decisive in the prose written from it.

Rendered literally, the flag becomes *"the build is not authorized"* — which is what it says, and
which a downstream agent reads as a prohibition. The entry file then instructs that agent not to
write code, the board marks every phase blocked, and **the package refuses an instruction the
operator is entitled to give.** The operator asks their coding agent to start; their own research
folder tells it no.

| Says | Reads as | Use |
| --- | --- | --- |
| "The build is not authorized" | The run is withholding permission | **Never** |
| "Do not write application code" | An instruction to the operator's agent, from a document with no authority to give one | **Never** |
| "The specification is complete; whether to build is not established and the decision is yours" | An accurate report of two different states | **Yes** |

**This changes nothing about the verdict.** A run that recommends against building says so, as
forcefully as the evidence supports, in the first thing the file says. What changes is that it
recommends rather than forbids — and it names the sentence from the operator that resolves the
question, so the folder is not waiting on something nobody knows how to supply.

**Then write the branch the file usually omits: what happens if they authorize it anyway.**
Almost every entry file states the not-authorized path and stops, which leaves the agent that
receives *"start building"* with the recommendation and no route through it. Name where to start,
and name what changes about the sequencing when the open question is being answered by building
instead of by asking. **An operator overruling a recommendation is entitled to the best version of
the thing they asked for, not a worse one delivered reluctantly.**

> **The failure mode this prevents is not an unbuilt product. It is a run whose honest finding
> gets discarded wholesale** — because the only way past a prohibition is to ignore the document
> that issued it, and a reader who ignores one paragraph stops reading the rest.

---

## Integration contracts built on inference carry their verification step

**Where the specification describes an external system the run could not read** — an API inferred
from error messages, a schema reconstructed from documentation that may be stale, a third-party
behavior taken from support threads — **the handoff names the verification step that must precede
implementation, and states that it blocks.**

This is not an engineering instruction; the framework does not verify it. **It is a disclosure**:
the run is saying which parts of its own specification are `[assumption]` rather than `[verified]`,
and building an adapter on an unverified assumption is a defect the specification can prevent and
the code cannot.

**Bury it and it disappears.** An `[assumption]` tag inside an interface definition on page nine is
invisible to a builder who was told the package is complete.

---

## What this step does not do

- **It does not create a git repository.** Runs are private and gitignored by the framework
  repo. Whether this becomes the team's repository, and when, is the operator's decision.
- **It does not rewrite any deliverable for the builder.** A specification paraphrased for
  readability is a second source of truth, and the two disagree within a week.
- **It does not authorize the build.** Where the run's verdict or a gate blocks it, the entry
  file's first section says so and states what an agent may do instead.

---

## What the operator still owes

Name what the build cannot start or finish without, taken from `12-Build-Handoff.md`'s
blocked work: account access, a vendor quote, a legal opinion, domain-language copy, a
decision the run recorded as decision-dependent.

**Each with an owner and the point at which it bites.** "Before the first paying customer" is
a different urgency from "before the first line of code", and a list that does not
distinguish them is treated as uniformly ignorable.

---

## Checklist

- [ ] Validator exits 0, and the delivery checkpoint has been presented
- [ ] The operator has confirmed the entry-file convention their tool expects
- [ ] Entry file written at the run directory root
- [ ] Every directory in the run folder is explained, so none is read at the wrong moment
- [ ] Where the verdict or a gate blocks the build, that is the first thing the file says
- [ ] `state.run.readiness` is recorded, with `blocked_on` naming what is missing and whose it is
- [ ] `development_authorized` is false unless the operator recorded an override, with their basis
- [ ] Where the commercial gate is open, the file says what an agent may usefully do instead
- [ ] No sentence phrases an undecided question as withheld permission, and none instructs the operator's agent to refuse work
- [ ] The file names the sentence from the operator that resolves the open question
- [ ] The authorize-anyway branch is written: where to start, and what changes about the sequencing
- [ ] Every integration contract built on inference names its verification step and says it blocks
- [ ] A bare "analyze this project and start developing" would be sufficient
- [ ] Every path it names resolves from the run directory root — checked, not assumed
- [ ] Nothing in it points outside the run directory
- [ ] Reading order stated: what is instruction, what is reference, what is research
- [ ] The current phase is named and pointed at, and its acceptance test is not restated here
- [ ] The board and this file agree about whether work may start
- [ ] Non-negotiables carry their consequences, not just their rules
- [ ] Blocked work listed with owners and the moment each one bites
- [ ] The specification and the audit trail are marked not-to-be-edited-in-place

---

> **Handoff Principle**
>
> A specification nobody reads is indistinguishable from one that was never written.
>
> The last step of a run is not producing the artifacts. It is making the folder they are
> already in the place the work starts, with the reasons attached to the rules.
