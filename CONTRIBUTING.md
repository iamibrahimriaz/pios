# Contributing

Product Intelligence OS is a body of method, not a program. Contributions are
prose, structure and judgment rather than code — which makes the bar different
from a typical repository, and worth stating clearly.

---

## Before you start

```bash
pip3 install -r requirements.txt
python3 framework/engine/validate.py
```

It must exit 0 before you change anything, and again before you open a pull
request. Twenty-two checks: YAML parses, required files exist, the dependency graph
is complete and acyclic, gate criteria match their documentation, the manifest
and the modules agree, prerequisites resolve, skills are valid and do not
self-modify, no run content is tracked, spelling is American.

If you use Claude Code, the `/pios-author` skill loads the authoring rules for
you. Otherwise read [`framework/AUTHORING.md`](framework/AUTHORING.md) — it is
the specification, and this file does not repeat it.

---

## What is most useful

| Contribution | Why it is wanted |
| --- | --- |
| **A defect found by running it** | The single most valuable thing right now. Especially a gate you could not pass honestly, or a template you could not fill |
| **A vertical pack** in `framework/packs/` | Domain knowledge — regulatory landscape, incumbents, standard entities — that specializes a run |
| **A gate criterion that closes a real gap** | Each module's `learn/20-Future-Improvements.md` lists its own known limitations. Start there |
| **An anti-example** | A filled-in artifact that looks plausible and is wrong. These teach more than correct examples. Write it from scratch — never harvest one from a real run |

---

## Runs are never contributed

**Do not attach a completed run to an issue or a pull request.** Nothing under
`projects/` or `examples/` is tracked by git, and a structural check fails the
build if any of it appears. This is not a formality — a run carries real market
research, named customers, pricing and unreleased strategy, and none of it is
this project's to publish.

What crosses back into the framework is the defect, stated so it stands on its own:

| Not this | This |
| --- | --- |
| "In my run, the pricing gate failed" | "The pricing gate cannot be passed when the buyer and the user are different people" |
| "Module 05 missed the obvious incumbent" | "05-competition's gate does not force the incumbent platform to be named" |

If the reasoning only makes sense with your run in front of you, it is not a
framework change yet. Nothing needs to be redacted, because nothing is sent.

---

## The rule that decides where content goes

> If an agent mid-run would **act differently** for having read it, it belongs in
> `core/`. If it explains why the module exists to a human, it belongs in
> `learn/`.

An executing agent reads `core/`, `knowledge/` and `resources/`, and **skips
`learn/` entirely**. Nothing in `learn/` may carry an operating instruction —
the agent will never see it. This is the most common mistake in contributions to
this project.

---

## Traps that have already caught someone

**Quote gate criteria beginning with `>=`.** Unquoted, YAML reads `>` as a folded
block scalar and the file silently fails to parse. This defect sat in seven of
fourteen `module.yaml` files undetected, because nothing had ever parsed them.

```yaml
gate:
  - ">= 3 trends with direction and evidence"      # correct
  - '"Do nothing / status quo" evaluated'          # correct
```

**Gate criteria must match word for word** between `module.yaml` and
`core/11-Quality-Gate.md`. `module.yaml` is the source of truth. The validator
enforces this; it was added after finding thirteen headings that paraphrased
their criteria.

**Never invent a citation.** The `18-References.md` files are *methodology* —
they route a question to a source type and mark what is structurally unsourceable
before launch. A fabricated title, author or page number is the exact failure the
evidence policy exists to prevent, and it is grounds for rejecting a pull request
outright.

**American spelling.** Enforced by the validator.

---

## Changes that need a stronger argument than usual

Some constraints look arbitrary and are load-bearing. A pull request touching one
should say which limitation it fixes and what it would break.

- **`declared_shortfall` stays an exception to `04-problem` only.** The moment any
  gate can be waived by declaration, no gate binds anywhere.
- **The status quo stays in `05-competition`'s gate.** It is the largest
  competitor in most markets and the first thing dropped for being unglamorous.
- **Three solution options stays hard in `07-strategy`.** Every request to relax
  it comes from a run where the answer felt obvious — exactly the runs where a
  second option is worth the most.
- **Exactly one north star metric in `12-metrics`.** A balanced set relocates the
  priority decision into whichever meeting the conflict surfaces in.
- **Three evidence tags, no partial credit.** Every intermediate tier invented for
  this purpose becomes the default within a few runs.
- **`01-idea` never renders a verdict.** A score at that stage is preference
  wearing a number, and eleven modules inherit it as a finding.

Each module's `learn/20-Future-Improvements.md` also lists what should *not*
change in that module, and why. Read the relevant one first.

---

## House style

Match the surrounding files. Short paragraphs, one idea each. `#` for all
headings — this repository does not use a single-H1 convention, so MD025 linter
warnings are expected and are not defects. `>` blockquotes for principles. Tables
for anything comparative. Close each file with a `> **X Principle**` block.

**Give the cost of doing it wrong, not just the instruction.** "Ask which
country" beats "consider the regulatory context." Avoid motivational filler and
advice that would apply to any framework.

---

## Pull requests

State which limitation you are addressing, and what it would break. A change to
one module is frequently a change to several, because outputs flow downstream —
so say what you traced.

A pull request is likely to be accepted when it:

- Names a specific limitation, ideally one the project already documents
- Passes the validator
- Keeps the four-layer separation intact
- Reads like the files around it

A pull request is likely to be declined when it:

- Softens a gate because a run found it inconvenient
- Adds an evidence tier, a second north star, or a verdict to `01-idea`
- Moves operating instructions into `learn/`, or curriculum into `core/`
- Cites a source that cannot be retrieved

---

## Reporting a problem

Say which module, which gate, and what you were doing. A report reading "module
04's third criterion cannot be satisfied honestly for a pre-launch consumer
product, because…" is directly actionable. "The framework is too strict" is not.

If a gate genuinely cannot be passed honestly, that is a defect in the gate and
worth raising. The framework is meant to be demanding, not impossible.

---

## Licensing

Contributions are accepted under the [MIT License](LICENSE), the same terms the
project ships under.
