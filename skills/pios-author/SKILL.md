---
name: pios-author
description: >
  Extend or modify the Product Intelligence OS framework itself — write a new module,
  add a vertical pack, add or change a gate criterion, add a deliverable template, or
  edit any file under framework/. Enforces the four-layer architecture, the core/learn
  test, frontmatter and gate parity rules, and runs the structural validator. Invoke for
  "add a module", "write a pack for healthcare", "change this gate", "add a deliverable",
  "edit the constitution", or any contribution to the framework. Do NOT use this for
  running a research session on a product idea — that is the `pios` skill.
---

# Product Intelligence OS — Authoring

You are modifying the framework itself, not using it. Different rules apply.

**Read `framework/AUTHORING.md` first.** It is the specification for this work and this
file does not repeat it. What follows is the part that is easiest to get wrong.

---

## Before you start — you must be inside the repository

Authoring edits the framework itself, so unlike `/pios` it cannot run from another
project. Check:

```bash
test -f framework/AUTHORING.md && echo "ok" || echo "not in the framework repository"
```

If you are not, stop and tell the operator:

> Authoring changes the framework itself, so it has to run from inside the Product
> Intelligence OS repository. `cd` there and invoke `/pios-author` again — if `PIOS_HOME`
> is set, that is where it lives.

Then, before changing anything:

```bash
pip3 install -r requirements.txt
python3 framework/engine/validate.py
```

It must exit 0 before you start and again before you finish. Thirty-seven checks. Read
`framework/AUTHORING.md` — it is the specification, and this file does not repeat it.

---

## The rule that decides everything

> If an agent mid-run would **act differently** for having read it, it belongs in `core/`.
> If it explains why the module exists to a human, it belongs in `learn/`.

An executing agent reads `core/`, `knowledge/` and `resources/`, and **skips `learn/`
entirely**. Content in the wrong layer either bloats the agent's context with curriculum,
or hides operating instructions where the agent will never look.

Nothing in `learn/` may carry an operating instruction. This is not a style preference —
it is why the split exists.

---

## Order of work for a new module

`module.yaml` is written **first**, before any prose. It forces you to decide what the
module actually produces, and everything in `core/` then serves those outputs. A module
written in the opposite order produces beautiful principles that connect to nothing.

1. `module.yaml` — id, purpose, depends_on, consumes, produces, feeds_deliverables, gate,
   on_fail
2. `core/06-Framework.md` — the method
3. `core/07-Workflow.md` — the handoff contract
4. `core/13-Template.md` — the output shape
5. `core/11-Quality-Gate.md` — the gate, expanded criterion by criterion
6. `core/12-Checklist.md`
7. The remaining `core/` files, then `knowledge/`, `resources/`, `learn/`

Eleven `core/` files, eight `learn/` files, three `resources/` files. The validator checks
all of them exist.

---

## Traps specific to this repository

**Quote gate criteria that begin with `>=`.** Unquoted, YAML reads `>` as a folded block
scalar and the file silently fails to parse. This defect existed in seven of fourteen
modules and nobody noticed, because nothing had ever parsed them. The same applies to any
criterion starting with a quote character.

```yaml
gate:
  - ">= 3 trends with direction and evidence"      # correct
  - '"Do nothing / status quo" evaluated'          # correct
```

**Gate criteria must match exactly** between `module.yaml` and `core/11-Quality-Gate.md`.
`module.yaml` is the source of truth; the Quality-Gate file explains how to evaluate each,
using the identical wording. The validator enforces this.

**Prerequisites are real paths.** They resolve against `framework/modules/`,
`framework/constitution/`, `framework/`, or the citing file's own directory. The one
permitted non-path form is `<module> gate passed`.

**Keep the wiring symmetric.** If a module declares `feeds_deliverables`, the manifest's
`fed_by` for that artifact must name the module, and vice versa. If a module `consumes`
something, `depends_on` must include whoever produces it.

**Every deliverable needs acceptance criteria and an audience.** An artifact that cannot
fail its own criteria is not a deliverable.

---

## House style

