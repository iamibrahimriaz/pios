# Product Intelligence OS

> **The research stage before the code.**
>
> AI made building cheap. It made building the wrong thing cheap too.

[![validate](https://github.com/iamibrahimriaz/pios/actions/workflows/validate.yml/badge.svg)](https://github.com/iamibrahimriaz/pios/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

You describe a product idea in one sentence. PIOS researches it, argues with it, specifies it,
and hands you the documents an engineer or a coding agent starts building from.

**Or it tells you not to build it — and that is a complete, successful result.**

---

## What it actually is

PIOS is **not a program.** It is a body of method — 623 markdown files and 18 YAML files —
that an AI coding agent reads and executes. You supply the agent; this repository supplies the
discipline.

It runs **14 gated research modules** in sequence: market, users, problem, competition,
business, strategy, then product and technical specification. Every factual claim it writes
carries a source tag. Every module has a gate it must pass before the next one starts. When a
gate cannot be passed honestly, the run stops rather than proceeding on a guess.

| | |
| --- | --- |
| **Input** | One idea, loosely described |
| **Process** | 14 modules · gated · evidence-bound · 3 human checkpoints |
| **Output** | 15–17 documents in `./pios/<slug>/`, or a documented "not yet" |
| **Time** | Hours across several sessions. It was not designed to be fast |

---

## Install

### Claude Code

```bash
claude plugin marketplace add iamibrahimriaz/pios
claude plugin install pios@pios
```

That is the whole install. No clone, no environment variable, no Python.

### Gemini CLI

```bash
gemini extensions install https://github.com/iamibrahimriaz/pios
```

### Any other agent

Clone this repository beside your project and tell the agent to read [`AGENTS.md`](AGENTS.md).
That file is the complete operating manual — startup sequence, per-module loop, the rules it
may not break, and how to know when it is finished.

**Requirements:** an AI coding agent that can read and write files.
**Python is not required to run PIOS** — only for the two optional validators.

---

## Use it

From **any** project directory:

```
/pios   an app that helps small gyms manage memberships
```

The run lands in `./pios/gym-memberships/` — beside the code it describes.

```
/pios                          resume where you left off
/pios   what stage am I at?    status only, no work
```

A full run does not fit in one session. Invoking `/pios` again finds the existing `state.yaml`
and continues from the next unpassed module.

### It is an interview, not a button

**The run stops three times and hands control back to you.** This is the design, not a
malfunction — an agent that guesses your jurisdiction produces a confident plan for the wrong
country.

| Stop | What it asks |
| --- | --- |
| After module 01 | At least five clarifying questions. Jurisdiction, who pays and delivery surface are not optional — it is forbidden from guessing them |
| After module 07 | Confirm the MVP cut. That is a commercial commitment, not a research finding |
| Before delivery | Review the artifact set and the stated confidence |

Between those, when something is genuinely undecidable, it stops and asks rather than picking a
plausible answer.

---

## What you get

```
./pios/<slug>/
├── DECISION.md              one page — read this first
├── CLAUDE.md                what an AI agent reads to start building
│
├── 00-decision/             the recommendation and what it rests on
│     00-Executive-Summary.md
├── 01-research/             the evidence base, and the limits of it
│     01-Research-Dossier.md · 02-Problem-Validation.md · 10-Risks-and-Assumptions.md
├── 02-product/              what it is, who for, how it wins
│     03-PRD.md · 04-Feature-Spec.md · 08-UX-Flows.md · 15-AI-Strategy.md
├── 03-technical/            how it is built
│     05-Data-Model.md · 06-API-Contract.md · 07-Architecture.md
├── 04-delivery/             how it ships, and how it is run afterwards
│     09-Roadmap.md · 11-Success-Metrics.md · 12-Build-Handoff.md
│     13-Growth-Plan.md · 14-Operations-Plan.md · 16-Engineering-Setup.md
│
├── proposal/                proposal.html — send this to get a yes
├── presentation/            engineering-kickoff.pptx
├── phases/                  the board: what may be started now
└── milestone-zero/          only when the strategy says validate first
```

**The two a builder actually works from:**

- **`12-Build-Handoff.md`** — what to build, in what order, and what "correct" means. It stands
  completely alone; it assumes no access to the research conversation.
- **`16-Engineering-Setup.md`** — how to run, test and ship it. Environment, secrets, seed data,
  test strategy, CI, deployment, pre-launch checklist.

Together they take a coding agent from an empty directory to a verified deploy. From there,
`14-Operations-Plan.md` takes over.

**Four audiences, four documents.** The specification is written for the builder. The person
deciding whether it gets funded will not read sixteen files — they get `DECISION.md` and the
proposal. An agent opening the folder cold gets `CLAUDE.md`. None is optional, and a run that
concludes *do not build* still produces every one.

### Then hand it to your builder

```
Read pios/gym-memberships/12-Build-Handoff.md and start Phase 1.
```

**PIOS never writes application code.** The handoff is the last research artifact, not the
first build step — pair it with [Superpowers](https://github.com/obra/superpowers), spec-kit,
or whatever you already build with.

---

## How it works

```
   frame          research              decide          specify       operationalise    deliver
 ┌────────┐  ┌──────────────────┐  ┌─────────────┐  ┌───────────┐  ┌──────────────┐  ┌────────┐
 │01 idea │─▶│02 market         │─▶│06 business  │─▶│08 product │─▶│10 execution  │─▶│ 15–17  │
 │        │  │03 user           │  │07 strategy  │  │09 tech    │  │11 growth     │  │ docs   │
 │ ▲ asks │  │04 problem        │  │ ▲ confirm   │  │14 ai      │  │12 metrics    │  │ ▲      │
 │        │  │05 competition    │  │             │  │           │  │13 operations │  │ review │
 └────────┘  └──────────────────┘  └─────────────┘  └───────────┘  └──────────────┘  └────────┘
```

A module may not start until every module it depends on has **passed its gate**. A failed gate
stops the run. Three failures on one module halt it and escalate to you.

Each of the 14 modules carries four layers:

| Layer | Teaches | Read by |
| --- | --- | --- |
| `core/` | How to think — frameworks, workflow, questions, quality gate | the agent |
| `knowledge/` | What to know — concepts, terminology, methods | the agent |
| `resources/` | Templates, examples, **anti-examples** | the agent |
| `learn/` | Curriculum — why it matters, reflection | humans only |

Plus a `module.yaml` — its machine-readable contract: what it depends on, what it consumes,
what it produces, and the gate it must pass.

---

## What makes it different is what it refuses to do

Plenty of tools will write you a PRD. These are the rules that make this one worth the hours:

**Every claim carries exactly one tag.**

```
[verified: <source>]              checked against a named, retrievable source
[inferred: <basis>]               reasoned from something verified
[assumption: needs validation]    believed, not established
```

An untagged claim is a defect. **An assumption is never smoothed into a fact** — a blueprint
that states what it assumed is useful; one that silently asserts it is a liability.

**Gates fail.** Uncertainty about a gate is a fail, not a pass. A gate that never fails is not
a gate.

**Six claims about a problem are never collapsed into one.** Existence · frequency · severity ·
business impact · solution demand · willingness to pay. Evidence for one is not evidence for
another. *A problem can be real, recurring and expensively documented, and people will still
not pay to prevent it.*

**"Insufficient evidence" is never reported as "failed validation."** The error always runs in
that direction, and it converts *we did not ask* into *they said no*. Six failure classes keep
them apart.

**A late answer forces a re-derivation, not a find-and-replace.** If an early premise changes
after that module passed, every conclusion since is retested to a verdict — survived, changed,
or withdrawn.

**Engineering-ready is not development-authorized.** No run sets it. A count of ticked
engineering boxes says the product is specified; it says nothing about whether anyone will pay
for it.

**Runs are private.** Yours never leave your machine. `.gitignore`, a structural check and a CI
step all enforce it.

---

## Checking the output

Optional, and the only thing that needs Python:

```bash
pip3 install -r requirements.txt
python3 framework/engine/validate-run.py ./pios/<slug>
```

This lints a **finished run** for what a tired agent stops doing: dropped evidence tags,
`«placeholder»` scaffolding left in a delivered artifact, an empty evidence log, assumptions
with no validation method, confidence still `unknown`, an identifier a code block operates on
that no code block defines. **A non-zero exit means the run is not deliverable.**

To check the **framework** instead:

```bash
python3 framework/engine/validate.py       # 40 structural checks
```

---

## Status

**Complete and structurally validated. Not yet proven by use.**

| | |
| --- | --- |
| Framework | Complete — 14 modules, 4 layers each, 15 required deliverables |
| Structural checks | 40, all passing |
| Plugin install | Verified working from a directory outside the repository |
| Reference runs | **Not published** — see below |
| Vertical packs | Planned, not built |

Every claim about *structure* here is verified. **No claim about *outcomes* has been tested by
a published run.**

**Completed runs are not published here, and will not be.** A run carries real market research,
named customers, pricing and unreleased strategy — the framework is open; what people put
through it is theirs.

What crosses back into the framework is **the defect, never the project.** If you run it and
something broke — a gate you could not pass honestly, a template you could not fill — that is
the most valuable contribution available, and it needs none of your research to be useful.

---

## Repository layout

```
framework/          ships to users; read-only during a run
  constitution/       governing principles — how to think
  engine/             how a run executes — order, gates, evidence, state, review
  deliverables/       manifest.yaml — THE OUTPUT SPECIFICATION
  modules/            the 14 lifecycle domains
  packs/              optional vertical knowledge — planned, not yet built

skills/             /pios (run a session) · /pios-author (extend the framework)
commands/           /pios-learn — contribute a defect back as a pull request
.claude-plugin/     plugin.json + marketplace.json — the install manifests
AGENTS.md           how an agent executes a run — start here
```

---

## Contributing

| | |
| --- | --- |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to add or improve a module, gate or template |
| [CLAUDE.md](CLAUDE.md) | Read this first if you are an AI agent |
| [framework/AUTHORING.md](framework/AUTHORING.md) | The specification for framework changes |
| [CHANGELOG.md](CHANGELOG.md) | Release history, and the release ritual |
| [USAGE.md](USAGE.md) | Every install mode, and troubleshooting |

Run `/pios-learn` after a session to turn its friction log into a proposal and a pull request.
It writes nothing under `framework/`, and strips every project detail before anything leaves
your machine.

**All pull requests are reviewed and merged by the maintainer.**

---

## Guiding principle

> **Don't teach AI what to write. Teach AI how to think.**

The objective is not better documents. It is better decisions.

MIT © [Ibrahim Riaz](https://github.com/iamibrahimriaz)
