---
name: pios
description: >
  Run a Product Intelligence OS research session — turn one loosely described product
  idea into a build-ready blueprint of 15 gated, evidence-tagged artifacts. Starts a new
  run, resumes an existing one, or reports status. Invoke whenever someone wants to
  research, validate, scope, spec or plan a product idea in this repository: "research
  this idea", "run PIOS on X", "continue my run", "what stage is my project at", "is this
  idea worth building". Handles the full 14-module sequence, the three human checkpoints,
  and the run validator.
---

# Product Intelligence OS — Run a Session

You are executing a product research run using this repository's framework. One idea goes
in; fifteen build-ready artifacts come out, or an honest verdict that it should not be
built.

**This skill governs the session. `AGENTS.md` governs the work.** Read `AGENTS.md`
completely before producing anything — it is the operating manual and this file does not
repeat it.

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

---

## Step 0 — Locate the framework and the run directory

The framework can be used two ways. **Resolve which one you are in before anything else**,
because every other path in this file depends on it.

```bash
if [ -f framework/engine/run-order.yaml ]; then
  echo "MODE=in-repo";  echo "FRAMEWORK=$(pwd)/framework";  echo "RUNS=$(pwd)/projects"
elif [ -n "$PIOS_HOME" ] && [ -f "$PIOS_HOME/framework/engine/run-order.yaml" ]; then
  echo "MODE=external"; echo "FRAMEWORK=$PIOS_HOME/framework"; echo "RUNS=$(pwd)/pios"
else
  echo "MODE=unresolved"
fi
```

> **Read the two absolute paths out of that output and use them literally from now on.**
>
> Shell variables **do not survive between commands** — each one runs in a fresh shell, so
> `$RUNS` and `$PIOS_HOME` will be empty in every later step. A command like
> `mkdir -p "$RUNS"/my-idea` would expand to `mkdir -p /my-idea` and try to write at the
> filesystem root.
>
> Wherever this file writes `<FRAMEWORK>` or `<RUNS>`, substitute the actual absolute path
> the command above printed.

| Mode | You are | `<FRAMEWORK>` | `<RUNS>` |
| --- | --- | --- | --- |
| **in-repo** | Inside the PIOS repository | `<repo>/framework` | `<repo>/projects` |
| **external** | In any other project | `$PIOS_HOME/framework` | `<this project>/pios` |

**Record both paths in `state.yaml`** as `project.framework_path` and `project.run_dir` as
soon as you create it. A later session resumes by reading them from there rather than
re-deriving — which is what makes resume work when `PIOS_HOME` is set differently, or not
set at all, in that session.

**If unresolved**, stop and tell the operator exactly this, then wait:

> I cannot find the framework. Either run this from inside the Product Intelligence OS
> repository, or point `PIOS_HOME` at where you cloned it:
>
> `export PIOS_HOME="$HOME/Projects/product-intelligence-os"`
>
> Add that line to your shell profile to make it permanent. See `USAGE.md` in the
> framework repository.

Do not guess a location, and do not proceed without the framework. Every module's method
lives there; without it you would be improvising, which is the one thing this framework
exists to prevent.

`AGENTS.md` writes framework paths relative to the repository root — read those as
`<FRAMEWORK>/…` too.

**The framework is read-only during a run**, in both modes. Read from it; never write to
it. Everything you produce goes under `<RUNS>/<slug>/`. This includes not editing this
skill file mid-run: in external mode it lives inside someone's shared framework clone, and
a run must not change the method for every other project on the machine.

State the mode in one line before you begin, so the operator knows where output will land:
*"External mode. Framework at ~/Projects/product-intelligence-os. Writing to ./pios/."*

---

## Step 1 — Establish the mode before anything else

```bash
ls <RUNS>/*/state.yaml 2>/dev/null
```

| What you find | Mode |
| --- | --- |
| No `state.yaml` anywhere | **NEW RUN** |
| One or more exist | **RESUME** — never start a second run over an existing one |
| Operator asked "what stage / status" | **STATUS** — report and stop |

If a run exists and the operator describes a *different* idea, ask which they mean. Do not
overwrite `state.yaml`. Never rewrite `state.project.raw_idea` under any circumstances.

---

## Step 2A — NEW RUN

**Capture the idea verbatim first.** Before you interpret anything, write down the
operator's exact words. Everything else in the framework is downstream of this sentence,
and a paraphrase silently changes the project.

1. Choose a kebab-case slug from the idea — `gym-membership-manager`, not `project-1`.
2. Create the run directory:

   ```bash
   mkdir -p <RUNS>/<slug>/research <RUNS>/<slug>/deliverables
   cp <FRAMEWORK>/engine/state-schema.yaml <RUNS>/<slug>/state.yaml
   ```

3. Edit `state.yaml`: strip the commented examples, set `slug`, paste the operator's words
   verbatim into `raw_idea`, set `created`. Leave `jurisdiction` empty — module 01 asks
   for it.
