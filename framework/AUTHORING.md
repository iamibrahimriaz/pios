# Authoring a Module

This document defines what belongs in every file of a Product Intelligence OS module.

It exists so that a module written today and a module contributed a year from now behave
identically when an agent executes them. Consistency is not an aesthetic preference here —
the engine reads these files positionally, and an agent that finds a workflow where it
expected a framework will improvise.

**Reference module:** `modules/01-idea/` is complete and canonical. When this document and
that module disagree, the module is right and this document needs updating.

---

## The Four Layers

| Layer | Answers | Read by | Required |
| --- | --- | --- | --- |
| `core/` | How do I *do* this? | the agent | yes |
| `knowledge/` | What do I need to *know*? | the agent | yes |
| `resources/` | What can I *reuse*? | the agent | as available |
| `learn/` | Why does this matter? | humans | optional |

Plus `module.yaml` — the machine-readable contract. Not optional.

The split between `core/` and `learn/` is load-bearing. An executing agent reads `core/`
and skips `learn/` entirely. Content in the wrong layer either bloats the agent's context
with curriculum or hides operating instructions where the agent will not look.

**The test:** if an agent mid-run would act differently for having read it, it belongs in
`core/`. If it explains why the module exists to a human, it belongs in `learn/`.

---

## `module.yaml` — the contract

Write this **first**, before any prose. It forces you to decide what the module actually
produces, and everything in `core/` then serves those outputs.

```yaml
id: 05-competition
name: Competition
purpose: One sentence. What this module establishes.
depends_on: [02-market, 03-user, 04-problem]
consumes: [market_definition, segments, ranked_problems]
produces: [competitor_matrix, gap_analysis, positioning]
feeds_deliverables: [research-dossier, executive-summary]
gate:
  - Objectively checkable criterion
  - Another one
on_fail: return to 02-market
```

Rules:

- `produces` names must be stable — later modules reference them via `consumes`.
- Every name in `produces` must appear in `state.outputs` by the time the gate runs.
- Gate criteria must be **checkable**. "Research is thorough" is not a criterion.
  "≥5 competitors identified with sources" is.
- `on_fail` names a real module, or `halt and request input from the human operator`.
- Every name in `feeds_deliverables` must exist in `deliverables/manifest.yaml`.

---

## `core/` — the eleven operative files

An agent reads these in numeric order. Each has one job. Do not blend them: a workflow
buried inside a principles document does not get executed.

### `00-Purpose.md`
What this module establishes and why it exists in the sequence. Scope: what it covers and
explicitly what it does not, with a pointer to the module that does. Orientation, not
instruction.

### `03-Core-Principles.md`
The domain-specific beliefs that govern judgment here. Numbered, each with a short
justification. These are the rules an agent falls back on when the workflow does not
cover a situation.

### `04-Mental-Models.md`
Ways of *seeing* the domain — lenses, not procedures. Each model states what it reveals
that the others do not. Include when to combine them.

### `05-Best-Practices.md`
What experienced practitioners do that inexperienced ones do not. Concrete and
transferable. If a line could appear in any module unchanged, it is too generic to keep.

### `06-Framework.md`
**The method.** The repeatable procedure for this domain, in named steps or passes, each
producing something concrete. This is the most important file in `core/`.

Requirements:
- Named, ordered stages
- Each stage states what it **produces**, mapped to `module.yaml`'s `produces`
- Explicit statement of which stages may not be skipped
- A "common failures" section with the cost of each

### `07-Workflow.md`
**The procedure.** What `06-Framework.md` looks like as executable steps: read this, write
that, check this, stop here.

Requirements:
- Position in the run, with dependencies
- Numbered steps from initialization to handoff
- Which state fields are written at each step
- The review step, the gate step, and any human checkpoint
- A **handoff contract**: exactly what the next module will read, and from where

### `08-Questions-To-Answer.md`
The interrogation bank. Grouped by theme. Every question states what goes wrong if it is
unanswered.

Distinguish clearly:
- **Internal** questions the agent answers from research
- **Operator** questions only a human can answer

Include the asking test — *would a different answer change the work?* — and an
anti-patterns table. Questions that fail the test do not count toward gate minimums.

### `09-Research-Methodology.md`
How to establish evidence in this domain, and how deep to go.

Requirements:
- What research belongs in this module
- What belongs to **other** modules, named explicitly — this prevents duplicated and
  premature work
- Domain-specific sourcing guidance: what counts as a good source here
- What to do when retrieval is unavailable
- Timeboxing guidance

### `11-Quality-Gate.md`
Expands each `module.yaml` gate criterion into: what passing requires, how to test it, and
a fails/passes example.

Must include:
- The governing rule — uncertainty is a fail, not a pass
- The universal gates most often missed in this module
- A worked verdict block in YAML
- On-failure behavior, including the three-attempt limit
- "What a passing module looks like"

### `12-Checklist.md`
Everything to verify **before** reaching the gate, in execution order: entry, per-stage,
research, assembly, state, review, gate, exit.

End with a **red flags** section — symptoms that mean the module should be re-run
regardless of whether the gate technically passed.

### `13-Template.md`
The working output document for this module, written to `projects/<slug>/research/<id>.md`.

Requirements:
- Usage instructions and marker conventions above a clear separator
- Sections mapping to the framework's stages
- Evidence tags on every factual claim
- A handoff section naming exactly what the next module consumes
- An evidence standing summary
- A completion check in an HTML comment, removed when done

