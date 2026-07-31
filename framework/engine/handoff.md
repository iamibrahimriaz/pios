# Handoff — making the run directory buildable

The run does not end when `validate-run.py` exits 0. It ends when someone can open the run
directory, say *"analyze this project and start developing"*, and have that be enough.

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

## What this step produces

**One file, at the root of the run directory**, named by whatever convention the operator's
tool expects — `CLAUDE.md`, `AGENTS.md`, or another. **Ask; do not guess.** If they have no
preference, write `CLAUDE.md` and say so.

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
5. **The current milestone, and only that one**, with its end-to-end acceptance test.
6. **The order of work inside that milestone.**
7. **The non-negotiables, each with the cost of breaking it.** A rule whose reason is absent
   gets refactored away by someone who assumes it was arbitrary.
8. **The blocked list** — what to ask about rather than decide.
9. **A progress file to maintain**, and an instruction not to edit the specification or the
   audit trail in place. If a document is wrong, the builder says so; they do not correct it,
   because the run's record of what it believed is what makes the output auditable.

**Point 7 is the one that decays.** Copy the constraint and its consequence together, or the
constraint travels alone and does not survive contact with a library that suggests otherwise.

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

## What this step does not do

- **It does not create a git repository.** Runs are private and gitignored by the framework
  repo. Whether this becomes the team's repository, and when, is the operator's decision.
- **It does not rewrite any deliverable for the builder.** A specification paraphrased for
  readability is a second source of truth, and the two disagree within a week.
- **It does not run automatically.** A run that reached "do not build", or an operator still
  deciding, does not need this. Offer it; do not assume it.

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
- [ ] A bare "analyze this project and start developing" would be sufficient
- [ ] Every path it names resolves from the run directory root — checked, not assumed
- [ ] Nothing in it points outside the run directory
- [ ] Reading order stated: what is instruction, what is reference, what is research
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