4. Read, in this order, all under `<FRAMEWORK>/`: `constitution/core/`,
   `engine/evidence-policy.md` (twice), `engine/run-order.yaml`, `engine/gates.yaml`,
   `engine/review-loop.md`, `deliverables/manifest.yaml`. Also read `<FRAMEWORK>/../AGENTS.md`.
5. Begin `01-idea`.

---

## Step 2B — RESUME

A full run does not fit in one session. Resuming correctly is the most important thing
this skill does.

1. Read `<RUNS>/<slug>/state.yaml` in full — including `project.framework_path` and
   `project.run_dir`, which tell you where everything is without re-deriving it. It is the
   run's memory: you are continuing work, not starting fresh.
2. Check `run.completed_modules` and `run.failed_gates`.
3. Re-read the constitution and evidence policy. **Do not skip this** because a previous
   session read them — you did not, and the discipline degrades immediately without them.
4. Find the next module in `<FRAMEWORK>/engine/run-order.yaml` whose `depends_on` have all
   passed, and resume there.
5. If the last session ended mid-module, redo that module. A half-written module is worse
   than an unstarted one, because its outputs look complete.

Tell the operator where you are before working: *"Resuming `<slug>` at module 07. Modules
01–06 passed. Two open assumptions carried."*

---

## Step 3 — Work the modules

Follow the per-module loop in `AGENTS.md` exactly. Two additions that belong to session
management rather than to the method:

**Write to `<RUNS>/<slug>/state.yaml` before you run out of room.** Losing a module's outputs to an
exhausted context is the most common way a run is damaged. Write outputs and evidence as
you produce them, not at the end of the module.

**One module at a time.** Do not batch modules to move faster. Each has a gate, and a gate
you skipped to save time is the thing the framework exists to prevent.

**Announce each module** in one line as you start it, so the operator can follow the run:
*"Module 04 — problem validation. Ranking against module 03's jobs."*

---

## Step 4 — The three checkpoints are real stops

At each, present the finding and **stop**. Do not answer your own questions and continue.

**After `01-idea`** — you must have at least five clarifying questions. Ask them as a
numbered list, plainly, in the operator's language. Include at least one whose answer you
would rather not hear. Jurisdiction and payer are not optional; the run cannot proceed
without them.

**After `07-strategy`** — present the option comparison, your recommendation, and what
would change it. The MVP cut is a commercial commitment and it is the operator's to
confirm.

**Before delivery** — present the artifact set and the overall confidence.

Between checkpoints, if something is genuinely undecidable — a jurisdiction, a buyer, a
scope boundary — stop and ask. Record it in `state.open_questions` with `blocking: true`.
**Do not pick a plausible answer and proceed.**

---

## Step 5 — Finish

1. Fill every required artifact from `<FRAMEWORK>/deliverables/templates/` into
   `<RUNS>/<slug>/deliverables/`. Write
   `12-Build-Handoff.md` and `16-Engineering-Setup.md` last, and
   `00-Executive-Summary.md` last of all.
2. Remove every `«placeholder»`, `<!-- fill -->` and `<!-- ACCEPTANCE -->` block.
3. Set `run.confidence` to `high`, `medium` or `low`. Not `unknown`.
4. Run the validator:

   ```bash
   python3 <FRAMEWORK>/engine/validate-run.py <RUNS>/<slug>
   ```

5. **A non-zero exit means the run is not deliverable.** Fix what it reports. Do not
   report completion to the operator until it exits 0.

---

## What this framework is for, and what it is not

It exists to make research **auditable**, not to make it agreeable. The most valuable
output this run can produce is sometimes "do not build this" — the Executive Summary's
first acceptance criterion permits exactly that verdict, and a run that reaches it
honestly has saved the operator far more than one that reaches a plan.

Three habits carry more weight than everything else:

**Tag every claim.** `[verified: source]`, `[inferred: basis]`,
`[assumption: needs validation]`. An untagged claim is a defect. **Never smooth an
assumption into a fact** — this single failure destroys the framework's entire value,
because nothing downstream can detect it.

**A failed gate stops you.** Uncertainty about a gate is a fail, not a pass. Follow
`on_fail` and go back. Three failures on one module halts the run and escalates to the
operator.

**Skip `learn/` entirely.** It is human curriculum. Read `core/` for method, `knowledge/`
for concepts, `resources/` for worked examples and anti-examples.

**Never write inside `<FRAMEWORK>` or its repository.** The framework is read-only during a run. If you
believe the framework itself needs changing, say so and stop — that is the `/pios-author`
skill's job, not this one.

---

## Reporting status

When asked for status rather than work, read `<RUNS>/<slug>/state.yaml` and report:

- Which modules have passed, and which is next
- Overall confidence, and what would raise it
- Open assumptions, and which is load-bearing
- Any blocking open question, and who owns it
- Whether a shortfall was declared, and whether it has been carried

Then stop. A status request is not an instruction to continue the run.