State plainly: a section that cannot be filled is a finding. Never delete a section to
hide a gap; never write filler to occupy one.

---

## `knowledge/` — what to know

Domain concepts, terminology, methods and models. One file per concept, named for the
concept (`TAM.md`, `Five-Forces.md`, `Jobs-To-Be-Done.md`) — not numbered.

Subdirectories where a module spans several sub-domains, as in
`09-technology/knowledge/{architecture,database,api,security,scalability}/`.

Each file: what the concept is, when it applies, how to apply it here, and where it
misleads. That last part matters most — a framework applied outside its range produces
confident nonsense.

Knowledge is **reference**, not procedure. An agent consults it when the workflow calls
for a concept it needs. If a file tells the agent what to *do*, it belongs in `core/`.

---

## `resources/` — what to reuse

`14-Examples.md`, `15-Anti-Examples.md`, `18-References.md`, plus subdirectories as real
content accumulates.

**Do not pre-create empty resource directories.** Empty scaffolding reads as coverage that
does not exist. A directory appears when there is something to put in it.

Anti-examples are worth more than examples. A filled-in artifact that looks plausible and
is wrong, annotated with *why* it is wrong, teaches more than a correct one.

---

## `learn/` — human curriculum

`01-Why-It-Matters`, `02-Learning-Objectives`, `10-Common-Mistakes`, `16-Evaluation`,
`17-Reflection`, `19-Related-Modules`, `20-Future-Improvements`, `README`.

Written for a person learning product management, not for an executing agent. This layer
is what makes PIOS usable as a curriculum as well as a machine — but it must never carry
operating instructions, because the agent does not read it.

---

## Frontmatter

Every `core/` and `learn/` file carries:

```yaml
---
Title: Framework
Module: 01-idea
Section: core
Category: Method
Version: 1.0.0
Status: Approved
Owner: Product Intelligence OS
Review Cycle: Every 6 Months
Purpose: One sentence.
Audience: [AI Agents, Product Managers]
Prerequisites: [paths that must be read first]
Outputs: [what reading this enables]
Related Modules: [ids in the current scheme]
Tags: [...]
---
```

Rules:

- `Module` and `Related Modules` use **current** ids (`03-user`, not `04-Users`).
  Stale references are the most common defect when the scheme changes.
- `Section` is the directory name: `core`, `learn`.
- Omit `Created` / `Last Updated` rather than leaving `YYYY-MM-DD` placeholders. Git
  records dates; a placeholder date is worse than no date.
- `Prerequisites` are real paths, checkable by a script. Paths resolve against
  `framework/modules/`, `framework/constitution/`, `framework/`, or the citing file's own
  directory — in that order. The one permitted non-path form is a semantic precondition
  reading `<module> gate passed` (or `<a> and <b> gates passed`); anything else is a
  defect. Run `python3 framework/engine/validate.py` to check.
- **Gate criteria that begin with `>=` must be quoted** in `module.yaml`. Unquoted, YAML
  reads `>` as a folded block scalar and the file fails to parse — silently, because
  nothing reads these files until an agent does. The same applies to any criterion
  starting with a quote character.

---

## House Style

Match `modules/01-idea/` and `constitution/`:

- Short paragraphs. One idea each.
- `#` for section headings throughout — this repo does not use a single-H1 convention.
- `>` blockquotes for principles and warnings.
- Tables for anything comparative.
- Close each file with a `> **X Principle**` block.
- **American spelling**, consistently.
- Concrete over abstract. "Ask which country" beats "consider the regulatory context".
- Give the cost of doing it wrong, not just the instruction.

Avoid: motivational filler, restating the constitution, generic advice that would apply to
any module unchanged, and sections written to satisfy the template while saying nothing.

---

## Authoring Order

Working in this order avoids rewrites:

1. `module.yaml` — decide the contract
2. `13-Template.md` — decide the output
3. `06-Framework.md` — decide the method that fills it
4. `07-Workflow.md` — turn the method into steps
5. `08-Questions-To-Answer.md` — the interrogation the method needs
6. `09-Research-Methodology.md` — how evidence gets established
7. `11-Quality-Gate.md` — expand the contract's criteria
8. `12-Checklist.md` — everything above, as verification
9. `00`, `03`, `04`, `05` — purpose, principles, models, practices
10. `knowledge/`, `resources/`, `learn/`

Output first, prose last. A module written in the opposite order produces beautiful
principles that do not connect to anything the engine consumes.

---

## Before Submitting a Module

- [ ] `module.yaml` complete; every `produces` name used by a downstream `consumes` or deliverable
- [ ] All eleven `core/` files present and non-empty
- [ ] `13-Template.md` sections map to `06-Framework.md` stages
- [ ] Gate criteria in `11-Quality-Gate.md` match `module.yaml` exactly
- [ ] `07-Workflow.md` handoff contract matches the downstream module's `consumes`
- [ ] Every `Related Modules` reference uses current ids
- [ ] No `YYYY-MM-DD` placeholders
- [ ] No empty directories
- [ ] American spelling throughout
- [ ] Nothing in `learn/` that an agent needs to execute correctly
- [ ] `python3 framework/engine/validate.py` exits 0

---

> **Authoring Principle**
>
> A module is not a document about a domain.
>
> It is a set of instructions that produces a specific output, reliably, by an agent
> that has never seen this domain before.
