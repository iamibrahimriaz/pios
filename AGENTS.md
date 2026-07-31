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
buyer, or scope is unclear, ask the operator. Do not pick a plausible answer and proceed —
a wrong jurisdiction produces a wrong product.

**A failed gate stops you.** Uncertainty about a gate is a fail, not a pass. Three
failures on one module halts the run and escalates to the human.

**Preserve reasoning, not just conclusions.** Every decision records the alternatives it
rejected. The output must be auditable by someone who was not present.

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
examples/             completed reference runs — none yet
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

**Run it before you tell the operator you are finished.** A non-zero exit means the run is
not deliverable.

---

## When you are done

A run is complete when every `required` artifact in the manifest exists, meets its
acceptance criteria, and no artifact contradicts another.

The last thing you check is the standalone test on `12-Build-Handoff.md`:

> Could an agent open this file, with no other context, and start writing code today?

If no, the run is not finished.
