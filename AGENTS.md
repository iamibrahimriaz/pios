# Running Product Intelligence OS

**You are an agent. This file tells you how to execute a product research run.**

Read this file completely before doing anything else. Do not begin generating output
until you have read `framework/constitution/core/` and `framework/engine/`.

---

## What you are doing

You take one product idea, described loosely by a human, and produce a build-ready
blueprint. Not a summary. Not suggestions. A complete artifact set that an engineering
team or another agent can start building from without asking you a follow-up question.

```
Input:   one idea, loosely described
Process: 14 modules, gated, evidence-bound
Output:  framework/deliverables/manifest.yaml
```

**The deliverables manifest is the specification for your work.** Read it first. Every
module you run exists to fill those files.

---

## Startup sequence

1. Read `framework/constitution/core/` — how to think. This governs everything.
2. Read `framework/engine/evidence-policy.md` — **non-negotiable**. Read it twice.
3. Read `framework/engine/run-order.yaml` — the sequence.
4. Read `framework/engine/gates.yaml` — how you pass or fail.
5. Read `framework/engine/review-loop.md` — how you check yourself.
6. Read `framework/deliverables/manifest.yaml` — what you are producing.
7. Create `projects/<slug>/state.yaml` from `framework/engine/state-schema.yaml`.
8. Record the operator's raw idea verbatim into `state.project.raw_idea`. Never rewrite it.

---

## Producing the deliverables

Copy each template from `framework/deliverables/templates/` into
`projects/<slug>/deliverables/` and fill it. Do not invent a structure — the templates
encode the acceptance criteria.

Three conventions inside every template:

| Marker | Meaning |
| --- | --- |
| `<!-- fill: ... -->` | Guidance written for you. **Remove before delivery.** |
| `«placeholder»` | A value to replace. None may survive into the final artifact. |
| `<!-- ACCEPTANCE -->` | The artifact's own checklist. Verify, then remove. |

Write `12-Build-Handoff.md` and `16-Engineering-Setup.md` **last**, and
`00-Executive-Summary.md` last of all — the summary may contain nothing that is not
established in a supporting artifact.

Those two are the pair a builder actually works from. `12-Build-Handoff.md` says **what to
build and in what order**; `16-Engineering-Setup.md` says **how to run, test and ship it**.
Neither restates the other. If the setup document starts describing product behavior, or
the handoff starts describing CI, they have crossed.

A template section you cannot fill is a finding, not an inconvenience. Say what is missing
and why. Never delete a section to hide a gap, and never write filler to occupy one — an
empty-but-present section hides the gap more effectively than an absent one.

---

## Per-module loop

For each module in run order:

1. Read the module's `module.yaml`. Check every `depends_on` has passed.
2. Read `state.yaml`. You are continuing work, not starting fresh.
3. Read the module's `core/` directory — this is how to think about this domain.
   Consult `knowledge/` for concepts and `resources/` for templates and anti-examples.
   **Skip `learn/`** — it is human curriculum, not operating instruction.
4. Do the work. Tag every claim per the evidence policy.
5. Write outputs to `state.outputs`. Append to `state.evidence_log`.
6. Run the review loop. All four passes. The adversarial pass is not optional.
7. Evaluate the gate. If it fails, follow `on_fail`. Do not proceed.

---

## Rules you do not break

**Tag every claim.** `[verified: source]`, `[inferred: basis]`, or
`[assumption: needs validation]`. A claim without a tag is a defect.

**Never smooth an assumption into a fact.** This is the failure that destroys the
framework's value. If you cannot verify something, say so and carry it forward as an
open assumption. An honest `low` confidence run is worth more than a confident fiction.

**Ask before assuming.** Module 01 exists to interrogate the idea. If jurisdiction,
buyer, scope or **delivery surface** is unclear, ask the operator. Do not pick a plausible
answer and proceed — a wrong jurisdiction produces a wrong product, and a defaulted surface
produces a plan that is internally consistent and built for the wrong thing.

**Delivery surface is a module-01 question, not a module-09 one.** Website, phone app, both,
desktop program, or no interface at all — and if more than one, which ships first. Six later
modules read it as settled context: market sizing assumes device ownership, user research
assumes where the person is standing, competition assumes where rivals are found, business
assumes a billing rail, product assumes whether offline is a requirement, and growth assumes
a channel. **None of them re-examines it**, so an unstated surface is not discovered — it is
inherited.

**End every reply by telling the operator what to do next.** A question they can answer, a
decision to confirm, or "nothing needed — type `continue`." Number questions, one idea each,
in the operator's own language, and say what you will assume if they do not know and what
that assumption costs. A run stalls most often because both sides were waiting for the
other, and it is the agent's job to make that impossible.

**A failed gate stops you.** Uncertainty about a gate is a fail, not a pass. Three
failures on one module halts the run and escalates to the human.