American spelling. `#` for all headings — this repo does not use a single-H1 convention,
so MD025 linter warnings are expected and are not defects. Short paragraphs, one idea
each. `>` blockquotes for principles. Tables for anything comparative. `«placeholder»`
markers. Close each file with a `> **X Principle**` block.

**Give the cost of doing it wrong, not just the instruction.** "Ask which country" beats
"consider the regulatory context." Avoid motivational filler and generic advice that would
apply to any framework.

In `resources/`, **anti-examples are weighted heaviest**. A filled-in artifact that looks
plausible and is wrong teaches more than a correct one, because the failure it demonstrates
is the one people actually commit.

In `18-References.md` files, **never invent a citation.** Those files are methodology —
they route a question to a source type and mark what is structurally unsourceable before
launch. A fabricated title or page number is the exact failure the evidence policy exists
to prevent.

---

## Before you finish

```bash
python3 framework/engine/validate.py
```

It must exit 0. Thirty-seven checks: YAML parses, required files exist, dependency graph is
complete and acyclic, gate parity holds, manifest and modules agree, **no two manifest
artifacts claim the same path**, **every artifact names a folder the layout defines and every
folder is used**, prerequisites resolve, no stale identifiers, **every engine method file is
reachable from something an agent reads**, **every controlled-vocabulary value in `gates.yaml`
reaches a skill that teaches it**, skills carry no self-modification instruction, no run
content is tracked, American spelling.

Then walk `AUTHORING.md`'s submission checklist. The item most often missed is the last
one: **nothing in `learn/` that an agent needs to execute correctly.**

---

## Folding a lesson from a run back into the framework

Runs are where the framework's real defects surface. Runs are also private —
`projects/` and `examples/` are gitignored, and a structural check fails the build
if any run content is tracked. Both things are true at once, so the lesson crosses
the boundary and the project never does.

**Start from the run's own friction log.** A completed run leaves `state.friction_log` —
the places the framework got in the agent's way, recorded as they happened rather than
remembered afterwards. Read it before anything else; it is the cheapest source of real
defects this project has, and entries marked `operator_visible: true` are the ones that
cost a person something.

**It is not the whole picture.** The log records where the framework blocked the *agent*.
It cannot record where the framework was confusing, slow or unclear to the *operator* —
that only arrives when they say so, and historically it has been the more valuable half.
Ask for it; do not wait for it.

**State the defect so it stands on its own.** If the reasoning only makes sense
with the run in front of you, it is not a framework change yet.

| Not this | This |
| --- | --- |
| "In the Acme run, the pricing gate failed" | "The pricing gate cannot be passed when the buyer and the user are different people" |
| "Module 05 missed the incumbent" | "05-competition's gate does not force the incumbent platform to be named" |

**Never carry across** a client or company name, a real price, a named customer, a
market size figure, or a sentence lifted from a deliverable. Anti-examples in
`resources/` are written from scratch. A harvested one is a leak wearing a
teaching costume, and it is the most likely way this repository ever publishes
something it should not have.

The commit message explains the defect, not the project that revealed it.

---

## What must never be added to this framework

**The framework produces the pre-development package — research, specification, proposal,
handoff — and stops there.** `constitution/core/00-Purpose.md` states the boundary; this is the
authoring consequence.

**Do not add modules, engine steps, templates or skills that perform, direct or verify
development work.** Specifically: no build module, no test-authoring step, no scaffolding
generator, no deployment or release process, no code-review or QA method.

**Expect the request repeatedly.** "Now build it" follows every completed run, and it arrives
disguised as a small, reasonable extension — a setup helper, a scaffolding step, "just the
repository layout". Each looks like a natural continuation of the handoff. **Together they turn
a research framework into a half-built engineering one**, governed by evidence rules that cannot
judge whether code works.

**The test:** does this change help establish what is true, or does it help produce a working
system? The second belongs to the project that receives the package.

---

## The principle every change is judged against

> **Accurate uncertainty outranks unsupported confidence.**
> `constitution/core/03-Core-Principles.md`, Principle 16.

**Any change that would reduce the uncertainty a run records must state what evidence justifies the
reduction.** Not what makes the output read better, not what makes a gate easier to pass — what
evidence.

