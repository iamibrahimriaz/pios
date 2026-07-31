# Using Product Intelligence OS

How to install it, run it, and get the output where you need it.

If you only read one section, read [Which mode do you want](#which-mode-do-you-want).

---

## What you are installing

Product Intelligence OS is **not a program.** It is a body of method — 611 markdown
files and 18 YAML files — that an AI agent reads and executes. It has no runtime of its
own.

You supply the agent. This repository supplies the discipline.

| | |
| --- | --- |
| **You need** | An AI coding agent that can read and write files. [Claude Code](https://claude.com/claude-code) is the reference implementation |
| **Plus** | `git`, and `python3` with PyYAML for the two validators |
| **You do not need** | Node, a database, an API key, or a build step |

---

## Install

```bash
git clone https://github.com/iamibrahimriaz/pios.git
cd pios
pip3 install -r requirements.txt
python3 framework/engine/validate.py
```

The last command must print **All structural checks pass.** If it does, you are ready.

Clone it **once**. Do not copy it into each project — it is 611 files of method with
nothing to do with your application's source, and copies drift apart within months.

---

## Which mode do you want

There are two ways to use it. Both work; they differ in where your research output
lands.

### Mode 1 — Workspace (default, nothing to configure)

You work inside the framework repository. Every run lives there.

```
~/Projects/pios/
  framework/                     the method
  projects/gym-memberships/      run 1
  projects/rug-estate/           run 2
```

**Choose this if** you want all your research in one place. Runs sit side by side, which
is what lets you notice patterns across them — that your market sizing is always
optimistic, or your timing verdict is always "right now". Each module's
`learn/17-Reflection.md` asks you to look for exactly those patterns, and they are
invisible when runs are scattered.

**Nothing to set up.** Open Claude Code in the repository and go.

### Mode 2 — External (`PIOS_HOME`)

You work in your own project. The framework stays where you cloned it; the run output
lands in the project you are working on.

```
~/Projects/pios/                       the framework — read-only, never written to
~/Projects/my-app/
  pios/my-app/                         the run lives here
    state.yaml
    deliverables/                      the 15 artifacts
  src/
```

**Choose this if** you want the research to live beside the code it describes, so your
coding agent can read `12-Build-Handoff.md` from inside the same repository it is
building in.

---

## Setting up Mode 2

Two steps: install the skill globally, and tell it where the framework is.

### Automatic

```bash
cd ~/Projects/pios
./scripts/install-skill.sh
```

It symlinks the skill into `~/.claude/skills/` — a link rather than a copy, so
`git pull` updates your installed skill too — and prints the one line to add to your
shell profile.

### Manual

```bash
# 1. make the skill available everywhere
ln -s ~/Projects/pios/.claude/skills/pios ~/.claude/skills/pios

# 2. tell it where the framework lives  (add to ~/.zshrc or ~/.bashrc)
export PIOS_HOME="$HOME/Projects/pios"
```

Restart your terminal, then check:

```bash
echo $PIOS_HOME
python3 "$PIOS_HOME/framework/engine/validate.py"
```

### Two things to know about the global install

**Inside the framework repository, `/pios` exists twice** — once project-scoped, once
global. They are the same file, because the installer creates a symlink rather than a
copy, so whichever loads behaves identically. It is only ever a duplicate listing, never
a conflict.

**The symlink points at your clone.** If you move or delete the repository, `/pios`
breaks. Re-run `./scripts/install-skill.sh` from the new location. The upside of a link
over a copy is that `git pull` updates your installed skill automatically.

**Windows:** the installer is a bash script. Use WSL, or do it manually — create the
`~/.claude/skills/pios` link (or copy the folder) and set `PIOS_HOME` in your environment
variables.

### How the skill decides which mode it is in

```
framework/engine/run-order.yaml exists in the current directory?
   yes -> workspace mode:  framework is ./framework,  runs go to ./projects/<slug>/
   no  -> is PIOS_HOME set and valid?
             yes -> external mode: framework is $PIOS_HOME/framework,
                                   runs go to ./pios/<slug>/
             no  -> it stops and tells you to set PIOS_HOME
```

It will never guess a location or run without the framework.

---

## Running a session

From either mode, in Claude Code:

```
/pios   an app that helps small gyms manage memberships
```

That is the whole interface. To pick a run back up later — a full run does **not** fit
in one session — invoke `/pios` again in the same directory. It finds the existing
`state.yaml` and resumes from the next unpassed module.

```
/pios                          continue where I left off
/pios   what stage am I at?    status only, no work
```

### What actually happens

It is an interview, not a button. The run **stops three times** and hands control back
to you.

| Stop | What it asks |
| --- | --- |
| After module 01 | At least five clarifying questions. Jurisdiction and who pays are not optional — the agent is forbidden from guessing them |
| After module 07 | Confirm the MVP cut. It is a commercial commitment, not a research finding |
| Before delivery | Review the artifact set and the stated confidence |

Between those, if something is genuinely undecidable, it stops and asks rather than
picking a plausible answer.

**Expect hours of agent work across several sessions**, not seconds. Fourteen gated
modules, each with an adversarial review pass. It was not designed to be fast.

---

## What you get

Fifteen required artifacts, plus two more when the scope calls for them.

```
<run>/deliverables/
  00-Executive-Summary.md      opens with: build, adjust, or do not build
  01-Research-Dossier.md
  02-Problem-Validation.md
  03-PRD.md
  04-Feature-Spec.md
  05-Data-Model.md
  06-API-Contract.md
  07-Architecture.md
  08-UX-Flows.md
  09-Roadmap.md
  10-Risks-and-Assumptions.md
  11-Success-Metrics.md
  12-Build-Handoff.md          what to build, in what order
  16-Engineering-Setup.md      how to run, test and ship it
  14-Operations-Plan.md        who is awake, what it costs, whose name is on it
```

The last three are what a builder actually works from, and they hand over to each other
in that order.

### Checking the output

```bash
python3 "$PIOS_HOME/framework/engine/validate-run.py" pios/<slug>
```

Or, in workspace mode:

```bash
python3 framework/engine/validate-run.py projects/<slug>
```

This lints a finished run: dropped evidence tags, `«placeholder»` scaffolding left in a
delivered artifact, an empty evidence log, assumptions with no validation method,
confidence still `unknown`, and whether a declared shortfall or a cost breach was
actually carried through.

**A non-zero exit means the run is not deliverable.**

---

## Moving the output into your build

In workspace mode, copy the artifacts to wherever you are building:

```bash
mkdir -p ~/Projects/my-app/docs/product
cp projects/<slug>/deliverables/*.md ~/Projects/my-app/docs/product/
```

In external mode they are already in the project.

Then, in that repository, point your coding agent at them:

> Read `docs/product/12-Build-Handoff.md` and `docs/product/16-Engineering-Setup.md`,
> then start on milestone 1.

The Build Handoff is written to be read with no other context — that is its first
acceptance criterion.

---

## Extending the framework

A second skill, for changing the framework rather than using it:

```
/pios-author   add a vertical pack for healthcare
```

This one only runs **inside** the repository, since it edits the framework. See
[CONTRIBUTING.md](CONTRIBUTING.md) and [`framework/AUTHORING.md`](framework/AUTHORING.md).

---

## Without Claude Code

The skills are a convenience, not a requirement. Any agent that reads and writes files
can run this:

> Read `AGENTS.md` in this repository and follow it. My idea is: «one sentence».

`AGENTS.md` is the complete operating manual — startup sequence, per-module loop, the
rules it may not break, and how to know when it is finished.

---

## Troubleshooting

**"I cannot find the framework."**
`PIOS_HOME` is unset or wrong. `echo $PIOS_HOME` and check the path contains
`framework/engine/run-order.yaml`. If you set it in a profile, restart the terminal.

**`/pios` does not appear.**
In workspace mode, confirm you opened Claude Code at the repository root — the skill is
project-scoped. In external mode, confirm `~/.claude/skills/pios/SKILL.md` exists and
restart the session.

**`ModuleNotFoundError: No module named 'yaml'`**
`pip3 install -r requirements.txt`.

**The run stopped and asked me something.**
That is the design. Jurisdiction, buyer and the MVP cut cannot be inferred, and the
framework forbids the agent from picking a plausible answer.

**A gate cannot be passed honestly.**
That is a defect in the gate, not user error. Open an issue using the
*"A gate cannot be passed honestly"* template — it is currently one of the most useful
reports this project can receive.

**The agent wants to change the framework mid-run.**
It should not. The framework is read-only during a run. If it is genuinely wrong, stop
and use `/pios-author`.

---

## A note on where this stands

The framework is complete and structurally validated — 22 checks, all passing — and
**has not yet been proven by a published run.**

**Your runs stay yours.** Nothing under `projects/` or `examples/` is ever
committed — `.gitignore` excludes it and a structural check fails the build if
anything slips through. The framework is open source; the research you put through
it is not, and no run of yours will appear in this repository or anyone else's.

If you use it, the most valuable thing you can contribute is what broke — the
defect, not the project. See [CONTRIBUTING.md](CONTRIBUTING.md).
