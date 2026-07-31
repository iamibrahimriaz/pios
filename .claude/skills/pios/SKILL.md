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

## The reply contract — end every message by telling the operator what to do next

**This applies to every reply you send during a run, without exception**, from the first
message to the last. A run is long, most of it is you working, and the operator cannot see
your state. If a reply does not end by saying what happens next, they have to guess whether
to wait, answer something, or type something — and the usual result is that the run stalls
with neither side knowing the other is waiting.

**Close every message with a short block that names exactly one of these three:**

| Situation | The closing block says |
| --- | --- |
| You need an answer before you can continue | The questions, numbered, in plain language — and **"Answer these and I'll continue."** Say which are blocking and which can be deferred |
| You want confirmation before committing to something | The decision, your recommendation, and **"Type `continue` to go ahead, or tell me what to change."** |
| You are mid-run and nothing is needed from them | What you just finished, what you are doing next, and **"Nothing needed from you — type `continue` and I'll keep going."** |

**Write it for the person, not for the framework.** No module numbers without a plain-English
gloss, no gate vocabulary, no internal field names. "I need to know who pays for this before
I can size the market" lands; "01-idea criterion 4 is unsatisfied" does not.

**Ask in the operator's language.** If they wrote to you in Bengali, Hindi, Urdu or anything
else, ask in that language. `state.project.language` records it. A precise question the
operator cannot read is a blocked run.

**Numbered questions, one idea each.** Never a paragraph containing four questions — the
operator will answer the first and the last. Number them so they can reply "1. yes, 2. no,
3. skip" and you can match the answers to the questions without ambiguity.

**Say what happens if they don't know.** Every blocking question gets a fallback sentence:
what you will assume if they say "I don't know", and what that assumption will cost. An
operator who cannot answer must never be stuck — but they must see the price of the default
before it is applied.

> **The test:** could the operator close this message and know, without re-reading it, whether
> the ball is in their court? If not, the message is not finished.

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
> `export PIOS_HOME="$HOME/Projects/pios"`
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
*"External mode. Framework at ~/Projects/pios. Writing to ./pios/."*

---

## Step 1 — Establish the mode before anything else

**Several runs live side by side.** One directory per idea, and they do not interact. An
existing run is not a reason to avoid starting a new one — it is only a reason never to
write into it.

```bash
ls -d <RUNS>/*/ 2>/dev/null && grep -h "raw_idea" <RUNS>/*/state.yaml 2>/dev/null
```

**The mode follows what the operator asked for, not how many runs exist:**

| What the operator did | Mode |
| --- | --- |
| Described an idea that does not match any existing run's `raw_idea` | **NEW RUN** — a new slug, a new directory, alongside whatever else is there |
| Named an existing run, or said "continue" / "resume" with exactly one run present | **RESUME** that run |
| Asked "what stage", "status", "where are we" | **STATUS** — report and stop |
| Said "continue" with **more than one** run present | **Ask which.** List them by slug with a one-line summary of each and stop |
| Described an idea that is arguably a restatement of an existing run | **Ask.** Show the existing run's `raw_idea` verbatim and ask whether this is the same project or a new one |

**A second run is a normal thing to start.** Nothing is shared between runs except the
framework itself, so a new idea costs an existing run nothing.

**What is forbidden is writing into the wrong run.** Never overwrite an existing
`state.yaml`, never reuse a slug that already exists, and never rewrite
`state.project.raw_idea` under any circumstances — including on the run you are creating,
once it is written.

**When in doubt, ask before creating a directory.** A wrongly-created run directory is
cheap to delete; a wrongly-*resumed* run silently mixes two ideas' evidence into one state
file, and nothing downstream can detect it.

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

**Record friction the moment it happens.** When the framework gets in your way — a gate
criterion you cannot evaluate as written, a template section with no home for something real,
a question you had to ask the operator twice, an instruction that turned out to be wrong —
append it to `state.friction_log` before moving on. Mark it `operator_visible: true` if they
hit it rather than you.

**Do not stop to discuss it, and do not fix the framework.** The framework is read-only
during a run; `/pios-author` is where changes are made, afterwards and deliberately. Note it
and keep going.

> **Written at the end, this list is worthless.** By then every rough edge has been worked
> around, and a workaround is indistinguishable in memory from something that went smoothly.
> The friction that is worth fixing is exactly the friction you stopped noticing.

---

## Step 4 — The three checkpoints are real stops

At each, present the finding and **stop**. Do not answer your own questions and continue.

**After `01-idea`** — you must have at least five clarifying questions. Ask them as a
numbered list, plainly, in the operator's language. Include at least one whose answer you
would rather not hear.

**Three answers are not optional and the run cannot proceed without them:** the
**jurisdiction**, the **payer**, and the **delivery surface** — is this a website, a phone
app, both, a desktop program, or something with no interface at all, and if more than one,
which comes first. Ask the surface question in those words. It is not a technology question
and it does not wait for module 09: market sizing, user context, where competitors are
found, the billing rail, whether offline is a requirement and the entire acquisition channel
are all downstream of it, and none of them re-examines it later.

End the message with **"Answer these and I'll start the research."**

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

### Then send the completion message

**The research is not finished when the files are written. It is finished when the operator
knows what they have and what to do with it.** Send one message, in their language,
containing exactly these five parts and nothing else:

**1 — The verdict, in one line.** Build it, build it with changes, or do not build it. Then
the confidence level and, in one sentence, what would raise it.

**2 — What was produced.** The artifact count and where the files are, as an absolute path
the operator can paste into a file manager. Name the two that matter — the build handoff and
the engineering setup — and say in one line each what they are for.

**3 — The three things they must not miss.** The failed gate, the unresolved decision, the
assumption the whole plan rests on. Whatever the run's real weak points are. Do not soften
them and do not bury them under the good news.

**4 — The instruction to start building.** A block the operator can copy and hand to a
developer or to a coding agent with no other context, naming absolute paths:

> Build the product specified in `<RUNS>/<slug>/deliverables/12-Build-Handoff.md`.
> Read that file first and completely — it is self-contained and states what to build, in
> what order, and what "correct" means. Set the project up using `16-Engineering-Setup.md`
> in the same directory. The data model, API contract and acceptance criteria are in the
> sibling artifacts it references.
>
> **Do not start anything listed under "Blocked Work" in §12 of the handoff.** Those items
> are waiting on a decision or an answer that no amount of engineering produces.

**If the run reached "do not build", the block above is replaced by what to do instead** —
the cheapest test that would change the verdict, and what it costs. Never hand over a build
instruction for something the research says should not be built.

**5 — The closing line.** What you need from them now, per the reply contract: the decisions
still open, and **"Tell me which of these you want to resolve and I'll pick it up."**

**If `state.friction_log` is not empty, add one short paragraph before the closing line** —
not a section, a paragraph. Name the two or three places the framework itself got in the way
during this run, in plain language, and say that `/pios-author` is where they get fixed. The
operator does not have to act on it and should not be asked to; they are being told the list
exists so it is not lost.

**Then ask the one question they can answer and you cannot:** *"Was there anything about how
this run went that annoyed you?"* Your own friction log records where the framework blocked
**you**. It cannot see where it was confusing, slow or unclear to **them** — and that is the
feedback that has historically changed this framework most.

**Say plainly whether they can start building today.** An operator holding fifteen documents
cannot tell whether the plan is ready or whether something must be answered first. If a
blocker stands between them and the first line of code, that sentence is the most important
one in the message, and it goes near the top rather than in a table at the end.

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