This applies to more changes than it first appears: softening a gate criterion, adding a fourth
evidence tag, letting a confidence level be set by hand, permitting a template section to be
omitted, or widening any waiver. **Each is locally reasonable and each spends the same
property.** If you cannot name the evidence, the change is a preference and should be argued as one.

---

## Changes that need a stronger argument than usual

Some parts of this framework are load-bearing in ways that are not obvious. Before
changing any of these, state which limitation you are fixing and what it would break:

- **`declared_shortfall` stays an exception to `04-problem` only.** The moment any gate can
  be waived by declaration, no gate binds anywhere.
- **The status quo stays in `05-competition`'s gate.** It is the largest competitor in most
  markets and the first thing dropped for being unglamorous.
- **Three solution options stays hard in `07-strategy`.** Every request to relax it comes
  from a run where the answer felt obvious — exactly the runs where a second option is
  worth most.
- **Exactly one north star metric in `12-metrics`.** A balanced set relocates the priority
  decision into whichever meeting the conflict surfaces in.
- **The evidence tags stay three, with no partial credit.** Every intermediate tier
  invented for this purpose becomes the default within a few runs.
- **`01-idea` never renders a verdict.** A score at that stage is preference wearing a
  number, and eleven modules inherit it as a finding.
- **Neither skill file self-modifies.** Both are edited deliberately, in a commit, like any
  other framework change. A skill that rewrites itself during a run diverges per machine,
  conflicts on `git pull`, and quietly makes one user's method different from everyone
  else's — which is the one property this framework cannot afford to lose. If a session
  learns something durable, say so and change it here on purpose.
- **`inconclusive` and `blocked` stay separate validation outcomes.** They look like a
  distinction without a difference until a run reports a distribution failure as a demand
  failure and kills a product nobody was ever asked about.
- **The six claims stay six.** Existence, frequency, severity, business impact, solution
  demand, willingness to pay. Every proposal to merge them arrives as "these are really the
  same thing at different strengths" — and the merge always runs in the direction that lets
  problem evidence stand in for demand evidence.
- **A generated option stays marked.** The mark costs one field and looks redundant on every
  run where the generated option loses. It is worth its cost only on the runs where it wins,
  which are the runs where the recommendation changed.
- **`development_authorized` is never set by a run**, and the readiness states stay five.
  Collapsing them into one "ready" flag is the single most requested simplification and the
  one that converts a research framework's output into a build authorization.
- **`state.version` gating stays.** It is what lets a required check be added without
  rewriting history. A change that makes a new check fail an older run has broken the
  property that makes completed runs worth keeping.
- **Technical feasibility, product demand, willingness to pay and business viability stay
  four separate judgements.** The merge always arrives as "these are all just viability", and
  it always runs in the direction that lets a passed feasibility gate stand in for the three
  that were not passed. A run that specified a buildable product nobody was shown to want
  must be able to say exactly that, in one sentence, without hedging any of the four.
- **A run may recommend against building, and nothing may be added that makes that harder to
  reach.** An operator whose run ended in "do not build yet" named it the most valuable
  outcome they got — they had expected a development-ready specification and the research
  established that technical completeness is not product validation. Every change that
  smooths the path from a complete artifact set to a build is spending that property.
- **The six failure classes stay six, and `insufficient_evidence` never merges with
  `failed_validation`.** They read as degrees of the same thing and they are not: one means
  nobody asked, the other means somebody answered no. The merge always runs in the direction
  that converts an unasked question into a negative result, which kills products that were
  never tested.

**And read `state.confirmed_value` in every run you are folding lessons from.** It records
mechanisms an operator confirmed were worth their cost. The friction log tells you what went
wrong; that key is the only thing that tells you what went right, and **a mechanism that costs
effort in every module and appears in no friction entry looks exactly like a candidate for
simplification.** It is a record of confirmation rather than a prohibition — you may still
change what it names, but the change must state what replaces the property it provided.

Each module's `learn/20-Future-Improvements.md` lists that module's real limitations and
what should not change. Read the relevant one before proposing a change to it.