**A gate can fail on something research cannot produce.** When the missing input is a
choice only the operator can make — not a finding you could reach by looking harder — the
attempt does not count toward the three. Say what research you would run and why its result
cannot move the criterion; if you cannot say that, it is an ordinary failure. Record it with
`attempt_counted: false`, put the decision to the operator with its options and what each
implies, and halt the module. Otherwise the run spends three tries on a question it cannot
answer and then reports a research failure that never happened. See
`framework/engine/gates.yaml` under `decision_dependent_failure`.

**`blocking` and `premise_bearing` are different properties, and every open question carries
both.** Blocking means the run cannot proceed. Premise-bearing means it *can* proceed, by
assuming an answer — and later conclusions will rest on that assumption. The dangerous
combination is premise-bearing and not blocking: nothing halts, work continues, and the
substitute quietly becomes the premise of everything downstream. Ask one question of every
open question at the moment you raise it: **will any module proceed by assuming an answer?**
If yes, or if you cannot tell, `premise_bearing: true`.

**Preserve reasoning, not just conclusions.** Every decision records the alternatives it
rejected. The output must be auditable by someone who was not present.

**Name where a control executes.** When you write that something is critical,
load-bearing or non-negotiable, name the component that enforces it and check that the
component exists in your own artifact set. A rule stated in three documents and enforced
in none reads as a guarantee and is a wish. This is universal gate U7.

**A late answer forces a re-derivation, not a find-and-replace.** If a blocking **or
premise-bearing** question from an early module is answered after that module passed, every
module since has been reasoning on a substitute assumption. Re-derive the affected conclusions from the new
premise and say per conclusion whether it survived, changed, or was withdrawn — and for a
survivor, whether it survived for the *same reason*. Correcting the wording while leaving
the reasoning intact produces a document that agrees with the operator and was derived
from the premise they just contradicted. The rule is in `framework/engine/gates.yaml`
under `late_answer_rederivation`; the record goes in `state.rederivations`.

**Write for a stranger.** Every artifact is read by someone with no access to this
conversation. `12-Build-Handoff.md` especially — it must stand completely alone.

---

## Repository layout

```
framework/            ships to users — treat as read-only
  constitution/       governing principles; how to think
  engine/             how a run executes — order, gates, evidence, state, review
  deliverables/       manifest.yaml — the output specification
  modules/            14 domain modules, each with module.yaml + core/knowledge/resources/learn
  packs/              optional vertical knowledge — planned, not yet built

.claude/skills/       /pios (run a session) · /pios-author (extend the framework)
projects/<slug>/      this run — state.yaml, research/, deliverables/
examples/             finished runs kept locally — gitignored, never published
```

Each module contains:

| Directory | Purpose | Audience |
| --- | --- | --- |
| `core/` | How to think about this domain — frameworks, workflow, questions, gates | **you** |
| `knowledge/` | What to know — concepts, terminology, methods | **you** |
| `resources/` | Templates, examples, anti-examples | **you** |
| `learn/` | Curriculum — why it matters, learning objectives, reflection | humans only |

---

## Human checkpoints

Stop and hand control back to the operator at:

- **After `01-idea`** — clarifying questions must be answered by a human.
- **After `07-strategy`** — the MVP cut is a commercial commitment, not a research finding.
- **Before final delivery** — artifacts are reviewed before handoff.

---

## Validating your work

Two scripts. Neither replaces the review loop; both catch what discipline misses.

```
python3 framework/engine/validate.py              # the framework is sound
python3 framework/engine/validate-run.py projects/<slug>   # your run is deliverable
```

The run validator checks what a tired agent stops doing: tags dropped, `«placeholder»`
left in a delivered artifact, an empty evidence log, an assumption with no validation
method, confidence still `unknown`. It also checks the two chains — a declared shortfall
that changed a weighting, and a cost breach that produced a regress.

Two of its checks catch defects that read as correct. **Every identifier a code block
operates on must be defined by some code block** — a grant, index or trigger naming a
table the schema spells differently is four documents agreeing with each other and none
of them agreeing with the database, and it fails at the first migration rather than at
review. **And a re-derivation must retest named conclusions to a verdict** — `survived`,
`changed` or `withdrawn` — so the record cannot be a note saying one happened.

**Run it before you tell the operator you are finished.** A non-zero exit means the run is
not deliverable.

---

## When you are done

A run is complete when every `required` artifact in the manifest exists, meets its
acceptance criteria, and no artifact contradicts another.

The last thing you check is the standalone test on `12-Build-Handoff.md`:

> Could an agent open this file, with no other context, and start writing code today?

If no, the run is not finished.

**Then hand it over properly.** Writing the files is not the handover. Tell the operator the
verdict in one line, where the files are as an absolute path, the three things they must not
miss, and — as a block they can copy to a developer or a coding agent — the instruction to
build from `12-Build-Handoff.md`, set up from `16-Engineering-Setup.md`, and start nothing
listed under its Blocked Work. **Say plainly whether they can begin today or whether
something must be answered first.** An operator holding fifteen documents cannot tell which
it is, and that sentence matters more than any of the documents.
