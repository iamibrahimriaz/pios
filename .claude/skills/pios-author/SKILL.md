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

## Self-learning mode (ALWAYS ON)

This skill improves itself. Treat every task as a chance to make this skill more expert —
always target becoming more skillful.

**After any task that used this skill** — and immediately whenever you discover something
durable mid-task — update this skill (`SKILL.md`, and/or its `reference/` files) to encode
what you learned, so the next session starts smarter. This is a standing instruction, not
optional.

**Capture** (what makes the skill more skillful):
- Corrected assumptions or facts the skill got wrong, omitted, or that have since changed.
- Non-obvious gotchas, pitfalls, and "I wish I'd known that" moments.
- New/changed file locations, commands, conventions, or tooling realities.
- A sharper workflow or better step ordering than what's written here.

**Do NOT capture:** one-off conversation details, secrets/credentials, anything already
covered here, or task-specific scratch notes. Keep edits tight and high-signal — append to
the right existing section, never bloat. Every edit must make the skill strictly better.

**Self-check before you finish a task:** "What did I learn that this skill should have told
me up front?" If anything, write it in now.

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

It must exit 0 before you start and again before you finish. Twenty checks. Read
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

It must exit 0. Nineteen checks: YAML parses, required files exist, dependency graph is
complete and acyclic, gate parity holds, manifest and modules agree, prerequisites
resolve, no stale identifiers, American spelling.

Then walk `AUTHORING.md`'s submission checklist. The item most often missed is the last
one: **nothing in `learn/` that an agent needs to execute correctly.**

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

Each module's `learn/20-Future-Improvements.md` lists that module's real limitations and
what should not change. Read the relevant one before proposing a change to it.
